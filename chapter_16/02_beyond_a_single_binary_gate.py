# The LAYA Handbook — Chapter 16: Confidence Gating and the Escalation Pattern
# Section: Beyond a Single Binary Gate

def route_ticket(state):
    result = agent.predict(state, TICKET_QUESTIONS)
    dept = result["answers"]["department"]
    conf = dept["answer_confidence"]

    if conf >= 0.90:
        auto_route(dept["choice"])
    elif conf >= 0.70:
        expedited_review(state, result)   # likely correct, worth a quick human glance
    else:
        standard_review(state, result)    # genuinely uncertain, full triage needed
