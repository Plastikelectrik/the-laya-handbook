# The LAYA Handbook — Chapter 3: Installing Laya: pip, Hugging Face Checkpoints, and Apache 2.0
# Section: Confirming the Apache 2.0 License in Practice

# Confirm there is no network dependency once the checkpoint is cached:
# disconnect from the network, then run this in the same environment
# you loaded the checkpoint in earlier — it still returns an answer.
import laya
agent = laya.load("convaiinnovations/laya")
print(agent.predict({"text": "hello"}, {}))
