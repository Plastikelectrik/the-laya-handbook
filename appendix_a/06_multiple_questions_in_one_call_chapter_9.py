# The LAYA Handbook — Appendix A: API and Primitive Quick Reference
# Section: Multiple Questions in One Call (Chapter 9)

result = agent.predict(state, {
    "q1_name": {...},  # choice (Chapter 6)
    "q2_name": {...},  # score (Chapter 7)
    "q3_name": {...},  # noul (Chapter 8)
})
# result["answers"]["q1_name"], result["answers"]["q2_name"], result["answers"]["q3_name"]
