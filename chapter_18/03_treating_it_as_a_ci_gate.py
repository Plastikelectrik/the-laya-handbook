# The LAYA Handbook — Chapter 18: Golden-Set Testing Discipline
# Section: Treating It as a CI Gate

CURRENT_METRICS = evaluate_against_golden_set(TICKET_QUESTIONS_V1, GOLDEN_SET, agent)
CANDIDATE_METRICS = evaluate_against_golden_set(TICKET_QUESTIONS_V2, GOLDEN_SET, agent)

ACCURACY_FLOOR_DROP = 0.02   # candidate may not be worse than this, in absolute accuracy
ECE_CEILING_RISE = 0.01      # candidate may not be worse than this, in absolute ECE

def gate_passes():
    acc_ok = CANDIDATE_METRICS["accuracy"] >= CURRENT_METRICS["accuracy"] - ACCURACY_FLOOR_DROP
    ece_ok = CANDIDATE_METRICS["ece"] <= CURRENT_METRICS["ece"] + ECE_CEILING_RISE
    return acc_ok and ece_ok
