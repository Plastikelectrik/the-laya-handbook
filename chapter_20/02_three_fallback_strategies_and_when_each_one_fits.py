# The LAYA Handbook — Chapter 20: Degraded-Mode Design: What Happens When Inference Fails
# Section: Three Fallback Strategies, and When Each One Fits

def route_ticket_with_fallback(state, health):
    if not health.is_degraded():
        try:
            result = router.predict(state, TICKET_QUESTIONS)
            return result["answers"]["department"]["choice"]
        except InferenceError:
            health.record_failure()
            # fall through to the degraded-mode strategy below

    # Degraded mode: a rules fallback for department routing specifically —
    # crude relative to Laya, but far better than failing the request outright.
    body = state.get("body", "").lower()
    if "cancel" in body or "refund" in body:
        return "retention"
    if "error" in body or "broken" in body:
        return "technical"
    return "general"
