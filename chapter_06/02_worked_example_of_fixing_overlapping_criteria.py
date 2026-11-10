# The LAYA Handbook — Chapter 6: Choice: Calibrated Classification in One Forward Pass
# Section: A Worked Example of Fixing Overlapping Criteria
# Note: excerpt of dictionary entries shown in isolation; it is not runnable on its own.

# Before: genuinely overlapping
"spam": "unwanted promotional or repetitive content",
"low_quality": "content that adds little value to the discussion",

# After: redrawn so a real example can be placed confidently in exactly one
"spam": "commercial promotion, links to unrelated products or services, or
         the same message posted repeatedly across multiple threads",
"low_quality": "on-topic but unhelpful — vague, low-effort, or substance-free,
               with no promotional or repetitive intent",
