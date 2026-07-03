def get_asyncio_loop():
    """asyncio has deprecated get_event_loop

    Replicate it here, with our desired semantics:

    - always returns a valid, not-closed loop
    - not thread-local like asyncio's,
      because we only want one loop for IPython
    - if called from inside a coroutine (e.g. in ipykernel),
      return the running loop

    .. versionadded:: 8.0
    """

class _AsyncIORunner:
    def __call__(self, coro):
        """
        Handler for asyncio autoawait
        """

class _AsyncIOProxy:
    """Proxy-object for an asyncio

    Any coroutine methods will be wrapped in event_loop.run_
    """
    def __init__(self, obj, event_loop) -> None: ...
    def __getattr__(self, key): ...
    def __dir__(self): ...
