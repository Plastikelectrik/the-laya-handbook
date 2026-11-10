# The LAYA Handbook — Chapter 4: Your First Prediction: agent.predict() End to End
# Section: Handling an Unexpected Result Shape Defensively

def predict_safely(agent, state, questions):
    result = agent.predict(state, questions)
    missing = set(questions.keys()) - set(result["answers"].keys())
    if missing:
        raise RuntimeError(f"Laya did not return answers for: {missing}")
    return result
