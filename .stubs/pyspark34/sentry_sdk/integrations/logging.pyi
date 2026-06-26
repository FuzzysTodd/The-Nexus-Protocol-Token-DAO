import logging
from _typeshed import Incomplete
from logging import LogRecord
from sentry_sdk._compat import iteritems as iteritems, utc_from_timestamp as utc_from_timestamp
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import Integration as Integration
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, current_stacktrace as current_stacktrace, event_from_exception as event_from_exception, to_string as to_string
from typing import Any

DEFAULT_LEVEL: Incomplete
DEFAULT_EVENT_LEVEL: Incomplete
LOGGING_TO_EVENT_LEVEL: Incomplete

def ignore_logger(name: str) -> None:
    """This disables recording (both in breadcrumbs and as events) calls to
    a logger of a specific name.  Among other uses, many of our integrations
    use this to prevent their actions being recorded as breadcrumbs. Exposed
    to users as a way to quiet spammy loggers.

    :param name: The name of the logger to ignore (same string you would pass to ``logging.getLogger``).
    """

class LoggingIntegration(Integration):
    identifier: str
    def __init__(self, level: int | None = ..., event_level: int | None = ...) -> None: ...
    @staticmethod
    def setup_once() -> None: ...

class _BaseHandler(logging.Handler):
    COMMON_RECORD_ATTRS: Incomplete

class EventHandler(_BaseHandler):
    """
    A logging handler that emits Sentry events for each log record

    Note that you do not have to use this class if the logging integration is enabled, which it is by default.
    """
    def emit(self, record: LogRecord) -> Any: ...
SentryHandler = EventHandler

class BreadcrumbHandler(_BaseHandler):
    """
    A logging handler that records breadcrumbs for each log record.

    Note that you do not have to use this class if the logging integration is enabled, which it is by default.
    """
    def emit(self, record: LogRecord) -> Any: ...
