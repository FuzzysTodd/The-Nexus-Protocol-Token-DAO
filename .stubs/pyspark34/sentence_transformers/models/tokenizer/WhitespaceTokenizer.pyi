from .WordTokenizer import ENGLISH_STOP_WORDS as ENGLISH_STOP_WORDS, WordTokenizer as WordTokenizer
from _typeshed import Incomplete
from typing import Iterable, List

class WhitespaceTokenizer(WordTokenizer):
    """
    Simple and fast white-space tokenizer. Splits sentence based on white spaces.
    Punctuation are stripped from tokens.
    """
    stop_words: Incomplete
    do_lower_case: Incomplete
    def __init__(self, vocab: Iterable[str] = [], stop_words: Iterable[str] = ..., do_lower_case: bool = False) -> None: ...
    def get_vocab(self): ...
    vocab: Incomplete
    word2idx: Incomplete
    def set_vocab(self, vocab: Iterable[str]): ...
    def tokenize(self, text: str) -> List[int]: ...
    def save(self, output_path: str): ...
    @staticmethod
    def load(input_path: str): ...
