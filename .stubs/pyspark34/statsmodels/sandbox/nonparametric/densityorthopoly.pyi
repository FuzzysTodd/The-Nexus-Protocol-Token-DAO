from _typeshed import Incomplete

sqr2: Incomplete

class FPoly:
    """Orthonormal (for weight=1) Fourier Polynomial on [0,1]

    orthonormal polynomial but density needs corfactor that I do not see what
    it is analytically

    parameterization on [0,1] from

    Sam Efromovich: Orthogonal series density estimation,
    2010 John Wiley & Sons, Inc. WIREs Comp Stat 2010 2 467-476


    """
    order: Incomplete
    domain: Incomplete
    intdomain: Incomplete
    def __init__(self, order) -> None: ...
    def __call__(self, x): ...

class F2Poly:
    """Orthogonal (for weight=1) Fourier Polynomial on [0,pi]

    is orthogonal but first component does not square-integrate to 1
    final result seems to need a correction factor of sqrt(pi)
    _corfactor = sqrt(pi) from integrating the density

    Parameterization on [0, pi] from

    Peter Hall, Cross-Validation and the Smoothing of Orthogonal Series Density
    Estimators, JOURNAL OF MULTIVARIATE ANALYSIS 21, 189-206 (1987)

    """
    order: Incomplete
    domain: Incomplete
    intdomain: Incomplete
    offsetfactor: int
    def __init__(self, order) -> None: ...
    def __call__(self, x): ...

class ChebyTPoly:
    """Orthonormal (for weight=1) Chebychev Polynomial on (-1,1)


    Notes
    -----
    integration requires to stay away from boundary, offsetfactor > 0
    maybe this implies that we cannot use it for densities that are > 0 at
    boundary ???

    or maybe there is a mistake close to the boundary, sometimes integration works.

    """
    order: Incomplete
    poly: Incomplete
    domain: Incomplete
    intdomain: Incomplete
    offsetfactor: float
    def __init__(self, order) -> None: ...
    def __call__(self, x): ...

logpi2: Incomplete

class HPoly:
    """Orthonormal (for weight=1) Hermite Polynomial, uses finite bounds

    for current use with DensityOrthoPoly domain is defined as [-6,6]

    """
    order: Incomplete
    poly: Incomplete
    domain: Incomplete
    offsetfactor: float
    def __init__(self, order) -> None: ...
    def __call__(self, x): ...

def polyvander(x, polybase, order: int = 5): ...
def inner_cont(polys, lower, upper, weight: Incomplete | None = None):
    """inner product of continuous function (with weight=1)

    Parameters
    ----------
    polys : list of callables
        polynomial instances
    lower : float
        lower integration limit
    upper : float
        upper integration limit
    weight : callable or None
        weighting function

    Returns
    -------
    innp : ndarray
        symmetric 2d square array with innerproduct of all function pairs
    err : ndarray
        numerical error estimate from scipy.integrate.quad, same dimension as innp

    Examples
    --------
    >>> from scipy.special import chebyt
    >>> polys = [chebyt(i) for i in range(4)]
    >>> r, e = inner_cont(polys, -1, 1)
    >>> r
    array([[ 2.        ,  0.        , -0.66666667,  0.        ],
           [ 0.        ,  0.66666667,  0.        , -0.4       ],
           [-0.66666667,  0.        ,  0.93333333,  0.        ],
           [ 0.        , -0.4       ,  0.        ,  0.97142857]])

    """
def is_orthonormal_cont(polys, lower, upper, rtol: int = 0, atol: float = 1e-08):
    """check whether functions are orthonormal

    Parameters
    ----------
    polys : list of polynomials or function

    Returns
    -------
    is_orthonormal : bool
        is False if the innerproducts are not close to 0 or 1

    Notes
    -----
    this stops as soon as the first deviation from orthonormality is found.

    Examples
    --------
    >>> from scipy.special import chebyt
    >>> polys = [chebyt(i) for i in range(4)]
    >>> r, e = inner_cont(polys, -1, 1)
    >>> r
    array([[ 2.        ,  0.        , -0.66666667,  0.        ],
           [ 0.        ,  0.66666667,  0.        , -0.4       ],
           [-0.66666667,  0.        ,  0.93333333,  0.        ],
           [ 0.        , -0.4       ,  0.        ,  0.97142857]])
    >>> is_orthonormal_cont(polys, -1, 1, atol=1e-6)
    False

    >>> polys = [ChebyTPoly(i) for i in range(4)]
    >>> r, e = inner_cont(polys, -1, 1)
    >>> r
    array([[  1.00000000e+00,   0.00000000e+00,  -9.31270888e-14,
              0.00000000e+00],
           [  0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
             -9.47850712e-15],
           [ -9.31270888e-14,   0.00000000e+00,   1.00000000e+00,
              0.00000000e+00],
           [  0.00000000e+00,  -9.47850712e-15,   0.00000000e+00,
              1.00000000e+00]])
    >>> is_orthonormal_cont(polys, -1, 1, atol=1e-6)
    True

    """

class DensityOrthoPoly:
    """Univariate density estimation by orthonormal series expansion


    Uses an orthonormal polynomial basis to approximate a univariate density.


    currently all arguments can be given to fit, I might change it to requiring
    arguments in __init__ instead.
    """
    polybase: Incomplete
    polys: Incomplete
    def __init__(self, polybase: Incomplete | None = None, order: int = 5) -> None: ...
    offsetfac: Incomplete
    offset: Incomplete
    shrink: Incomplete
    shift: Incomplete
    x: Incomplete
    coeffs: Incomplete
    def fit(self, x, polybase: Incomplete | None = None, order: int = 5, limits: Incomplete | None = None):
        """estimate the orthogonal polynomial approximation to the density

        """
    def evaluate(self, xeval, order: Incomplete | None = None): ...
    def __call__(self, xeval):
        """alias for evaluate, except no order argument"""

def density_orthopoly(x, polybase, order: int = 5, xeval: Incomplete | None = None): ...
