from _typeshed import Incomplete
from docker.transport.basehttpadapter import BaseHTTPAdapter as BaseHTTPAdapter

PoolManager: Incomplete

class SSLHTTPAdapter(BaseHTTPAdapter):
    """An HTTPS Transport Adapter that uses an arbitrary SSL version."""
    __attrs__: Incomplete
    ssl_version: Incomplete
    assert_hostname: Incomplete
    assert_fingerprint: Incomplete
    def __init__(self, ssl_version: Incomplete | None = None, assert_hostname: Incomplete | None = None, assert_fingerprint: Incomplete | None = None, **kwargs) -> None: ...
    poolmanager: Incomplete
    def init_poolmanager(self, connections, maxsize, block: bool = False) -> None: ...
    def get_connection(self, *args, **kwargs):
        """
        Ensure assert_hostname is set correctly on our pool

        We already take care of a normal poolmanager via init_poolmanager

        But we still need to take care of when there is a proxy poolmanager
        """
    def can_override_ssl_version(self): ...
