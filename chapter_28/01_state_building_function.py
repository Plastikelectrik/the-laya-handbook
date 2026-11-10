# The LAYA Handbook — Chapter 28: Capstone Part 2: Building, Testing, and Deploying the Pipeline
# Section: The State-Building Function

def build_state(raw_ticket):
    """Chapter 5's discipline: translate raw input into exactly what the
    questions need, nothing more. Kept separate and testable on its own."""
    return {
        "subject": raw_ticket["subject"],
        "body": raw_ticket["body"],
    }
