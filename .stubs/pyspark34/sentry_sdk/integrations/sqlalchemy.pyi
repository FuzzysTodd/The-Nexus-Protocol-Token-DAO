from sentry_sdk._compat import text_type as text_type
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import SPANDATA as SPANDATA
from sentry_sdk.db.explain_plan.sqlalchemy import attach_explain_plan_to_span as attach_explain_plan_to_span
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.tracing import Span as Span
from sentry_sdk.tracing_utils import record_sql_queries as record_sql_queries
from sentry_sdk.utils import parse_version as parse_version

class SqlalchemyIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...
