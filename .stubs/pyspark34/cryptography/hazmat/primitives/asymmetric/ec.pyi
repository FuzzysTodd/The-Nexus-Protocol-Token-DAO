import abc
import typing
from _typeshed import Incomplete
from cryptography import utils as utils
from cryptography.hazmat._oid import ObjectIdentifier as ObjectIdentifier
from cryptography.hazmat.primitives import _serialization, hashes as hashes
from cryptography.hazmat.primitives.asymmetric import utils as asym_utils

class EllipticCurveOID:
    SECP192R1: Incomplete
    SECP224R1: Incomplete
    SECP256K1: Incomplete
    SECP256R1: Incomplete
    SECP384R1: Incomplete
    SECP521R1: Incomplete
    BRAINPOOLP256R1: Incomplete
    BRAINPOOLP384R1: Incomplete
    BRAINPOOLP512R1: Incomplete
    SECT163K1: Incomplete
    SECT163R2: Incomplete
    SECT233K1: Incomplete
    SECT233R1: Incomplete
    SECT283K1: Incomplete
    SECT283R1: Incomplete
    SECT409K1: Incomplete
    SECT409R1: Incomplete
    SECT571K1: Incomplete
    SECT571R1: Incomplete

class EllipticCurve(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        """
        The name of the curve. e.g. secp256r1.
        """
    @property
    @abc.abstractmethod
    def key_size(self) -> int:
        """
        Bit size of a secret scalar for the curve.
        """

class EllipticCurveSignatureAlgorithm(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def algorithm(self) -> asym_utils.Prehashed | hashes.HashAlgorithm:
        """
        The digest algorithm used with this signature.
        """

class EllipticCurvePrivateKey(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def exchange(self, algorithm: ECDH, peer_public_key: EllipticCurvePublicKey) -> bytes:
        """
        Performs a key exchange operation using the provided algorithm with the
        provided peer's public key.
        """
    @abc.abstractmethod
    def public_key(self) -> EllipticCurvePublicKey:
        """
        The EllipticCurvePublicKey for this private key.
        """
    @property
    @abc.abstractmethod
    def curve(self) -> EllipticCurve:
        """
        The EllipticCurve that this key is on.
        """
    @property
    @abc.abstractmethod
    def key_size(self) -> int:
        """
        Bit size of a secret scalar for the curve.
        """
    @abc.abstractmethod
    def sign(self, data: bytes, signature_algorithm: EllipticCurveSignatureAlgorithm) -> bytes:
        """
        Signs the data
        """
    @abc.abstractmethod
    def private_numbers(self) -> EllipticCurvePrivateNumbers:
        """
        Returns an EllipticCurvePrivateNumbers.
        """
    @abc.abstractmethod
    def private_bytes(self, encoding: _serialization.Encoding, format: _serialization.PrivateFormat, encryption_algorithm: _serialization.KeySerializationEncryption) -> bytes:
        """
        Returns the key serialized as bytes.
        """
EllipticCurvePrivateKeyWithSerialization = EllipticCurvePrivateKey

class EllipticCurvePublicKey(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def curve(self) -> EllipticCurve:
        """
        The EllipticCurve that this key is on.
        """
    @property
    @abc.abstractmethod
    def key_size(self) -> int:
        """
        Bit size of a secret scalar for the curve.
        """
    @abc.abstractmethod
    def public_numbers(self) -> EllipticCurvePublicNumbers:
        """
        Returns an EllipticCurvePublicNumbers.
        """
    @abc.abstractmethod
    def public_bytes(self, encoding: _serialization.Encoding, format: _serialization.PublicFormat) -> bytes:
        """
        Returns the key serialized as bytes.
        """
    @abc.abstractmethod
    def verify(self, signature: bytes, data: bytes, signature_algorithm: EllipticCurveSignatureAlgorithm) -> None:
        """
        Verifies the signature of the data.
        """
    @classmethod
    def from_encoded_point(cls, curve: EllipticCurve, data: bytes) -> EllipticCurvePublicKey: ...
    @abc.abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Checks equality.
        """
EllipticCurvePublicKeyWithSerialization = EllipticCurvePublicKey

class SECT571R1(EllipticCurve):
    name: str
    key_size: int

class SECT409R1(EllipticCurve):
    name: str
    key_size: int

class SECT283R1(EllipticCurve):
    name: str
    key_size: int

class SECT233R1(EllipticCurve):
    name: str
    key_size: int

class SECT163R2(EllipticCurve):
    name: str
    key_size: int

class SECT571K1(EllipticCurve):
    name: str
    key_size: int

class SECT409K1(EllipticCurve):
    name: str
    key_size: int

class SECT283K1(EllipticCurve):
    name: str
    key_size: int

class SECT233K1(EllipticCurve):
    name: str
    key_size: int

class SECT163K1(EllipticCurve):
    name: str
    key_size: int

class SECP521R1(EllipticCurve):
    name: str
    key_size: int

class SECP384R1(EllipticCurve):
    name: str
    key_size: int

class SECP256R1(EllipticCurve):
    name: str
    key_size: int

class SECP256K1(EllipticCurve):
    name: str
    key_size: int

class SECP224R1(EllipticCurve):
    name: str
    key_size: int

class SECP192R1(EllipticCurve):
    name: str
    key_size: int

class BrainpoolP256R1(EllipticCurve):
    name: str
    key_size: int

class BrainpoolP384R1(EllipticCurve):
    name: str
    key_size: int

class BrainpoolP512R1(EllipticCurve):
    name: str
    key_size: int

class ECDSA(EllipticCurveSignatureAlgorithm):
    def __init__(self, algorithm: asym_utils.Prehashed | hashes.HashAlgorithm) -> None: ...
    @property
    def algorithm(self) -> asym_utils.Prehashed | hashes.HashAlgorithm: ...

def generate_private_key(curve: EllipticCurve, backend: typing.Any = None) -> EllipticCurvePrivateKey: ...
def derive_private_key(private_value: int, curve: EllipticCurve, backend: typing.Any = None) -> EllipticCurvePrivateKey: ...

class EllipticCurvePublicNumbers:
    def __init__(self, x: int, y: int, curve: EllipticCurve) -> None: ...
    def public_key(self, backend: typing.Any = None) -> EllipticCurvePublicKey: ...
    @property
    def curve(self) -> EllipticCurve: ...
    @property
    def x(self) -> int: ...
    @property
    def y(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class EllipticCurvePrivateNumbers:
    def __init__(self, private_value: int, public_numbers: EllipticCurvePublicNumbers) -> None: ...
    def private_key(self, backend: typing.Any = None) -> EllipticCurvePrivateKey: ...
    @property
    def private_value(self) -> int: ...
    @property
    def public_numbers(self) -> EllipticCurvePublicNumbers: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class ECDH: ...

def get_curve_for_oid(oid: ObjectIdentifier) -> typing.Type[EllipticCurve]: ...
