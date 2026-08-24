from nltk.classify.naivebayes import NaiveBayesClassifier as NaiveBayesClassifier
from nltk.probability import DictionaryProbDist as DictionaryProbDist, ELEProbDist as ELEProbDist, FreqDist as FreqDist

class PositiveNaiveBayesClassifier(NaiveBayesClassifier):
    @staticmethod
    def train(positive_featuresets, unlabeled_featuresets, positive_prob_prior: float = 0.5, estimator=...):
        """
        :param positive_featuresets: An iterable of featuresets that are known as positive
            examples (i.e., their label is ``True``).

        :param unlabeled_featuresets: An iterable of featuresets whose label is unknown.

        :param positive_prob_prior: A prior estimate of the probability of the label
            ``True`` (default 0.5).
        """

def demo() -> None: ...
