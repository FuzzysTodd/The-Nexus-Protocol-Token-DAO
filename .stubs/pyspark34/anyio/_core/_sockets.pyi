import socket
import ssl
from .. import to_thread as to_thread
from ..abc import ConnectedUDPSocket as ConnectedUDPSocket, IPAddressType as IPAddressType, IPSockAddrType as IPSockAddrType, SocketListener as SocketListener, SocketStream as SocketStream, UDPSocket as UDPSocket, UNIXSocketStream as UNIXSocketStream
from ..streams.stapled import MultiListener as MultiListener
from ..streams.tls import TLSStream as TLSStream
from ._eventloop import get_asynclib as get_asynclib
from ._resources import aclose_forcefully as aclose_forcefully
from ._synchronization import Event as Event
from ._tasks import create_task_group as create_task_group, move_on_after as move_on_after
from _typeshed import Incomplete
from os import PathLike
from socket import AddressFamily, SocketKind
from typing import Awaitable, List, Literal, Tuple, overload

IPPROTO_IPV6: Incomplete
GetAddrInfoReturnType = List[Tuple[AddressFamily, SocketKind, int, str, Tuple[str, int]]]
AnyIPAddressFamily: Incomplete
IPAddressFamily: Incomplete

@overload
async def connect_tcp(remote_host: IPAddressType, remote_port: int, *, local_host: IPAddressType | None = ..., ssl_context: ssl.SSLContext | None = ..., tls_standard_compatible: bool = ..., tls_hostname: str, happy_eyeballs_delay: float = ...) -> TLSStream: ...
@overload
async def connect_tcp(remote_host: IPAddressType, remote_port: int, *, local_host: IPAddressType | None = ..., ssl_context: ssl.SSLContext, tls_standard_compatible: bool = ..., tls_hostname: str | None = ..., happy_eyeballs_delay: float = ...) -> TLSStream: ...
@overload
async def connect_tcp(remote_host: IPAddressType, remote_port: int, *, local_host: IPAddressType | None = ..., tls: Literal[True], ssl_context: ssl.SSLContext | None = ..., tls_standard_compatible: bool = ..., tls_hostname: str | None = ..., happy_eyeballs_delay: float = ...) -> TLSStream: ...
@overload
async def connect_tcp(remote_host: IPAddressType, remote_port: int, *, local_host: IPAddressType | None = ..., tls: Literal[False], ssl_context: ssl.SSLContext | None = ..., tls_standard_compatible: bool = ..., tls_hostname: str | None = ..., happy_eyeballs_delay: float = ...) -> SocketStream: ...
@overload
async def connect_tcp(remote_host: IPAddressType, remote_port: int, *, local_host: IPAddressType | None = ..., happy_eyeballs_delay: float = ...) -> SocketStream: ...
async def connect_unix(path: str | PathLike[str]) -> UNIXSocketStream:
    """
    Connect to the given UNIX socket.

    Not available on Windows.

    :param path: path to the socket
    :return: a socket stream object

    """
async def create_tcp_listener(*, local_host: IPAddressType | None = None, local_port: int = 0, family: AnyIPAddressFamily = ..., backlog: int = 65536, reuse_port: bool = False) -> MultiListener[SocketStream]:
    """
    Create a TCP socket listener.

    :param local_port: port number to listen on
    :param local_host: IP address of the interface to listen on. If omitted, listen on
        all IPv4 and IPv6 interfaces. To listen on all interfaces on a specific address
        family, use ``0.0.0.0`` for IPv4 or ``::`` for IPv6.
    :param family: address family (used if ``local_host`` was omitted)
    :param backlog: maximum number of queued incoming connections (up to a maximum of
        2**16, or 65536)
    :param reuse_port: ``True`` to allow multiple sockets to bind to the same
        address/port (not supported on Windows)
    :return: a list of listener objects

    """
async def create_unix_listener(path: str | PathLike[str], *, mode: int | None = None, backlog: int = 65536) -> SocketListener:
    """
    Create a UNIX socket listener.

    Not available on Windows.

    :param path: path of the socket
    :param mode: permissions to set on the socket
    :param backlog: maximum number of queued incoming connections (up to a maximum of 2**16, or
        65536)
    :return: a listener object

    .. versionchanged:: 3.0
        If a socket already exists on the file system in the given path, it will be removed first.

    """
