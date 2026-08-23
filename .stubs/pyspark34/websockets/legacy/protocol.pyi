import asyncio
from ..exceptions import ConnectionClosed
from ..frames import Close
from ..typing import Data, LoggerLike
from .framing import Frame
from _typeshed import Incomplete
from typing import Any, AsyncIterable, AsyncIterator, Awaitable, Iterable

__all__ = ['WebSocketCommonProtocol', 'broadcast']

class WebSocketCommonProtocol(asyncio.Protocol):
    '''
    WebSocket connection.

    :class:`WebSocketCommonProtocol` provides APIs shared between WebSocket
    servers and clients. You shouldn\'t use it directly. Instead, use
    :class:`~websockets.client.WebSocketClientProtocol` or
    :class:`~websockets.server.WebSocketServerProtocol`.

    This documentation focuses on low-level details that aren\'t covered in the
    documentation of :class:`~websockets.client.WebSocketClientProtocol` and
    :class:`~websockets.server.WebSocketServerProtocol` for the sake of
    simplicity.

    Once the connection is open, a Ping_ frame is sent every ``ping_interval``
    seconds. This serves as a keepalive. It helps keeping the connection open,
    especially in the presence of proxies with short timeouts on inactive
    connections. Set ``ping_interval`` to :obj:`None` to disable this behavior.

    .. _Ping: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.5.2

    If the corresponding Pong_ frame isn\'t received within ``ping_timeout``
    seconds, the connection is considered unusable and is closed with code 1011.
    This ensures that the remote endpoint remains responsive. Set
    ``ping_timeout`` to :obj:`None` to disable this behavior.

    .. _Pong: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.5.3

    See the discussion of :doc:`timeouts <../../topics/timeouts>` for details.

    The ``close_timeout`` parameter defines a maximum wait time for completing
    the closing handshake and terminating the TCP connection. For legacy
    reasons, :meth:`close` completes in at most ``5 * close_timeout`` seconds
    for clients and ``4 * close_timeout`` for servers.

    ``close_timeout`` is a parameter of the protocol because websockets usually
    calls :meth:`close` implicitly upon exit:

    * on the client side, when using :func:`~websockets.client.connect` as a
      context manager;
    * on the server side, when the connection handler terminates.

    To apply a timeout to any other API, wrap it in :func:`~asyncio.timeout` or
    :func:`~asyncio.wait_for`.

    The ``max_size`` parameter enforces the maximum size for incoming messages
    in bytes. The default value is 1\xa0MiB. If a larger message is received,
    :meth:`recv` will raise :exc:`~websockets.exceptions.ConnectionClosedError`
    and the connection will be closed with code 1009.

    The ``max_queue`` parameter sets the maximum length of the queue that
    holds incoming messages. The default value is ``32``. Messages are added
    to an in-memory queue when they\'re received; then :meth:`recv` pops from
    that queue. In order to prevent excessive memory consumption when
    messages are received faster than they can be processed, the queue must
    be bounded. If the queue fills up, the protocol stops processing incoming
    data until :meth:`recv` is called. In this situation, various receive
    buffers (at least in :mod:`asyncio` and in the OS) will fill up, then the
    TCP receive window will shrink, slowing down transmission to avoid packet
    loss.

    Since Python can use up to 4 bytes of memory to represent a single
    character, each connection may use up to ``4 * max_size * max_queue``
    bytes of memory to store incoming messages. By default, this is 128\xa0MiB.
    You may want to lower the limits, depending on your application\'s
    requirements.

    The ``read_limit`` argument sets the high-water limit of the buffer for
    incoming bytes. The low-water limit is half the high-water limit. The
    default value is 64\xa0KiB, half of asyncio\'s default (based on the current
    implementation of :class:`~asyncio.StreamReader`).

    The ``write_limit`` argument sets the high-water limit of the buffer for
    outgoing bytes. The low-water limit is a quarter of the high-water limit.
    The default value is 64\xa0KiB, equal to asyncio\'s default (based on the
    current implementation of ``FlowControlMixin``).

    See the discussion of :doc:`memory usage <../../topics/memory>` for details.

    Args:
        logger: Logger for this server.
            It defaults to ``logging.getLogger("websockets.protocol")``.
            See the :doc:`logging guide <../../topics/logging>` for details.
        ping_interval: Delay between keepalive pings in seconds.
            :obj:`None` disables keepalive pings.
        ping_timeout: Timeout for keepalive pings in seconds.
            :obj:`None` disables timeouts.
        close_timeout: Timeout for closing the connection in seconds.
            For legacy reasons, the actual timeout is 4 or 5 times larger.
        max_size: Maximum size of incoming messages in bytes.
            :obj:`None` disables the limit.
        max_queue: Maximum number of incoming messages in receive buffer.
            :obj:`None` disables the limit.
        read_limit: High-water mark of read buffer in bytes.
        write_limit: High-water mark of write buffer in bytes.

    '''
    is_client: bool
    side: str
    ping_interval: Incomplete
    ping_timeout: Incomplete
    close_timeout: Incomplete
    max_size: Incomplete
    max_queue: Incomplete
    read_limit: Incomplete
    write_limit: Incomplete
    id: Incomplete
    logger: Incomplete
    debug: Incomplete
    loop: Incomplete
    legacy_recv: Incomplete
    reader: Incomplete
    state: Incomplete
    path: Incomplete
    request_headers: Incomplete
    response_headers: Incomplete
    extensions: Incomplete
    subprotocol: Incomplete
    close_rcvd: Incomplete
    close_sent: Incomplete
    close_rcvd_then_sent: Incomplete
    connection_lost_waiter: Incomplete
    messages: Incomplete
    pings: Incomplete
    latency: int
    transfer_data_task: Incomplete
    transfer_data_exc: Incomplete
    keepalive_ping_task: Incomplete
    close_connection_task: Incomplete
    def __init__(self, *, logger: LoggerLike | None = None, ping_interval: float | None = 20, ping_timeout: float | None = 20, close_timeout: float | None = None, max_size: int | None = ..., max_queue: int | None = ..., read_limit: int = ..., write_limit: int = ..., host: str | None = None, port: int | None = None, secure: bool | None = None, legacy_recv: bool = False, loop: asyncio.AbstractEventLoop | None = None, timeout: float | None = None) -> None: ...
    def connection_open(self) -> None:
        """
        Callback when the WebSocket opening handshake completes.

        Enter the OPEN state and start the data transfer phase.

        """
    @property
    def host(self) -> str | None: ...
    @property
    def port(self) -> int | None: ...
    @property
    def secure(self) -> bool | None: ...
    @property
    def local_address(self) -> Any:
        """
        Local address of the connection.

        For IPv4 connections, this is a ``(host, port)`` tuple.

        The format of the address depends on the address family;
        see :meth:`~socket.socket.getsockname`.

        :obj:`None` if the TCP connection isn't established yet.

        """
    @property
    def remote_address(self) -> Any:
        """
        Remote address of the connection.

        For IPv4 connections, this is a ``(host, port)`` tuple.

        The format of the address depends on the address family;
        see :meth:`~socket.socket.getpeername`.

        :obj:`None` if the TCP connection isn't established yet.

        """
    @property
    def open(self) -> bool:
        """
        :obj:`True` when the connection is open; :obj:`False` otherwise.

        This attribute may be used to detect disconnections. However, this
        approach is discouraged per the EAFP_ principle. Instead, you should
        handle :exc:`~websockets.exceptions.ConnectionClosed` exceptions.

        .. _EAFP: https://docs.python.org/3/glossary.html#term-eafp

        """
    @property
    def closed(self) -> bool:
        """
        :obj:`True` when the connection is closed; :obj:`False` otherwise.

        Be aware that both :attr:`open` and :attr:`closed` are :obj:`False`
        during the opening and closing sequences.

        """
    @property
    def close_code(self) -> int | None:
        """
        WebSocket close code, defined in `section 7.1.5 of RFC 6455`_.

        .. _section 7.1.5 of RFC 6455:
            https://www.rfc-editor.org/rfc/rfc6455.html#section-7.1.5

        :obj:`None` if the connection isn't closed yet.

        """
    @property
    def close_reason(self) -> str | None:
        """
        WebSocket close reason, defined in `section 7.1.6 of RFC 6455`_.

        .. _section 7.1.6 of RFC 6455:
            https://www.rfc-editor.org/rfc/rfc6455.html#section-7.1.6

        :obj:`None` if the connection isn't closed yet.

        """
    async def __aiter__(self) -> AsyncIterator[Data]:
        """
        Iterate on incoming messages.

        The iterator exits normally when the connection is closed with the close
        code 1000 (OK) or 1001 (going away) or without a close code.

        It raises a :exc:`~websockets.exceptions.ConnectionClosedError`
        exception when the connection is closed with any other code.

        """
    async def recv(self) -> Data:
        """
        Receive the next message.

        When the connection is closed, :meth:`recv` raises
        :exc:`~websockets.exceptions.ConnectionClosed`. Specifically, it raises
        :exc:`~websockets.exceptions.ConnectionClosedOK` after a normal
        connection closure and
        :exc:`~websockets.exceptions.ConnectionClosedError` after a protocol
        error or a network failure. This is how you detect the end of the
        message stream.

        Canceling :meth:`recv` is safe. There's no risk of losing the next
        message. The next invocation of :meth:`recv` will return it.

        This makes it possible to enforce a timeout by wrapping :meth:`recv` in
        :func:`~asyncio.timeout` or :func:`~asyncio.wait_for`.

        Returns:
            Data: A string (:class:`str`) for a Text_ frame. A bytestring
            (:class:`bytes`) for a Binary_ frame.

            .. _Text: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.6
            .. _Binary: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.6

        Raises:
            ConnectionClosed: When the connection is closed.
            RuntimeError: If two coroutines call :meth:`recv` concurrently.

        """
    async def send(self, message: Data | Iterable[Data] | AsyncIterable[Data]) -> None:
        """
        Send a message.

        A string (:class:`str`) is sent as a Text_ frame. A bytestring or
        bytes-like object (:class:`bytes`, :class:`bytearray`, or
        :class:`memoryview`) is sent as a Binary_ frame.

        .. _Text: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.6
        .. _Binary: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.6

        :meth:`send` also accepts an iterable or an asynchronous iterable of
        strings, bytestrings, or bytes-like objects to enable fragmentation_.
        Each item is treated as a message fragment and sent in its own frame.
        All items must be of the same type, or else :meth:`send` will raise a
        :exc:`TypeError` and the connection will be closed.

        .. _fragmentation: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.4

        :meth:`send` rejects dict-like objects because this is often an error.
        (If you want to send the keys of a dict-like object as fragments, call
        its :meth:`~dict.keys` method and pass the result to :meth:`send`.)

        Canceling :meth:`send` is discouraged. Instead, you should close the
        connection with :meth:`close`. Indeed, there are only two situations
        where :meth:`send` may yield control to the event loop and then get
        canceled; in both cases, :meth:`close` has the same effect and is
        more clear:

        1. The write buffer is full. If you don't want to wait until enough
           data is sent, your only alternative is to close the connection.
           :meth:`close` will likely time out then abort the TCP connection.
        2. ``message`` is an asynchronous iterator that yields control.
           Stopping in the middle of a fragmented message will cause a
           protocol error and the connection will be closed.

        When the connection is closed, :meth:`send` raises
        :exc:`~websockets.exceptions.ConnectionClosed`. Specifically, it
        raises :exc:`~websockets.exceptions.ConnectionClosedOK` after a normal
        connection closure and
        :exc:`~websockets.exceptions.ConnectionClosedError` after a protocol
        error or a network failure.

        Args:
            message (Union[Data, Iterable[Data], AsyncIterable[Data]): message
                to send.

        Raises:
            ConnectionClosed: When the connection is closed.
            TypeError: If ``message`` doesn't have a supported type.

        """
    async def close(self, code: int = ..., reason: str = '') -> None:
        """
        Perform the closing handshake.

        :meth:`close` waits for the other end to complete the handshake and
        for the TCP connection to terminate. As a consequence, there's no need
        to await :meth:`wait_closed` after :meth:`close`.

        :meth:`close` is idempotent: it doesn't do anything once the
        connection is closed.

        Wrapping :func:`close` in :func:`~asyncio.create_task` is safe, given
        that errors during connection termination aren't particularly useful.

        Canceling :meth:`close` is discouraged. If it takes too long, you can
        set a shorter ``close_timeout``. If you don't want to wait, let the
        Python process exit, then the OS will take care of closing the TCP
        connection.

        Args:
            code: WebSocket close code.
            reason: WebSocket close reason.

        """
    async def wait_closed(self) -> None:
        """
        Wait until the connection is closed.

        This coroutine is identical to the :attr:`closed` attribute, except it
        can be awaited.

        This can make it easier to detect connection termination, regardless
        of its cause, in tasks that interact with the WebSocket connection.

        """
    async def ping(self, data: Data | None = None) -> Awaitable[None]:
        """
        Send a Ping_.

        .. _Ping: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.5.2

        A ping may serve as a keepalive, as a check that the remote endpoint
        received all messages up to this point, or to measure :attr:`latency`.

        Canceling :meth:`ping` is discouraged. If :meth:`ping` doesn't return
        immediately, it means the write buffer is full. If you don't want to
        wait, you should close the connection.

        Canceling the :class:`~asyncio.Future` returned by :meth:`ping` has no
        effect.

        Args:
            data (Optional[Data]): payload of the ping; a string will be
                encoded to UTF-8; or :obj:`None` to generate a payload
                containing four random bytes.

        Returns:
            ~asyncio.Future[float]: A future that will be completed when the
            corresponding pong is received. You can ignore it if you don't
            intend to wait. The result of the future is the latency of the
            connection in seconds.

            ::

                pong_waiter = await ws.ping()
                # only if you want to wait for the corresponding pong
                latency = await pong_waiter

        Raises:
            ConnectionClosed: When the connection is closed.
            RuntimeError: If another ping was sent with the same data and
                the corresponding pong wasn't received yet.

        """
    async def pong(self, data: Data = b'') -> None:
        """
        Send a Pong_.

        .. _Pong: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.5.3

        An unsolicited pong may serve as a unidirectional heartbeat.

        Canceling :meth:`pong` is discouraged. If :meth:`pong` doesn't return
        immediately, it means the write buffer is full. If you don't want to
        wait, you should close the connection.

        Args:
            data (Data): Payload of the pong. A string will be encoded to
                UTF-8.

        Raises:
            ConnectionClosed: When the connection is closed.

        """
    def connection_closed_exc(self) -> ConnectionClosed: ...
    async def ensure_open(self) -> None:
        """
        Check that the WebSocket connection is open.

        Raise :exc:`~websockets.exceptions.ConnectionClosed` if it isn't.

        """
    async def transfer_data(self) -> None:
        """
        Read incoming messages and put them in a queue.

        This coroutine runs in a task until the closing handshake is started.

        """
    async def read_message(self) -> Data | None:
        """
        Read a single message from the connection.

        Re-assemble data frames if the message is fragmented.

        Return :obj:`None` when the closing handshake is started.

        """
    async def read_data_frame(self, max_size: int | None) -> Frame | None:
        """
        Read a single data frame from the connection.

        Process control frames received before the next data frame.

        Return :obj:`None` if a close frame is encountered before any data frame.

        """
    async def read_frame(self, max_size: int | None) -> Frame:
        """
        Read a single frame from the connection.

        """
    def write_frame_sync(self, fin: bool, opcode: int, data: bytes) -> None: ...
    async def drain(self) -> None: ...
    async def write_frame(self, fin: bool, opcode: int, data: bytes, *, _state: int = ...) -> None: ...
    async def write_close_frame(self, close: Close, data: bytes | None = None) -> None:
        """
        Write a close frame if and only if the connection state is OPEN.

        This dedicated coroutine must be used for writing close frames to
        ensure that at most one close frame is sent on a given connection.

        """
    async def keepalive_ping(self) -> None:
        """
        Send a Ping frame and wait for a Pong frame at regular intervals.

        This coroutine exits when the connection terminates and one of the
        following happens:

        - :meth:`ping` raises :exc:`ConnectionClosed`, or
        - :meth:`close_connection` cancels :attr:`keepalive_ping_task`.

        """
    async def close_connection(self) -> None:
        """
        7.1.1. Close the WebSocket Connection

        When the opening handshake succeeds, :meth:`connection_open` starts
        this coroutine in a task. It waits for the data transfer phase to
        complete then it closes the TCP connection cleanly.

        When the opening handshake fails, :meth:`fail_connection` does the
        same. There's no data transfer phase in that case.

        """
    async def close_transport(self) -> None:
        """
        Close the TCP connection.

        """
    async def wait_for_connection_lost(self) -> bool:
        """
        Wait until the TCP connection is closed or ``self.close_timeout`` elapses.

        Return :obj:`True` if the connection is closed and :obj:`False`
        otherwise.

        """
    def fail_connection(self, code: int = ..., reason: str = '') -> None:
        """
        7.1.7. Fail the WebSocket Connection

        This requires:

        1. Stopping all processing of incoming data, which means cancelling
           :attr:`transfer_data_task`. The close code will be 1006 unless a
           close frame was received earlier.

        2. Sending a close frame with an appropriate code if the opening
           handshake succeeded and the other side is likely to process it.

        3. Closing the connection. :meth:`close_connection` takes care of
           this once :attr:`transfer_data_task` exits after being canceled.

        (The specification describes these steps in the opposite order.)

        """
    def abort_pings(self) -> None:
        """
        Raise ConnectionClosed in pending keepalive pings.

        They'll never receive a pong once the connection is closed.

        """
    transport: Incomplete
    def connection_made(self, transport: asyncio.BaseTransport) -> None:
        """
        Configure write buffer limits.

        The high-water limit is defined by ``self.write_limit``.

        The low-water limit currently defaults to ``self.write_limit // 4`` in
        :meth:`~asyncio.WriteTransport.set_write_buffer_limits`, which should
        be all right for reasonable use cases of this library.

        This is the earliest point where we can get hold of the transport,
        which means it's the best point for configuring it.

        """
    def connection_lost(self, exc: Exception | None) -> None:
        """
        7.1.4. The WebSocket Connection is Closed.

        """
    def pause_writing(self) -> None: ...
    def resume_writing(self) -> None: ...
    def data_received(self, data: bytes) -> None: ...
    def eof_received(self) -> None:
        """
        Close the transport after receiving EOF.

        The WebSocket protocol has its own closing handshake: endpoints close
        the TCP or TLS connection after sending and receiving a close frame.

        As a consequence, they never need to write after receiving EOF, so
        there's no reason to keep the transport open by returning :obj:`True`.

        Besides, that doesn't work on TLS connections.

        """

