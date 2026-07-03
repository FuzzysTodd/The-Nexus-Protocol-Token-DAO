import abc
from _typeshed import Incomplete
from cryptography import utils as utils
from cryptography.exceptions import UnsupportedAlgorithm as UnsupportedAlgorithm
from cryptography.hazmat.primitives._cipheralgorithm import BlockCipherAlgorithm as BlockCipherAlgorithm, CipherAlgorithm as CipherAlgorithm
from cryptography.hazmat.primitives.ciphers import algorithms as algorithms

class Mode(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        '''
        A string naming this mode (e.g. "ECB", "CBC").
        '''
    @abc.abstractmethod
    def validate_for_algorithm(self, algorithm: CipherAlgorithm) -> None:
        """
        Checks that all the necessary invariants of this (mode, algorithm)
        combination are met.
        """

class ModeWithInitializationVector(Mode, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def initialization_vector(self) -> bytes:
        """
        The value of the initialization vector for this mode as bytes.
        """

class ModeWithTweak(Mode, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def tweak(self) -> bytes:
        """
        The value of the tweak for this mode as bytes.
        """

class ModeWithNonce(Mode, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def nonce(self) -> bytes:
        """
        The value of the nonce for this mode as bytes.
        """

class ModeWithAuthenticationTag(Mode, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def tag(self) -> bytes | None:
        """
        The value of the tag supplied to the constructor of this mode.
        """

class CBC(ModeWithInitializationVector):
    name: str
    def __init__(self, initialization_vector: bytes) -> None: ...
    @property
    def initialization_vector(self) -> bytes: ...
    validate_for_algorithm: Incomplete

class XTS(ModeWithTweak):
    name: str
    def __init__(self, tweak: bytes) -> None: ...
    @property
    def tweak(self) -> bytes: ...
    def validate_for_algorithm(self, algorithm: CipherAlgorithm) -> None: ...

class ECB(Mode):
    name: str
    validate_for_algorithm: Incomplete

class OFB(ModeWithInitializationVector):
    name: str
    def __init__(self, initialization_vector: bytes) -> None: ...
    @property
    def initialization_vector(self) -> bytes: ...
    validate_for_algorithm: Incomplete

class CFB(ModeWithInitializationVector):
    name: str
    def __init__(self, initialization_vector: bytes) -> None: ...
    @property
    def initialization_vector(self) -> bytes: ...
    validate_for_algorithm: Incomplete

class CFB8(ModeWithInitializationVector):
    name: str
    def __init__(self, initialization_vector: bytes) -> None: ...
    @property
    def initialization_vector(self) -> bytes: ...
    validate_for_algorithm: Incomplete

class CTR(ModeWithNonce):
    name: str
    def __init__(self, nonce: bytes) -> None: ...
    @property
    def nonce(self) -> bytes: ...
    def validate_for_algorithm(self, algorithm: CipherAlgorithm) -> None: ...

class GCM(ModeWithInitializationVector, ModeWithAuthenticationTag):
    name: str
    def __init__(self, initialization_vector: bytes, tag: bytes | None = None, min_tag_length: int = 16) -> None: ...
    @property
    def tag(self) -> bytes | None: ...
    @property
    def initialization_vector(self) -> bytes: ...
    def validate_for_algorithm(self, algorithm: CipherAlgorithm) -> None: ...
