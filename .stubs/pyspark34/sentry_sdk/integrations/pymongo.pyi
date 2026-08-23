from _typeshed import Incomplete
from pymongo import monitoring
from pymongo.monitoring import CommandFailedEvent as CommandFailedEvent, CommandStartedEvent as CommandStartedEvent, CommandSucceededEvent as CommandSucceededEvent
from sentry_sdk import Hub as Hub
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import SPANDATA as SPANDATA
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.tracing import Span as Span
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions

SAFE_COMMAND_ATTRIBUTES: Incomplete

class CommandTracer(monitoring.CommandListener):
    def __init__(self) -> None: ...
    def started(self, event: CommandStartedEvent) -> None: ...
    def failed(self, event: CommandFailedEvent) -> None: ...
    def succeeded(self, event: CommandSucceededEvent) -> None: ...

class PyMongoIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...
