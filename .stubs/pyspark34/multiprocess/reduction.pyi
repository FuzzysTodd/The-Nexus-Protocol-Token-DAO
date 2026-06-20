import pickle
from _typeshed import Incomplete
from abc import ABCMeta

__all__ = ['send_handle', 'recv_handle', 'ForkingPickler', 'register', 'dump', 'DupFd', 'sendfds', 'recvfds']

class ForkingPickler(pickle.Pickler):
    """Pickler subclass used by multiprocess."""
    dispatch_table: Incomplete
    def __init__(self, *args, **kwds) -> None: ...
    @classmethod
    def register(cls, type, reduce) -> None:
        """Register a reduce function for a type."""
    @classmethod
    def dumps(cls, obj, protocol: Incomplete | None = None, *args, **kwds): ...
    loads: Incomplete

register: Incomplete

def dump(obj, file, protocol: Incomplete | None = None, *args, **kwds) -> None:
    """Replacement for pickle.dump() using ForkingPickler."""
def sendfds(sock, fds) -> None:
    """Send an array of fds over an AF_UNIX socket."""
def recvfds(sock, size):
    """Receive an array of fds over an AF_UNIX socket."""
def send_handle(conn, handle, destination_pid) -> None:
    """Send a handle over a local connection."""
def recv_handle(conn):
    """Receive a handle over a local connection."""
def DupFd(fd):
    """Return a wrapper for an fd."""

class _C:
    def f(self) -> None: ...

class AbstractReducer(metaclass=ABCMeta):
    """Abstract base class for use in implementing a Reduction class
    suitable for use in replacing the standard reduction mechanism
    used in multiprocess."""
    ForkingPickler = ForkingPickler
    register = register
    dump = dump
    send_handle = send_handle
    recv_handle = recv_handle
    sendfds = sendfds
    recvfds = recvfds
    DupFd = DupFd
    def __init__(self, *args) -> None: ...