async def create_udp_socket(family: AnyIPAddressFamily = ..., *, local_host: IPAddressType | None = None, local_port: int = 0, reuse_port: bool = False) -> UDPSocket:
    """
    Create a UDP socket.

    If ``local_port`` has been given, the socket will be bound to this port on the local
    machine, making this socket suitable for providing UDP based services.

    :param family: address family (``AF_INET`` or ``AF_INET6``) – automatically determined from
        ``local_host`` if omitted
    :param local_host: IP address or host name of the local interface to bind to
    :param local_port: local port to bind to
    :param reuse_port: ``True`` to allow multiple sockets to bind to the same address/port
        (not supported on Windows)
    :return: a UDP socket

    """
async def create_connected_udp_socket(remote_host: IPAddressType, remote_port: int, *, family: AnyIPAddressFamily = ..., local_host: IPAddressType | None = None, local_port: int = 0, reuse_port: bool = False) -> ConnectedUDPSocket:
    """
    Create a connected UDP socket.

    Connected UDP sockets can only communicate with the specified remote host/port, and any packets
    sent from other sources are dropped.

    :param remote_host: remote host to set as the default target
    :param remote_port: port on the remote host to set as the default target
    :param family: address family (``AF_INET`` or ``AF_INET6``) – automatically determined from
        ``local_host`` or ``remote_host`` if omitted
    :param local_host: IP address or host name of the local interface to bind to
    :param local_port: local port to bind to
    :param reuse_port: ``True`` to allow multiple sockets to bind to the same address/port
        (not supported on Windows)
    :return: a connected UDP socket

    """
async def getaddrinfo(host: bytearray | bytes | str, port: str | int | None, *, family: int | AddressFamily = 0, type: int | SocketKind = 0, proto: int = 0, flags: int = 0) -> GetAddrInfoReturnType:
    """
    Look up a numeric IP address given a host name.

    Internationalized domain names are translated according to the (non-transitional) IDNA 2008
    standard.

    .. note:: 4-tuple IPv6 socket addresses are automatically converted to 2-tuples of
        (host, port), unlike what :func:`socket.getaddrinfo` does.

    :param host: host name
    :param port: port number
    :param family: socket family (`'AF_INET``, ...)
    :param type: socket type (``SOCK_STREAM``, ...)
    :param proto: protocol number
    :param flags: flags to pass to upstream ``getaddrinfo()``
    :return: list of tuples containing (family, type, proto, canonname, sockaddr)

    .. seealso:: :func:`socket.getaddrinfo`

    """
def getnameinfo(sockaddr: IPSockAddrType, flags: int = 0) -> Awaitable[tuple[str, str]]:
    """
    Look up the host name of an IP address.

    :param sockaddr: socket address (e.g. (ipaddress, port) for IPv4)
    :param flags: flags to pass to upstream ``getnameinfo()``
    :return: a tuple of (host name, service name)

    .. seealso:: :func:`socket.getnameinfo`

    """
def wait_socket_readable(sock: socket.socket) -> Awaitable[None]:
    """
    Wait until the given socket has data to be read.

    This does **NOT** work on Windows when using the asyncio backend with a proactor event loop
    (default on py3.8+).

    .. warning:: Only use this on raw sockets that have not been wrapped by any higher level
        constructs like socket streams!

    :param sock: a socket object
    :raises ~anyio.ClosedResourceError: if the socket was closed while waiting for the
        socket to become readable
    :raises ~anyio.BusyResourceError: if another task is already waiting for the socket
        to become readable

    """
def wait_socket_writable(sock: socket.socket) -> Awaitable[None]:
    """
    Wait until the given socket can be written to.

    This does **NOT** work on Windows when using the asyncio backend with a proactor event loop
    (default on py3.8+).

    .. warning:: Only use this on raw sockets that have not been wrapped by any higher level
        constructs like socket streams!

    :param sock: a socket object
    :raises ~anyio.ClosedResourceError: if the socket was closed while waiting for the
        socket to become writable
    :raises ~anyio.BusyResourceError: if another task is already waiting for the socket
        to become writable

    """
def convert_ipv6_sockaddr(sockaddr: tuple[str, int, int, int] | tuple[str, int]) -> tuple[str, int]:
    """
    Convert a 4-tuple IPv6 socket address to a 2-tuple (address, port) format.

    If the scope ID is nonzero, it is added to the address, separated with ``%``.
    Otherwise the flow id and scope id are simply cut off from the tuple.
    Any other kinds of socket addresses are returned as-is.

    :param sockaddr: the result of :meth:`~socket.socket.getsockname`
    :return: the converted socket address

    """
