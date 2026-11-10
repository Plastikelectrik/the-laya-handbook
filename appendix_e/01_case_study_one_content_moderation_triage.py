# The LAYA Handbook — Appendix E: Worked Case Studies
# Section: Case Study One: Content Moderation Triage

MODERATION_QUESTIONS = {
    "disposition": {
        "type": "choice",
        "instructions": "Does this post clearly comply with policy, clearly violate it, or need human review?",
        "criteria": {
            "approve": "clearly complies with content policy, no plausible concern",
            "reject": "clearly and unambiguously violates a specific named policy section",
            "review": "borderline, context-dependent, or policy-ambiguous content",
        },
    },
    "policy_section": {
        "type": "choice",
        "instructions": "If this violates policy, which section does it violate?",
        "criteria": {"harassment": "...", "misinformation": "...", "spam": "...", "other": "..."},
    },
}
MODERATION_THRESHOLD = 0.93   # considerably higher than the capstone's 0.82 — stakes justify it
