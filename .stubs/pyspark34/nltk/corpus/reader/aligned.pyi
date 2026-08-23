from _typeshed import Incomplete
from nltk.corpus.reader.api import CorpusReader as CorpusReader
from nltk.corpus.reader.util import StreamBackedCorpusView as StreamBackedCorpusView, concat as concat, read_alignedsent_block as read_alignedsent_block
from nltk.tokenize import RegexpTokenizer as RegexpTokenizer, WhitespaceTokenizer as WhitespaceTokenizer
from nltk.translate import AlignedSent as AlignedSent, Alignment as Alignment

class AlignedCorpusReader(CorpusReader):
    """
    Reader for corpora of word-aligned sentences.  Tokens are assumed
    to be separated by whitespace.  Sentences begin on separate lines.
    """
    def __init__(self, root, fileids, sep: str = '/', word_tokenizer=..., sent_tokenizer=..., alignedsent_block_reader=..., encoding: str = 'latin1') -> None:
        """
        Construct a new Aligned Corpus reader for a set of documents
        located at the given root directory.  Example usage:

            >>> root = '/...path to corpus.../'
            >>> reader = AlignedCorpusReader(root, '.*', '.txt') # doctest: +SKIP

        :param root: The root directory for this corpus.
        :param fileids: A list or regexp specifying the fileids in this corpus.
        """
    def words(self, fileids: Incomplete | None = None):
        """
        :return: the given file(s) as a list of words
            and punctuation symbols.
        :rtype: list(str)
        """
    def sents(self, fileids: Incomplete | None = None):
        """
        :return: the given file(s) as a list of
            sentences or utterances, each encoded as a list of word
            strings.
        :rtype: list(list(str))
        """
    def aligned_sents(self, fileids: Incomplete | None = None):
        """
        :return: the given file(s) as a list of AlignedSent objects.
        :rtype: list(AlignedSent)
        """

class AlignedSentCorpusView(StreamBackedCorpusView):
    """
    A specialized corpus view for aligned sentences.
    ``AlignedSentCorpusView`` objects are typically created by
    ``AlignedCorpusReader`` (not directly by nltk users).
    """
    def __init__(self, corpus_file, encoding, aligned, group_by_sent, word_tokenizer, sent_tokenizer, alignedsent_block_reader) -> None: ...
    def read_block(self, stream): ...
