from _typeshed import Incomplete
from collections.abc import Generator
from pyu2f import errors as errors, hid as hid

def HidUsageSelector(device): ...
def DiscoverLocalHIDU2FDevices(selector=...) -> Generator[Incomplete, None, None]: ...

class UsbHidTransport:
    """Implements the U2FHID transport protocol.

  This class implements the U2FHID transport protocol from the
  FIDO U2F specs.  This protocol manages fragmenting longer messages
  over a short hid frame (usually 64 bytes).  It exposes an APDU
  channel through the MSG command as well as a series of other commands
  for configuring and interacting with the device.
  """
    U2FHID_PING: int
    U2FHID_MSG: int
    U2FHID_WINK: int
    U2FHID_PROMPT: int
    U2FHID_INIT: int
    U2FHID_LOCK: int
    U2FHID_ERROR: int
    U2FHID_SYNC: int
    U2FHID_BROADCAST_CID: Incomplete
    ERR_CHANNEL_BUSY: Incomplete
    class InitPacket:
        """Represent an initial U2FHID packet.

    Represent an initial U2FHID packet.  This packet contains
    metadata necessary to interpret the entire packet stream associated
    with a particular exchange (read or write).

    Attributes:
      packet_size: The size of the hid report (packet) used.  Usually 64.
      cid: The channel id for the connection to the device.
      size: The size of the entire message to be sent (including
          all continuation packets)
      payload: The portion of the message to put into the init packet.
          This must be smaller than packet_size - 7 (the overhead for
          an init packet).
    """
        packet_size: Incomplete
        cid: Incomplete
        cmd: Incomplete
        size: Incomplete
        payload: Incomplete
        def __init__(self, packet_size, cid, cmd, size, payload) -> None: ...
        def ToWireFormat(self):
            """Serializes the packet."""
        @staticmethod
        def FromWireFormat(packet_size, data):
            """Derializes the packet.

      Deserializes the packet from wire format.

      Args:
        packet_size: The size of all packets (usually 64)
        data: List of ints or bytearray containing the data from the wire.

      Returns:
        InitPacket object for specified data

      Raises:
        InvalidPacketError: if the data isn't a valid InitPacket
      """
    class ContPacket:
        """Represents a continutation U2FHID packet.

    Represents a continutation U2FHID packet.  These packets follow
    the intial packet and contains the remaining data in a particular
    message.

    Attributes:
      packet_size: The size of the hid report (packet) used.  Usually 64.
      cid: The channel id for the connection to the device.
      seq: The sequence number for this continuation packet.  The first
          continuation packet is 0 and it increases from there.
      payload:  The payload to put into this continuation packet.  This
          must be less than packet_size - 5 (the overhead of the
          continuation packet is 5).
    """
        packet_size: Incomplete
        cid: Incomplete
        seq: Incomplete
        payload: Incomplete
        def __init__(self, packet_size, cid, seq, payload) -> None: ...
        def ToWireFormat(self):
            """Serializes the packet."""
        @staticmethod
        def FromWireFormat(packet_size, data):
            """Derializes the packet.

      Deserializes the packet from wire format.

      Args:
        packet_size: The size of all packets (usually 64)
        data: List of ints or bytearray containing the data from the wire.

      Returns:
        InitPacket object for specified data

      Raises:
        InvalidPacketError: if the data isn't a valid ContPacket
      """
    hid_device: Incomplete
    packet_size: Incomplete
    read_timeout_secs: Incomplete
    logger: Incomplete
    def __init__(self, hid_device, read_timeout_secs: float = 3.0) -> None: ...
    def SendMsgBytes(self, msg): ...
    def SendBlink(self, length): ...
    def SendWink(self): ...
    def SendPing(self, data): ...
    cid: Incomplete
    u2fhid_version: Incomplete
    def InternalInit(self) -> None:
        """Initializes the device and obtains channel id."""
    def InternalExchange(self, cmd, payload_in):
        """Sends and receives a message from the device."""
    def InternalSend(self, cmd, payload) -> None:
        """Sends a message to the device, including fragmenting it."""
    def InternalSendPacket(self, packet) -> None: ...
    def InternalReadFrame(self): ...
    def InternalRecv(self):
        """Receives a message from the device, including defragmenting it."""
