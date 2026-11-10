# The LAYA Handbook — Chapter 26: Observability: Logging, Auditing, and Dashboards for Decision Systems
# Section: What a Single Prediction Log Entry Needs

import hashlib, json, time

def log_prediction(state, questions, result, routing_info, checkpoint_version):
    state_hash = hashlib.sha256(json.dumps(state, sort_keys=True).encode()).hexdigest()
    entry = {
        "timestamp": time.time(),
        "state_hash": state_hash,       # not the raw state — see this chapter's privacy note
        "questions_asked": list(questions.keys()),
        "answers": {
            name: {k: v for k, v in answer.items() if k != "probabilities"}
            for name, answer in result["answers"].items()
        },
        "full_distributions": {
            name: answer.get("probabilities") for name, answer in result["answers"].items()
        },
        "checkpoint_version": checkpoint_version,
        "routing_model": routing_info.get("model") if routing_info else None,
    }
    audit_log.write(entry)
