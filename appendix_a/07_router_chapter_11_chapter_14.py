# The LAYA Handbook — Appendix A: API and Primitive Quick Reference
# Section: The Router (Chapter 11, Chapter 14)

from laya import Router

router = Router(preload=True)                  # construct ONCE per process, at startup
router = Router(preload=True, device="cuda")   # explicit device placement
router = Router(preload=True, max_loaded=3)     # keep all 3 checkpoints (default 2)

result = router.predict(state, questions)       # same shape as agent.predict()
result["routing"]["model"]                      # which checkpoint answered

decision = router.route(state, questions)       # dispatch decision only, no prediction
decision.model, decision.reason

router.attach("english", existing_agent)        # use an already-loaded agent
