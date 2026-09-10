from _typeshed import Incomplete
from collections.abc import Generator
from nltk.chunk.api import ChunkParserI as ChunkParserI
from nltk.chunk.util import ChunkScore as ChunkScore
from nltk.classify import MaxentClassifier as MaxentClassifier
from nltk.data import find as find
from nltk.tag import ClassifierBasedTagger as ClassifierBasedTagger, pos_tag as pos_tag
from nltk.tokenize import word_tokenize as word_tokenize
from nltk.tree import Tree as Tree

class NEChunkParserTagger(ClassifierBasedTagger):
    """
    The IOB tagger used by the chunk parser.
    """
    def __init__(self, train) -> None: ...

class NEChunkParser(ChunkParserI):
    """
    Expected input: list of pos-tagged words
    """
    def __init__(self, train) -> None: ...
    def parse(self, tokens):
        """
        Each token should be a pos-tagged word
        """

def shape(word): ...
def simplify_pos(s): ...
def postag_tree(tree): ...
def load_ace_data(roots, fmt: str = 'binary', skip_bnews: bool = True) -> Generator[Incomplete, Incomplete, None]: ...
def load_ace_file(textfile, fmt) -> Generator[Incomplete, None, Incomplete]: ...
def cmp_chunks(correct, guessed) -> None: ...
def build_model(fmt: str = 'binary'): ...
