# The LAYA Handbook — Chapter 17: Designing Production Criteria: The Department, Urgency, and Churn Model
# Section: Versioning Criteria Changes Safely

TICKET_QUESTIONS_V1 = { ... }   # the Chapter 12 version
TICKET_QUESTIONS_V2 = { ... }   # this chapter's version, with the "general"
                                # department and the refined churn_risk wording

# evaluate_against_golden_set() and GOLDEN_SET:
# built in Chapter 18
# Evaluate both versions against the SAME golden set before switching:
v1_metrics = evaluate_against_golden_set(TICKET_QUESTIONS_V1, GOLDEN_SET, agent)
v2_metrics = evaluate_against_golden_set(TICKET_QUESTIONS_V2, GOLDEN_SET, agent)
compare(v1_metrics, v2_metrics)
