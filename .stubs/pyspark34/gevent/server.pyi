from _typeshed import Incomplete
from gevent.baseserver import BaseServer

__all__ = ['StreamServer', 'DatagramServer']

class StreamServer(BaseServer):
    """
    A generic TCP server.

    Accepts connections on a listening socket and spawns user-provided
    *handle* function for each connection with 2 arguments: the client
    socket and the client address.

    Note that although the errors in a successfully spawned handler
    will not affect the server or other connections, the errors raised
    by :func:`accept` and *spawn* cause the server to stop accepting
    for a short amount of time. The exact period depends on the values
    of :attr:`min_delay` and :attr:`max_delay` attributes.

    The delay starts with :attr:`min_delay` and doubles with each
    successive error until it reaches :attr:`max_delay`. A successful
    :func:`accept` resets the delay to :attr:`min_delay` again.

    See :class:`~gevent.baseserver.BaseServer` for information on defining the *handle*
    function and important restrictions on it.

    **SSL Support**

    The server can optionally work in SSL mode when given the correct
    keyword arguments. (That is, the presence of any keyword arguments
    will trigger SSL mode.) On Python 2.7.9 and later (any Python
    version that supports the :class:`ssl.SSLContext`), this can be
    done with a configured ``SSLContext``. On any Python version, it
    can be done by passing the appropriate arguments for
    :func:`ssl.wrap_socket`.

    The incoming socket will be wrapped into an SSL socket before
    being passed to the *handle* function.

    If the *ssl_context* keyword argument is present, it should
    contain an :class:`ssl.SSLContext`. The remaining keyword
    arguments are passed to the :meth:`ssl.SSLContext.wrap_socket`
    method of that object. Depending on the Python version, supported arguments
    may include:

    - server_hostname
    - suppress_ragged_eofs
    - do_handshake_on_connect

    .. caution:: When using an SSLContext, it should either be
       imported from :mod:`gevent.ssl`, or the process needs to be monkey-patched.
       If the process is not monkey-patched and you pass the standard library
       SSLContext, the resulting client sockets will not cooperate with gevent.

    Otherwise, keyword arguments are assumed to apply to :func:`ssl.wrap_socket`.
    These keyword arguments may include:

    - keyfile
    - certfile
    - cert_reqs
    - ssl_version
    - ca_certs
    - suppress_ragged_eofs
    - do_handshake_on_connect
    - ciphers

    .. versionchanged:: 1.2a2
       Add support for the *ssl_context* keyword argument.

    """
    backlog: int
    reuse_addr = DEFAULT_REUSE_ADDR
    wrap_socket: Incomplete
    ssl_args: Incomplete
    def __init__(self, listener, handle: Incomplete | None = None, backlog: Incomplete | None = None, spawn: str = 'default', **ssl_args) -> None: ...
    @property
    def ssl_enabled(self): ...
    def set_listener(self, listener) -> None: ...
    socket: Incomplete
    address: Incomplete
    def init_socket(self) -> None: ...
    @classmethod
    def get_listener(cls, address, backlog: Incomplete | None = None, family: Incomplete | None = None): ...
    def do_read(self): ...
    def do_close(self, sock, *args) -> None: ...
    def wrap_socket_and_handle(self, client_socket, address): ...

class DatagramServer(BaseServer):
    """A UDP server"""
    reuse_addr = DEFAULT_REUSE_ADDR
    def __init__(self, *args, **kwargs) -> None: ...
    socket: Incomplete
    address: Incomplete
    def init_socket(self) -> None: ...
    @classmethod
    def get_listener(cls, address, family: Incomplete | None = None): ...
    def do_read(self): ...
    def sendto(self, *args) -> None: ...
