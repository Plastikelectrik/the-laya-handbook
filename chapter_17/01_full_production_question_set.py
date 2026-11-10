# The LAYA Handbook — Chapter 17: Designing Production Criteria: The Department, Urgency, and Churn Model
# Section: The Full Production Question Set

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
        "criteria": [
            "not urgent, can wait several business days",
            "normal, respond within one business day",
            "high, respond within a few hours",
            "critical, active outage, data loss, or security exposure",
        ],
    },
    "churn_risk": {
        "type": "noul",
        "instructions": "Does the customer express real intent to cancel, "
                        "downgrade, or switch to a competitor — not just "
                        "frustration with no stated intent to leave?",
    },
}
