from sentry_sdk._types import Event as Event, Hint as Hint, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP, SPANDATA as SPANDATA
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import Integration as Integration
from sentry_sdk.scope import add_global_event_processor as add_global_event_processor
from sentry_sdk.tracing_utils import EnvironHeaders as EnvironHeaders, should_propagate_trace as should_propagate_trace
from sentry_sdk.utils import SENSITIVE_DATA_SUBSTITUTE as SENSITIVE_DATA_SUBSTITUTE, capture_internal_exceptions as capture_internal_exceptions, is_sentry_url as is_sentry_url, logger as logger, parse_url as parse_url, safe_repr as safe_repr

class StdlibIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...

def get_subprocess_traceparent_headers() -> EnvironHeaders: ...
