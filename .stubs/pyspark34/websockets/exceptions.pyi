from . import datastructures, frames, http11
from .typing import StatusLike
from _typeshed import Incomplete

__all__ = ['WebSocketException', 'ConnectionClosed', 'ConnectionClosedError', 'ConnectionClosedOK', 'InvalidHandshake', 'SecurityError', 'InvalidMessage', 'InvalidHeader', 'InvalidHeaderFormat', 'InvalidHeaderValue', 'InvalidOrigin', 'InvalidUpgrade', 'InvalidStatus', 'InvalidStatusCode', 'NegotiationError', 'DuplicateParameter', 'InvalidParameterName', 'InvalidParameterValue', 'AbortHandshake', 'RedirectHandshake', 'InvalidState', 'InvalidURI', 'PayloadTooBig', 'ProtocolError', 'WebSocketProtocolError']

class WebSocketException(Exception):
    """
    Base class for all exceptions defined by websockets.

    """

class ConnectionClosed(WebSocketException):
    """
    Raised when trying to interact with a closed connection.

    Attributes:
        rcvd (Optional[Close]): if a close frame was received, its code and
            reason are available in ``rcvd.code`` and ``rcvd.reason``.
        sent (Optional[Close]): if a close frame was sent, its code and reason
            are available in ``sent.code`` and ``sent.reason``.
        rcvd_then_sent (Optional[bool]): if close frames were received and
            sent, this attribute tells in which order this happened, from the
            perspective of this side of the connection.

    """
    rcvd: Incomplete
    sent: Incomplete
    rcvd_then_sent: Incomplete
    def __init__(self, rcvd: frames.Close | None, sent: frames.Close | None, rcvd_then_sent: bool | None = None) -> None: ...
    @property
    def code(self) -> int: ...
    @property
    def reason(self) -> str: ...

class ConnectionClosedError(ConnectionClosed):
    """
    Like :exc:`ConnectionClosed`, when the connection terminated with an error.

    A close frame with a code other than 1000 (OK) or 1001 (going away) was
    received or sent, or the closing handshake didn't complete properly.

    """
class ConnectionClosedOK(ConnectionClosed):
    """
    Like :exc:`ConnectionClosed`, when the connection terminated properly.

    A close code with code 1000 (OK) or 1001 (going away) or without a code was
    received and sent.

    """
class InvalidHandshake(WebSocketException):
    """
    Raised during the handshake when the WebSocket connection fails.

    """
class SecurityError(InvalidHandshake):
    """
    Raised when a handshake request or response breaks a security rule.

    Security limits are hard coded.

    """
class InvalidMessage(InvalidHandshake):
    """
    Raised when a handshake request or response is malformed.

    """

class InvalidHeader(InvalidHandshake):
    """
    Raised when an HTTP header doesn't have a valid format or value.

    """
    name: Incomplete
    value: Incomplete
    def __init__(self, name: str, value: str | None = None) -> None: ...

class InvalidHeaderFormat(InvalidHeader):
    """
    Raised when an HTTP header cannot be parsed.

    The format of the header doesn't match the grammar for that header.

    """
    def __init__(self, name: str, error: str, header: str, pos: int) -> None: ...

class InvalidHeaderValue(InvalidHeader):
    """
    Raised when an HTTP header has a wrong value.

    The format of the header is correct but a value isn't acceptable.

    """

class InvalidOrigin(InvalidHeader):
    """
    Raised when the Origin header in a request isn't allowed.

    """
    def __init__(self, origin: str | None) -> None: ...

class InvalidUpgrade(InvalidHeader):
    """
    Raised when the Upgrade or Connection header isn't correct.

    """

class InvalidStatus(InvalidHandshake):
    """
    Raised when a handshake response rejects the WebSocket upgrade.

    """
    response: Incomplete
    def __init__(self, response: http11.Response) -> None: ...

class InvalidStatusCode(InvalidHandshake):
    """
    Raised when a handshake response status code is invalid.

    """
    status_code: Incomplete
    headers: Incomplete
    def __init__(self, status_code: int, headers: datastructures.Headers) -> None: ...

class NegotiationError(InvalidHandshake):
    """
    Raised when negotiating an extension fails.

    """

class DuplicateParameter(NegotiationError):
    """
    Raised when a parameter name is repeated in an extension header.

    """
    name: Incomplete
    def __init__(self, name: str) -> None: ...

class InvalidParameterName(NegotiationError):
    """
    Raised when a parameter name in an extension header is invalid.

    """
    name: Incomplete
    def __init__(self, name: str) -> None: ...

class InvalidParameterValue(NegotiationError):
    """
    Raised when a parameter value in an extension header is invalid.

    """
    name: Incomplete
    value: Incomplete
    def __init__(self, name: str, value: str | None) -> None: ...

class AbortHandshake(InvalidHandshake):
    """
    Raised to abort the handshake on purpose and return an HTTP response.

    This exception is an implementation detail.

    The public API
    is :meth:`~websockets.server.WebSocketServerProtocol.process_request`.

    Attributes:
        status (~http.HTTPStatus): HTTP status code.
        headers (Headers): HTTP response headers.
        body (bytes): HTTP response body.
    """
    status: Incomplete
    headers: Incomplete
    body: Incomplete
    def __init__(self, status: StatusLike, headers: datastructures.HeadersLike, body: bytes = b'') -> None: ...

class RedirectHandshake(InvalidHandshake):
    """
    Raised when a handshake gets redirected.

    This exception is an implementation detail.

    """
    uri: Incomplete
    def __init__(self, uri: str) -> None: ...

class InvalidState(WebSocketException, AssertionError):
    """
    Raised when an operation is forbidden in the current state.

    This exception is an implementation detail.

    It should never be raised in normal circumstances.

    """

class InvalidURI(WebSocketException):
    """
    Raised when connecting to a URI that isn't a valid WebSocket URI.

    """
    uri: Incomplete
    msg: Incomplete
    def __init__(self, uri: str, msg: str) -> None: ...

class PayloadTooBig(WebSocketException):
    """
    Raised when receiving a frame with a payload exceeding the maximum size.

    """
class ProtocolError(WebSocketException):
    """
    Raised when a frame breaks the protocol.

    """
WebSocketProtocolError = ProtocolError
