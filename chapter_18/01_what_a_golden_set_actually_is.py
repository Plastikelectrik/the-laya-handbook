# The LAYA Handbook — Chapter 18: Golden-Set Testing Discipline
# Section: What a Golden Set Actually Is

GOLDEN_SET = [
    {
        "state": {"subject": "Cancel my plan", "body": "Charged twice, cancel now."},
        "true_department": "retention",
        "true_urgency": 2,
        "true_churn_risk": True,
    },
    {
        "state": {"subject": "Export broken", "body": "Export does nothing when clicked."},
        "true_department": "technical",
        "true_urgency": 1,
        "true_churn_risk": False,
    },
    # ... fifty to several hundred more, covering real edge cases ...
]
