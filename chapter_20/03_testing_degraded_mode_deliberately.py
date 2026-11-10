# The LAYA Handbook — Chapter 20: Degraded-Mode Design: What Happens When Inference Fails
# Section: Testing Degraded Mode Deliberately

def run_degraded_mode_drill(health, sample_tickets):
    original_check = health.is_degraded
    health.is_degraded = lambda: True   # force degraded mode for this drill
    try:
        results = [route_ticket_with_fallback(t, health) for t in sample_tickets]
        review_results_for_reasonableness(results)   # a human checks these, not just "no exception"
    finally:
        health.is_degraded = original_check
