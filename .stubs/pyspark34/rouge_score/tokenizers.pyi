import abc
from rouge_score import tokenize as tokenize

class Tokenizer(abc.ABC, metaclass=abc.ABCMeta):
    """Abstract base class for a tokenizer.

  Subclasses of Tokenizer must implement the tokenize() method.
  """
    @abc.abstractmethod
    def tokenize(self, text): ...

class DefaultTokenizer(Tokenizer):
    """Default tokenizer which tokenizes on whitespace."""
    def __init__(self, use_stemmer: bool = False) -> None:
        """Constructor for DefaultTokenizer.

    Args:
      use_stemmer: boolean, indicating whether Porter stemmer should be used to
      strip word suffixes to improve matching.
    """
    def tokenize(self, text): ...
