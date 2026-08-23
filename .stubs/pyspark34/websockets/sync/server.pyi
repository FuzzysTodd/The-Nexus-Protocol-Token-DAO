import socket
import ssl
from ..extensions.base import ServerExtensionFactory
from ..http11 import Request, Response
from ..protocol import Event
from ..server import ServerProtocol
from ..typing import LoggerLike, Origin, Subprotocol
from .connection import Connection
from _typeshed import Incomplete
from types import TracebackType
from typing import Any, Callable, Sequence, Type

__all__ = ['serve', 'unix_serve', 'ServerConnection', 'WebSocketServer']

class ServerConnection(Connection):
    """
    Threaded implementation of a WebSocket server connection.

    :class:`ServerConnection` provides :meth:`recv` and :meth:`send` methods for
    receiving and sending messages.

    It supports iteration to receive messages::

        for message in websocket:
            process(message)

    The iterator exits normally when the connection is closed with close code
    1000 (OK) or 1001 (going away) or without a close code. It raises a
    :exc:`~websockets.exceptions.ConnectionClosedError` when the connection is
    closed with any other code.

    Args:
        socket: Socket connected to a WebSocket client.
        protocol: Sans-I/O connection.
        close_timeout: Timeout for closing the connection in seconds.

    """
    protocol: Incomplete
    request_rcvd: Incomplete
    def __init__(self, socket: socket.socket, protocol: ServerProtocol, *, close_timeout: float | None = 10) -> None: ...
    response: Incomplete
    def handshake(self, process_request: Callable[[ServerConnection, Request], Response | None] | None = None, process_response: Callable[[ServerConnection, Request, Response], Response | None] | None = None, server_header: str | None = ..., timeout: float | None = None) -> None:
        """
        Perform the opening handshake.

        """
    request: Incomplete
    def process_event(self, event: Event) -> None:
        """
        Process one incoming event.

        """
    def recv_events(self) -> None:
        """
        Read incoming data from the socket and process events.

        """

class WebSocketServer:
    """
    WebSocket server returned by :func:`serve`.

    This class mirrors the API of :class:`~socketserver.BaseServer`, notably the
    :meth:`~socketserver.BaseServer.serve_forever` and
    :meth:`~socketserver.BaseServer.shutdown` methods, as well as the context
    manager protocol.

    Args:
        socket: Server socket listening for new connections.
        handler: Handler for one connection. Receives the socket and address
            returned by :meth:`~socket.socket.accept`.
        logger: Logger for this server.

    """
    socket: Incomplete
    handler: Incomplete
    logger: Incomplete
    def __init__(self, socket: socket.socket, handler: Callable[[socket.socket, Any], None], logger: LoggerLike | None = None) -> None: ...
    def serve_forever(self) -> None:
        """
        See :meth:`socketserver.BaseServer.serve_forever`.

        This method doesn't return. Calling :meth:`shutdown` from another thread
        stops the server.

        Typical use::

            with serve(...) as server:
                server.serve_forever()

        """
    def shutdown(self) -> None:
        """
        See :meth:`socketserver.BaseServer.shutdown`.

        """
    def fileno(self) -> int:
        """
        See :meth:`socketserver.BaseServer.fileno`.

        """
    def __enter__(self) -> WebSocketServer: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...

