from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['BigramCollocationFinder', 'TrigramCollocationFinder', 'QuadgramCollocationFinder']

class AbstractCollocationFinder:
    """
    An abstract base class for collocation finders whose purpose is to
    collect collocation candidate frequencies, filter and rank them.

    As a minimum, collocation finders require the frequencies of each
    word in a corpus, and the joint frequency of word tuples. This data
    should be provided through nltk.probability.FreqDist objects or an
    identical interface.
    """
    word_fd: Incomplete
    N: Incomplete
    ngram_fd: Incomplete
    def __init__(self, word_fd, ngram_fd) -> None: ...
    @classmethod
    def from_documents(cls, documents):
        """Constructs a collocation finder given a collection of documents,
        each of which is a list (or iterable) of tokens.
        """
    def apply_freq_filter(self, min_freq):
        """Removes candidate ngrams which have frequency less than min_freq."""
    def apply_ngram_filter(self, fn):
        """Removes candidate ngrams (w1, w2, ...) where fn(w1, w2, ...)
        evaluates to True.
        """
    def apply_word_filter(self, fn):
        """Removes candidate ngrams (w1, w2, ...) where any of (fn(w1), fn(w2),
        ...) evaluates to True.
        """
    def score_ngrams(self, score_fn):
        """Returns a sequence of (ngram, score) pairs ordered from highest to
        lowest score, as determined by the scoring function provided.
        """
    def nbest(self, score_fn, n):
        """Returns the top n ngrams when scored by the given function."""
    def above_score(self, score_fn, min_score) -> Generator[Incomplete, None, None]:
        """Returns a sequence of ngrams, ordered by decreasing score, whose
        scores each exceed the given minimum score.
        """

class BigramCollocationFinder(AbstractCollocationFinder):
    """A tool for the finding and ranking of bigram collocations or other
    association measures. It is often useful to use from_words() rather than
    constructing an instance directly.
    """
    default_ws: int
    window_size: Incomplete
    def __init__(self, word_fd, bigram_fd, window_size: int = 2) -> None:
        """Construct a BigramCollocationFinder, given FreqDists for
        appearances of words and (possibly non-contiguous) bigrams.
        """
    @classmethod
    def from_words(cls, words, window_size: int = 2):
        """Construct a BigramCollocationFinder for all bigrams in the given
        sequence.  When window_size > 2, count non-contiguous bigrams, in the
        style of Church and Hanks's (1990) association ratio.
        """
    def score_ngram(self, score_fn, w1, w2):
        """Returns the score for a given bigram using the given scoring
        function.  Following Church and Hanks (1990), counts are scaled by
        a factor of 1/(window_size - 1).
        """

class TrigramCollocationFinder(AbstractCollocationFinder):
    """A tool for the finding and ranking of trigram collocations or other
    association measures. It is often useful to use from_words() rather than
    constructing an instance directly.
    """
    default_ws: int
    wildcard_fd: Incomplete
    bigram_fd: Incomplete
    def __init__(self, word_fd, bigram_fd, wildcard_fd, trigram_fd) -> None:
        """Construct a TrigramCollocationFinder, given FreqDists for
        appearances of words, bigrams, two words with any word between them,
        and trigrams.
        """
    @classmethod
    def from_words(cls, words, window_size: int = 3):
        """Construct a TrigramCollocationFinder for all trigrams in the given
        sequence.
        """
    def bigram_finder(self):
        """Constructs a bigram collocation finder with the bigram and unigram
        data from this finder. Note that this does not include any filtering
        applied to this finder.
        """
    def score_ngram(self, score_fn, w1, w2, w3):
        """Returns the score for a given trigram using the given scoring
        function.
        """

class QuadgramCollocationFinder(AbstractCollocationFinder):
    """A tool for the finding and ranking of quadgram collocations or other association measures.
    It is often useful to use from_words() rather than constructing an instance directly.
    """
    default_ws: int
    iii: Incomplete
    ii: Incomplete
    ixi: Incomplete
    ixxi: Incomplete
    iixi: Incomplete
    ixii: Incomplete
    def __init__(self, word_fd, quadgram_fd, ii, iii, ixi, ixxi, iixi, ixii) -> None:
        """Construct a QuadgramCollocationFinder, given FreqDists for appearances of words,
        bigrams, trigrams, two words with one word and two words between them, three words
        with a word between them in both variations.
        """
    @classmethod
    def from_words(cls, words, window_size: int = 4): ...
    def score_ngram(self, score_fn, w1, w2, w3, w4): ...
