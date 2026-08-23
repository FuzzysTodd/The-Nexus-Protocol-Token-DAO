import abc
import tornado
from _typeshed import Incomplete
from tornado import gen as gen, httpclient as httpclient, httputil as httputil, simple_httpclient as simple_httpclient
from tornado.concurrent import Future as Future, future_set_result_unless_cancelled as future_set_result_unless_cancelled
from tornado.escape import native_str as native_str, to_unicode as to_unicode, utf8 as utf8
from tornado.ioloop import IOLoop as IOLoop, PeriodicCallback as PeriodicCallback
from tornado.iostream import IOStream as IOStream, StreamClosedError as StreamClosedError
from tornado.log import app_log as app_log, gen_log as gen_log
from tornado.netutil import Resolver as Resolver
from tornado.queues import Queue as Queue
from tornado.tcpclient import TCPClient as TCPClient
from types import TracebackType
from typing import Any, Awaitable, Callable, Dict, List, Type
from typing_extensions import Protocol

class _Compressor(Protocol):
    def compress(self, data: bytes) -> bytes: ...
    def flush(self, mode: int) -> bytes: ...

class _Decompressor(Protocol):
    unconsumed_tail: bytes
    def decompress(self, data: bytes, max_length: int) -> bytes: ...

class _WebSocketDelegate(Protocol):
    def on_ws_connection_close(self, close_code: int | None = None, close_reason: str | None = None) -> None: ...
    def on_message(self, message: str | bytes) -> Awaitable[None] | None: ...
    def on_ping(self, data: bytes) -> None: ...
    def on_pong(self, data: bytes) -> None: ...
    def log_exception(self, typ: Type[BaseException] | None, value: BaseException | None, tb: TracebackType | None) -> None: ...

class WebSocketError(Exception): ...
class WebSocketClosedError(WebSocketError):
    """Raised by operations on a closed connection.

    .. versionadded:: 3.2
    """
class _DecompressTooLargeError(Exception): ...

class _WebSocketParams:
    ping_interval: Incomplete
    ping_timeout: Incomplete
    max_message_size: Incomplete
    compression_options: Incomplete
    def __init__(self, ping_interval: float | None = None, ping_timeout: float | None = None, max_message_size: int = ..., compression_options: Dict[str, Any] | None = None) -> None: ...

