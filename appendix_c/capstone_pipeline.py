# The LAYA Handbook — Appendix C: Capstone Full Source Listing
# The complete ticket-routing pipeline from Chapters 27-28, in one file.


# ----------------------------------------------------------------------
# Imports, Constants, and Question Set
# ----------------------------------------------------------------------

import hashlib, json, random, time
from laya import Router

TICKET_QUESTIONS = {
    "department": {
        "type": "choice",
        "instructions": "Which department should handle this ticket?",
        "criteria": {
            "billing": "invoices, payments, refunds, charges, pricing questions",
            "technical": "bugs, outages, system errors, broken features",
            "retention": "cancellation requests, downgrade requests, churn signals",
            "general": "account questions, feature requests, anything not above",
        },
    },
    "urgency": {
        "type": "score",
        "instructions": "How urgent is this ticket, considering both stated "
                        "urgency and the real business impact described?",
        "criteria": ["not urgent", "normal", "high", "critical"],
    },
    "churn_risk": {
        "type": "noul",
        "instructions": "Does the customer express real intent to cancel, "
                        "downgrade, or switch to a competitor — not just "
                        "frustration with no stated intent to leave?",
    },
}

DEPARTMENT_THRESHOLD = 0.82
CHURN_THRESHOLD = 0.75
CHECKPOINT_VERSION = "convaiinnovations/laya@v1"
CANDIDATE_ROLLOUT_PERCENT = 5


# ----------------------------------------------------------------------
# State Building
# ----------------------------------------------------------------------

def build_state(raw_ticket):
    return {
        "subject": raw_ticket["subject"],
        "body": raw_ticket["body"],
    }


# ----------------------------------------------------------------------
# Health Tracking and Degraded-Mode Fallback
# ----------------------------------------------------------------------

class InferenceHealth:
    def __init__(self, failure_window_s=60, failure_threshold=5):
        self.failure_window_s = failure_window_s
        self.failure_threshold = failure_threshold
        self._failures = []

    def record_failure(self):
        now = time.time()
        self._failures = [t for t in self._failures if now - t < self.failure_window_s]
        self._failures.append(now)

    def is_degraded(self):
        now = time.time()
        self._failures = [t for t in self._failures if now - t < self.failure_window_s]
        return len(self._failures) >= self.failure_threshold

health = InferenceHealth()

def fallback_department(state):
    body = state.get("body", "").lower()
    if "cancel" in body or "refund" in body:
        return "retention"
    if "error" in body or "broken" in body:
        return "technical"
    return "general"


# ----------------------------------------------------------------------
# Structured Logging
# ----------------------------------------------------------------------

def log_prediction(state, questions, result, routing_info, checkpoint_version):
    state_hash = hashlib.sha256(json.dumps(state, sort_keys=True).encode()).hexdigest()
    entry = {
        "timestamp": time.time(),
        "state_hash": state_hash,
        "questions_asked": list(questions.keys()),
        "checkpoint_version": checkpoint_version,
        "routing_model": routing_info.get("model") if routing_info else None,
    }
    if result is not None:
        entry["answers"] = {
            name: {k: v for k, v in answer.items() if k != "probabilities"}
            for name, answer in result["answers"].items()
        }
    audit_log.write(entry)


# ----------------------------------------------------------------------
# Startup and Readiness
# ----------------------------------------------------------------------

router = None

def startup():
    global router
    router = Router(preload=True, max_loaded=2)

def readiness_check():
    return router is not None


# ----------------------------------------------------------------------
# The Complete Routing Function
# ----------------------------------------------------------------------

def route_ticket(raw_ticket):
    state = build_state(raw_ticket)

    if health.is_degraded():
        department = fallback_department(state)
        log_prediction(state, TICKET_QUESTIONS, None, None, "fallback")
        return {"department": department, "needs_human_review": True, "mode": "degraded"}

    try:
        result = router.predict(state, TICKET_QUESTIONS)
    except InferenceError:
        health.record_failure()
        return route_ticket(raw_ticket)

    dept = result["answers"]["department"]
    urgency = result["answers"]["urgency"]
    churn = result["answers"]["churn_risk"]

    log_prediction(state, TICKET_QUESTIONS, result, result.get("routing"), CHECKPOINT_VERSION)

    if churn["noul"] >= CHURN_THRESHOLD:
        log_churn_risk_for_retention_review(state, churn["noul"])

    confident = dept["answer_confidence"] >= effective_threshold("default", "department")
    return {
        "department": dept["choice"] if confident else None,
        "department_confidence":
            dept["answer_confidence"],
        "urgency_score": urgency["score"],
        "needs_human_review": not confident,
        "mode": "normal",
    }


# ----------------------------------------------------------------------
# Golden-Set Gate Before Deployment
# ----------------------------------------------------------------------

metrics = evaluate_against_golden_set(TICKET_QUESTIONS, CAPSTONE_GOLDEN_SET, router)
assert metrics["accuracy"] >= MINIMUM_ACCEPTABLE_ACCURACY
assert metrics["ece"] <= MAXIMUM_ACCEPTABLE_ECE


# ----------------------------------------------------------------------
# Staged Rollout Wrapper
# ----------------------------------------------------------------------

def route_ticket_with_rollout(raw_ticket):
    use_candidate = random.random() < (CANDIDATE_ROLLOUT_PERCENT / 100)
    questions = TICKET_QUESTIONS_CANDIDATE if use_candidate else TICKET_QUESTIONS
    result = route_ticket(raw_ticket)
    result["version"] = "candidate" if use_candidate else "current"
    return result
