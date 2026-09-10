import typing as _t
from .encoding import base64_decode as base64_decode, base64_encode as base64_encode, want_bytes as want_bytes
from .exc import BadSignature as BadSignature
from _typeshed import Incomplete

class SigningAlgorithm:
    """Subclasses must implement :meth:`get_signature` to provide
    signature generation functionality.
    """
    def get_signature(self, key: bytes, value: bytes) -> bytes:
        """Returns the signature for the given key and value."""
    def verify_signature(self, key: bytes, value: bytes, sig: bytes) -> bool:
        """Verifies the given signature matches the expected
        signature.
        """

class NoneAlgorithm(SigningAlgorithm):
    """Provides an algorithm that does not perform any signing and
    returns an empty signature.
    """
    def get_signature(self, key: bytes, value: bytes) -> bytes: ...

class HMACAlgorithm(SigningAlgorithm):
    """Provides signature generation using HMACs."""
    default_digest_method: _t.Any
    digest_method: Incomplete
    def __init__(self, digest_method: _t.Any = None) -> None: ...
    def get_signature(self, key: bytes, value: bytes) -> bytes: ...

class Signer:
    """A signer securely signs bytes, then unsigns them to verify that
    the value hasn't been changed.

    The secret key should be a random string of ``bytes`` and should not
    be saved to code or version control. Different salts should be used
    to distinguish signing in different contexts. See :doc:`/concepts`
    for information about the security of the secret key and salt.

    :param secret_key: The secret key to sign and verify with. Can be a
        list of keys, oldest to newest, to support key rotation.
    :param salt: Extra key to combine with ``secret_key`` to distinguish
        signatures in different contexts.
    :param sep: Separator between the signature and value.
    :param key_derivation: How to derive the signing key from the secret
        key and salt. Possible values are ``concat``, ``django-concat``,
        or ``hmac``. Defaults to :attr:`default_key_derivation`, which
        defaults to ``django-concat``.
    :param digest_method: Hash function to use when generating the HMAC
        signature. Defaults to :attr:`default_digest_method`, which
        defaults to :func:`hashlib.sha1`. Note that the security of the
        hash alone doesn't apply when used intermediately in HMAC.
    :param algorithm: A :class:`SigningAlgorithm` instance to use
        instead of building a default :class:`HMACAlgorithm` with the
        ``digest_method``.

    .. versionchanged:: 2.0
        Added support for key rotation by passing a list to
        ``secret_key``.

    .. versionchanged:: 0.18
        ``algorithm`` was added as an argument to the class constructor.

    .. versionchanged:: 0.14
        ``key_derivation`` and ``digest_method`` were added as arguments
        to the class constructor.
    """
    default_digest_method: _t.Any
    default_key_derivation: str
    secret_keys: Incomplete
    sep: Incomplete
    salt: Incomplete
    key_derivation: Incomplete
    digest_method: Incomplete
    algorithm: Incomplete
    def __init__(self, secret_key: _t_secret_key, salt: _t_opt_str_bytes = b'itsdangerous.Signer', sep: _t_str_bytes = b'.', key_derivation: str | None = None, digest_method: _t.Any | None = None, algorithm: SigningAlgorithm | None = None) -> None: ...
    @property
    def secret_key(self) -> bytes:
        """The newest (last) entry in the :attr:`secret_keys` list. This
        is for compatibility from before key rotation support was added.
        """
    def derive_key(self, secret_key: _t_opt_str_bytes = None) -> bytes:
        """This method is called to derive the key. The default key
        derivation choices can be overridden here. Key derivation is not
        intended to be used as a security method to make a complex key
        out of a short password. Instead you should use large random
        secret keys.

        :param secret_key: A specific secret key to derive from.
            Defaults to the last item in :attr:`secret_keys`.

        .. versionchanged:: 2.0
            Added the ``secret_key`` parameter.
        """
    def get_signature(self, value: _t_str_bytes) -> bytes:
        """Returns the signature for the given value."""
    def sign(self, value: _t_str_bytes) -> bytes:
        """Signs the given string."""
    def verify_signature(self, value: _t_str_bytes, sig: _t_str_bytes) -> bool:
        """Verifies the signature for the given value."""
    def unsign(self, signed_value: _t_str_bytes) -> bytes:
        """Unsigns the given string."""
    def validate(self, signed_value: _t_str_bytes) -> bool:
        """Only validates the given signed value. Returns ``True`` if
        the signature exists and is valid.
        """
