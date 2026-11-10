# The LAYA Handbook — Chapter 7: Score: Ordinal Judgments on a Rubric
# Section: Anatomy of a Score Question

questions = {
    "urgency": {
        "type": "score",
        "instructions": "How urgent is this support ticket?",
        "criteria": [
            "not urgent, can wait days",
            "normal, respond within a business day",
            "high, respond within hours",
            "critical, active outage or data loss",
        ],
    },
}

result = agent.predict(state, questions)
answer = result["answers"]["urgency"]

answer["score"]          # 2.08  — a continuous expected value, not just 0/1/2/3
answer["answer_confidence"]  # 0.55
answer["probabilities"]  # {'0': 0.03, '1': 0.14,
                         #  '2': 0.55, '3': 0.28}
