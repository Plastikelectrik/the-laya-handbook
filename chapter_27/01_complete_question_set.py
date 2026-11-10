# The LAYA Handbook — Chapter 27: Capstone Part 1: Designing the Ticket-Routing Pipeline
# Section: The Complete Question Set

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

DEPARTMENT_THRESHOLD = 0.82   # org floor, teams may raise — Chapter 21
CHURN_THRESHOLD = 0.75        # owned by the retention team — Chapter 21
