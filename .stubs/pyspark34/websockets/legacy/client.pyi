from ..datastructures import Headers, HeadersLike
from ..extensions import ClientExtensionFactory, Extension
from ..typing import LoggerLike, Origin, Subprotocol
from ..uri import WebSocketURI
from .protocol import WebSocketCommonProtocol
from _typeshed import Incomplete
from types import TracebackType
from typing import Any, AsyncIterator, Callable, Generator, List, Sequence, Tuple, Type

__all__ = ['connect', 'unix_connect', 'WebSocketClientProtocol']

class WebSocketClientProtocol(WebSocketCommonProtocol):
    """
    WebSocket client connection.

    :class:`WebSocketClientProtocol` provides :meth:`recv` and :meth:`send`
    coroutines for receiving and sending messages.

    It supports asynchronous iteration to receive incoming messages::

        async for message in websocket:
            await process(message)

    The iterator exits normally when the connection is closed with close code
    1000 (OK) or 1001 (going away) or without a close code. It raises
    a :exc:`~websockets.exceptions.ConnectionClosedError` when the connection
    is closed with any other code.

    See :func:`connect` for the documentation of ``logger``, ``origin``,
    ``extensions``, ``subprotocols``, ``extra_headers``, and
    ``user_agent_header``.

    See :class:`~websockets.legacy.protocol.WebSocketCommonProtocol` for the
    documentation of ``ping_interval``, ``ping_timeout``, ``close_timeout``,
    ``max_size``, ``max_queue``, ``read_limit``, and ``write_limit``.

    """
    is_client: bool
    side: str
    origin: Incomplete
    available_extensions: Incomplete
    available_subprotocols: Incomplete
    extra_headers: Incomplete
    user_agent_header: Incomplete
    def __init__(self, *, logger: LoggerLike | None = None, origin: Origin | None = None, extensions: Sequence[ClientExtensionFactory] | None = None, subprotocols: Sequence[Subprotocol] | None = None, extra_headers: HeadersLike | None = None, user_agent_header: str | None = ..., **kwargs: Any) -> None: ...
    path: Incomplete
    request_headers: Incomplete
    def write_http_request(self, path: str, headers: Headers) -> None:
        """
        Write request line and headers to the HTTP request.

        """
    response_headers: Incomplete
    async def read_http_response(self) -> Tuple[int, Headers]:
        """
        Read status line and headers from the HTTP response.

        If the response contains a body, it may be read from ``self.reader``
        after this coroutine returns.

        Raises:
            InvalidMessage: If the HTTP message is malformed or isn't an
                HTTP/1.1 GET response.

        """
    @staticmethod
    def process_extensions(headers: Headers, available_extensions: Sequence[ClientExtensionFactory] | None) -> List[Extension]:
        """
        Handle the Sec-WebSocket-Extensions HTTP response header.

        Check that each extension is supported, as well as its parameters.

        Return the list of accepted extensions.

        Raise :exc:`~websockets.exceptions.InvalidHandshake` to abort the
        connection.

        :rfc:`6455` leaves the rules up to the specification of each
        :extension.

        To provide this level of flexibility, for each extension accepted by
        the server, we check for a match with each extension available in the
        client configuration. If no match is found, an exception is raised.

        If several variants of the same extension are accepted by the server,
        it may be configured several times, which won't make sense in general.
        Extensions must implement their own requirements. For this purpose,
        the list of previously accepted extensions is provided.

        Other requirements, for example related to mandatory extensions or the
        order of extensions, may be implemented by overriding this method.

        """
    @staticmethod
    def process_subprotocol(headers: Headers, available_subprotocols: Sequence[Subprotocol] | None) -> Subprotocol | None:
        """
        Handle the Sec-WebSocket-Protocol HTTP response header.

        Check that it contains exactly one supported subprotocol.

        Return the selected subprotocol.

        """
    extensions: Incomplete
    subprotocol: Incomplete
    async def handshake(self, wsuri: WebSocketURI, origin: Origin | None = None, available_extensions: Sequence[ClientExtensionFactory] | None = None, available_subprotocols: Sequence[Subprotocol] | None = None, extra_headers: HeadersLike | None = None) -> None:
        """
        Perform the client side of the opening handshake.

        Args:
            wsuri: URI of the WebSocket server.
            origin: Value of the ``Origin`` header.
            extensions: List of supported extensions, in order in which they
                should be negotiated and run.
            subprotocols: List of supported subprotocols, in order of decreasing
                preference.
            extra_headers: Arbitrary HTTP headers to add to the handshake request.

        Raises:
            InvalidHandshake: If the handshake fails.

        """

