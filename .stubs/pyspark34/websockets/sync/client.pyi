import socket
import ssl
from ..client import ClientProtocol
from ..datastructures import HeadersLike
from ..extensions.base import ClientExtensionFactory
from ..protocol import Event
from ..typing import LoggerLike, Origin, Subprotocol
from .connection import Connection
from _typeshed import Incomplete
from typing import Any, Sequence, Type

__all__ = ['connect', 'unix_connect', 'ClientConnection']

class ClientConnection(Connection):
    """
    Threaded implementation of a WebSocket client connection.

    :class:`ClientConnection` provides :meth:`recv` and :meth:`send` methods for
    receiving and sending messages.

    It supports iteration to receive messages::

        for message in websocket:
            process(message)

    The iterator exits normally when the connection is closed with close code
    1000 (OK) or 1001 (going away) or without a close code. It raises a
    :exc:`~websockets.exceptions.ConnectionClosedError` when the connection is
    closed with any other code.

    Args:
        socket: Socket connected to a WebSocket server.
        protocol: Sans-I/O connection.
        close_timeout: Timeout for closing the connection in seconds.

    """
    protocol: Incomplete
    response_rcvd: Incomplete
    def __init__(self, socket: socket.socket, protocol: ClientProtocol, *, close_timeout: float | None = 10) -> None: ...
    request: Incomplete
    def handshake(self, additional_headers: HeadersLike | None = None, user_agent_header: str | None = ..., timeout: float | None = None) -> None:
        """
        Perform the opening handshake.

        """
    response: Incomplete
    def process_event(self, event: Event) -> None:
        """
        Process one incoming event.

        """
    def recv_events(self) -> None:
        """
        Read incoming data from the socket and process events.

        """

def connect(uri: str, *, sock: socket.socket | None = None, ssl_context: ssl.SSLContext | None = None, server_hostname: str | None = None, unix: bool = False, path: str | None = None, origin: Origin | None = None, extensions: Sequence[ClientExtensionFactory] | None = None, subprotocols: Sequence[Subprotocol] | None = None, additional_headers: HeadersLike | None = None, user_agent_header: str | None = ..., compression: str | None = 'deflate', open_timeout: float | None = 10, close_timeout: float | None = 10, max_size: int | None = ..., logger: LoggerLike | None = None, create_connection: Type[ClientConnection] | None = None) -> ClientConnection:
    '''
    Connect to the WebSocket server at ``uri``.

    This function returns a :class:`ClientConnection` instance, which you can
    use to send and receive messages.

    :func:`connect` may be used as a context manager::

        async with websockets.sync.client.connect(...) as websocket:
            ...

    The connection is closed automatically when exiting the context.

    Args:
        uri: URI of the WebSocket server.
        sock: Preexisting TCP socket. ``sock`` overrides the host and port
            from ``uri``. You may call :func:`socket.create_connection` to
            create a suitable TCP socket.
        ssl_context: Configuration for enabling TLS on the connection.
        server_hostname: Host name for the TLS handshake. ``server_hostname``
            overrides the host name from ``uri``.
        origin: Value of the ``Origin`` header, for servers that require it.
        extensions: List of supported extensions, in order in which they
            should be negotiated and run.
        subprotocols: List of supported subprotocols, in order of decreasing
            preference.
        additional_headers (HeadersLike | None): Arbitrary HTTP headers to add
            to the handshake request.
        user_agent_header: Value of  the ``User-Agent`` request header.
            It defaults to ``"Python/x.y.z websockets/X.Y"``.
            Setting it to :obj:`None` removes the header.
        compression: The "permessage-deflate" extension is enabled by default.
            Set ``compression`` to :obj:`None` to disable it. See the
            :doc:`compression guide <../../topics/compression>` for details.
        open_timeout: Timeout for opening the connection in seconds.
            :obj:`None` disables the timeout.
        close_timeout: Timeout for closing the connection in seconds.
            :obj:`None` disables the timeout.
        max_size: Maximum size of incoming messages in bytes.
            :obj:`None` disables the limit.
        logger: Logger for this client.
            It defaults to ``logging.getLogger("websockets.client")``.
            See the :doc:`logging guide <../../topics/logging>` for details.
        create_connection: Factory for the :class:`ClientConnection` managing
            the connection. Set it to a wrapper or a subclass to customize
            connection handling.

    Raises:
        InvalidURI: If ``uri`` isn\'t a valid WebSocket URI.
        OSError: If the TCP connection fails.
        InvalidHandshake: If the opening handshake fails.
        TimeoutError: If the opening handshake times out.

    '''
def unix_connect(path: str | None = None, uri: str | None = None, **kwargs: Any) -> ClientConnection:
    """
    Connect to a WebSocket server listening on a Unix socket.

    This function is identical to :func:`connect`, except for the additional
    ``path`` argument. It's only available on Unix.

    It's mainly useful for debugging servers listening on Unix sockets.

    Args:
        path: File system path to the Unix socket.
        uri: URI of the WebSocket server. ``uri`` defaults to
            ``ws://localhost/`` or, when a ``ssl_context`` is provided, to
            ``wss://localhost/``.

    """
