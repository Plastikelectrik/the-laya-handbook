# The LAYA Handbook — Chapter 23: Security and Reliability for a Self-Hosted Model
# Section: Checkpoint Integrity

import hashlib

def verify_checkpoint(path, expected_sha256):
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hasher.update(chunk)
    actual = hasher.hexdigest()
    if actual != expected_sha256:
        raise ValueError(f"checkpoint integrity check failed: expected {expected_sha256}, got {actual}")
