import abc
import grpc
import threading
import types
from _typeshed import Incomplete
from grpc._cython import cygrpc as cygrpc
from grpc._typing import ChannelArgumentType as ChannelArgumentType, DeserializingFunction as DeserializingFunction, IntegratedCallFactory as IntegratedCallFactory, MetadataType as MetadataType, NullaryCallbackType as NullaryCallbackType, ResponseType as ResponseType, SerializingFunction as SerializingFunction, UserTag as UserTag
from typing import Any, Callable, Iterator, List, Sequence, Set, Tuple

class _RPCState:
    condition: threading.Condition
    due: Set[cygrpc.OperationType]
    initial_metadata: MetadataType | None
    response: Any
    trailing_metadata: MetadataType | None
    code: grpc.StatusCode | None
    details: str | None
    debug_error_string: str | None
    cancelled: bool
    callbacks: List[NullaryCallbackType]
    fork_epoch: int | None
    def __init__(self, due: Sequence[cygrpc.OperationType], initial_metadata: MetadataType | None, trailing_metadata: MetadataType | None, code: grpc.StatusCode | None, details: str | None) -> None: ...
    def reset_postfork_child(self) -> None: ...

class _InactiveRpcError(grpc.RpcError, grpc.Call, grpc.Future, metaclass=abc.ABCMeta):
    """An RPC error not tied to the execution of a particular RPC.

    The RPC represented by the state object must not be in-progress or
    cancelled.

    Attributes:
      _state: An instance of _RPCState.
    """
    def __init__(self, state: _RPCState) -> None: ...
    def initial_metadata(self) -> MetadataType | None: ...
    def trailing_metadata(self) -> MetadataType | None: ...
    def code(self) -> grpc.StatusCode | None: ...
    def details(self) -> str | None: ...
    def debug_error_string(self) -> str | None: ...
    def cancel(self) -> bool:
        """See grpc.Future.cancel."""
    def cancelled(self) -> bool:
        """See grpc.Future.cancelled."""
    def running(self) -> bool:
        """See grpc.Future.running."""
    def done(self) -> bool:
        """See grpc.Future.done."""
    def result(self, timeout: float | None = None) -> Any:
        """See grpc.Future.result."""
    def exception(self, timeout: float | None = None) -> Exception | None:
        """See grpc.Future.exception."""
    def traceback(self, timeout: float | None = None) -> types.TracebackType | None:
        """See grpc.Future.traceback."""
    def add_done_callback(self, fn: Callable[[grpc.Future], None], timeout: float | None = None) -> None:
        """See grpc.Future.add_done_callback."""

class _Rendezvous(grpc.RpcError, grpc.RpcContext):
    """An RPC iterator.

    Attributes:
      _state: An instance of _RPCState.
      _call: An instance of SegregatedCall or IntegratedCall.
        In either case, the _call object is expected to have operate, cancel,
        and next_event methods.
      _response_deserializer: A callable taking bytes and return a Python
        object.
      _deadline: A float representing the deadline of the RPC in seconds. Or
        possibly None, to represent an RPC with no deadline at all.
    """
    def __init__(self, state: _RPCState, call: cygrpc.SegregatedCall | cygrpc.IntegratedCall, response_deserializer: DeserializingFunction | None, deadline: float | None) -> None: ...
    def is_active(self) -> bool:
        """See grpc.RpcContext.is_active"""
    def time_remaining(self) -> float | None:
        """See grpc.RpcContext.time_remaining"""
    def cancel(self) -> bool:
        """See grpc.RpcContext.cancel"""
    def add_callback(self, callback: NullaryCallbackType) -> bool:
        """See grpc.RpcContext.add_callback"""
    def __iter__(self): ...
    def next(self): ...
    def __next__(self): ...
    def debug_error_string(self) -> str | None: ...
    def __del__(self) -> None: ...

