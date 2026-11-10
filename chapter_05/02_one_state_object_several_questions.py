# The LAYA Handbook — Chapter 5: The State Object: Giving Laya Something to Reason About
# Section: One State Object, Several Questions

state = {
    "subject": "Cancel my subscription",
    "body": "Charged twice, no response in three days. Cancel it.",
}

# The SAME state object, reused across three separate calls here —
# Chapter 9 shows asking all three in one call instead.
# *_QUESTION: question dicts as in Chapters 6-8
dept = agent.predict(state, {"department": DEPARTMENT_QUESTION})
urgency = agent.predict(state, {"urgency": URGENCY_QUESTION})
churn = agent.predict(state, {"churn_risk": CHURN_QUESTION})
