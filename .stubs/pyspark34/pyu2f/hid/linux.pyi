from _typeshed import Incomplete
from collections.abc import Generator
from pyu2f import errors as errors
from pyu2f.hid import base as base

REPORT_DESCRIPTOR_KEY_MASK: int
LONG_ITEM_ENCODING: int
OUTPUT_ITEM: int
INPUT_ITEM: int
COLLECTION_ITEM: int
REPORT_COUNT: int
REPORT_SIZE: int
USAGE_PAGE: int
USAGE: int

def GetValueLength(rd, pos):
    """Get value length for a key in rd.

  For a key at position pos in the Report Descriptor rd, return the length
  of the associated value.  This supports both short and long format
  values.

  Args:
    rd: Report Descriptor
    pos: The position of the key in rd.

  Returns:
    (key_size, data_len) where key_size is the number of bytes occupied by
    the key and data_len is the length of the value associated by the key.
  """
def ReadLsbBytes(rd, offset, value_size):
    """Reads value_size bytes from rd at offset, least signifcant byte first."""

class NoReportCountFound(Exception): ...

def ParseReportDescriptor(rd, desc):
    """Parse the binary report descriptor.

  Parse the binary report descriptor into a DeviceDescriptor object.

  Args:
    rd: The binary report descriptor
    desc: The DeviceDescriptor object to update with the results
        from parsing the descriptor.

  Returns:
    None
  """
def ParseUevent(uevent, desc) -> None: ...

class LinuxHidDevice(base.HidDevice):
    """Implementation of HID device for linux.

  Implementation of HID device interface for linux that uses block
  devices to interact with the device and sysfs to enumerate/discover
  device metadata.
  """
    @staticmethod
    def Enumerate() -> Generator[Incomplete, None, None]: ...
    dev: Incomplete
    desc: Incomplete
    def __init__(self, path) -> None: ...
    def GetInReportDataLength(self):
        """See base class."""
    def GetOutReportDataLength(self):
        """See base class."""
    def Write(self, packet) -> None:
        """See base class."""
    def Read(self):
        """See base class."""