class _SingleThreadedRendezvous(_Rendezvous, grpc.Call, grpc.Future):
    '''An RPC iterator operating entirely on a single thread.

    The __next__ method of _SingleThreadedRendezvous does not depend on the
    existence of any other thread, including the "channel spin thread".
    However, this means that its interface is entirely synchronous. So this
    class cannot completely fulfill the grpc.Future interface. The result,
    exception, and traceback methods will never block and will instead raise
    an exception if calling the method would result in blocking.

    This means that these methods are safe to call from add_done_callback
    handlers.
    '''
    def cancelled(self) -> bool: ...
    def running(self) -> bool: ...
    def done(self) -> bool: ...
    def result(self, timeout: float | None = None) -> Any:
        """Returns the result of the computation or raises its exception.

        This method will never block. Instead, it will raise an exception
        if calling this method would otherwise result in blocking.

        Since this method will never block, any `timeout` argument passed will
        be ignored.
        """
    def exception(self, timeout: float | None = None) -> Exception | None:
        """Return the exception raised by the computation.

        This method will never block. Instead, it will raise an exception
        if calling this method would otherwise result in blocking.

        Since this method will never block, any `timeout` argument passed will
        be ignored.
        """
    def traceback(self, timeout: float | None = None) -> types.TracebackType | None:
        """Access the traceback of the exception raised by the computation.

        This method will never block. Instead, it will raise an exception
        if calling this method would otherwise result in blocking.

        Since this method will never block, any `timeout` argument passed will
        be ignored.
        """
    def add_done_callback(self, fn: Callable[[grpc.Future], None]) -> None: ...
    def initial_metadata(self) -> MetadataType | None:
        """See grpc.Call.initial_metadata"""
    def trailing_metadata(self) -> MetadataType | None:
        """See grpc.Call.trailing_metadata"""
    def code(self) -> grpc.StatusCode | None:
        """See grpc.Call.code"""
    def details(self) -> str | None:
        """See grpc.Call.details"""
    def debug_error_string(self) -> str | None: ...

class _MultiThreadedRendezvous(_Rendezvous, grpc.Call, grpc.Future):
    """An RPC iterator that depends on a channel spin thread.

    This iterator relies upon a per-channel thread running in the background,
    dequeueing events from the completion queue, and notifying threads waiting
    on the threading.Condition object in the _RPCState object.

    This extra thread allows _MultiThreadedRendezvous to fulfill the grpc.Future interface
    and to mediate a bidirection streaming RPC.
    """
    def initial_metadata(self) -> MetadataType | None:
        """See grpc.Call.initial_metadata"""
    def trailing_metadata(self) -> MetadataType | None:
        """See grpc.Call.trailing_metadata"""
    def code(self) -> grpc.StatusCode | None:
        """See grpc.Call.code"""
    def details(self) -> str | None:
        """See grpc.Call.details"""
    def debug_error_string(self) -> str | None: ...
    def cancelled(self) -> bool: ...
    def running(self) -> bool: ...
    def done(self) -> bool: ...
    def result(self, timeout: float | None = None) -> Any:
        """Returns the result of the computation or raises its exception.

        See grpc.Future.result for the full API contract.
        """
    def exception(self, timeout: float | None = None) -> Exception | None:
        """Return the exception raised by the computation.

        See grpc.Future.exception for the full API contract.
        """
    def traceback(self, timeout: float | None = None) -> types.TracebackType | None:
        """Access the traceback of the exception raised by the computation.

        See grpc.future.traceback for the full API contract.
        """
    def add_done_callback(self, fn: Callable[[grpc.Future], None]) -> None: ...

class _UnaryUnaryMultiCallable(grpc.UnaryUnaryMultiCallable):
    def __init__(self, channel: cygrpc.Channel, managed_call: IntegratedCallFactory, method: bytes, request_serializer: SerializingFunction | None, response_deserializer: DeserializingFunction | None) -> None: ...
    def __call__(self, request: Any, timeout: float | None = None, metadata: MetadataType | None = None, credentials: grpc.CallCredentials | None = None, wait_for_ready: bool | None = None, compression: grpc.Compression | None = None) -> Any: ...
    def with_call(self, request: Any, timeout: float | None = None, metadata: MetadataType | None = None, credentials: grpc.CallCredentials | None = None, wait_for_ready: bool | None = None, compression: grpc.Compression | None = None) -> Tuple[Any, grpc.Call]: ...
    def future(self, request: Any, timeout: float | None = None, metadata: MetadataType | None = None, credentials: grpc.CallCredentials | None = None, wait_for_ready: bool | None = None, compression: grpc.Compression | None = None) -> _MultiThreadedRendezvous: ...

class _SingleThreadedUnaryStreamMultiCallable(grpc.UnaryStreamMultiCallable):
    def __init__(self, channel: cygrpc.Channel, method: bytes, request_serializer: SerializingFunction, response_deserializer: DeserializingFunction) -> None: ...
    def __call__(self, request: Any, timeout: float | None = None, metadata: MetadataType | None = None, credentials: grpc.CallCredentials | None = None, wait_for_ready: bool | None = None, compression: grpc.Compression | None = None) -> _SingleThreadedRendezvous: ...

