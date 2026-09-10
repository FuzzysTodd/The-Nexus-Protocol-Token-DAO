import typing
from cryptography import utils as utils
from cryptography.exceptions import AlreadyFinalized as AlreadyFinalized, InvalidKey as InvalidKey
from cryptography.hazmat.primitives import constant_time as constant_time, hashes as hashes
from cryptography.hazmat.primitives.kdf import KeyDerivationFunction as KeyDerivationFunction

class X963KDF(KeyDerivationFunction):
    def __init__(self, algorithm: hashes.HashAlgorithm, length: int, sharedinfo: bytes | None, backend: typing.Any = None) -> None: ...
    def derive(self, key_material: bytes) -> bytes: ...
    def verify(self, key_material: bytes, expected_key: bytes) -> None: ...
