import abc
import datetime
import typing
from _typeshed import Incomplete
from cryptography import utils as utils
from cryptography.hazmat.primitives import hashes as hashes, serialization as serialization
from cryptography.hazmat.primitives.asymmetric import dsa as dsa, ec as ec, ed25519 as ed25519, ed448 as ed448, padding as padding, rsa as rsa, x25519 as x25519, x448 as x448
from cryptography.hazmat.primitives.asymmetric.types import CertificateIssuerPrivateKeyTypes as CertificateIssuerPrivateKeyTypes, CertificateIssuerPublicKeyTypes as CertificateIssuerPublicKeyTypes, CertificatePublicKeyTypes as CertificatePublicKeyTypes
from cryptography.x509.extensions import Extension as Extension, ExtensionType as ExtensionType, Extensions as Extensions
from cryptography.x509.name import Name as Name, _ASN1Type
from cryptography.x509.oid import ObjectIdentifier as ObjectIdentifier

class AttributeNotFound(Exception):
    oid: Incomplete
    def __init__(self, msg: str, oid: ObjectIdentifier) -> None: ...

class Attribute:
    def __init__(self, oid: ObjectIdentifier, value: bytes, _type: int = ...) -> None: ...
    @property
    def oid(self) -> ObjectIdentifier: ...
    @property
    def value(self) -> bytes: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class Attributes:
    def __init__(self, attributes: typing.Iterable[Attribute]) -> None: ...
    __len__: Incomplete
    __iter__: Incomplete
    __getitem__: Incomplete
    def get_attribute_for_oid(self, oid: ObjectIdentifier) -> Attribute: ...

class Version(utils.Enum):
    v1: int
    v3: int

class InvalidVersion(Exception):
    parsed_version: Incomplete
    def __init__(self, msg: str, parsed_version: int) -> None: ...

