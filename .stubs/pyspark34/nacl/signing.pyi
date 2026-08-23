from _typeshed import Incomplete
from nacl import encoding as encoding
from nacl.public import PrivateKey as _Curve25519_PrivateKey, PublicKey as _Curve25519_PublicKey
from nacl.utils import StringFixer as StringFixer, random as random

class SignedMessage(bytes):
    """
    A bytes subclass that holds a messaged that has been signed by a
    :class:`SigningKey`.
    """
    @property
    def signature(self) -> bytes:
        """
        The signature contained within the :class:`SignedMessage`.
        """
    @property
    def message(self) -> bytes:
        """
        The message contained within the :class:`SignedMessage`.
        """

class VerifyKey(encoding.Encodable, StringFixer):
    """
    The public key counterpart to an Ed25519 SigningKey for producing digital
    signatures.

    :param key: [:class:`bytes`] Serialized Ed25519 public key
    :param encoder: A class that is able to decode the `key`
    """
    def __init__(self, key: bytes, encoder: encoding.Encoder = ...) -> None: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def verify(self, smessage: bytes, signature: bytes | None = None, encoder: encoding.Encoder = ...) -> bytes:
        """
        Verifies the signature of a signed message, returning the message
        if it has not been tampered with else raising
        :class:`~nacl.signing.BadSignatureError`.

        :param smessage: [:class:`bytes`] Either the original messaged or a
            signature and message concated together.
        :param signature: [:class:`bytes`] If an unsigned message is given for
            smessage then the detached signature must be provided.
        :param encoder: A class that is able to decode the secret message and
            signature.
        :rtype: :class:`bytes`
        """
    def to_curve25519_public_key(self) -> _Curve25519_PublicKey:
        """
        Converts a :class:`~nacl.signing.VerifyKey` to a
        :class:`~nacl.public.PublicKey`

        :rtype: :class:`~nacl.public.PublicKey`
        """

class SigningKey(encoding.Encodable, StringFixer):
    """
    Private key for producing digital signatures using the Ed25519 algorithm.

    Signing keys are produced from a 32-byte (256-bit) random seed value. This
    value can be passed into the :class:`~nacl.signing.SigningKey` as a
    :func:`bytes` whose length is 32.

    .. warning:: This **must** be protected and remain secret. Anyone who knows
        the value of your :class:`~nacl.signing.SigningKey` or it's seed can
        masquerade as you.

    :param seed: [:class:`bytes`] Random 32-byte value (i.e. private key)
    :param encoder: A class that is able to decode the seed

    :ivar: verify_key: [:class:`~nacl.signing.VerifyKey`] The verify
        (i.e. public) key that corresponds with this signing key.
    """
    verify_key: Incomplete
    def __init__(self, seed: bytes, encoder: encoding.Encoder = ...) -> None: ...
    def __bytes__(self) -> bytes: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @classmethod
    def generate(cls) -> SigningKey:
        """
        Generates a random :class:`~nacl.signing.SigningKey` object.

        :rtype: :class:`~nacl.signing.SigningKey`
        """
    def sign(self, message: bytes, encoder: encoding.Encoder = ...) -> SignedMessage:
        """
        Sign a message using this key.

        :param message: [:class:`bytes`] The data to be signed.
        :param encoder: A class that is used to encode the signed message.
        :rtype: :class:`~nacl.signing.SignedMessage`
        """
    def to_curve25519_private_key(self) -> _Curve25519_PrivateKey:
        """
        Converts a :class:`~nacl.signing.SigningKey` to a
        :class:`~nacl.public.PrivateKey`

        :rtype: :class:`~nacl.public.PrivateKey`
        """
