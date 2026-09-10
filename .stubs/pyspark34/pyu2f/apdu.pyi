from _typeshed import Incomplete
from pyu2f import errors as errors

CMD_REGISTER: int
CMD_AUTH: int
CMD_VERSION: int

class CommandApdu:
    """Represents a Command APDU.

  Represents a Command APDU sent to the security key.  Encoding
  is specified in FIDO U2F standards.
  """
    cla: Incomplete
    ins: Incomplete
    p1: Incomplete
    p2: Incomplete
    data: Incomplete
    def __init__(self, cla, ins, p1, p2, data: Incomplete | None = None) -> None: ...
    def ToByteArray(self):
        """Serialize the command.

    Encodes the command as per the U2F specs, using the standard
    ISO 7816-4 extended encoding.  All Commands expect data, so
    Le is always present.

    Returns:
      Python bytearray of the encoded command.
    """
    def ToLegacyU2FByteArray(self):
        """Serialize the command in the legacy format.

    Encodes the command as per the U2F specs, using the legacy
    encoding in which LC is always present.

    Returns:
      Python bytearray of the encoded command.
    """
    def InternalEncodeLc(self): ...

class ResponseApdu:
    """Represents a Response APDU.

  Represents a Response APU sent by the security key.  Encoding
  is specified in FIDO U2F standards.
  """
    body: Incomplete
    sw1: Incomplete
    sw2: Incomplete
    dbg_full_packet: Incomplete
    def __init__(self, data) -> None: ...
    def IsSuccess(self): ...
    def CheckSuccessOrRaise(self) -> None: ...
