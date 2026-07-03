import abc
from cryptography.exceptions import UnsupportedAlgorithm as UnsupportedAlgorithm
from cryptography.hazmat.primitives import _serialization

class Ed25519PublicKey(metaclass=abc.ABCMeta):
    @classmethod
    def from_public_bytes(cls, data: bytes) -> Ed25519PublicKey: ...
    @abc.abstractmethod
    def public_bytes(self, encoding: _serialization.Encoding, format: _serialization.PublicFormat) -> bytes:
        """
        The serialized bytes of the public key.
        """
    @abc.abstractmethod
    def public_bytes_raw(self) -> bytes:
        """
        The raw bytes of the public key.
        Equivalent to public_bytes(Raw, Raw).
        """
    @abc.abstractmethod
    def verify(self, signature: bytes, data: bytes) -> None:
        """
        Verify the signature.
        """
    @abc.abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Checks equality.
        """

class Ed25519PrivateKey(metaclass=abc.ABCMeta):
    @classmethod
    def generate(cls) -> Ed25519PrivateKey: ...
    @classmethod
    def from_private_bytes(cls, data: bytes) -> Ed25519PrivateKey: ...
    @abc.abstractmethod
    def public_key(self) -> Ed25519PublicKey:
        """
        The Ed25519PublicKey derived from the private key.
        """
    @abc.abstractmethod
    def private_bytes(self, encoding: _serialization.Encoding, format: _serialization.PrivateFormat, encryption_algorithm: _serialization.KeySerializationEncryption) -> bytes:
        """
        The serialized bytes of the private key.
        """
    @abc.abstractmethod
    def private_bytes_raw(self) -> bytes:
        """
        The raw bytes of the private key.
        Equivalent to private_bytes(Raw, Raw, NoEncryption()).
        """
    @abc.abstractmethod
    def sign(self, data: bytes) -> bytes:
        """
        Signs the data.
        """
