from _typeshed import Incomplete
from sanic.request import Request as Request, RequestParameters as RequestParameters
from sanic.router import Route as Route
from sentry_sdk._compat import reraise as reraise, urlparse as urlparse
from sentry_sdk._types import Event as Event, EventProcessor as EventProcessor, Hint as Hint, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations._wsgi_common import RequestExtractor as RequestExtractor
from sentry_sdk.integrations.logging import ignore_logger as ignore_logger
from sentry_sdk.tracing import TRANSACTION_SOURCE_COMPONENT as TRANSACTION_SOURCE_COMPONENT
from sentry_sdk.utils import CONTEXTVARS_ERROR_MESSAGE as CONTEXTVARS_ERROR_MESSAGE, HAS_REAL_CONTEXTVARS as HAS_REAL_CONTEXTVARS, capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception, parse_version as parse_version
from typing import Any, Dict

old_error_handler_lookup: Incomplete
old_handle_request: Incomplete
old_router_get: Incomplete
old_startup: Incomplete

class SanicIntegration(Integration):
    identifier: str
    version: Incomplete
    @staticmethod
    def setup_once() -> None: ...

class SanicRequestExtractor(RequestExtractor):
    def content_length(self) -> int: ...
    def cookies(self) -> Dict[str, str]: ...
    def raw_data(self) -> bytes: ...
    def form(self) -> RequestParameters: ...
    def is_json(self) -> bool: ...
    def json(self) -> Any | None: ...
    def files(self) -> RequestParameters: ...
    def size_of_file(self, file: Any) -> int: ...
