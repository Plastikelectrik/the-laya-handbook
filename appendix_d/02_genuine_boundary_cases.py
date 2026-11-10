# The LAYA Handbook — Appendix D: Golden-Set Example Bank
# Section: Genuine Boundary Cases

GENUINE_BOUNDARY_CASES = [
    {"state": {"subject": "Billing error caused by a bug", "body": "A software bug double-charged my card — please fix "
                                                            "the bug and refund the extra charge."},
     "true_department": "technical",
     "note": "root cause is the bug; the refund is a downstream consequence, not the primary issue"},
    {"state": {"subject": "Thinking about leaving", "body": "Your pricing changed and I'm reconsidering whether "
                                                          "this is worth it, but haven't decided yet."},
     "true_churn_risk": False,
     "note": "ambivalence, not stated intent — expect a moderate noul (about 0.55), not a high one"},
]