def broadcast(websockets: Iterable[WebSocketCommonProtocol], message: Data, raise_exceptions: bool = False) -> None:
    """
    Broadcast a message to several WebSocket connections.

    A string (:class:`str`) is sent as a Text_ frame. A bytestring or bytes-like
    object (:class:`bytes`, :class:`bytearray`, or :class:`memoryview`) is sent
    as a Binary_ frame.

    .. _Text: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.6
    .. _Binary: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.6

    :func:`broadcast` pushes the message synchronously to all connections even
    if their write buffers are overflowing. There's no backpressure.

    If you broadcast messages faster than a connection can handle them, messages
    will pile up in its write buffer until the connection times out. Keep
    ``ping_interval`` and ``ping_timeout`` low to prevent excessive memory usage
    from slow connections.

    Unlike :meth:`~websockets.server.WebSocketServerProtocol.send`,
    :func:`broadcast` doesn't support sending fragmented messages. Indeed,
    fragmentation is useful for sending large messages without buffering them in
    memory, while :func:`broadcast` buffers one copy per connection as fast as
    possible.

    :func:`broadcast` skips connections that aren't open in order to avoid
    errors on connections where the closing handshake is in progress.

    :func:`broadcast` ignores failures to write the message on some connections.
    It continues writing to other connections. On Python 3.11 and above, you
    may set ``raise_exceptions`` to :obj:`True` to record failures and raise all
    exceptions in a :pep:`654` :exc:`ExceptionGroup`.

    Args:
        websockets: WebSocket connections to which the message will be sent.
        message: Message to send.
        raise_exceptions: Whether to raise an exception in case of failures.

    Raises:
        TypeError: If ``message`` doesn't have a supported type.

    """
