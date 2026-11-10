# The LAYA Handbook — Chapter 18: Golden-Set Testing Discipline
# Section: A Complete Evaluation Harness

from collections import defaultdict

def evaluate_against_golden_set(questions, golden_set, agent):
    correct, n = 0, 0
    buckets = defaultdict(list)

    for example in golden_set:
        if "true_department" not in example:
            continue   # labels another question
        n += 1
        result = agent.predict(example["state"], questions)
        dept = result["answers"]["department"]
        was_correct = dept["choice"] == example["true_department"]
        correct += was_correct
        bucket = round(dept["answer_confidence"], 1)
        buckets[bucket].append(was_correct)

    accuracy = correct / n
    ece = 0.0
    for bucket, outcomes in buckets.items():
        observed = sum(outcomes) / len(outcomes)
        weight = len(outcomes) / n
        ece += weight * abs(bucket - observed)

    return {"accuracy": accuracy, "ece": ece, "n": n}
