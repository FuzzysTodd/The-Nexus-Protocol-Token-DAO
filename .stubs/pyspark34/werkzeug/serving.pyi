import io
import socket
import socketserver
import ssl
import typing as t
from .exceptions import InternalServerError as InternalServerError
from .urls import uri_to_iri as uri_to_iri
from _typeshed import Incomplete
from _typeshed.wsgi import WSGIApplication as WSGIApplication, WSGIEnvironment as WSGIEnvironment
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKeyWithSerialization as RSAPrivateKeyWithSerialization
from cryptography.x509 import Certificate as Certificate
from http.server import BaseHTTPRequestHandler, HTTPServer

class _SslDummy:
    def __getattr__(self, name: str) -> t.Any: ...

can_fork: Incomplete
ForkingMixIn = socketserver.ForkingMixIn

class ForkingMixIn: ...

af_unix: Incomplete
LISTEN_QUEUE: int

class DechunkedInput(io.RawIOBase):
    """An input stream that handles Transfer-Encoding 'chunked'"""
    def __init__(self, rfile: t.IO[bytes]) -> None: ...
    def readable(self) -> bool: ...
    def read_chunk_len(self) -> int: ...
    def readinto(self, buf: bytearray) -> int: ...

class WSGIRequestHandler(BaseHTTPRequestHandler):
    """A request handler that implements WSGI dispatching."""
    server: BaseWSGIServer
    @property
    def server_version(self) -> str: ...
    client_address: Incomplete
    def make_environ(self) -> WSGIEnvironment: ...
    environ: Incomplete
    close_connection: bool
    def run_wsgi(self) -> None: ...
    def handle(self) -> None:
        """Handles a request ignoring dropped connections."""
    def connection_dropped(self, error: BaseException, environ: WSGIEnvironment | None = None) -> None:
        """Called if the connection was closed by the client.  By default
        nothing happens.
        """
    def __getattr__(self, name: str) -> t.Any: ...
    def address_string(self) -> str: ...
    def port_integer(self) -> int: ...
    def log_request(self, code: int | str = '-', size: int | str = '-') -> None: ...
    def log_error(self, format: str, *args: t.Any) -> None: ...
    def log_message(self, format: str, *args: t.Any) -> None: ...
    def log(self, type: str, message: str, *args: t.Any) -> None: ...

def generate_adhoc_ssl_pair(cn: str | None = None) -> tuple[Certificate, RSAPrivateKeyWithSerialization]: ...
def make_ssl_devcert(base_path: str, host: str | None = None, cn: str | None = None) -> tuple[str, str]:
    """Creates an SSL key for development.  This should be used instead of
    the ``'adhoc'`` key which generates a new cert on each server start.
    It accepts a path for where it should store the key and cert and
    either a host or CN.  If a host is given it will use the CN
    ``*.host/CN=host``.

    For more information see :func:`run_simple`.

    .. versionadded:: 0.9

    :param base_path: the path to the certificate and key.  The extension
                      ``.crt`` is added for the certificate, ``.key`` is
                      added for the key.
    :param host: the name of the host.  This can be used as an alternative
                 for the `cn`.
    :param cn: the `CN` to use.
    """
def generate_adhoc_ssl_context() -> ssl.SSLContext:
    """Generates an adhoc SSL context for the development server."""
def load_ssl_context(cert_file: str, pkey_file: str | None = None, protocol: int | None = None) -> ssl.SSLContext:
    """Loads SSL context from cert/private key files and optional protocol.
    Many parameters are directly taken from the API of
    :py:class:`ssl.SSLContext`.

    :param cert_file: Path of the certificate to use.
    :param pkey_file: Path of the private key to use. If not given, the key
                      will be obtained from the certificate file.
    :param protocol: A ``PROTOCOL`` constant from the :mod:`ssl` module.
        Defaults to :data:`ssl.PROTOCOL_TLS_SERVER`.
    """
def is_ssl_error(error: Exception | None = None) -> bool:
    """Checks if the given error (or the current one) is an SSL error."""
def select_address_family(host: str, port: int) -> socket.AddressFamily:
    """Return ``AF_INET4``, ``AF_INET6``, or ``AF_UNIX`` depending on
    the host and port."""
def get_sockaddr(host: str, port: int, family: socket.AddressFamily) -> tuple[str, int] | str:
    """Return a fully qualified socket address that can be passed to
    :func:`socket.bind`."""
def get_interface_ip(family: socket.AddressFamily) -> str:
    """Get the IP address of an external interface. Used when binding to
    0.0.0.0 or ::1 to show a more useful URL.

    :meta private:
    """

class BaseWSGIServer(HTTPServer):
    """A WSGI server that that handles one request at a time.

    Use :func:`make_server` to create a server instance.
    """
    multithread: bool
    multiprocess: bool
    request_queue_size = LISTEN_QUEUE
    allow_reuse_address: bool
    host: Incomplete
    port: Incomplete
    app: Incomplete
    passthrough_errors: Incomplete
    address_family: Incomplete
    socket: Incomplete
    server_address: Incomplete
    ssl_context: Incomplete
    def __init__(self, host: str, port: int, app: WSGIApplication, handler: type[WSGIRequestHandler] | None = None, passthrough_errors: bool = False, ssl_context: _TSSLContextArg | None = None, fd: int | None = None) -> None: ...
    def log(self, type: str, message: str, *args: t.Any) -> None: ...
    def serve_forever(self, poll_interval: float = 0.5) -> None: ...
    def handle_error(self, request: t.Any, client_address: tuple[str, int] | str) -> None: ...
    def log_startup(self) -> None:
        """Show information about the address when starting the server."""

