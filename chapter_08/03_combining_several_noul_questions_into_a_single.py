# The LAYA Handbook — Chapter 8: Noul: Calibrated Yes/No Questions
# Section: Combining Several Noul Questions Into a Single Risk Score

RISK_QUESTIONS = {
    "unusual_amount": {"type": "noul", "instructions": "Is this amount unusually large for this customer's typical transaction history?"},
    "new_destination": {"type": "noul", "instructions": "Is the destination account newly added to this customer's profile?"},
    "unusual_timing": {"type": "noul", "instructions": "Does this request fall outside the customer's usual activity hours?"},
}

def combined_risk(answers):
    # A simple, interpretable combination — not the only reasonable one,
    # but a defensible starting point over an opaque black-box combiner.
    signals = [answers[q]["noul"] for q in RISK_QUESTIONS]
    return 1 - (1 - signals[0]) * (1 - signals[1]) * (1 - signals[2])
