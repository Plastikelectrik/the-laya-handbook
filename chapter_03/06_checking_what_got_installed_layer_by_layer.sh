#!/usr/bin/env bash
# The LAYA Handbook — Chapter 3: Installing Laya: pip, Hugging Face Checkpoints, and Apache 2.0
# Section: Checking What Got Installed, Layer by Layer

pip show laya
# Name, Version, Location, Requires: ... — confirms exactly what is on disk
pip list | grep -i laya   # sanity-check there is exactly one installed version
