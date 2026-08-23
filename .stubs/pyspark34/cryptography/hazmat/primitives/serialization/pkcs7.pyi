import email.message
import typing
from _typeshed import Incomplete
from cryptography import utils as utils, x509 as x509
from cryptography.hazmat.primitives import hashes as hashes, serialization as serialization
from cryptography.hazmat.primitives.asymmetric import ec as ec, rsa as rsa

def load_pem_pkcs7_certificates(data: bytes) -> typing.List[x509.Certificate]: ...
def load_der_pkcs7_certificates(data: bytes) -> typing.List[x509.Certificate]: ...
def serialize_certificates(certs: typing.List[x509.Certificate], encoding: serialization.Encoding) -> bytes: ...

PKCS7HashTypes: Incomplete
PKCS7PrivateKeyTypes: Incomplete

class PKCS7Options(utils.Enum):
    Text: str
    Binary: str
    DetachedSignature: str
    NoCapabilities: str
    NoAttributes: str
    NoCerts: str

class PKCS7SignatureBuilder:
    def __init__(self, data: bytes | None = None, signers: typing.List[typing.Tuple[x509.Certificate, PKCS7PrivateKeyTypes, PKCS7HashTypes]] = [], additional_certs: typing.List[x509.Certificate] = []) -> None: ...
    def set_data(self, data: bytes) -> PKCS7SignatureBuilder: ...
    def add_signer(self, certificate: x509.Certificate, private_key: PKCS7PrivateKeyTypes, hash_algorithm: PKCS7HashTypes) -> PKCS7SignatureBuilder: ...
    def add_certificate(self, certificate: x509.Certificate) -> PKCS7SignatureBuilder: ...
    def sign(self, encoding: serialization.Encoding, options: typing.Iterable[PKCS7Options], backend: typing.Any = None) -> bytes: ...

class OpenSSLMimePart(email.message.MIMEPart): ...
