from _typeshed import Incomplete
from sentry_sdk._compat import PY2 as PY2, reraise as reraise
from sentry_sdk._functools import partial as partial
from sentry_sdk._types import EventProcessor as EventProcessor, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk._werkzeug import get_host as get_host
from sentry_sdk.api import continue_trace as continue_trace
from sentry_sdk.consts import OP as OP
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.sessions import auto_session_tracking as auto_session_tracking
from sentry_sdk.tracing import TRANSACTION_SOURCE_ROUTE as TRANSACTION_SOURCE_ROUTE, Transaction as Transaction
from sentry_sdk.utils import ContextVar as ContextVar, ExcInfo as ExcInfo, capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception
from typing import Any, Callable, Dict, Iterator, Protocol, TypeVar

WsgiResponseIter = TypeVar('WsgiResponseIter')
WsgiResponseHeaders = TypeVar('WsgiResponseHeaders')
WsgiExcInfo = TypeVar('WsgiExcInfo')

class StartResponse(Protocol):
    def __call__(self, status: str, response_headers: WsgiResponseHeaders, exc_info: WsgiExcInfo | None = None) -> WsgiResponseIter: ...

def wsgi_decoding_dance(s: str, charset: str = 'utf-8', errors: str = 'replace') -> str: ...
def get_request_url(environ: Dict[str, str], use_x_forwarded_for: bool = False) -> str:
    """Return the absolute URL without query string for the given WSGI
    environment."""

class SentryWsgiMiddleware:
    app: Incomplete
    use_x_forwarded_for: Incomplete
    def __init__(self, app: Callable[[Dict[str, str], Callable[..., Any]], Any], use_x_forwarded_for: bool = False) -> None: ...
    def __call__(self, environ: Dict[str, str], start_response: Callable[..., Any]) -> _ScopedResponse: ...

def get_client_ip(environ: Dict[str, str]) -> Any | None:
    """
    Infer the user IP address from various headers. This cannot be used in
    security sensitive situations since the value may be forged from a client,
    but it's good enough for the event payload.
    """

class _ScopedResponse:
    def __init__(self, hub: Hub, response: Iterator[bytes]) -> None: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def close(self) -> None: ...
