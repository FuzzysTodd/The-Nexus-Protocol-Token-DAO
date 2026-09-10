from _typeshed import Incomplete

__all__ = ['stateful_transform', 'center', 'standardize', 'scale']

def stateful_transform(class_):
    """Create a stateful transform callable object from a class that fulfills
    the :ref:`stateful transform protocol <stateful-transform-protocol>`.
    """

class Center:
    """center(x)

    A stateful transform that centers input data, i.e., subtracts the mean.

    If input has multiple columns, centers each column separately.

    Equivalent to ``standardize(x, rescale=False)``
    """
    def __init__(self) -> None: ...
    def memorize_chunk(self, x) -> None: ...
    def memorize_finish(self) -> None: ...
    def transform(self, x): ...

center: Incomplete

class Standardize:
    """standardize(x, center=True, rescale=True, ddof=0)

    A stateful transform that standardizes input data, i.e. it subtracts the
    mean and divides by the sample standard deviation.

    Either centering or rescaling or both can be disabled by use of keyword
    arguments. The `ddof` argument controls the delta degrees of freedom when
    computing the standard deviation (cf. :func:`numpy.std`). The default of
    ``ddof=0`` produces the maximum likelihood estimate; use ``ddof=1`` if you
    prefer the square root of the unbiased estimate of the variance.

    If input has multiple columns, standardizes each column separately.

    .. note:: This function computes the mean and standard deviation using a
       memory-efficient online algorithm, making it suitable for use with
       large incrementally processed data-sets.
    """
    current_n: int
    current_mean: Incomplete
    current_M2: Incomplete
    def __init__(self) -> None: ...
    def memorize_chunk(self, x, center: bool = True, rescale: bool = True, ddof: int = 0) -> None: ...
    def memorize_finish(self) -> None: ...
    def transform(self, x, center: bool = True, rescale: bool = True, ddof: int = 0): ...

standardize: Incomplete
scale = standardize
