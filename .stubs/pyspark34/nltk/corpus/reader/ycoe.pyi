from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from _typeshed import Incomplete
from nltk.corpus.reader.bracket_parse import BracketParseCorpusReader as BracketParseCorpusReader
from nltk.corpus.reader.tagged import TaggedCorpusReader as TaggedCorpusReader
from nltk.tokenize import RegexpTokenizer as RegexpTokenizer

class YCOECorpusReader(CorpusReader):
    """
    Corpus reader for the York-Toronto-Helsinki Parsed Corpus of Old
    English Prose (YCOE), a 1.5 million word syntactically-annotated
    corpus of Old English prose texts.
    """
    def __init__(self, root, encoding: str = 'utf8') -> None: ...
    def documents(self, fileids: Incomplete | None = None):
        """
        Return a list of document identifiers for all documents in
        this corpus, or for the documents with the given file(s) if
        specified.
        """
    def fileids(self, documents: Incomplete | None = None):
        """
        Return a list of file identifiers for the files that make up
        this corpus, or that store the given document(s) if specified.
        """
    def words(self, documents: Incomplete | None = None): ...
    def sents(self, documents: Incomplete | None = None): ...
    def paras(self, documents: Incomplete | None = None): ...
    def tagged_words(self, documents: Incomplete | None = None): ...
    def tagged_sents(self, documents: Incomplete | None = None): ...
    def tagged_paras(self, documents: Incomplete | None = None): ...
    def parsed_sents(self, documents: Incomplete | None = None): ...

class YCOEParseCorpusReader(BracketParseCorpusReader):
    """Specialized version of the standard bracket parse corpus reader
    that strips out (CODE ...) and (ID ...) nodes."""

class YCOETaggedCorpusReader(TaggedCorpusReader):
    def __init__(self, root, items, encoding: str = 'utf8') -> None: ...

documents: Incomplete
