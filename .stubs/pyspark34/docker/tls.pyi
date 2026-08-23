from . import errors as errors
from .transport import SSLHTTPAdapter as SSLHTTPAdapter
from _typeshed import Incomplete

class TLSConfig:
    """
    TLS configuration.

    Args:
        client_cert (tuple of str): Path to client cert, path to client key.
        ca_cert (str): Path to CA cert file.
        verify (bool or str): This can be a bool or a path to a CA cert
            file to verify against. If ``True``, verify using ca_cert;
            if ``False`` or not specified, do not verify.
        ssl_version (int): A valid `SSL version`_.
        assert_hostname (bool): Verify the hostname of the server.

    .. _`SSL version`:
        https://docs.python.org/3.5/library/ssl.html#ssl.PROTOCOL_TLSv1
    """
    cert: Incomplete
    ca_cert: Incomplete
    verify: Incomplete
    ssl_version: Incomplete
    assert_hostname: Incomplete
    assert_fingerprint: Incomplete
    def __init__(self, client_cert: Incomplete | None = None, ca_cert: Incomplete | None = None, verify: Incomplete | None = None, ssl_version: Incomplete | None = None, assert_hostname: Incomplete | None = None, assert_fingerprint: Incomplete | None = None) -> None: ...
    def configure_client(self, client) -> None:
        """
        Configure a client with these TLS options.
        """
