# The LAYA Handbook — Chapter 21: Multi-Tenant and Team Threshold Governance
# Section: Sunsetting a Team’s Custom Threshold

TEAM_THRESHOLDS = {
    "trust_and_safety": {
        "churn_risk": {"value": 0.92, "owner": "t_safety_lead", "review_by": "2025-06-01"},
    },
}

def effective_threshold(team, question_name, today):
    floor = ORG_WIDE_FLOOR[question_name]
    entry = TEAM_THRESHOLDS.get(team, {}).get(question_name)
    if entry is None or today > entry["review_by"]:
        return floor   # expired or never set — fail safe to the org floor
    return max(floor, entry["value"])
