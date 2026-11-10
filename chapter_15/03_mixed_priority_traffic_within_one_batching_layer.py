# The LAYA Handbook — Chapter 15: Batched Prediction at Scale
# Section: Mixed-Priority Traffic Within One Batching Layer

INTERACTIVE_WINDOW_MS = 10
BULK_WINDOW_MS = 200

# Two independent accumulation loops, both calling router.predict_batch() against
# the SAME preloaded Router (Chapter 14) — only the batching policy differs,
# not the underlying model or checkpoint being served.
