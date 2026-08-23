from .extras import mvstdnormcdf as mvstdnormcdf
from _typeshed import Incomplete

def chi2_pdf(self, x, df):
    """pdf of chi-square distribution"""
def chi_pdf(x, df): ...
def chi_logpdf(x, df): ...
def funbgh(s, a, b, R, df): ...
def funbgh2(s, a, b, R, df): ...
def bghfactor(df): ...
def mvstdtprob(a, b, R, df, ieps: float = 1e-05, quadkwds: Incomplete | None = None, mvstkwds: Incomplete | None = None):
    """
    Probability of rectangular area of standard t distribution

    assumes mean is zero and R is correlation matrix

    Notes
    -----
    This function does not calculate the estimate of the combined error
    between the underlying multivariate normal probability calculations
    and the integration.
    """
def multivariate_t_rvs(m, S, df=..., n: int = 1):
    """generate random variables of multivariate t distribution

    Parameters
    ----------
    m : array_like
        mean of random variable, length determines dimension of random variable
    S : array_like
        square array of covariance  matrix
    df : int or float
        degrees of freedom
    n : int
        number of observations, return random array will be (n, len(m))

    Returns
    -------
    rvs : ndarray, (n, len(m))
        each row is an independent draw of a multivariate t distributed
        random variable


    """
