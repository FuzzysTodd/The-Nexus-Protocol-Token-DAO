from _typeshed import Incomplete
from sentry_sdk._functools import partial as partial
from sentry_sdk._types import Event as Event, Hint as Hint, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.api import continue_trace as continue_trace
from sentry_sdk.consts import OP as OP
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.sessions import auto_session_tracking as auto_session_tracking
from sentry_sdk.tracing import SOURCE_FOR_STYLE as SOURCE_FOR_STYLE, TRANSACTION_SOURCE_COMPONENT as TRANSACTION_SOURCE_COMPONENT, TRANSACTION_SOURCE_ROUTE as TRANSACTION_SOURCE_ROUTE, TRANSACTION_SOURCE_URL as TRANSACTION_SOURCE_URL, Transaction as Transaction
from sentry_sdk.utils import CONTEXTVARS_ERROR_MESSAGE as CONTEXTVARS_ERROR_MESSAGE, ContextVar as ContextVar, HAS_REAL_CONTEXTVARS as HAS_REAL_CONTEXTVARS, event_from_exception as event_from_exception, logger as logger, transaction_from_function as transaction_from_function
from typing import Any

TRANSACTION_STYLE_VALUES: Incomplete

class SentryAsgiMiddleware:
    transaction_style: Incomplete
    mechanism_type: Incomplete
    app: Incomplete
    __call__: Incomplete
    def __init__(self, app: Any, unsafe_context_data: bool = False, transaction_style: str = 'endpoint', mechanism_type: str = 'asgi') -> None:
        """
        Instrument an ASGI application with Sentry. Provides HTTP/websocket
        data to sent events and basic handling for exceptions bubbling up
        through the middleware.

        :param unsafe_context_data: Disable errors when a proper contextvars installation could not be found. We do not recommend changing this from the default.
        """
    def event_processor(self, event: Event, hint: Hint, asgi_scope: Any) -> Event | None: ...
