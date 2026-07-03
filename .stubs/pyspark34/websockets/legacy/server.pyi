import asyncio
import http
import socket
from ..datastructures import Headers, HeadersLike
from ..extensions import Extension, ServerExtensionFactory
from ..typing import LoggerLike, Origin, StatusLike, Subprotocol
from .protocol import WebSocketCommonProtocol
from _typeshed import Incomplete
from types import TracebackType
from typing import Any, Awaitable, Callable, Generator, Iterable, List, Sequence, Tuple, Type

__all__ = ['serve', 'unix_serve', 'WebSocketServerProtocol', 'WebSocketServer']

HeadersLikeOrCallable = HeadersLike | Callable[[str, Headers], HeadersLike]
HTTPResponse = Tuple[StatusLike, HeadersLike, bytes]

class WebSocketServerProtocol(WebSocketCommonProtocol):
    """
    WebSocket server connection.

    :class:`WebSocketServerProtocol` provides :meth:`recv` and :meth:`send`
    coroutines for receiving and sending messages.

    It supports asynchronous iteration to receive messages::

        async for message in websocket:
            await process(message)

    The iterator exits normally when the connection is closed with close code
    1000 (OK) or 1001 (going away) or without a close code. It raises
    a :exc:`~websockets.exceptions.ConnectionClosedError` when the connection
    is closed with any other code.

    You may customize the opening handshake in a subclass by
    overriding :meth:`process_request` or :meth:`select_subprotocol`.

    Args:
        ws_server: WebSocket server that created this connection.

    See :func:`serve` for the documentation of ``ws_handler``, ``logger``, ``origins``,
    ``extensions``, ``subprotocols``, ``extra_headers``, and ``server_header``.

    See :class:`~websockets.legacy.protocol.WebSocketCommonProtocol` for the
    documentation of ``ping_interval``, ``ping_timeout``, ``close_timeout``,
    ``max_size``, ``max_queue``, ``read_limit``, and ``write_limit``.

    """
    is_client: bool
    side: str
    ws_handler: Incomplete
    ws_server: Incomplete
    origins: Incomplete
    available_extensions: Incomplete
    available_subprotocols: Incomplete
    extra_headers: Incomplete
    server_header: Incomplete
    open_timeout: Incomplete
    def __init__(self, ws_handler: Callable[[WebSocketServerProtocol], Awaitable[Any]] | Callable[[WebSocketServerProtocol, str], Awaitable[Any]], ws_server: WebSocketServer, *, logger: LoggerLike | None = None, origins: Sequence[Origin | None] | None = None, extensions: Sequence[ServerExtensionFactory] | None = None, subprotocols: Sequence[Subprotocol] | None = None, extra_headers: HeadersLikeOrCallable | None = None, server_header: str | None = ..., process_request: Callable[[str, Headers], Awaitable[HTTPResponse | None]] | None = None, select_subprotocol: Callable[[Sequence[Subprotocol], Sequence[Subprotocol]], Subprotocol] | None = None, open_timeout: float | None = 10, **kwargs: Any) -> None: ...
    handler_task: Incomplete
    def connection_made(self, transport: asyncio.BaseTransport) -> None:
        """
        Register connection and initialize a task to handle it.

        """
    async def handler(self) -> None:
        """
        Handle the lifecycle of a WebSocket connection.

        Since this method doesn't have a caller able to handle exceptions, it
        attempts to log relevant ones and guarantees that the TCP connection is
        closed before exiting.

        """
    path: Incomplete
    request_headers: Incomplete
    async def read_http_request(self) -> Tuple[str, Headers]:
        """
        Read request line and headers from the HTTP request.

        If the request contains a body, it may be read from ``self.reader``
        after this coroutine returns.

        Raises:
            InvalidMessage: if the HTTP message is malformed or isn't an
                HTTP/1.1 GET request.

        """
    response_headers: Incomplete
    def write_http_response(self, status: http.HTTPStatus, headers: Headers, body: bytes | None = None) -> None:
        """
        Write status line and headers to the HTTP response.

        This coroutine is also able to write a response body.

        """
    async def process_request(self, path: str, request_headers: Headers) -> HTTPResponse | None:
        """
        Intercept the HTTP request and return an HTTP response if appropriate.

        You may override this method in a :class:`WebSocketServerProtocol`
        subclass, for example:

        * to return an HTTP 200 OK response on a given path; then a load
          balancer can use this path for a health check;
        * to authenticate the request and return an HTTP 401 Unauthorized or an
          HTTP 403 Forbidden when authentication fails.

        You may also override this method with the ``process_request``
        argument of :func:`serve` and :class:`WebSocketServerProtocol`. This
        is equivalent, except ``process_request`` won't have access to the
        protocol instance, so it can't store information for later use.

        :meth:`process_request` is expected to complete quickly. If it may run
        for a long time, then it should await :meth:`wait_closed` and exit if
        :meth:`wait_closed` completes, or else it could prevent the server
        from shutting down.

        Args:
            path: request path, including optional query string.
            request_headers: request headers.

        Returns:
            Optional[Tuple[StatusLike, HeadersLike, bytes]]: :obj:`None`
            to continue the WebSocket handshake normally.

            An HTTP response, represented by a 3-uple of the response status,
            headers, and body, to abort the WebSocket handshake and return
            that HTTP response instead.

        """
    @staticmethod
    def process_origin(headers: Headers, origins: Sequence[Origin | None] | None = None) -> Origin | None:
        """
        Handle the Origin HTTP request header.

        Args:
            headers: request headers.
            origins: optional list of acceptable origins.

        Raises:
            InvalidOrigin: if the origin isn't acceptable.

        """
    @staticmethod
    def process_extensions(headers: Headers, available_extensions: Sequence[ServerExtensionFactory] | None) -> Tuple[str | None, List[Extension]]:
        """
        Handle the Sec-WebSocket-Extensions HTTP request header.

        Accept or reject each extension proposed in the client request.
        Negotiate parameters for accepted extensions.

        Return the Sec-WebSocket-Extensions HTTP response header and the list
        of accepted extensions.

        :rfc:`6455` leaves the rules up to the specification of each
        :extension.

        To provide this level of flexibility, for each extension proposed by
        the client, we check for a match with each extension available in the
        server configuration. If no match is found, the extension is ignored.

        If several variants of the same extension are proposed by the client,
        it may be accepted several times, which won't make sense in general.
        Extensions must implement their own requirements. For this purpose,
        the list of previously accepted extensions is provided.

        This process doesn't allow the server to reorder extensions. It can
        only select a subset of the extensions proposed by the client.

        Other requirements, for example related to mandatory extensions or the
        order of extensions, may be implemented by overriding this method.

        Args:
            headers: request headers.
            extensions: optional list of supported extensions.

        Raises:
            InvalidHandshake: to abort the handshake with an HTTP 400 error.

        """
    def process_subprotocol(self, headers: Headers, available_subprotocols: Sequence[Subprotocol] | None) -> Subprotocol | None:
        """
        Handle the Sec-WebSocket-Protocol HTTP request header.

        Return Sec-WebSocket-Protocol HTTP response header, which is the same
        as the selected subprotocol.

        Args:
            headers: request headers.
            available_subprotocols: optional list of supported subprotocols.

        Raises:
            InvalidHandshake: to abort the handshake with an HTTP 400 error.

        """
    def select_subprotocol(self, client_subprotocols: Sequence[Subprotocol], server_subprotocols: Sequence[Subprotocol]) -> Subprotocol | None:
        """
        Pick a subprotocol among those supported by the client and the server.

        If several subprotocols are available, select the preferred subprotocol
        by giving equal weight to the preferences of the client and the server.

        If no subprotocol is available, proceed without a subprotocol.

        You may provide a ``select_subprotocol`` argument to :func:`serve` or
        :class:`WebSocketServerProtocol` to override this logic. For example,
        you could reject the handshake if the client doesn't support a
        particular subprotocol, rather than accept the handshake without that
        subprotocol.

        Args:
            client_subprotocols: list of subprotocols offered by the client.
            server_subprotocols: list of subprotocols available on the server.

        Returns:
            Optional[Subprotocol]: Selected subprotocol, if a common subprotocol
            was found.

            :obj:`None` to continue without a subprotocol.

        """
    origin: Incomplete
    async def handshake(self, origins: Sequence[Origin | None] | None = None, available_extensions: Sequence[ServerExtensionFactory] | None = None, available_subprotocols: Sequence[Subprotocol] | None = None, extra_headers: HeadersLikeOrCallable | None = None) -> str:
        """
        Perform the server side of the opening handshake.

        Args:
            origins: list of acceptable values of the Origin HTTP header;
                include :obj:`None` if the lack of an origin is acceptable.
            extensions: list of supported extensions, in order in which they
                should be tried.
            subprotocols: list of supported subprotocols, in order of
                decreasing preference.
            extra_headers: arbitrary HTTP headers to add to the response when
                the handshake succeeds.

        Returns:
            str: path of the URI of the request.

        Raises:
            InvalidHandshake: if the handshake fails.

        """

