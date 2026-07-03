import zmq
import zmq.asyncio
from typing import Awaitable, List, overload
from zmq._typing import TypedDict

__all__ = ['parse_monitor_message', 'recv_monitor_message']

class _MonitorMessage(TypedDict):
    event: int
    value: int
    endpoint: bytes

def parse_monitor_message(msg: List[bytes]) -> _MonitorMessage:
    """decode zmq_monitor event messages.

    Parameters
    ----------
    msg : list(bytes)
        zmq multipart message that has arrived on a monitor PAIR socket.

        First frame is::

            16 bit event id
            32 bit event value
            no padding

        Second frame is the endpoint as a bytestring

    Returns
    -------
    event : dict
        event description as dict with the keys `event`, `value`, and `endpoint`.
    """
@overload
def recv_monitor_message(socket: zmq.asyncio.Socket, flags: int = 0) -> Awaitable[_MonitorMessage]: ...
@overload
def recv_monitor_message(socket: zmq.Socket[bytes], flags: int = 0) -> _MonitorMessage: ...
