import enum
from .exceptions import ConnectionClosed
from .frames import Frame
from .http11 import Request, Response
from .typing import LoggerLike
from _typeshed import Incomplete
from typing import Generator, List

__all__ = ['Protocol', 'Side', 'State', 'SEND_EOF']

Event = Request | Response | Frame

class Side(enum.IntEnum):
    """A WebSocket connection is either a server or a client."""
    SERVER: Incomplete
    CLIENT: Incomplete

class State(enum.IntEnum):
    """A WebSocket connection is in one of these four states."""
    CONNECTING: Incomplete
    OPEN: Incomplete
    CLOSING: Incomplete
    CLOSED: Incomplete

SEND_EOF: bytes

class Protocol:
    '''
    Sans-I/O implementation of a WebSocket connection.

    Args:
        side: :attr:`~Side.CLIENT` or :attr:`~Side.SERVER`.
        state: initial state of the WebSocket connection.
        max_size: maximum size of incoming messages in bytes;
            :obj:`None` disables the limit.
        logger: logger for this connection; depending on ``side``,
            defaults to ``logging.getLogger("websockets.client")``
            or ``logging.getLogger("websockets.server")``;
            see the :doc:`logging guide <../../topics/logging>` for details.

    '''
    id: Incomplete
    logger: Incomplete
    debug: Incomplete
    side: Incomplete
    max_size: Incomplete
    cur_size: Incomplete
    expect_continuation_frame: bool
    origin: Incomplete
    extensions: Incomplete
    subprotocol: Incomplete
    close_rcvd: Incomplete
    close_sent: Incomplete
    close_rcvd_then_sent: Incomplete
    handshake_exc: Incomplete
    eof_sent: bool
    reader: Incomplete
    events: Incomplete
    writes: Incomplete
    parser: Incomplete
    parser_exc: Incomplete
    def __init__(self, side: Side, *, state: State = ..., max_size: int | None = ..., logger: LoggerLike | None = None) -> None: ...
    @property
    def state(self) -> State:
        """
        WebSocket connection state.

        Defined in 4.1, 4.2, 7.1.3, and 7.1.4 of :rfc:`6455`.

        """
    @state.setter
    def state(self, state: State) -> None: ...
    @property
    def close_code(self) -> int | None:
        """
        `WebSocket close code`_.

        .. _WebSocket close code:
            https://www.rfc-editor.org/rfc/rfc6455.html#section-7.1.5

        :obj:`None` if the connection isn't closed yet.

        """
    @property
    def close_reason(self) -> str | None:
        """
        `WebSocket close reason`_.

        .. _WebSocket close reason:
            https://www.rfc-editor.org/rfc/rfc6455.html#section-7.1.6

        :obj:`None` if the connection isn't closed yet.

        """
    @property
    def close_exc(self) -> ConnectionClosed:
        """
        Exception to raise when trying to interact with a closed connection.

        Don't raise this exception while the connection :attr:`state`
        is :attr:`~websockets.protocol.State.CLOSING`; wait until
        it's :attr:`~websockets.protocol.State.CLOSED`.

        Indeed, the exception includes the close code and reason, which are
        known only once the connection is closed.

        Raises:
            AssertionError: if the connection isn't closed yet.

        """
    def receive_data(self, data: bytes) -> None:
        """
        Receive data from the network.

        After calling this method:

        - You must call :meth:`data_to_send` and send this data to the network.
        - You should call :meth:`events_received` and process resulting events.

        Raises:
            EOFError: if :meth:`receive_eof` was called earlier.

        """
    def receive_eof(self) -> None:
        '''
        Receive the end of the data stream from the network.

        After calling this method:

        - You must call :meth:`data_to_send` and send this data to the network;
          it will return ``[b""]``, signaling the end of the stream, or ``[]``.
        - You aren\'t expected to call :meth:`events_received`; it won\'t return
          any new events.

        Raises:
            EOFError: if :meth:`receive_eof` was called earlier.

        '''
    def send_continuation(self, data: bytes, fin: bool) -> None:
        """
        Send a `Continuation frame`_.

        .. _Continuation frame:
            https://datatracker.ietf.org/doc/html/rfc6455#section-5.6

        Parameters:
            data: payload containing the same kind of data
                as the initial frame.
            fin: FIN bit; set it to :obj:`True` if this is the last frame
                of a fragmented message and to :obj:`False` otherwise.

        Raises:
            ProtocolError: if a fragmented message isn't in progress.

        """
    def send_text(self, data: bytes, fin: bool = True) -> None:
        """
        Send a `Text frame`_.

        .. _Text frame:
            https://datatracker.ietf.org/doc/html/rfc6455#section-5.6

        Parameters:
            data: payload containing text encoded with UTF-8.
            fin: FIN bit; set it to :obj:`False` if this is the first frame of
                a fragmented message.

        Raises:
            ProtocolError: if a fragmented message is in progress.

        """
    def send_binary(self, data: bytes, fin: bool = True) -> None:
        """
        Send a `Binary frame`_.

        .. _Binary frame:
            https://datatracker.ietf.org/doc/html/rfc6455#section-5.6

        Parameters:
            data: payload containing arbitrary binary data.
            fin: FIN bit; set it to :obj:`False` if this is the first frame of
                a fragmented message.

        Raises:
            ProtocolError: if a fragmented message is in progress.

        """
    def send_close(self, code: int | None = None, reason: str = '') -> None:
        """
        Send a `Close frame`_.

        .. _Close frame:
            https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.1

        Parameters:
            code: close code.
            reason: close reason.

        Raises:
            ProtocolError: if a fragmented message is being sent, if the code
                isn't valid, or if a reason is provided without a code

        """
    def send_ping(self, data: bytes) -> None:
        """
        Send a `Ping frame`_.

        .. _Ping frame:
            https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.2

        Parameters:
            data: payload containing arbitrary binary data.

        """
    def send_pong(self, data: bytes) -> None:
        """
        Send a `Pong frame`_.

        .. _Pong frame:
            https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.3

        Parameters:
            data: payload containing arbitrary binary data.

        """
    def fail(self, code: int, reason: str = '') -> None:
        """
        `Fail the WebSocket connection`_.

        .. _Fail the WebSocket connection:
            https://datatracker.ietf.org/doc/html/rfc6455#section-7.1.7

        Parameters:
            code: close code
            reason: close reason

        Raises:
            ProtocolError: if the code isn't valid.
        """
    def events_received(self) -> List[Event]:
        """
        Fetch events generated from data received from the network.

        Call this method immediately after any of the ``receive_*()`` methods.

        Process resulting events, likely by passing them to the application.

        Returns:
            List[Event]: Events read from the connection.
        """
    def data_to_send(self) -> List[bytes]:
        """
        Obtain data to send to the network.

        Call this method immediately after any of the ``receive_*()``,
        ``send_*()``, or :meth:`fail` methods.

        Write resulting data to the connection.

        The empty bytestring :data:`~websockets.protocol.SEND_EOF` signals
        the end of the data stream. When you receive it, half-close the TCP
        connection.

        Returns:
            List[bytes]: Data to write to the connection.

        """
    def close_expected(self) -> bool:
        """
        Tell if the TCP connection is expected to close soon.

        Call this method immediately after any of the ``receive_*()``,
        ``send_close()``, or :meth:`fail` methods.

        If it returns :obj:`True`, schedule closing the TCP connection after a
        short timeout if the other side hasn't already closed it.

        Returns:
            bool: Whether the TCP connection is expected to close soon.

        """
    def parse(self) -> Generator[None, None, None]:
        """
        Parse incoming data into frames.

        :meth:`receive_data` and :meth:`receive_eof` run this generator
        coroutine until it needs more data or reaches EOF.

        :meth:`parse` never raises an exception. Instead, it sets the
        :attr:`parser_exc` and yields control.

        """
    def discard(self) -> Generator[None, None, None]:
        """
        Discard incoming data.

        This coroutine replaces :meth:`parse`:

        - after receiving a close frame, during a normal closure (1.4);
        - after sending a close frame, during an abnormal closure (7.1.7).

        """
    def recv_frame(self, frame: Frame) -> None:
        """
        Process an incoming frame.

        """
    def send_frame(self, frame: Frame) -> None: ...
    def send_eof(self) -> None: ...
