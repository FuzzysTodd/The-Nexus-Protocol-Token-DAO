from _typeshed import Incomplete
from functools import cached_property as cached_property
from graphql import GraphQLError as GraphQLError, GraphQLResolveInfo as GraphQLResolveInfo
from sentry_sdk import configure_scope as configure_scope, start_span as start_span
from sentry_sdk._types import EventProcessor as EventProcessor, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations.logging import ignore_logger as ignore_logger
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception, logger as logger, parse_version as parse_version
from strawberry.extensions import SchemaExtension
from strawberry.http import GraphQLHTTPResponse as GraphQLHTTPResponse
from strawberry.types import ExecutionContext as ExecutionContext, ExecutionResult as ExecutionResult
from typing import Any, Callable, Generator

class StrawberryIntegration(Integration):
    identifier: str
    async_execution: Incomplete
    def __init__(self, async_execution: bool | None = None) -> None: ...
    @staticmethod
    def setup_once() -> None: ...

class SentryAsyncExtension(SchemaExtension):
    execution_context: Incomplete
    def __init__(self, *, execution_context: ExecutionContext | None = None) -> None: ...
    def hash_query(self, query: str) -> str: ...
    graphql_span: Incomplete
    def on_operation(self) -> Generator[None, None, None]: ...
    validation_span: Incomplete
    def on_validate(self) -> Generator[None, None, None]: ...
    parsing_span: Incomplete
    def on_parse(self) -> Generator[None, None, None]: ...
    def should_skip_tracing(self, _next: Callable[[Any, GraphQLResolveInfo, Any, Any], Any], info: GraphQLResolveInfo) -> bool: ...
    async def resolve(self, _next: Callable[[Any, GraphQLResolveInfo, Any, Any], Any], root: Any, info: GraphQLResolveInfo, *args: str, **kwargs: Any) -> Any: ...

class SentrySyncExtension(SentryAsyncExtension):
    def resolve(self, _next: Callable[[Any, Any, Any, Any], Any], root: Any, info: GraphQLResolveInfo, *args: str, **kwargs: Any) -> Any: ...
