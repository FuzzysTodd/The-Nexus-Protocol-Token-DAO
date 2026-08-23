from _typeshed import Incomplete
from nltk.lm.api import Smoothing as Smoothing
from nltk.probability import ConditionalFreqDist as ConditionalFreqDist

class WittenBell(Smoothing):
    """Witten-Bell smoothing."""
    def __init__(self, vocabulary, counter, **kwargs) -> None: ...
    def alpha_gamma(self, word, context): ...
    def unigram_score(self, word): ...

class AbsoluteDiscounting(Smoothing):
    """Smoothing with absolute discount."""
    discount: Incomplete
    def __init__(self, vocabulary, counter, discount: float = 0.75, **kwargs) -> None: ...
    def alpha_gamma(self, word, context): ...
    def unigram_score(self, word): ...

class KneserNey(Smoothing):
    """Kneser-Ney Smoothing.

    This is an extension of smoothing with a discount.

    Resources:
    - https://pages.ucsd.edu/~rlevy/lign256/winter2008/kneser_ney_mini_example.pdf
    - https://www.youtube.com/watch?v=ody1ysUTD7o
    - https://medium.com/@dennyc/a-simple-numerical-example-for-kneser-ney-smoothing-nlp-4600addf38b8
    - https://www.cl.uni-heidelberg.de/courses/ss15/smt/scribe6.pdf
    - https://www-i6.informatik.rwth-aachen.de/publications/download/951/Kneser-ICASSP-1995.pdf
    """
    discount: Incomplete
    def __init__(self, vocabulary, counter, order, discount: float = 0.1, **kwargs) -> None: ...
    def unigram_score(self, word): ...
    def alpha_gamma(self, word, context): ...
