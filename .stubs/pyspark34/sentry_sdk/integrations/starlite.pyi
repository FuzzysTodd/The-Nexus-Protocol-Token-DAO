from sentry_sdk._types import Event as Event
from sentry_sdk.consts import OP as OP
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware as SentryAsgiMiddleware
from sentry_sdk.tracing import SOURCE_FOR_STYLE as SOURCE_FOR_STYLE, TRANSACTION_SOURCE_ROUTE as TRANSACTION_SOURCE_ROUTE
from sentry_sdk.utils import event_from_exception as event_from_exception, transaction_from_function as transaction_from_function
from starlite import MiddlewareProtocol as MiddlewareProtocol, Request as Request, State as State
from starlite.types import ASGIApp as ASGIApp, HTTPReceiveMessage as HTTPReceiveMessage, HTTPScope as HTTPScope, Message as Message, Middleware as Middleware, Receive as Receive, Scope as Scope, Send as Send, WebSocketReceiveMessage as WebSocketReceiveMessage
from typing import Any, Dict

class SentryStarliteASGIMiddleware(SentryAsgiMiddleware):
    def __init__(self, app: ASGIApp) -> None: ...

class StarliteIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...

def patch_app_init() -> None:
    """
    Replaces the Starlite class's `__init__` function in order to inject `after_exception` handlers and set the
    `SentryStarliteASGIMiddleware` as the outmost middleware in the stack.
    See:
    - https://starlite-api.github.io/starlite/usage/0-the-starlite-app/5-application-hooks/#after-exception
    - https://starlite-api.github.io/starlite/usage/7-middleware/0-middleware-intro/
    """
def patch_middlewares() -> None: ...
def enable_span_for_middleware(middleware: Middleware) -> Middleware: ...
def patch_http_route_handle() -> None: ...
def retrieve_user_from_scope(scope: Scope) -> Dict[str, Any] | None: ...
def exception_handler(exc: Exception, scope: Scope, _: State) -> None: ...
