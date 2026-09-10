import asyncio
import enum
import grpc
from . import _base_call
from ._metadata import Metadata
from ._typing import DeserializingFunction, DoneCallbackType, RequestIterableType, RequestType, ResponseType, SerializingFunction
from grpc._cython import cygrpc
from typing import AsyncIterator

__all__ = ['AioRpcError', 'Call', 'UnaryUnaryCall', 'UnaryStreamCall']

class AioRpcError(grpc.RpcError):
    """An implementation of RpcError to be used by the asynchronous API.

    Raised RpcError is a snapshot of the final status of the RPC, values are
    determined. Hence, its methods no longer needs to be coroutines.
    """
    def __init__(self, code: grpc.StatusCode, initial_metadata: Metadata, trailing_metadata: Metadata, details: str | None = None, debug_error_string: str | None = None) -> None:
        """Constructor.

        Args:
          code: The status code with which the RPC has been finalized.
          details: Optional details explaining the reason of the error.
          initial_metadata: Optional initial metadata that could be sent by the
            Server.
          trailing_metadata: Optional metadata that could be sent by the Server.
        """
    def code(self) -> grpc.StatusCode:
        """Accesses the status code sent by the server.

        Returns:
          The `grpc.StatusCode` status code.
        """
    def details(self) -> str | None:
        """Accesses the details sent by the server.

        Returns:
          The description of the error.
        """
    def initial_metadata(self) -> Metadata:
        """Accesses the initial metadata sent by the server.

        Returns:
          The initial metadata received.
        """
    def trailing_metadata(self) -> Metadata:
        """Accesses the trailing metadata sent by the server.

        Returns:
          The trailing metadata received.
        """
    def debug_error_string(self) -> str:
        """Accesses the debug error string sent by the server.

        Returns:
          The debug error string received.
        """

class Call:
    """Base implementation of client RPC Call object.

    Implements logic around final status, metadata and cancellation.
    """
    def __init__(self, cython_call: cygrpc._AioCall, metadata: Metadata, request_serializer: SerializingFunction, response_deserializer: DeserializingFunction, loop: asyncio.AbstractEventLoop) -> None: ...
    def __del__(self) -> None: ...
    def cancelled(self) -> bool: ...
    def cancel(self) -> bool: ...
    def done(self) -> bool: ...
    def add_done_callback(self, callback: DoneCallbackType) -> None: ...
    def time_remaining(self) -> float | None: ...
    async def initial_metadata(self) -> Metadata: ...
    async def trailing_metadata(self) -> Metadata: ...
    async def code(self) -> grpc.StatusCode: ...
    async def details(self) -> str: ...
    async def debug_error_string(self) -> str: ...

class _APIStyle(enum.IntEnum):
    UNKNOWN: int
    ASYNC_GENERATOR: int
    READER_WRITER: int

class _UnaryResponseMixin(Call):
    def cancel(self) -> bool: ...
    def __await__(self) -> ResponseType:
        """Wait till the ongoing RPC request finishes."""

class _StreamResponseMixin(Call):
    def cancel(self) -> bool: ...
    def __aiter__(self) -> AsyncIterator[ResponseType]: ...
    async def read(self) -> ResponseType: ...

class _StreamRequestMixin(Call):
    def cancel(self) -> bool: ...
    async def write(self, request: RequestType) -> None: ...
    async def done_writing(self) -> None:
        """Signal peer that client is done writing.

        This method is idempotent.
        """
    async def wait_for_connection(self) -> None: ...

class UnaryUnaryCall(_UnaryResponseMixin, Call, _base_call.UnaryUnaryCall):
    """Object for managing unary-unary RPC calls.

    Returned when an instance of `UnaryUnaryMultiCallable` object is called.
    """
    def __init__(self, request: RequestType, deadline: float | None, metadata: Metadata, credentials: grpc.CallCredentials | None, wait_for_ready: bool | None, channel: cygrpc.AioChannel, method: bytes, request_serializer: SerializingFunction, response_deserializer: DeserializingFunction, loop: asyncio.AbstractEventLoop) -> None: ...
    async def wait_for_connection(self) -> None: ...

class UnaryStreamCall(_StreamResponseMixin, Call, _base_call.UnaryStreamCall):
    """Object for managing unary-stream RPC calls.

    Returned when an instance of `UnaryStreamMultiCallable` object is called.
    """
    def __init__(self, request: RequestType, deadline: float | None, metadata: Metadata, credentials: grpc.CallCredentials | None, wait_for_ready: bool | None, channel: cygrpc.AioChannel, method: bytes, request_serializer: SerializingFunction, response_deserializer: DeserializingFunction, loop: asyncio.AbstractEventLoop) -> None: ...
    async def wait_for_connection(self) -> None: ...

class StreamUnaryCall(_StreamRequestMixin, _UnaryResponseMixin, Call, _base_call.StreamUnaryCall):
    """Object for managing stream-unary RPC calls.

    Returned when an instance of `StreamUnaryMultiCallable` object is called.
    """
    def __init__(self, request_iterator: RequestIterableType | None, deadline: float | None, metadata: Metadata, credentials: grpc.CallCredentials | None, wait_for_ready: bool | None, channel: cygrpc.AioChannel, method: bytes, request_serializer: SerializingFunction, response_deserializer: DeserializingFunction, loop: asyncio.AbstractEventLoop) -> None: ...

class StreamStreamCall(_StreamRequestMixin, _StreamResponseMixin, Call, _base_call.StreamStreamCall):
    """Object for managing stream-stream RPC calls.

    Returned when an instance of `StreamStreamMultiCallable` object is called.
    """
    def __init__(self, request_iterator: RequestIterableType | None, deadline: float | None, metadata: Metadata, credentials: grpc.CallCredentials | None, wait_for_ready: bool | None, channel: cygrpc.AioChannel, method: bytes, request_serializer: SerializingFunction, response_deserializer: DeserializingFunction, loop: asyncio.AbstractEventLoop) -> None: ...
