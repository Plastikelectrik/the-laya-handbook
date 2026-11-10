# The LAYA Handbook — Chapter 16: Confidence Gating and the Escalation Pattern
# Section: Gating on More Than the Top Confidence

def margin(distribution):
    values = sorted(distribution.values(), reverse=True)
    return values[0] - values[1] if len(values) > 1 else values[0]

def route_ticket(state):
    result = agent.predict(state, TICKET_QUESTIONS)
    dept = result["answers"]["department"]
    if dept["answer_confidence"] >= DEPARTMENT_THRESHOLD and margin(dept["probabilities"]) >= 0.3:
        auto_route(dept["choice"])
    else:
        escalate_to_human(state, result)
