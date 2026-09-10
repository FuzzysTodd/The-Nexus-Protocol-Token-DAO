from _typeshed import Incomplete
from statsmodels.regression.linear_model import yule_walker as yule_walker
from statsmodels.stats.moment_helpers import cov2corr as cov2corr

def corr_equi(k_vars, rho):
    """create equicorrelated correlation matrix with rho on off diagonal

    Parameters
    ----------
    k_vars : int
        number of variables, correlation matrix will be (k_vars, k_vars)
    rho : float
        correlation between any two random variables

    Returns
    -------
    corr : ndarray (k_vars, k_vars)
        correlation matrix

    """
def corr_ar(k_vars, ar):
    """create autoregressive correlation matrix

    This might be MA, not AR, process if used for residual process - check

    Parameters
    ----------
    ar : array_like, 1d
        AR lag-polynomial including 1 for lag 0


    """
def corr_arma(k_vars, ar, ma):
    """create arma correlation matrix

    converts arma to autoregressive lag-polynomial with k_var lags

    ar and arma might need to be switched for generating residual process

    Parameters
    ----------
    ar : array_like, 1d
        AR lag-polynomial including 1 for lag 0
    ma : array_like, 1d
        MA lag-polynomial

    """
def corr2cov(corr, std):
    """convert correlation matrix to covariance matrix

    Parameters
    ----------
    corr : ndarray, (k_vars, k_vars)
        correlation matrix
    std : ndarray, (k_vars,) or scalar
        standard deviation for the vector of random variables. If scalar, then
        it is assumed that all variables have the same scale given by std.

    """
def whiten_ar(x, ar_coefs, order):
    """
    Whiten a series of columns according to an AR(p) covariance structure.

    This drops the initial conditions (Cochran-Orcut ?)
    Uses loop, so for short ar polynomials only, use lfilter otherwise

    This needs to improve, option on method, full additional to conditional

    Parameters
    ----------
    x : array_like, (nobs,) or (nobs, k_vars)
        The data to be whitened along axis 0
    ar_coefs : ndarray
        coefficients of AR lag- polynomial,   TODO: ar or ar_coefs?
    order : int

    Returns
    -------
    x_new : ndarray
        transformed array
    """
def yule_walker_acov(acov, order: int = 1, method: str = 'unbiased', df: Incomplete | None = None, inv: bool = False):
    """
    Estimate AR(p) parameters from acovf using Yule-Walker equation.


    Parameters
    ----------
    acov : array_like, 1d
        auto-covariance
    order : int, optional
        The order of the autoregressive process.  Default is 1.
    inv : bool
        If inv is True the inverse of R is also returned.  Default is False.

    Returns
    -------
    rho : ndarray
        The estimated autoregressive coefficients
    sigma
        TODO
    Rinv : ndarray
        inverse of the Toepliz matrix
    """

class ARCovariance:
    """
    experimental class for Covariance of AR process
    classmethod? staticmethods?
    """
    ar: Incomplete
    ar_coefs: Incomplete
    k_lags: Incomplete
    arcoefs: Incomplete
    def __init__(self, ar: Incomplete | None = None, ar_coefs: Incomplete | None = None, sigma: float = 1.0) -> None: ...
    @classmethod
    def fit(cls, cov, order, **kwds): ...
    def whiten(self, x): ...
    def corr(self, k_vars: Incomplete | None = None): ...
    def cov(self, k_vars: Incomplete | None = None): ...
