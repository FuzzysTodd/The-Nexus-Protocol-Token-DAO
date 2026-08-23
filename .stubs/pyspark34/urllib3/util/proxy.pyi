from .ssl_ import create_urllib3_context as create_urllib3_context, resolve_cert_reqs as resolve_cert_reqs, resolve_ssl_version as resolve_ssl_version
from _typeshed import Incomplete

def connection_requires_http_tunnel(proxy_url: Incomplete | None = None, proxy_config: Incomplete | None = None, destination_scheme: Incomplete | None = None):
    """
    Returns True if the connection requires an HTTP CONNECT through the proxy.

    :param URL proxy_url:
        URL of the proxy.
    :param ProxyConfig proxy_config:
        Proxy configuration from poolmanager.py
    :param str destination_scheme:
        The scheme of the destination. (i.e https, http, etc)
    """
def create_proxy_ssl_context(ssl_version, cert_reqs, ca_certs: Incomplete | None = None, ca_cert_dir: Incomplete | None = None, ca_cert_data: Incomplete | None = None):
    """
    Generates a default proxy ssl context if one hasn't been provided by the
    user.
    """
