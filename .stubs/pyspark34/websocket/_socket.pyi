from ._exceptions import *
from ._ssl_compat import *
from ._utils import *
import socket
from _typeshed import Incomplete

__all__ = ['DEFAULT_SOCKET_OPTION', 'sock_opt', 'setdefaulttimeout', 'getdefaulttimeout', 'recv', 'recv_line', 'send']

DEFAULT_SOCKET_OPTION: Incomplete

class sock_opt:
    sockopt: Incomplete
    sslopt: Incomplete
    timeout: Incomplete
    def __init__(self, sockopt: list, sslopt: dict) -> None: ...

def setdefaulttimeout(timeout: int | float | None) -> None:
    """
    Set the global timeout setting to connect.

    Parameters
    ----------
    timeout: int or float
        default socket timeout time (in seconds)
    """
def getdefaulttimeout() -> int | float | None:
    """
    Get default timeout

    Returns
    ----------
    _default_timeout: int or float
        Return the global timeout setting (in seconds) to connect.
    """
def recv(sock: socket.socket, bufsize: int) -> bytes: ...
def recv_line(sock: socket.socket) -> bytes: ...
def send(sock: socket.socket, data: bytes | str) -> int: ...
