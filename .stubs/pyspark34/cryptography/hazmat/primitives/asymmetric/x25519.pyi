import abc
from cryptography.exceptions import UnsupportedAlgorithm as UnsupportedAlgorithm
from cryptography.hazmat.primitives import _serialization

class X25519PublicKey(metaclass=abc.ABCMeta):
    @classmethod
    def from_public_bytes(cls, data: bytes) -> X25519PublicKey: ...
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
    def __eq__(self, other: object) -> bool:
        """
        Checks equality.
        """

class X25519PrivateKey(metaclass=abc.ABCMeta):
    @classmethod
    def generate(cls) -> X25519PrivateKey: ...
    @classmethod
    def from_private_bytes(cls, data: bytes) -> X25519PrivateKey: ...
    @abc.abstractmethod
    def public_key(self) -> X25519PublicKey:
        """
        Returns the public key assosciated with this private key
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
    def exchange(self, peer_public_key: X25519PublicKey) -> bytes:
        """
        Performs a key exchange operation using the provided peer's public key.
        """
