# The LAYA Handbook — Chapter 15: Batched Prediction at Scale
# Section: From One State Object to Many

states = [
    {"subject": "Cancel my subscription", "body": "Charged twice, cancel it."},
    {"subject": "Export broken", "body": "Export button does nothing."},
    {"subject": "Invoice question", "body": "Why was I billed $12 extra?"},
]

results = agent.predict_batch(
    states, TICKET_QUESTIONS)  # one result each

for state, result in zip(states, results):
    print(result["answers"]["department"]["choice"])
