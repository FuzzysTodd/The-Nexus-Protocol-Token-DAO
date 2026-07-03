import zmq
from .asyncio import AsyncioAuthenticator
from typing import Any

__all__ = ['IOLoopAuthenticator']

class IOLoopAuthenticator(AsyncioAuthenticator):
    """ZAP authentication for use in the tornado IOLoop"""
    def __init__(self, context: zmq.Context | None = None, encoding: str = 'utf-8', log: Any = None, io_loop: Any = None) -> None: ...
