# The LAYA Handbook — Chapter 16: Confidence Gating and the Escalation Pattern
# Section: Threshold Asymmetry Across Error Types

PER_OPTION_THRESHOLD = {
    "billing": 0.75,
    "technical": 0.75,
    "retention": 0.75,
    "security": 0.95,   # a costlier mistake deserves a stricter bar
}

def route_ticket(state):
    result = agent.predict(state, TICKET_QUESTIONS)
    dept = result["answers"]["department"]
    required = PER_OPTION_THRESHOLD[dept["choice"]]
    if dept["answer_confidence"] >= required:
        auto_route(dept["choice"])
    else:
        escalate_to_human(state, result)
