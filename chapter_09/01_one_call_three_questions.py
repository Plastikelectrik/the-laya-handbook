# The LAYA Handbook — Chapter 9: Asking Several Questions at Once: Shared Encoding, Independent Answers
# Section: One Call, Three Questions

state = {
    "from": "user@acme.com",
    "subject": "Cancel my subscription — this is unacceptable",
    "body": "I've been overcharged twice now and support hasn't "
            "responded in three days. I want to cancel.",
}

questions = {
    "department": {
        "type": "choice",
        "instructions": "Which department should handle this?",
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

result = agent.predict(state, questions)
print(result["answers"]["department"]["choice"])     # 'retention'
print(result["answers"]["urgency"]["score"])          # 2.6
print(result["answers"]["churn_risk"]["noul"])        # 0.91
