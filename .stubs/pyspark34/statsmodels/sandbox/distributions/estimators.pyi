from _typeshed import Incomplete

cache: Incomplete

def gammamomentcond(distfn, params, mom2, quantile: Incomplete | None = None):
    """estimate distribution parameters based method of moments (mean,
    variance) for distributions with 1 shape parameter and fixed loc=0.

    Returns
    -------
    cond : function

    Notes
    -----
    first test version, quantile argument not used

    """
def gammamomentcond2(distfn, params, mom2, quantile: Incomplete | None = None):
    """estimate distribution parameters based method of moments (mean,
    variance) for distributions with 1 shape parameter and fixed loc=0.

    Returns
    -------
    difference : ndarray
        difference between theoretical and empirical moments

    Notes
    -----
    first test version, quantile argument not used

    The only difference to previous function is return type.

    """
def momentcondunbound(distfn, params, mom2, quantile: Incomplete | None = None):
    """moment conditions for estimating distribution parameters using method
    of moments, uses mean, variance and one quantile for distributions
    with 1 shape parameter.

    Returns
    -------
    difference : ndarray
        difference between theoretical and empirical moments and quantiles

    """
def momentcondunboundls(distfn, params, mom2, quantile: Incomplete | None = None, shape: Incomplete | None = None):
    """moment conditions for estimating loc and scale of a distribution
    with method of moments using either 2 quantiles or 2 moments (not both).

    Returns
    -------
    difference : ndarray
        difference between theoretical and empirical moments or quantiles

    """
def momentcondquant(distfn, params, mom2, quantile: Incomplete | None = None, shape: Incomplete | None = None):
    """moment conditions for estimating distribution parameters by matching
    quantiles, defines as many moment conditions as quantiles.

    Returns
    -------
    difference : ndarray
        difference between theoretical and empirical quantiles

    Notes
    -----
    This can be used for method of moments or for generalized method of
    moments.

    """
def fitquantilesgmm(distfn, x, start: Incomplete | None = None, pquant: Incomplete | None = None, frozen: Incomplete | None = None): ...
def fitbinned(distfn, freq, binedges, start, fixed: Incomplete | None = None):
    """estimate parameters of distribution function for binned data using MLE

    Parameters
    ----------
    distfn : distribution instance
        needs to have cdf method, as in scipy.stats
    freq : ndarray, 1d
        frequency count, e.g. obtained by histogram
    binedges : ndarray, 1d
        binedges including lower and upper bound
    start : tuple or array_like ?
        starting values, needs to have correct length

    Returns
    -------
    paramest : ndarray
        estimated parameters

    Notes
    -----
    todo: add fixed parameter option

    added factorial

    """
def fitbinnedgmm(distfn, freq, binedges, start, fixed: Incomplete | None = None, weightsoptimal: bool = True):
    """estimate parameters of distribution function for binned data using GMM

    Parameters
    ----------
    distfn : distribution instance
        needs to have cdf method, as in scipy.stats
    freq : ndarray, 1d
        frequency count, e.g. obtained by histogram
    binedges : ndarray, 1d
        binedges including lower and upper bound
    start : tuple or array_like ?
        starting values, needs to have correct length
    fixed : None
        not used yet
    weightsoptimal : bool
        If true, then the optimal weighting matrix for GMM is used. If false,
        then the identity matrix is used

    Returns
    -------
    paramest : ndarray
        estimated parameters

    Notes
    -----
    todo: add fixed parameter option

    added factorial

    """
def hess_ndt(fun, pars, args, options): ...
def logmps(params, xsorted, dist):
    """calculate negative log of Product-of-Spacings

    Parameters
    ----------
    params : array_like, tuple ?
        parameters of the distribution funciton
    xsorted : array_like
        data that is already sorted
    dist : instance of a distribution class
        only cdf method is used

    Returns
    -------
    mps : float
        negative log of Product-of-Spacings


    Notes
    -----
    MPS definiton from JKB page 233
    """
def getstartparams(dist, data):
    """get starting values for estimation of distribution parameters

    Parameters
    ----------
    dist : distribution instance
        the distribution instance needs to have either a method fitstart
        or an attribute numargs
    data : ndarray
        data for which preliminary estimator or starting value for
        parameter estimation is desired

    Returns
    -------
    x0 : ndarray
        preliminary estimate or starting value for the parameters of
        the distribution given the data, including loc and scale

    """
def fit_mps(dist, data, x0: Incomplete | None = None):
    """Estimate distribution parameters with Maximum Product-of-Spacings

    Parameters
    ----------
    params : array_like, tuple ?
        parameters of the distribution funciton
    xsorted : array_like
        data that is already sorted
    dist : instance of a distribution class
        only cdf method is used

    Returns
    -------
    x : ndarray
        estimates for the parameters of the distribution given the data,
        including loc and scale


    """
