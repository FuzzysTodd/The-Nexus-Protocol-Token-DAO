import typing
from cryptography import utils as utils
from cryptography.exceptions import AlreadyFinalized as AlreadyFinalized, InvalidKey as InvalidKey, UnsupportedAlgorithm as UnsupportedAlgorithm
from cryptography.hazmat.primitives import ciphers as ciphers, cmac as cmac, constant_time as constant_time, hashes as hashes, hmac as hmac
from cryptography.hazmat.primitives.kdf import KeyDerivationFunction as KeyDerivationFunction

class Mode(utils.Enum):
    CounterMode: str

class CounterLocation(utils.Enum):
    BeforeFixed: str
    AfterFixed: str
    MiddleFixed: str

class _KBKDFDeriver:
    def __init__(self, prf: typing.Callable, mode: Mode, length: int, rlen: int, llen: int | None, location: CounterLocation, break_location: int | None, label: bytes | None, context: bytes | None, fixed: bytes | None) -> None: ...
    def derive(self, key_material: bytes, prf_output_size: int) -> bytes: ...

class KBKDFHMAC(KeyDerivationFunction):
    def __init__(self, algorithm: hashes.HashAlgorithm, mode: Mode, length: int, rlen: int, llen: int | None, location: CounterLocation, label: bytes | None, context: bytes | None, fixed: bytes | None, backend: typing.Any = None, *, break_location: int | None = None) -> None: ...
    def derive(self, key_material: bytes) -> bytes: ...
    def verify(self, key_material: bytes, expected_key: bytes) -> None: ...

class KBKDFCMAC(KeyDerivationFunction):
    def __init__(self, algorithm, mode: Mode, length: int, rlen: int, llen: int | None, location: CounterLocation, label: bytes | None, context: bytes | None, fixed: bytes | None, backend: typing.Any = None, *, break_location: int | None = None) -> None: ...
    def derive(self, key_material: bytes) -> bytes: ...
    def verify(self, key_material: bytes, expected_key: bytes) -> None: ...
