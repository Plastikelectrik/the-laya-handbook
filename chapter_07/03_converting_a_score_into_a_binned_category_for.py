# The LAYA Handbook — Chapter 7: Score: Ordinal Judgments on a Rubric
# Section: Converting a Score Into a Binned Category for Reporting

def urgency_label(score):
    if score >= 2.5: return "high"
    if score >= 1.0: return "medium"
    return "low"

# Used only for a human-facing report — the raw score remains
# the value any threshold comparison or logged record should use.
