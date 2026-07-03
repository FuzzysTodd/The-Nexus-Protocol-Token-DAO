import abc
import typing
from cryptography.hazmat.primitives import _serialization, hashes as hashes
from cryptography.hazmat.primitives._asymmetric import AsymmetricPadding as AsymmetricPadding
from cryptography.hazmat.primitives.asymmetric import utils as asym_utils

class RSAPrivateKey(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def decrypt(self, ciphertext: bytes, padding: AsymmetricPadding) -> bytes:
        """
        Decrypts the provided ciphertext.
        """
    @property
    @abc.abstractmethod
    def key_size(self) -> int:
        """
        The bit length of the public modulus.
        """
    @abc.abstractmethod
    def public_key(self) -> RSAPublicKey:
        """
        The RSAPublicKey associated with this private key.
        """
    @abc.abstractmethod
    def sign(self, data: bytes, padding: AsymmetricPadding, algorithm: asym_utils.Prehashed | hashes.HashAlgorithm) -> bytes:
        """
        Signs the data.
        """
    @abc.abstractmethod
    def private_numbers(self) -> RSAPrivateNumbers:
        """
        Returns an RSAPrivateNumbers.
        """
    @abc.abstractmethod
    def private_bytes(self, encoding: _serialization.Encoding, format: _serialization.PrivateFormat, encryption_algorithm: _serialization.KeySerializationEncryption) -> bytes:
        """
        Returns the key serialized as bytes.
        """
RSAPrivateKeyWithSerialization = RSAPrivateKey

class RSAPublicKey(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def encrypt(self, plaintext: bytes, padding: AsymmetricPadding) -> bytes:
        """
        Encrypts the given plaintext.
        """
    @property
    @abc.abstractmethod
    def key_size(self) -> int:
        """
        The bit length of the public modulus.
        """
    @abc.abstractmethod
    def public_numbers(self) -> RSAPublicNumbers:
        """
        Returns an RSAPublicNumbers
        """
    @abc.abstractmethod
    def public_bytes(self, encoding: _serialization.Encoding, format: _serialization.PublicFormat) -> bytes:
        """
        Returns the key serialized as bytes.
        """
    @abc.abstractmethod
    def verify(self, signature: bytes, data: bytes, padding: AsymmetricPadding, algorithm: asym_utils.Prehashed | hashes.HashAlgorithm) -> None:
        """
        Verifies the signature of the data.
        """
    @abc.abstractmethod
    def recover_data_from_signature(self, signature: bytes, padding: AsymmetricPadding, algorithm: hashes.HashAlgorithm | None) -> bytes:
        """
        Recovers the original data from the signature.
        """
    @abc.abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Checks equality.
        """
RSAPublicKeyWithSerialization = RSAPublicKey

def generate_private_key(public_exponent: int, key_size: int, backend: typing.Any = None) -> RSAPrivateKey: ...
def rsa_crt_iqmp(p: int, q: int) -> int:
    """
    Compute the CRT (q ** -1) % p value from RSA primes p and q.
    """
def rsa_crt_dmp1(private_exponent: int, p: int) -> int:
    """
    Compute the CRT private_exponent % (p - 1) value from the RSA
    private_exponent (d) and p.
    """
def rsa_crt_dmq1(private_exponent: int, q: int) -> int:
    """
    Compute the CRT private_exponent % (q - 1) value from the RSA
    private_exponent (d) and q.
    """
def rsa_recover_prime_factors(n: int, e: int, d: int) -> typing.Tuple[int, int]:
    """
    Compute factors p and q from the private exponent d. We assume that n has
    no more than two factors. This function is adapted from code in PyCrypto.
    """

class RSAPrivateNumbers:
    def __init__(self, p: int, q: int, d: int, dmp1: int, dmq1: int, iqmp: int, public_numbers: RSAPublicNumbers) -> None: ...
    @property
    def p(self) -> int: ...
    @property
    def q(self) -> int: ...
    @property
    def d(self) -> int: ...
    @property
    def dmp1(self) -> int: ...
    @property
    def dmq1(self) -> int: ...
    @property
    def iqmp(self) -> int: ...
    @property
    def public_numbers(self) -> RSAPublicNumbers: ...
    def private_key(self, backend: typing.Any = None, *, unsafe_skip_rsa_key_validation: bool = False) -> RSAPrivateKey: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class RSAPublicNumbers:
    def __init__(self, e: int, n: int) -> None: ...
    @property
    def e(self) -> int: ...
    @property
    def n(self) -> int: ...
    def public_key(self, backend: typing.Any = None) -> RSAPublicKey: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
