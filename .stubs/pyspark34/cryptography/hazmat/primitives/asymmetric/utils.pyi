from _typeshed import Incomplete
from cryptography.hazmat.bindings._rust import asn1 as asn1
from cryptography.hazmat.primitives import hashes as hashes

decode_dss_signature: Incomplete
encode_dss_signature: Incomplete

class Prehashed:
    def __init__(self, algorithm: hashes.HashAlgorithm) -> None: ...
    @property
    def digest_size(self) -> int: ...
