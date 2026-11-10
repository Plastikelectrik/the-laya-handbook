# The LAYA Handbook — Chapter 28: Capstone Part 2: Building, Testing, and Deploying the Pipeline
# Section: The Complete Routing Function

# CHECKPOINT_VERSION: version string of the
# deployed checkpoint (defined in Appendix C)
def route_ticket(raw_ticket):
    state = build_state(raw_ticket)

    if health.is_degraded():
        department = fallback_department(state)
        log_prediction(state, TICKET_QUESTIONS, None, None, "fallback")   # Chapter 26
        return {"department": department, "needs_human_review": True, "mode": "degraded"}

    try:
        result = router.predict(state, TICKET_QUESTIONS)
    except InferenceError:
        health.record_failure()
        return route_ticket(raw_ticket)   # retry once, now under degraded-mode logic

    dept = result["answers"]["department"]
    urgency = result["answers"]["urgency"]
    churn = result["answers"]["churn_risk"]

    log_prediction(state, TICKET_QUESTIONS, result, result.get("routing"), CHECKPOINT_VERSION)

    if churn["noul"] >= CHURN_THRESHOLD:
        log_churn_risk_for_retention_review(state, churn["noul"])   # parallel, not a gate

    confident = dept["answer_confidence"] >= effective_threshold("default", "department")   # Chapter 21
    return {
        "department": dept["choice"] if confident else None,
        "department_confidence":
            dept["answer_confidence"],
        "urgency_score": urgency["score"],
        "needs_human_review": not confident,
        "mode": "normal",
    }
