from _typeshed import Incomplete
from ariadne.types import GraphQLError as GraphQLError, GraphQLResult as GraphQLResult, GraphQLSchema as GraphQLSchema, QueryParser as QueryParser
from graphql.language.ast import DocumentNode as DocumentNode
from sentry_sdk._types import EventProcessor as EventProcessor, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.integrations._wsgi_common import request_body_within_bounds as request_body_within_bounds
from sentry_sdk.integrations.logging import ignore_logger as ignore_logger
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, event_from_exception as event_from_exception, parse_version as parse_version

ariadne_graphql: Incomplete

class AriadneIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...
