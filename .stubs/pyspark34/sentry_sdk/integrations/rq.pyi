from rq.job import Job as Job
from sentry_sdk._types import EventProcessor as EventProcessor, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.api import continue_trace as continue_trace
from sentry_sdk.consts import OP as OP
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations.logging import ignore_logger as ignore_logger
from sentry_sdk.tracing import TRANSACTION_SOURCE_TASK as TRANSACTION_SOURCE_TASK
from sentry_sdk.utils import ExcInfo as ExcInfo, capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception, format_timestamp as format_timestamp, parse_version as parse_version

class RqIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...
