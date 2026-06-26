import grpc
from google.protobuf.message import Message as Message
from grpc import HandlerCallDetails as HandlerCallDetails, RpcMethodHandler as RpcMethodHandler, ServicerContext as ServicerContext
from sentry_sdk import Hub as Hub
from sentry_sdk._types import MYPY as MYPY
from sentry_sdk.consts import OP as OP
from sentry_sdk.integrations import DidNotEnable as DidNotEnable
from sentry_sdk.tracing import TRANSACTION_SOURCE_CUSTOM as TRANSACTION_SOURCE_CUSTOM, Transaction as Transaction
from typing import Callable

class ServerInterceptor(grpc.ServerInterceptor):
    def __init__(self, find_name: Callable[[ServicerContext], str] | None = None) -> None: ...
    def intercept_service(self, continuation: Callable[[HandlerCallDetails], RpcMethodHandler], handler_call_details: HandlerCallDetails) -> RpcMethodHandler: ...
