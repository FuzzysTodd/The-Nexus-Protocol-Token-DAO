import abc
import typing
from cryptography.hazmat.primitives import _serialization

def generate_parameters(generator: int, key_size: int, backend: typing.Any = None) -> DHParameters: ...

class DHParameterNumbers:
    def __init__(self, p: int, g: int, q: int | None = None) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def parameters(self, backend: typing.Any = None) -> DHParameters: ...
    @property
    def p(self) -> int: ...
    @property
    def g(self) -> int: ...
    @property
    def q(self) -> int | None: ...

class DHPublicNumbers:
    def __init__(self, y: int, parameter_numbers: DHParameterNumbers) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def public_key(self, backend: typing.Any = None) -> DHPublicKey: ...
    @property
    def y(self) -> int: ...
    @property
    def parameter_numbers(self) -> DHParameterNumbers: ...

class DHPrivateNumbers:
    def __init__(self, x: int, public_numbers: DHPublicNumbers) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def private_key(self, backend: typing.Any = None) -> DHPrivateKey: ...
    @property
    def public_numbers(self) -> DHPublicNumbers: ...
    @property
    def x(self) -> int: ...

class DHParameters(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def generate_private_key(self) -> DHPrivateKey:
        """
        Generates and returns a DHPrivateKey.
        """
    @abc.abstractmethod
    def parameter_bytes(self, encoding: _serialization.Encoding, format: _serialization.ParameterFormat) -> bytes:
        """
        Returns the parameters serialized as bytes.
        """
    @abc.abstractmethod
    def parameter_numbers(self) -> DHParameterNumbers:
        """
        Returns a DHParameterNumbers.
        """
DHParametersWithSerialization = DHParameters

class DHPublicKey(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def key_size(self) -> int:
        """
        The bit length of the prime modulus.
        """
    @abc.abstractmethod
    def parameters(self) -> DHParameters:
        """
        The DHParameters object associated with this public key.
        """
    @abc.abstractmethod
    def public_numbers(self) -> DHPublicNumbers:
        """
        Returns a DHPublicNumbers.
        """
    @abc.abstractmethod
    def public_bytes(self, encoding: _serialization.Encoding, format: _serialization.PublicFormat) -> bytes:
        """
        Returns the key serialized as bytes.
        """
    @abc.abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Checks equality.
        """
DHPublicKeyWithSerialization = DHPublicKey

class DHPrivateKey(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def key_size(self) -> int:
        """
        The bit length of the prime modulus.
        """
    @abc.abstractmethod
    def public_key(self) -> DHPublicKey:
        """
        The DHPublicKey associated with this private key.
        """
    @abc.abstractmethod
    def parameters(self) -> DHParameters:
        """
        The DHParameters object associated with this private key.
        """
    @abc.abstractmethod
    def exchange(self, peer_public_key: DHPublicKey) -> bytes:
        """
        Given peer's DHPublicKey, carry out the key exchange and
        return shared key as bytes.
        """
    @abc.abstractmethod
    def private_numbers(self) -> DHPrivateNumbers:
        """
        Returns a DHPrivateNumbers.
        """
    @abc.abstractmethod
    def private_bytes(self, encoding: _serialization.Encoding, format: _serialization.PrivateFormat, encryption_algorithm: _serialization.KeySerializationEncryption) -> bytes:
        """
        Returns the key serialized as bytes.
        """
DHPrivateKeyWithSerialization = DHPrivateKey
