from nltk.corpus.reader.api import *
from _typeshed import Incomplete
from nltk.corpus.reader import WordListCorpusReader as WordListCorpusReader

class IgnoreReadmeCorpusView(StreamBackedCorpusView):
    """
    This CorpusView is used to skip the initial readme block of the corpus.
    """
    def __init__(self, *args, **kwargs) -> None: ...

class OpinionLexiconCorpusReader(WordListCorpusReader):
    """
    Reader for Liu and Hu opinion lexicon.  Blank lines and readme are ignored.

        >>> from nltk.corpus import opinion_lexicon
        >>> opinion_lexicon.words()
        ['2-faced', '2-faces', 'abnormal', 'abolish', ...]

    The OpinionLexiconCorpusReader provides shortcuts to retrieve positive/negative
    words:

        >>> opinion_lexicon.negative()
        ['2-faced', '2-faces', 'abnormal', 'abolish', ...]

    Note that words from `words()` method are sorted by file id, not alphabetically:

        >>> opinion_lexicon.words()[0:10] # doctest: +NORMALIZE_WHITESPACE
        ['2-faced', '2-faces', 'abnormal', 'abolish', 'abominable', 'abominably',
        'abominate', 'abomination', 'abort', 'aborted']
        >>> sorted(opinion_lexicon.words())[0:10] # doctest: +NORMALIZE_WHITESPACE
        ['2-faced', '2-faces', 'a+', 'abnormal', 'abolish', 'abominable', 'abominably',
        'abominate', 'abomination', 'abort']
    """
    CorpusView = IgnoreReadmeCorpusView
    def words(self, fileids: Incomplete | None = None):
        """
        Return all words in the opinion lexicon. Note that these words are not
        sorted in alphabetical order.

        :param fileids: a list or regexp specifying the ids of the files whose
            words have to be returned.
        :return: the given file(s) as a list of words and punctuation symbols.
        :rtype: list(str)
        """
    def positive(self):
        """
        Return all positive words in alphabetical order.

        :return: a list of positive words.
        :rtype: list(str)
        """
    def negative(self):
        """
        Return all negative words in alphabetical order.

        :return: a list of negative words.
        :rtype: list(str)
        """
