from nltk.corpus.reader.api import *
from nltk.tokenize import *
from _typeshed import Incomplete

class ProsConsCorpusReader(CategorizedCorpusReader, CorpusReader):
    """
    Reader for the Pros and Cons sentence dataset.

        >>> from nltk.corpus import pros_cons
        >>> pros_cons.sents(categories='Cons') # doctest: +NORMALIZE_WHITESPACE
        [['East', 'batteries', '!', 'On', '-', 'off', 'switch', 'too', 'easy',
        'to', 'maneuver', '.'], ['Eats', '...', 'no', ',', 'GULPS', 'batteries'],
        ...]
        >>> pros_cons.words('IntegratedPros.txt')
        ['Easy', 'to', 'use', ',', 'economical', '!', ...]
    """
    CorpusView = StreamBackedCorpusView
    def __init__(self, root, fileids, word_tokenizer=..., encoding: str = 'utf8', **kwargs) -> None:
        """
        :param root: The root directory for the corpus.
        :param fileids: a list or regexp specifying the fileids in the corpus.
        :param word_tokenizer: a tokenizer for breaking sentences or paragraphs
            into words. Default: `WhitespaceTokenizer`
        :param encoding: the encoding that should be used to read the corpus.
        :param kwargs: additional parameters passed to CategorizedCorpusReader.
        """
    def sents(self, fileids: Incomplete | None = None, categories: Incomplete | None = None):
        """
        Return all sentences in the corpus or in the specified files/categories.

        :param fileids: a list or regexp specifying the ids of the files whose
            sentences have to be returned.
        :param categories: a list specifying the categories whose sentences
            have to be returned.
        :return: the given file(s) as a list of sentences. Each sentence is
            tokenized using the specified word_tokenizer.
        :rtype: list(list(str))
        """
    def words(self, fileids: Incomplete | None = None, categories: Incomplete | None = None):
        """
        Return all words and punctuation symbols in the corpus or in the specified
        files/categories.

        :param fileids: a list or regexp specifying the ids of the files whose
            words have to be returned.
        :param categories: a list specifying the categories whose words have
            to be returned.
        :return: the given file(s) as a list of words and punctuation symbols.
        :rtype: list(str)
        """
