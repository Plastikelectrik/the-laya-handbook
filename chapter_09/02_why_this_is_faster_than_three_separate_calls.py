# The LAYA Handbook — Chapter 9: Asking Several Questions at Once: Shared Encoding, Independent Answers
# Section: Why This Is Faster Than Three Separate Calls

# Slower: three separate forward passes, roughly 33ms each = ~99ms total
dept = agent.predict(state, {"department": DEPARTMENT_QUESTION})
urg = agent.predict(state, {"urgency": URGENCY_QUESTION})
churn = agent.predict(state, {"churn_risk": CHURN_QUESTION})

# Faster: one shared encoding, three independent answers —
# roughly 20-25ms total for the same three answers
result = agent.predict(state, {
    "department": DEPARTMENT_QUESTION,
    "urgency": URGENCY_QUESTION,
    "churn_risk": CHURN_QUESTION,
})
