# The LAYA Handbook — Chapter 14: Production Architecture and the Router(preload=True) Pattern
# Section: Preloading Inside an Async or Threaded Server

import asyncio

_startup_lock = asyncio.Lock()
_router = None

async def get_router():
    global _router
    async with _startup_lock:
        if _router is None:
            _router = Router(preload=True, max_loaded=2)
    return _router
