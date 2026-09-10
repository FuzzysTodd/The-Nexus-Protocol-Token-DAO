from _typeshed import Incomplete
from pip import __version__ as __version__
from pip._internal.metadata import get_default_environment as get_default_environment
from pip._internal.models.link import Link as Link
from pip._internal.network.auth import MultiDomainBasicAuth as MultiDomainBasicAuth
from pip._internal.network.cache import SafeFileCache as SafeFileCache
from pip._internal.utils.compat import has_tls as has_tls
from pip._internal.utils.glibc import libc_ver as libc_ver
from pip._internal.utils.misc import build_url_from_netloc as build_url_from_netloc, parse_netloc as parse_netloc
from pip._internal.utils.urls import url_to_path as url_to_path
from pip._vendor import requests as requests, urllib3 as urllib3
from pip._vendor.cachecontrol import CacheControlAdapter as _BaseCacheControlAdapter
from pip._vendor.requests.adapters import BaseAdapter as BaseAdapter, DEFAULT_POOLBLOCK as DEFAULT_POOLBLOCK, HTTPAdapter as _BaseHTTPAdapter
from pip._vendor.requests.models import PreparedRequest as PreparedRequest, Response as Response
from pip._vendor.requests.structures import CaseInsensitiveDict as CaseInsensitiveDict
from pip._vendor.urllib3.connectionpool import ConnectionPool as ConnectionPool
from pip._vendor.urllib3.exceptions import InsecureRequestWarning as InsecureRequestWarning
from pip._vendor.urllib3.poolmanager import PoolManager as PoolManager
from ssl import SSLContext
from typing import Any, Generator, List, Mapping, Sequence, Tuple

logger: Incomplete
SecureOrigin = Tuple[str, str, int | str | None]
SECURE_ORIGINS: List[SecureOrigin]
CI_ENVIRONMENT_VARIABLES: Incomplete

def looks_like_ci() -> bool:
    """
    Return whether it looks like pip is running under CI.
    """
def user_agent() -> str:
    """
    Return a string representing the user agent.
    """

class LocalFSAdapter(BaseAdapter):
    def send(self, request: PreparedRequest, stream: bool = False, timeout: float | Tuple[float, float] | None = None, verify: bool | str = True, cert: str | Tuple[str, str] | None = None, proxies: Mapping[str, str] | None = None) -> Response: ...
    def close(self) -> None: ...

class _SSLContextAdapterMixin:
    """Mixin to add the ``ssl_context`` constructor argument to HTTP adapters.

    The additional argument is forwarded directly to the pool manager. This allows us
    to dynamically decide what SSL store to use at runtime, which is used to implement
    the optional ``truststore`` backend.
    """
    def __init__(self, *, ssl_context: SSLContext | None = None, **kwargs: Any) -> None: ...
    def init_poolmanager(self, connections: int, maxsize: int, block: bool = ..., **pool_kwargs: Any) -> PoolManager: ...

class HTTPAdapter(_SSLContextAdapterMixin, _BaseHTTPAdapter): ...
class CacheControlAdapter(_SSLContextAdapterMixin, _BaseCacheControlAdapter): ...

class InsecureHTTPAdapter(HTTPAdapter):
    def cert_verify(self, conn: ConnectionPool, url: str, verify: bool | str, cert: str | Tuple[str, str] | None) -> None: ...

class InsecureCacheControlAdapter(CacheControlAdapter):
    def cert_verify(self, conn: ConnectionPool, url: str, verify: bool | str, cert: str | Tuple[str, str] | None) -> None: ...

class PipSession(requests.Session):
    timeout: int | None
    pip_trusted_origins: Incomplete
    auth: Incomplete
    def __init__(self, *args: Any, retries: int = 0, cache: str | None = None, trusted_hosts: Sequence[str] = (), index_urls: List[str] | None = None, ssl_context: SSLContext | None = None, **kwargs: Any) -> None:
        """
        :param trusted_hosts: Domains not to emit warnings for when not using
            HTTPS.
        """
    def update_index_urls(self, new_index_urls: List[str]) -> None:
        """
        :param new_index_urls: New index urls to update the authentication
            handler with.
        """
    def add_trusted_host(self, host: str, source: str | None = None, suppress_logging: bool = False) -> None:
        """
        :param host: It is okay to provide a host that has previously been
            added.
        :param source: An optional source string, for logging where the host
            string came from.
        """
    def iter_secure_origins(self) -> Generator[SecureOrigin, None, None]: ...
    def is_secure_origin(self, location: Link) -> bool: ...
    def request(self, method: str, url: str, *args: Any, **kwargs: Any) -> Response: ...
