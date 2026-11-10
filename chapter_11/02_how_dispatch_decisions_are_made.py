# The LAYA Handbook — Chapter 11: The Router: Automatic Model Selection and Multilingual Text
# Section: How Dispatch Decisions Are Made

decision = router.route({"body": "Ich habe eine Frage zu meiner Rechnung."}, questions)
print(decision.model)    # 'multilingual'
print(decision.reason)   # "Latin script but language looks like 'de', not English"
