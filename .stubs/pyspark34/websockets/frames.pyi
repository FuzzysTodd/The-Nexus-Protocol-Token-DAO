import dataclasses
import enum
from . import extensions
from .typing import Data
from _typeshed import Incomplete
from typing import Callable, Generator, Sequence, Tuple

__all__ = ['Opcode', 'OP_CONT', 'OP_TEXT', 'OP_BINARY', 'OP_CLOSE', 'OP_PING', 'OP_PONG', 'DATA_OPCODES', 'CTRL_OPCODES', 'Frame', 'prepare_data', 'prepare_ctrl', 'Close']

class Opcode(enum.IntEnum):
    """Opcode values for WebSocket frames."""
    CONT: Incomplete
    TEXT: Incomplete
    BINARY: Incomplete
    CLOSE: Incomplete
    PING: Incomplete
    PONG: Incomplete

OP_CONT: Incomplete
OP_TEXT: Incomplete
OP_BINARY: Incomplete
OP_CLOSE: Incomplete
OP_PING: Incomplete
OP_PONG: Incomplete
DATA_OPCODES: Incomplete
CTRL_OPCODES: Incomplete

class CloseCode(enum.IntEnum):
    """Close code values for WebSocket close frames."""
    NORMAL_CLOSURE: int
    GOING_AWAY: int
    PROTOCOL_ERROR: int
    UNSUPPORTED_DATA: int
    NO_STATUS_RCVD: int
    ABNORMAL_CLOSURE: int
    INVALID_DATA: int
    POLICY_VIOLATION: int
    MESSAGE_TOO_BIG: int
    MANDATORY_EXTENSION: int
    INTERNAL_ERROR: int
    SERVICE_RESTART: int
    TRY_AGAIN_LATER: int
    BAD_GATEWAY: int
    TLS_HANDSHAKE: int

@dataclasses.dataclass
class Frame:
    """
    WebSocket frame.

    Attributes:
        opcode: Opcode.
        data: Payload data.
        fin: FIN bit.
        rsv1: RSV1 bit.
        rsv2: RSV2 bit.
        rsv3: RSV3 bit.

    Only these fields are needed. The MASK bit, payload length and masking-key
    are handled on the fly when parsing and serializing frames.

    """
    opcode: Opcode
    data: bytes
    fin: bool = ...
    rsv1: bool = ...
    rsv2: bool = ...
    rsv3: bool = ...
    @classmethod
    def parse(cls, read_exact: Callable[[int], Generator[None, None, bytes]], *, mask: bool, max_size: int | None = None, extensions: Sequence[extensions.Extension] | None = None) -> Generator[None, None, Frame]:
        """
        Parse a WebSocket frame.

        This is a generator-based coroutine.

        Args:
            read_exact: generator-based coroutine that reads the requested
                bytes or raises an exception if there isn't enough data.
            mask: whether the frame should be masked i.e. whether the read
                happens on the server side.
            max_size: maximum payload size in bytes.
            extensions: list of extensions, applied in reverse order.

        Raises:
            EOFError: if the connection is closed without a full WebSocket frame.
            UnicodeDecodeError: if the frame contains invalid UTF-8.
            PayloadTooBig: if the frame's payload size exceeds ``max_size``.
            ProtocolError: if the frame contains incorrect values.

        """
    def serialize(self, *, mask: bool, extensions: Sequence[extensions.Extension] | None = None) -> bytes:
        """
        Serialize a WebSocket frame.

        Args:
            mask: whether the frame should be masked i.e. whether the write
                happens on the client side.
            extensions: list of extensions, applied in order.

        Raises:
            ProtocolError: if the frame contains incorrect values.

        """
    def check(self) -> None:
        """
        Check that reserved bits and opcode have acceptable values.

        Raises:
            ProtocolError: if a reserved bit or the opcode is invalid.

        """
    def __init__(self, opcode, data, fin, rsv1, rsv2, rsv3) -> None: ...

def prepare_data(data: Data) -> Tuple[int, bytes]:
    """
    Convert a string or byte-like object to an opcode and a bytes-like object.

    This function is designed for data frames.

    If ``data`` is a :class:`str`, return ``OP_TEXT`` and a :class:`bytes`
    object encoding ``data`` in UTF-8.

    If ``data`` is a bytes-like object, return ``OP_BINARY`` and a bytes-like
    object.

    Raises:
        TypeError: if ``data`` doesn't have a supported type.

    """
def prepare_ctrl(data: Data) -> bytes:
    """
    Convert a string or byte-like object to bytes.

    This function is designed for ping and pong frames.

    If ``data`` is a :class:`str`, return a :class:`bytes` object encoding
    ``data`` in UTF-8.

    If ``data`` is a bytes-like object, return a :class:`bytes` object.

    Raises:
        TypeError: if ``data`` doesn't have a supported type.

    """

@dataclasses.dataclass
class Close:
    """
    Code and reason for WebSocket close frames.

    Attributes:
        code: Close code.
        reason: Close reason.

    """
    code: int
    reason: str
    @classmethod
    def parse(cls, data: bytes) -> Close:
        """
        Parse the payload of a close frame.

        Args:
            data: payload of the close frame.

        Raises:
            ProtocolError: if data is ill-formed.
            UnicodeDecodeError: if the reason isn't valid UTF-8.

        """
    def serialize(self) -> bytes:
        """
        Serialize the payload of a close frame.

        """
    def check(self) -> None:
        """
        Check that the close code has a valid value for a close frame.

        Raises:
            ProtocolError: if the close code is invalid.

        """
    def __init__(self, code, reason) -> None: ...
