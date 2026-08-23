from _typeshed import Incomplete

__all__ = ['inject_into_urllib3', 'extract_from_urllib3']

def inject_into_urllib3() -> None:
    """
    Monkey-patch urllib3 with SecureTransport-backed SSL-support.
    """
def extract_from_urllib3() -> None:
    """
    Undo monkey-patching by :func:`inject_into_urllib3`.
    """

class WrappedSocket:
    """
    API-compatibility wrapper for Python's OpenSSL wrapped socket object.

    Note: _makefile_refs, _drop(), and _reuse() are needed for the garbage
    collector of PyPy.
    """
    socket: Incomplete
    context: Incomplete
    def __init__(self, socket) -> None: ...
    def handshake(self, server_hostname, verify, trust_bundle, min_version, max_version, client_cert, client_key, client_key_passphrase, alpn_protocols) -> None:
        """
        Actually performs the TLS handshake. This is run automatically by
        wrapped socket, and shouldn't be needed in user code.
        """
    def fileno(self): ...
    def recv(self, bufsiz): ...
    def recv_into(self, buffer, nbytes: Incomplete | None = None): ...
    def settimeout(self, timeout) -> None: ...
    def gettimeout(self): ...
    def send(self, data): ...
    def sendall(self, data) -> None: ...
    def shutdown(self) -> None: ...
    def close(self): ...
    def getpeercert(self, binary_form: bool = False): ...
    def version(self): ...

class SecureTransportContext:
    """
    I am a wrapper class for the SecureTransport library, to translate the
    interface of the standard library ``SSLContext`` object to calls into
    SecureTransport.
    """
    def __init__(self, protocol) -> None: ...
    @property
    def check_hostname(self):
        """
        SecureTransport cannot have its hostname checking disabled. For more,
        see the comment on getpeercert() in this file.
        """
    @check_hostname.setter
    def check_hostname(self, value) -> None:
        """
        SecureTransport cannot have its hostname checking disabled. For more,
        see the comment on getpeercert() in this file.
        """
    @property
    def options(self): ...
    @options.setter
    def options(self, value) -> None: ...
    @property
    def verify_mode(self): ...
    @verify_mode.setter
    def verify_mode(self, value) -> None: ...
    def set_default_verify_paths(self) -> None: ...
    def load_default_certs(self): ...
    def set_ciphers(self, ciphers) -> None: ...
    def load_verify_locations(self, cafile: Incomplete | None = None, capath: Incomplete | None = None, cadata: Incomplete | None = None) -> None: ...
    def load_cert_chain(self, certfile, keyfile: Incomplete | None = None, password: Incomplete | None = None) -> None: ...
    def set_alpn_protocols(self, protocols) -> None:
        """
        Sets the ALPN protocols that will later be set on the context.

        Raises a NotImplementedError if ALPN is not supported.
        """
    def wrap_socket(self, sock, server_side: bool = False, do_handshake_on_connect: bool = True, suppress_ragged_eofs: bool = True, server_hostname: Incomplete | None = None): ...
