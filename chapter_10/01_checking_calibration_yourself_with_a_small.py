# The LAYA Handbook — Chapter 10: Understanding Calibration: What a Probability From Laya Actually Means
# Section: Checking Calibration Yourself, With a Small Labeled Set

from collections import defaultdict

buckets = defaultdict(list)   # bucket -> list of (was_correct: bool)

for state, questions, true_answer in labeled_examples:
    result = agent.predict(state, questions)
    answer = result["answers"]["department"]
    bucket = round(answer["answer_confidence"], 1)   # groups into 0.1-wide bands
    buckets[bucket].append(answer["choice"] == true_answer)

for bucket in sorted(buckets):
    observed_accuracy = sum(buckets[bucket]) / len(buckets[bucket])
    print(f"confidence ~{bucket}: observed accuracy {observed_accuracy:.2f} "
          f"(n={len(buckets[bucket])})")
