import types
import typing
from _typeshed import Incomplete
from enum import Enum
from starlette._utils import is_async_callable as is_async_callable
from starlette.concurrency import run_in_threadpool as run_in_threadpool
from starlette.convertors import CONVERTOR_TYPES as CONVERTOR_TYPES, Convertor as Convertor
from starlette.datastructures import Headers as Headers, URL as URL, URLPath as URLPath
from starlette.exceptions import HTTPException as HTTPException
from starlette.middleware import Middleware as Middleware
from starlette.requests import Request as Request
from starlette.responses import PlainTextResponse as PlainTextResponse, RedirectResponse as RedirectResponse
from starlette.types import ASGIApp as ASGIApp, Lifespan as Lifespan, Receive as Receive, Scope as Scope, Send as Send
from starlette.websockets import WebSocket as WebSocket, WebSocketClose as WebSocketClose

class NoMatchFound(Exception):
    """
    Raised by `.url_for(name, **path_params)` and `.url_path_for(name, **path_params)`
    if no matching route exists.
    """
    def __init__(self, name: str, path_params: typing.Dict[str, typing.Any]) -> None: ...

class Match(Enum):
    NONE: int
    PARTIAL: int
    FULL: int

def iscoroutinefunction_or_partial(obj: typing.Any) -> bool:
    """
    Correctly determines if an object is a coroutine function,
    including those wrapped in functools.partial objects.
    """
def request_response(func: typing.Callable) -> ASGIApp:
    """
    Takes a function or coroutine `func(request) -> response`,
    and returns an ASGI application.
    """
def websocket_session(func: typing.Callable) -> ASGIApp:
    """
    Takes a coroutine `func(session)`, and returns an ASGI application.
    """
def get_name(endpoint: typing.Callable) -> str: ...
def replace_params(path: str, param_convertors: typing.Dict[str, Convertor], path_params: typing.Dict[str, str]) -> typing.Tuple[str, dict]: ...

PARAM_REGEX: Incomplete

def compile_path(path: str) -> typing.Tuple[typing.Pattern, str, typing.Dict[str, Convertor]]:
    '''
    Given a path string, like: "/{username:str}",
    or a host string, like: "{subdomain}.mydomain.org", return a three-tuple
    of (regex, format, {param_name:convertor}).

    regex:      "/(?P<username>[^/]+)"
    format:     "/{username}"
    convertors: {"username": StringConvertor()}
    '''

