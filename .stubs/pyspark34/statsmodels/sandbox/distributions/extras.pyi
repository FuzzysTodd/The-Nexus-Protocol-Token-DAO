from _typeshed import Incomplete
from scipy.stats import distributions
from statsmodels.stats.moment_helpers import mc2mvsk as mc2mvsk, mvsk2mc as mvsk2mc

class SkewNorm_gen(distributions.rv_continuous):
    """univariate Skew-Normal distribution of Azzalini

    class follows scipy.stats.distributions pattern
    but with __init__


    """
    def __init__(self) -> None: ...

skewnorm: Incomplete

class SkewNorm2_gen(distributions.rv_continuous):
    """univariate Skew-Normal distribution of Azzalini

    class follows scipy.stats.distributions pattern

    """

skewnorm2: Incomplete

class ACSkewT_gen(distributions.rv_continuous):
    """univariate Skew-T distribution of Azzalini

    class follows scipy.stats.distributions pattern
    but with __init__
    """
    def __init__(self) -> None: ...

def pdf_moments_st(cnt):
    """Return the Gaussian expanded pdf function given the list of central
    moments (first one is mean).

    version of scipy.stats, any changes ?
    the scipy.stats version has a bug and returns normal distribution
    """
def pdf_mvsk(mvsk):
    """Return the Gaussian expanded pdf function given the list of 1st, 2nd
    moment and skew and Fisher (excess) kurtosis.



    Parameters
    ----------
    mvsk : list of mu, mc2, skew, kurt
        distribution is matched to these four moments

    Returns
    -------
    pdffunc : function
        function that evaluates the pdf(x), where x is the non-standardized
        random variable.


    Notes
    -----

    Changed so it works only if four arguments are given. Uses explicit
    formula, not loop.

    This implements a Gram-Charlier expansion of the normal distribution
    where the first 2 moments coincide with those of the normal distribution
    but skew and kurtosis can deviate from it.

    In the Gram-Charlier distribution it is possible that the density
    becomes negative. This is the case when the deviation from the
    normal distribution is too large.



    References
    ----------
    https://en.wikipedia.org/wiki/Edgeworth_series
    Johnson N.L., S. Kotz, N. Balakrishnan: Continuous Univariate
    Distributions, Volume 1, 2nd ed., p.30
    """
def pdf_moments(cnt):
    """Return the Gaussian expanded pdf function given the list of central
    moments (first one is mean).

    Changed so it works only if four arguments are given. Uses explicit
    formula, not loop.

    Notes
    -----

    This implements a Gram-Charlier expansion of the normal distribution
    where the first 2 moments coincide with those of the normal distribution
    but skew and kurtosis can deviate from it.

    In the Gram-Charlier distribution it is possible that the density
    becomes negative. This is the case when the deviation from the
    normal distribution is too large.



    References
    ----------
    https://en.wikipedia.org/wiki/Edgeworth_series
    Johnson N.L., S. Kotz, N. Balakrishnan: Continuous Univariate
    Distributions, Volume 1, 2nd ed., p.30
    """

class NormExpan_gen(distributions.rv_continuous):
    """Gram-Charlier Expansion of Normal distribution

    class follows scipy.stats.distributions pattern
    but with __init__

    """
    mvsk: Incomplete
    cnt: Incomplete
    def __init__(self, args, **kwds) -> None: ...

def get_u_argskwargs(**kwargs): ...

class Transf_gen(distributions.rv_continuous):
    """a class for non-linear monotonic transformation of a continuous random variable

    """
    func: Incomplete
    funcinv: Incomplete
    numargs: Incomplete
    decr: Incomplete
    kls: Incomplete
    def __init__(self, kls, func, funcinv, *args, **kwargs) -> None: ...

def inverse(x): ...

mux: Incomplete
stdx: Incomplete

def inversew(x): ...
def inversew_inv(x): ...
def identit(x): ...

invdnormalg: Incomplete
lognormalg: Incomplete
loggammaexpg: Incomplete

class ExpTransf_gen(distributions.rv_continuous):
    """Distribution based on log/exp transformation

    the constructor can be called with a distribution class
    and generates the distribution of the transformed random variable

    """
    numargs: Incomplete
    kls: Incomplete
    def __init__(self, kls, *args, **kwargs) -> None: ...

class LogTransf_gen(distributions.rv_continuous):
    """Distribution based on log/exp transformation

    the constructor can be called with a distribution class
    and generates the distribution of the transformed random variable

    """
    numargs: Incomplete
    kls: Incomplete
    def __init__(self, kls, *args, **kwargs) -> None: ...

