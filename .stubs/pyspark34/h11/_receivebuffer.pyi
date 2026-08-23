from typing import List

__all__ = ['ReceiveBuffer']

class ReceiveBuffer:
    def __init__(self) -> None: ...
    def __iadd__(self, byteslike: bytes | bytearray) -> ReceiveBuffer: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __bytes__(self) -> bytes: ...
    def maybe_extract_at_most(self, count: int) -> bytearray | None:
        """
        Extract a fixed number of bytes from the buffer.
        """
    def maybe_extract_next_line(self) -> bytearray | None:
        """
        Extract the first line, if it is completed in the buffer.
        """
    def maybe_extract_lines(self) -> List[bytearray] | None:
        """
        Extract everything up to the first blank line, and return a list of lines.
        """
    def is_next_line_obviously_invalid_request_line(self) -> bool: ...
