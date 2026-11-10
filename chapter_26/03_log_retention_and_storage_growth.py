# The LAYA Handbook — Chapter 26: Observability: Logging, Auditing, and Dashboards for Decision Systems
# Section: Log Retention and Storage Growth

# Illustrative tiering policy, not a universal recommendation — set your own
# windows against your actual drift-detection and audit requirements.
HOT_STORAGE_DAYS = 90     # fast storage, used by dashboards and drift checks
ARCHIVE_STORAGE_DAYS = 730   # slower, cheaper storage, for audit/compliance lookups
# Beyond ARCHIVE_STORAGE_DAYS: deleted, per Chapter 30's retention policy,
# unless a specific legal hold requires longer retention for a specific record.
