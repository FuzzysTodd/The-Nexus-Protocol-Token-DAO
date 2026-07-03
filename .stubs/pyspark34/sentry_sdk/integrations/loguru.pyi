import enum
import loguru
from _typeshed import Incomplete
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations.logging import BreadcrumbHandler as BreadcrumbHandler, EventHandler as EventHandler, _BaseHandler

class LoggingLevels(enum.IntEnum):
    TRACE: int
    DEBUG: int
    INFO: int
    SUCCESS: int
    WARNING: int
    ERROR: int
    CRITICAL: int

DEFAULT_LEVEL: Incomplete
DEFAULT_EVENT_LEVEL: Incomplete

class LoguruIntegration(Integration):
    identifier: str
    def __init__(self, level: int | None = ..., event_level: int | None = ..., breadcrumb_format: str | loguru.FormatFunction = ..., event_format: str | loguru.FormatFunction = ...) -> None: ...
    @staticmethod
    def setup_once() -> None: ...

class _LoguruBaseHandler(_BaseHandler): ...
class LoguruEventHandler(_LoguruBaseHandler, EventHandler):
    """Modified version of :class:`sentry_sdk.integrations.logging.EventHandler` to use loguru's level names."""
class LoguruBreadcrumbHandler(_LoguruBaseHandler, BreadcrumbHandler):
    """Modified version of :class:`sentry_sdk.integrations.logging.BreadcrumbHandler` to use loguru's level names."""
