import asyncio
import grpc
from . import _base_call
from ._call import AioRpcError as AioRpcError, StreamStreamCall as StreamStreamCall, StreamUnaryCall as StreamUnaryCall, UnaryStreamCall as UnaryStreamCall, UnaryUnaryCall as UnaryUnaryCall
from ._metadata import Metadata as Metadata
from ._typing import DeserializingFunction as DeserializingFunction, DoneCallbackType as DoneCallbackType, RequestIterableType as RequestIterableType, RequestType as RequestType, ResponseIterableType as ResponseIterableType, ResponseType as ResponseType, SerializingFunction as SerializingFunction
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from collections.abc import Generator
from grpc._cython import cygrpc as cygrpc
from typing import AsyncIterable, Awaitable, Callable, NamedTuple, Sequence

class ServerInterceptor(metaclass=ABCMeta):
    """Affords intercepting incoming RPCs on the service-side.

    This is an EXPERIMENTAL API.
    """
    @abstractmethod
    async def intercept_service(self, continuation: Callable[[grpc.HandlerCallDetails], Awaitable[grpc.RpcMethodHandler]], handler_call_details: grpc.HandlerCallDetails) -> grpc.RpcMethodHandler:
        """Intercepts incoming RPCs before handing them over to a handler.

        Args:
            continuation: A function that takes a HandlerCallDetails and
                proceeds to invoke the next interceptor in the chain, if any,
                or the RPC handler lookup logic, with the call details passed
                as an argument, and returns an RpcMethodHandler instance if
                the RPC is considered serviced, or None otherwise.
            handler_call_details: A HandlerCallDetails describing the RPC.

        Returns:
            An RpcMethodHandler with which the RPC may be serviced if the
            interceptor chooses to service this RPC, or None otherwise.
        """

class ClientCallDetails(NamedTuple('ClientCallDetails', [('method', Incomplete), ('timeout', Incomplete), ('metadata', Incomplete), ('credentials', Incomplete), ('wait_for_ready', Incomplete)]), grpc.ClientCallDetails):
    """Describes an RPC to be invoked.

    This is an EXPERIMENTAL API.

    Args:
        method: The method name of the RPC.
        timeout: An optional duration of time in seconds to allow for the RPC.
        metadata: Optional metadata to be transmitted to the service-side of
          the RPC.
        credentials: An optional CallCredentials for the RPC.
        wait_for_ready: An optional flag to enable :term:`wait_for_ready` mechanism.
    """
    method: str
    timeout: float | None
    metadata: Metadata | None
    credentials: grpc.CallCredentials | None
    wait_for_ready: bool | None

class ClientInterceptor(metaclass=ABCMeta):
    """Base class used for all Aio Client Interceptor classes"""

class UnaryUnaryClientInterceptor(ClientInterceptor, metaclass=ABCMeta):
    """Affords intercepting unary-unary invocations."""
    @abstractmethod
    async def intercept_unary_unary(self, continuation: Callable[[ClientCallDetails, RequestType], UnaryUnaryCall], client_call_details: ClientCallDetails, request: RequestType) -> UnaryUnaryCall | ResponseType:
        """Intercepts a unary-unary invocation asynchronously.

        Args:
          continuation: A coroutine that proceeds with the invocation by
            executing the next interceptor in the chain or invoking the
            actual RPC on the underlying Channel. It is the interceptor's
            responsibility to call it if it decides to move the RPC forward.
            The interceptor can use
            `call = await continuation(client_call_details, request)`
            to continue with the RPC. `continuation` returns the call to the
            RPC.
          client_call_details: A ClientCallDetails object describing the
            outgoing RPC.
          request: The request value for the RPC.

        Returns:
          An object with the RPC response.

        Raises:
          AioRpcError: Indicating that the RPC terminated with non-OK status.
          asyncio.CancelledError: Indicating that the RPC was canceled.
        """

class UnaryStreamClientInterceptor(ClientInterceptor, metaclass=ABCMeta):
    """Affords intercepting unary-stream invocations."""
    @abstractmethod
    async def intercept_unary_stream(self, continuation: Callable[[ClientCallDetails, RequestType], UnaryStreamCall], client_call_details: ClientCallDetails, request: RequestType) -> ResponseIterableType | UnaryStreamCall:
        """Intercepts a unary-stream invocation asynchronously.

        The function could return the call object or an asynchronous
        iterator, in case of being an asyncrhonous iterator this will
        become the source of the reads done by the caller.

        Args:
          continuation: A coroutine that proceeds with the invocation by
            executing the next interceptor in the chain or invoking the
            actual RPC on the underlying Channel. It is the interceptor's
            responsibility to call it if it decides to move the RPC forward.
            The interceptor can use
            `call = await continuation(client_call_details, request)`
            to continue with the RPC. `continuation` returns the call to the
            RPC.
          client_call_details: A ClientCallDetails object describing the
            outgoing RPC.
          request: The request value for the RPC.

        Returns:
          The RPC Call or an asynchronous iterator.

        Raises:
          AioRpcError: Indicating that the RPC terminated with non-OK status.
          asyncio.CancelledError: Indicating that the RPC was canceled.
        """