class WebSocketServer:
    '''
    WebSocket server returned by :func:`serve`.

    This class provides the same interface as :class:`~asyncio.Server`,
    notably the :meth:`~asyncio.Server.close`
    and :meth:`~asyncio.Server.wait_closed` methods.

    It keeps track of WebSocket connections in order to close them properly
    when shutting down.

    Args:
        logger: Logger for this server.
            It defaults to ``logging.getLogger("websockets.server")``.
            See the :doc:`logging guide <../../topics/logging>` for details.

    '''
    logger: Incomplete
    websockets: Incomplete
    close_task: Incomplete
    closed_waiter: Incomplete
    def __init__(self, logger: LoggerLike | None = None) -> None: ...
    server: Incomplete
    def wrap(self, server: asyncio.base_events.Server) -> None:
        """
        Attach to a given :class:`~asyncio.Server`.

        Since :meth:`~asyncio.loop.create_server` doesn't support injecting a
        custom ``Server`` class, the easiest solution that doesn't rely on
        private :mod:`asyncio` APIs is to:

        - instantiate a :class:`WebSocketServer`
        - give the protocol factory a reference to that instance
        - call :meth:`~asyncio.loop.create_server` with the factory
        - attach the resulting :class:`~asyncio.Server` with this method

        """
    def register(self, protocol: WebSocketServerProtocol) -> None:
        """
        Register a connection with this server.

        """
    def unregister(self, protocol: WebSocketServerProtocol) -> None:
        """
        Unregister a connection with this server.

        """
    def close(self, close_connections: bool = True) -> None:
        """
        Close the server.

        * Close the underlying :class:`~asyncio.Server`.
        * When ``close_connections`` is :obj:`True`, which is the default,
          close existing connections. Specifically:

          * Reject opening WebSocket connections with an HTTP 503 (service
            unavailable) error. This happens when the server accepted the TCP
            connection but didn't complete the opening handshake before closing.
          * Close open WebSocket connections with close code 1001 (going away).

        * Wait until all connection handlers terminate.

        :meth:`close` is idempotent.

        """
    async def wait_closed(self) -> None:
        """
        Wait until the server is closed.

        When :meth:`wait_closed` returns, all TCP connections are closed and
        all connection handlers have returned.

        To ensure a fast shutdown, a connection handler should always be
        awaiting at least one of:

        * :meth:`~WebSocketServerProtocol.recv`: when the connection is closed,
          it raises :exc:`~websockets.exceptions.ConnectionClosedOK`;
        * :meth:`~WebSocketServerProtocol.wait_closed`: when the connection is
          closed, it returns.

        Then the connection handler is immediately notified of the shutdown;
        it can clean up and exit.

        """
    def get_loop(self) -> asyncio.AbstractEventLoop:
        """
        See :meth:`asyncio.Server.get_loop`.

        """
    def is_serving(self) -> bool:
        """
        See :meth:`asyncio.Server.is_serving`.

        """
    async def start_serving(self) -> None:
        """
        See :meth:`asyncio.Server.start_serving`.

        Typical use::

            server = await serve(..., start_serving=False)
            # perform additional setup here...
            # ... then start the server
            await server.start_serving()

        """
    async def serve_forever(self) -> None:
        """
        See :meth:`asyncio.Server.serve_forever`.

        Typical use::

            server = await serve(...)
            # this coroutine doesn't return
            # canceling it stops the server
            await server.serve_forever()

        This is an alternative to using :func:`serve` as an asynchronous context
        manager. Shutdown is triggered by canceling :meth:`serve_forever`
        instead of exiting a :func:`serve` context.

        """
    @property
    def sockets(self) -> Iterable[socket.socket]:
        """
        See :attr:`asyncio.Server.sockets`.

        """
    async def __aenter__(self) -> WebSocketServer: ...
    async def __aexit__(self, exc_type: Type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...

class Serve:
    '''
    Start a WebSocket server listening on ``host`` and ``port``.

    Whenever a client connects, the server creates a
    :class:`WebSocketServerProtocol`, performs the opening handshake, and
    delegates to the connection handler, ``ws_handler``.

    The handler receives the :class:`WebSocketServerProtocol` and uses it to
    send and receive messages.

    Once the handler completes, either normally or with an exception, the
    server performs the closing handshake and closes the connection.

    Awaiting :func:`serve` yields a :class:`WebSocketServer`. This object
    provides a :meth:`~WebSocketServer.close` method to shut down the server::

        stop = asyncio.Future()  # set this future to exit the server

        server = await serve(...)
        await stop
        await server.close()

    :func:`serve` can be used as an asynchronous context manager. Then, the
    server is shut down automatically when exiting the context::

        stop = asyncio.Future()  # set this future to exit the server

        async with serve(...):
            await stop

    Args:
        ws_handler: Connection handler. It receives the WebSocket connection,
            which is a :class:`WebSocketServerProtocol`, in argument.
        host: Network interfaces the server binds to.
            See :meth:`~asyncio.loop.create_server` for details.
        port: TCP port the server listens on.
            See :meth:`~asyncio.loop.create_server` for details.
        create_protocol: Factory for the :class:`asyncio.Protocol` managing
            the connection. It defaults to :class:`WebSocketServerProtocol`.
            Set it to a wrapper or a subclass to customize connection handling.
        logger: Logger for this server.
            It defaults to ``logging.getLogger("websockets.server")``.
            See the :doc:`logging guide <../../topics/logging>` for details.
        compression: The "permessage-deflate" extension is enabled by default.
            Set ``compression`` to :obj:`None` to disable it. See the
            :doc:`compression guide <../../topics/compression>` for details.
        origins: Acceptable values of the ``Origin`` header, for defending
            against Cross-Site WebSocket Hijacking attacks. Include :obj:`None`
            in the list if the lack of an origin is acceptable.
        extensions: List of supported extensions, in order in which they
            should be negotiated and run.
        subprotocols: List of supported subprotocols, in order of decreasing
            preference.
        extra_headers (Union[HeadersLike, Callable[[str, Headers], HeadersLike]]):
            Arbitrary HTTP headers to add to the response. This can be
            a :data:`~websockets.datastructures.HeadersLike` or a callable
            taking the request path and headers in arguments and returning
            a :data:`~websockets.datastructures.HeadersLike`.
        server_header: Value of  the ``Server`` response header.
            It defaults to ``"Python/x.y.z websockets/X.Y"``.
            Setting it to :obj:`None` removes the header.
        process_request (Optional[Callable[[str, Headers],             Awaitable[Optional[Tuple[StatusLike, HeadersLike, bytes]]]]]):
            Intercept HTTP request before the opening handshake.
            See :meth:`~WebSocketServerProtocol.process_request` for details.
        select_subprotocol: Select a subprotocol supported by the client.
            See :meth:`~WebSocketServerProtocol.select_subprotocol` for details.
        open_timeout: Timeout for opening connections in seconds.
            :obj:`None` disables the timeout.

    See :class:`~websockets.legacy.protocol.WebSocketCommonProtocol` for the
    documentation of ``ping_interval``, ``ping_timeout``, ``close_timeout``,
    ``max_size``, ``max_queue``, ``read_limit``, and ``write_limit``.

    Any other keyword arguments are passed the event loop\'s
    :meth:`~asyncio.loop.create_server` method.

    For example:

    * You can set ``ssl`` to a :class:`~ssl.SSLContext` to enable TLS.

    * You can set ``sock`` to a :obj:`~socket.socket` that you created
      outside of websockets.

    Returns:
        WebSocketServer: WebSocket server.

    '''
    ws_server: Incomplete
    def __init__(self, ws_handler: Callable[[WebSocketServerProtocol], Awaitable[Any]] | Callable[[WebSocketServerProtocol, str], Awaitable[Any]], host: str | Sequence[str] | None = None, port: int | None = None, *, create_protocol: Callable[..., WebSocketServerProtocol] | None = None, logger: LoggerLike | None = None, compression: str | None = 'deflate', origins: Sequence[Origin | None] | None = None, extensions: Sequence[ServerExtensionFactory] | None = None, subprotocols: Sequence[Subprotocol] | None = None, extra_headers: HeadersLikeOrCallable | None = None, server_header: str | None = ..., process_request: Callable[[str, Headers], Awaitable[HTTPResponse | None]] | None = None, select_subprotocol: Callable[[Sequence[Subprotocol], Sequence[Subprotocol]], Subprotocol] | None = None, open_timeout: float | None = 10, ping_interval: float | None = 20, ping_timeout: float | None = 20, close_timeout: float | None = None, max_size: int | None = ..., max_queue: int | None = ..., read_limit: int = ..., write_limit: int = ..., **kwargs: Any) -> None: ...
    async def __aenter__(self) -> WebSocketServer: ...
    async def __aexit__(self, exc_type: Type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...
    def __await__(self) -> Generator[Any, None, WebSocketServer]: ...
    async def __await_impl__(self) -> WebSocketServer: ...
    __iter__ = __await__
serve = Serve

def unix_serve(ws_handler: Callable[[WebSocketServerProtocol], Awaitable[Any]] | Callable[[WebSocketServerProtocol, str], Awaitable[Any]], path: str | None = None, **kwargs: Any) -> Serve:
    """
    Start a WebSocket server listening on a Unix socket.

    This function is identical to :func:`serve`, except the ``host`` and
    ``port`` arguments are replaced by ``path``. It is only available on Unix.

    Unrecognized keyword arguments are passed the event loop's
    :meth:`~asyncio.loop.create_unix_server` method.

    It's useful for deploying a server behind a reverse proxy such as nginx.

    Args:
        path: File system path to the Unix socket.

    """
