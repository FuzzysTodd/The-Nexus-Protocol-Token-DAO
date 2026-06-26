import ssl
from _typeshed import Incomplete
from tornado import httputil as httputil, iostream as iostream, netutil as netutil
from tornado.escape import native_str as native_str
from tornado.http1connection import HTTP1ConnectionParameters as HTTP1ConnectionParameters, HTTP1ServerConnection as HTTP1ServerConnection
from tornado.tcpserver import TCPServer as TCPServer
from tornado.util import Configurable as Configurable
from typing import Any, Awaitable, Callable, Dict, List, Tuple, Type

class HTTPServer(TCPServer, Configurable, httputil.HTTPServerConnectionDelegate):
    '''A non-blocking, single-threaded HTTP server.

    A server is defined by a subclass of `.HTTPServerConnectionDelegate`,
    or, for backwards compatibility, a callback that takes an
    `.HTTPServerRequest` as an argument. The delegate is usually a
    `tornado.web.Application`.

    `HTTPServer` supports keep-alive connections by default
    (automatically for HTTP/1.1, or for HTTP/1.0 when the client
    requests ``Connection: keep-alive``).

    If ``xheaders`` is ``True``, we support the
    ``X-Real-Ip``/``X-Forwarded-For`` and
    ``X-Scheme``/``X-Forwarded-Proto`` headers, which override the
    remote IP and URI scheme/protocol for all requests.  These headers
    are useful when running Tornado behind a reverse proxy or load
    balancer.  The ``protocol`` argument can also be set to ``https``
    if Tornado is run behind an SSL-decoding proxy that does not set one of
    the supported ``xheaders``.

    By default, when parsing the ``X-Forwarded-For`` header, Tornado will
    select the last (i.e., the closest) address on the list of hosts as the
    remote host IP address.  To select the next server in the chain, a list of
    trusted downstream hosts may be passed as the ``trusted_downstream``
    argument.  These hosts will be skipped when parsing the ``X-Forwarded-For``
    header.

    To make this server serve SSL traffic, send the ``ssl_options`` keyword
    argument with an `ssl.SSLContext` object. For compatibility with older
    versions of Python ``ssl_options`` may also be a dictionary of keyword
    arguments for the `ssl.wrap_socket` method.::

       ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
       ssl_ctx.load_cert_chain(os.path.join(data_dir, "mydomain.crt"),
                               os.path.join(data_dir, "mydomain.key"))
       HTTPServer(application, ssl_options=ssl_ctx)

    `HTTPServer` initialization follows one of three patterns (the
    initialization methods are defined on `tornado.tcpserver.TCPServer`):

    1. `~tornado.tcpserver.TCPServer.listen`: single-process::

            async def main():
                server = HTTPServer()
                server.listen(8888)
                await asyncio.Event.wait()

            asyncio.run(main())

       In many cases, `tornado.web.Application.listen` can be used to avoid
       the need to explicitly create the `HTTPServer`.

       While this example does not create multiple processes on its own, when
       the ``reuse_port=True`` argument is passed to ``listen()`` you can run
       the program multiple times to create a multi-process service.

    2. `~tornado.tcpserver.TCPServer.add_sockets`: multi-process::

            sockets = bind_sockets(8888)
            tornado.process.fork_processes(0)
            async def post_fork_main():
                server = HTTPServer()
                server.add_sockets(sockets)
                await asyncio.Event().wait()
            asyncio.run(post_fork_main())

       The ``add_sockets`` interface is more complicated, but it can be used with
       `tornado.process.fork_processes` to run a multi-process service with all
       worker processes forked from a single parent.  ``add_sockets`` can also be
       used in single-process servers if you want to create your listening
       sockets in some way other than `~tornado.netutil.bind_sockets`.

       Note that when using this pattern, nothing that touches the event loop
       can be run before ``fork_processes``.

    3. `~tornado.tcpserver.TCPServer.bind`/`~tornado.tcpserver.TCPServer.start`:
       simple **deprecated** multi-process::

            server = HTTPServer()
            server.bind(8888)
            server.start(0)  # Forks multiple sub-processes
            IOLoop.current().start()

       This pattern is deprecated because it requires interfaces in the
       `asyncio` module that have been deprecated since Python 3.10. Support for
       creating multiple processes in the ``start`` method will be removed in a
       future version of Tornado.

    .. versionchanged:: 4.0
       Added ``decompress_request``, ``chunk_size``, ``max_header_size``,
       ``idle_connection_timeout``, ``body_timeout``, ``max_body_size``
       arguments.  Added support for `.HTTPServerConnectionDelegate`
       instances as ``request_callback``.

    .. versionchanged:: 4.1
       `.HTTPServerConnectionDelegate.start_request` is now called with
       two arguments ``(server_conn, request_conn)`` (in accordance with the
       documentation) instead of one ``(request_conn)``.

    .. versionchanged:: 4.2
       `HTTPServer` is now a subclass of `tornado.util.Configurable`.

    .. versionchanged:: 4.5
       Added the ``trusted_downstream`` argument.

    .. versionchanged:: 5.0
       The ``io_loop`` argument has been removed.
    '''
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    request_callback: Incomplete
    xheaders: Incomplete
    protocol: Incomplete
    conn_params: Incomplete
    trusted_downstream: Incomplete
    def initialize(self, request_callback: httputil.HTTPServerConnectionDelegate | Callable[[httputil.HTTPServerRequest], None], no_keep_alive: bool = False, xheaders: bool = False, ssl_options: Dict[str, Any] | ssl.SSLContext | None = None, protocol: str | None = None, decompress_request: bool = False, chunk_size: int | None = None, max_header_size: int | None = None, idle_connection_timeout: float | None = None, body_timeout: float | None = None, max_body_size: int | None = None, max_buffer_size: int | None = None, trusted_downstream: List[str] | None = None) -> None: ...
    @classmethod
    def configurable_base(cls) -> Type[Configurable]: ...
    @classmethod
    def configurable_default(cls) -> Type[Configurable]: ...
    async def close_all_connections(self) -> None:
        """Close all open connections and asynchronously wait for them to finish.

        This method is used in combination with `~.TCPServer.stop` to
        support clean shutdowns (especially for unittests). Typical
        usage would call ``stop()`` first to stop accepting new
        connections, then ``await close_all_connections()`` to wait for
        existing connections to finish.

        This method does not currently close open websocket connections.

        Note that this method is a coroutine and must be called with ``await``.

        """
    def handle_stream(self, stream: iostream.IOStream, address: Tuple) -> None: ...
    def start_request(self, server_conn: object, request_conn: httputil.HTTPConnection) -> httputil.HTTPMessageDelegate: ...
    def on_close(self, server_conn: object) -> None: ...

