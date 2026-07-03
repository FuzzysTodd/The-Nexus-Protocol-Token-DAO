import typing
from _typeshed import Incomplete
from starlette.types import Receive as Receive, Scope as Scope, Send as Send

def build_environ(scope: Scope, body: bytes) -> dict:
    """
    Builds a scope and request body into a WSGI environ object.
    """

class WSGIMiddleware:
    app: Incomplete
    def __init__(self, app: typing.Callable) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...

class WSGIResponder:
    app: Incomplete
    scope: Incomplete
    status: Incomplete
    response_headers: Incomplete
    response_started: bool
    exc_info: Incomplete
    def __init__(self, app: typing.Callable, scope: Scope) -> None: ...
    async def __call__(self, receive: Receive, send: Send) -> None: ...
    async def sender(self, send: Send) -> None: ...
    def start_response(self, status: str, response_headers: typing.List[typing.Tuple[str, str]], exc_info: typing.Any = None) -> None: ...
    def wsgi(self, environ: dict, start_response: typing.Callable) -> None: ...
