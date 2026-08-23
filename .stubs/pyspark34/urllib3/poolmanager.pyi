from .request import RequestMethods
from _typeshed import Incomplete

__all__ = ['PoolManager', 'ProxyManager', 'proxy_from_url']

PoolKey: Incomplete
ProxyConfig: Incomplete

class PoolManager(RequestMethods):
    """
    Allows for arbitrary requests while transparently keeping track of
    necessary connection pools for you.

    :param num_pools:
        Number of connection pools to cache before discarding the least
        recently used pool.

    :param headers:
        Headers to include with all requests, unless other headers are given
        explicitly.

    :param \\**connection_pool_kw:
        Additional parameters are used to create fresh
        :class:`urllib3.connectionpool.ConnectionPool` instances.

    Example::

        >>> manager = PoolManager(num_pools=2)
        >>> r = manager.request('GET', 'http://google.com/')
        >>> r = manager.request('GET', 'http://google.com/mail')
        >>> r = manager.request('GET', 'http://yahoo.com/')
        >>> len(manager.pools)
        2

    """
    proxy: Incomplete
    proxy_config: Incomplete
    connection_pool_kw: Incomplete
    pools: Incomplete
    pool_classes_by_scheme: Incomplete
    key_fn_by_scheme: Incomplete
    def __init__(self, num_pools: int = 10, headers: Incomplete | None = None, **connection_pool_kw) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None): ...
    def clear(self) -> None:
        """
        Empty our store of pools and direct them all to close.

        This will not affect in-flight connections, but they will not be
        re-used after completion.
        """
    def connection_from_host(self, host, port: Incomplete | None = None, scheme: str = 'http', pool_kwargs: Incomplete | None = None):
        """
        Get a :class:`urllib3.connectionpool.ConnectionPool` based on the host, port, and scheme.

        If ``port`` isn't given, it will be derived from the ``scheme`` using
        ``urllib3.connectionpool.port_by_scheme``. If ``pool_kwargs`` is
        provided, it is merged with the instance's ``connection_pool_kw``
        variable and used to create the new connection pool, if one is
        needed.
        """
    def connection_from_context(self, request_context):
        """
        Get a :class:`urllib3.connectionpool.ConnectionPool` based on the request context.

        ``request_context`` must at least contain the ``scheme`` key and its
        value must be a key in ``key_fn_by_scheme`` instance variable.
        """
    def connection_from_pool_key(self, pool_key, request_context: Incomplete | None = None):
        """
        Get a :class:`urllib3.connectionpool.ConnectionPool` based on the provided pool key.

        ``pool_key`` should be a namedtuple that only contains immutable
        objects. At a minimum it must have the ``scheme``, ``host``, and
        ``port`` fields.
        """
    def connection_from_url(self, url, pool_kwargs: Incomplete | None = None):
        """
        Similar to :func:`urllib3.connectionpool.connection_from_url`.

        If ``pool_kwargs`` is not provided and a new pool needs to be
        constructed, ``self.connection_pool_kw`` is used to initialize
        the :class:`urllib3.connectionpool.ConnectionPool`. If ``pool_kwargs``
        is provided, it is used instead. Note that if a new pool does not
        need to be created for the request, the provided ``pool_kwargs`` are
        not used.
        """
    def urlopen(self, method, url, redirect: bool = True, **kw):
        """
        Same as :meth:`urllib3.HTTPConnectionPool.urlopen`
        with custom cross-host redirect logic and only sends the request-uri
        portion of the ``url``.

        The given ``url`` parameter must be absolute, such that an appropriate
        :class:`urllib3.connectionpool.ConnectionPool` can be chosen for it.
        """

class ProxyManager(PoolManager):
    """
    Behaves just like :class:`PoolManager`, but sends all requests through
    the defined proxy, using the CONNECT method for HTTPS URLs.

    :param proxy_url:
        The URL of the proxy to be used.

    :param proxy_headers:
        A dictionary containing headers that will be sent to the proxy. In case
        of HTTP they are being sent with each request, while in the
        HTTPS/CONNECT case they are sent only once. Could be used for proxy
        authentication.

    :param proxy_ssl_context:
        The proxy SSL context is used to establish the TLS connection to the
        proxy when using HTTPS proxies.

    :param use_forwarding_for_https:
        (Defaults to False) If set to True will forward requests to the HTTPS
        proxy to be made on behalf of the client instead of creating a TLS
        tunnel via the CONNECT method. **Enabling this flag means that request
        and response headers and content will be visible from the HTTPS proxy**
        whereas tunneling keeps request and response headers and content
        private.  IP address, target hostname, SNI, and port are always visible
        to an HTTPS proxy even when this flag is disabled.

    Example:
        >>> proxy = urllib3.ProxyManager('http://localhost:3128/')
        >>> r1 = proxy.request('GET', 'http://google.com/')
        >>> r2 = proxy.request('GET', 'http://httpbin.org/')
        >>> len(proxy.pools)
        1
        >>> r3 = proxy.request('GET', 'https://httpbin.org/')
        >>> r4 = proxy.request('GET', 'https://twitter.com/')
        >>> len(proxy.pools)
        3

    """
    proxy: Incomplete
    proxy_headers: Incomplete
    proxy_ssl_context: Incomplete
    proxy_config: Incomplete
    def __init__(self, proxy_url, num_pools: int = 10, headers: Incomplete | None = None, proxy_headers: Incomplete | None = None, proxy_ssl_context: Incomplete | None = None, use_forwarding_for_https: bool = False, **connection_pool_kw) -> None: ...
    def connection_from_host(self, host, port: Incomplete | None = None, scheme: str = 'http', pool_kwargs: Incomplete | None = None): ...
    def urlopen(self, method, url, redirect: bool = True, **kw):
        """Same as HTTP(S)ConnectionPool.urlopen, ``url`` must be absolute."""

def proxy_from_url(url, **kw): ...
