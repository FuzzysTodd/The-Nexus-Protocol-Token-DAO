from _typeshed import Incomplete
from pyu2f import errors as errors

class ClientData:
    """FIDO U2F ClientData.

  Implements the ClientData object of the FIDO U2F protocol.
  """
    TYP_AUTHENTICATION: str
    TYP_REGISTRATION: str
    typ: Incomplete
    raw_server_challenge: Incomplete
    origin: Incomplete
    def __init__(self, typ, raw_server_challenge, origin) -> None: ...
    def GetJson(self):
        """Returns JSON version of ClientData compatible with FIDO spec."""

class RegisteredKey:
    key_handle: Incomplete
    version: Incomplete
    def __init__(self, key_handle, version: str = 'U2F_V2') -> None: ...

class RegisterResponse:
    registration_data: Incomplete
    client_data: Incomplete
    def __init__(self, registration_data, client_data) -> None: ...

class SignResponse:
    key_handle: Incomplete
    signature_data: Incomplete
    client_data: Incomplete
    def __init__(self, key_handle, signature_data, client_data) -> None: ...
