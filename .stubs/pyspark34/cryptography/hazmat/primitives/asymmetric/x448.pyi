import abc
from cryptography.exceptions import UnsupportedAlgorithm as UnsupportedAlgorithm
from cryptography.hazmat.primitives import _serialization

class X448PublicKey(metaclass=abc.ABCMeta):
    @classmethod
    def from_public_bytes(cls, data: bytes) -> X448PublicKey: ...
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

class X448PrivateKey(metaclass=abc.ABCMeta):
    @classmethod
    def generate(cls) -> X448PrivateKey: ...
    @classmethod
    def from_private_bytes(cls, data: bytes) -> X448PrivateKey: ...
    @abc.abstractmethod
    def public_key(self) -> X448PublicKey:
        """
        Returns the public key associated with this private key
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
    def exchange(self, peer_public_key: X448PublicKey) -> bytes:
        """
        Performs a key exchange operation using the provided peer's public key.
        """
