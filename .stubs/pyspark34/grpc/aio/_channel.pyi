import asyncio
import grpc
from . import _base_call, _base_channel
from ._call import StreamStreamCall as StreamStreamCall, StreamUnaryCall as StreamUnaryCall, UnaryStreamCall as UnaryStreamCall, UnaryUnaryCall as UnaryUnaryCall
from ._interceptor import ClientInterceptor as ClientInterceptor, InterceptedStreamStreamCall as InterceptedStreamStreamCall, InterceptedStreamUnaryCall as InterceptedStreamUnaryCall, InterceptedUnaryStreamCall as InterceptedUnaryStreamCall, InterceptedUnaryUnaryCall as InterceptedUnaryUnaryCall, StreamStreamClientInterceptor as StreamStreamClientInterceptor, StreamUnaryClientInterceptor as StreamUnaryClientInterceptor, UnaryStreamClientInterceptor as UnaryStreamClientInterceptor, UnaryUnaryClientInterceptor as UnaryUnaryClientInterceptor
from ._metadata import Metadata as Metadata
from ._typing import ChannelArgumentType as ChannelArgumentType, DeserializingFunction as DeserializingFunction, RequestIterableType as RequestIterableType, SerializingFunction as SerializingFunction
from grpc._cython import cygrpc as cygrpc
from typing import Any, List, Sequence

class _BaseMultiCallable:
    """Base class of all multi callable objects.

    Handles the initialization logic and stores common attributes.
    """
    def __init__(self, channel: cygrpc.AioChannel, method: bytes, request_serializer: SerializingFunction, response_deserializer: DeserializingFunction, interceptors: Sequence[ClientInterceptor] | None, references: List[Any], loop: asyncio.AbstractEventLoop) -> None: ...

class UnaryUnaryMultiCallable(_BaseMultiCallable, _base_channel.UnaryUnaryMultiCallable):
    def __call__(self, request: Any, *, timeout: float | None = None, metadata: Metadata | None = None, credentials: grpc.CallCredentials | None = None, wait_for_ready: bool | None = None, compression: grpc.Compression | None = None) -> _base_call.UnaryUnaryCall: ...

class UnaryStreamMultiCallable(_BaseMultiCallable, _base_channel.UnaryStreamMultiCallable):
    def __call__(self, request: Any, *, timeout: float | None = None, metadata: Metadata | None = None, credentials: grpc.CallCredentials | None = None, wait_for_ready: bool | None = None, compression: grpc.Compression | None = None) -> _base_call.UnaryStreamCall: ...

class StreamUnaryMultiCallable(_BaseMultiCallable, _base_channel.StreamUnaryMultiCallable):
    def __call__(self, request_iterator: RequestIterableType | None = None, timeout: float | None = None, metadata: Metadata | None = None, credentials: grpc.CallCredentials | None = None, wait_for_ready: bool | None = None, compression: grpc.Compression | None = None) -> _base_call.StreamUnaryCall: ...

class StreamStreamMultiCallable(_BaseMultiCallable, _base_channel.StreamStreamMultiCallable):
    def __call__(self, request_iterator: RequestIterableType | None = None, timeout: float | None = None, metadata: Metadata | None = None, credentials: grpc.CallCredentials | None = None, wait_for_ready: bool | None = None, compression: grpc.Compression | None = None) -> _base_call.StreamStreamCall: ...

class Channel(_base_channel.Channel):
    def __init__(self, target: str, options: ChannelArgumentType, credentials: grpc.ChannelCredentials | None, compression: grpc.Compression | None, interceptors: Sequence[ClientInterceptor] | None) -> None:
        """Constructor.

        Args:
          target: The target to which to connect.
          options: Configuration options for the channel.
          credentials: A cygrpc.ChannelCredentials or None.
          compression: An optional value indicating the compression method to be
            used over the lifetime of the channel.
          interceptors: An optional list of interceptors that would be used for
            intercepting any RPC executed with that channel.
        """
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...
    async def close(self, grace: float | None = None): ...
    def __del__(self) -> None: ...
    def get_state(self, try_to_connect: bool = False) -> grpc.ChannelConnectivity: ...
    async def wait_for_state_change(self, last_observed_state: grpc.ChannelConnectivity) -> None: ...
    async def channel_ready(self) -> None: ...
    def unary_unary(self, method: str, request_serializer: SerializingFunction | None = None, response_deserializer: DeserializingFunction | None = None) -> UnaryUnaryMultiCallable: ...
    def unary_stream(self, method: str, request_serializer: SerializingFunction | None = None, response_deserializer: DeserializingFunction | None = None) -> UnaryStreamMultiCallable: ...
    def stream_unary(self, method: str, request_serializer: SerializingFunction | None = None, response_deserializer: DeserializingFunction | None = None) -> StreamUnaryMultiCallable: ...
    def stream_stream(self, method: str, request_serializer: SerializingFunction | None = None, response_deserializer: DeserializingFunction | None = None) -> StreamStreamMultiCallable: ...

def insecure_channel(target: str, options: ChannelArgumentType | None = None, compression: grpc.Compression | None = None, interceptors: Sequence[ClientInterceptor] | None = None):
    """Creates an insecure asynchronous Channel to a server.

    Args:
      target: The server address
      options: An optional list of key-value pairs (:term:`channel_arguments`
        in gRPC Core runtime) to configure the channel.
      compression: An optional value indicating the compression method to be
        used over the lifetime of the channel.
      interceptors: An optional sequence of interceptors that will be executed for
        any call executed with this channel.

    Returns:
      A Channel.
    """
def secure_channel(target: str, credentials: grpc.ChannelCredentials, options: ChannelArgumentType | None = None, compression: grpc.Compression | None = None, interceptors: Sequence[ClientInterceptor] | None = None):
    """Creates a secure asynchronous Channel to a server.

    Args:
      target: The server address.
      credentials: A ChannelCredentials instance.
      options: An optional list of key-value pairs (:term:`channel_arguments`
        in gRPC Core runtime) to configure the channel.
      compression: An optional value indicating the compression method to be
        used over the lifetime of the channel.
      interceptors: An optional sequence of interceptors that will be executed for
        any call executed with this channel.

    Returns:
      An aio.Channel.
    """
