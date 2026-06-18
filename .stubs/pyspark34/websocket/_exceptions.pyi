from _typeshed import Incomplete

class WebSocketException(Exception):
    """
    WebSocket exception class.
    """
class WebSocketProtocolException(WebSocketException):
    """
    If the WebSocket protocol is invalid, this exception will be raised.
    """
class WebSocketPayloadException(WebSocketException):
    """
    If the WebSocket payload is invalid, this exception will be raised.
    """
class WebSocketConnectionClosedException(WebSocketException):
    """
    If remote host closed the connection or some network error happened,
    this exception will be raised.
    """
class WebSocketTimeoutException(WebSocketException):
    """
    WebSocketTimeoutException will be raised at socket timeout during read/write data.
    """
class WebSocketProxyException(WebSocketException):
    """
    WebSocketProxyException will be raised when proxy error occurred.
    """

class WebSocketBadStatusException(WebSocketException):
    """
    WebSocketBadStatusException will be raised when we get bad handshake status code.
    """
    status_code: Incomplete
    resp_headers: Incomplete
    resp_body: Incomplete
    def __init__(self, message: str, status_code: int, status_message: Incomplete | None = None, resp_headers: Incomplete | None = None, resp_body: Incomplete | None = None) -> None: ...

class WebSocketAddressException(WebSocketException):
    """
    If the websocket address info cannot be found, this exception will be raised.
    """
