# The LAYA Handbook — Chapter 28: Capstone Part 2: Building, Testing, and Deploying the Pipeline
# Section: Degraded-Mode Fallback, Scoped to This Pipeline

health = InferenceHealth(failure_window_s=60, failure_threshold=5)   # Chapter 20

def fallback_department(state):
    body = state.get("body", "").lower()
    if "cancel" in body or "refund" in body:
        return "retention"
    if "error" in body or "broken" in body:
        return "technical"
    return "general"
