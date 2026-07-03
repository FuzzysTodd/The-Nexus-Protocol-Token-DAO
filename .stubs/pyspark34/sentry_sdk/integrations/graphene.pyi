from graphene.language.source import Source as Source
from graphql.execution import ExecutionResult as ExecutionResult
from graphql.type import GraphQLSchema as GraphQLSchema
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception, parse_version as parse_version

class GrapheneIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...
