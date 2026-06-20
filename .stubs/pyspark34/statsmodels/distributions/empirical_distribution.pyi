from _typeshed import Incomplete

class StepFunction:
    """
    A basic step function.

    Values at the ends are handled in the simplest way possible:
    everything to the left of x[0] is set to ival; everything
    to the right of x[-1] is set to y[-1].

    Parameters
    ----------
    x : array_like
    y : array_like
    ival : float
        ival is the value given to the values to the left of x[0]. Default
        is 0.
    sorted : bool
        Default is False.
    side : {'left', 'right'}, optional
        Default is 'left'. Defines the shape of the intervals constituting the
        steps. 'right' correspond to [a, b) intervals and 'left' to (a, b].

    Examples
    --------
    >>> import numpy as np
    >>> from statsmodels.distributions.empirical_distribution import (
    >>>     StepFunction)
    >>>
    >>> x = np.arange(20)
    >>> y = np.arange(20)
    >>> f = StepFunction(x, y)
    >>>
    >>> print(f(3.2))
    3.0
    >>> print(f([[3.2,4.5],[24,-3.1]]))
    [[  3.   4.]
     [ 19.   0.]]
    >>> f2 = StepFunction(x, y, side='right')
    >>>
    >>> print(f(3.0))
    2.0
    >>> print(f2(3.0))
    3.0
    """
    side: Incomplete
    x: Incomplete
    y: Incomplete
    n: Incomplete
    def __init__(self, x, y, ival: float = 0.0, sorted: bool = False, side: str = 'left') -> None: ...
    def __call__(self, time): ...

class ECDF(StepFunction):
    """
    Return the Empirical CDF of an array as a step function.

    Parameters
    ----------
    x : array_like
        Observations
    side : {'left', 'right'}, optional
        Default is 'right'. Defines the shape of the intervals constituting the
        steps. 'right' correspond to [a, b) intervals and 'left' to (a, b].

    Returns
    -------
    Empirical CDF as a step function.

    Examples
    --------
    >>> import numpy as np
    >>> from statsmodels.distributions.empirical_distribution import ECDF
    >>>
    >>> ecdf = ECDF([3, 3, 1, 4])
    >>>
    >>> ecdf([3, 55, 0.5, 1.5])
    array([ 0.75,  1.  ,  0.  ,  0.25])
    """
    def __init__(self, x, side: str = 'right') -> None: ...

class ECDFDiscrete(StepFunction):
    """
    Return the Empirical Weighted CDF of an array as a step function.

    Parameters
    ----------
    x : array_like
        Data values. If freq_weights is None, then x is treated as observations
        and the ecdf is computed from the frequency counts of unique values
        using nunpy.unique.
        If freq_weights is not None, then x will be taken as the support of the
        mass point distribution with freq_weights as counts for x values.
        The x values can be arbitrary sortable values and need not be integers.
    freq_weights : array_like
        Weights of the observations.  sum(freq_weights) is interpreted as nobs
        for confint.
        If freq_weights is None, then the frequency counts for unique values
        will be computed from the data x.
    side : {'left', 'right'}, optional
        Default is 'right'. Defines the shape of the intervals constituting the
        steps. 'right' correspond to [a, b) intervals and 'left' to (a, b].

    Returns
    -------
    Weighted ECDF as a step function.

    Examples
    --------
    >>> import numpy as np
    >>> from statsmodels.distributions.empirical_distribution import (
    >>>     ECDFDiscrete)
    >>>
    >>> ewcdf = ECDFDiscrete([3, 3, 1, 4])
    >>> ewcdf([3, 55, 0.5, 1.5])
    array([0.75, 1.  , 0.  , 0.25])
    >>>
    >>> ewcdf = ECDFDiscrete([3, 1, 4], [1.25, 2.5, 5])
    >>>
    >>> ewcdf([3, 55, 0.5, 1.5])
    array([0.42857143, 1., 0. , 0.28571429])
    >>> print('e1 and e2 are equivalent ways of defining the same ECDF')
    e1 and e2 are equivalent ways of defining the same ECDF
    >>> e1 = ECDFDiscrete([3.5, 3.5, 1.5, 1, 4])
    >>> e2 = ECDFDiscrete([3.5, 1.5, 1, 4], freq_weights=[2, 1, 1, 1])
    >>> print(e1.x, e2.x)
    [-inf  1.   1.5  3.5  4. ] [-inf  1.   1.5  3.5  4. ]
    >>> print(e1.y, e2.y)
    [0.  0.2 0.4 0.8 1. ] [0.  0.2 0.4 0.8 1. ]
    """
    def __init__(self, x, freq_weights: Incomplete | None = None, side: str = 'right') -> None: ...

def monotone_fn_inverter(fn, x, vectorized: bool = True, **keywords):
    """
    Given a monotone function fn (no checking is done to verify monotonicity)
    and a set of x values, return an linearly interpolated approximation
    to its inverse from its values on x.
    """