class Connect:
    '''
    Connect to the WebSocket server at ``uri``.

    Awaiting :func:`connect` yields a :class:`WebSocketClientProtocol` which
    can then be used to send and receive messages.

    :func:`connect` can be used as a asynchronous context manager::

        async with websockets.connect(...) as websocket:
            ...

    The connection is closed automatically when exiting the context.

    :func:`connect` can be used as an infinite asynchronous iterator to
    reconnect automatically on errors::

        async for websocket in websockets.connect(...):
            try:
                ...
            except websockets.ConnectionClosed:
                continue

    The connection is closed automatically after each iteration of the loop.

    If an error occurs while establishing the connection, :func:`connect`
    retries with exponential backoff. The backoff delay starts at three
    seconds and increases up to one minute.

    If an error occurs in the body of the loop, you can handle the exception
    and :func:`connect` will reconnect with the next iteration; or you can
    let the exception bubble up and break out of the loop. This lets you
    decide which errors trigger a reconnection and which errors are fatal.

    Args:
        uri: URI of the WebSocket server.
        create_protocol: Factory for the :class:`asyncio.Protocol` managing
            the connection. It defaults to :class:`WebSocketClientProtocol`.
            Set it to a wrapper or a subclass to customize connection handling.
        logger: Logger for this client.
            It defaults to ``logging.getLogger("websockets.client")``.
            See the :doc:`logging guide <../../topics/logging>` for details.
        compression: The "permessage-deflate" extension is enabled by default.
            Set ``compression`` to :obj:`None` to disable it. See the
            :doc:`compression guide <../../topics/compression>` for details.
        origin: Value of the ``Origin`` header, for servers that require it.
        extensions: List of supported extensions, in order in which they
            should be negotiated and run.
        subprotocols: List of supported subprotocols, in order of decreasing
            preference.
        extra_headers: Arbitrary HTTP headers to add to the handshake request.
        user_agent_header: Value of  the ``User-Agent`` request header.
            It defaults to ``"Python/x.y.z websockets/X.Y"``.
            Setting it to :obj:`None` removes the header.
        open_timeout: Timeout for opening the connection in seconds.
            :obj:`None` disables the timeout.

    See :class:`~websockets.legacy.protocol.WebSocketCommonProtocol` for the
    documentation of ``ping_interval``, ``ping_timeout``, ``close_timeout``,
    ``max_size``, ``max_queue``, ``read_limit``, and ``write_limit``.

    Any other keyword arguments are passed the event loop\'s
    :meth:`~asyncio.loop.create_connection` method.

    For example:

    * You can set ``ssl`` to a :class:`~ssl.SSLContext` to enforce TLS
      settings. When connecting to a ``wss://`` URI, if ``ssl`` isn\'t
      provided, a TLS context is created
      with :func:`~ssl.create_default_context`.

    * You can set ``host`` and ``port`` to connect to a different host and
      port from those found in ``uri``. This only changes the destination of
      the TCP connection. The host name from ``uri`` is still used in the TLS
      handshake for secure connections and in the ``Host`` header.

    Raises:
        InvalidURI: If ``uri`` isn\'t a valid WebSocket URI.
        OSError: If the TCP connection fails.
        InvalidHandshake: If the opening handshake fails.
        ~asyncio.TimeoutError: If the opening handshake times out.

    '''
    MAX_REDIRECTS_ALLOWED: int
    open_timeout: Incomplete
    logger: Incomplete
    def __init__(self, uri: str, *, create_protocol: Callable[..., WebSocketClientProtocol] | None = None, logger: LoggerLike | None = None, compression: str | None = 'deflate', origin: Origin | None = None, extensions: Sequence[ClientExtensionFactory] | None = None, subprotocols: Sequence[Subprotocol] | None = None, extra_headers: HeadersLike | None = None, user_agent_header: str | None = ..., open_timeout: float | None = 10, ping_interval: float | None = 20, ping_timeout: float | None = 20, close_timeout: float | None = None, max_size: int | None = ..., max_queue: int | None = ..., read_limit: int = ..., write_limit: int = ..., **kwargs: Any) -> None: ...
    def handle_redirect(self, uri: str) -> None: ...
    BACKOFF_MIN: float
    BACKOFF_MAX: float
    BACKOFF_FACTOR: float
    BACKOFF_INITIAL: int
    async def __aiter__(self) -> AsyncIterator[WebSocketClientProtocol]: ...
    async def __aenter__(self) -> WebSocketClientProtocol: ...
    async def __aexit__(self, exc_type: Type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...
    def __await__(self) -> Generator[Any, None, WebSocketClientProtocol]: ...
    async def __await_impl_timeout__(self) -> WebSocketClientProtocol: ...
    protocol: Incomplete
    async def __await_impl__(self) -> WebSocketClientProtocol: ...
    __iter__ = __await__
connect = Connect

def unix_connect(path: str | None = None, uri: str = 'ws://localhost/', **kwargs: Any) -> Connect:
    """
    Similar to :func:`connect`, but for connecting to a Unix socket.

    This function builds upon the event loop's
    :meth:`~asyncio.loop.create_unix_connection` method.

    It is only available on Unix.

    It's mainly useful for debugging servers listening on Unix sockets.

    Args:
        path: File system path to the Unix socket.
        uri: URI of the WebSocket server; the host is used in the TLS
            handshake for secure connections and in the ``Host`` header.

    """
