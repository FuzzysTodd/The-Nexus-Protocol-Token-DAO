from _typeshed import Incomplete
from sentry_sdk import Hub as Hub
from sentry_sdk._compat import reraise as reraise
from sentry_sdk._types import ExcInfo as ExcInfo, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.integrations import Integration as Integration
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception
from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

class ThreadingIntegration(Integration):
    identifier: str
    propagate_hub: Incomplete
    def __init__(self, propagate_hub: bool = False) -> None: ...
    run: Incomplete
    @staticmethod
    def setup_once() -> None: ...
