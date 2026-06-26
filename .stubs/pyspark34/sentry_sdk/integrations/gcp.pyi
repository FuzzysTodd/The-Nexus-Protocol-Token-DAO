from _typeshed import Incomplete
from sentry_sdk._compat import datetime_utcnow as datetime_utcnow, reraise as reraise
from sentry_sdk._types import Event as Event, EventProcessor as EventProcessor, Hint as Hint, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.api import continue_trace as continue_trace
from sentry_sdk.consts import OP as OP
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import Integration as Integration
from sentry_sdk.tracing import TRANSACTION_SOURCE_COMPONENT as TRANSACTION_SOURCE_COMPONENT
from sentry_sdk.utils import AnnotatedValue as AnnotatedValue, TimeoutThread as TimeoutThread, capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception, logger as logger
from typing import Any, Callable, TypeVar

TIMEOUT_WARNING_BUFFER: float
MILLIS_TO_SECONDS: float
F = TypeVar('F', bound=Callable[..., Any])

class GcpIntegration(Integration):
    identifier: str
    timeout_warning: Incomplete
    def __init__(self, timeout_warning: bool = False) -> None: ...
    @staticmethod
    def setup_once() -> None: ...