class ThreadedWSGIServer(socketserver.ThreadingMixIn, BaseWSGIServer):
    """A WSGI server that handles concurrent requests in separate
    threads.

    Use :func:`make_server` to create a server instance.
    """
    multithread: bool
    daemon_threads: bool

class ForkingWSGIServer(ForkingMixIn, BaseWSGIServer):
    """A WSGI server that handles concurrent requests in separate forked
    processes.

    Use :func:`make_server` to create a server instance.
    """
    multiprocess: bool
    max_children: Incomplete
    def __init__(self, host: str, port: int, app: WSGIApplication, processes: int = 40, handler: type[WSGIRequestHandler] | None = None, passthrough_errors: bool = False, ssl_context: _TSSLContextArg | None = None, fd: int | None = None) -> None: ...

def make_server(host: str, port: int, app: WSGIApplication, threaded: bool = False, processes: int = 1, request_handler: type[WSGIRequestHandler] | None = None, passthrough_errors: bool = False, ssl_context: _TSSLContextArg | None = None, fd: int | None = None) -> BaseWSGIServer:
    """Create an appropriate WSGI server instance based on the value of
    ``threaded`` and ``processes``.

    This is called from :func:`run_simple`, but can be used separately
    to have access to the server object, such as to run it in a separate
    thread.

    See :func:`run_simple` for parameter docs.
    """
def is_running_from_reloader() -> bool:
    """Check if the server is running as a subprocess within the
    Werkzeug reloader.

    .. versionadded:: 0.10
    """
def run_simple(hostname: str, port: int, application: WSGIApplication, use_reloader: bool = False, use_debugger: bool = False, use_evalex: bool = True, extra_files: t.Iterable[str] | None = None, exclude_patterns: t.Iterable[str] | None = None, reloader_interval: int = 1, reloader_type: str = 'auto', threaded: bool = False, processes: int = 1, request_handler: type[WSGIRequestHandler] | None = None, static_files: dict[str, str | tuple[str, str]] | None = None, passthrough_errors: bool = False, ssl_context: _TSSLContextArg | None = None) -> None:
    '''Start a development server for a WSGI application. Various
    optional features can be enabled.

    .. warning::

        Do not use the development server when deploying to production.
        It is intended for use only during local development. It is not
        designed to be particularly efficient, stable, or secure.

    :param hostname: The host to bind to, for example ``\'localhost\'``.
        Can be a domain, IPv4 or IPv6 address, or file path starting
        with ``unix://`` for a Unix socket.
    :param port: The port to bind to, for example ``8080``. Using ``0``
        tells the OS to pick a random free port.
    :param application: The WSGI application to run.
    :param use_reloader: Use a reloader process to restart the server
        process when files are changed.
    :param use_debugger: Use Werkzeug\'s debugger, which will show
        formatted tracebacks on unhandled exceptions.
    :param use_evalex: Make the debugger interactive. A Python terminal
        can be opened for any frame in the traceback. Some protection is
        provided by requiring a PIN, but this should never be enabled
        on a publicly visible server.
    :param extra_files: The reloader will watch these files for changes
        in addition to Python modules. For example, watch a
        configuration file.
    :param exclude_patterns: The reloader will ignore changes to any
        files matching these :mod:`fnmatch` patterns. For example,
        ignore cache files.
    :param reloader_interval: How often the reloader tries to check for
        changes.
    :param reloader_type: The reloader to use. The ``\'stat\'`` reloader
        is built in, but may require significant CPU to watch files. The
        ``\'watchdog\'`` reloader is much more efficient but requires
        installing the ``watchdog`` package first.
    :param threaded: Handle concurrent requests using threads. Cannot be
        used with ``processes``.
    :param processes: Handle concurrent requests using up to this number
        of processes. Cannot be used with ``threaded``.
    :param request_handler: Use a different
        :class:`~BaseHTTPServer.BaseHTTPRequestHandler` subclass to
        handle requests.
    :param static_files: A dict mapping URL prefixes to directories to
        serve static files from using
        :class:`~werkzeug.middleware.SharedDataMiddleware`.
    :param passthrough_errors: Don\'t catch unhandled exceptions at the
        server level, let the server crash instead. If ``use_debugger``
        is enabled, the debugger will still catch such errors.
    :param ssl_context: Configure TLS to serve over HTTPS. Can be an
        :class:`ssl.SSLContext` object, a ``(cert_file, key_file)``
        tuple to create a typical context, or the string ``\'adhoc\'`` to
        generate a temporary self-signed certificate.

    .. versionchanged:: 2.1
        Instructions are shown for dealing with an "address already in
        use" error.

    .. versionchanged:: 2.1
        Running on ``0.0.0.0`` or ``::`` shows the loopback IP in
        addition to a real IP.

    .. versionchanged:: 2.1
        The command-line interface was removed.

    .. versionchanged:: 2.0
        Running on ``0.0.0.0`` or ``::`` shows a real IP address that
        was bound as well as a warning not to run the development server
        in production.

    .. versionchanged:: 2.0
        The ``exclude_patterns`` parameter was added.

    .. versionchanged:: 0.15
        Bind to a Unix socket by passing a ``hostname`` that starts with
        ``unix://``.

    .. versionchanged:: 0.10
        Improved the reloader and added support for changing the backend
        through the ``reloader_type`` parameter.

    .. versionchanged:: 0.9
        A command-line interface was added.

    .. versionchanged:: 0.8
        ``ssl_context`` can be a tuple of paths to the certificate and
        private key files.

    .. versionchanged:: 0.6
        The ``ssl_context`` parameter was added.

    .. versionchanged:: 0.5
       The ``static_files`` and ``passthrough_errors`` parameters were
       added.
    '''
