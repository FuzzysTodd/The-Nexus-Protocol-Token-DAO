from ..connection import HTTPConnection as HTTPConnection, HTTPSConnection as HTTPSConnection
from ..connectionpool import HTTPConnectionPool as HTTPConnectionPool, HTTPSConnectionPool as HTTPSConnectionPool
from ..exceptions import ConnectTimeoutError as ConnectTimeoutError, DependencyWarning as DependencyWarning, NewConnectionError as NewConnectionError
from ..poolmanager import PoolManager as PoolManager
from ..util.url import parse_url as parse_url
from _typeshed import Incomplete

class SOCKSConnection(HTTPConnection):
    """
    A plain-text HTTP connection that connects via a SOCKS proxy.
    """
    def __init__(self, *args, **kwargs) -> None: ...

class SOCKSHTTPSConnection(SOCKSConnection, HTTPSConnection): ...

class SOCKSHTTPConnectionPool(HTTPConnectionPool):
    ConnectionCls = SOCKSConnection

class SOCKSHTTPSConnectionPool(HTTPSConnectionPool):
    ConnectionCls = SOCKSHTTPSConnection

class SOCKSProxyManager(PoolManager):
    """
    A version of the urllib3 ProxyManager that routes connections via the
    defined SOCKS proxy.
    """
    pool_classes_by_scheme: Incomplete
    proxy_url: Incomplete
    def __init__(self, proxy_url, username: Incomplete | None = None, password: Incomplete | None = None, num_pools: int = 10, headers: Incomplete | None = None, **connection_pool_kw) -> None: ...
