from nltk.corpus.reader.api import *
from nltk.tokenize import *
from _typeshed import Incomplete

STARS: Incomplete
COMPARISON: Incomplete
CLOSE_COMPARISON: Incomplete
GRAD_COMPARISON: Incomplete
NON_GRAD_COMPARISON: Incomplete
ENTITIES_FEATS: Incomplete
KEYWORD: Incomplete

class Comparison:
    """
    A Comparison represents a comparative sentence and its constituents.
    """
    text: Incomplete
    comp_type: Incomplete
    entity_1: Incomplete
    entity_2: Incomplete
    feature: Incomplete
    keyword: Incomplete
    def __init__(self, text: Incomplete | None = None, comp_type: Incomplete | None = None, entity_1: Incomplete | None = None, entity_2: Incomplete | None = None, feature: Incomplete | None = None, keyword: Incomplete | None = None) -> None:
        """
        :param text: a string (optionally tokenized) containing a comparison.
        :param comp_type: an integer defining the type of comparison expressed.
            Values can be: 1 (Non-equal gradable), 2 (Equative), 3 (Superlative),
            4 (Non-gradable).
        :param entity_1: the first entity considered in the comparison relation.
        :param entity_2: the second entity considered in the comparison relation.
        :param feature: the feature considered in the comparison relation.
        :param keyword: the word or phrase which is used for that comparative relation.
        """

class ComparativeSentencesCorpusReader(CorpusReader):
    '''
    Reader for the Comparative Sentence Dataset by Jindal and Liu (2006).

        >>> from nltk.corpus import comparative_sentences
        >>> comparison = comparative_sentences.comparisons()[0]
        >>> comparison.text # doctest: +NORMALIZE_WHITESPACE
        [\'its\', \'fast-forward\', \'and\', \'rewind\', \'work\', \'much\', \'more\', \'smoothly\',
        \'and\', \'consistently\', \'than\', \'those\', \'of\', \'other\', \'models\', \'i\', "\'ve",
        \'had\', \'.\']
        >>> comparison.entity_2
        \'models\'
        >>> (comparison.feature, comparison.keyword)
        (\'rewind\', \'more\')
        >>> len(comparative_sentences.comparisons())
        853
    '''
    CorpusView = StreamBackedCorpusView
    def __init__(self, root, fileids, word_tokenizer=..., sent_tokenizer: Incomplete | None = None, encoding: str = 'utf8') -> None:
        """
        :param root: The root directory for this corpus.
        :param fileids: a list or regexp specifying the fileids in this corpus.
        :param word_tokenizer: tokenizer for breaking sentences or paragraphs
            into words. Default: `WhitespaceTokenizer`
        :param sent_tokenizer: tokenizer for breaking paragraphs into sentences.
        :param encoding: the encoding that should be used to read the corpus.
        """
    def comparisons(self, fileids: Incomplete | None = None):
        """
        Return all comparisons in the corpus.

        :param fileids: a list or regexp specifying the ids of the files whose
            comparisons have to be returned.
        :return: the given file(s) as a list of Comparison objects.
        :rtype: list(Comparison)
        """
    def keywords(self, fileids: Incomplete | None = None):
        """
        Return a set of all keywords used in the corpus.

        :param fileids: a list or regexp specifying the ids of the files whose
            keywords have to be returned.
        :return: the set of keywords and comparative phrases used in the corpus.
        :rtype: set(str)
        """
    def keywords_readme(self):
        """
        Return the list of words and constituents considered as clues of a
        comparison (from listOfkeywords.txt).
        """
    def sents(self, fileids: Incomplete | None = None):
        """
        Return all sentences in the corpus.

        :param fileids: a list or regexp specifying the ids of the files whose
            sentences have to be returned.
        :return: all sentences of the corpus as lists of tokens (or as plain
            strings, if no word tokenizer is specified).
        :rtype: list(list(str)) or list(str)
        """
    def words(self, fileids: Incomplete | None = None):
        """
        Return all words and punctuation symbols in the corpus.

        :param fileids: a list or regexp specifying the ids of the files whose
            words have to be returned.
        :return: the given file(s) as a list of words and punctuation symbols.
        :rtype: list(str)
        """
