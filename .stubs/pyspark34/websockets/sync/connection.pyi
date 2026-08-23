import socket
import threading
from ..protocol import Event, Protocol, State
from ..typing import Data, Subprotocol
from _typeshed import Incomplete
from types import TracebackType
from typing import Any, Iterable, Iterator, Type

__all__ = ['Connection']

class Connection:
    """
    Threaded implementation of a WebSocket connection.

    :class:`Connection` provides APIs shared between WebSocket servers and
    clients.

    You shouldn't use it directly. Instead, use
    :class:`~websockets.sync.client.ClientConnection` or
    :class:`~websockets.sync.server.ServerConnection`.

    """
    recv_bufsize: int
    socket: Incomplete
    protocol: Incomplete
    close_timeout: Incomplete
    id: Incomplete
    logger: Incomplete
    debug: Incomplete
    request: Incomplete
    response: Incomplete
    protocol_mutex: Incomplete
    recv_messages: Incomplete
    send_in_progress: bool
    close_deadline: Incomplete
    pings: Incomplete
    recv_events_thread: Incomplete
    recv_events_exc: Incomplete
    def __init__(self, socket: socket.socket, protocol: Protocol, *, close_timeout: float | None = 10) -> None: ...
    @property
    def local_address(self) -> Any:
        """
        Local address of the connection.

        For IPv4 connections, this is a ``(host, port)`` tuple.

        The format of the address depends on the address family.
        See :meth:`~socket.socket.getsockname`.

        """
    @property
    def remote_address(self) -> Any:
        """
        Remote address of the connection.

        For IPv4 connections, this is a ``(host, port)`` tuple.

        The format of the address depends on the address family.
        See :meth:`~socket.socket.getpeername`.

        """
    @property
    def subprotocol(self) -> Subprotocol | None:
        """
        Subprotocol negotiated during the opening handshake.

        :obj:`None` if no subprotocol was negotiated.

        """
    def __enter__(self) -> Connection: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...
    def __iter__(self) -> Iterator[Data]:
        """
        Iterate on incoming messages.

        The iterator calls :meth:`recv` and yields messages in an infinite loop.

        It exits when the connection is closed normally. It raises a
        :exc:`~websockets.exceptions.ConnectionClosedError` exception after a
        protocol error or a network failure.

        """
    def recv(self, timeout: float | None = None) -> Data:
        """
        Receive the next message.

        When the connection is closed, :meth:`recv` raises
        :exc:`~websockets.exceptions.ConnectionClosed`. Specifically, it raises
        :exc:`~websockets.exceptions.ConnectionClosedOK` after a normal closure
        and :exc:`~websockets.exceptions.ConnectionClosedError` after a protocol
        error or a network failure. This is how you detect the end of the
        message stream.

        If ``timeout`` is :obj:`None`, block until a message is received. If
        ``timeout`` is set and no message is received within ``timeout``
        seconds, raise :exc:`TimeoutError`. Set ``timeout`` to ``0`` to check if
        a message was already received.

        If the message is fragmented, wait until all fragments are received,
        reassemble them, and return the whole message.

        Returns:
            A string (:class:`str`) for a Text_ frame or a bytestring
            (:class:`bytes`) for a Binary_ frame.

            .. _Text: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.6
            .. _Binary: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.6

        Raises:
            ConnectionClosed: When the connection is closed.
            RuntimeError: If two threads call :meth:`recv` or
                :meth:`recv_streaming` concurrently.

        """
    def recv_streaming(self) -> Iterator[Data]:
        """
        Receive the next message frame by frame.

        If the message is fragmented, yield each fragment as it is received.
        The iterator must be fully consumed, or else the connection will become
        unusable.

        :meth:`recv_streaming` raises the same exceptions as :meth:`recv`.

        Returns:
            An iterator of strings (:class:`str`) for a Text_ frame or
            bytestrings (:class:`bytes`) for a Binary_ frame.

            .. _Text: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.6
            .. _Binary: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.6

        Raises:
            ConnectionClosed: When the connection is closed.
            RuntimeError: If two threads call :meth:`recv` or
                :meth:`recv_streaming` concurrently.

        """
    def send(self, message: Data | Iterable[Data]) -> None:
        """
        Send a message.

        A string (:class:`str`) is sent as a Text_ frame. A bytestring or
        bytes-like object (:class:`bytes`, :class:`bytearray`, or
        :class:`memoryview`) is sent as a Binary_ frame.

        .. _Text: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.6
        .. _Binary: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.6

        :meth:`send` also accepts an iterable of strings, bytestrings, or
        bytes-like objects to enable fragmentation_. Each item is treated as a
        message fragment and sent in its own frame. All items must be of the
        same type, or else :meth:`send` will raise a :exc:`TypeError` and the
        connection will be closed.

        .. _fragmentation: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.4

        :meth:`send` rejects dict-like objects because this is often an error.
        (If you really want to send the keys of a dict-like object as fragments,
        call its :meth:`~dict.keys` method and pass the result to :meth:`send`.)

        When the connection is closed, :meth:`send` raises
        :exc:`~websockets.exceptions.ConnectionClosed`. Specifically, it
        raises :exc:`~websockets.exceptions.ConnectionClosedOK` after a normal
        connection closure and
        :exc:`~websockets.exceptions.ConnectionClosedError` after a protocol
        error or a network failure.

        Args:
            message: Message to send.

        Raises:
            ConnectionClosed: When the connection is closed.
            RuntimeError: If a connection is busy sending a fragmented message.
            TypeError: If ``message`` doesn't have a supported type.

        """
    def close(self, code: int = ..., reason: str = '') -> None:
        """
        Perform the closing handshake.

        :meth:`close` waits for the other end to complete the handshake, for the
        TCP connection to terminate, and for all incoming messages to be read
        with :meth:`recv`.

        :meth:`close` is idempotent: it doesn't do anything once the
        connection is closed.

        Args:
            code: WebSocket close code.
            reason: WebSocket close reason.

        """
    def ping(self, data: Data | None = None) -> threading.Event:
        """
        Send a Ping_.

        .. _Ping: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.5.2

        A ping may serve as a keepalive or as a check that the remote endpoint
        received all messages up to this point

        Args:
            data: Payload of the ping. A :class:`str` will be encoded to UTF-8.
                If ``data`` is :obj:`None`, the payload is four random bytes.

        Returns:
            An event that will be set when the corresponding pong is received.
            You can ignore it if you don't intend to wait.

            ::

                pong_event = ws.ping()
                pong_event.wait()  # only if you want to wait for the pong

        Raises:
            ConnectionClosed: When the connection is closed.
            RuntimeError: If another ping was sent with the same data and
                the corresponding pong wasn't received yet.

        """
    def pong(self, data: Data = b'') -> None:
        """
        Send a Pong_.

        .. _Pong: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.5.3

        An unsolicited pong may serve as a unidirectional heartbeat.

        Args:
            data: Payload of the pong. A :class:`str` will be encoded to UTF-8.

        Raises:
            ConnectionClosed: When the connection is closed.

        """
    def process_event(self, event: Event) -> None:
        """
        Process one incoming event.

        This method is overridden in subclasses to handle the handshake.

        """
    def acknowledge_pings(self, data: bytes) -> None:
        """
        Acknowledge pings when receiving a pong.

        """
    def recv_events(self) -> None:
        """
        Read incoming data from the socket and process events.

        Run this method in a thread as long as the connection is alive.

        ``recv_events()`` exits immediately when the ``self.socket`` is closed.

        """
    def send_context(self, *, expected_state: State = ...) -> Iterator[None]:
        '''
        Create a context for writing to the connection from user code.

        On entry, :meth:`send_context` acquires the connection lock and checks
        that the connection is open; on exit, it writes outgoing data to the
        socket::

            with self.send_context():
                self.protocol.send_text(message.encode("utf-8"))

        When the connection isn\'t open on entry, when the connection is expected
        to close on exit, or when an unexpected error happens, terminating the
        connection, :meth:`send_context` waits until the connection is closed
        then raises :exc:`~websockets.exceptions.ConnectionClosed`.

        '''
    def send_data(self) -> None:
        """
        Send outgoing data.

        This method requires holding protocol_mutex.

        Raises:
            OSError: When a socket operations fails.

        """
    def set_recv_events_exc(self, exc: BaseException | None) -> None:
        """
        Set recv_events_exc, if not set yet.

        This method requires holding protocol_mutex.

        """
    def close_socket(self) -> None:
        """
        Shutdown and close socket. Close message assembler.

        Calling close_socket() guarantees that recv_events() terminates. Indeed,
        recv_events() may block only on socket.recv() or on recv_messages.put().

        """
