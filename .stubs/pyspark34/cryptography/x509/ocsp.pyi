import abc
import datetime
import typing
from cryptography import utils as utils, x509 as x509
from cryptography.hazmat.bindings._rust import ocsp as ocsp
from cryptography.hazmat.primitives import hashes as hashes, serialization as serialization
from cryptography.hazmat.primitives.asymmetric.types import CertificateIssuerPrivateKeyTypes as CertificateIssuerPrivateKeyTypes

class OCSPResponderEncoding(utils.Enum):
    HASH: str
    NAME: str

class OCSPResponseStatus(utils.Enum):
    SUCCESSFUL: int
    MALFORMED_REQUEST: int
    INTERNAL_ERROR: int
    TRY_LATER: int
    SIG_REQUIRED: int
    UNAUTHORIZED: int

class OCSPCertStatus(utils.Enum):
    GOOD: int
    REVOKED: int
    UNKNOWN: int

class _SingleResponse:
    def __init__(self, cert: x509.Certificate, issuer: x509.Certificate, algorithm: hashes.HashAlgorithm, cert_status: OCSPCertStatus, this_update: datetime.datetime, next_update: datetime.datetime | None, revocation_time: datetime.datetime | None, revocation_reason: x509.ReasonFlags | None) -> None: ...

class OCSPRequest(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def issuer_key_hash(self) -> bytes:
        """
        The hash of the issuer public key
        """
    @property
    @abc.abstractmethod
    def issuer_name_hash(self) -> bytes:
        """
        The hash of the issuer name
        """
    @property
    @abc.abstractmethod
    def hash_algorithm(self) -> hashes.HashAlgorithm:
        """
        The hash algorithm used in the issuer name and key hashes
        """
    @property
    @abc.abstractmethod
    def serial_number(self) -> int:
        """
        The serial number of the cert whose status is being checked
        """
    @abc.abstractmethod
    def public_bytes(self, encoding: serialization.Encoding) -> bytes:
        """
        Serializes the request to DER
        """
    @property
    @abc.abstractmethod
    def extensions(self) -> x509.Extensions:
        """
        The list of request extensions. Not single request extensions.
        """

class OCSPSingleResponse(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def certificate_status(self) -> OCSPCertStatus:
        """
        The status of the certificate (an element from the OCSPCertStatus enum)
        """
    @property
    @abc.abstractmethod
    def revocation_time(self) -> datetime.datetime | None:
        """
        The date of when the certificate was revoked or None if not
        revoked.
        """
    @property
    @abc.abstractmethod
    def revocation_reason(self) -> x509.ReasonFlags | None:
        """
        The reason the certificate was revoked or None if not specified or
        not revoked.
        """
    @property
    @abc.abstractmethod
    def this_update(self) -> datetime.datetime:
        """
        The most recent time at which the status being indicated is known by
        the responder to have been correct
        """
    @property
    @abc.abstractmethod
    def next_update(self) -> datetime.datetime | None:
        """
        The time when newer information will be available
        """
    @property
    @abc.abstractmethod
    def issuer_key_hash(self) -> bytes:
        """
        The hash of the issuer public key
        """
    @property
    @abc.abstractmethod
    def issuer_name_hash(self) -> bytes:
        """
        The hash of the issuer name
        """
    @property
    @abc.abstractmethod
    def hash_algorithm(self) -> hashes.HashAlgorithm:
        """
        The hash algorithm used in the issuer name and key hashes
        """
    @property
    @abc.abstractmethod
    def serial_number(self) -> int:
        """
        The serial number of the cert whose status is being checked
        """

class OCSPResponse(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def responses(self) -> typing.Iterator[OCSPSingleResponse]:
        """
        An iterator over the individual SINGLERESP structures in the
        response
        """
    @property
    @abc.abstractmethod
    def response_status(self) -> OCSPResponseStatus:
        """
        The status of the response. This is a value from the OCSPResponseStatus
        enumeration
        """
    @property
    @abc.abstractmethod
    def signature_algorithm_oid(self) -> x509.ObjectIdentifier:
        """
        The ObjectIdentifier of the signature algorithm
        """
    @property
    @abc.abstractmethod
    def signature_hash_algorithm(self) -> hashes.HashAlgorithm | None:
        """
        Returns a HashAlgorithm corresponding to the type of the digest signed
        """
    @property
    @abc.abstractmethod
    def signature(self) -> bytes:
        """
        The signature bytes
        """
    @property
    @abc.abstractmethod
    def tbs_response_bytes(self) -> bytes:
        """
        The tbsResponseData bytes
        """
    @property
    @abc.abstractmethod
    def certificates(self) -> typing.List[x509.Certificate]:
        """
        A list of certificates used to help build a chain to verify the OCSP
        response. This situation occurs when the OCSP responder uses a delegate
        certificate.
        """
    @property
    @abc.abstractmethod
    def responder_key_hash(self) -> bytes | None:
        """
        The responder's key hash or None
        """
    @property
    @abc.abstractmethod
    def responder_name(self) -> x509.Name | None:
        """
        The responder's Name or None
        """
    @property
    @abc.abstractmethod
    def produced_at(self) -> datetime.datetime:
        """
        The time the response was produced
        """
    @property
    @abc.abstractmethod
    def certificate_status(self) -> OCSPCertStatus:
        """
        The status of the certificate (an element from the OCSPCertStatus enum)
        """
    @property
    @abc.abstractmethod
    def revocation_time(self) -> datetime.datetime | None:
        """
        The date of when the certificate was revoked or None if not
        revoked.
        """
    @property
    @abc.abstractmethod
    def revocation_reason(self) -> x509.ReasonFlags | None:
        """
        The reason the certificate was revoked or None if not specified or
        not revoked.
        """
    @property
    @abc.abstractmethod
    def this_update(self) -> datetime.datetime:
        """
        The most recent time at which the status being indicated is known by
        the responder to have been correct
        """
    @property
    @abc.abstractmethod
    def next_update(self) -> datetime.datetime | None:
        """
        The time when newer information will be available
        """
    @property
    @abc.abstractmethod
    def issuer_key_hash(self) -> bytes:
        """
        The hash of the issuer public key
        """
    @property
    @abc.abstractmethod
    def issuer_name_hash(self) -> bytes:
        """
        The hash of the issuer name
        """
    @property
    @abc.abstractmethod
    def hash_algorithm(self) -> hashes.HashAlgorithm:
        """
        The hash algorithm used in the issuer name and key hashes
        """
    @property
    @abc.abstractmethod
    def serial_number(self) -> int:
        """
        The serial number of the cert whose status is being checked
        """
    @property
    @abc.abstractmethod
    def extensions(self) -> x509.Extensions:
        """
        The list of response extensions. Not single response extensions.
        """
    @property
    @abc.abstractmethod
    def single_extensions(self) -> x509.Extensions:
        """
        The list of single response extensions. Not response extensions.
        """
    @abc.abstractmethod
    def public_bytes(self, encoding: serialization.Encoding) -> bytes:
        """
        Serializes the response to DER
        """

class OCSPRequestBuilder:
    def __init__(self, request: typing.Tuple[x509.Certificate, x509.Certificate, hashes.HashAlgorithm] | None = None, request_hash: typing.Tuple[bytes, bytes, int, hashes.HashAlgorithm] | None = None, extensions: typing.List[x509.Extension[x509.ExtensionType]] = []) -> None: ...
    def add_certificate(self, cert: x509.Certificate, issuer: x509.Certificate, algorithm: hashes.HashAlgorithm) -> OCSPRequestBuilder: ...
    def add_certificate_by_hash(self, issuer_name_hash: bytes, issuer_key_hash: bytes, serial_number: int, algorithm: hashes.HashAlgorithm) -> OCSPRequestBuilder: ...
    def add_extension(self, extval: x509.ExtensionType, critical: bool) -> OCSPRequestBuilder: ...
    def build(self) -> OCSPRequest: ...

class OCSPResponseBuilder:
    def __init__(self, response: _SingleResponse | None = None, responder_id: typing.Tuple[x509.Certificate, OCSPResponderEncoding] | None = None, certs: typing.List[x509.Certificate] | None = None, extensions: typing.List[x509.Extension[x509.ExtensionType]] = []) -> None: ...
    def add_response(self, cert: x509.Certificate, issuer: x509.Certificate, algorithm: hashes.HashAlgorithm, cert_status: OCSPCertStatus, this_update: datetime.datetime, next_update: datetime.datetime | None, revocation_time: datetime.datetime | None, revocation_reason: x509.ReasonFlags | None) -> OCSPResponseBuilder: ...
    def responder_id(self, encoding: OCSPResponderEncoding, responder_cert: x509.Certificate) -> OCSPResponseBuilder: ...
    def certificates(self, certs: typing.Iterable[x509.Certificate]) -> OCSPResponseBuilder: ...
    def add_extension(self, extval: x509.ExtensionType, critical: bool) -> OCSPResponseBuilder: ...
    def sign(self, private_key: CertificateIssuerPrivateKeyTypes, algorithm: hashes.HashAlgorithm | None) -> OCSPResponse: ...
    @classmethod
    def build_unsuccessful(cls, response_status: OCSPResponseStatus) -> OCSPResponse: ...

def load_der_ocsp_request(data: bytes) -> OCSPRequest: ...
def load_der_ocsp_response(data: bytes) -> OCSPResponse: ...
