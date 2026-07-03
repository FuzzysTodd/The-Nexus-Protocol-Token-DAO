class AadClientCertificate:
    """Wraps 'cryptography' to provide the crypto operations AadClient requires for certificate authentication.

    :param bytes pem_bytes: bytes of a a PEM-encoded certificate including the (RSA) private key
    :param bytes password: (optional) the certificate's password
    """
    def __init__(self, pem_bytes: bytes, password: bytes | None = None) -> None: ...
    @property
    def thumbprint(self) -> str:
        """The certificate's SHA1 thumbprint as a base64url-encoded string.

        :rtype: str
        """
    def sign(self, plaintext: bytes) -> bytes:
        """Sign bytes using RS256.

        :param bytes plaintext: Bytes to sign.
        :return: The signature.
        :rtype: bytes
        """
