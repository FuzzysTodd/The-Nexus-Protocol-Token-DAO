import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from typing import Iterable, List

ENGLISH_STOP_WORDS: Incomplete

class WordTokenizer(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def set_vocab(self, vocab: Iterable[str]): ...
    @abstractmethod
    def get_vocab(self, vocab: Iterable[str]): ...
    @abstractmethod
    def tokenize(self, text: str) -> List[int]: ...
    @abstractmethod
    def save(self, output_path: str): ...
    @staticmethod
    @abstractmethod
    def load(input_path: str): ...
