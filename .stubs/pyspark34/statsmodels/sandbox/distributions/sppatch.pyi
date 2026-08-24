from _typeshed import Incomplete
from statsmodels.compat.python import lmap as lmap

def nnlf_fr(self, thetash, x, frmask): ...
def fit_fr(self, data, *args, **kwds):
    """estimate distribution parameters by MLE taking some parameters as fixed

    Parameters
    ----------
    data : ndarray, 1d
        data for which the distribution parameters are estimated,
    args : list ? check
        starting values for optimization
    kwds :

      - 'frozen' : array_like
           values for frozen distribution parameters and, for elements with
           np.nan, the corresponding parameter will be estimated

    Returns
    -------
    argest : ndarray
        estimated parameters


    Examples
    --------
    generate random sample
    >>> np.random.seed(12345)
    >>> x = stats.gamma.rvs(2.5, loc=0, scale=1.2, size=200)

    estimate all parameters
    >>> stats.gamma.fit(x)
    array([ 2.0243194 ,  0.20395655,  1.44411371])
    >>> stats.gamma.fit_fr(x, frozen=[np.nan, np.nan, np.nan])
    array([ 2.0243194 ,  0.20395655,  1.44411371])

    keep loc fixed, estimate shape and scale parameters
    >>> stats.gamma.fit_fr(x, frozen=[np.nan, 0.0, np.nan])
    array([ 2.45603985,  1.27333105])

    keep loc and scale fixed, estimate shape parameter
    >>> stats.gamma.fit_fr(x, frozen=[np.nan, 0.0, 1.0])
    array([ 3.00048828])
    >>> stats.gamma.fit_fr(x, frozen=[np.nan, 0.0, 1.2])
    array([ 2.57792969])

    estimate only scale parameter for fixed shape and loc
    >>> stats.gamma.fit_fr(x, frozen=[2.5, 0.0, np.nan])
    array([ 1.25087891])

    Notes
    -----
    self is an instance of a distribution class. This can be attached to
    scipy.stats.distributions.rv_continuous

    *Todo*

    * check if docstring is correct
    * more input checking, args is list ? might also apply to current fit method

    """
def expect(self, fn: Incomplete | None = None, args=(), loc: int = 0, scale: int = 1, lb: Incomplete | None = None, ub: Incomplete | None = None, conditional: bool = False):
    """calculate expected value of a function with respect to the distribution

    location and scale only tested on a few examples

    Parameters
    ----------
        all parameters are keyword parameters
        fn : function (default: identity mapping)
           Function for which integral is calculated. Takes only one argument.
        args : tuple
           argument (parameters) of the distribution
        lb, ub : numbers
           lower and upper bound for integration, default is set to the support
           of the distribution
        conditional : bool (False)
           If true then the integral is corrected by the conditional probability
           of the integration interval. The return value is the expectation
           of the function, conditional on being in the given interval.

    Returns
    -------
        expected value : float

    Notes
    -----
    This function has not been checked for it's behavior when the integral is
    not finite. The integration behavior is inherited from scipy.integrate.quad.

    """
def expect_v2(self, fn: Incomplete | None = None, args=(), loc: int = 0, scale: int = 1, lb: Incomplete | None = None, ub: Incomplete | None = None, conditional: bool = False):
    """calculate expected value of a function with respect to the distribution

    location and scale only tested on a few examples

    Parameters
    ----------
        all parameters are keyword parameters
        fn : function (default: identity mapping)
           Function for which integral is calculated. Takes only one argument.
        args : tuple
           argument (parameters) of the distribution
        lb, ub : numbers
           lower and upper bound for integration, default is set using
           quantiles of the distribution, see Notes
        conditional : bool (False)
           If true then the integral is corrected by the conditional probability
           of the integration interval. The return value is the expectation
           of the function, conditional on being in the given interval.

    Returns
    -------
        expected value : float

    Notes
    -----
    This function has not been checked for it's behavior when the integral is
    not finite. The integration behavior is inherited from scipy.integrate.quad.

    The default limits are lb = self.ppf(1e-9, *args), ub = self.ppf(1-1e-9, *args)

    For some heavy tailed distributions, 'alpha', 'cauchy', 'halfcauchy',
    'levy', 'levy_l', and for 'ncf', the default limits are not set correctly
    even  when the expectation of the function is finite. In this case, the
    integration limits, lb and ub, should be chosen by the user. For example,
    for the ncf distribution, ub=1000 works in the examples.

    There are also problems with numerical integration in some other cases,
    for example if the distribution is very concentrated and the default limits
    are too large.

    """
