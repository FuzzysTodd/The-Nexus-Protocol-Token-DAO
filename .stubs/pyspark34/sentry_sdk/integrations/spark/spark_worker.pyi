from sentry_sdk import configure_scope as configure_scope
from sentry_sdk._types import Event as Event, ExcInfo as ExcInfo, Hint as Hint, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import Integration as Integration
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, event_hint_with_exc_info as event_hint_with_exc_info, exc_info_from_error as exc_info_from_error, single_exception_from_error_tuple as single_exception_from_error_tuple, walk_exception_chain as walk_exception_chain

class SparkWorkerIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...
