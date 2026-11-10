# The LAYA Handbook — Chapter 9: Asking Several Questions at Once: Shared Encoding, Independent Answers
# Section: Building the Questions Dict Programmatically

def make_urgency_question(extra_context=""):
    base_instructions = "How urgent is this ticket?"
    return {
        "type": "score",
        "instructions": f"{base_instructions} {extra_context}".strip(),
        "criteria": ["not urgent", "normal", "high", "critical"],
    }

questions = {
    "department": DEPARTMENT_QUESTION,
    "urgency": make_urgency_question("Consider this is an enterprise account."),
    "churn_risk": CHURN_QUESTION,
}
