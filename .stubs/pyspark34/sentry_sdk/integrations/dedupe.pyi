from sentry_sdk._types import Event as Event, Hint as Hint, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import Integration as Integration
from sentry_sdk.scope import add_global_event_processor as add_global_event_processor
from sentry_sdk.utils import ContextVar as ContextVar

class DedupeIntegration(Integration):
    identifier: str
    def __init__(self) -> None: ...
    @staticmethod
    def setup_once() -> None: ...
