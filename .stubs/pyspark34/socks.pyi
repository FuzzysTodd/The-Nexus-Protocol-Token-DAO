import socket
from _typeshed import Incomplete

__version__: str
log: Incomplete
PROXY_TYPE_SOCKS4: int
SOCKS4: int
PROXY_TYPE_SOCKS5: int
SOCKS5: int
PROXY_TYPE_HTTP: int
HTTP: int
PROXY_TYPES: Incomplete
PRINTABLE_PROXY_TYPES: Incomplete

def set_self_blocking(function): ...

class ProxyError(IOError):
    """Socket_err contains original socket.error exception."""
    msg: Incomplete
    socket_err: Incomplete
    def __init__(self, msg, socket_err: Incomplete | None = None) -> None: ...

class GeneralProxyError(ProxyError): ...
class ProxyConnectionError(ProxyError): ...
class SOCKS5AuthError(ProxyError): ...
class SOCKS5Error(ProxyError): ...
class SOCKS4Error(ProxyError): ...
class HTTPError(ProxyError): ...

SOCKS4_ERRORS: Incomplete
SOCKS5_ERRORS: Incomplete
DEFAULT_PORTS: Incomplete

def set_default_proxy(proxy_type: Incomplete | None = None, addr: Incomplete | None = None, port: Incomplete | None = None, rdns: bool = True, username: Incomplete | None = None, password: Incomplete | None = None) -> None:
    """Sets a default proxy.

    All further socksocket objects will use the default unless explicitly
    changed. All parameters are as for socket.set_proxy()."""
def setdefaultproxy(*args, **kwargs): ...
def get_default_proxy():
    """Returns the default proxy, set by set_default_proxy."""
getdefaultproxy = get_default_proxy

def wrap_module(module) -> None:
    """Attempts to replace a module's socket library with a SOCKS socket.

    Must set a default proxy using set_default_proxy(...) first. This will
    only work on modules that import socket directly into the namespace;
    most of the Python Standard Library falls into this category."""
wrapmodule = wrap_module

def create_connection(dest_pair, timeout: Incomplete | None = None, source_address: Incomplete | None = None, proxy_type: Incomplete | None = None, proxy_addr: Incomplete | None = None, proxy_port: Incomplete | None = None, proxy_rdns: bool = True, proxy_username: Incomplete | None = None, proxy_password: Incomplete | None = None, socket_options: Incomplete | None = None):
    """create_connection(dest_pair, *[, timeout], **proxy_args) -> socket object

    Like socket.create_connection(), but connects to proxy
    before returning the socket object.

    dest_pair - 2-tuple of (IP/hostname, port).
    **proxy_args - Same args passed to socksocket.set_proxy() if present.
    timeout - Optional socket timeout value, in seconds.
    source_address - tuple (host, port) for the socket to bind to as its source
    address before connecting (only for compatibility)
    """

class _BaseSocket(socket.socket):
    """Allows Python 2 delegated methods such as send() to be overridden."""
    def __init__(self, *pos, **kw) -> None: ...

method: Incomplete

class socksocket(_BaseSocket):
    '''socksocket([family[, type[, proto]]]) -> socket object

    Open a SOCKS enabled socket. The parameters are the same as
    those of the standard socket init. In order for SOCKS to work,
    you must specify family=AF_INET and proto=0.
    The "type" argument must be either SOCK_STREAM or SOCK_DGRAM.
    '''
    default_proxy: Incomplete
    proxy: Incomplete
    proxy_sockname: Incomplete
    proxy_peername: Incomplete
    def __init__(self, family=..., type=..., proto: int = 0, *args, **kwargs) -> None: ...
    def settimeout(self, timeout) -> None: ...
    def gettimeout(self): ...
    def setblocking(self, v) -> None: ...
    def set_proxy(self, proxy_type: Incomplete | None = None, addr: Incomplete | None = None, port: Incomplete | None = None, rdns: bool = True, username: Incomplete | None = None, password: Incomplete | None = None) -> None:
        """ Sets the proxy to be used.

        proxy_type -  The type of the proxy to be used. Three types
                        are supported: PROXY_TYPE_SOCKS4 (including socks4a),
                        PROXY_TYPE_SOCKS5 and PROXY_TYPE_HTTP
        addr -        The address of the server (IP or DNS).
        port -        The port of the server. Defaults to 1080 for SOCKS
                        servers and 8080 for HTTP proxy servers.
        rdns -        Should DNS queries be performed on the remote side
                       (rather than the local side). The default is True.
                       Note: This has no effect with SOCKS4 servers.
        username -    Username to authenticate with to the server.
                       The default is no authentication.
        password -    Password to authenticate with to the server.
                       Only relevant when username is also provided."""
    def setproxy(self, *args, **kwargs): ...
    def bind(self, *pos, **kw):
        """Implements proxy connection for UDP sockets.

        Happens during the bind() phase."""
    def sendto(self, bytes, *args, **kwargs): ...
    def send(self, bytes, flags: int = 0, **kwargs): ...
    def recvfrom(self, bufsize, flags: int = 0): ...
    def recv(self, *pos, **kw): ...
    def close(self): ...
    def get_proxy_sockname(self):
        """Returns the bound IP address and port number at the proxy."""
    getproxysockname = get_proxy_sockname
    def get_proxy_peername(self):
        """
        Returns the IP and port number of the proxy.
        """
    getproxypeername = get_proxy_peername
    def get_peername(self):
        """Returns the IP address and port number of the destination machine.

        Note: get_proxy_peername returns the proxy."""
    getpeername = get_peername
    def connect(self, dest_pair, catch_errors: Incomplete | None = None) -> None:
        """
        Connects to the specified destination through a proxy.
        Uses the same API as socket's connect().
        To select the proxy server, use set_proxy().

        dest_pair - 2-tuple of (IP/hostname, port).
        """
    def connect_ex(self, dest_pair):
        ''' https://docs.python.org/3/library/socket.html#socket.socket.connect_ex
        Like connect(address), but return an error indicator instead of raising an exception for errors returned by the C-level connect() call (other problems, such as "host not found" can still raise exceptions).
        '''
