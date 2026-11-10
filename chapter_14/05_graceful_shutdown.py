# The LAYA Handbook — Chapter 14: Production Architecture and the Router(preload=True) Pattern
# Section: Graceful Shutdown

import signal

shutting_down = False

def handle_shutdown_signal(signum, frame):
    global shutting_down
    shutting_down = True   # stop accepting NEW work; let in-flight requests finish

signal.signal(signal.SIGTERM, handle_shutdown_signal)