def serve(handler: Callable[[ServerConnection], None], host: str | None = None, port: int | None = None, *, sock: socket.socket | None = None, ssl_context: ssl.SSLContext | None = None, unix: bool = False, path: str | None = None, origins: Sequence[Origin | None] | None = None, extensions: Sequence[ServerExtensionFactory] | None = None, subprotocols: Sequence[Subprotocol] | None = None, select_subprotocol: Callable[[ServerConnection, Sequence[Subprotocol]], Subprotocol | None] | None = None, process_request: Callable[[ServerConnection, Request], Response | None] | None = None, process_response: Callable[[ServerConnection, Request, Response], Response | None] | None = None, server_header: str | None = ..., compression: str | None = 'deflate', open_timeout: float | None = 10, close_timeout: float | None = 10, max_size: int | None = ..., logger: LoggerLike | None = None, create_connection: Type[ServerConnection] | None = None) -> WebSocketServer:
    '''
    Create a WebSocket server listening on ``host`` and ``port``.

    Whenever a client connects, the server creates a :class:`ServerConnection`,
    performs the opening handshake, and delegates to the ``handler``.

    The handler receives a :class:`ServerConnection` instance, which you can use
    to send and receive messages.

    Once the handler completes, either normally or with an exception, the server
    performs the closing handshake and closes the connection.

    :class:`WebSocketServer` mirrors the API of
    :class:`~socketserver.BaseServer`. Treat it as a context manager to ensure
    that it will be closed and call the :meth:`~WebSocketServer.serve_forever`
    method to serve requests::

        def handler(websocket):
            ...

        with websockets.sync.server.serve(handler, ...) as server:
            server.serve_forever()

    Args:
        handler: Connection handler. It receives the WebSocket connection,
            which is a :class:`ServerConnection`, in argument.
        host: Network interfaces the server binds to.
            See :func:`~socket.create_server` for details.
        port: TCP port the server listens on.
            See :func:`~socket.create_server` for details.
        sock: Preexisting TCP socket. ``sock`` replaces ``host`` and ``port``.
            You may call :func:`socket.create_server` to create a suitable TCP
            socket.
        ssl_context: Configuration for enabling TLS on the connection.
        origins: Acceptable values of the ``Origin`` header, for defending
            against Cross-Site WebSocket Hijacking attacks. Include :obj:`None`
            in the list if the lack of an origin is acceptable.
        extensions: List of supported extensions, in order in which they
            should be negotiated and run.
        subprotocols: List of supported subprotocols, in order of decreasing
            preference.
        select_subprotocol: Callback for selecting a subprotocol among
            those supported by the client and the server. It receives a
            :class:`ServerConnection` (not a
            :class:`~websockets.server.ServerProtocol`!) instance and a list of
            subprotocols offered by the client. Other than the first argument,
            it has the same behavior as the
            :meth:`ServerProtocol.select_subprotocol
            <websockets.server.ServerProtocol.select_subprotocol>` method.
        process_request: Intercept the request during the opening handshake.
            Return an HTTP response to force the response or :obj:`None` to
            continue normally. When you force an HTTP 101 Continue response,
            the handshake is successful. Else, the connection is aborted.
        process_response: Intercept the response during the opening handshake.
            Return an HTTP response to force the response or :obj:`None` to
            continue normally. When you force an HTTP 101 Continue response,
            the handshake is successful. Else, the connection is aborted.
        server_header: Value of  the ``Server`` response header.
            It defaults to ``"Python/x.y.z websockets/X.Y"``. Setting it to
            :obj:`None` removes the header.
        compression: The "permessage-deflate" extension is enabled by default.
            Set ``compression`` to :obj:`None` to disable it. See the
            :doc:`compression guide <../../topics/compression>` for details.
        open_timeout: Timeout for opening connections in seconds.
            :obj:`None` disables the timeout.
        close_timeout: Timeout for closing connections in seconds.
            :obj:`None` disables the timeout.
        max_size: Maximum size of incoming messages in bytes.
            :obj:`None` disables the limit.
        logger: Logger for this server.
            It defaults to ``logging.getLogger("websockets.server")``. See the
            :doc:`logging guide <../../topics/logging>` for details.
        create_connection: Factory for the :class:`ServerConnection` managing
            the connection. Set it to a wrapper or a subclass to customize
            connection handling.
    '''
def unix_serve(handler: Callable[[ServerConnection], Any], path: str | None = None, **kwargs: Any) -> WebSocketServer:
    """
    Create a WebSocket server listening on a Unix socket.

    This function is identical to :func:`serve`, except the ``host`` and
    ``port`` arguments are replaced by ``path``. It's only available on Unix.

    It's useful for deploying a server behind a reverse proxy such as nginx.

    Args:
        handler: Connection handler. It receives the WebSocket connection,
            which is a :class:`ServerConnection`, in argument.
        path: File system path to the Unix socket.

    """
