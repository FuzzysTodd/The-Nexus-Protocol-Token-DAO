import concurrent.futures
import socket
import ssl
from _typeshed import Incomplete
from tornado.concurrent import dummy_executor as dummy_executor, run_on_executor as run_on_executor
from tornado.ioloop import IOLoop as IOLoop
from tornado.util import Configurable as Configurable, errno_from_exception as errno_from_exception
from typing import Any, Awaitable, Callable, Dict, List, Tuple, Type

def bind_sockets(port: int, address: str | None = None, family: socket.AddressFamily = ..., backlog: int = ..., flags: int | None = None, reuse_port: bool = False) -> List[socket.socket]:
    """Creates listening sockets bound to the given port and address.

    Returns a list of socket objects (multiple sockets are returned if
    the given address maps to multiple IP addresses, which is most common
    for mixed IPv4 and IPv6 use).

    Address may be either an IP address or hostname.  If it's a hostname,
    the server will listen on all IP addresses associated with the
    name.  Address may be an empty string or None to listen on all
    available interfaces.  Family may be set to either `socket.AF_INET`
    or `socket.AF_INET6` to restrict to IPv4 or IPv6 addresses, otherwise
    both will be used if available.

    The ``backlog`` argument has the same meaning as for
    `socket.listen() <socket.socket.listen>`.

    ``flags`` is a bitmask of AI_* flags to `~socket.getaddrinfo`, like
    ``socket.AI_PASSIVE | socket.AI_NUMERICHOST``.

    ``reuse_port`` option sets ``SO_REUSEPORT`` option for every socket
    in the list. If your platform doesn't support this option ValueError will
    be raised.
    """
def bind_unix_socket(file: str, mode: int = 384, backlog: int = ...) -> socket.socket:
    """Creates a listening unix socket.

        If a socket with the given name already exists, it will be deleted.
        If any other file with that name exists, an exception will be
        raised.

        Returns a socket object (not a list of socket objects like
        `bind_sockets`)
        """
def add_accept_handler(sock: socket.socket, callback: Callable[[socket.socket, Any], None]) -> Callable[[], None]:
    """Adds an `.IOLoop` event handler to accept new connections on ``sock``.

    When a connection is accepted, ``callback(connection, address)`` will
    be run (``connection`` is a socket object, and ``address`` is the
    address of the other end of the connection).  Note that this signature
    is different from the ``callback(fd, events)`` signature used for
    `.IOLoop` handlers.

    A callable is returned which, when called, will remove the `.IOLoop`
    event handler and stop processing further incoming connections.

    .. versionchanged:: 5.0
       The ``io_loop`` argument (deprecated since version 4.1) has been removed.

    .. versionchanged:: 5.0
       A callable is returned (``None`` was returned before).
    """
def is_valid_ip(ip: str) -> bool:
    """Returns ``True`` if the given string is a well-formed IP address.

    Supports IPv4 and IPv6.
    """

class Resolver(Configurable):
    """Configurable asynchronous DNS resolver interface.

    By default, a blocking implementation is used (which simply calls
    `socket.getaddrinfo`).  An alternative implementation can be
    chosen with the `Resolver.configure <.Configurable.configure>`
    class method::

        Resolver.configure('tornado.netutil.ThreadedResolver')

    The implementations of this interface included with Tornado are

    * `tornado.netutil.DefaultLoopResolver`
    * `tornado.netutil.DefaultExecutorResolver` (deprecated)
    * `tornado.netutil.BlockingResolver` (deprecated)
    * `tornado.netutil.ThreadedResolver` (deprecated)
    * `tornado.netutil.OverrideResolver`
    * `tornado.platform.twisted.TwistedResolver` (deprecated)
    * `tornado.platform.caresresolver.CaresResolver` (deprecated)

    .. versionchanged:: 5.0
       The default implementation has changed from `BlockingResolver` to
       `DefaultExecutorResolver`.

    .. versionchanged:: 6.2
       The default implementation has changed from `DefaultExecutorResolver` to
       `DefaultLoopResolver`.
    """
    @classmethod
    def configurable_base(cls) -> Type['Resolver']: ...
    @classmethod
    def configurable_default(cls) -> Type['Resolver']: ...
    def resolve(self, host: str, port: int, family: socket.AddressFamily = ...) -> Awaitable[List[Tuple[int, Any]]]:
        """Resolves an address.

        The ``host`` argument is a string which may be a hostname or a
        literal IP address.

        Returns a `.Future` whose result is a list of (family,
        address) pairs, where address is a tuple suitable to pass to
        `socket.connect <socket.socket.connect>` (i.e. a ``(host,
        port)`` pair for IPv4; additional fields may be present for
        IPv6). If a ``callback`` is passed, it will be run with the
        result as an argument when it is complete.

        :raises IOError: if the address cannot be resolved.

        .. versionchanged:: 4.4
           Standardized all implementations to raise `IOError`.

        .. versionchanged:: 6.0 The ``callback`` argument was removed.
           Use the returned awaitable object instead.

        """
    def close(self) -> None:
        """Closes the `Resolver`, freeing any resources used.

        .. versionadded:: 3.1

        """

