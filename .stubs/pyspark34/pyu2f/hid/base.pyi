from _typeshed import Incomplete

class HidDevice:
    """Base class for all HID devices in this package."""
    @staticmethod
    def Enumerate() -> None:
        """Enumerates all the hid devices.

    This function enumerates all the hid device and provides metadata
    for helping the client select one.

    Returns:
      A list of dictionaries of metadata.  Each implementation is required
      to provide at least: vendor_id, product_id, product_string, usage,
      usage_page, and path.
    """
    def __init__(self, path) -> None:
        """Initialize the device at path."""
    def GetInReportDataLength(self) -> None:
        """Returns the max input report data length in bytes.

    Returns the max input report data length in bytes.  This excludes the
    report id.
    """
    def GetOutReportDataLength(self) -> None:
        """Returns the max output report data length in bytes.

    Returns the max output report data length in bytes.  This excludes the
    report id.
    """
    def Write(self, packet) -> None:
        """Writes packet to device.

    Writes the packet to the device.

    Args:
      packet: An array of integers to write to the device.  Excludes the report
      ID. Must be equal to GetOutReportLength().
    """
    def Read(self) -> None:
        """Reads packet from device.

    Reads the packet from the device.

    Returns:
      An array of integers read from the device.  Excludes the report ID.
      The length is equal to GetInReportDataLength().
    """

class DeviceDescriptor:
    """Descriptor for basic attributes of the device."""
    usage_page: Incomplete
    usage: Incomplete
    vendor_id: Incomplete
    product_id: Incomplete
    product_string: Incomplete
    path: Incomplete
    internal_max_in_report_len: int
    internal_max_out_report_len: int
    def ToPublicDict(self): ...
