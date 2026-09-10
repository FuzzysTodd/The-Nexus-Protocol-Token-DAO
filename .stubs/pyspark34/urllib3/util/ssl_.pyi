from ..exceptions import InsecurePlatformWarning as InsecurePlatformWarning, ProxySchemeUnsupported as ProxySchemeUnsupported, SNIMissingWarning as SNIMissingWarning, SSLError as SSLError
from .ssltransport import SSLTransport as SSLTransport
from .url import BRACELESS_IPV6_ADDRZ_RE as BRACELESS_IPV6_ADDRZ_RE, IPV4_RE as IPV4_RE
from _typeshed import Incomplete
from ssl import PROTOCOL_SSLv23 as PROTOCOL_TLS

SSLContext: Incomplete
SSLTransport: Incomplete
HAS_SNI: bool
IS_PYOPENSSL: bool
IS_SECURETRANSPORT: bool
ALPN_PROTOCOLS: Incomplete
HASHFUNC_MAP: Incomplete
PROTOCOL_SSLv23 = PROTOCOL_TLS
PROTOCOL_SSLv23 = PROTOCOL_TLS
PROTOCOL_TLS_CLIENT = PROTOCOL_TLS
DEFAULT_CIPHERS: Incomplete

class SSLContext:
    protocol: Incomplete
    check_hostname: bool
    verify_mode: Incomplete
    ca_certs: Incomplete
    options: int
    certfile: Incomplete
    keyfile: Incomplete
    ciphers: Incomplete
    def __init__(self, protocol_version) -> None: ...
    def load_cert_chain(self, certfile, keyfile) -> None: ...
    def load_verify_locations(self, cafile: Incomplete | None = None, capath: Incomplete | None = None, cadata: Incomplete | None = None) -> None: ...
    def set_ciphers(self, cipher_suite) -> None: ...
    def wrap_socket(self, socket, server_hostname: Incomplete | None = None, server_side: bool = False): ...

def assert_fingerprint(cert, fingerprint) -> None:
    """
    Checks if given fingerprint matches the supplied certificate.

    :param cert:
        Certificate as bytes object.
    :param fingerprint:
        Fingerprint as string of hexdigits, can be interspersed by colons.
    """
def resolve_cert_reqs(candidate):
    """
    Resolves the argument to a numeric constant, which can be passed to
    the wrap_socket function/method from the ssl module.
    Defaults to :data:`ssl.CERT_REQUIRED`.
    If given a string it is assumed to be the name of the constant in the
    :mod:`ssl` module or its abbreviation.
    (So you can specify `REQUIRED` instead of `CERT_REQUIRED`.
    If it's neither `None` nor a string we assume it is already the numeric
    constant which can directly be passed to wrap_socket.
    """
def resolve_ssl_version(candidate):
    """
    like resolve_cert_reqs
    """
def create_urllib3_context(ssl_version: Incomplete | None = None, cert_reqs: Incomplete | None = None, options: Incomplete | None = None, ciphers: Incomplete | None = None):
    """All arguments have the same meaning as ``ssl_wrap_socket``.

    By default, this function does a lot of the same work that
    ``ssl.create_default_context`` does on Python 3.4+. It:

    - Disables SSLv2, SSLv3, and compression
    - Sets a restricted set of server ciphers

    If you wish to enable SSLv3, you can do::

        from urllib3.util import ssl_
        context = ssl_.create_urllib3_context()
        context.options &= ~ssl_.OP_NO_SSLv3

    You can do the same to enable compression (substituting ``COMPRESSION``
    for ``SSLv3`` in the last line above).

    :param ssl_version:
        The desired protocol version to use. This will default to
        PROTOCOL_SSLv23 which will negotiate the highest protocol that both
        the server and your installation of OpenSSL support.
    :param cert_reqs:
        Whether to require the certificate verification. This defaults to
        ``ssl.CERT_REQUIRED``.
    :param options:
        Specific OpenSSL options. These default to ``ssl.OP_NO_SSLv2``,
        ``ssl.OP_NO_SSLv3``, ``ssl.OP_NO_COMPRESSION``, and ``ssl.OP_NO_TICKET``.
    :param ciphers:
        Which cipher suites to allow the server to select.
    :returns:
        Constructed SSLContext object with specified options
    :rtype: SSLContext
    """
def ssl_wrap_socket(sock, keyfile: Incomplete | None = None, certfile: Incomplete | None = None, cert_reqs: Incomplete | None = None, ca_certs: Incomplete | None = None, server_hostname: Incomplete | None = None, ssl_version: Incomplete | None = None, ciphers: Incomplete | None = None, ssl_context: Incomplete | None = None, ca_cert_dir: Incomplete | None = None, key_password: Incomplete | None = None, ca_cert_data: Incomplete | None = None, tls_in_tls: bool = False):
    """
    All arguments except for server_hostname, ssl_context, and ca_cert_dir have
    the same meaning as they do when using :func:`ssl.wrap_socket`.

    :param server_hostname:
        When SNI is supported, the expected hostname of the certificate
    :param ssl_context:
        A pre-made :class:`SSLContext` object. If none is provided, one will
        be created using :func:`create_urllib3_context`.
    :param ciphers:
        A string of ciphers we wish the client to support.
    :param ca_cert_dir:
        A directory containing CA certificates in multiple separate files, as
        supported by OpenSSL's -CApath flag or the capath argument to
        SSLContext.load_verify_locations().
    :param key_password:
        Optional password if the keyfile is encrypted.
    :param ca_cert_data:
        Optional string containing CA certificates in PEM format suitable for
        passing as the cadata parameter to SSLContext.load_verify_locations()
    :param tls_in_tls:
        Use SSLTransport to wrap the existing socket.
    """
def is_ipaddress(hostname):
    """Detects whether the hostname given is an IPv4 or IPv6 address.
    Also detects IPv6 addresses with Zone IDs.

    :param str hostname: Hostname to examine.
    :return: True if the hostname is an IP address, False otherwise.
    """
