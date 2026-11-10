# The LAYA Handbook — Chapter 7: Score: Ordinal Judgments on a Rubric
# Section: A Worked Example: Review Helpfulness

state = {
    "review_text": "Bought this for hiking. Great grip in wet conditions, "
                    "runs about half a size small, and the laces are "
                    "noticeably thinner than the previous model I owned.",
    "star_rating": 4,
}

questions = {
    "helpfulness": {
        "type": "score",
        "instructions": "How helpful is this review to a prospective buyer?",
        "criteria": [
            "no specific detail, could apply to any product",
            "one specific, useful detail",
            "several specific details covering different aspects",
            "comprehensive: fit, performance, and comparison to alternatives",
        ],
    },
}
