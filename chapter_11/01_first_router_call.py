# The LAYA Handbook — Chapter 11: The Router: Automatic Model Selection and Multilingual Text
# Section: A First Router Call

from laya import Router

router = Router(preload=True)

state_en = {"body": "I was charged twice, please refund."}
state_hi = {"body": "मुझसे दो बार शुल्क लिया गया"}

questions = {
    "department": {
        "type": "choice",
        "instructions": "Which department should handle this?",
        "criteria": {"billing": "charges, refunds", "technical": "bugs, errors"},
    },
}

res_en = router.predict(state_en, questions)
res_hi = router.predict(state_hi, questions)

print(res_en["routing"]["model"])   # 'english'
print(res_hi["routing"]["model"])   # 'multilingual'
