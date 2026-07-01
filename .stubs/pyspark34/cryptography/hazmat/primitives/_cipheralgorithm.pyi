import abc
import typing

class CipherAlgorithm(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        '''
        A string naming this mode (e.g. "AES", "Camellia").
        '''
    @property
    @abc.abstractmethod
    def key_sizes(self) -> typing.FrozenSet[int]:
        """
        Valid key sizes for this algorithm in bits
        """
    @property
    @abc.abstractmethod
    def key_size(self) -> int:
        """
        The size of the key being used as an integer in bits (e.g. 128, 256).
        """

class BlockCipherAlgorithm(CipherAlgorithm, metaclass=abc.ABCMeta):
    key: bytes
    @property
    @abc.abstractmethod
    def block_size(self) -> int:
        """
        The size of a block as an integer in bits (e.g. 64, 128).
        """
