import ssl
from _typeshed import Incomplete
from gunicorn.workers import base
from types import FrameType
from typing import Any

__all__ = ['GunicornWebWorker', 'GunicornUVLoopWebWorker', 'GunicornTokioWebWorker']

SSLContext = ssl.SSLContext
SSLContext = object

class GunicornWebWorker(base.Worker):
    DEFAULT_AIOHTTP_LOG_FORMAT: Incomplete
    DEFAULT_GUNICORN_LOG_FORMAT: Incomplete
    exit_code: int
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    loop: Incomplete
    def init_process(self) -> None: ...
    def run(self) -> None: ...
    def init_signals(self) -> None: ...
    alive: bool
    def handle_quit(self, sig: int, frame: FrameType) -> None: ...
    def handle_abort(self, sig: int, frame: FrameType) -> None: ...

class GunicornUVLoopWebWorker(GunicornWebWorker):
    def init_process(self) -> None: ...

class GunicornTokioWebWorker(GunicornWebWorker):
    def init_process(self) -> None: ...
