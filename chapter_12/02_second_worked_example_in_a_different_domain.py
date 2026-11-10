# The LAYA Handbook — Chapter 12: Writing Criteria That Produce Calibrated Answers, and a First End-to-End Example
# Section: A Second Worked Example, in a Different Domain

MODERATION_QUESTIONS = {
    "policy_category": {
        "type": "choice",
        "instructions": "Which policy category, if any, does this comment violate?",
        "criteria": {
            "none": "no apparent policy violation",
            "harassment": "targeted insults or threats directed at a specific person",
            "spam": "commercial promotion or repetitive posting, per Chapter 6's own example",
            "other": "a clear violation that doesn't fit the categories above",
        },
    },
    "severity": {
        "type": "score",
        "instructions": "If this is a violation, how severe is it?",
        "criteria": ["not a violation", "minor", "moderate", "severe"],
    },
}

def moderate_comment(raw_comment):
    state = {"text": raw_comment["text"]}       # build state
    result = agent.predict(state, MODERATION_QUESTIONS)   # ask questions
    category = result["answers"]["policy_category"]
    severity = result["answers"]["severity"]
    needs_review = category["choice"] != "none" and category["answer_confidence"] >= 0.7   # decide
    return {"category": category["choice"], "severity_score": severity["score"], "needs_review": needs_review}
