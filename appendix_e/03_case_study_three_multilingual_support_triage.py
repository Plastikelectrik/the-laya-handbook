# The LAYA Handbook — Appendix E: Worked Case Studies
# Section: Case Study Three: Multilingual Support Triage

router = Router(preload=True, max_loaded=4)   # one checkpoint per supported language

def route_multilingual_ticket(raw_ticket):
    state = build_state(raw_ticket)
    result = router.predict(state, TICKET_QUESTIONS_BY_LANGUAGE[detect_or_declared_language(raw_ticket)])
    return result
