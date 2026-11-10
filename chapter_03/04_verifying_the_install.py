# The LAYA Handbook — Chapter 3: Installing Laya: pip, Hugging Face Checkpoints, and Apache 2.0
# Section: Verifying the Install

import laya
print(laya.__version__)

agent = laya.load("convaiinnovations/laya")
print(type(agent))
