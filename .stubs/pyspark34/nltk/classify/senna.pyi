from _typeshed import Incomplete
from nltk.tag.api import TaggerI as TaggerI

class Senna(TaggerI):
    SUPPORTED_OPERATIONS: Incomplete
    operations: Incomplete
    def __init__(self, senna_path, operations, encoding: str = 'utf-8') -> None: ...
    def executable(self, base_path):
        """
        The function that determines the system specific binary that should be
        used in the pipeline. In case, the system is not known the default senna binary will
        be used.
        """
    def tag(self, tokens):
        """
        Applies the specified operation(s) on a list of tokens.
        """
    def tag_sents(self, sentences):
        """
        Applies the tag method over a list of sentences. This method will return a
        list of dictionaries. Every dictionary will contain a word with its
        calculated annotations/tags.
        """
