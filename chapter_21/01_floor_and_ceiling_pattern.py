# The LAYA Handbook — Chapter 21: Multi-Tenant and Team Threshold Governance
# Section: The Floor-and-Ceiling Pattern

ORG_WIDE_FLOOR = {
    "department": 0.70,
    "churn_risk": 0.70,
}

TEAM_THRESHOLDS = {
    "billing": {"department": 0.75},
    "trust_and_safety": {"churn_risk": 0.92},
}

def effective_threshold(team, question_name):
    floor = ORG_WIDE_FLOOR[question_name]
    team_value = TEAM_THRESHOLDS.get(team, {}).get(question_name, floor)
    return max(floor, team_value)   # a team can only raise the bar, never lower it
