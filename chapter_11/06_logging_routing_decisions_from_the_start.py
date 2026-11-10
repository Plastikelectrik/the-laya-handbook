# The LAYA Handbook — Chapter 11: The Router: Automatic Model Selection and Multilingual Text
# Section: Logging Routing Decisions From the Start

def predict_and_log(router, state, questions):
    result = router.predict(state, questions)
    minimal_log_entry = {
        "routing_model": result["routing"]["model"],
        "top_department_confidence": result["answers"].get("department", {}).get("answer_confidence"),
    }
    quick_log.write(minimal_log_entry)   # Chapter 26 builds the full version of this
    return result
