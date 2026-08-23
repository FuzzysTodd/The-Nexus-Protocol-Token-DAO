import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Generator
from nltk.internals import overridden as overridden
from nltk.tokenize.util import string_span_tokenize as string_span_tokenize
from typing import Iterator, List, Tuple

class TokenizerI(ABC, metaclass=abc.ABCMeta):
    """
    A processing interface for tokenizing a string.
    Subclasses must define ``tokenize()`` or ``tokenize_sents()`` (or both).
    """
    @abstractmethod
    def tokenize(self, s: str) -> List[str]:
        """
        Return a tokenized copy of *s*.

        :rtype: List[str]
        """
    def span_tokenize(self, s: str) -> Iterator[Tuple[int, int]]:
        """
        Identify the tokens using integer offsets ``(start_i, end_i)``,
        where ``s[start_i:end_i]`` is the corresponding token.

        :rtype: Iterator[Tuple[int, int]]
        """
    def tokenize_sents(self, strings: List[str]) -> List[List[str]]:
        """
        Apply ``self.tokenize()`` to each element of ``strings``.  I.e.:

            return [self.tokenize(s) for s in strings]

        :rtype: List[List[str]]
        """
    def span_tokenize_sents(self, strings: List[str]) -> Iterator[List[Tuple[int, int]]]:
        """
        Apply ``self.span_tokenize()`` to each element of ``strings``.  I.e.:

            return [self.span_tokenize(s) for s in strings]

        :yield: List[Tuple[int, int]]
        """

class StringTokenizer(TokenizerI, metaclass=abc.ABCMeta):
    """A tokenizer that divides a string into substrings by splitting
    on the specified string (defined in subclasses).
    """
    def tokenize(self, s): ...
    def span_tokenize(self, s) -> Generator[Incomplete, Incomplete, None]: ...
