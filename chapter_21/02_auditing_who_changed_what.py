# The LAYA Handbook — Chapter 21: Multi-Tenant and Team Threshold Governance
# Section: Auditing Who Changed What

def set_team_threshold(team, question_name, new_value, changed_by, reason):
    old_value = TEAM_THRESHOLDS.get(team, {}).get(question_name)
    if new_value < ORG_WIDE_FLOOR[question_name]:
        raise ValueError("cannot set a team threshold below the org-wide floor")
    TEAM_THRESHOLDS.setdefault(team, {})[question_name] = new_value
    audit_log.record({
        "event": "threshold_change",
        "team": team,
        "question": question_name,
        "old_value": old_value,
        "new_value": new_value,
        "changed_by": changed_by,
        "reason": reason,
    })
