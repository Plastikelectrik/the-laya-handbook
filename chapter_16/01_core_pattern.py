# The LAYA Handbook — Chapter 16: Confidence Gating and the Escalation Pattern
# Section: The Core Pattern

DEPARTMENT_THRESHOLD = 0.82   # calibrated against a golden set — Chapter 18

def route_ticket(state):
    result = agent.predict(state, TICKET_QUESTIONS)
    dept = result["answers"]["department"]
    if (dept["answer_confidence"]
            >= DEPARTMENT_THRESHOLD):
        auto_route(dept["choice"])
    else:
        escalate_to_human(state, result)
