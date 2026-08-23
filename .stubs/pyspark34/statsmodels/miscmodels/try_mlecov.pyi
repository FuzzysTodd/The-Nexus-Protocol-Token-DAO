from statsmodels.base.model import GenericLikelihoodModel as GenericLikelihoodModel
from statsmodels.datasets import sunspots as sunspots
from statsmodels.tsa.arima_process import ArmaProcess as ArmaProcess, arma_acovf as arma_acovf, arma_generate_sample as arma_generate_sample

def mvn_loglike_sum(x, sigma):
    """loglike multivariate normal

    copied from GLS and adjusted names
    not sure why this differes from mvn_loglike
    """
def mvn_loglike(x, sigma):
    """loglike multivariate normal

    assumes x is 1d, (nobs,) and sigma is 2d (nobs, nobs)

    brute force from formula
    no checking of correct inputs
    use of inv and log-det should be replace with something more efficient
    """
def mvn_loglike_chol(x, sigma):
    """loglike multivariate normal

    assumes x is 1d, (nobs,) and sigma is 2d (nobs, nobs)

    brute force from formula
    no checking of correct inputs
    use of inv and log-det should be replace with something more efficient
    """
def mvn_nloglike_obs(x, sigma):
    """loglike multivariate normal

    assumes x is 1d, (nobs,) and sigma is 2d (nobs, nobs)

    brute force from formula
    no checking of correct inputs
    use of inv and log-det should be replace with something more efficient
    """
def invertibleroots(ma): ...
def getpoly(self, params): ...

class MLEGLS(GenericLikelihoodModel):
    """ARMA model with exact loglikelhood for short time series

    Inverts (nobs, nobs) matrix, use only for nobs <= 200 or so.

    This class is a pattern for small sample GLS-like models. Intended use
    for loglikelihood of initial observations for ARMA.



    TODO:
    This might be missing the error variance. Does it assume error is
       distributed N(0,1)
    Maybe extend to mean handling, or assume it is already removed.
    """
    def loglike(self, params): ...
    def fit_invertible(self, *args, **kwds): ...
