from . import kernels as kernels
from _typeshed import Incomplete
from statsmodels.compat.python import lzip as lzip
from statsmodels.tools.validation import array_like as array_like

class KDE:
    """
    Kernel Density Estimator

    Parameters
    ----------
    x : array_like
        N-dimensional array from which the density is to be estimated
    kernel : Kernel Class
        Should be a class from *
    """
    kernel: Incomplete
    n: Incomplete
    x: Incomplete
    def __init__(self, x, kernel: Incomplete | None = None) -> None: ...
    def density(self, x): ...
    def __call__(self, x, h: str = 'scott'): ...
    def evaluate(self, x, h: str = 'silverman'): ...
