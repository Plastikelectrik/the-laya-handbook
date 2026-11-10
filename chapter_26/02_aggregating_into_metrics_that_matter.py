# The LAYA Handbook — Chapter 26: Observability: Logging, Auditing, and Dashboards for Decision Systems
# Section: Aggregating Into Metrics That Matter

def daily_metrics(log_entries_for_day):
    total = len(log_entries_for_day)
    escalated = sum(
        1 for e in log_entries_for_day
        if e["answers"].get("department", {}).get("answer_confidence", 1.0) < DEPARTMENT_THRESHOLD
    )
    return {
        "total_predictions": total,
        "escalation_rate": escalated / total if total else 0.0,
    }
