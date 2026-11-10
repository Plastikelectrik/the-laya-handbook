# The LAYA Handbook — Chapter 14: Production Architecture and the Router(preload=True) Pattern
# Section: Health Checks and Readiness

router = None

def startup():
    global router
    router = Router(preload=True, max_loaded=2)

def readiness_check():
    return router is not None

# Call startup() once during process initialization, before accepting
# any traffic; wire readiness_check() to whatever health-check endpoint
# your serving framework and orchestrator (Kubernetes, ECS, etc.) expect.
