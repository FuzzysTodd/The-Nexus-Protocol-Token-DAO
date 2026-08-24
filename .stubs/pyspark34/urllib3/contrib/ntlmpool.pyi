from .. import HTTPSConnectionPool as HTTPSConnectionPool
from ..packages.six.moves.http_client import HTTPSConnection as HTTPSConnection
from _typeshed import Incomplete

log: Incomplete

class NTLMConnectionPool(HTTPSConnectionPool):
    """
    Implements an NTLM authentication version of an urllib3 connection pool
    """
    scheme: str
    authurl: Incomplete
    rawuser: Incomplete
    domain: Incomplete
    user: Incomplete
    pw: Incomplete
    def __init__(self, user, pw, authurl, *args, **kwargs) -> None:
        """
        authurl is a random URL on the server that is protected by NTLM.
        user is the Windows user, probably in the DOMAIN\\username format.
        pw is the password for the user.
        """
    def urlopen(self, method, url, body: Incomplete | None = None, headers: Incomplete | None = None, retries: int = 3, redirect: bool = True, assert_same_host: bool = True): ...
