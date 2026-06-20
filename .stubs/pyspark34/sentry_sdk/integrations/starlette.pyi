from _typeshed import Incomplete
from sentry_sdk._compat import iteritems as iteritems
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations._wsgi_common import request_body_within_bounds as request_body_within_bounds
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware as SentryAsgiMiddleware
from sentry_sdk.tracing import SOURCE_FOR_STYLE as SOURCE_FOR_STYLE, TRANSACTION_SOURCE_COMPONENT as TRANSACTION_SOURCE_COMPONENT, TRANSACTION_SOURCE_ROUTE as TRANSACTION_SOURCE_ROUTE
from sentry_sdk.utils import AnnotatedValue as AnnotatedValue, capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception, logger as logger, parse_version as parse_version, transaction_from_function as transaction_from_function
from starlette.requests import Request as Request
from starlette.types import ASGIApp as ASGIApp, Receive as Receive, Send as Send
from typing import Any, Dict

TRANSACTION_STYLE_VALUES: Incomplete

class StarletteIntegration(Integration):
    identifier: str
    transaction_style: str
    def __init__(self, transaction_style: str = 'url') -> None: ...
    @staticmethod
    def setup_once() -> None: ...

def patch_exception_middleware(middleware_class: Any) -> None:
    """
    Capture all exceptions in Starlette app and
    also extract user information.
    """
def patch_authentication_middleware(middleware_class: Any) -> None:
    """
    Add user information to Sentry scope.
    """
def patch_middlewares() -> None:
    """
    Patches Starlettes `Middleware` class to record
    spans for every middleware invoked.
    """
def patch_asgi_app() -> None:
    """
    Instrument Starlette ASGI app using the SentryAsgiMiddleware.
    """
def patch_request_response() -> None: ...
def patch_templates() -> None: ...

class StarletteRequestExtractor:
    """
    Extracts useful information from the Starlette request
    (like form data or cookies) and adds it to the Sentry event.
    """
    request: Request
    def __init__(self, request: Request) -> None: ...
    def extract_cookies_from_request(self) -> Dict[str, Any] | None: ...
    async def extract_request_info(self) -> Dict[str, Any] | None: ...
    async def content_length(self) -> int | None: ...
    def cookies(self) -> Dict[str, Any]: ...
    async def form(self) -> Any: ...
    def is_json(self) -> bool: ...
    async def json(self) -> Dict[str, Any] | None: ...
