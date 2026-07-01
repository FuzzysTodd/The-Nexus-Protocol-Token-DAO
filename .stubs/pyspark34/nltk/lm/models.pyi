from _typeshed import Incomplete
from nltk.lm.api import LanguageModel as LanguageModel, Smoothing as Smoothing
from nltk.lm.smoothing import AbsoluteDiscounting as AbsoluteDiscounting, KneserNey as KneserNey, WittenBell as WittenBell

class MLE(LanguageModel):
    """Class for providing MLE ngram model scores.

    Inherits initialization from BaseNgramModel.
    """
    def unmasked_score(self, word, context: Incomplete | None = None):
        """Returns the MLE score for a word given a context.

        Args:
        - word is expected to be a string
        - context is expected to be something reasonably convertible to a tuple
        """

class Lidstone(LanguageModel):
    """Provides Lidstone-smoothed scores.

    In addition to initialization arguments from BaseNgramModel also requires
    a number by which to increase the counts, gamma.
    """
    gamma: Incomplete
    def __init__(self, gamma, *args, **kwargs) -> None: ...
    def unmasked_score(self, word, context: Incomplete | None = None):
        """Add-one smoothing: Lidstone or Laplace.

        To see what kind, look at `gamma` attribute on the class.

        """

class Laplace(Lidstone):
    """Implements Laplace (add one) smoothing.

    Initialization identical to BaseNgramModel because gamma is always 1.
    """
    def __init__(self, *args, **kwargs) -> None: ...

class StupidBackoff(LanguageModel):
    """Provides StupidBackoff scores.

    In addition to initialization arguments from BaseNgramModel also requires
    a parameter alpha with which we scale the lower order probabilities.
    Note that this is not a true probability distribution as scores for ngrams
    of the same order do not sum up to unity.
    """
    alpha: Incomplete
    def __init__(self, alpha: float = 0.4, *args, **kwargs) -> None: ...
    def unmasked_score(self, word, context: Incomplete | None = None): ...

class InterpolatedLanguageModel(LanguageModel):
    """Logic common to all interpolated language models.

    The idea to abstract this comes from Chen & Goodman 1995.
    Do not instantiate this class directly!
    """
    estimator: Incomplete
    def __init__(self, smoothing_cls, order, **kwargs) -> None: ...
    def unmasked_score(self, word, context: Incomplete | None = None): ...

class WittenBellInterpolated(InterpolatedLanguageModel):
    """Interpolated version of Witten-Bell smoothing."""
    def __init__(self, order, **kwargs) -> None: ...

class AbsoluteDiscountingInterpolated(InterpolatedLanguageModel):
    """Interpolated version of smoothing with absolute discount."""
    def __init__(self, order, discount: float = 0.75, **kwargs) -> None: ...

class KneserNeyInterpolated(InterpolatedLanguageModel):
    """Interpolated version of Kneser-Ney smoothing."""
    def __init__(self, order, discount: float = 0.1, **kwargs) -> None: ...
