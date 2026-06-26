from chalice.app import EventSourceHandler as ChaliceEventSourceHandler
from sentry_sdk._compat import reraise as reraise
from sentry_sdk._functools import wraps as wraps
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.tracing import TRANSACTION_SOURCE_COMPONENT as TRANSACTION_SOURCE_COMPONENT
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception, parse_version as parse_version
from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

class EventSourceHandler(ChaliceEventSourceHandler):
    def __call__(self, event: Any, context: Any) -> Any: ...

class ChaliceIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...
