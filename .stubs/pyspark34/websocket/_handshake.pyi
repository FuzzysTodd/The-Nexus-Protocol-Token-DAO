from ._exceptions import *
from ._http import *
from ._logging import *
from ._socket import *
from _typeshed import Incomplete

__all__ = ['handshake_response', 'handshake', 'SUPPORTED_REDIRECT_STATUSES']

SUPPORTED_REDIRECT_STATUSES: Incomplete

class handshake_response:
    status: Incomplete
    headers: Incomplete
    subprotocol: Incomplete
    def __init__(self, status: int, headers: dict, subprotocol) -> None: ...

def handshake(sock, url: str, hostname: str, port: int, resource: str, **options): ...
