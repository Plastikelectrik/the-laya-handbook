# The LAYA Handbook — Chapter 4: Your First Prediction: agent.predict() End to End
# Section: Reading the Result

answer = result["answers"]["department"]

print(answer["choice"])         # 'retention'
print(answer["answer_confidence"])  # 0.91
print(answer["probabilities"])  # {'billing': 0.04, 'technical': 0.05,
                                 #  'retention': 0.91}
