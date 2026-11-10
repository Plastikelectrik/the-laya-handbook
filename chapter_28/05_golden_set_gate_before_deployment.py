# The LAYA Handbook — Chapter 28: Capstone Part 2: Building, Testing, and Deploying the Pipeline
# Section: The Golden-Set Gate Before Deployment

metrics = evaluate_against_golden_set(TICKET_QUESTIONS, CAPSTONE_GOLDEN_SET, router)
print(metrics)   # {'accuracy': 0.91, 'ece': 0.035, 'n': 180}

assert metrics["accuracy"] >= MINIMUM_ACCEPTABLE_ACCURACY
assert metrics["ece"] <= MAXIMUM_ACCEPTABLE_ECE
