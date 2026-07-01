from _typeshed import Incomplete
from nltk.classify.maxent import MaxentClassifier as MaxentClassifier
from nltk.classify.util import accuracy as accuracy
from nltk.tokenize import RegexpTokenizer as RegexpTokenizer

class RTEFeatureExtractor:
    """
    This builds a bag of words for both the text and the hypothesis after
    throwing away some stopwords, then calculates overlap and difference.
    """
    stop: Incomplete
    stopwords: Incomplete
    negwords: Incomplete
    text_tokens: Incomplete
    hyp_tokens: Incomplete
    text_words: Incomplete
    hyp_words: Incomplete
    def __init__(self, rtepair, stop: bool = True, use_lemmatize: bool = False) -> None:
        """
        :param rtepair: a ``RTEPair`` from which features should be extracted
        :param stop: if ``True``, stopwords are thrown away.
        :type stop: bool
        """
    def overlap(self, toktype, debug: bool = False):
        """
        Compute the overlap between text and hypothesis.

        :param toktype: distinguish Named Entities from ordinary words
        :type toktype: 'ne' or 'word'
        """
    def hyp_extra(self, toktype, debug: bool = True):
        """
        Compute the extraneous material in the hypothesis.

        :param toktype: distinguish Named Entities from ordinary words
        :type toktype: 'ne' or 'word'
        """

def rte_features(rtepair): ...
def rte_featurize(rte_pairs): ...
def rte_classifier(algorithm, sample_N: Incomplete | None = None): ...
