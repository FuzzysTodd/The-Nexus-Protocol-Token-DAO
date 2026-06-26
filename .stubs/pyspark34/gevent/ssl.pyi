import ssl as __ssl__
from _typeshed import Incomplete
from gevent._util import copy_globals as copy_globals
from gevent.socket import socket as socket, timeout_default as timeout_default

__implements__: Incomplete
__extra__: Incomplete
__imports__: Incomplete
orig_SSLContext = __ssl__.SSLContext

class _contextawaresock(socket._gevent_sock_class):
    def __init__(self, family, type, proto, fileno, sslsocket_wref) -> None: ...

class _Callback:
    user_function: Incomplete
    def __init__(self, user_function) -> None: ...
    def __call__(self, conn, *args): ...

class SSLContext(orig_SSLContext):
    sslsocket_class: Incomplete
    def wrap_socket(self, sock, server_side: bool = False, do_handshake_on_connect: bool = True, suppress_ragged_eofs: bool = True, server_hostname: Incomplete | None = None, session: Incomplete | None = None): ...
    @orig_SSLContext.options.setter
    def options(self, value) -> None: ...
    @orig_SSLContext.verify_flags.setter
    def verify_flags(self, value) -> None: ...
    @orig_SSLContext.verify_mode.setter
    def verify_mode(self, value) -> None: ...
    @orig_SSLContext.minimum_version.setter
    def minimum_version(self, value) -> None: ...
    @orig_SSLContext.maximum_version.setter
    def maximum_version(self, value) -> None: ...
    @property
    def sni_callback(self): ...
    @sni_callback.setter
    def sni_callback(self, value) -> None: ...
    def set_servername_callback(self, server_name_callback) -> None: ...

class SSLSocket(socket):
    """
    gevent `ssl.SSLSocket
    <https://docs.python.org/3/library/ssl.html#ssl-sockets>`_ for
    Python 3.
    """
    keyfile: Incomplete
    certfile: Incomplete
    cert_reqs: Incomplete
    ssl_version: Incomplete
    ca_certs: Incomplete
    ciphers: Incomplete
    server_side: Incomplete
    server_hostname: Incomplete
    do_handshake_on_connect: Incomplete
    suppress_ragged_eofs: Incomplete
    def __init__(self, sock: Incomplete | None = None, keyfile: Incomplete | None = None, certfile: Incomplete | None = None, server_side: bool = False, cert_reqs=..., ssl_version=..., ca_certs: Incomplete | None = None, do_handshake_on_connect: bool = True, family=..., type=..., proto: int = 0, fileno: Incomplete | None = None, suppress_ragged_eofs: bool = True, npn_protocols: Incomplete | None = None, ciphers: Incomplete | None = None, server_hostname: Incomplete | None = None, _session: Incomplete | None = None, _context: Incomplete | None = None) -> None: ...
    @property
    def context(self): ...
    @context.setter
    def context(self, ctx) -> None: ...
    @property
    def session(self):
        """The SSLSession for client socket."""
    @session.setter
    def session(self, session) -> None: ...
    @property
    def session_reused(self):
        """Was the client session reused during handshake"""
    def dup(self) -> None: ...
    def read(self, nbytes: int = 2014, buffer: Incomplete | None = None):
        """Read up to LEN bytes and return them.
        Return zero-length string on EOF."""
    def write(self, data):
        """Write DATA to the underlying SSL channel.  Returns
        number of bytes of DATA actually transmitted."""
    def getpeercert(self, binary_form: bool = False):
        """Returns a formatted version of the data in the
        certificate provided by the other end of the SSL channel.
        Return None if no certificate was provided, {} if a
        certificate was provided, but not validated."""
    def selected_npn_protocol(self): ...
    def selected_alpn_protocol(self): ...
    def shared_ciphers(self):
        """Return a list of ciphers shared by the client during the handshake or
            None if this is not a valid server connection.
            """
    def version(self):
        """Return a string identifying the protocol version used by the
            current SSL channel. """
    def cipher(self): ...
    def compression(self): ...
    def send(self, data, flags: int = 0, timeout=...): ...
    def sendto(self, data, flags_or_addr, addr: Incomplete | None = None): ...
    def sendmsg(self, *args, **kwargs) -> None: ...
    def sendall(self, data, flags: int = 0): ...
    def recv(self, buflen: int = 1024, flags: int = 0): ...
    def recv_into(self, buffer, nbytes: Incomplete | None = None, flags: int = 0): ...
    def recvfrom(self, buflen: int = 1024, flags: int = 0): ...
    def recvfrom_into(self, buffer, nbytes: Incomplete | None = None, flags: int = 0): ...
    def recvmsg(self, *args, **kwargs) -> None: ...
    def recvmsg_into(self, *args, **kwargs) -> None: ...
    def pending(self): ...
    def shutdown(self, how) -> None: ...
    def unwrap(self): ...
    def do_handshake(self) -> None:
        """Perform a TLS/SSL handshake."""
    def connect(self, addr) -> None:
        """Connects to remote ADDR, and then wraps the connection in
        an SSL channel."""
    def connect_ex(self, addr):
        """Connects to remote ADDR, and then wraps the connection in
        an SSL channel."""
    def accept(self):
        """
        Accepts a new connection from a remote client, and returns a
        tuple containing that new connection wrapped with a
        server-side SSL channel, and the address of the remote client.
        """
    def get_channel_binding(self, cb_type: str = 'tls-unique'):
        """Get channel binding data for current connection.  Raise ValueError
        if the requested `cb_type` is not supported.  Return bytes of the data
        or None if the data is not available (e.g. before the handshake).
        """
    def verify_client_post_handshake(self): ...

def wrap_socket(sock, keyfile: Incomplete | None = None, certfile: Incomplete | None = None, server_side: bool = False, cert_reqs=..., ssl_version=..., ca_certs: Incomplete | None = None, do_handshake_on_connect: bool = True, suppress_ragged_eofs: bool = True, ciphers: Incomplete | None = None): ...
def get_server_certificate(addr, ssl_version=..., ca_certs: Incomplete | None = None):
    """Retrieve the certificate from the server at the specified address,
    and return it as a PEM-encoded string.
    If 'ca_certs' is specified, validate the server cert against it.
    If 'ssl_version' is specified, use it in the connection attempt."""
