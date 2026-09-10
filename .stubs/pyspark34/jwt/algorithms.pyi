import abc
from .exceptions import InvalidKeyError as InvalidKeyError
from .types import HashlibHash as HashlibHash, JWKDict as JWKDict
from .utils import base64url_decode as base64url_decode, base64url_encode as base64url_encode, der_to_raw_signature as der_to_raw_signature, force_bytes as force_bytes, from_base64url_uint as from_base64url_uint, is_pem_format as is_pem_format, is_ssh_key as is_ssh_key, raw_to_der_signature as raw_to_der_signature, to_base64url_uint as to_base64url_uint
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurve as EllipticCurve, EllipticCurvePrivateKey
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PrivateKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from typing import Any, ClassVar, Literal, NoReturn, overload

has_crypto: bool
AllowedRSAKeys: Incomplete
AllowedECKeys: Incomplete
AllowedOKPKeys: Incomplete
AllowedKeys: Incomplete
AllowedPrivateKeys: Incomplete
AllowedPublicKeys: Incomplete
requires_cryptography: Incomplete

def get_default_algorithms() -> dict[str, Algorithm]:
    """
    Returns the algorithms that are implemented by the library.
    """

class Algorithm(ABC, metaclass=abc.ABCMeta):
    """
    The interface for an algorithm used to sign and verify tokens.
    """
    def compute_hash_digest(self, bytestr: bytes) -> bytes:
        """
        Compute a hash digest using the specified algorithm's hash algorithm.

        If there is no hash algorithm, raises a NotImplementedError.
        """
    @abstractmethod
    def prepare_key(self, key: Any) -> Any:
        """
        Performs necessary validation and conversions on the key and returns
        the key value in the proper format for sign() and verify().
        """
    @abstractmethod
    def sign(self, msg: bytes, key: Any) -> bytes:
        """
        Returns a digital signature for the specified message
        using the specified key value.
        """
    @abstractmethod
    def verify(self, msg: bytes, key: Any, sig: bytes) -> bool:
        """
        Verifies that the specified digital signature is valid
        for the specified message and key values.
        """
    @overload
    @staticmethod
    @abstractmethod
    def to_jwk(key_obj, as_dict: Literal[True]) -> JWKDict: ...
    @overload
    @staticmethod
    @abstractmethod
    def to_jwk(key_obj, as_dict: Literal[False] = False) -> str: ...
    @staticmethod
    @abstractmethod
    def from_jwk(jwk: str | JWKDict) -> Any:
        """
        Deserializes a given key from JWK back into a key object
        """

class NoneAlgorithm(Algorithm):
    """
    Placeholder for use when no signing or verification
    operations are required.
    """
    def prepare_key(self, key: str | None) -> None: ...
    def sign(self, msg: bytes, key: None) -> bytes: ...
    def verify(self, msg: bytes, key: None, sig: bytes) -> bool: ...
    @staticmethod
    def to_jwk(key_obj: Any, as_dict: bool = False) -> NoReturn: ...
    @staticmethod
    def from_jwk(jwk: str | JWKDict) -> NoReturn: ...

class HMACAlgorithm(Algorithm):
    """
    Performs signing and verification operations using HMAC
    and the specified hash function.
    """
    SHA256: ClassVar[HashlibHash]
    SHA384: ClassVar[HashlibHash]
    SHA512: ClassVar[HashlibHash]
    hash_alg: Incomplete
    def __init__(self, hash_alg: HashlibHash) -> None: ...
    def prepare_key(self, key: str | bytes) -> bytes: ...
    @overload
    @staticmethod
    def to_jwk(key_obj: str | bytes, as_dict: Literal[True]) -> JWKDict: ...
    @overload
    @staticmethod
    def to_jwk(key_obj: str | bytes, as_dict: Literal[False] = False) -> str: ...
    @staticmethod
    def from_jwk(jwk: str | JWKDict) -> bytes: ...
    def sign(self, msg: bytes, key: bytes) -> bytes: ...
    def verify(self, msg: bytes, key: bytes, sig: bytes) -> bool: ...

