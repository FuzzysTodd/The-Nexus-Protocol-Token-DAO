from nltk.corpus.reader.api import *
from nltk.tokenize import *
from _typeshed import Incomplete

class CategorizedSentencesCorpusReader(CategorizedCorpusReader, CorpusReader):
    '''
    A reader for corpora in which each row represents a single instance, mainly
    a sentence. Istances are divided into categories based on their file identifiers
    (see CategorizedCorpusReader).
    Since many corpora allow rows that contain more than one sentence, it is
    possible to specify a sentence tokenizer to retrieve all sentences instead
    than all rows.

    Examples using the Subjectivity Dataset:

    >>> from nltk.corpus import subjectivity
    >>> subjectivity.sents()[23] # doctest: +NORMALIZE_WHITESPACE
    [\'television\', \'made\', \'him\', \'famous\', \',\', \'but\', \'his\', \'biggest\', \'hits\',
    \'happened\', \'off\', \'screen\', \'.\']
    >>> subjectivity.categories()
    [\'obj\', \'subj\']
    >>> subjectivity.words(categories=\'subj\')
    [\'smart\', \'and\', \'alert\', \',\', \'thirteen\', ...]

    Examples using the Sentence Polarity Dataset:

    >>> from nltk.corpus import sentence_polarity
    >>> sentence_polarity.sents() # doctest: +NORMALIZE_WHITESPACE
    [[\'simplistic\', \',\', \'silly\', \'and\', \'tedious\', \'.\'], ["it\'s", \'so\', \'laddish\',
    \'and\', \'juvenile\', \',\', \'only\', \'teenage\', \'boys\', \'could\', \'possibly\', \'find\',
    \'it\', \'funny\', \'.\'], ...]
    >>> sentence_polarity.categories()
    [\'neg\', \'pos\']
    '''
    CorpusView = StreamBackedCorpusView
    def __init__(self, root, fileids, word_tokenizer=..., sent_tokenizer: Incomplete | None = None, encoding: str = 'utf8', **kwargs) -> None:
        """
        :param root: The root directory for the corpus.
        :param fileids: a list or regexp specifying the fileids in the corpus.
        :param word_tokenizer: a tokenizer for breaking sentences or paragraphs
            into words. Default: `WhitespaceTokenizer`
        :param sent_tokenizer: a tokenizer for breaking paragraphs into sentences.
        :param encoding: the encoding that should be used to read the corpus.
        :param kwargs: additional parameters passed to CategorizedCorpusReader.
        """
    def sents(self, fileids: Incomplete | None = None, categories: Incomplete | None = None):
        """
        Return all sentences in the corpus or in the specified file(s).

        :param fileids: a list or regexp specifying the ids of the files whose
            sentences have to be returned.
        :param categories: a list specifying the categories whose sentences have
            to be returned.
        :return: the given file(s) as a list of sentences.
            Each sentence is tokenized using the specified word_tokenizer.
        :rtype: list(list(str))
        """
    def words(self, fileids: Incomplete | None = None, categories: Incomplete | None = None):
        """
        Return all words and punctuation symbols in the corpus or in the specified
        file(s).

        :param fileids: a list or regexp specifying the ids of the files whose
            words have to be returned.
        :param categories: a list specifying the categories whose words have to
            be returned.
        :return: the given file(s) as a list of words and punctuation symbols.
        :rtype: list(str)
        """
