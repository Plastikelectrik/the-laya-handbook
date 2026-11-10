# The LAYA Handbook — Chapter 28: Capstone Part 2: Building, Testing, and Deploying the Pipeline
# Section: Startup: One Preloaded Router, Built Once

from laya import Router

router = None

def startup():
    global router
    router = Router(preload=True, max_loaded=2)   # Chapter 14

def readiness_check():
    return router is not None