class RSAAlgorithm(Algorithm):
    """
        Performs signing and verification operations using
        RSASSA-PKCS-v1_5 and the specified hash function.
        """
    SHA256: ClassVar[type[hashes.HashAlgorithm]]
    SHA384: ClassVar[type[hashes.HashAlgorithm]]
    SHA512: ClassVar[type[hashes.HashAlgorithm]]
    hash_alg: Incomplete
    def __init__(self, hash_alg: type[hashes.HashAlgorithm]) -> None: ...
    def prepare_key(self, key: AllowedRSAKeys | str | bytes) -> AllowedRSAKeys: ...
    @overload
    @staticmethod
    def to_jwk(key_obj: AllowedRSAKeys, as_dict: Literal[True]) -> JWKDict: ...
    @overload
    @staticmethod
    def to_jwk(key_obj: AllowedRSAKeys, as_dict: Literal[False] = False) -> str: ...
    @staticmethod
    def from_jwk(jwk: str | JWKDict) -> AllowedRSAKeys: ...
    def sign(self, msg: bytes, key: RSAPrivateKey) -> bytes: ...
    def verify(self, msg: bytes, key: RSAPublicKey, sig: bytes) -> bool: ...

class ECAlgorithm(Algorithm):
    """
        Performs signing and verification operations using
        ECDSA and the specified hash function
        """
    SHA256: ClassVar[type[hashes.HashAlgorithm]]
    SHA384: ClassVar[type[hashes.HashAlgorithm]]
    SHA512: ClassVar[type[hashes.HashAlgorithm]]
    hash_alg: Incomplete
    def __init__(self, hash_alg: type[hashes.HashAlgorithm]) -> None: ...
    def prepare_key(self, key: AllowedECKeys | str | bytes) -> AllowedECKeys: ...
    def sign(self, msg: bytes, key: EllipticCurvePrivateKey) -> bytes: ...
    def verify(self, msg: bytes, key: AllowedECKeys, sig: bytes) -> bool: ...
    @overload
    @staticmethod
    def to_jwk(key_obj: AllowedECKeys, as_dict: Literal[True]) -> JWKDict: ...
    @overload
    @staticmethod
    def to_jwk(key_obj: AllowedECKeys, as_dict: Literal[False] = False) -> str: ...
    @staticmethod
    def from_jwk(jwk: str | JWKDict) -> AllowedECKeys: ...

class RSAPSSAlgorithm(RSAAlgorithm):
    """
        Performs a signature using RSASSA-PSS with MGF1
        """
    def sign(self, msg: bytes, key: RSAPrivateKey) -> bytes: ...
    def verify(self, msg: bytes, key: RSAPublicKey, sig: bytes) -> bool: ...

class OKPAlgorithm(Algorithm):
    """
        Performs signing and verification operations using EdDSA

        This class requires ``cryptography>=2.6`` to be installed.
        """
    def __init__(self, **kwargs: Any) -> None: ...
    def prepare_key(self, key: AllowedOKPKeys | str | bytes) -> AllowedOKPKeys: ...
    def sign(self, msg: str | bytes, key: Ed25519PrivateKey | Ed448PrivateKey) -> bytes:
        """
            Sign a message ``msg`` using the EdDSA private key ``key``
            :param str|bytes msg: Message to sign
            :param Ed25519PrivateKey}Ed448PrivateKey key: A :class:`.Ed25519PrivateKey`
                or :class:`.Ed448PrivateKey` isinstance
            :return bytes signature: The signature, as bytes
            """
    def verify(self, msg: str | bytes, key: AllowedOKPKeys, sig: str | bytes) -> bool:
        """
            Verify a given ``msg`` against a signature ``sig`` using the EdDSA key ``key``

            :param str|bytes sig: EdDSA signature to check ``msg`` against
            :param str|bytes msg: Message to sign
            :param Ed25519PrivateKey|Ed25519PublicKey|Ed448PrivateKey|Ed448PublicKey key:
                A private or public EdDSA key instance
            :return bool verified: True if signature is valid, False if not.
            """
    @overload
    @staticmethod
    def to_jwk(key: AllowedOKPKeys, as_dict: Literal[True]) -> JWKDict: ...
    @overload
    @staticmethod
    def to_jwk(key: AllowedOKPKeys, as_dict: Literal[False] = False) -> str: ...
    @staticmethod
    def from_jwk(jwk: str | JWKDict) -> AllowedOKPKeys: ...
