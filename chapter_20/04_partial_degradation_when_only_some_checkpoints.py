# The LAYA Handbook — Chapter 20: Degraded-Mode Design: What Happens When Inference Fails
# Section: Partial Degradation: When Only Some Checkpoints Fail

class PerCheckpointHealth:
    def __init__(self):
        self.health_by_checkpoint = {}   # checkpoint name -> InferenceHealth

    def record_failure(self, checkpoint_name):
        self.health_by_checkpoint.setdefault(checkpoint_name, InferenceHealth()).record_failure()

    def is_degraded(self, checkpoint_name):
        h = self.health_by_checkpoint.get(checkpoint_name)
        return h.is_degraded() if h else False
