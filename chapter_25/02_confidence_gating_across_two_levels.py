# The LAYA Handbook — Chapter 25: Scaling Beyond a Single Checkpoint: Hierarchical and High-Cardinality Routing
# Section: Confidence Gating Across Two Levels

TOP_LEVEL_THRESHOLD = 0.80
SUB_LEVEL_THRESHOLD = 0.75

def resolve_sku_gated(state):
    top = agent.predict(state, TOP_LEVEL_QUESTION)["answers"]["product_line"]
    if top["answer_confidence"] < TOP_LEVEL_THRESHOLD:
        return None   # escalate: uncertain even at the top level

    sub_questions = SUB_QUESTIONS_BY_LINE[top["choice"]]
    sub = agent.predict(state, sub_questions)["answers"]["sku"]
    if sub["answer_confidence"] < SUB_LEVEL_THRESHOLD:
        return None   # escalate: confident about the branch, uncertain within it

    return sub["choice"]
