from _typeshed import Incomplete

__all__ = ['Socket', 'IPC_PATH_MAX_LEN']

IPC_PATH_MAX_LEN: Incomplete

class Socket:
    context: Incomplete
    socket_type: Incomplete
    copy_threshold: int
    def __init__(self, context: Incomplete | None = None, socket_type: Incomplete | None = None, shadow: int = 0, copy_threshold: Incomplete | None = None) -> None: ...
    @property
    def underlying(self):
        """The address of the underlying libzmq socket"""
    @property
    def closed(self): ...
    def close(self, linger: Incomplete | None = None) -> None: ...
    def bind(self, address) -> None: ...
    def unbind(self, address) -> None: ...
    def connect(self, address) -> None: ...
    def disconnect(self, address) -> None: ...
    def set(self, option, value) -> None: ...
    def get(self, option): ...
    def send(self, data, flags: int = 0, copy: bool = False, track: bool = False): ...
    def recv(self, flags: int = 0, copy: bool = True, track: bool = False): ...
    def monitor(self, addr, events: int = -1) -> None:
        """s.monitor(addr, flags)

        Start publishing socket events on inproc.
        See libzmq docs for zmq_monitor for details.

        Note: requires libzmq >= 3.2

        Parameters
        ----------
        addr : str
            The inproc url used for monitoring. Passing None as
            the addr will cause an existing socket monitor to be
            deregistered.
        events : int [default: zmq.EVENT_ALL]
            The zmq event bitmask for which events will be sent to the monitor.
        """
