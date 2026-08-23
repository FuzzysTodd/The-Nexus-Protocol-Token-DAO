import abc
import typing
from _typeshed import Incomplete
from cryptography.exceptions import AlreadyFinalized as AlreadyFinalized, AlreadyUpdated as AlreadyUpdated, NotYetFinalized as NotYetFinalized
from cryptography.hazmat.backends.openssl.ciphers import _CipherContext as _BackendCipherContext
from cryptography.hazmat.primitives._cipheralgorithm import CipherAlgorithm as CipherAlgorithm
from cryptography.hazmat.primitives.ciphers import modes as modes

class CipherContext(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, data: bytes) -> bytes:
        """
        Processes the provided bytes through the cipher and returns the results
        as bytes.
        """
    @abc.abstractmethod
    def update_into(self, data: bytes, buf: bytes) -> int:
        """
        Processes the provided bytes and writes the resulting data into the
        provided buffer. Returns the number of bytes written.
        """
    @abc.abstractmethod
    def finalize(self) -> bytes:
        """
        Returns the results of processing the final block as bytes.
        """

class AEADCipherContext(CipherContext, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def authenticate_additional_data(self, data: bytes) -> None:
        """
        Authenticates the provided bytes.
        """

class AEADDecryptionContext(AEADCipherContext, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def finalize_with_tag(self, tag: bytes) -> bytes:
        """
        Returns the results of processing the final block as bytes and allows
        delayed passing of the authentication tag.
        """

class AEADEncryptionContext(AEADCipherContext, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def tag(self) -> bytes:
        """
        Returns tag bytes. This is only available after encryption is
        finalized.
        """
Mode = typing.TypeVar('Mode', bound=modes.Mode | None, covariant=True)

class Cipher(typing.Generic[Mode]):
    algorithm: Incomplete
    mode: Incomplete
    def __init__(self, algorithm: CipherAlgorithm, mode: Mode, backend: typing.Any = None) -> None: ...
    @typing.overload
    def encryptor(self) -> AEADEncryptionContext: ...
    @typing.overload
    def encryptor(self) -> CipherContext: ...
    @typing.overload
    def decryptor(self) -> AEADDecryptionContext: ...
    @typing.overload
    def decryptor(self) -> CipherContext: ...

class _CipherContext(CipherContext):
    def __init__(self, ctx: _BackendCipherContext) -> None: ...
    def update(self, data: bytes) -> bytes: ...
    def update_into(self, data: bytes, buf: bytes) -> int: ...
    def finalize(self) -> bytes: ...

class _AEADCipherContext(AEADCipherContext):
    def __init__(self, ctx: _BackendCipherContext) -> None: ...
    def update(self, data: bytes) -> bytes: ...
    def update_into(self, data: bytes, buf: bytes) -> int: ...
    def finalize(self) -> bytes: ...
    def authenticate_additional_data(self, data: bytes) -> None: ...

class _AEADDecryptionContext(_AEADCipherContext, AEADDecryptionContext):
    def finalize_with_tag(self, tag: bytes) -> bytes: ...

class _AEADEncryptionContext(_AEADCipherContext, AEADEncryptionContext):
    @property
    def tag(self) -> bytes: ...
