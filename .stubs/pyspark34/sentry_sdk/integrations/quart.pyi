from _typeshed import Incomplete
from quart import Request as Request
from sentry_sdk._functools import wraps as wraps
from sentry_sdk._types import EventProcessor as EventProcessor, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware as SentryAsgiMiddleware
from sentry_sdk.scope import Scope as Scope
from sentry_sdk.tracing import SOURCE_FOR_STYLE as SOURCE_FOR_STYLE
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception

TRANSACTION_STYLE_VALUES: Incomplete

class QuartIntegration(Integration):
    identifier: str
    transaction_style: str
    def __init__(self, transaction_style: str = 'endpoint') -> None: ...
    @staticmethod
    def setup_once() -> None: ...

def patch_asgi_app() -> None: ...
def patch_scaffold_route() -> None: ...
