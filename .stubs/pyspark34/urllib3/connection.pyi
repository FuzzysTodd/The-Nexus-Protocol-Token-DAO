import ssl
from ._collections import HTTPHeaderDict as HTTPHeaderDict
from ._version import __version__ as __version__
from .exceptions import ConnectTimeoutError as ConnectTimeoutError, NewConnectionError as NewConnectionError, SubjectAltNameWarning as SubjectAltNameWarning, SystemTimeWarning as SystemTimeWarning
from .packages.six.moves.http_client import HTTPConnection as _HTTPConnection, HTTPException as HTTPException
from .util import SKIPPABLE_HEADERS as SKIPPABLE_HEADERS, SKIP_HEADER as SKIP_HEADER, connection as connection
from .util.proxy import create_proxy_ssl_context as create_proxy_ssl_context
from .util.ssl_ import assert_fingerprint as assert_fingerprint, create_urllib3_context as create_urllib3_context, is_ipaddress as is_ipaddress, resolve_cert_reqs as resolve_cert_reqs, resolve_ssl_version as resolve_ssl_version, ssl_wrap_socket as ssl_wrap_socket
from .util.ssl_match_hostname import CertificateError as CertificateError, match_hostname as match_hostname
from _typeshed import Incomplete

BaseSSLError = ssl.SSLError

class BaseSSLError(BaseException): ...
ConnectionError = ConnectionError

class ConnectionError(Exception): ...
BrokenPipeError = BrokenPipeError

class BrokenPipeError(Exception): ...

log: Incomplete
port_by_scheme: Incomplete
RECENT_DATE: Incomplete

class HTTPConnection(_HTTPConnection):
    """
    Based on :class:`http.client.HTTPConnection` but provides an extra constructor
    backwards-compatibility layer between older and newer Pythons.

    Additional keyword parameters are used to configure attributes of the connection.
    Accepted parameters include:

    - ``strict``: See the documentation on :class:`urllib3.connectionpool.HTTPConnectionPool`
    - ``source_address``: Set the source address for the current connection.
    - ``socket_options``: Set specific options on the underlying socket. If not specified, then
      defaults are loaded from ``HTTPConnection.default_socket_options`` which includes disabling
      Nagle's algorithm (sets TCP_NODELAY to 1) unless the connection is behind a proxy.

      For example, if you wish to enable TCP Keep Alive in addition to the defaults,
      you might pass:

      .. code-block:: python

         HTTPConnection.default_socket_options + [
             (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
         ]

      Or you may want to disable the defaults by passing an empty list (e.g., ``[]``).
    """
    default_port: Incomplete
    default_socket_options: Incomplete
    is_verified: bool
    proxy_is_verified: Incomplete
    source_address: Incomplete
    socket_options: Incomplete
    proxy: Incomplete
    proxy_config: Incomplete
    def __init__(self, *args, **kw) -> None: ...
    @property
    def host(self):
        """
        Getter method to remove any trailing dots that indicate the hostname is an FQDN.

        In general, SSL certificates don't include the trailing dot indicating a
        fully-qualified domain name, and thus, they don't validate properly when
        checked against a domain name that includes the dot. In addition, some
        servers may not expect to receive the trailing dot when provided.

        However, the hostname with trailing dot is critical to DNS resolution; doing a
        lookup with the trailing dot will properly only resolve the appropriate FQDN,
        whereas a lookup without a trailing dot will search the system's search domain
        list. Thus, it's important to keep the original host around for use only in
        those cases where it's appropriate (i.e., when doing DNS lookup to establish the
        actual TCP connection across which we're going to send HTTP requests).
        """
    @host.setter
    def host(self, value) -> None:
        """
        Setter for the `host` property.

        We assume that only urllib3 uses the _dns_host attribute; httplib itself
        only uses `host`, and it seems reasonable that other libraries follow suit.
        """
    def connect(self) -> None: ...
    def putrequest(self, method, url, *args, **kwargs):
        """ """
    def putheader(self, header, *values) -> None:
        """ """
    def request(self, method, url, body: Incomplete | None = None, headers: Incomplete | None = None) -> None: ...
    def request_chunked(self, method, url, body: Incomplete | None = None, headers: Incomplete | None = None) -> None:
        """
        Alternative to the common request method, which sends the
        body with chunked encoding and not as one block
        """

class HTTPSConnection(HTTPConnection):
    """
    Many of the parameters to this constructor are passed to the underlying SSL
    socket by means of :py:func:`urllib3.util.ssl_wrap_socket`.
    """
    default_port: Incomplete
    cert_reqs: Incomplete
    ca_certs: Incomplete
    ca_cert_dir: Incomplete
    ca_cert_data: Incomplete
    ssl_version: Incomplete
    assert_fingerprint: Incomplete
    tls_in_tls_required: bool
    key_file: Incomplete
    cert_file: Incomplete
    key_password: Incomplete
    ssl_context: Incomplete
    server_hostname: Incomplete
    def __init__(self, host, port: Incomplete | None = None, key_file: Incomplete | None = None, cert_file: Incomplete | None = None, key_password: Incomplete | None = None, strict: Incomplete | None = None, timeout=..., ssl_context: Incomplete | None = None, server_hostname: Incomplete | None = None, **kw) -> None: ...
    assert_hostname: Incomplete
    def set_cert(self, key_file: Incomplete | None = None, cert_file: Incomplete | None = None, cert_reqs: Incomplete | None = None, key_password: Incomplete | None = None, ca_certs: Incomplete | None = None, assert_hostname: Incomplete | None = None, assert_fingerprint: Incomplete | None = None, ca_cert_dir: Incomplete | None = None, ca_cert_data: Incomplete | None = None) -> None:
        """
        This method should only be called once, before the connection is used.
        """
    sock: Incomplete
    auto_open: int
    is_verified: Incomplete
    def connect(self) -> None: ...

class DummyConnection:
    """Used to detect a failed ConnectionCls import."""
HTTPSConnection = DummyConnection
VerifiedHTTPSConnection = HTTPSConnection
