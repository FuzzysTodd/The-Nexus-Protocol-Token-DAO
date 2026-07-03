import zmq as _zmq
from _typeshed import Incomplete
from asyncio import Future
from typing import Any, Awaitable, Dict, List, NamedTuple, Tuple, TypeVar, overload
from zmq import EVENTS as EVENTS, POLLIN as POLLIN, POLLOUT as POLLOUT
from zmq._typing import Literal as Literal

class _FutureEvent(NamedTuple):
    future: Future
    kind: str
    kwargs: Dict
    msg: Any
    timer: Any

class _Async:
    """Mixin for common async logic"""

class _AsyncPoller(_Async, _zmq.Poller):
    """Poller that returns a Future on poll, instead of blocking."""
    raw_sockets: List[Any]
    def poll(self, timeout: int = -1) -> Awaitable[List[Tuple[Any, int]]]:
        """Return a Future for a poll event"""

class _NoTimer:
    @staticmethod
    def cancel() -> None: ...
T = TypeVar('T', bound='_AsyncSocket')

class _AsyncSocket(_Async, _zmq.Socket[Future]):
    def __init__(self, context: Incomplete | None = None, socket_type: int = -1, io_loop: Incomplete | None = None, _from_socket: _zmq.Socket | None = None, **kwargs) -> None: ...
    @classmethod
    def from_socket(cls, socket: _zmq.Socket, io_loop: Any = None) -> T:
        """Create an async socket from an existing Socket"""
    def close(self, linger: int | None = None) -> None: ...
    def get(self, key): ...
    @overload
    def recv_multipart(self, flags: int = 0, *, track: bool = False) -> Awaitable[List[bytes]]: ...
    @overload
    def recv_multipart(self, flags: int = 0, *, copy: Literal[True], track: bool = False) -> Awaitable[List[bytes]]: ...
    @overload
    def recv_multipart(self, flags: int = 0, *, copy: Literal[False], track: bool = False) -> Awaitable[List[_zmq.Frame]]: ...
    @overload
    def recv_multipart(self, flags: int = 0, copy: bool = True, track: bool = False) -> Awaitable[List[bytes] | List[_zmq.Frame]]: ...
    def recv(self, flags: int = 0, copy: bool = True, track: bool = False) -> Awaitable[bytes | _zmq.Frame]:
        """Receive a single zmq frame.

        Returns a Future, whose result will be the received frame.

        Recommend using recv_multipart instead.
        """
    def send_multipart(self, msg_parts: Any, flags: int = 0, copy: bool = True, track: bool = False, **kwargs) -> Awaitable[_zmq.MessageTracker | None]:
        """Send a complete multipart zmq message.

        Returns a Future that resolves when sending is complete.
        """
    def send(self, data: Any, flags: int = 0, copy: bool = True, track: bool = False, **kwargs: Any) -> Awaitable[_zmq.MessageTracker | None]:
        """Send a single zmq frame.

        Returns a Future that resolves when sending is complete.

        Recommend using send_multipart instead.
        """
    def poll(self, timeout: Incomplete | None = None, flags=...) -> Awaitable[int]:
        """poll the socket for events

        returns a Future for the poll results.
        """
    def recv_string(self, *args, **kwargs) -> Awaitable[str]: ...
    def send_string(self, s: str, flags: int = 0, encoding: str = 'utf-8') -> Awaitable[None]: ...
