from _typeshed import Incomplete
from nltk.corpus.reader.api import CorpusReader as CorpusReader, SyntaxCorpusReader as SyntaxCorpusReader
from nltk.corpus.reader.util import FileSystemPathPointer as FileSystemPathPointer, find_corpus_fileids as find_corpus_fileids, read_blankline_block as read_blankline_block
from nltk.parse import DependencyGraph as DependencyGraph

class KNBCorpusReader(SyntaxCorpusReader):
    """
    This class implements:
      - ``__init__``, which specifies the location of the corpus
        and a method for detecting the sentence blocks in corpus files.
      - ``_read_block``, which reads a block from the input stream.
      - ``_word``, which takes a block and returns a list of list of words.
      - ``_tag``, which takes a block and returns a list of list of tagged
        words.
      - ``_parse``, which takes a block and returns a list of parsed
        sentences.

    The structure of tagged words:
      tagged_word = (word(str), tags(tuple))
      tags = (surface, reading, lemma, pos1, posid1, pos2, posid2, pos3, posid3, others ...)

    Usage example

    >>> from nltk.corpus.util import LazyCorpusLoader
    >>> knbc = LazyCorpusLoader(
    ...     'knbc/corpus1',
    ...     KNBCorpusReader,
    ...     r'.*/KN.*',
    ...     encoding='euc-jp',
    ... )

    >>> len(knbc.sents()[0])
    9

    """
    morphs2str: Incomplete
    def __init__(self, root, fileids, encoding: str = 'utf8', morphs2str=...) -> None:
        """
        Initialize KNBCorpusReader
        morphs2str is a function to convert morphlist to str for tree representation
        for _parse()
        """

def demo(): ...
def test() -> None: ...
