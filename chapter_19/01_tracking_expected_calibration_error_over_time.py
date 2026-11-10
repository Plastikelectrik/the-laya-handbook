# The LAYA Handbook — Chapter 19: Calibration Drift: Detecting When Confidence Stops Meaning What It Used To
# Section: Tracking Expected Calibration Error Over Time

def weekly_ece(predictions_with_outcomes):
    """predictions_with_outcomes: list of (confidence, was_correct) tuples
    gathered from production predictions whose real outcome later became known."""
    buckets = defaultdict(list)
    for confidence, was_correct in predictions_with_outcomes:
        buckets[round(confidence, 1)].append(was_correct)

    ece = 0.0
    total = len(predictions_with_outcomes)
    for bucket, outcomes in buckets.items():
        observed = sum(outcomes) / len(outcomes)
        ece += (len(outcomes) / total) * abs(bucket - observed)
    return ece
