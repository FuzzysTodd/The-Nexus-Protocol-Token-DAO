from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.tokenize import *
from _typeshed import Incomplete
from nltk.corpus.reader.timit import read_timit_block as read_timit_block
from nltk.tag import map_tag as map_tag, str2tuple as str2tuple

class TaggedCorpusReader(CorpusReader):
    """
    Reader for simple part-of-speech tagged corpora.  Paragraphs are
    assumed to be split using blank lines.  Sentences and words can be
    tokenized using the default tokenizers, or by custom tokenizers
    specified as parameters to the constructor.  Words are parsed
    using ``nltk.tag.str2tuple``.  By default, ``'/'`` is used as the
    separator.  I.e., words should have the form::

       word1/tag1 word2/tag2 word3/tag3 ...

    But custom separators may be specified as parameters to the
    constructor.  Part of speech tags are case-normalized to upper
    case.
    """
    def __init__(self, root, fileids, sep: str = '/', word_tokenizer=..., sent_tokenizer=..., para_block_reader=..., encoding: str = 'utf8', tagset: Incomplete | None = None) -> None:
        """
        Construct a new Tagged Corpus reader for a set of documents
        located at the given root directory.  Example usage:

            >>> root = '/...path to corpus.../'
            >>> reader = TaggedCorpusReader(root, '.*', '.txt') # doctest: +SKIP

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
    def paras(self, fileids: Incomplete | None = None):
        """
        :return: the given file(s) as a list of
            paragraphs, each encoded as a list of sentences, which are
            in turn encoded as lists of word strings.
        :rtype: list(list(list(str)))
        """
    def tagged_words(self, fileids: Incomplete | None = None, tagset: Incomplete | None = None):
        """
        :return: the given file(s) as a list of tagged
            words and punctuation symbols, encoded as tuples
            ``(word,tag)``.
        :rtype: list(tuple(str,str))
        """
    def tagged_sents(self, fileids: Incomplete | None = None, tagset: Incomplete | None = None):
        """
        :return: the given file(s) as a list of
            sentences, each encoded as a list of ``(word,tag)`` tuples.

        :rtype: list(list(tuple(str,str)))
        """
    def tagged_paras(self, fileids: Incomplete | None = None, tagset: Incomplete | None = None):
        """
        :return: the given file(s) as a list of
            paragraphs, each encoded as a list of sentences, which are
            in turn encoded as lists of ``(word,tag)`` tuples.
        :rtype: list(list(list(tuple(str,str))))
        """

class CategorizedTaggedCorpusReader(CategorizedCorpusReader, TaggedCorpusReader):
    """
    A reader for part-of-speech tagged corpora whose documents are
    divided into categories based on their file identifiers.
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the corpus reader.  Categorization arguments
        (``cat_pattern``, ``cat_map``, and ``cat_file``) are passed to
        the ``CategorizedCorpusReader`` constructor.  The remaining arguments
        are passed to the ``TaggedCorpusReader``.
        """
    def tagged_words(self, fileids: Incomplete | None = None, categories: Incomplete | None = None, tagset: Incomplete | None = None): ...
    def tagged_sents(self, fileids: Incomplete | None = None, categories: Incomplete | None = None, tagset: Incomplete | None = None): ...
    def tagged_paras(self, fileids: Incomplete | None = None, categories: Incomplete | None = None, tagset: Incomplete | None = None): ...

class TaggedCorpusView(StreamBackedCorpusView):
    """
    A specialized corpus view for tagged documents.  It can be
    customized via flags to divide the tagged corpus documents up by
    sentence or paragraph, and to include or omit part of speech tags.
    ``TaggedCorpusView`` objects are typically created by
    ``TaggedCorpusReader`` (not directly by nltk users).
    """
    def __init__(self, corpus_file, encoding, tagged, group_by_sent, group_by_para, sep, word_tokenizer, sent_tokenizer, para_block_reader, tag_mapping_function: Incomplete | None = None) -> None: ...
    def read_block(self, stream):
        """Reads one paragraph at a time."""

class MacMorphoCorpusReader(TaggedCorpusReader):
    """
    A corpus reader for the MAC_MORPHO corpus.  Each line contains a
    single tagged word, using '_' as a separator.  Sentence boundaries
    are based on the end-sentence tag ('_.').  Paragraph information
    is not included in the corpus, so each paragraph returned by
    ``self.paras()`` and ``self.tagged_paras()`` contains a single
    sentence.
    """
    def __init__(self, root, fileids, encoding: str = 'utf8', tagset: Incomplete | None = None) -> None: ...

class TimitTaggedCorpusReader(TaggedCorpusReader):
    """
    A corpus reader for tagged sentences that are included in the TIMIT corpus.
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def paras(self) -> None: ...
    def tagged_paras(self) -> None: ...
