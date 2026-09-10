import concurrent.futures
import io
from _typeshed import Incomplete
from typing import Iterable, Tuple
from uvicorn._types import ASGIReceiveCallable as ASGIReceiveCallable, ASGIReceiveEvent as ASGIReceiveEvent, ASGISendCallable as ASGISendCallable, ASGISendEvent as ASGISendEvent, Environ as Environ, ExcInfo as ExcInfo, HTTPRequestEvent as HTTPRequestEvent, HTTPResponseBodyEvent as HTTPResponseBodyEvent, HTTPResponseStartEvent as HTTPResponseStartEvent, HTTPScope as HTTPScope, StartResponse as StartResponse, WSGIApp as WSGIApp

def build_environ(scope: HTTPScope, message: ASGIReceiveEvent, body: io.BytesIO) -> Environ:
    """
    Builds a scope and request message into a WSGI environ object.
    """

class _WSGIMiddleware:
    app: Incomplete
    executor: Incomplete
    def __init__(self, app: WSGIApp, workers: int = 10) -> None: ...
    async def __call__(self, scope: HTTPScope, receive: ASGIReceiveCallable, send: ASGISendCallable) -> None: ...

class WSGIResponder:
    app: Incomplete
    executor: Incomplete
    scope: Incomplete
    status: Incomplete
    response_headers: Incomplete
    send_event: Incomplete
    send_queue: Incomplete
    loop: Incomplete
    response_started: bool
    exc_info: Incomplete
    def __init__(self, app: WSGIApp, executor: concurrent.futures.ThreadPoolExecutor, scope: HTTPScope) -> None: ...
    async def __call__(self, receive: ASGIReceiveCallable, send: ASGISendCallable) -> None: ...
    async def sender(self, send: ASGISendCallable) -> None: ...
    def start_response(self, status: str, response_headers: Iterable[Tuple[str, str]], exc_info: ExcInfo | None = None) -> None: ...
    def wsgi(self, environ: Environ, start_response: StartResponse) -> None: ...
