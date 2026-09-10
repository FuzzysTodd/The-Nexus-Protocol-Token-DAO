from _typeshed import Incomplete
from gunicorn.workers.base import Worker
from typing import Any, Dict
from uvicorn.config import Config as Config
from uvicorn.main import Server as Server

class UvicornWorker(Worker):
    """
    A worker class for Gunicorn that interfaces with an ASGI consumer callable,
    rather than a WSGI callable.
    """
    CONFIG_KWARGS: Dict[str, Any]
    config: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def init_process(self) -> None: ...
    def init_signals(self) -> None: ...
    def run(self) -> None: ...
    async def callback_notify(self) -> None: ...

class UvicornH11Worker(UvicornWorker):
    CONFIG_KWARGS: Incomplete
