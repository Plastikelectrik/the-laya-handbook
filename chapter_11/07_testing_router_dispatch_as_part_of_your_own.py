# The LAYA Handbook — Chapter 11: The Router: Automatic Model Selection and Multilingual Text
# Section: Testing Router Dispatch as Part of Your Own Test Suite

ROUTING_TEST_CASES = [
    ({"body": "Please refund my order."}, "english"),
    ({"body": "मुझसे दो बार शुल्क लिया गया"}, "multilingual"),
    ({"body": "Ich habe eine Frage."}, "multilingual"),
]

def test_router_dispatch():
    for state, expected_model in ROUTING_TEST_CASES:
        decision = router.route(state, {})
        assert decision.model == expected_model, decision.reason