class TransfTwo_gen(distributions.rv_continuous):
    """Distribution based on a non-monotonic (u- or hump-shaped transformation)

    the constructor can be called with a distribution class, and functions
    that define the non-linear transformation.
    and generates the distribution of the transformed random variable

    Note: the transformation, it's inverse and derivatives need to be fully
    specified: func, funcinvplus, funcinvminus, derivplus,  derivminus.
    Currently no numerical derivatives or inverse are calculated

    This can be used to generate distribution instances similar to the
    distributions in scipy.stats.

    """
    func: Incomplete
    funcinvplus: Incomplete
    funcinvminus: Incomplete
    derivplus: Incomplete
    derivminus: Incomplete
    numargs: Incomplete
    shape: Incomplete
    kls: Incomplete
    def __init__(self, kls, func, funcinvplus, funcinvminus, derivplus, derivminus, *args, **kwargs) -> None: ...

class SquareFunc:
    """class to hold quadratic function with inverse function and derivative

    using instance methods instead of class methods, if we want extension
    to parametrized function
    """
    def inverseplus(self, x): ...
    def inverseminus(self, x): ...
    def derivplus(self, x): ...
    def derivminus(self, x): ...
    def squarefunc(self, x): ...

sqfunc: Incomplete
squarenormalg: Incomplete
squaretg: Incomplete

def inverseplus(x): ...
def inverseminus(x): ...
def derivplus(x): ...
def derivminus(x): ...
def negsquarefunc(x): ...

negsquarenormalg: Incomplete

def absfunc(x): ...

absnormalg: Incomplete
informcode: Incomplete

def mvstdnormcdf(lower, upper, corrcoef, **kwds):
    """standardized multivariate normal cumulative distribution function

    This is a wrapper for scipy.stats._mvn.mvndst which calculates
    a rectangular integral over a standardized multivariate normal
    distribution.

    This function assumes standardized scale, that is the variance in each dimension
    is one, but correlation can be arbitrary, covariance = correlation matrix

    Parameters
    ----------
    lower, upper : array_like, 1d
       lower and upper integration limits with length equal to the number
       of dimensions of the multivariate normal distribution. It can contain
       -np.inf or np.inf for open integration intervals
    corrcoef : float or array_like
       specifies correlation matrix in one of three ways, see notes
    optional keyword parameters to influence integration
        * maxpts : int, maximum number of function values allowed. This
             parameter can be used to limit the time. A sensible
             strategy is to start with `maxpts` = 1000*N, and then
             increase `maxpts` if ERROR is too large.
        * abseps : float absolute error tolerance.
        * releps : float relative error tolerance.

    Returns
    -------
    cdfvalue : float
        value of the integral


    Notes
    -----
    The correlation matrix corrcoef can be given in 3 different ways
    If the multivariate normal is two-dimensional than only the
    correlation coefficient needs to be provided.
    For general dimension the correlation matrix can be provided either
    as a one-dimensional array of the upper triangular correlation
    coefficients stacked by rows, or as full square correlation matrix

    See Also
    --------
    mvnormcdf : cdf of multivariate normal distribution without
        standardization

    Examples
    --------

    >>> print(mvstdnormcdf([-np.inf,-np.inf], [0.0,np.inf], 0.5))
    0.5
    >>> corr = [[1.0, 0, 0.5],[0,1,0],[0.5,0,1]]
    >>> print(mvstdnormcdf([-np.inf,-np.inf,-100.0], [0.0,0.0,0.0], corr, abseps=1e-6))
    0.166666399198
    >>> print(mvstdnormcdf([-np.inf,-np.inf,-100.0],[0.0,0.0,0.0],corr, abseps=1e-8))
    something wrong completion with ERROR > EPS and MAXPTS function values used;
                        increase MAXPTS to decrease ERROR; 1.048330348e-006
    0.166666546218
    >>> print(mvstdnormcdf([-np.inf,-np.inf,-100.0],[0.0,0.0,0.0], corr,                             maxpts=100000, abseps=1e-8))
    0.166666588293

    """
def mvnormcdf(upper, mu, cov, lower: Incomplete | None = None, **kwds):
    """multivariate normal cumulative distribution function

    This is a wrapper for scipy.stats._mvn.mvndst which calculates
    a rectangular integral over a multivariate normal distribution.

    Parameters
    ----------
    lower, upper : array_like, 1d
       lower and upper integration limits with length equal to the number
       of dimensions of the multivariate normal distribution. It can contain
       -np.inf or np.inf for open integration intervals
    mu : array_lik, 1d
       list or array of means
    cov : array_like, 2d
       specifies covariance matrix
    optional keyword parameters to influence integration
        * maxpts : int, maximum number of function values allowed. This
             parameter can be used to limit the time. A sensible
             strategy is to start with `maxpts` = 1000*N, and then
             increase `maxpts` if ERROR is too large.
        * abseps : float absolute error tolerance.
        * releps : float relative error tolerance.

    Returns
    -------
    cdfvalue : float
        value of the integral


    Notes
    -----
    This function normalizes the location and scale of the multivariate
    normal distribution and then uses `mvstdnormcdf` to call the integration.

    See Also
    --------
    mvstdnormcdf : location and scale standardized multivariate normal cdf
    """
