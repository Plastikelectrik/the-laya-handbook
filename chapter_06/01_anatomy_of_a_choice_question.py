# The LAYA Handbook — Chapter 6: Choice: Calibrated Classification in One Forward Pass
# Section: Anatomy of a Choice Question

questions = {
    "severity": {
        "type": "choice",
        "instructions": "Classify the severity of this bug report.",
        "criteria": {
            "critical": "production down, data loss, security exposure",
            "major": "core feature broken, no workaround",
            "minor": "non-core feature broken, workaround exists",
            "cosmetic": "visual or wording issue only",
        },
    },
}

result = agent.predict(state, questions)
answer = result["answers"]["severity"]

answer["choice"]         # 'major'  (the winning option)
answer["answer_confidence"]  # 0.87  (the winning option's probability)
answer["probabilities"]  # {'critical': 0.02, 'major': 0.87,
                          #  'minor': 0.09, 'cosmetic': 0.02}
