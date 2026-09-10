from _typeshed import Incomplete
from grpc._cython import cygrpc as cygrpc
from grpc._typing import DeserializingFunction as DeserializingFunction, SerializingFunction as SerializingFunction
from typing import Any, AnyStr, Callable

CYGRPC_CONNECTIVITY_STATE_TO_CHANNEL_CONNECTIVITY: Incomplete
CYGRPC_STATUS_CODE_TO_STATUS_CODE: Incomplete
STATUS_CODE_TO_CYGRPC_STATUS_CODE: Incomplete
MAXIMUM_WAIT_TIMEOUT: float

def encode(s: AnyStr) -> bytes: ...
def decode(b: AnyStr) -> str: ...
def serialize(message: Any, serializer: SerializingFunction | None) -> bytes: ...
def deserialize(serialized_message: bytes, deserializer: DeserializingFunction | None) -> Any: ...
def fully_qualified_method(group: str, method: str) -> str: ...
def wait(wait_fn: Callable[..., bool], wait_complete_fn: Callable[[], bool], timeout: float | None = None, spin_cb: Callable[[], None] | None = None) -> bool:
    """Blocks waiting for an event without blocking the thread indefinitely.

    See https://github.com/grpc/grpc/issues/19464 for full context. CPython's
    `threading.Event.wait` and `threading.Condition.wait` methods, if invoked
    without a timeout kwarg, may block the calling thread indefinitely. If the
    call is made from the main thread, this means that signal handlers may not
    run for an arbitrarily long period of time.

    This wrapper calls the supplied wait function with an arbitrary short
    timeout to ensure that no signal handler has to wait longer than
    MAXIMUM_WAIT_TIMEOUT before executing.

    Args:
      wait_fn: A callable acceptable a single float-valued kwarg named
        `timeout`. This function is expected to be one of `threading.Event.wait`
        or `threading.Condition.wait`.
      wait_complete_fn: A callable taking no arguments and returning a bool.
        When this function returns true, it indicates that waiting should cease.
      timeout: An optional float-valued number of seconds after which the wait
        should cease.
      spin_cb: An optional Callable taking no arguments and returning nothing.
        This callback will be called on each iteration of the spin. This may be
        used for, e.g. work related to forking.

    Returns:
      True if a timeout was supplied and it was reached. False otherwise.
    """
def validate_port_binding_result(address: str, port: int) -> int:
    """Validates if the port binding succeed.

    If the port returned by Core is 0, the binding is failed. However, in that
    case, the Core API doesn't return a detailed failing reason. The best we
    can do is raising an exception to prevent further confusion.

    Args:
        address: The address string to be bound.
        port: An int returned by core
    """
