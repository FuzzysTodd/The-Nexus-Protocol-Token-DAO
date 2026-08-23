import abc
from _typeshed import Incomplete
from cryptography.hazmat.primitives import hashes as hashes
from cryptography.hazmat.primitives._asymmetric import AsymmetricPadding as AsymmetricPadding
from cryptography.hazmat.primitives.asymmetric import rsa as rsa

class PKCS1v15(AsymmetricPadding):
    name: str

class _MaxLength:
    """Sentinel value for `MAX_LENGTH`."""
class _Auto:
    """Sentinel value for `AUTO`."""
class _DigestLength:
    """Sentinel value for `DIGEST_LENGTH`."""

class PSS(AsymmetricPadding):
    MAX_LENGTH: Incomplete
    AUTO: Incomplete
    DIGEST_LENGTH: Incomplete
    name: str
    def __init__(self, mgf: MGF, salt_length: int | _MaxLength | _Auto | _DigestLength) -> None: ...

class OAEP(AsymmetricPadding):
    name: str
    def __init__(self, mgf: MGF, algorithm: hashes.HashAlgorithm, label: bytes | None) -> None: ...

class MGF(metaclass=abc.ABCMeta): ...

class MGF1(MGF):
    MAX_LENGTH: Incomplete
    def __init__(self, algorithm: hashes.HashAlgorithm) -> None: ...

def calculate_max_pss_salt_length(key: rsa.RSAPrivateKey | rsa.RSAPublicKey, hash_algorithm: hashes.HashAlgorithm) -> int: ...
