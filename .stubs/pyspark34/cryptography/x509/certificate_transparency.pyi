import abc
import datetime
from cryptography import utils as utils
from cryptography.hazmat.primitives.hashes import HashAlgorithm as HashAlgorithm

class LogEntryType(utils.Enum):
    X509_CERTIFICATE: int
    PRE_CERTIFICATE: int

class Version(utils.Enum):
    v1: int

class SignatureAlgorithm(utils.Enum):
    """
    Signature algorithms that are valid for SCTs.

    These are exactly the same as SignatureAlgorithm in RFC 5246 (TLS 1.2).

    See: <https://datatracker.ietf.org/doc/html/rfc5246#section-7.4.1.4.1>
    """
    ANONYMOUS: int
    RSA: int
    DSA: int
    ECDSA: int

class SignedCertificateTimestamp(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def version(self) -> Version:
        """
        Returns the SCT version.
        """
    @property
    @abc.abstractmethod
    def log_id(self) -> bytes:
        """
        Returns an identifier indicating which log this SCT is for.
        """
    @property
    @abc.abstractmethod
    def timestamp(self) -> datetime.datetime:
        """
        Returns the timestamp for this SCT.
        """
    @property
    @abc.abstractmethod
    def entry_type(self) -> LogEntryType:
        """
        Returns whether this is an SCT for a certificate or pre-certificate.
        """
    @property
    @abc.abstractmethod
    def signature_hash_algorithm(self) -> HashAlgorithm:
        """
        Returns the hash algorithm used for the SCT's signature.
        """
    @property
    @abc.abstractmethod
    def signature_algorithm(self) -> SignatureAlgorithm:
        """
        Returns the signing algorithm used for the SCT's signature.
        """
    @property
    @abc.abstractmethod
    def signature(self) -> bytes:
        """
        Returns the signature for this SCT.
        """
    @property
    @abc.abstractmethod
    def extension_bytes(self) -> bytes:
        """
        Returns the raw bytes of any extensions for this SCT.
        """
