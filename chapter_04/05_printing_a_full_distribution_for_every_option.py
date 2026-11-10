# The LAYA Handbook — Chapter 4: Your First Prediction: agent.predict() End to End
# Section: Printing a Full Distribution for Every Option, Not Just the Winner

for option, probability in sorted(answer["probabilities"].items(), key=lambda kv: -kv[1]):
    print(f"{option:12s} {probability:.3f}")
# billing      0.04
# technical    0.05
# retention    0.91
