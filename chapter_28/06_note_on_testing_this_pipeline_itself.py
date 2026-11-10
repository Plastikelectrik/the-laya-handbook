# The LAYA Handbook — Chapter 28: Capstone Part 2: Building, Testing, and Deploying the Pipeline
# Section: A Note on Testing This Pipeline Itself

def test_fallback_department_detects_cancellation():
    state = {"subject": "...", "body": "Please cancel my account immediately."}
    assert fallback_department(state) == "retention"

def test_fallback_department_detects_technical_error():
    state = {"subject": "...", "body": "The export feature is broken and throws an error."}
    assert fallback_department(state) == "technical"
