import datetime
import socket
import ssl
from _typeshed import Incomplete
from tornado import gen as gen
from tornado.concurrent import Future as Future, future_add_done_callback as future_add_done_callback
from tornado.gen import TimeoutError as TimeoutError
from tornado.ioloop import IOLoop as IOLoop
from tornado.iostream import IOStream as IOStream
from tornado.netutil import Resolver as Resolver
from typing import Any, Callable, Dict, Iterator, List, Tuple

class _Connector:
    '''A stateless implementation of the "Happy Eyeballs" algorithm.

    "Happy Eyeballs" is documented in RFC6555 as the recommended practice
    for when both IPv4 and IPv6 addresses are available.

    In this implementation, we partition the addresses by family, and
    make the first connection attempt to whichever address was
    returned first by ``getaddrinfo``.  If that connection fails or
    times out, we begin a connection in parallel to the first address
    of the other family.  If there are additional failures we retry
    with other addresses, keeping one connection attempt per family
    in flight at a time.

    http://tools.ietf.org/html/rfc6555

    '''
    io_loop: Incomplete
    connect: Incomplete
    future: Incomplete
    timeout: Incomplete
    connect_timeout: Incomplete
    last_error: Incomplete
    remaining: Incomplete
    streams: Incomplete
    def __init__(self, addrinfo: List[Tuple], connect: Callable[[socket.AddressFamily, Tuple], Tuple[IOStream, 'Future[IOStream]']]) -> None: ...
    @staticmethod
    def split(addrinfo: List[Tuple]) -> Tuple[List[Tuple[socket.AddressFamily, Tuple]], List[Tuple[socket.AddressFamily, Tuple]]]:
        """Partition the ``addrinfo`` list by address family.

        Returns two lists.  The first list contains the first entry from
        ``addrinfo`` and all others with the same family, and the
        second list contains all other addresses (normally one list will
        be AF_INET and the other AF_INET6, although non-standard resolvers
        may return additional families).
        """
    def start(self, timeout: float = ..., connect_timeout: float | datetime.timedelta | None = None) -> Future[Tuple[socket.AddressFamily, Any, IOStream]]: ...
    def try_connect(self, addrs: Iterator[Tuple[socket.AddressFamily, Tuple]]) -> None: ...
    def on_connect_done(self, addrs: Iterator[Tuple[socket.AddressFamily, Tuple]], af: socket.AddressFamily, addr: Tuple, future: Future[IOStream]) -> None: ...
    def set_timeout(self, timeout: float) -> None: ...
    def on_timeout(self) -> None: ...
    def clear_timeout(self) -> None: ...
    def set_connect_timeout(self, connect_timeout: float | datetime.timedelta) -> None: ...
    def on_connect_timeout(self) -> None: ...
    def clear_timeouts(self) -> None: ...
    def close_streams(self) -> None: ...

class TCPClient:
    """A non-blocking TCP connection factory.

    .. versionchanged:: 5.0
       The ``io_loop`` argument (deprecated since version 4.1) has been removed.
    """
    resolver: Incomplete
    def __init__(self, resolver: Resolver | None = None) -> None: ...
    def close(self) -> None: ...
    async def connect(self, host: str, port: int, af: socket.AddressFamily = ..., ssl_options: Dict[str, Any] | ssl.SSLContext | None = None, max_buffer_size: int | None = None, source_ip: str | None = None, source_port: int | None = None, timeout: float | datetime.timedelta | None = None) -> IOStream:
        """Connect to the given host and port.

        Asynchronously returns an `.IOStream` (or `.SSLIOStream` if
        ``ssl_options`` is not None).

        Using the ``source_ip`` kwarg, one can specify the source
        IP address to use when establishing the connection.
        In case the user needs to resolve and
        use a specific interface, it has to be handled outside
        of Tornado as this depends very much on the platform.

        Raises `TimeoutError` if the input future does not complete before
        ``timeout``, which may be specified in any form allowed by
        `.IOLoop.add_timeout` (i.e. a `datetime.timedelta` or an absolute time
        relative to `.IOLoop.time`)

        Similarly, when the user requires a certain source port, it can
        be specified using the ``source_port`` arg.

        .. versionchanged:: 4.5
           Added the ``source_ip`` and ``source_port`` arguments.

        .. versionchanged:: 5.0
           Added the ``timeout`` argument.
        """
