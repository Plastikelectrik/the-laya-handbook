# The LAYA Handbook — Chapter 31: Laya Alongside LLMs: Where System 1 Fits in a Larger System
# Section: The Orchestration Pattern

def triage_with_llm_escalation(raw_ticket):
    state = build_state(raw_ticket)
    result = router.predict(state, TICKET_QUESTIONS)
    dept = result["answers"]["department"]

    if (dept["answer_confidence"]
            >= DEPARTMENT_THRESHOLD):
        return {"department": dept["choice"], "handled_by": "laya"}

    # Genuinely ambiguous: Laya has correctly told us it is uncertain.
    # An LLM, given the same state object, can reason through the
    # ambiguity in a way a fixed, enumerable answer set cannot capture —
    # or a human can, if the stakes warrant a person rather than a model.
    llm_answer = llm_classify_with_reasoning(state, TICKET_QUESTIONS["department"])
    return {"department": llm_answer, "handled_by": "llm", "laya_confidence": dept["answer_confidence"]}