class _UnaryStreamMultiCallable(grpc.UnaryStreamMultiCallable):
    def __init__(self, channel: cygrpc.Channel, managed_call: IntegratedCallFactory, method: bytes, request_serializer: SerializingFunction, response_deserializer: DeserializingFunction) -> None: ...
    def __call__(self, request: Any, timeout: float | None = None, metadata: MetadataType | None = None, credentials: grpc.CallCredentials | None = None, wait_for_ready: bool | None = None, compression: grpc.Compression | None = None) -> _MultiThreadedRendezvous: ...

class _StreamUnaryMultiCallable(grpc.StreamUnaryMultiCallable):
    def __init__(self, channel: cygrpc.Channel, managed_call: IntegratedCallFactory, method: bytes, request_serializer: SerializingFunction | None, response_deserializer: DeserializingFunction | None) -> None: ...
    def __call__(self, request_iterator: Iterator, timeout: float | None = None, metadata: MetadataType | None = None, credentials: grpc.CallCredentials | None = None, wait_for_ready: bool | None = None, compression: grpc.Compression | None = None) -> Any: ...
    def with_call(self, request_iterator: Iterator, timeout: float | None = None, metadata: MetadataType | None = None, credentials: grpc.CallCredentials | None = None, wait_for_ready: bool | None = None, compression: grpc.Compression | None = None) -> Tuple[Any, grpc.Call]: ...
    def future(self, request_iterator: Iterator, timeout: float | None = None, metadata: MetadataType | None = None, credentials: grpc.CallCredentials | None = None, wait_for_ready: bool | None = None, compression: grpc.Compression | None = None) -> _MultiThreadedRendezvous: ...

class _StreamStreamMultiCallable(grpc.StreamStreamMultiCallable):
    def __init__(self, channel: cygrpc.Channel, managed_call: IntegratedCallFactory, method: bytes, request_serializer: SerializingFunction | None = None, response_deserializer: DeserializingFunction | None = None) -> None: ...
    def __call__(self, request_iterator: Iterator, timeout: float | None = None, metadata: MetadataType | None = None, credentials: grpc.CallCredentials | None = None, wait_for_ready: bool | None = None, compression: grpc.Compression | None = None) -> _MultiThreadedRendezvous: ...

class _InitialMetadataFlags(int):
    """Stores immutable initial metadata flags"""
    def __new__(cls, value: int = ...): ...
    def with_wait_for_ready(self, wait_for_ready: bool | None) -> int: ...

class _ChannelCallState:
    channel: cygrpc.Channel
    managed_calls: int
    threading: bool
    lock: Incomplete
    def __init__(self, channel: cygrpc.Channel) -> None: ...
    def reset_postfork_child(self) -> None: ...
    def __del__(self) -> None: ...

class _ChannelConnectivityState:
    lock: threading.RLock
    channel: grpc.Channel
    polling: bool
    connectivity: grpc.ChannelConnectivity
    try_to_connect: bool
    callbacks_and_connectivities: List[Sequence[Callable[[grpc.ChannelConnectivity], None] | grpc.ChannelConnectivity | None]]
    delivering: bool
    def __init__(self, channel: grpc.Channel) -> None: ...
    def reset_postfork_child(self) -> None: ...

class Channel(grpc.Channel):
    """A cygrpc.Channel-backed implementation of grpc.Channel."""
    def __init__(self, target: str, options: Sequence[ChannelArgumentType], credentials: grpc.ChannelCredentials | None, compression: grpc.Compression | None) -> None:
        """Constructor.

        Args:
          target: The target to which to connect.
          options: Configuration options for the channel.
          credentials: A cygrpc.ChannelCredentials or None.
          compression: An optional value indicating the compression method to be
            used over the lifetime of the channel.
        """
    def subscribe(self, callback: Callable[[grpc.ChannelConnectivity], None], try_to_connect: bool | None = None) -> None: ...
    def unsubscribe(self, callback: Callable[[grpc.ChannelConnectivity], None]) -> None: ...
    def unary_unary(self, method: str, request_serializer: SerializingFunction | None = None, response_deserializer: DeserializingFunction | None = None) -> grpc.UnaryUnaryMultiCallable: ...
    def unary_stream(self, method: str, request_serializer: SerializingFunction | None = None, response_deserializer: DeserializingFunction | None = None) -> grpc.UnaryStreamMultiCallable: ...
    def stream_unary(self, method: str, request_serializer: SerializingFunction | None = None, response_deserializer: DeserializingFunction | None = None) -> grpc.StreamUnaryMultiCallable: ...
    def stream_stream(self, method: str, request_serializer: SerializingFunction | None = None, response_deserializer: DeserializingFunction | None = None) -> grpc.StreamStreamMultiCallable: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None): ...
    def close(self) -> None: ...
    def __del__(self) -> None: ...
