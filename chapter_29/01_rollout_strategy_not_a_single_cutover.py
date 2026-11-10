# The LAYA Handbook — Chapter 29: Deployment and Monitoring in Practice
# Section: A Rollout Strategy, Not a Single Cutover

import random

CANDIDATE_ROLLOUT_PERCENT = 5   # start small; raise only as confidence builds

def route_ticket_with_rollout(raw_ticket):
    use_candidate = random.random() < (CANDIDATE_ROLLOUT_PERCENT / 100)
    questions = TICKET_QUESTIONS_CANDIDATE if use_candidate else TICKET_QUESTIONS_CURRENT
    result = route_ticket_core(raw_ticket, questions)
    result["version"] = "candidate" if use_candidate else "current"
    return result
