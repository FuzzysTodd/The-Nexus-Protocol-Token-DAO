from ._exceptions import *
import selectors
import socket
from _typeshed import Incomplete
from typing import Any, Callable

__all__ = ['WebSocketApp']

class DispatcherBase:
    """
    DispatcherBase
    """
    app: Incomplete
    ping_timeout: Incomplete
    def __init__(self, app: Any, ping_timeout: float) -> None: ...
    def timeout(self, seconds: int, callback: Callable) -> None: ...
    def reconnect(self, seconds: int, reconnector: Callable) -> None: ...

class Dispatcher(DispatcherBase):
    """
    Dispatcher
    """
    def read(self, sock: socket.socket, read_callback: Callable, check_callback: Callable) -> None: ...

class SSLDispatcher(DispatcherBase):
    """
    SSLDispatcher
    """
    def read(self, sock: socket.socket, read_callback: Callable, check_callback: Callable) -> None: ...
    def select(self, sock, sel: selectors.DefaultSelector): ...

class WrappedDispatcher:
    """
    WrappedDispatcher
    """
    app: Incomplete
    ping_timeout: Incomplete
    dispatcher: Incomplete
    def __init__(self, app, ping_timeout: float, dispatcher: Dispatcher) -> None: ...
    def read(self, sock: socket.socket, read_callback: Callable, check_callback: Callable) -> None: ...
    def timeout(self, seconds: int, callback: Callable) -> None: ...
    def reconnect(self, seconds: int, reconnector: Callable) -> None: ...

class WebSocketApp:
    """
    Higher level of APIs are provided. The interface is like JavaScript WebSocket object.
    """
    url: Incomplete
    header: Incomplete
    cookie: Incomplete
    on_open: Incomplete
    on_message: Incomplete
    on_data: Incomplete
    on_error: Incomplete
    on_close: Incomplete
    on_ping: Incomplete
    on_pong: Incomplete
    on_cont_message: Incomplete
    keep_running: bool
    get_mask_key: Incomplete
    sock: Incomplete
    last_ping_tm: int
    last_pong_tm: int
    ping_thread: Incomplete
    stop_ping: Incomplete
    ping_interval: int
    ping_timeout: Incomplete
    ping_payload: str
    subprotocols: Incomplete
    prepared_socket: Incomplete
    has_errored: bool
    has_done_teardown: bool
    has_done_teardown_lock: Incomplete
    def __init__(self, url: str, header: list | dict | Callable = None, on_open: Callable = None, on_message: Callable = None, on_error: Callable = None, on_close: Callable = None, on_ping: Callable = None, on_pong: Callable = None, on_cont_message: Callable = None, keep_running: bool = True, get_mask_key: Callable = None, cookie: str = None, subprotocols: list = None, on_data: Callable = None, socket: socket.socket = None) -> None:
        """
        WebSocketApp initialization

        Parameters
        ----------
        url: str
            Websocket url.
        header: list or dict or Callable
            Custom header for websocket handshake.
            If the parameter is a callable object, it is called just before the connection attempt.
            The returned dict or list is used as custom header value.
            This could be useful in order to properly setup timestamp dependent headers.
        on_open: function
            Callback object which is called at opening websocket.
            on_open has one argument.
            The 1st argument is this class object.
        on_message: function
            Callback object which is called when received data.
            on_message has 2 arguments.
            The 1st argument is this class object.
            The 2nd argument is utf-8 data received from the server.
        on_error: function
            Callback object which is called when we get error.
            on_error has 2 arguments.
            The 1st argument is this class object.
            The 2nd argument is exception object.
        on_close: function
            Callback object which is called when connection is closed.
            on_close has 3 arguments.
            The 1st argument is this class object.
            The 2nd argument is close_status_code.
            The 3rd argument is close_msg.
        on_cont_message: function
            Callback object which is called when a continuation
            frame is received.
            on_cont_message has 3 arguments.
            The 1st argument is this class object.
            The 2nd argument is utf-8 string which we get from the server.
            The 3rd argument is continue flag. if 0, the data continue
            to next frame data
        on_data: function
            Callback object which is called when a message received.
            This is called before on_message or on_cont_message,
            and then on_message or on_cont_message is called.
            on_data has 4 argument.
            The 1st argument is this class object.
            The 2nd argument is utf-8 string which we get from the server.
            The 3rd argument is data type. ABNF.OPCODE_TEXT or ABNF.OPCODE_BINARY will be came.
            The 4th argument is continue flag. If 0, the data continue
        keep_running: bool
            This parameter is obsolete and ignored.
        get_mask_key: function
            A callable function to get new mask keys, see the
            WebSocket.set_mask_key's docstring for more information.
        cookie: str
            Cookie value.
        subprotocols: list
            List of available sub protocols. Default is None.
        socket: socket
            Pre-initialized stream socket.
        """
    def send(self, data: str, opcode: int = ...) -> None:
        """
        send message

        Parameters
        ----------
        data: str
            Message to send. If you set opcode to OPCODE_TEXT,
            data must be utf-8 string or unicode.
        opcode: int
            Operation code of data. Default is OPCODE_TEXT.
        """
    def close(self, **kwargs) -> None:
        """
        Close websocket connection.
        """
    def run_forever(self, sockopt: tuple = None, sslopt: dict = None, ping_interval: float = 0, ping_timeout: float | None = None, ping_payload: str = '', http_proxy_host: str = None, http_proxy_port: int | str = None, http_no_proxy: list = None, http_proxy_auth: tuple = None, http_proxy_timeout: float = None, skip_utf8_validation: bool = False, host: str = None, origin: str = None, dispatcher: Dispatcher = None, suppress_origin: bool = False, proxy_type: str = None, reconnect: int = None) -> bool:
        '''
        Run event loop for WebSocket framework.

        This loop is an infinite loop and is alive while websocket is available.

        Parameters
        ----------
        sockopt: tuple
            Values for socket.setsockopt.
            sockopt must be tuple
            and each element is argument of sock.setsockopt.
        sslopt: dict
            Optional dict object for ssl socket option.
        ping_interval: int or float
            Automatically send "ping" command
            every specified period (in seconds).
            If set to 0, no ping is sent periodically.
        ping_timeout: int or float
            Timeout (in seconds) if the pong message is not received.
        ping_payload: str
            Payload message to send with each ping.
        http_proxy_host: str
            HTTP proxy host name.
        http_proxy_port: int or str
            HTTP proxy port. If not set, set to 80.
        http_no_proxy: list
            Whitelisted host names that don\'t use the proxy.
        http_proxy_timeout: int or float
            HTTP proxy timeout, default is 60 sec as per python-socks.
        http_proxy_auth: tuple
            HTTP proxy auth information. tuple of username and password. Default is None.
        skip_utf8_validation: bool
            skip utf8 validation.
        host: str
            update host header.
        origin: str
            update origin header.
        dispatcher: Dispatcher object
            customize reading data from socket.
        suppress_origin: bool
            suppress outputting origin header.
        proxy_type: str
            type of proxy from: http, socks4, socks4a, socks5, socks5h
        reconnect: int
            delay interval when reconnecting

        Returns
        -------
        teardown: bool
            False if the `WebSocketApp` is closed or caught KeyboardInterrupt,
            True if any other exception was raised during a loop.
        '''
    def create_dispatcher(self, ping_timeout: int, dispatcher: Dispatcher = None, is_ssl: bool = False) -> DispatcherBase: ...
