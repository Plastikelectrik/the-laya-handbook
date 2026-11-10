# The LAYA Handbook — Chapter 8: Noul: Calibrated Yes/No Questions
# Section: A Worked Example With Two Thresholds

state = {
    "proposed_action": "refund_transaction",
    "proposed_amount": 8400.00,
    "customer_original_amount": 84.00,
    "reasoning_given": "Customer requested a refund for their recent order.",
}

questions = {
    "amount_mismatch": {
        "type": "noul",
        "instructions": "Does the proposed refund amount differ from the "
                        "customer's original transaction amount by more "
                        "than a plausible rounding or fee adjustment?",
    },
}

answer = agent.predict(state, questions)["answers"]["amount_mismatch"]

if answer["noul"] >= 0.9:
    block_action("refund amount mismatch", confidence=answer["noul"])
elif answer["noul"] >= 0.5:
    escalate_to_human("possible refund amount mismatch", confidence=answer["noul"])
else:
    allow_action()
