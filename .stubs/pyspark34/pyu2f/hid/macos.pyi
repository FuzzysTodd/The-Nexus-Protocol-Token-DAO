import ctypes
from _typeshed import Incomplete
from pyu2f import errors as errors
from pyu2f.hid import base as base

logger: Incomplete
DEVICE_PATH_BUFFER_SIZE: int
DEVICE_STRING_PROPERTY_BUFFER_SIZE: int
HID_DEVICE_PROPERTY_VENDOR_ID: str
HID_DEVICE_PROPERTY_PRODUCT_ID: str
HID_DEVICE_PROPERTY_PRODUCT: str
HID_DEVICE_PROPERTY_PRIMARY_USAGE: str
HID_DEVICE_PROPERTY_PRIMARY_USAGE_PAGE: str
HID_DEVICE_PROPERTY_MAX_INPUT_REPORT_SIZE: str
HID_DEVICE_PROPERTY_MAX_OUTPUT_REPORT_SIZE: str
HID_DEVICE_PROPERTY_REPORT_ID: str

class _CFType(ctypes.Structure): ...
class _CFString(_CFType): ...
class _CFSet(_CFType): ...
class _IOHIDManager(_CFType): ...
class _IOHIDDevice(_CFType): ...
class _CFRunLoop(_CFType): ...
class _CFAllocator(_CFType): ...

CF_SET_REF: Incomplete
CF_STRING_REF: Incomplete
CF_TYPE_REF: Incomplete
CF_RUN_LOOP_REF: Incomplete
CF_RUN_LOOP_RUN_RESULT = ctypes.c_int32
CF_ALLOCATOR_REF: Incomplete
CF_TYPE_ID = ctypes.c_ulong
CF_INDEX = ctypes.c_long
CF_TIME_INTERVAL = ctypes.c_double
IO_RETURN = ctypes.c_uint
IO_HID_REPORT_TYPE = ctypes.c_uint
IO_OBJECT_T = ctypes.c_uint
MACH_PORT_T = ctypes.c_uint
IO_STRING_T = ctypes.c_char_p
IO_SERVICE_T = IO_OBJECT_T
IO_REGISTRY_ENTRY_T = IO_OBJECT_T
IO_HID_MANAGER_REF: Incomplete
IO_HID_DEVICE_REF: Incomplete
IO_HID_REPORT_CALLBACK: Incomplete
K_CF_NUMBER_SINT32_TYPE: int
K_CF_STRING_ENCODING_UTF8: int
K_CF_ALLOCATOR_DEFAULT: Incomplete
K_IO_SERVICE_PLANE: bytes
K_IO_MASTER_PORT_DEFAULT: int
K_IO_HID_REPORT_TYPE_OUTPUT: int
K_IO_RETURN_SUCCESS: int
K_CF_RUN_LOOP_RUN_STOPPED: int
K_CF_RUN_LOOP_RUN_TIMED_OUT: int
K_CF_RUN_LOOP_RUN_HANDLED_SOURCE: int
iokit: Incomplete
cf: Incomplete

def CFStr(s):
    """Builds a CFString from a python string.

  Args:
    s: source string

  Returns:
    CFStringRef representation of the source string

  Resulting CFString must be CFReleased when no longer needed.
  """
def GetDeviceIntProperty(dev_ref, key):
    """Reads int property from the HID device."""
def GetDeviceStringProperty(dev_ref, key):
    """Reads string property from the HID device."""
def GetDevicePath(device_handle):
    """Obtains the unique path for the device.

  Args:
    device_handle: reference to the device

  Returns:
    A unique path for the device, obtained from the IO Registry

  """
def HidReadCallback(read_queue, result, sender, report_type, report_id, report, report_length) -> None:
    """Handles incoming IN report from HID device."""

REGISTERED_READ_CALLBACK: Incomplete

def DeviceReadThread(hid_device) -> None:
    """Binds a device to the thread's run loop, then starts the run loop.

  Args:
    hid_device: The MacOsHidDevice object

  The HID manager requires a run loop to handle Report reads. This thread
  function serves that purpose.
  """

class MacOsHidDevice(base.HidDevice):
    """Implementation of HID device for MacOS.

  Uses IOKit HID Manager to interact with the device.
  """
    @staticmethod
    def Enumerate():
        """See base class."""
    device_handle: Incomplete
    device_path: Incomplete
    read_queue: Incomplete
    run_loop_ref: Incomplete
    read_thread: Incomplete
    internal_max_in_report_len: Incomplete
    internal_max_out_report_len: Incomplete
    in_report_buffer: Incomplete
    def __init__(self, path) -> None: ...
    def GetInReportDataLength(self):
        """See base class."""
    def GetOutReportDataLength(self):
        """See base class."""
    def Write(self, packet) -> None:
        """See base class."""
    def Read(self):
        """See base class."""
    def __del__(self) -> None: ...
