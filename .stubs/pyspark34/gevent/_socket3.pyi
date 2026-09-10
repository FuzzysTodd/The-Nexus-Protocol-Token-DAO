import _socket
from _typeshed import Incomplete
from gevent import _socketcommon
from gevent._compat import PYPY as PYPY
from gevent._util import copy_globals as copy_globals

__socket__ = _socketcommon.__socket__
__implements__: Incomplete
__extensions__: Incomplete
__imports__: Incomplete
__dns__: Incomplete
SocketIO = __socket__.SocketIO

class _closedsocket:
    family: Incomplete
    type: Incomplete
    proto: Incomplete
    orig_fileno: Incomplete
    description: Incomplete
    def __init__(self, family, type, proto, orig_fileno, description) -> None: ...
    def fileno(self): ...
    def close(self) -> None:
        """No-op"""
    detach = fileno
    send: Incomplete
    recv: Incomplete
    recv_into: Incomplete
    sendto: Incomplete
    recvfrom: Incomplete
    recvfrom_into: Incomplete
    getsockname: Incomplete
    def __bool__(self) -> bool: ...
    __getattr__: Incomplete

class _wrefsocket(_socket.socket):
    timeout: Incomplete

class socket(_socketcommon.SocketMixin):
    """
    gevent `socket.socket <https://docs.python.org/3/library/socket.html#socket-objects>`_
    for Python 3.

    This object should have the same API as the standard library socket linked to above. Not all
    methods are specifically documented here; when they are they may point out a difference
    to be aware of or may document a method the standard library does not.
    """
    timeout: Incomplete
    hub: Incomplete
    def __init__(self, family: int = -1, type: int = -1, proto: int = -1, fileno: Incomplete | None = None) -> None: ...
    def __getattr__(self, name): ...
    @property
    def type(self): ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def dup(self):
        """dup() -> socket object

        Return a new socket object connected to the same system resource.
        """
    def accept(self):
        """accept() -> (socket object, address info)

        Wait for an incoming connection.  Return a new socket
        representing the connection, and the address of the client.
        For IP sockets, the address info is a pair (hostaddr, port).
        """
    def makefile(self, mode: str = 'r', buffering: Incomplete | None = None, *, encoding: Incomplete | None = None, errors: Incomplete | None = None, newline: Incomplete | None = None):
        """Return an I/O stream connected to the socket

        The arguments are as for io.open() after the filename,
        except the only mode characters supported are 'r', 'w' and 'b'.
        The semantics are similar too.
        """
    def close(self) -> None: ...
    @property
    def closed(self): ...
    def detach(self):
        """
        detach() -> file descriptor

        Close the socket object without closing the underlying file
        descriptor. The object cannot be used after this call; when the
        real file descriptor is closed, the number that was previously
        used here may be reused. The fileno() method, after this call,
        will return an invalid socket id.

        The previous descriptor is returned.

        .. versionchanged:: 1.5

           Also immediately drop any native event loop resources.
        """
    def recvmsg(self, *args): ...
    def recvmsg_into(self, buffers, *args): ...
    def sendmsg(self, buffers, ancdata=(), flags: int = 0, address: Incomplete | None = None): ...
    def sendfile(self, file, offset: int = 0, count: Incomplete | None = None):
        """sendfile(file[, offset[, count]]) -> sent

        Send a file until EOF is reached by using high-performance
        os.sendfile() and return the total number of bytes which
        were sent.
        *file* must be a regular file object opened in binary mode.
        If os.sendfile() is not available (e.g. Windows) or file is
        not a regular file socket.send() will be used instead.
        *offset* tells from where to start reading the file.
        If specified, *count* is the total number of bytes to transmit
        as opposed to sending the file until EOF is reached.
        File position is updated on return or also in case of error in
        which case file.tell() can be used to figure out the number of
        bytes which were sent.
        The socket must be of SOCK_STREAM type.
        Non-blocking sockets are not supported.

        .. versionadded:: 1.1rc4
           Added in Python 3.5, but available under all Python 3 versions in
           gevent.
        """
    def get_inheritable(self): ...
    def set_inheritable(self, inheritable) -> None: ...
    def get_inheritable(self): ...
    def set_inheritable(self, inheritable) -> None: ...
SocketType = socket

def fromfd(fd, family, type, proto: int = 0):
    """ fromfd(fd, family, type[, proto]) -> socket object

    Create a socket object from a duplicate of the given file
    descriptor.  The remaining arguments are the same as for socket().
    """
def fromshare(info):
    """ fromshare(info) -> socket object

        Create a socket object from a the bytes object returned by
        socket.share(pid).
        """
def socketpair(family: Incomplete | None = None, type=..., proto: int = 0):
    """socketpair([family[, type[, proto]]]) -> (socket object, socket object)

        Create a pair of socket objects from the sockets returned by the platform
        socketpair() function.
        The arguments are the same as for socket() except the default family is
        AF_UNIX if defined on the platform; otherwise, the default is AF_INET.

        .. versionchanged:: 1.2
           All Python 3 versions on Windows supply this function (natively
           supplied by Python 3.5 and above).
        """

__version_specific__: Incomplete
