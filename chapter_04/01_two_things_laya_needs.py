# The LAYA Handbook — Chapter 4: Your First Prediction: agent.predict() End to End
# Section: The Two Things Laya Needs

import laya

agent = laya.load("convaiinnovations/laya")

state = {
    "subject": "Cancel my subscription",
    "body": "I've been charged twice this month and support hasn't "
            "responded in three days. I want to cancel.",
}

questions = {
    "department": {
        "type": "choice",
        "instructions": "Which department should handle this ticket?",
        "criteria": {
            "billing": "invoices, payments, refunds, charges",
            "technical": "bugs, outages, system errors",
            "retention": "cancellation requests, churn risk",
        },
    },
}

result = agent.predict(state, questions)
