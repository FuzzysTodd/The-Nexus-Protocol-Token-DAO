import asyncio
from .base_protocol import BaseProtocol
from .streams import DataQueue
from .typedefs import Final
from _typeshed import Incomplete
from enum import IntEnum
from typing import Any, Callable, List, NamedTuple, Tuple

__all__ = ['WS_CLOSED_MESSAGE', 'WS_CLOSING_MESSAGE', 'WS_KEY', 'WebSocketReader', 'WebSocketWriter', 'WSMessage', 'WebSocketError', 'WSMsgType', 'WSCloseCode']

class WSCloseCode(IntEnum):
    OK: int
    GOING_AWAY: int
    PROTOCOL_ERROR: int
    UNSUPPORTED_DATA: int
    ABNORMAL_CLOSURE: int
    INVALID_TEXT: int
    POLICY_VIOLATION: int
    MESSAGE_TOO_BIG: int
    MANDATORY_EXTENSION: int
    INTERNAL_ERROR: int
    SERVICE_RESTART: int
    TRY_AGAIN_LATER: int
    BAD_GATEWAY: int

class WSMsgType(IntEnum):
    CONTINUATION: int
    TEXT: int
    BINARY: int
    PING: int
    PONG: int
    CLOSE: int
    CLOSING: int
    CLOSED: int
    ERROR: int
    text = TEXT
    binary = BINARY
    ping = PING
    pong = PONG
    close = CLOSE
    closing = CLOSING
    closed = CLOSED
    error = ERROR

WS_KEY: Final[bytes]

class _WSMessageBase(NamedTuple):
    type: Incomplete
    data: Incomplete
    extra: Incomplete

class WSMessage(_WSMessageBase):
    def json(self, *, loads: Callable[[Any], Any] = ...) -> Any:
        """Return parsed JSON data.

        .. versionadded:: 0.22
        """

WS_CLOSED_MESSAGE: Incomplete
WS_CLOSING_MESSAGE: Incomplete

class WebSocketError(Exception):
    """WebSocket protocol parser error."""
    code: Incomplete
    def __init__(self, code: int, message: str) -> None: ...

class WSHandshakeError(Exception):
    """WebSocket protocol handshake error."""

class WSParserState(IntEnum):
    READ_HEADER: int
    READ_PAYLOAD_LENGTH: int
    READ_PAYLOAD_MASK: int
    READ_PAYLOAD: int

class WebSocketReader:
    queue: Incomplete
    def __init__(self, queue: DataQueue[WSMessage], max_msg_size: int, compress: bool = True) -> None: ...
    def feed_eof(self) -> None: ...
    def feed_data(self, data: bytes) -> Tuple[bool, bytes]: ...
    def parse_frame(self, buf: bytes) -> List[Tuple[bool, int | None, bytearray, bool | None]]:
        """Return the next frame from the socket."""

class WebSocketWriter:
    protocol: Incomplete
    transport: Incomplete
    use_mask: Incomplete
    randrange: Incomplete
    compress: Incomplete
    notakeover: Incomplete
    def __init__(self, protocol: BaseProtocol, transport: asyncio.Transport, *, use_mask: bool = False, limit: int = ..., random: Any = ..., compress: int = 0, notakeover: bool = False) -> None: ...
    async def pong(self, message: bytes = b'') -> None:
        """Send pong message."""
    async def ping(self, message: bytes = b'') -> None:
        """Send ping message."""
    async def send(self, message: str | bytes, binary: bool = False, compress: int | None = None) -> None:
        """Send a frame over the websocket with message as its payload."""
    async def close(self, code: int = 1000, message: bytes = b'') -> None:
        """Close the websocket, sending the specified code and message."""
