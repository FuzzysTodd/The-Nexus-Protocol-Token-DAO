import typing
from _typeshed import Incomplete
from starlette._utils import is_async_callable as is_async_callable
from starlette.concurrency import run_in_threadpool as run_in_threadpool
from starlette.exceptions import HTTPException as HTTPException, WebSocketException as WebSocketException
from starlette.requests import Request as Request
from starlette.responses import PlainTextResponse as PlainTextResponse, Response as Response
from starlette.types import ASGIApp as ASGIApp, Message as Message, Receive as Receive, Scope as Scope, Send as Send
from starlette.websockets import WebSocket as WebSocket

class ExceptionMiddleware:
    app: Incomplete
    debug: Incomplete
    def __init__(self, app: ASGIApp, handlers: typing.Mapping[typing.Any, typing.Callable[[Request, Exception], Response]] | None = None, debug: bool = False) -> None: ...
    def add_exception_handler(self, exc_class_or_status_code: int | typing.Type[Exception], handler: typing.Callable[[Request, Exception], Response]) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    def http_exception(self, request: Request, exc: HTTPException) -> Response: ...
    async def websocket_exception(self, websocket: WebSocket, exc: WebSocketException) -> None: ...
