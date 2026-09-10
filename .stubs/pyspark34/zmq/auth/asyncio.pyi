import zmq
from .base import Authenticator
from typing import Any

__all__ = ['AsyncioAuthenticator']

class AsyncioAuthenticator(Authenticator):
    """ZAP authentication for use in the asyncio IO loop"""
    def __init__(self, context: zmq.Context | None = None, loop: Any = None, encoding: str = 'utf-8', log: Any = None) -> None: ...
    def start(self) -> None:
        """Start ZAP authentication"""
    def stop(self) -> None:
        """Stop ZAP authentication"""
