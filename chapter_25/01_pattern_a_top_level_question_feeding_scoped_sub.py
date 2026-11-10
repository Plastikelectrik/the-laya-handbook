# The LAYA Handbook — Chapter 25: Scaling Beyond a Single Checkpoint: Hierarchical and High-Cardinality Routing
# Section: The Pattern: A Top-Level Question Feeding Scoped Sub-Routers

TOP_LEVEL_QUESTION = {
    "product_line": {
        "type": "choice",
        "instructions": "Which product line does this support request concern?",
        "criteria": {
            "routers": "home and office networking hardware",
            "storage": "external and network-attached storage devices",
            "software": "the companion mobile and desktop applications",
        },
    },
}

SUB_QUESTIONS_BY_LINE = {
    "routers": {
        "sku": {
            "type": "choice",
            "instructions": "Which specific router model does this concern?",
            "criteria": {"rt-100": "entry-level, single-band", "rt-400": "mid-range, dual-band",
                         "rt-900": "flagship, tri-band mesh"},
        },
    },
    "storage": { "sku": { "type": "choice", "instructions": "...", "criteria": {"...": "..."} } },
    "software": { "sku": { "type": "choice", "instructions": "...", "criteria": {"...": "..."} } },
}

def resolve_sku(state):
    top = agent.predict(state, TOP_LEVEL_QUESTION)["answers"]["product_line"]
    sub_questions = SUB_QUESTIONS_BY_LINE[top["choice"]]
    sub = agent.predict(state, sub_questions)["answers"]["sku"]
    return top, sub
