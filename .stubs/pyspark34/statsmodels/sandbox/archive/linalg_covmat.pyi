from .linalg_decomp_1 import SvdArray as SvdArray
from _typeshed import Incomplete

sqrt2pi: Incomplete
logsqrt2pi: Incomplete

class StandardNormal:
    """Distribution of vector x, with independent distribution N(0,1)

    this is the same as univariate normal for pdf and logpdf

    other methods not checked/adjusted yet

    """
    def rvs(self, size): ...
    def pdf(self, x): ...
    def logpdf(self, x): ...

class AffineTransform:
    """affine full rank transformation of a multivariate distribution

    no dimension checking, assumes everything broadcasts correctly
    first version without bound support

    provides distribution of y given distribution of x
    y = const + tmat * x

    """
    const: Incomplete
    tmat: Incomplete
    dist: Incomplete
    nrv: Incomplete
    tmatinv: Incomplete
    absdet: Incomplete
    logabsdet: Incomplete
    def __init__(self, const, tmat, dist) -> None: ...
    def rvs(self, size): ...
    def transform(self, x): ...
    def invtransform(self, y): ...
    def pdf(self, x): ...
    def logpdf(self, x): ...

class MultivariateNormalChol:
    """multivariate normal distribution with cholesky decomposition of sigma

    ignoring mean at the beginning, maybe

    needs testing for broadcasting to contemporaneously but not intertemporaly
    correlated random variable, which axis?,
    maybe swapaxis or rollaxis if x.ndim != mean.ndim == (sigma.ndim - 1)

    initially 1d is ok, 2d should work with iid in axis 0 and mvn in axis 1

    """
    mean: Incomplete
    sigma: Incomplete
    sigmainv: Incomplete
    cholsigma: Incomplete
    cholsigmainv: Incomplete
    def __init__(self, mean, sigma) -> None: ...
    def whiten(self, x): ...
    def logpdf_obs(self, x): ...
    def logpdf(self, x): ...
    def pdf(self, x): ...

class MultivariateNormal:
    mean: Incomplete
    sigma: Incomplete
    def __init__(self, mean, sigma) -> None: ...

def loglike_ar1(x, rho):
    """loglikelihood of AR(1) process, as a test case

    sigma_u partially hard coded

    Greene chapter 12 eq. (12-31)
    """
def ar2transform(x, arcoefs):
    """

    (Greene eq 12-30)
    """
def mvn_loglike(x, sigma):
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

nobs: int
x: Incomplete
autocov: Incomplete
sigma: Incomplete
cholsigma: Incomplete
sigmainv: Incomplete
cholsigmainv: Incomplete
x_whitened: Incomplete
logdetsigma: Incomplete
sigma2: float
llike: Incomplete
ll: Incomplete
ls: Incomplete
normtransf: Incomplete
mch: Incomplete
xw: Incomplete
