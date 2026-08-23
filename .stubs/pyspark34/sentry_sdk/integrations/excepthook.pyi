from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import Integration as Integration
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception
from types import TracebackType
from typing import Any, Callable, Type

Excepthook = Callable[[Type[BaseException], BaseException, TracebackType | None], Any]

class ExcepthookIntegration(Integration):
    identifier: str
    always_run: bool
    def __init__(self, always_run: bool = False) -> None: ...
    @staticmethod
    def setup_once() -> None: ...
