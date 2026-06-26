from _typeshed import Incomplete
from typing import Tuple
from wandb.proto.wandb_internal_pb2 import Record as Record

logger: Incomplete
LEVELDBLOG_HEADER_LEN: int
LEVELDBLOG_BLOCK_LEN: int
LEVELDBLOG_DATA_LEN: Incomplete
LEVELDBLOG_FULL: int
LEVELDBLOG_FIRST: int
LEVELDBLOG_MIDDLE: int
LEVELDBLOG_LAST: int
LEVELDBLOG_HEADER_IDENT: str
LEVELDBLOG_HEADER_MAGIC: int
LEVELDBLOG_HEADER_VERSION: int

def strtobytes(x):
    """strtobytes."""
strtobytes = str

class DataStore:
    def __init__(self) -> None: ...
    def open_for_write(self, fname: str) -> None: ...
    def open_for_append(self, fname) -> None: ...
    def open_for_scan(self, fname) -> None: ...
    def seek(self, offset: int) -> None: ...
    def get_offset(self) -> int: ...
    def in_last_block(self):
        """Determine if we're in the last block to handle in-progress writes."""
    def scan_record(self): ...
    def scan_data(self): ...
    def ensure_flushed(self, off: int) -> None: ...
    def write(self, obj: Record) -> Tuple[int, int, int]:
        """Write a protocol buffer.

        Arguments:
            obj: Protocol buffer to write.

        Returns:
            (start_offset, end_offset, flush_offset) if successful,
            None otherwise

        """
    def close(self) -> None: ...
