from .adal_error import AdalError as AdalError
from .constants import Jwt as Jwt
from .log import Logger as Logger
from _typeshed import Incomplete

class SelfSignedJwt:
    NumCharIn128BitHexString: Incomplete
    numCharIn160BitHexString: Incomplete
    ThumbprintRegEx: str
    def __init__(self, call_context, authority, client_id) -> None: ...
    def create(self, certificate, thumbprint, public_certificate): ...
