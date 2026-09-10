from . import errors as errors
from .io import gfile as gfile
from _typeshed import Incomplete

TFE_DEVICE_PLACEMENT_WARN: int
TFE_DEVICE_PLACEMENT_SILENT_FOR_INT32: int
TFE_DEVICE_PLACEMENT_SILENT: int
TFE_DEVICE_PLACEMENT_EXPLICIT: int

def __getattr__(attr): ...
def TF_bfloat16_type(): ...
def masked_crc32c(data): ...
def u32(x): ...

CRC_TABLE: Incomplete
CRC_INIT: int

def crc_update(crc, data):
    """Update CRC-32C checksum with data.

    Args:
      crc: 32-bit checksum to update as long.
      data: byte array, string or iterable over bytes.
    Returns:
      32-bit updated CRC-32C as long.
    """
def crc_finalize(crc):
    """Finalize CRC-32C checksum.

    This function should be called as last step of crc calculation.
    Args:
      crc: 32-bit checksum as long.
    Returns:
      finalized 32-bit checksum as long
    """
def crc32c(data):
    """Compute CRC-32C checksum of the data.

    Args:
      data: byte array, string or iterable over bytes.
    Returns:
      32-bit CRC-32C checksum of data as long.
    """

class PyRecordReader_New:
    filename: Incomplete
    start_offset: Incomplete
    compression_type: Incomplete
    status: Incomplete
    curr_event: Incomplete
    file_handle: Incomplete
    def __init__(self, filename: Incomplete | None = None, start_offset: int = 0, compression_type: Incomplete | None = None, status: Incomplete | None = None) -> None: ...
    def GetNext(self) -> None: ...
    def record(self): ...
