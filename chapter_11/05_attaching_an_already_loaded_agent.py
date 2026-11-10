# The LAYA Handbook — Chapter 11: The Router: Automatic Model Selection and Multilingual Text
# Section: Attaching an Already-Loaded Agent

existing_agent = laya.load("convaiinnovations/laya")
router = Router(preload=False)
router.attach("english", existing_agent)
# router now uses existing_agent for English input instead of loading its own
