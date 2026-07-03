from _typeshed import Incomplete
from gql.transport import AsyncTransport as AsyncTransport, Transport as Transport
from graphql import DocumentNode as DocumentNode, VariableDefinitionNode
from sentry_sdk._types import EventProcessor as EventProcessor, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.utils import event_from_exception as event_from_exception, parse_version as parse_version
from typing import Dict, Tuple

EventDataType = Dict[str, str | Tuple[VariableDefinitionNode, ...]]
MIN_GQL_VERSION: Incomplete

class GQLIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...