class DefaultExecutorResolver(Resolver):
    """Resolver implementation using `.IOLoop.run_in_executor`.

    .. versionadded:: 5.0

    .. deprecated:: 6.2

       Use `DefaultLoopResolver` instead.
    """
    async def resolve(self, host: str, port: int, family: socket.AddressFamily = ...) -> List[Tuple[int, Any]]: ...

class DefaultLoopResolver(Resolver):
    """Resolver implementation using `asyncio.loop.getaddrinfo`."""
    async def resolve(self, host: str, port: int, family: socket.AddressFamily = ...) -> List[Tuple[int, Any]]: ...

class ExecutorResolver(Resolver):
    """Resolver implementation using a `concurrent.futures.Executor`.

    Use this instead of `ThreadedResolver` when you require additional
    control over the executor being used.

    The executor will be shut down when the resolver is closed unless
    ``close_resolver=False``; use this if you want to reuse the same
    executor elsewhere.

    .. versionchanged:: 5.0
       The ``io_loop`` argument (deprecated since version 4.1) has been removed.

    .. deprecated:: 5.0
       The default `Resolver` now uses `asyncio.loop.getaddrinfo`;
       use that instead of this class.
    """
    executor: Incomplete
    close_executor: Incomplete
    def initialize(self, executor: concurrent.futures.Executor | None = None, close_executor: bool = True) -> None: ...
    def close(self) -> None: ...
    def resolve(self, host: str, port: int, family: socket.AddressFamily = ...) -> List[Tuple[int, Any]]: ...

class BlockingResolver(ExecutorResolver):
    """Default `Resolver` implementation, using `socket.getaddrinfo`.

    The `.IOLoop` will be blocked during the resolution, although the
    callback will not be run until the next `.IOLoop` iteration.

    .. deprecated:: 5.0
       The default `Resolver` now uses `.IOLoop.run_in_executor`; use that instead
       of this class.
    """
    def initialize(self) -> None: ...

class ThreadedResolver(ExecutorResolver):
    """Multithreaded non-blocking `Resolver` implementation.

    Requires the `concurrent.futures` package to be installed
    (available in the standard library since Python 3.2,
    installable with ``pip install futures`` in older versions).

    The thread pool size can be configured with::

        Resolver.configure('tornado.netutil.ThreadedResolver',
                           num_threads=10)

    .. versionchanged:: 3.1
       All ``ThreadedResolvers`` share a single thread pool, whose
       size is set by the first one to be created.

    .. deprecated:: 5.0
       The default `Resolver` now uses `.IOLoop.run_in_executor`; use that instead
       of this class.
    """
    def initialize(self, num_threads: int = 10) -> None: ...

class OverrideResolver(Resolver):
    '''Wraps a resolver with a mapping of overrides.

    This can be used to make local DNS changes (e.g. for testing)
    without modifying system-wide settings.

    The mapping can be in three formats::

        {
            # Hostname to host or ip
            "example.com": "127.0.1.1",

            # Host+port to host+port
            ("login.example.com", 443): ("localhost", 1443),

            # Host+port+address family to host+port
            ("login.example.com", 443, socket.AF_INET6): ("::1", 1443),
        }

    .. versionchanged:: 5.0
       Added support for host-port-family triplets.
    '''
    resolver: Incomplete
    mapping: Incomplete
    def initialize(self, resolver: Resolver, mapping: dict) -> None: ...
    def close(self) -> None: ...
    def resolve(self, host: str, port: int, family: socket.AddressFamily = ...) -> Awaitable[List[Tuple[int, Any]]]: ...

def ssl_options_to_context(ssl_options: Dict[str, Any] | ssl.SSLContext, server_side: bool | None = None) -> ssl.SSLContext:
    """Try to convert an ``ssl_options`` dictionary to an
    `~ssl.SSLContext` object.

    The ``ssl_options`` dictionary contains keywords to be passed to
    `ssl.wrap_socket`.  In Python 2.7.9+, `ssl.SSLContext` objects can
    be used instead.  This function converts the dict form to its
    `~ssl.SSLContext` equivalent, and may be used when a component which
    accepts both forms needs to upgrade to the `~ssl.SSLContext` version
    to use features like SNI or NPN.

    .. versionchanged:: 6.2

       Added server_side argument. Omitting this argument will
       result in a DeprecationWarning on Python 3.10.

    """
def ssl_wrap_socket(socket: socket.socket, ssl_options: Dict[str, Any] | ssl.SSLContext, server_hostname: str | None = None, server_side: bool | None = None, **kwargs: Any) -> ssl.SSLSocket:
    """Returns an ``ssl.SSLSocket`` wrapping the given socket.

    ``ssl_options`` may be either an `ssl.SSLContext` object or a
    dictionary (as accepted by `ssl_options_to_context`).  Additional
    keyword arguments are passed to ``wrap_socket`` (either the
    `~ssl.SSLContext` method or the `ssl` module function as
    appropriate).

    .. versionchanged:: 6.2

       Added server_side argument. Omitting this argument will
       result in a DeprecationWarning on Python 3.10.
    """
