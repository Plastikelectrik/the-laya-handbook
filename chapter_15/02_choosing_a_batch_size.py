# The LAYA Handbook — Chapter 15: Batched Prediction at Scale
# Section: Choosing a Batch Size

import time

SAMPLE_STATE = states[0]  # a ticket from above

def measure_throughput(batch_size, n_batches=5):
    sample_states = [SAMPLE_STATE] * batch_size
    start = time.perf_counter()
    for _ in range(n_batches):
        agent.predict_batch(sample_states,
                            TICKET_QUESTIONS)
    elapsed = time.perf_counter() - start
    total_predictions = batch_size * n_batches
    return total_predictions / elapsed   # predictions per second

for bs in [1, 4, 8, 16, 32, 64, 128]:
    print(bs, measure_throughput(bs))
