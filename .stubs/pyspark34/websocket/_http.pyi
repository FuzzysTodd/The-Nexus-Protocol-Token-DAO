from ._exceptions import *
from ._logging import *
from ._socket import *
from ._ssl_compat import *
from ._url import *
from python_socks._errors import *
from _typeshed import Incomplete

__all__ = ['proxy_info', 'connect', 'read_headers']

class ProxyError(Exception): ...
class ProxyTimeoutError(Exception): ...
class ProxyConnectionError(Exception): ...

class proxy_info:
    proxy_host: Incomplete
    proxy_port: Incomplete
    auth: Incomplete
    no_proxy: Incomplete
    proxy_protocol: Incomplete
    proxy_timeout: Incomplete
    def __init__(self, **options) -> None: ...

def connect(url: str, options, proxy, socket): ...
def read_headers(sock): ...
