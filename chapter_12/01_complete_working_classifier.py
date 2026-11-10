# The LAYA Handbook — Chapter 12: Writing Criteria That Produce Calibrated Answers, and a First End-to-End Example
# Section: A Complete, Working Classifier

import laya

agent = laya.load("convaiinnovations/laya")

DEPARTMENT_THRESHOLD = 0.75   # a placeholder — Chapter 18 covers calibrating
                              # a real threshold against a labeled golden set

TICKET_QUESTIONS = {
    "department": {
        "type": "choice",
        "instructions": "Which department should handle this ticket?",
        "criteria": {
            "billing": "invoices, payments, refunds, charges",
            "technical": "bugs, outages, system errors",
            "retention": "cancellation requests, churn risk",
        },
    },
    "urgency": {
        "type": "score",
        "instructions": "How urgent is this ticket?",
        "criteria": ["not urgent", "normal", "high", "critical"],
    },
    "churn_risk": {
        "type": "noul",
        "instructions": "Does the customer express intent to cancel?",
    },
}


def build_state(raw_ticket):
    """Translate a raw ticket payload into the state object Laya reads.
    Kept as its own function, per Chapter 5, so it can be tested on its
    own — this is the piece most worth unit-testing in a real system."""
    return {
        "subject": raw_ticket["subject"],
        "body": raw_ticket["body"],
    }


def triage(raw_ticket):
    state = build_state(raw_ticket)
    result = agent.predict(state, TICKET_QUESTIONS)
    dept = result["answers"]["department"]
    urgency = result["answers"]["urgency"]
    churn = result["answers"]["churn_risk"]

    return {
        "department": dept["choice"] if dept["answer_confidence"] >= DEPARTMENT_THRESHOLD else None,
        "department_confidence":
            dept["answer_confidence"],
        "urgency_score": urgency["score"],
        "churn_risk": churn["noul"] >= 0.7,
        "needs_human_review": dept["answer_confidence"] < DEPARTMENT_THRESHOLD,
    }


if __name__ == "__main__":
    sample = {
        "subject": "Cancel my subscription",
        "body": "Charged twice, no response in three days. Cancel it.",
    }
    print(triage(sample))
