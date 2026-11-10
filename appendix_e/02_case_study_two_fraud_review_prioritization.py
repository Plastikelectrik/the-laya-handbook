# The LAYA Handbook — Appendix E: Worked Case Studies
# Section: Case Study Two: Fraud Review Prioritization

FRAUD_QUESTIONS = {
    "review_priority": {
        "type": "score",
        "instructions": "How urgently does this flagged transaction need human fraud review, "
                        "considering transaction size, account history, and stated flags together?",
        "criteria": ["low priority", "standard", "elevated", "immediate"],
    },
}

def queue_order(flagged_transactions):
    scored = [(t, agent.predict(build_state(t), FRAUD_QUESTIONS)["answers"]["review_priority"]["score"])
              for t in flagged_transactions]
    return [t for t, _ in sorted(scored, key=lambda pair: pair[1], reverse=True)]
