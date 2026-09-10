from .WordTokenizer import ENGLISH_STOP_WORDS as ENGLISH_STOP_WORDS, WordTokenizer as WordTokenizer
from _typeshed import Incomplete
from typing import Iterable, List

logger: Incomplete

class PhraseTokenizer(WordTokenizer):
    """Tokenizes the text with respect to existent phrases in the vocab.

    This tokenizers respects phrases that are in the vocab. Phrases are separated with 'ngram_separator', for example,
    in Google News word2vec file, ngrams are separated with a _ like New_York. These phrases are detected in text and merged as one special token. (New York is the ... => [New_York, is, the])
    """
    stop_words: Incomplete
    do_lower_case: Incomplete
    ngram_separator: Incomplete
    max_ngram_length: Incomplete
    def __init__(self, vocab: Iterable[str] = [], stop_words: Iterable[str] = ..., do_lower_case: bool = False, ngram_separator: str = '_', max_ngram_length: int = 5) -> None: ...
    def get_vocab(self): ...
    vocab: Incomplete
    word2idx: Incomplete
    ngram_lookup: Incomplete
    ngram_lengths: Incomplete
    def set_vocab(self, vocab: Iterable[str]): ...
    def tokenize(self, text: str) -> List[int]: ...
    def save(self, output_path: str): ...
    @staticmethod
    def load(input_path: str): ...
