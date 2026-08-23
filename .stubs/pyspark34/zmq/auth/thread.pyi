import asyncio
import zmq
import zmq.asyncio
from .base import Authenticator
from _typeshed import Incomplete
from threading import Thread
from typing import Any

__all__ = ['ThreadAuthenticator']

class AuthenticationThread(Thread):
    """A Thread for running a zmq Authenticator

    This is run in the background by ThreadAuthenticator
    """
    pipe: zmq.Socket
    loop: asyncio.AbstractEventLoop
    authenticator: Authenticator
    poller: zmq.asyncio.Poller | None
    log: Incomplete
    started: Incomplete
    def __init__(self, authenticator: Authenticator, pipe: zmq.Socket) -> None: ...
    def run(self) -> None:
        """Start the Authentication Agent thread task"""

class ThreadAuthenticator(Authenticator):
    """Run ZAP authentication in a background thread"""
    pipe: zmq.Socket
    pipe_endpoint: str
    thread: AuthenticationThread
    def __init__(self, context: zmq.Context | None = None, encoding: str = 'utf-8', log: Any = None) -> None: ...
    def start(self) -> None:
        """Start the authentication thread"""
    def stop(self) -> None:
        """Stop the authentication thread"""
    def is_alive(self) -> bool:
        """Is the ZAP thread currently running?"""
    def __del__(self) -> None: ...
