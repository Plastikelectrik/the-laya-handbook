# The LAYA Handbook — Chapter 14: Production Architecture and the Router(preload=True) Pattern
# Section: One Process, Many Workers

# Gunicorn-style WSGI app, worker_count processes, each with its own router
# gunicorn --workers 4 --preload app:application
#
# --preload here is Gunicorn's own flag (fork workers after loading the app
# module once) and is unrelated to Router(preload=True) — do not confuse
# the two; check your own framework's docs for how worker startup and
# module-level code interact before relying on either preloading mechanism.