class _CallableAdapter(httputil.HTTPMessageDelegate):
    connection: Incomplete
    request_callback: Incomplete
    request: Incomplete
    delegate: Incomplete
    def __init__(self, request_callback: Callable[[httputil.HTTPServerRequest], None], request_conn: httputil.HTTPConnection) -> None: ...
    def headers_received(self, start_line: httputil.RequestStartLine | httputil.ResponseStartLine, headers: httputil.HTTPHeaders) -> Awaitable[None] | None: ...
    def data_received(self, chunk: bytes) -> Awaitable[None] | None: ...
    def finish(self) -> None: ...
    def on_connection_close(self) -> None: ...

class _HTTPRequestContext:
    address: Incomplete
    address_family: Incomplete
    remote_ip: Incomplete
    protocol: Incomplete
    trusted_downstream: Incomplete
    def __init__(self, stream: iostream.IOStream, address: Tuple, protocol: str | None, trusted_downstream: List[str] | None = None) -> None: ...

class _ProxyAdapter(httputil.HTTPMessageDelegate):
    connection: Incomplete
    delegate: Incomplete
    def __init__(self, delegate: httputil.HTTPMessageDelegate, request_conn: httputil.HTTPConnection) -> None: ...
    def headers_received(self, start_line: httputil.RequestStartLine | httputil.ResponseStartLine, headers: httputil.HTTPHeaders) -> Awaitable[None] | None: ...
    def data_received(self, chunk: bytes) -> Awaitable[None] | None: ...
    def finish(self) -> None: ...
    def on_connection_close(self) -> None: ...
HTTPRequest = httputil.HTTPServerRequest
