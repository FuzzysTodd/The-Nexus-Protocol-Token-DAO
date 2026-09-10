from _typeshed import Incomplete
from nltk.internals import deprecated as deprecated
from nltk.metrics.distance import binary_distance as binary_distance
from nltk.probability import ConditionalFreqDist as ConditionalFreqDist, FreqDist as FreqDist

log: Incomplete

class AnnotationTask:
    """Represents an annotation task, i.e. people assign labels to items.

    Notation tries to match notation in Artstein and Poesio (2007).

    In general, coders and items can be represented as any hashable object.
    Integers, for example, are fine, though strings are more readable.
    Labels must support the distance functions applied to them, so e.g.
    a string-edit-distance makes no sense if your labels are integers,
    whereas interval distance needs numeric values.  A notable case of this
    is the MASI metric, which requires Python sets.
    """
    distance: Incomplete
    I: Incomplete
    K: Incomplete
    C: Incomplete
    data: Incomplete
    def __init__(self, data: Incomplete | None = None, distance=...) -> None:
        """Initialize an annotation task.

        The data argument can be None (to create an empty annotation task) or a sequence of 3-tuples,
        each representing a coder's labeling of an item:
        ``(coder,item,label)``

        The distance argument is a function taking two arguments (labels) and producing a numerical distance.
        The distance from a label to itself should be zero:
        ``distance(l,l) = 0``
        """
    def load_array(self, array) -> None:
        """Load an sequence of annotation results, appending to any data already loaded.

        The argument is a sequence of 3-tuples, each representing a coder's labeling of an item:
            (coder,item,label)
        """
    def agr(self, cA, cB, i, data: Incomplete | None = None):
        """Agreement between two coders on a given item"""
    def Nk(self, k): ...
    def Nik(self, i, k): ...
    def Nck(self, c, k): ...
    def N(self, k: Incomplete | None = None, i: Incomplete | None = None, c: Incomplete | None = None):
        '''Implements the "n-notation" used in Artstein and Poesio (2007)'''
    def Ao(self, cA, cB):
        """Observed agreement between two coders on all items."""
    def avg_Ao(self):
        """Average observed agreement across all coders and items."""
    def Do_Kw_pairwise(self, cA, cB, max_distance: float = 1.0):
        """The observed disagreement for the weighted kappa coefficient."""
    def Do_Kw(self, max_distance: float = 1.0):
        """Averaged over all labelers"""
    def S(self):
        """Bennett, Albert and Goldstein 1954"""
    def pi(self):
        """Scott 1955; here, multi-pi.
        Equivalent to K from Siegel and Castellan (1988).

        """
    def Ae_kappa(self, cA, cB): ...
    def kappa_pairwise(self, cA, cB):
        """ """
    def kappa(self):
        """Cohen 1960
        Averages naively over kappas for each coder pair.

        """
    def multi_kappa(self):
        """Davies and Fleiss 1982
        Averages over observed and expected agreements for each coder pair.

        """
    def Disagreement(self, label_freqs): ...
    def alpha(self):
        """Krippendorff 1980"""
    def weighted_kappa_pairwise(self, cA, cB, max_distance: float = 1.0):
        """Cohen 1968"""
    def weighted_kappa(self, max_distance: float = 1.0):
        """Cohen 1968"""
