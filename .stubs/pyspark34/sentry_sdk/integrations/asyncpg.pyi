from _typeshed import Incomplete
from asyncpg.cursor import BaseCursor
from sentry_sdk import Hub as Hub
from sentry_sdk.consts import OP as OP, SPANDATA as SPANDATA
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.tracing import Span as Span
from sentry_sdk.tracing_utils import record_sql_queries as record_sql_queries
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, parse_version as parse_version
from typing import TypeVar

asyncpg_version: Incomplete

class AsyncPGIntegration(Integration):
    identifier: str
    def __init__(self, *, record_params: bool = False) -> None: ...
    @staticmethod
    def setup_once() -> None: ...
T = TypeVar('T')
SubCursor = TypeVar('SubCursor', bound=BaseCursor)
