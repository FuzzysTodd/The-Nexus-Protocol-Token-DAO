from .. import extensions as extensions, frames as frames
from ..exceptions import PayloadTooBig as PayloadTooBig, ProtocolError as ProtocolError
from ..frames import Close as Close, prepare_data as prepare_data
from ..utils import apply_mask as apply_mask
from typing import Any, Awaitable, Callable, NamedTuple, Sequence, Tuple

class Frame(NamedTuple):
    fin: bool
    opcode: frames.Opcode
    data: bytes
    rsv1: bool = ...
    rsv2: bool = ...
    rsv3: bool = ...
    @property
    def new_frame(self) -> frames.Frame: ...
    def check(self) -> None: ...
    @classmethod
    async def read(cls, reader: Callable[[int], Awaitable[bytes]], *, mask: bool, max_size: int | None = None, extensions: Sequence[extensions.Extension] | None = None) -> Frame:
        """
        Read a WebSocket frame.

        Args:
            reader: Coroutine that reads exactly the requested number of
                bytes, unless the end of file is reached.
            mask: Whether the frame should be masked i.e. whether the read
                happens on the server side.
            max_size: Maximum payload size in bytes.
            extensions: List of extensions, applied in reverse order.

        Raises:
            PayloadTooBig: If the frame exceeds ``max_size``.
            ProtocolError: If the frame contains incorrect values.

        """
    def write(self, write: Callable[[bytes], Any], *, mask: bool, extensions: Sequence[extensions.Extension] | None = None) -> None:
        """
        Write a WebSocket frame.

        Args:
            frame: Frame to write.
            write: Function that writes bytes.
            mask: Whether the frame should be masked i.e. whether the write
                happens on the client side.
            extensions: List of extensions, applied in order.

        Raises:
            ProtocolError: If the frame contains incorrect values.

        """

def parse_close(data: bytes) -> Tuple[int, str]:
    """
    Parse the payload from a close frame.

    Returns:
        Close code and reason.

    Raises:
        ProtocolError: If data is ill-formed.
        UnicodeDecodeError: If the reason isn't valid UTF-8.

    """
def serialize_close(code: int, reason: str) -> bytes:
    """
    Serialize the payload for a close frame.

    """
