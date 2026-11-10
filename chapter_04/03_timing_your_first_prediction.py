# The LAYA Handbook — Chapter 4: Your First Prediction: agent.predict() End to End
# Section: Timing Your First Prediction

import time

start = time.perf_counter()
result = agent.predict(state, questions)
elapsed_ms = (time.perf_counter() - start) * 1000
print(f"{elapsed_ms:.1f} ms")