class WebSocketHandler(tornado.web.RequestHandler):
    '''Subclass this class to create a basic WebSocket handler.

    Override `on_message` to handle incoming messages, and use
    `write_message` to send messages to the client. You can also
    override `open` and `on_close` to handle opened and closed
    connections.

    Custom upgrade response headers can be sent by overriding
    `~tornado.web.RequestHandler.set_default_headers` or
    `~tornado.web.RequestHandler.prepare`.

    See http://dev.w3.org/html5/websockets/ for details on the
    JavaScript interface.  The protocol is specified at
    http://tools.ietf.org/html/rfc6455.

    Here is an example WebSocket handler that echos back all received messages
    back to the client:

    .. testcode::

      class EchoWebSocket(tornado.websocket.WebSocketHandler):
          def open(self):
              print("WebSocket opened")

          def on_message(self, message):
              self.write_message(u"You said: " + message)

          def on_close(self):
              print("WebSocket closed")

    .. testoutput::
       :hide:

    WebSockets are not standard HTTP connections. The "handshake" is
    HTTP, but after the handshake, the protocol is
    message-based. Consequently, most of the Tornado HTTP facilities
    are not available in handlers of this type. The only communication
    methods available to you are `write_message()`, `ping()`, and
    `close()`. Likewise, your request handler class should implement
    `open()` method rather than ``get()`` or ``post()``.

    If you map the handler above to ``/websocket`` in your application, you can
    invoke it in JavaScript with::

      var ws = new WebSocket("ws://localhost:8888/websocket");
      ws.onopen = function() {
         ws.send("Hello, world");
      };
      ws.onmessage = function (evt) {
         alert(evt.data);
      };

    This script pops up an alert box that says "You said: Hello, world".

    Web browsers allow any site to open a websocket connection to any other,
    instead of using the same-origin policy that governs other network
    access from JavaScript.  This can be surprising and is a potential
    security hole, so since Tornado 4.0 `WebSocketHandler` requires
    applications that wish to receive cross-origin websockets to opt in
    by overriding the `~WebSocketHandler.check_origin` method (see that
    method\'s docs for details).  Failure to do so is the most likely
    cause of 403 errors when making a websocket connection.

    When using a secure websocket connection (``wss://``) with a self-signed
    certificate, the connection from a browser may fail because it wants
    to show the "accept this certificate" dialog but has nowhere to show it.
    You must first visit a regular HTML page using the same certificate
    to accept it before the websocket connection will succeed.

    If the application setting ``websocket_ping_interval`` has a non-zero
    value, a ping will be sent periodically, and the connection will be
    closed if a response is not received before the ``websocket_ping_timeout``.

    Messages larger than the ``websocket_max_message_size`` application setting
    (default 10MiB) will not be accepted.

    .. versionchanged:: 4.5
       Added ``websocket_ping_interval``, ``websocket_ping_timeout``, and
       ``websocket_max_message_size``.
    '''
    ws_connection: Incomplete
    close_code: Incomplete
    close_reason: Incomplete
    def __init__(self, application: tornado.web.Application, request: httputil.HTTPServerRequest, **kwargs: Any) -> None: ...
    open_args: Incomplete
    open_kwargs: Incomplete
    async def get(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def ping_interval(self) -> float | None:
        """The interval for websocket keep-alive pings.

        Set websocket_ping_interval = 0 to disable pings.
        """
    @property
    def ping_timeout(self) -> float | None:
        """If no ping is received in this many seconds,
        close the websocket connection (VPNs, etc. can fail to cleanly close ws connections).
        Default is max of 3 pings or 30 seconds.
        """
    @property
    def max_message_size(self) -> int:
        """Maximum allowed message size.

        If the remote peer sends a message larger than this, the connection
        will be closed.

        Default is 10MiB.
        """
    def write_message(self, message: bytes | str | Dict[str, Any], binary: bool = False) -> Future[None]:
        """Sends the given message to the client of this Web Socket.

        The message may be either a string or a dict (which will be
        encoded as json).  If the ``binary`` argument is false, the
        message will be sent as utf8; in binary mode any byte string
        is allowed.

        If the connection is already closed, raises `WebSocketClosedError`.
        Returns a `.Future` which can be used for flow control.

        .. versionchanged:: 3.2
           `WebSocketClosedError` was added (previously a closed connection
           would raise an `AttributeError`)

        .. versionchanged:: 4.3
           Returns a `.Future` which can be used for flow control.

        .. versionchanged:: 5.0
           Consistently raises `WebSocketClosedError`. Previously could
           sometimes raise `.StreamClosedError`.
        """
    def select_subprotocol(self, subprotocols: List[str]) -> str | None:
        """Override to implement subprotocol negotiation.

        ``subprotocols`` is a list of strings identifying the
        subprotocols proposed by the client.  This method may be
        overridden to return one of those strings to select it, or
        ``None`` to not select a subprotocol.

        Failure to select a subprotocol does not automatically abort
        the connection, although clients may close the connection if
        none of their proposed subprotocols was selected.

        The list may be empty, in which case this method must return
        None. This method is always called exactly once even if no
        subprotocols were proposed so that the handler can be advised
        of this fact.

        .. versionchanged:: 5.1

           Previously, this method was called with a list containing
           an empty string instead of an empty list if no subprotocols
           were proposed by the client.
        """
    @property
    def selected_subprotocol(self) -> str | None:
        """The subprotocol returned by `select_subprotocol`.

        .. versionadded:: 5.1
        """
    def get_compression_options(self) -> Dict[str, Any] | None:
        """Override to return compression options for the connection.

        If this method returns None (the default), compression will
        be disabled.  If it returns a dict (even an empty one), it
        will be enabled.  The contents of the dict may be used to
        control the following compression options:

        ``compression_level`` specifies the compression level.

        ``mem_level`` specifies the amount of memory used for the internal compression state.

         These parameters are documented in details here:
         https://docs.python.org/3.6/library/zlib.html#zlib.compressobj

        .. versionadded:: 4.1

        .. versionchanged:: 4.5

           Added ``compression_level`` and ``mem_level``.
        """
    def open(self, *args: str, **kwargs: str) -> Awaitable[None] | None:
        """Invoked when a new WebSocket is opened.

        The arguments to `open` are extracted from the `tornado.web.URLSpec`
        regular expression, just like the arguments to
        `tornado.web.RequestHandler.get`.

        `open` may be a coroutine. `on_message` will not be called until
        `open` has returned.

        .. versionchanged:: 5.1

           ``open`` may be a coroutine.
        """
    def on_message(self, message: str | bytes) -> Awaitable[None] | None:
        """Handle incoming messages on the WebSocket

        This method must be overridden.

        .. versionchanged:: 4.5

           ``on_message`` can be a coroutine.
        """
    def ping(self, data: str | bytes = b'') -> None:
        """Send ping frame to the remote end.

        The data argument allows a small amount of data (up to 125
        bytes) to be sent as a part of the ping message. Note that not
        all websocket implementations expose this data to
        applications.

        Consider using the ``websocket_ping_interval`` application
        setting instead of sending pings manually.

        .. versionchanged:: 5.1

           The data argument is now optional.

        """
    def on_pong(self, data: bytes) -> None:
        """Invoked when the response to a ping frame is received."""
    def on_ping(self, data: bytes) -> None:
        """Invoked when the a ping frame is received."""
    def on_close(self) -> None:
        """Invoked when the WebSocket is closed.

        If the connection was closed cleanly and a status code or reason
        phrase was supplied, these values will be available as the attributes
        ``self.close_code`` and ``self.close_reason``.

        .. versionchanged:: 4.0

           Added ``close_code`` and ``close_reason`` attributes.
        """
    def close(self, code: int | None = None, reason: str | None = None) -> None:
        """Closes this Web Socket.

        Once the close handshake is successful the socket will be closed.

        ``code`` may be a numeric status code, taken from the values
        defined in `RFC 6455 section 7.4.1
        <https://tools.ietf.org/html/rfc6455#section-7.4.1>`_.
        ``reason`` may be a textual message about why the connection is
        closing.  These values are made available to the client, but are
        not otherwise interpreted by the websocket protocol.

        .. versionchanged:: 4.0

           Added the ``code`` and ``reason`` arguments.
        """
    def check_origin(self, origin: str) -> bool:
        '''Override to enable support for allowing alternate origins.

        The ``origin`` argument is the value of the ``Origin`` HTTP
        header, the url responsible for initiating this request.  This
        method is not called for clients that do not send this header;
        such requests are always allowed (because all browsers that
        implement WebSockets support this header, and non-browser
        clients do not have the same cross-site security concerns).

        Should return ``True`` to accept the request or ``False`` to
        reject it. By default, rejects all requests with an origin on
        a host other than this one.

        This is a security protection against cross site scripting attacks on
        browsers, since WebSockets are allowed to bypass the usual same-origin
        policies and don\'t use CORS headers.

        .. warning::

           This is an important security measure; don\'t disable it
           without understanding the security implications. In
           particular, if your authentication is cookie-based, you
           must either restrict the origins allowed by
           ``check_origin()`` or implement your own XSRF-like
           protection for websocket connections. See `these
           <https://www.christian-schneider.net/CrossSiteWebSocketHijacking.html>`_
           `articles
           <https://devcenter.heroku.com/articles/websocket-security>`_
           for more.

        To accept all cross-origin traffic (which was the default prior to
        Tornado 4.0), simply override this method to always return ``True``::

            def check_origin(self, origin):
                return True

        To allow connections from any subdomain of your site, you might
        do something like::

            def check_origin(self, origin):
                parsed_origin = urllib.parse.urlparse(origin)
                return parsed_origin.netloc.endswith(".mydomain.com")

        .. versionadded:: 4.0

        '''
    def set_nodelay(self, value: bool) -> None:
        """Set the no-delay flag for this stream.

        By default, small messages may be delayed and/or combined to minimize
        the number of packets sent.  This can sometimes cause 200-500ms delays
        due to the interaction between Nagle's algorithm and TCP delayed
        ACKs.  To reduce this delay (at the expense of possibly increasing
        bandwidth usage), call ``self.set_nodelay(True)`` once the websocket
        connection is established.

        See `.BaseIOStream.set_nodelay` for additional details.

        .. versionadded:: 3.1
        """
    def on_connection_close(self) -> None: ...
    def on_ws_connection_close(self, close_code: int | None = None, close_reason: str | None = None) -> None: ...
    def get_websocket_protocol(self) -> WebSocketProtocol | None: ...

class WebSocketProtocol(abc.ABC, metaclass=abc.ABCMeta):
    """Base class for WebSocket protocol versions."""
    handler: Incomplete
    stream: Incomplete
    client_terminated: bool
    server_terminated: bool
    def __init__(self, handler: _WebSocketDelegate) -> None: ...
    def on_connection_close(self) -> None: ...
    @abc.abstractmethod
    def close(self, code: int | None = None, reason: str | None = None) -> None: ...
    @abc.abstractmethod
    def is_closing(self) -> bool: ...
    @abc.abstractmethod
    async def accept_connection(self, handler: WebSocketHandler) -> None: ...
    @abc.abstractmethod
    def write_message(self, message: str | bytes | Dict[str, Any], binary: bool = False) -> Future[None]: ...
    @property
    @abc.abstractmethod
    def selected_subprotocol(self) -> str | None: ...
    @abc.abstractmethod
    def write_ping(self, data: bytes) -> None: ...
    @abc.abstractmethod
    def start_pinging(self) -> None: ...
    @abc.abstractmethod
    def set_nodelay(self, x: bool) -> None: ...

class _PerMessageDeflateCompressor:
    def __init__(self, persistent: bool, max_wbits: int | None, compression_options: Dict[str, Any] | None = None) -> None: ...
    def compress(self, data: bytes) -> bytes: ...

class _PerMessageDeflateDecompressor:
    def __init__(self, persistent: bool, max_wbits: int | None, max_message_size: int, compression_options: Dict[str, Any] | None = None) -> None: ...
    def decompress(self, data: bytes) -> bytes: ...

class WebSocketProtocol13(WebSocketProtocol):
    """Implementation of the WebSocket protocol from RFC 6455.

    This class supports versions 7 and 8 of the protocol in addition to the
    final version 13.
    """
    FIN: int
    RSV1: int
    RSV2: int
    RSV3: int
    RSV_MASK: Incomplete
    OPCODE_MASK: int
    stream: IOStream
    mask_outgoing: Incomplete
    params: Incomplete
    ping_callback: Incomplete
    last_ping: float
    last_pong: float
    close_code: Incomplete
    close_reason: Incomplete
    def __init__(self, handler: _WebSocketDelegate, mask_outgoing: bool, params: _WebSocketParams) -> None: ...
    @property
    def selected_subprotocol(self) -> str | None: ...
    @selected_subprotocol.setter
    def selected_subprotocol(self, value: str | None) -> None: ...
    async def accept_connection(self, handler: WebSocketHandler) -> None: ...
    @staticmethod
    def compute_accept_value(key: str | bytes) -> str:
        """Computes the value for the Sec-WebSocket-Accept header,
        given the value for Sec-WebSocket-Key.
        """
    def write_message(self, message: str | bytes | Dict[str, Any], binary: bool = False) -> Future[None]:
        """Sends the given message to the client of this Web Socket."""
    def write_ping(self, data: bytes) -> None:
        """Send ping frame."""
    server_terminated: bool
    def close(self, code: int | None = None, reason: str | None = None) -> None:
        """Closes the WebSocket connection."""
    def is_closing(self) -> bool:
        """Return ``True`` if this connection is closing.

        The connection is considered closing if either side has
        initiated its closing handshake or if the stream has been
        shut down uncleanly.
        """
    @property
    def ping_interval(self) -> float | None: ...
    @property
    def ping_timeout(self) -> float | None: ...
    def start_pinging(self) -> None:
        """Start sending periodic pings to keep the connection alive"""
    def periodic_ping(self) -> None:
        """Send a ping to keep the websocket alive

        Called periodically if the websocket_ping_interval is set and non-zero.
        """
    def set_nodelay(self, x: bool) -> None: ...

class WebSocketClientConnection(simple_httpclient._HTTPConnection):
    """WebSocket client connection.

    This class should not be instantiated directly; use the
    `websocket_connect` function instead.
    """
    protocol: WebSocketProtocol
    connect_future: Incomplete
    read_queue: Incomplete
    key: Incomplete
    close_code: Incomplete
    close_reason: Incomplete
    params: Incomplete
    tcp_client: Incomplete
    def __init__(self, request: httpclient.HTTPRequest, on_message_callback: Callable[[None | str | bytes], None] | None = None, compression_options: Dict[str, Any] | None = None, ping_interval: float | None = None, ping_timeout: float | None = None, max_message_size: int = ..., subprotocols: List[str] | None = [], resolver: Resolver | None = None) -> None: ...
    def close(self, code: int | None = None, reason: str | None = None) -> None:
        """Closes the websocket connection.

        ``code`` and ``reason`` are documented under
        `WebSocketHandler.close`.

        .. versionadded:: 3.2

        .. versionchanged:: 4.0

           Added the ``code`` and ``reason`` arguments.
        """
    def on_connection_close(self) -> None: ...
    def on_ws_connection_close(self, close_code: int | None = None, close_reason: str | None = None) -> None: ...
    headers: Incomplete
    final_callback: Incomplete
    async def headers_received(self, start_line: httputil.RequestStartLine | httputil.ResponseStartLine, headers: httputil.HTTPHeaders) -> None: ...
    def write_message(self, message: str | bytes | Dict[str, Any], binary: bool = False) -> Future[None]:
        """Sends a message to the WebSocket server.

        If the stream is closed, raises `WebSocketClosedError`.
        Returns a `.Future` which can be used for flow control.

        .. versionchanged:: 5.0
           Exception raised on a closed stream changed from `.StreamClosedError`
           to `WebSocketClosedError`.
        """
    def read_message(self, callback: Callable[[Future[None | str | bytes]], None] | None = None) -> Awaitable[None | str | bytes]:
        """Reads a message from the WebSocket server.

        If on_message_callback was specified at WebSocket
        initialization, this function will never return messages

        Returns a future whose result is the message, or None
        if the connection is closed.  If a callback argument
        is given it will be called with the future when it is
        ready.
        """
    def on_message(self, message: str | bytes) -> Awaitable[None] | None: ...
    def ping(self, data: bytes = b'') -> None:
        """Send ping frame to the remote end.

        The data argument allows a small amount of data (up to 125
        bytes) to be sent as a part of the ping message. Note that not
        all websocket implementations expose this data to
        applications.

        Consider using the ``ping_interval`` argument to
        `websocket_connect` instead of sending pings manually.

        .. versionadded:: 5.1

        """
    def on_pong(self, data: bytes) -> None: ...
    def on_ping(self, data: bytes) -> None: ...
    def get_websocket_protocol(self) -> WebSocketProtocol: ...
    @property
    def selected_subprotocol(self) -> str | None:
        """The subprotocol selected by the server.

        .. versionadded:: 5.1
        """
    def log_exception(self, typ: Type[BaseException] | None, value: BaseException | None, tb: TracebackType | None) -> None: ...

def websocket_connect(url: str | httpclient.HTTPRequest, callback: Callable[[Future[WebSocketClientConnection]], None] | None = None, connect_timeout: float | None = None, on_message_callback: Callable[[None | str | bytes], None] | None = None, compression_options: Dict[str, Any] | None = None, ping_interval: float | None = None, ping_timeout: float | None = None, max_message_size: int = ..., subprotocols: List[str] | None = None, resolver: Resolver | None = None) -> Awaitable[WebSocketClientConnection]:
    """Client-side websocket support.

    Takes a url and returns a Future whose result is a
    `WebSocketClientConnection`.

    ``compression_options`` is interpreted in the same way as the
    return value of `.WebSocketHandler.get_compression_options`.

    The connection supports two styles of operation. In the coroutine
    style, the application typically calls
    `~.WebSocketClientConnection.read_message` in a loop::

        conn = yield websocket_connect(url)
        while True:
            msg = yield conn.read_message()
            if msg is None: break
            # Do something with msg

    In the callback style, pass an ``on_message_callback`` to
    ``websocket_connect``. In both styles, a message of ``None``
    indicates that the connection has been closed.

    ``subprotocols`` may be a list of strings specifying proposed
    subprotocols. The selected protocol may be found on the
    ``selected_subprotocol`` attribute of the connection object
    when the connection is complete.

    .. versionchanged:: 3.2
       Also accepts ``HTTPRequest`` objects in place of urls.

    .. versionchanged:: 4.1
       Added ``compression_options`` and ``on_message_callback``.

    .. versionchanged:: 4.5
       Added the ``ping_interval``, ``ping_timeout``, and ``max_message_size``
       arguments, which have the same meaning as in `WebSocketHandler`.

    .. versionchanged:: 5.0
       The ``io_loop`` argument (deprecated since version 4.1) has been removed.

    .. versionchanged:: 5.1
       Added the ``subprotocols`` argument.

    .. versionchanged:: 6.3
       Added the ``resolver`` argument.
    """
