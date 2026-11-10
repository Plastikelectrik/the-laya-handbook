# The LAYA Handbook — Appendix D: Golden-Set Example Bank
# Section: Churn-Risk Edge Cases: Frustration Without Stated Intent

CHURN_RISK_EDGE_CASES_FRUSTRATION_WITHOUT_STATED_INTENT = [
    {"state": {"subject": "Frustrated", "body": "This is the third time this feature has been broken this month, "
                                                "very annoying."},
     "true_churn_risk": False,
     "note": "genuine frustration, no stated intent to leave — should NOT score as high churn risk (noul about 0.30)"},
    {"state": {"subject": "Done with this", "body": "This is the third time this month and I'm actively looking at "
                                                     "your competitor's plan now."},
     "true_churn_risk": True,
     "note": "same frustration, now with explicit stated intent — should score as high churn risk (noul about 0.88)"},
]
