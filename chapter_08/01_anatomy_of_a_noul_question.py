# The LAYA Handbook — Chapter 8: Noul: Calibrated Yes/No Questions
# Section: Anatomy of a Noul Question

questions = {
    "churn_risk": {
        "type": "noul",
        "instructions": "Does the customer express intent to cancel or leave?",
    },
}

result = agent.predict(state, questions)
answer = result["answers"]["churn_risk"]

answer["noul"]   # 0.83  — calibrated probability that the answer is TRUE
