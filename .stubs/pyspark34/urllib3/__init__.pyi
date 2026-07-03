from ._version import __version__
from .connectionpool import HTTPConnectionPool as HTTPConnectionPool, HTTPSConnectionPool as HTTPSConnectionPool, connection_from_url as connection_from_url
from .filepost import encode_multipart_formdata as encode_multipart_formdata
from .poolmanager import PoolManager as PoolManager, ProxyManager as ProxyManager, proxy_from_url as proxy_from_url
from .response import HTTPResponse as HTTPResponse
from .util.request import make_headers as make_headers
from .util.retry import Retry as Retry
from .util.timeout import Timeout as Timeout
from .util.url import get_host as get_host

__all__ = ['HTTPConnectionPool', 'HTTPSConnectionPool', 'PoolManager', 'ProxyManager', 'HTTPResponse', 'Retry', 'Timeout', 'add_stderr_logger', 'connection_from_url', 'disable_warnings', 'encode_multipart_formdata', 'get_host', 'make_headers', 'proxy_from_url']

__version__ = __version__

def add_stderr_logger(level=...):
    """
    Helper for quickly adding a StreamHandler to the logger. Useful for
    debugging.

    Returns the handler after adding it.
    """
def disable_warnings(category=...) -> None:
    """
    Helper for quickly disabling all urllib3 warnings.
    """
