# The LAYA Handbook — Chapter 20: Degraded-Mode Design: What Happens When Inference Fails
# Section: Healthy and Degraded as Explicit States

import time

class InferenceHealth:
    def __init__(self, failure_window_s=60, failure_threshold=5):
        self.recent_failures = []
        self.failure_window_s = failure_window_s
        self.failure_threshold = failure_threshold

    def record_failure(self):
        now = time.monotonic()
        self.recent_failures.append(now)
        cutoff = now - self.failure_window_s
        self.recent_failures = [t for t in self.recent_failures if t > cutoff]

    def is_degraded(self):
        return len(self.recent_failures) >= self.failure_threshold
