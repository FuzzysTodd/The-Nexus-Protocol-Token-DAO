import grpc
from google.protobuf.message import Message as Message
from grpc import Call as Call, ClientCallDetails as ClientCallDetails
from grpc._interceptor import _UnaryOutcome
from grpc.aio._interceptor import UnaryStreamCall as UnaryStreamCall
from sentry_sdk import Hub as Hub
from sentry_sdk._types import MYPY as MYPY
from sentry_sdk.consts import OP as OP
from sentry_sdk.integrations import DidNotEnable as DidNotEnable
from typing import Any, Callable, Iterable, Iterator

class ClientInterceptor(grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor):
    def intercept_unary_unary(self, continuation: Callable[[ClientCallDetails, Message], _UnaryOutcome], client_call_details: ClientCallDetails, request: Message) -> _UnaryOutcome: ...
    def intercept_unary_stream(self, continuation: Callable[[ClientCallDetails, Message], Iterable[Any] | UnaryStreamCall], client_call_details: ClientCallDetails, request: Message) -> Iterator[Message] | Call: ...
