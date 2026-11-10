# The LAYA Handbook — Chapter 17: Designing Production Criteria: The Department, Urgency, and Churn Model
# Section: Documenting Criteria Decisions Alongside the Code
# Note: excerpt of dictionary entries shown in isolation; it is not runnable on its own.

# churn_risk instructions, v2 (2024-11): added the explicit exclusion for
# frustration-without-stated-intent after golden-set review showed v1 was
# flagging a meaningful fraction of merely-angry tickets as churn risk,
# creating unnecessary retention-team workload. See golden-set eval
# comparison: v1 accuracy 0.84 / v2 accuracy 0.91 on the churn_risk slice.
"churn_risk": {
    "type": "noul",
    "instructions": "Does the customer express real intent to cancel, "
                    "downgrade, or switch to a competitor — not just "
                    "frustration with no stated intent to leave?",
},
