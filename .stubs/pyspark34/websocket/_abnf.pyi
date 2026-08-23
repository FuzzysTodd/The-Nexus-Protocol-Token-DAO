from ._exceptions import *
from _typeshed import Incomplete
from typing import Callable

__all__ = ['ABNF', 'continuous_frame', 'frame_buffer', 'STATUS_NORMAL', 'STATUS_GOING_AWAY', 'STATUS_PROTOCOL_ERROR', 'STATUS_UNSUPPORTED_DATA_TYPE', 'STATUS_STATUS_NOT_AVAILABLE', 'STATUS_ABNORMAL_CLOSED', 'STATUS_INVALID_PAYLOAD', 'STATUS_POLICY_VIOLATION', 'STATUS_MESSAGE_TOO_BIG', 'STATUS_INVALID_EXTENSION', 'STATUS_UNEXPECTED_CONDITION', 'STATUS_BAD_GATEWAY', 'STATUS_TLS_HANDSHAKE_ERROR']

STATUS_NORMAL: int
STATUS_GOING_AWAY: int
STATUS_PROTOCOL_ERROR: int
STATUS_UNSUPPORTED_DATA_TYPE: int
STATUS_STATUS_NOT_AVAILABLE: int
STATUS_ABNORMAL_CLOSED: int
STATUS_INVALID_PAYLOAD: int
STATUS_POLICY_VIOLATION: int
STATUS_MESSAGE_TOO_BIG: int
STATUS_INVALID_EXTENSION: int
STATUS_UNEXPECTED_CONDITION: int
STATUS_BAD_GATEWAY: int
STATUS_TLS_HANDSHAKE_ERROR: int

class ABNF:
    """
    ABNF frame class.
    See http://tools.ietf.org/html/rfc5234
    and http://tools.ietf.org/html/rfc6455#section-5.2
    """
    OPCODE_CONT: int
    OPCODE_TEXT: int
    OPCODE_BINARY: int
    OPCODE_CLOSE: int
    OPCODE_PING: int
    OPCODE_PONG: int
    OPCODES: Incomplete
    OPCODE_MAP: Incomplete
    LENGTH_7: int
    LENGTH_16: Incomplete
    LENGTH_63: Incomplete
    fin: Incomplete
    rsv1: Incomplete
    rsv2: Incomplete
    rsv3: Incomplete
    opcode: Incomplete
    data: Incomplete
    get_mask_key: Incomplete
    def __init__(self, fin: int = 0, rsv1: int = 0, rsv2: int = 0, rsv3: int = 0, opcode: int = ..., mask: int = 1, data: str | bytes = '') -> None:
        """
        Constructor for ABNF. Please check RFC for arguments.
        """
    def validate(self, skip_utf8_validation: bool = False) -> None:
        """
        Validate the ABNF frame.

        Parameters
        ----------
        skip_utf8_validation: skip utf8 validation.
        """
    @staticmethod
    def create_frame(data: bytes | str, opcode: int, fin: int = 1) -> ABNF:
        """
        Create frame to send text, binary and other data.

        Parameters
        ----------
        data: str
            data to send. This is string value(byte array).
            If opcode is OPCODE_TEXT and this value is unicode,
            data value is converted into unicode string, automatically.
        opcode: int
            operation code. please see OPCODE_MAP.
        fin: int
            fin flag. if set to 0, create continue fragmentation.
        """
    def format(self) -> bytes:
        """
        Format this object to string(byte array) to send data to server.
        """
    @staticmethod
    def mask(mask_key: str | bytes, data: str | bytes) -> bytes:
        """
        Mask or unmask data. Just do xor for each byte

        Parameters
        ----------
        mask_key: bytes or str
            4 byte mask.
        data: bytes or str
            data to mask/unmask.
        """

class frame_buffer:
    recv: Incomplete
    skip_utf8_validation: Incomplete
    recv_buffer: Incomplete
    lock: Incomplete
    def __init__(self, recv_fn: Callable[[int], int], skip_utf8_validation: bool) -> None: ...
    header: Incomplete
    length: Incomplete
    mask: Incomplete
    def clear(self) -> None: ...
    def has_received_header(self) -> bool: ...
    def recv_header(self) -> None: ...
    def has_mask(self) -> bool | int: ...
    def has_received_length(self) -> bool: ...
    def recv_length(self) -> None: ...
    def has_received_mask(self) -> bool: ...
    def recv_mask(self) -> None: ...
    def recv_frame(self) -> ABNF: ...
    def recv_strict(self, bufsize: int) -> bytes: ...

class continuous_frame:
    fire_cont_frame: Incomplete
    skip_utf8_validation: Incomplete
    cont_data: Incomplete
    recving_frames: Incomplete
    def __init__(self, fire_cont_frame: bool, skip_utf8_validation: bool) -> None: ...
    def validate(self, frame: ABNF) -> None: ...
    def add(self, frame: ABNF) -> None: ...
    def is_fire(self, frame: ABNF) -> bool | int: ...
    def extract(self, frame: ABNF) -> list: ...
