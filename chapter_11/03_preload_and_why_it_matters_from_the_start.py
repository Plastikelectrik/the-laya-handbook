# The LAYA Handbook — Chapter 11: The Router: Automatic Model Selection and Multilingual Text
# Section: Preload, and Why It Matters From the Start

router = Router(preload=True)                 # CPU or auto-detected device
router = Router(preload=True, device="cuda")   # explicit GPU placement
