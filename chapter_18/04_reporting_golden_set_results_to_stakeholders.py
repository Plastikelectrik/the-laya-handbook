# The LAYA Handbook — Chapter 18: Golden-Set Testing Discipline
# Section: Reporting Golden-Set Results to Stakeholders

def summarize_for_stakeholders(current_metrics, candidate_metrics, question_name):
    acc_delta = candidate_metrics["accuracy"] - current_metrics["accuracy"]
    ece_delta = candidate_metrics["ece"] - current_metrics["ece"]
    return (
        f"{question_name}: accuracy change {acc_delta:+.1%}, "
        f"calibration error change {ece_delta:+.3f} "
        f"(n={candidate_metrics['n']} golden-set examples)"
    )
