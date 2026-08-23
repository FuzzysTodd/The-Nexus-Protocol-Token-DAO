from _typeshed import Incomplete
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import Integration as Integration
from sentry_sdk.scope import add_global_event_processor as add_global_event_processor
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions

MODULE_RE: str
TYPE_RE: str
HEXVAL_RE: str
FRAME_RE: Incomplete

class GnuBacktraceIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...
