# The LAYA Handbook — Chapter 14: Production Architecture and the Router(preload=True) Pattern
# Section: The Core Pattern

# module-level, imported once per process — NOT inside a request handler
from laya import Router

router = Router(preload=True, max_loaded=2)


def handle_request(raw_ticket):
    """Called once per incoming request. Reuses the module-level router."""
    state = build_state(raw_ticket)
    result = router.predict(state, TICKET_QUESTIONS)
    return result
