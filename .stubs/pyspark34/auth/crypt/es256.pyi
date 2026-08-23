from _typeshed import Incomplete
from google.auth.crypt import base

class ES256Verifier(base.Verifier):
    """Verifies ECDSA cryptographic signatures using public keys.

    Args:
        public_key (
                cryptography.hazmat.primitives.asymmetric.ec.ECDSAPublicKey):
            The public key used to verify signatures.
    """
    def __init__(self, public_key) -> None: ...
    def verify(self, message, signature): ...
    @classmethod
    def from_string(cls, public_key):
        """Construct an Verifier instance from a public key or public
        certificate string.

        Args:
            public_key (Union[str, bytes]): The public key in PEM format or the
                x509 public key certificate.

        Returns:
            Verifier: The constructed verifier.

        Raises:
            ValueError: If the public key can't be parsed.
        """

class ES256Signer(base.Signer, base.FromServiceAccountMixin):
    """Signs messages with an ECDSA private key.

    Args:
        private_key (
                cryptography.hazmat.primitives.asymmetric.ec.ECDSAPrivateKey):
            The private key to sign with.
        key_id (str): Optional key ID used to identify this private key. This
            can be useful to associate the private key with its associated
            public key or certificate.
    """
    def __init__(self, private_key, key_id: Incomplete | None = None) -> None: ...
    @property
    def key_id(self): ...
    def sign(self, message): ...
    @classmethod
    def from_string(cls, key, key_id: Incomplete | None = None):
        '''Construct a RSASigner from a private key in PEM format.

        Args:
            key (Union[bytes, str]): Private key in PEM format.
            key_id (str): An optional key id used to identify the private key.

        Returns:
            google.auth.crypt._cryptography_rsa.RSASigner: The
            constructed signer.

        Raises:
            ValueError: If ``key`` is not ``bytes`` or ``str`` (unicode).
            UnicodeDecodeError: If ``key`` is ``bytes`` but cannot be decoded
                into a UTF-8 ``str``.
            ValueError: If ``cryptography`` "Could not deserialize key data."
        '''
