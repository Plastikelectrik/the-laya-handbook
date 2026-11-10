# The LAYA Handbook — Chapter 19: Calibration Drift: Detecting When Confidence Stops Meaning What It Used To
# Section: Setting an Alert Threshold

LAUNCH_ECE = 0.04
ECE_ALERT_MARGIN = 0.03
ECE_ALERT_THRESHOLD = LAUNCH_ECE + ECE_ALERT_MARGIN

def check_drift(predictions_with_outcomes):
    current = weekly_ece(predictions_with_outcomes)
    if current > ECE_ALERT_THRESHOLD:
        alert(f"Calibration drift: ECE {current:.3f} exceeds threshold {ECE_ALERT_THRESHOLD:.3f}")
    return current
