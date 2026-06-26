from _typeshed import Incomplete
from cryptography import utils as utils
from cryptography.hazmat.primitives.ciphers import BlockCipherAlgorithm as BlockCipherAlgorithm, CipherAlgorithm as CipherAlgorithm

class AES(BlockCipherAlgorithm):
    name: str
    block_size: int
    key_sizes: Incomplete
    key: Incomplete
    def __init__(self, key: bytes) -> None: ...
    @property
    def key_size(self) -> int: ...

class AES128(BlockCipherAlgorithm):
    name: str
    block_size: int
    key_sizes: Incomplete
    key_size: int
    key: Incomplete
    def __init__(self, key: bytes) -> None: ...

class AES256(BlockCipherAlgorithm):
    name: str
    block_size: int
    key_sizes: Incomplete
    key_size: int
    key: Incomplete
    def __init__(self, key: bytes) -> None: ...

class Camellia(BlockCipherAlgorithm):
    name: str
    block_size: int
    key_sizes: Incomplete
    key: Incomplete
    def __init__(self, key: bytes) -> None: ...
    @property
    def key_size(self) -> int: ...

class TripleDES(BlockCipherAlgorithm):
    name: str
    block_size: int
    key_sizes: Incomplete
    key: Incomplete
    def __init__(self, key: bytes) -> None: ...
    @property
    def key_size(self) -> int: ...

class Blowfish(BlockCipherAlgorithm):
    name: str
    block_size: int
    key_sizes: Incomplete
    key: Incomplete
    def __init__(self, key: bytes) -> None: ...
    @property
    def key_size(self) -> int: ...

class CAST5(BlockCipherAlgorithm):
    name: str
    block_size: int
    key_sizes: Incomplete
    key: Incomplete
    def __init__(self, key: bytes) -> None: ...
    @property
    def key_size(self) -> int: ...

class ARC4(CipherAlgorithm):
    name: str
    key_sizes: Incomplete
    key: Incomplete
    def __init__(self, key: bytes) -> None: ...
    @property
    def key_size(self) -> int: ...

class IDEA(BlockCipherAlgorithm):
    name: str
    block_size: int
    key_sizes: Incomplete
    key: Incomplete
    def __init__(self, key: bytes) -> None: ...
    @property
    def key_size(self) -> int: ...

class SEED(BlockCipherAlgorithm):
    name: str
    block_size: int
    key_sizes: Incomplete
    key: Incomplete
    def __init__(self, key: bytes) -> None: ...
    @property
    def key_size(self) -> int: ...

class ChaCha20(CipherAlgorithm):
    name: str
    key_sizes: Incomplete
    key: Incomplete
    def __init__(self, key: bytes, nonce: bytes) -> None: ...
    @property
    def nonce(self) -> bytes: ...
    @property
    def key_size(self) -> int: ...

class SM4(BlockCipherAlgorithm):
    name: str
    block_size: int
    key_sizes: Incomplete
    key: Incomplete
    def __init__(self, key: bytes) -> None: ...
    @property
    def key_size(self) -> int: ...