class StreamUnaryClientInterceptor(ClientInterceptor, metaclass=ABCMeta):
    """Affords intercepting stream-unary invocations."""
    @abstractmethod
    async def intercept_stream_unary(self, continuation: Callable[[ClientCallDetails, RequestType], StreamUnaryCall], client_call_details: ClientCallDetails, request_iterator: RequestIterableType) -> StreamUnaryCall:
        """Intercepts a stream-unary invocation asynchronously.

        Within the interceptor the usage of the call methods like `write` or
        even awaiting the call should be done carefully, since the caller
        could be expecting an untouched call, for example for start writing
        messages to it.

        Args:
          continuation: A coroutine that proceeds with the invocation by
            executing the next interceptor in the chain or invoking the
            actual RPC on the underlying Channel. It is the interceptor's
            responsibility to call it if it decides to move the RPC forward.
            The interceptor can use
            `call = await continuation(client_call_details, request_iterator)`
            to continue with the RPC. `continuation` returns the call to the
            RPC.
          client_call_details: A ClientCallDetails object describing the
            outgoing RPC.
          request_iterator: The request iterator that will produce requests
            for the RPC.

        Returns:
          The RPC Call.

        Raises:
          AioRpcError: Indicating that the RPC terminated with non-OK status.
          asyncio.CancelledError: Indicating that the RPC was canceled.
        """

class StreamStreamClientInterceptor(ClientInterceptor, metaclass=ABCMeta):
    """Affords intercepting stream-stream invocations."""
    @abstractmethod
    async def intercept_stream_stream(self, continuation: Callable[[ClientCallDetails, RequestType], StreamStreamCall], client_call_details: ClientCallDetails, request_iterator: RequestIterableType) -> ResponseIterableType | StreamStreamCall:
        """Intercepts a stream-stream invocation asynchronously.

        Within the interceptor the usage of the call methods like `write` or
        even awaiting the call should be done carefully, since the caller
        could be expecting an untouched call, for example for start writing
        messages to it.

        The function could return the call object or an asynchronous
        iterator, in case of being an asyncrhonous iterator this will
        become the source of the reads done by the caller.

        Args:
          continuation: A coroutine that proceeds with the invocation by
            executing the next interceptor in the chain or invoking the
            actual RPC on the underlying Channel. It is the interceptor's
            responsibility to call it if it decides to move the RPC forward.
            The interceptor can use
            `call = await continuation(client_call_details, request_iterator)`
            to continue with the RPC. `continuation` returns the call to the
            RPC.
          client_call_details: A ClientCallDetails object describing the
            outgoing RPC.
          request_iterator: The request iterator that will produce requests
            for the RPC.

        Returns:
          The RPC Call or an asynchronous iterator.

        Raises:
          AioRpcError: Indicating that the RPC terminated with non-OK status.
          asyncio.CancelledError: Indicating that the RPC was canceled.
        """

class InterceptedCall:
    """Base implementation for all intercepted call arities.

    Interceptors might have some work to do before the RPC invocation with
    the capacity of changing the invocation parameters, and some work to do
    after the RPC invocation with the capacity for accessing to the wrapped
    `UnaryUnaryCall`.

    It handles also early and later cancellations, when the RPC has not even
    started and the execution is still held by the interceptors or when the
    RPC has finished but again the execution is still held by the interceptors.

    Once the RPC is finally executed, all methods are finally done against the
    intercepted call, being at the same time the same call returned to the
    interceptors.

    As a base class for all of the interceptors implements the logic around
    final status, metadata and cancellation.
    """
    def __init__(self, interceptors_task: asyncio.Task) -> None: ...
    def __del__(self) -> None: ...
    def cancel(self) -> bool: ...
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...
    def add_done_callback(self, callback: DoneCallbackType) -> None: ...
    def time_remaining(self) -> float | None: ...
    async def initial_metadata(self) -> Metadata | None: ...
    async def trailing_metadata(self) -> Metadata | None: ...
    async def code(self) -> grpc.StatusCode: ...
    async def details(self) -> str: ...
    async def debug_error_string(self) -> str | None: ...
    async def wait_for_connection(self) -> None: ...

class _InterceptedUnaryResponseMixin:
    def __await__(self) -> Generator[Incomplete, Incomplete, Incomplete]: ...

class _InterceptedStreamResponseMixin:
    def __aiter__(self) -> AsyncIterable[ResponseType]: ...
    async def read(self) -> ResponseType: ...

class _InterceptedStreamRequestMixin:
    async def write(self, request: RequestType) -> None: ...
    async def done_writing(self) -> None:
        """Signal peer that client is done writing.

        This method is idempotent.
        """

