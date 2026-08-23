from _typeshed import Incomplete

__all__ = ['Client', 'Listener', 'Pipe', 'wait']

class _ConnectionBase:
    def __init__(self, handle, readable: bool = True, writable: bool = True) -> None: ...
    def __del__(self) -> None: ...
    @property
    def closed(self):
        """True if the connection is closed"""
    @property
    def readable(self):
        """True if the connection is readable"""
    @property
    def writable(self):
        """True if the connection is writable"""
    def fileno(self):
        """File descriptor or handle of the connection"""
    def close(self) -> None:
        """Close the connection"""
    def send_bytes(self, buf, offset: int = 0, size: Incomplete | None = None) -> None:
        """Send the bytes data from a bytes-like object"""
    def send(self, obj) -> None:
        """Send a (picklable) object"""
    def recv_bytes(self, maxlength: Incomplete | None = None):
        """
        Receive bytes data as a bytes object.
        """
    def recv_bytes_into(self, buf, offset: int = 0):
        """
        Receive bytes data into a writeable bytes-like object.
        Return the number of bytes read.
        """
    def recv(self):
        """Receive a (picklable) object"""
    def poll(self, timeout: float = 0.0):
        """Whether there is any input available to be read"""
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

class PipeConnection(_ConnectionBase):
    """
        Connection class based on a Windows named pipe.
        Overlapped I/O is used, so the handles must have been created
        with FILE_FLAG_OVERLAPPED.
        """
class Connection(_ConnectionBase):
    """
    Connection class based on an arbitrary file descriptor (Unix only), or
    a socket handle (Windows).
    """

class Listener:
    """
    Returns a listener object.

    This is a wrapper for a bound socket which is 'listening' for
    connections, or for a Windows named pipe.
    """
    def __init__(self, address: Incomplete | None = None, family: Incomplete | None = None, backlog: int = 1, authkey: Incomplete | None = None) -> None: ...
    def accept(self):
        """
        Accept a connection on the bound socket or named pipe of `self`.

        Returns a `Connection` object.
        """
    def close(self) -> None:
        """
        Close the bound socket or named pipe of `self`.
        """
    @property
    def address(self): ...
    @property
    def last_accepted(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

def Client(address, family: Incomplete | None = None, authkey: Incomplete | None = None):
    """
    Returns a connection to the address of a `Listener`
    """
def Pipe(duplex: bool = True):
    """
        Returns pair of connection objects at either end of a pipe
        """

class SocketListener:
    """
    Representation of a socket which is bound to an address and listening
    """
    def __init__(self, address, family, backlog: int = 1) -> None: ...
    def accept(self): ...
    def close(self) -> None: ...

class ConnectionWrapper:
    def __init__(self, conn, dumps, loads) -> None: ...
    def send(self, obj) -> None: ...
    def recv(self): ...

class XmlListener(Listener):
    def accept(self): ...

def wait(object_list, timeout: Incomplete | None = None):
    """
        Wait till an object in object_list is ready/readable.

        Returns list of those objects in object_list which are ready/readable.
        """
