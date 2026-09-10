from _typeshed import Incomplete
from pyu2f import apdu as apdu, errors as errors

class SecurityKey:
    """Low level api for talking to a security key.

  This class implements the low level api specified in FIDO
  U2F for talking to a security key.
  """
    transport: Incomplete
    use_legacy_format: bool
    logger: Incomplete
    def __init__(self, transport) -> None: ...
    def CmdRegister(self, challenge_param, app_param):
        """Register security key.

    Ask the security key to register with a particular origin & client.

    Args:
      challenge_param: Arbitrary 32 byte challenge string.
      app_param: Arbitrary 32 byte applciation parameter.

    Returns:
      A binary structure containing the key handle, attestation, and a
      signature over that by the attestation key.  The precise format
      is dictated by the FIDO U2F specs.

    Raises:
      TUPRequiredError: A Test of User Precense is required to proceed.
      ApduError: Something went wrong on the device.
    """
    def CmdAuthenticate(self, challenge_param, app_param, key_handle, check_only: bool = False):
        """Attempt to obtain an authentication signature.

    Ask the security key to sign a challenge for a particular key handle
    in order to authenticate the user.

    Args:
      challenge_param: SHA-256 hash of client_data object as a bytes
          object.
      app_param: SHA-256 hash of the app id as a bytes object.
      key_handle: The key handle to use to issue the signature as a bytes
          object.
      check_only: If true, only check if key_handle is valid.

    Returns:
      A binary structure containing the key handle, attestation, and a
      signature over that by the attestation key.  The precise format
      is dictated by the FIDO U2F specs.

    Raises:
      TUPRequiredError: If check_only is False, a Test of User Precense
          is required to proceed.  If check_only is True, this means
          the key_handle is valid.
      InvalidKeyHandleError: The key_handle is not valid for this device.
      ApduError: Something else went wrong on the device.
    """
    def CmdVersion(self):
        """Obtain the version of the device and test transport format.

    Obtains the version of the device and determines whether to use ISO
    7816-4 or the U2f variant.  This function should be called at least once
    before CmdAuthenticate or CmdRegister to make sure the object is using the
    proper transport for the device.

    Returns:
      The version of the U2F protocol in use.
    """
    def CmdBlink(self, time) -> None: ...
    def CmdWink(self) -> None: ...
    def CmdPing(self, data): ...
    def InternalSendApdu(self, apdu_to_send):
        """Send an APDU to the device.

    Sends an APDU to the device, possibly falling back to the legacy
    encoding format that is not ISO7816-4 compatible.

    Args:
      apdu_to_send: The CommandApdu object to send

    Returns:
      The ResponseApdu object constructed out of the devices reply.
    """
