from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from _typeshed import Incomplete

class StringCategoryCorpusReader(CorpusReader):
    def __init__(self, root, fileids, delimiter: str = ' ', encoding: str = 'utf8') -> None:
        """
        :param root: The root directory for this corpus.
        :param fileids: A list or regexp specifying the fileids in this corpus.
        :param delimiter: Field delimiter
        """
    def tuples(self, fileids: Incomplete | None = None): ...