class InterceptedUnaryUnaryCall(_InterceptedUnaryResponseMixin, InterceptedCall, _base_call.UnaryUnaryCall):
    """Used for running a `UnaryUnaryCall` wrapped by interceptors.

    For the `__await__` method is it is proxied to the intercepted call only when
    the interceptor task is finished.
    """
    def __init__(self, interceptors: Sequence[UnaryUnaryClientInterceptor], request: RequestType, timeout: float | None, metadata: Metadata, credentials: grpc.CallCredentials | None, wait_for_ready: bool | None, channel: cygrpc.AioChannel, method: bytes, request_serializer: SerializingFunction, response_deserializer: DeserializingFunction, loop: asyncio.AbstractEventLoop) -> None: ...
    def time_remaining(self) -> float | None: ...

class InterceptedUnaryStreamCall(_InterceptedStreamResponseMixin, InterceptedCall, _base_call.UnaryStreamCall):
    """Used for running a `UnaryStreamCall` wrapped by interceptors."""
    def __init__(self, interceptors: Sequence[UnaryStreamClientInterceptor], request: RequestType, timeout: float | None, metadata: Metadata, credentials: grpc.CallCredentials | None, wait_for_ready: bool | None, channel: cygrpc.AioChannel, method: bytes, request_serializer: SerializingFunction, response_deserializer: DeserializingFunction, loop: asyncio.AbstractEventLoop) -> None: ...
    def time_remaining(self) -> float | None: ...

class InterceptedStreamUnaryCall(_InterceptedUnaryResponseMixin, _InterceptedStreamRequestMixin, InterceptedCall, _base_call.StreamUnaryCall):
    """Used for running a `StreamUnaryCall` wrapped by interceptors.

    For the `__await__` method is it is proxied to the intercepted call only when
    the interceptor task is finished.
    """
    def __init__(self, interceptors: Sequence[StreamUnaryClientInterceptor], request_iterator: RequestIterableType | None, timeout: float | None, metadata: Metadata, credentials: grpc.CallCredentials | None, wait_for_ready: bool | None, channel: cygrpc.AioChannel, method: bytes, request_serializer: SerializingFunction, response_deserializer: DeserializingFunction, loop: asyncio.AbstractEventLoop) -> None: ...
    def time_remaining(self) -> float | None: ...

class InterceptedStreamStreamCall(_InterceptedStreamResponseMixin, _InterceptedStreamRequestMixin, InterceptedCall, _base_call.StreamStreamCall):
    """Used for running a `StreamStreamCall` wrapped by interceptors."""
    def __init__(self, interceptors: Sequence[StreamStreamClientInterceptor], request_iterator: RequestIterableType | None, timeout: float | None, metadata: Metadata, credentials: grpc.CallCredentials | None, wait_for_ready: bool | None, channel: cygrpc.AioChannel, method: bytes, request_serializer: SerializingFunction, response_deserializer: DeserializingFunction, loop: asyncio.AbstractEventLoop) -> None: ...
    def time_remaining(self) -> float | None: ...

class UnaryUnaryCallResponse(_base_call.UnaryUnaryCall):
    """Final UnaryUnaryCall class finished with a response."""
    def __init__(self, response: ResponseType) -> None: ...
    def cancel(self) -> bool: ...
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...
    def add_done_callback(self, unused_callback) -> None: ...
    def time_remaining(self) -> float | None: ...
    async def initial_metadata(self) -> Metadata | None: ...
    async def trailing_metadata(self) -> Metadata | None: ...
    async def code(self) -> grpc.StatusCode: ...
    async def details(self) -> str: ...
    async def debug_error_string(self) -> str | None: ...
    def __await__(self) -> Generator[None, None, Incomplete]: ...
    async def wait_for_connection(self) -> None: ...

class _StreamCallResponseIterator:
    def __init__(self, call: _base_call.UnaryStreamCall | _base_call.StreamStreamCall, response_iterator: AsyncIterable[ResponseType]) -> None: ...
    def cancel(self) -> bool: ...
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...
    def add_done_callback(self, callback) -> None: ...
    def time_remaining(self) -> float | None: ...
    async def initial_metadata(self) -> Metadata | None: ...
    async def trailing_metadata(self) -> Metadata | None: ...
    async def code(self) -> grpc.StatusCode: ...
    async def details(self) -> str: ...
    async def debug_error_string(self) -> str | None: ...
    def __aiter__(self): ...
    async def wait_for_connection(self) -> None: ...

class UnaryStreamCallResponseIterator(_StreamCallResponseIterator, _base_call.UnaryStreamCall):
    """UnaryStreamCall class wich uses an alternative response iterator."""
    async def read(self) -> ResponseType: ...

class StreamStreamCallResponseIterator(_StreamCallResponseIterator, _base_call.StreamStreamCall):
    """StreamStreamCall class wich uses an alternative response iterator."""
    async def read(self) -> ResponseType: ...
    async def write(self, request: RequestType) -> None: ...
    async def done_writing(self) -> None: ...
