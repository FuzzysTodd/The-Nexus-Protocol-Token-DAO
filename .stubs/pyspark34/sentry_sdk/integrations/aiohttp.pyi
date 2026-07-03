from _typeshed import Incomplete
from aiohttp import TraceConfig, TraceRequestEndParams as TraceRequestEndParams, TraceRequestStartParams as TraceRequestStartParams
from aiohttp.abc import AbstractMatchInfo as AbstractMatchInfo
from aiohttp.web_request import Request as Request
from sentry_sdk._compat import reraise as reraise
from sentry_sdk._types import EventProcessor as EventProcessor, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.api import continue_trace as continue_trace
from sentry_sdk.consts import OP as OP, SPANDATA as SPANDATA
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations._wsgi_common import request_body_within_bounds as request_body_within_bounds
from sentry_sdk.integrations.logging import ignore_logger as ignore_logger
from sentry_sdk.sessions import auto_session_tracking as auto_session_tracking
from sentry_sdk.tracing import BAGGAGE_HEADER_NAME as BAGGAGE_HEADER_NAME, SOURCE_FOR_STYLE as SOURCE_FOR_STYLE, TRANSACTION_SOURCE_ROUTE as TRANSACTION_SOURCE_ROUTE
from sentry_sdk.tracing_utils import should_propagate_trace as should_propagate_trace
from sentry_sdk.utils import AnnotatedValue as AnnotatedValue, CONTEXTVARS_ERROR_MESSAGE as CONTEXTVARS_ERROR_MESSAGE, ExcInfo as ExcInfo, HAS_REAL_CONTEXTVARS as HAS_REAL_CONTEXTVARS, SENSITIVE_DATA_SUBSTITUTE as SENSITIVE_DATA_SUBSTITUTE, capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception, logger as logger, parse_url as parse_url, parse_version as parse_version, transaction_from_function as transaction_from_function

TRANSACTION_STYLE_VALUES: Incomplete

class AioHttpIntegration(Integration):
    identifier: str
    transaction_style: Incomplete
    def __init__(self, transaction_style: str = 'handler_name') -> None: ...
    @staticmethod
    def setup_once() -> None: ...

def create_trace_config() -> TraceConfig: ...

BODY_NOT_READ_MESSAGE: str

def get_aiohttp_request_data(hub: Hub, request: Request) -> str | None | AnnotatedValue: ...
