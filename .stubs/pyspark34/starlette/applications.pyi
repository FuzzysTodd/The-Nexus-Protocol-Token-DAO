import typing
from _typeshed import Incomplete
from starlette.datastructures import State as State, URLPath as URLPath
from starlette.middleware import Middleware as Middleware
from starlette.middleware.base import BaseHTTPMiddleware as BaseHTTPMiddleware
from starlette.middleware.errors import ServerErrorMiddleware as ServerErrorMiddleware
from starlette.middleware.exceptions import ExceptionMiddleware as ExceptionMiddleware
from starlette.requests import Request as Request
from starlette.responses import Response as Response
from starlette.routing import BaseRoute as BaseRoute, Router as Router
from starlette.types import ASGIApp as ASGIApp, Lifespan as Lifespan, Receive as Receive, Scope as Scope, Send as Send

AppType = typing.TypeVar('AppType', bound='Starlette')

class Starlette:
    """
    Creates an application instance.

    **Parameters:**

    * **debug** - Boolean indicating if debug tracebacks should be returned on errors.
    * **routes** - A list of routes to serve incoming HTTP and WebSocket requests.
    * **middleware** - A list of middleware to run for every request. A starlette
    application will always automatically include two middleware classes.
    `ServerErrorMiddleware` is added as the very outermost middleware, to handle
    any uncaught errors occurring anywhere in the entire stack.
    `ExceptionMiddleware` is added as the very innermost middleware, to deal
    with handled exception cases occurring in the routing or endpoints.
    * **exception_handlers** - A mapping of either integer status codes,
    or exception class types onto callables which handle the exceptions.
    Exception handler callables should be of the form
    `handler(request, exc) -> response` and may be be either standard functions, or
    async functions.
    * **on_startup** - A list of callables to run on application startup.
    Startup handler callables do not take any arguments, and may be be either
    standard functions, or async functions.
    * **on_shutdown** - A list of callables to run on application shutdown.
    Shutdown handler callables do not take any arguments, and may be be either
    standard functions, or async functions.
    * **lifespan** - A lifespan context function, which can be used to perform
    startup and shutdown tasks. This is a newer style that replaces the
    `on_startup` and `on_shutdown` handlers. Use one or the other, not both.
    """
    debug: Incomplete
    state: Incomplete
    router: Incomplete
    exception_handlers: Incomplete
    user_middleware: Incomplete
    middleware_stack: Incomplete
    def __init__(self, debug: bool = False, routes: typing.Sequence[BaseRoute] | None = None, middleware: typing.Sequence[Middleware] | None = None, exception_handlers: typing.Mapping[typing.Any, typing.Callable[[Request, Exception], Response | typing.Awaitable[Response]]] | None = None, on_startup: typing.Sequence[typing.Callable] | None = None, on_shutdown: typing.Sequence[typing.Callable] | None = None, lifespan: Lifespan['AppType'] | None = None) -> None: ...
    def build_middleware_stack(self) -> ASGIApp: ...
    @property
    def routes(self) -> typing.List[BaseRoute]: ...
    def url_path_for(self, __name: str, **path_params: typing.Any) -> URLPath: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    def on_event(self, event_type: str) -> typing.Callable: ...
    def mount(self, path: str, app: ASGIApp, name: str | None = None) -> None: ...
    def host(self, host: str, app: ASGIApp, name: str | None = None) -> None: ...
    def add_middleware(self, middleware_class: type, **options: typing.Any) -> None: ...
    def add_exception_handler(self, exc_class_or_status_code: int | typing.Type[Exception], handler: typing.Callable) -> None: ...
    def add_event_handler(self, event_type: str, func: typing.Callable) -> None: ...
    def add_route(self, path: str, route: typing.Callable, methods: typing.List[str] | None = None, name: str | None = None, include_in_schema: bool = True) -> None: ...
    def add_websocket_route(self, path: str, route: typing.Callable, name: str | None = None) -> None: ...
    def exception_handler(self, exc_class_or_status_code: int | typing.Type[Exception]) -> typing.Callable: ...
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
    def middleware(self, middleware_type: str) -> typing.Callable:
        """
        We no longer document this decorator style API, and its usage is discouraged.
        Instead you should use the following approach:

        >>> middleware = [Middleware(...), ...]
        >>> app = Starlette(middleware=middleware)
        """
