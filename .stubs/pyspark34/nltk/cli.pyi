from _typeshed import Incomplete
from nltk import word_tokenize as word_tokenize
from nltk.util import parallelize_preprocess as parallelize_preprocess

CONTEXT_SETTINGS: Incomplete

def cli() -> None: ...
def tokenize_file(language, preserve_line, processes, encoding, delimiter) -> None:
    """This command tokenizes text stream using nltk.word_tokenize"""
