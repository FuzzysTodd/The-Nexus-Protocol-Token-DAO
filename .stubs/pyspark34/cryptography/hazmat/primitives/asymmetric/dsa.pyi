import abc
import typing
from cryptography.hazmat.primitives import _serialization, hashes as hashes
from cryptography.hazmat.primitives.asymmetric import utils as asym_utils

class DSAParameters(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def generate_private_key(self) -> DSAPrivateKey:
        """
        Generates and returns a DSAPrivateKey.
        """
    @abc.abstractmethod
    def parameter_numbers(self) -> DSAParameterNumbers:
        """
        Returns a DSAParameterNumbers.
        """
DSAParametersWithNumbers = DSAParameters

class DSAPrivateKey(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def key_size(self) -> int:
        """
        The bit length of the prime modulus.
        """
    @abc.abstractmethod
    def public_key(self) -> DSAPublicKey:
        """
        The DSAPublicKey associated with this private key.
        """
    @abc.abstractmethod
    def parameters(self) -> DSAParameters:
        """
        The DSAParameters object associated with this private key.
        """
    @abc.abstractmethod
    def sign(self, data: bytes, algorithm: asym_utils.Prehashed | hashes.HashAlgorithm) -> bytes:
        """
        Signs the data
        """
    @abc.abstractmethod
    def private_numbers(self) -> DSAPrivateNumbers:
        """
        Returns a DSAPrivateNumbers.
        """
    @abc.abstractmethod
    def private_bytes(self, encoding: _serialization.Encoding, format: _serialization.PrivateFormat, encryption_algorithm: _serialization.KeySerializationEncryption) -> bytes:
        """
        Returns the key serialized as bytes.
        """
DSAPrivateKeyWithSerialization = DSAPrivateKey

class DSAPublicKey(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def key_size(self) -> int:
        """
        The bit length of the prime modulus.
        """
    @abc.abstractmethod
    def parameters(self) -> DSAParameters:
        """
        The DSAParameters object associated with this public key.
        """
    @abc.abstractmethod
    def public_numbers(self) -> DSAPublicNumbers:
        """
        Returns a DSAPublicNumbers.
        """
    @abc.abstractmethod
    def public_bytes(self, encoding: _serialization.Encoding, format: _serialization.PublicFormat) -> bytes:
        """
        Returns the key serialized as bytes.
        """
    @abc.abstractmethod
    def verify(self, signature: bytes, data: bytes, algorithm: asym_utils.Prehashed | hashes.HashAlgorithm) -> None:
        """
        Verifies the signature of the data.
        """
    @abc.abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Checks equality.
        """
DSAPublicKeyWithSerialization = DSAPublicKey

class DSAParameterNumbers:
    def __init__(self, p: int, q: int, g: int) -> None: ...
    @property
    def p(self) -> int: ...
    @property
    def q(self) -> int: ...
    @property
    def g(self) -> int: ...
    def parameters(self, backend: typing.Any = None) -> DSAParameters: ...
    def __eq__(self, other: object) -> bool: ...

class DSAPublicNumbers:
    def __init__(self, y: int, parameter_numbers: DSAParameterNumbers) -> None: ...
    @property
    def y(self) -> int: ...
    @property
    def parameter_numbers(self) -> DSAParameterNumbers: ...
    def public_key(self, backend: typing.Any = None) -> DSAPublicKey: ...
    def __eq__(self, other: object) -> bool: ...

class DSAPrivateNumbers:
    def __init__(self, x: int, public_numbers: DSAPublicNumbers) -> None: ...
    @property
    def x(self) -> int: ...
    @property
    def public_numbers(self) -> DSAPublicNumbers: ...
    def private_key(self, backend: typing.Any = None) -> DSAPrivateKey: ...
    def __eq__(self, other: object) -> bool: ...

def generate_parameters(key_size: int, backend: typing.Any = None) -> DSAParameters: ...
def generate_private_key(key_size: int, backend: typing.Any = None) -> DSAPrivateKey: ...