class Certificate(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fingerprint(self, algorithm: hashes.HashAlgorithm) -> bytes:
        """
        Returns bytes using digest passed.
        """
    @property
    @abc.abstractmethod
    def serial_number(self) -> int:
        """
        Returns certificate serial number
        """
    @property
    @abc.abstractmethod
    def version(self) -> Version:
        """
        Returns the certificate version
        """
    @abc.abstractmethod
    def public_key(self) -> CertificatePublicKeyTypes:
        """
        Returns the public key
        """
    @property
    @abc.abstractmethod
    def not_valid_before(self) -> datetime.datetime:
        """
        Not before time (represented as UTC datetime)
        """
    @property
    @abc.abstractmethod
    def not_valid_after(self) -> datetime.datetime:
        """
        Not after time (represented as UTC datetime)
        """
    @property
    @abc.abstractmethod
    def issuer(self) -> Name:
        """
        Returns the issuer name object.
        """
    @property
    @abc.abstractmethod
    def subject(self) -> Name:
        """
        Returns the subject name object.
        """
    @property
    @abc.abstractmethod
    def signature_hash_algorithm(self) -> hashes.HashAlgorithm | None:
        """
        Returns a HashAlgorithm corresponding to the type of the digest signed
        in the certificate.
        """
    @property
    @abc.abstractmethod
    def signature_algorithm_oid(self) -> ObjectIdentifier:
        """
        Returns the ObjectIdentifier of the signature algorithm.
        """
    @property
    @abc.abstractmethod
    def signature_algorithm_parameters(self) -> None | padding.PSS | padding.PKCS1v15 | ec.ECDSA:
        """
        Returns the signature algorithm parameters.
        """
    @property
    @abc.abstractmethod
    def extensions(self) -> Extensions:
        """
        Returns an Extensions object.
        """
    @property
    @abc.abstractmethod
    def signature(self) -> bytes:
        """
        Returns the signature bytes.
        """
    @property
    @abc.abstractmethod
    def tbs_certificate_bytes(self) -> bytes:
        """
        Returns the tbsCertificate payload bytes as defined in RFC 5280.
        """
    @property
    @abc.abstractmethod
    def tbs_precertificate_bytes(self) -> bytes:
        """
        Returns the tbsCertificate payload bytes with the SCT list extension
        stripped.
        """
    @abc.abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Checks equality.
        """
    @abc.abstractmethod
    def __hash__(self) -> int:
        """
        Computes a hash.
        """
    @abc.abstractmethod
    def public_bytes(self, encoding: serialization.Encoding) -> bytes:
        """
        Serializes the certificate to PEM or DER format.
        """
    @abc.abstractmethod
    def verify_directly_issued_by(self, issuer: Certificate) -> None:
        """
        This method verifies that certificate issuer name matches the
        issuer subject name and that the certificate is signed by the
        issuer's private key. No other validation is performed.
        """

class RevokedCertificate(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def serial_number(self) -> int:
        """
        Returns the serial number of the revoked certificate.
        """
    @property
    @abc.abstractmethod
    def revocation_date(self) -> datetime.datetime:
        """
        Returns the date of when this certificate was revoked.
        """
    @property
    @abc.abstractmethod
    def extensions(self) -> Extensions:
        """
        Returns an Extensions object containing a list of Revoked extensions.
        """

class _RawRevokedCertificate(RevokedCertificate):
    def __init__(self, serial_number: int, revocation_date: datetime.datetime, extensions: Extensions) -> None: ...
    @property
    def serial_number(self) -> int: ...
    @property
    def revocation_date(self) -> datetime.datetime: ...
    @property
    def extensions(self) -> Extensions: ...

class CertificateRevocationList(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def public_bytes(self, encoding: serialization.Encoding) -> bytes:
        """
        Serializes the CRL to PEM or DER format.
        """
    @abc.abstractmethod
    def fingerprint(self, algorithm: hashes.HashAlgorithm) -> bytes:
        """
        Returns bytes using digest passed.
        """
    @abc.abstractmethod
    def get_revoked_certificate_by_serial_number(self, serial_number: int) -> RevokedCertificate | None:
        """
        Returns an instance of RevokedCertificate or None if the serial_number
        is not in the CRL.
        """
    @property
    @abc.abstractmethod
    def signature_hash_algorithm(self) -> hashes.HashAlgorithm | None:
        """
        Returns a HashAlgorithm corresponding to the type of the digest signed
        in the certificate.
        """
    @property
    @abc.abstractmethod
    def signature_algorithm_oid(self) -> ObjectIdentifier:
        """
        Returns the ObjectIdentifier of the signature algorithm.
        """
    @property
    @abc.abstractmethod
    def issuer(self) -> Name:
        """
        Returns the X509Name with the issuer of this CRL.
        """
    @property
    @abc.abstractmethod
    def next_update(self) -> datetime.datetime | None:
        """
        Returns the date of next update for this CRL.
        """
    @property
    @abc.abstractmethod
    def last_update(self) -> datetime.datetime:
        """
        Returns the date of last update for this CRL.
        """
    @property
    @abc.abstractmethod
    def extensions(self) -> Extensions:
        """
        Returns an Extensions object containing a list of CRL extensions.
        """
    @property
    @abc.abstractmethod
    def signature(self) -> bytes:
        """
        Returns the signature bytes.
        """
    @property
    @abc.abstractmethod
    def tbs_certlist_bytes(self) -> bytes:
        """
        Returns the tbsCertList payload bytes as defined in RFC 5280.
        """
    @abc.abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Checks equality.
        """
    @abc.abstractmethod
    def __len__(self) -> int:
        """
        Number of revoked certificates in the CRL.
        """
    @typing.overload
    def __getitem__(self, idx: int) -> RevokedCertificate: ...
    @typing.overload
    def __getitem__(self, idx: slice) -> typing.List[RevokedCertificate]: ...
    @abc.abstractmethod
    def __iter__(self) -> typing.Iterator[RevokedCertificate]:
        """
        Iterator over the revoked certificates
        """
    @abc.abstractmethod
    def is_signature_valid(self, public_key: CertificateIssuerPublicKeyTypes) -> bool:
        """
        Verifies signature of revocation list against given public key.
        """

class CertificateSigningRequest(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Checks equality.
        """
    @abc.abstractmethod
    def __hash__(self) -> int:
        """
        Computes a hash.
        """
    @abc.abstractmethod
    def public_key(self) -> CertificatePublicKeyTypes:
        """
        Returns the public key
        """
    @property
    @abc.abstractmethod
    def subject(self) -> Name:
        """
        Returns the subject name object.
        """
    @property
    @abc.abstractmethod
    def signature_hash_algorithm(self) -> hashes.HashAlgorithm | None:
        """
        Returns a HashAlgorithm corresponding to the type of the digest signed
        in the certificate.
        """
    @property
    @abc.abstractmethod
    def signature_algorithm_oid(self) -> ObjectIdentifier:
        """
        Returns the ObjectIdentifier of the signature algorithm.
        """
    @property
    @abc.abstractmethod
    def extensions(self) -> Extensions:
        """
        Returns the extensions in the signing request.
        """
    @property
    @abc.abstractmethod
    def attributes(self) -> Attributes:
        """
        Returns an Attributes object.
        """
    @abc.abstractmethod
    def public_bytes(self, encoding: serialization.Encoding) -> bytes:
        """
        Encodes the request to PEM or DER format.
        """
    @property
    @abc.abstractmethod
    def signature(self) -> bytes:
        """
        Returns the signature bytes.
        """
    @property
    @abc.abstractmethod
    def tbs_certrequest_bytes(self) -> bytes:
        """
        Returns the PKCS#10 CertificationRequestInfo bytes as defined in RFC
        2986.
        """
    @property
    @abc.abstractmethod
    def is_signature_valid(self) -> bool:
        """
        Verifies signature of signing request.
        """
    @abc.abstractmethod
    def get_attribute_for_oid(self, oid: ObjectIdentifier) -> bytes:
        """
        Get the attribute value for a given OID.
        """

def load_pem_x509_certificate(data: bytes, backend: typing.Any = None) -> Certificate: ...
def load_pem_x509_certificates(data: bytes) -> typing.List[Certificate]: ...
def load_der_x509_certificate(data: bytes, backend: typing.Any = None) -> Certificate: ...
def load_pem_x509_csr(data: bytes, backend: typing.Any = None) -> CertificateSigningRequest: ...
def load_der_x509_csr(data: bytes, backend: typing.Any = None) -> CertificateSigningRequest: ...
def load_pem_x509_crl(data: bytes, backend: typing.Any = None) -> CertificateRevocationList: ...
def load_der_x509_crl(data: bytes, backend: typing.Any = None) -> CertificateRevocationList: ...

class CertificateSigningRequestBuilder:
    def __init__(self, subject_name: Name | None = None, extensions: typing.List[Extension[ExtensionType]] = [], attributes: typing.List[typing.Tuple[ObjectIdentifier, bytes, int | None]] = []) -> None:
        """
        Creates an empty X.509 certificate request (v1).
        """
    def subject_name(self, name: Name) -> CertificateSigningRequestBuilder:
        """
        Sets the certificate requestor's distinguished name.
        """
    def add_extension(self, extval: ExtensionType, critical: bool) -> CertificateSigningRequestBuilder:
        """
        Adds an X.509 extension to the certificate request.
        """
    def add_attribute(self, oid: ObjectIdentifier, value: bytes, *, _tag: _ASN1Type | None = None) -> CertificateSigningRequestBuilder:
        """
        Adds an X.509 attribute with an OID and associated value.
        """
    def sign(self, private_key: CertificateIssuerPrivateKeyTypes, algorithm: _AllowedHashTypes | None, backend: typing.Any = None) -> CertificateSigningRequest:
        """
        Signs the request using the requestor's private key.
        """

class CertificateBuilder:
    def __init__(self, issuer_name: Name | None = None, subject_name: Name | None = None, public_key: CertificatePublicKeyTypes | None = None, serial_number: int | None = None, not_valid_before: datetime.datetime | None = None, not_valid_after: datetime.datetime | None = None, extensions: typing.List[Extension[ExtensionType]] = []) -> None: ...
    def issuer_name(self, name: Name) -> CertificateBuilder:
        """
        Sets the CA's distinguished name.
        """
    def subject_name(self, name: Name) -> CertificateBuilder:
        """
        Sets the requestor's distinguished name.
        """
    def public_key(self, key: CertificatePublicKeyTypes) -> CertificateBuilder:
        """
        Sets the requestor's public key (as found in the signing request).
        """
    def serial_number(self, number: int) -> CertificateBuilder:
        """
        Sets the certificate serial number.
        """
    def not_valid_before(self, time: datetime.datetime) -> CertificateBuilder:
        """
        Sets the certificate activation time.
        """
    def not_valid_after(self, time: datetime.datetime) -> CertificateBuilder:
        """
        Sets the certificate expiration time.
        """
    def add_extension(self, extval: ExtensionType, critical: bool) -> CertificateBuilder:
        """
        Adds an X.509 extension to the certificate.
        """
    def sign(self, private_key: CertificateIssuerPrivateKeyTypes, algorithm: _AllowedHashTypes | None, backend: typing.Any = None, *, rsa_padding: padding.PSS | padding.PKCS1v15 | None = None) -> Certificate:
        """
        Signs the certificate using the CA's private key.
        """

class CertificateRevocationListBuilder:
    def __init__(self, issuer_name: Name | None = None, last_update: datetime.datetime | None = None, next_update: datetime.datetime | None = None, extensions: typing.List[Extension[ExtensionType]] = [], revoked_certificates: typing.List[RevokedCertificate] = []) -> None: ...
    def issuer_name(self, issuer_name: Name) -> CertificateRevocationListBuilder: ...
    def last_update(self, last_update: datetime.datetime) -> CertificateRevocationListBuilder: ...
    def next_update(self, next_update: datetime.datetime) -> CertificateRevocationListBuilder: ...
    def add_extension(self, extval: ExtensionType, critical: bool) -> CertificateRevocationListBuilder:
        """
        Adds an X.509 extension to the certificate revocation list.
        """
    def add_revoked_certificate(self, revoked_certificate: RevokedCertificate) -> CertificateRevocationListBuilder:
        """
        Adds a revoked certificate to the CRL.
        """
    def sign(self, private_key: CertificateIssuerPrivateKeyTypes, algorithm: _AllowedHashTypes | None, backend: typing.Any = None) -> CertificateRevocationList: ...

class RevokedCertificateBuilder:
    def __init__(self, serial_number: int | None = None, revocation_date: datetime.datetime | None = None, extensions: typing.List[Extension[ExtensionType]] = []) -> None: ...
    def serial_number(self, number: int) -> RevokedCertificateBuilder: ...
    def revocation_date(self, time: datetime.datetime) -> RevokedCertificateBuilder: ...
    def add_extension(self, extval: ExtensionType, critical: bool) -> RevokedCertificateBuilder: ...
    def build(self, backend: typing.Any = None) -> RevokedCertificate: ...

def random_serial_number() -> int: ...