def expect_discrete(self, fn: Incomplete | None = None, args=(), loc: int = 0, lb: Incomplete | None = None, ub: Incomplete | None = None, conditional: bool = False):
    """calculate expected value of a function with respect to the distribution
    for discrete distribution

    Parameters
    ----------
        (self : distribution instance as defined in scipy stats)
        fn : function (default: identity mapping)
           Function for which integral is calculated. Takes only one argument.
        args : tuple
           argument (parameters) of the distribution
        optional keyword parameters
        lb, ub : numbers
           lower and upper bound for integration, default is set to the support
           of the distribution, lb and ub are inclusive (ul<=k<=ub)
        conditional : bool (False)
           If true then the expectation is corrected by the conditional
           probability of the integration interval. The return value is the
           expectation of the function, conditional on being in the given
           interval (k such that ul<=k<=ub).

    Returns
    -------
        expected value : float

    Notes
    -----
    * function is not vectorized
    * accuracy: uses self.moment_tol as stopping criterium
        for heavy tailed distribution e.g. zipf(4), accuracy for
        mean, variance in example is only 1e-5,
        increasing precision (moment_tol) makes zipf very slow
    * suppnmin=100 internal parameter for minimum number of points to evaluate
        could be added as keyword parameter, to evaluate functions with
        non-monotonic shapes, points include integers in (-suppnmin, suppnmin)
    * uses maxcount=1000 limits the number of points that are evaluated
        to break loop for infinite sums
        (a maximum of suppnmin+1000 positive plus suppnmin+1000 negative integers
        are evaluated)


    """
def distfitbootstrap(sample, distr, nrepl: int = 100):
    """run bootstrap for estimation of distribution parameters

    hard coded: only one shape parameter is allowed and estimated,
        loc=0 and scale=1 are fixed in the estimation

    Parameters
    ----------
    sample : ndarray
        original sample data for bootstrap
    distr : distribution instance with fit_fr method
    nrepl : int
        number of bootstrap replications

    Returns
    -------
    res : array (nrepl,)
        parameter estimates for all bootstrap replications

    """
def distfitmc(sample, distr, nrepl: int = 100, distkwds={}):
    """run Monte Carlo for estimation of distribution parameters

    hard coded: only one shape parameter is allowed and estimated,
        loc=0 and scale=1 are fixed in the estimation

    Parameters
    ----------
    sample : ndarray
        original sample data, in Monte Carlo only used to get nobs,
    distr : distribution instance with fit_fr method
    nrepl : int
        number of Monte Carlo replications

    Returns
    -------
    res : array (nrepl,)
        parameter estimates for all Monte Carlo replications

    """
def printresults(sample, arg, bres, kind: str = 'bootstrap') -> None:
    """calculate and print(Bootstrap or Monte Carlo result

    Parameters
    ----------
    sample : ndarray
        original sample data
    arg : float   (for general case will be array)
    bres : ndarray
        parameter estimates from Bootstrap or Monte Carlo run
    kind : {'bootstrap', 'montecarlo'}
        output is printed for Mootstrap (default) or Monte Carlo

    Returns
    -------
    None, currently only printing

    Notes
    -----
    still a bit a mess because it is used for both Bootstrap and Monte Carlo

    made correction:
        reference point for bootstrap is estimated parameter

    not clear:
        I'm not doing any ddof adjustment in estimation of variance, do we
        need ddof>0 ?

    todo: return results and string instead of printing

    """
