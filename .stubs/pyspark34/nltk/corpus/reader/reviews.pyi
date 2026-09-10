from nltk.corpus.reader.api import *
from nltk.tokenize import *
from _typeshed import Incomplete

TITLE: Incomplete
FEATURES: Incomplete
NOTES: Incomplete
SENT: Incomplete

class Review:
    """
    A Review is the main block of a ReviewsCorpusReader.
    """
    title: Incomplete
    review_lines: Incomplete
    def __init__(self, title: Incomplete | None = None, review_lines: Incomplete | None = None) -> None:
        """
        :param title: the title of the review.
        :param review_lines: the list of the ReviewLines that belong to the Review.
        """
    def add_line(self, review_line) -> None:
        """
        Add a line (ReviewLine) to the review.

        :param review_line: a ReviewLine instance that belongs to the Review.
        """
    def features(self):
        """
        Return a list of features in the review. Each feature is a tuple made of
        the specific item feature and the opinion strength about that feature.

        :return: all features of the review as a list of tuples (feat, score).
        :rtype: list(tuple)
        """
    def sents(self):
        """
        Return all tokenized sentences in the review.

        :return: all sentences of the review as lists of tokens.
        :rtype: list(list(str))
        """

class ReviewLine:
    """
    A ReviewLine represents a sentence of the review, together with (optional)
    annotations of its features and notes about the reviewed item.
    """
    sent: Incomplete
    features: Incomplete
    notes: Incomplete
    def __init__(self, sent, features: Incomplete | None = None, notes: Incomplete | None = None) -> None: ...

class ReviewsCorpusReader(CorpusReader):
    """
    Reader for the Customer Review Data dataset by Hu, Liu (2004).
    Note: we are not applying any sentence tokenization at the moment, just word
    tokenization.

        >>> from nltk.corpus import product_reviews_1
        >>> camera_reviews = product_reviews_1.reviews('Canon_G3.txt')
        >>> review = camera_reviews[0]
        >>> review.sents()[0] # doctest: +NORMALIZE_WHITESPACE
        ['i', 'recently', 'purchased', 'the', 'canon', 'powershot', 'g3', 'and', 'am',
        'extremely', 'satisfied', 'with', 'the', 'purchase', '.']
        >>> review.features() # doctest: +NORMALIZE_WHITESPACE
        [('canon powershot g3', '+3'), ('use', '+2'), ('picture', '+2'),
        ('picture quality', '+1'), ('picture quality', '+1'), ('camera', '+2'),
        ('use', '+2'), ('feature', '+1'), ('picture quality', '+3'), ('use', '+1'),
        ('option', '+1')]

    We can also reach the same information directly from the stream:

        >>> product_reviews_1.features('Canon_G3.txt')
        [('canon powershot g3', '+3'), ('use', '+2'), ...]

    We can compute stats for specific product features:

        >>> n_reviews = len([(feat,score) for (feat,score) in product_reviews_1.features('Canon_G3.txt') if feat=='picture'])
        >>> tot = sum([int(score) for (feat,score) in product_reviews_1.features('Canon_G3.txt') if feat=='picture'])
        >>> mean = tot / n_reviews
        >>> print(n_reviews, tot, mean)
        15 24 1.6
    """
    CorpusView = StreamBackedCorpusView
    def __init__(self, root, fileids, word_tokenizer=..., encoding: str = 'utf8') -> None:
        """
        :param root: The root directory for the corpus.
        :param fileids: a list or regexp specifying the fileids in the corpus.
        :param word_tokenizer: a tokenizer for breaking sentences or paragraphs
            into words. Default: `WordPunctTokenizer`
        :param encoding: the encoding that should be used to read the corpus.
        """
    def features(self, fileids: Incomplete | None = None):
        """
        Return a list of features. Each feature is a tuple made of the specific
        item feature and the opinion strength about that feature.

        :param fileids: a list or regexp specifying the ids of the files whose
            features have to be returned.
        :return: all features for the item(s) in the given file(s).
        :rtype: list(tuple)
        """
    def reviews(self, fileids: Incomplete | None = None):
        """
        Return all the reviews as a list of Review objects. If `fileids` is
        specified, return all the reviews from each of the specified files.

        :param fileids: a list or regexp specifying the ids of the files whose
            reviews have to be returned.
        :return: the given file(s) as a list of reviews.
        """
    def sents(self, fileids: Incomplete | None = None):
        """
        Return all sentences in the corpus or in the specified files.

        :param fileids: a list or regexp specifying the ids of the files whose
            sentences have to be returned.
        :return: the given file(s) as a list of sentences, each encoded as a
            list of word strings.
        :rtype: list(list(str))
        """
    def words(self, fileids: Incomplete | None = None):
        """
        Return all words and punctuation symbols in the corpus or in the specified
        files.

        :param fileids: a list or regexp specifying the ids of the files whose
            words have to be returned.
        :return: the given file(s) as a list of words and punctuation symbols.
        :rtype: list(str)
        """
