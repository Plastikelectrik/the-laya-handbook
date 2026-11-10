#!/usr/bin/env bash
# The LAYA Handbook — Chapter 3: Installing Laya: pip, Hugging Face Checkpoints, and Apache 2.0
# Section: Setting Up a Reproducible Development Environment

pip freeze > requirements.txt

# On a fresh machine or CI environment:
python -m venv laya-env
source laya-env/bin/activate
pip install -r requirements.txt
