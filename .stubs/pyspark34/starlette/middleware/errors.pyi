import inspect
import typing
from _typeshed import Incomplete
from starlette._utils import is_async_callable as is_async_callable
from starlette.concurrency import run_in_threadpool as run_in_threadpool
from starlette.requests import Request as Request
from starlette.responses import HTMLResponse as HTMLResponse, PlainTextResponse as PlainTextResponse, Response as Response
from starlette.types import ASGIApp as ASGIApp, Message as Message, Receive as Receive, Scope as Scope, Send as Send

STYLES: str
JS: str
TEMPLATE: str
FRAME_TEMPLATE: str
LINE: str
CENTER_LINE: str

class ServerErrorMiddleware:
    """
    Handles returning 500 responses when a server error occurs.

    If 'debug' is set, then traceback responses will be returned,
    otherwise the designated 'handler' will be called.

    This middleware class should generally be used to wrap *everything*
    else up, so that unhandled exceptions anywhere in the stack
    always result in an appropriate 500 response.
    """
    app: Incomplete
    handler: Incomplete
    debug: Incomplete
    def __init__(self, app: ASGIApp, handler: typing.Callable | None = None, debug: bool = False) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    def format_line(self, index: int, line: str, frame_lineno: int, frame_index: int) -> str: ...
    def generate_frame_html(self, frame: inspect.FrameInfo, is_collapsed: bool) -> str: ...
    def generate_html(self, exc: Exception, limit: int = 7) -> str: ...
    def generate_plain_text(self, exc: Exception) -> str: ...
    def debug_response(self, request: Request, exc: Exception) -> Response: ...
    def error_response(self, request: Request, exc: Exception) -> Response: ...
