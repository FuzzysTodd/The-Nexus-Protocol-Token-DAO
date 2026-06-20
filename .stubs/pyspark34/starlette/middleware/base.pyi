import typing
from _typeshed import Incomplete
from starlette.background import BackgroundTask as BackgroundTask
from starlette.requests import Request as Request
from starlette.responses import ContentStream as ContentStream, Response as Response, StreamingResponse as StreamingResponse
from starlette.types import ASGIApp as ASGIApp, Message as Message, Receive as Receive, Scope as Scope, Send as Send

RequestResponseEndpoint: Incomplete
DispatchFunction: Incomplete
T = typing.TypeVar('T')

class BaseHTTPMiddleware:
    app: Incomplete
    dispatch_func: Incomplete
    def __init__(self, app: ASGIApp, dispatch: DispatchFunction | None = None) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response: ...

class _StreamingResponse(StreamingResponse):
    def __init__(self, content: ContentStream, status_code: int = 200, headers: typing.Mapping[str, str] | None = None, media_type: str | None = None, background: BackgroundTask | None = None, info: typing.Mapping[str, typing.Any] | None = None) -> None: ...
    async def stream_response(self, send: Send) -> None: ...
