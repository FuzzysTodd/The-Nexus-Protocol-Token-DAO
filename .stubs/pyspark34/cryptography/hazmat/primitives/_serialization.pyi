import abc
from _typeshed import Incomplete
from cryptography import utils as utils
from cryptography.hazmat.primitives.hashes import HashAlgorithm as HashAlgorithm

class PBES(utils.Enum):
    PBESv1SHA1And3KeyTripleDESCBC: str
    PBESv2SHA256AndAES256CBC: str

class Encoding(utils.Enum):
    PEM: str
    DER: str
    OpenSSH: str
    Raw: str
    X962: str
    SMIME: str

class PrivateFormat(utils.Enum):
    PKCS8: str
    TraditionalOpenSSL: str
    Raw: str
    OpenSSH: str
    PKCS12: str
    def encryption_builder(self) -> KeySerializationEncryptionBuilder: ...

class PublicFormat(utils.Enum):
    SubjectPublicKeyInfo: str
    PKCS1: str
    OpenSSH: str
    Raw: str
    CompressedPoint: str
    UncompressedPoint: str

class ParameterFormat(utils.Enum):
    PKCS3: str

class KeySerializationEncryption(metaclass=abc.ABCMeta): ...

class BestAvailableEncryption(KeySerializationEncryption):
    password: Incomplete
    def __init__(self, password: bytes) -> None: ...

class NoEncryption(KeySerializationEncryption): ...

class KeySerializationEncryptionBuilder:
    def __init__(self, format: PrivateFormat, *, _kdf_rounds: int | None = None, _hmac_hash: HashAlgorithm | None = None, _key_cert_algorithm: PBES | None = None) -> None: ...
    def kdf_rounds(self, rounds: int) -> KeySerializationEncryptionBuilder: ...
    def hmac_hash(self, algorithm: HashAlgorithm) -> KeySerializationEncryptionBuilder: ...
    def key_cert_algorithm(self, algorithm: PBES) -> KeySerializationEncryptionBuilder: ...
    def build(self, password: bytes) -> KeySerializationEncryption: ...

class _KeySerializationEncryption(KeySerializationEncryption):
    password: Incomplete
    def __init__(self, format: PrivateFormat, password: bytes, *, kdf_rounds: int | None, hmac_hash: HashAlgorithm | None, key_cert_algorithm: PBES | None) -> None: ...