class BaseRoute:
    def matches(self, scope: Scope) -> typing.Tuple[Match, Scope]: ...
    def url_path_for(self, __name: str, **path_params: typing.Any) -> URLPath: ...
    async def handle(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """
        A route may be used in isolation as a stand-alone ASGI app.
        This is a somewhat contrived case, as they'll almost always be used
        within a Router, but could be useful for some tooling and minimal apps.
        """

class Route(BaseRoute):
    path: Incomplete
    endpoint: Incomplete
    name: Incomplete
    include_in_schema: Incomplete
    app: Incomplete
    methods: Incomplete
    def __init__(self, path: str, endpoint: typing.Callable, *, methods: typing.List[str] | None = None, name: str | None = None, include_in_schema: bool = True) -> None: ...
    def matches(self, scope: Scope) -> typing.Tuple[Match, Scope]: ...
    def url_path_for(self, __name: str, **path_params: typing.Any) -> URLPath: ...
    async def handle(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    def __eq__(self, other: typing.Any) -> bool: ...

class WebSocketRoute(BaseRoute):
    path: Incomplete
    endpoint: Incomplete
    name: Incomplete
    app: Incomplete
    def __init__(self, path: str, endpoint: typing.Callable, *, name: str | None = None) -> None: ...
    def matches(self, scope: Scope) -> typing.Tuple[Match, Scope]: ...
    def url_path_for(self, __name: str, **path_params: typing.Any) -> URLPath: ...
    async def handle(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    def __eq__(self, other: typing.Any) -> bool: ...

class Mount(BaseRoute):
    path: Incomplete
    app: Incomplete
    name: Incomplete
    def __init__(self, path: str, app: ASGIApp | None = None, routes: typing.Sequence[BaseRoute] | None = None, name: str | None = None, *, middleware: typing.Sequence[Middleware] | None = None) -> None: ...
    @property
    def routes(self) -> typing.List[BaseRoute]: ...
    def matches(self, scope: Scope) -> typing.Tuple[Match, Scope]: ...
    def url_path_for(self, __name: str, **path_params: typing.Any) -> URLPath: ...
    async def handle(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    def __eq__(self, other: typing.Any) -> bool: ...

class Host(BaseRoute):
    host: Incomplete
    app: Incomplete
    name: Incomplete
    def __init__(self, host: str, app: ASGIApp, name: str | None = None) -> None: ...
    @property
    def routes(self) -> typing.List[BaseRoute]: ...
    def matches(self, scope: Scope) -> typing.Tuple[Match, Scope]: ...
    def url_path_for(self, __name: str, **path_params: typing.Any) -> URLPath: ...
    async def handle(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    def __eq__(self, other: typing.Any) -> bool: ...

class _AsyncLiftContextManager(typing.AsyncContextManager[_T]):
    def __init__(self, cm: typing.ContextManager[_T]) -> None: ...
    async def __aenter__(self) -> _T: ...
    async def __aexit__(self, exc_type: typing.Type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> bool | None: ...

class _DefaultLifespan:
    def __init__(self, router: Router) -> None: ...
    async def __aenter__(self) -> None: ...
    async def __aexit__(self, *exc_info: object) -> None: ...
    def __call__(self, app: object) -> _T: ...

class Router:
    routes: Incomplete
    redirect_slashes: Incomplete
    default: Incomplete
    on_startup: Incomplete
    on_shutdown: Incomplete
    lifespan_context: Incomplete
    def __init__(self, routes: typing.Sequence[BaseRoute] | None = None, redirect_slashes: bool = True, default: ASGIApp | None = None, on_startup: typing.Sequence[typing.Callable] | None = None, on_shutdown: typing.Sequence[typing.Callable] | None = None, lifespan: Lifespan[typing.Any] | None = None) -> None: ...
    async def not_found(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    def url_path_for(self, __name: str, **path_params: typing.Any) -> URLPath: ...
    async def startup(self) -> None:
        """
        Run any `.on_startup` event handlers.
        """
    async def shutdown(self) -> None:
        """
        Run any `.on_shutdown` event handlers.
        """
    async def lifespan(self, scope: Scope, receive: Receive, send: Send) -> None:
        """
        Handle ASGI lifespan messages, which allows us to manage application
        startup and shutdown events.
        """
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """
        The main entry point to the Router class.
        """
    def __eq__(self, other: typing.Any) -> bool: ...
    def mount(self, path: str, app: ASGIApp, name: str | None = None) -> None: ...
    def host(self, host: str, app: ASGIApp, name: str | None = None) -> None: ...
    def add_route(self, path: str, endpoint: typing.Callable, methods: typing.List[str] | None = None, name: str | None = None, include_in_schema: bool = True) -> None: ...
    def add_websocket_route(self, path: str, endpoint: typing.Callable, name: str | None = None) -> None: ...
    def route(self, path: str, methods: typing.List[str] | None = None, name: str | None = None, include_in_schema: bool = True) -> typing.Callable:
        """
        We no longer document this decorator style API, and its usage is discouraged.
        Instead you should use the following approach:

        >>> routes = [Route(path, endpoint=...), ...]
        >>> app = Starlette(routes=routes)
        """
    def websocket_route(self, path: str, name: str | None = None) -> typing.Callable:
        """
        We no longer document this decorator style API, and its usage is discouraged.
        Instead you should use the following approach:

        >>> routes = [WebSocketRoute(path, endpoint=...), ...]
        >>> app = Starlette(routes=routes)
        """
    def add_event_handler(self, event_type: str, func: typing.Callable) -> None: ...
    def on_event(self, event_type: str) -> typing.Callable: ...
