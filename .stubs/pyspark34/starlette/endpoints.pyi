import typing
from _typeshed import Incomplete
from starlette import status as status
from starlette._utils import is_async_callable as is_async_callable
from starlette.concurrency import run_in_threadpool as run_in_threadpool
from starlette.exceptions import HTTPException as HTTPException
from starlette.requests import Request as Request
from starlette.responses import PlainTextResponse as PlainTextResponse, Response as Response
from starlette.types import Message as Message, Receive as Receive, Scope as Scope, Send as Send
from starlette.websockets import WebSocket as WebSocket

class HTTPEndpoint:
    scope: Incomplete
    receive: Incomplete
    send: Incomplete
    def __init__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    def __await__(self) -> typing.Generator: ...
    async def dispatch(self) -> None: ...
    async def method_not_allowed(self, request: Request) -> Response: ...

class WebSocketEndpoint:
    encoding: str | None
    scope: Incomplete
    receive: Incomplete
    send: Incomplete
    def __init__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    def __await__(self) -> typing.Generator: ...
    async def dispatch(self) -> None: ...
    async def decode(self, websocket: WebSocket, message: Message) -> typing.Any: ...
    async def on_connect(self, websocket: WebSocket) -> None:
        """Override to handle an incoming websocket connection"""
    async def on_receive(self, websocket: WebSocket, data: typing.Any) -> None:
        """Override to handle an incoming websocket message"""
    async def on_disconnect(self, websocket: WebSocket, close_code: int) -> None:
        """Override to handle a disconnecting websocket"""
