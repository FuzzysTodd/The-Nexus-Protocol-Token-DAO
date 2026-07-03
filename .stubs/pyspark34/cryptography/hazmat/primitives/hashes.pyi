import abc
from _typeshed import Incomplete

__all__ = ['HashAlgorithm', 'HashContext', 'Hash', 'ExtendableOutputFunction', 'SHA1', 'SHA512_224', 'SHA512_256', 'SHA224', 'SHA256', 'SHA384', 'SHA512', 'SHA3_224', 'SHA3_256', 'SHA3_384', 'SHA3_512', 'SHAKE128', 'SHAKE256', 'MD5', 'BLAKE2b', 'BLAKE2s', 'SM3']

class HashAlgorithm(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        '''
        A string naming this algorithm (e.g. "sha256", "md5").
        '''
    @property
    @abc.abstractmethod
    def digest_size(self) -> int:
        """
        The size of the resulting digest in bytes.
        """
    @property
    @abc.abstractmethod
    def block_size(self) -> int | None:
        """
        The internal block size of the hash function, or None if the hash
        function does not use blocks internally (e.g. SHA3).
        """

class HashContext(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def algorithm(self) -> HashAlgorithm:
        """
        A HashAlgorithm that will be used by this context.
        """
    @abc.abstractmethod
    def update(self, data: bytes) -> None:
        """
        Processes the provided bytes through the hash.
        """
    @abc.abstractmethod
    def finalize(self) -> bytes:
        """
        Finalizes the hash context and returns the hash digest as bytes.
        """
    @abc.abstractmethod
    def copy(self) -> HashContext:
        """
        Return a HashContext that is a copy of the current context.
        """

Hash: Incomplete

class ExtendableOutputFunction(metaclass=abc.ABCMeta):
    """
    An interface for extendable output functions.
    """

class SHA1(HashAlgorithm):
    name: str
    digest_size: int
    block_size: int

class SHA512_224(HashAlgorithm):
    name: str
    digest_size: int
    block_size: int

class SHA512_256(HashAlgorithm):
    name: str
    digest_size: int
    block_size: int

class SHA224(HashAlgorithm):
    name: str
    digest_size: int
    block_size: int

class SHA256(HashAlgorithm):
    name: str
    digest_size: int
    block_size: int

class SHA384(HashAlgorithm):
    name: str
    digest_size: int
    block_size: int

class SHA512(HashAlgorithm):
    name: str
    digest_size: int
    block_size: int

class SHA3_224(HashAlgorithm):
    name: str
    digest_size: int
    block_size: Incomplete

class SHA3_256(HashAlgorithm):
    name: str
    digest_size: int
    block_size: Incomplete

class SHA3_384(HashAlgorithm):
    name: str
    digest_size: int
    block_size: Incomplete

class SHA3_512(HashAlgorithm):
    name: str
    digest_size: int
    block_size: Incomplete

class SHAKE128(HashAlgorithm, ExtendableOutputFunction):
    name: str
    block_size: Incomplete
    def __init__(self, digest_size: int) -> None: ...
    @property
    def digest_size(self) -> int: ...

class SHAKE256(HashAlgorithm, ExtendableOutputFunction):
    name: str
    block_size: Incomplete
    def __init__(self, digest_size: int) -> None: ...
    @property
    def digest_size(self) -> int: ...

class MD5(HashAlgorithm):
    name: str
    digest_size: int
    block_size: int

class BLAKE2b(HashAlgorithm):
    name: str
    block_size: int
    def __init__(self, digest_size: int) -> None: ...
    @property
    def digest_size(self) -> int: ...

class BLAKE2s(HashAlgorithm):
    name: str
    block_size: int
    def __init__(self, digest_size: int) -> None: ...
    @property
    def digest_size(self) -> int: ...

class SM3(HashAlgorithm):
    name: str
    digest_size: int
    block_size: int
