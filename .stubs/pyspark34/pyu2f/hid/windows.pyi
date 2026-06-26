import ctypes
from _typeshed import Incomplete
from pyu2f import errors as errors
from pyu2f.hid import base as base

hid: Incomplete
setupapi: Incomplete
kernel32: Incomplete

class GUID(ctypes.Structure): ...

SETUPAPI_PACK: int

class DeviceInterfaceData(ctypes.Structure): ...
class DeviceInterfaceDetailData(ctypes.Structure): ...
class HidAttributes(ctypes.Structure): ...
class HidCapabilities(ctypes.Structure): ...
HDEVINFO = ctypes.c_void_p
HANDLE = ctypes.c_void_p
PHIDP_PREPARSED_DATA = ctypes.c_void_p
INVALID_HANDLE_VALUE: int
NTSTATUS = ctypes.c_long
HIDP_STATUS_SUCCESS: int
FILE_SHARE_READ: int
FILE_SHARE_WRITE: int
OPEN_EXISTING: int
ERROR_ACCESS_DENIED: int
GENERIC_WRITE: int
GENERIC_READ: int

def FillDeviceAttributes(device, descriptor) -> None:
    """Fill out the attributes of the device.

  Fills the devices HidAttributes and product string
  into the descriptor.

  Args:
    device: A handle to the open device
    descriptor: The DeviceDescriptor to populate with the
      attributes.

  Returns:
    None

  Raises:
    WindowsError when unable to obtain attributes or product
      string.
  """
def FillDeviceCapabilities(device, descriptor) -> None:
    """Fill out device capabilities.

  Fills the HidCapabilitites of the device into descriptor.

  Args:
    device: A handle to the open device
    descriptor: DeviceDescriptor to populate with the
      capabilities

  Returns:
    none

  Raises:
    WindowsError when unable to obtain capabilitites.
  """
def OpenDevice(path, enum: bool = False):
    """Open the device and return a handle to it."""

class WindowsHidDevice(base.HidDevice):
    """Implementation of raw HID interface on Windows."""
    @staticmethod
    def Enumerate():
        """See base class."""
    dev: Incomplete
    desc: Incomplete
    def __init__(self, path) -> None:
        """See base class."""
    def GetInReportDataLength(self):
        """See base class."""
    def GetOutReportDataLength(self):
        """See base class."""
    def Write(self, packet) -> None:
        """See base class."""
    def Read(self):
        """See base class."""
    def __del__(self) -> None:
        """Closes the file handle when object is GC-ed."""
