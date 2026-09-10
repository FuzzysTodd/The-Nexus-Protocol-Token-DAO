from _typeshed import Incomplete
from statsmodels.distributions.copula.copulas import Copula as Copula
from statsmodels.tools.rng_qrng import check_random_state as check_random_state

class IndependenceCopula(Copula):
    """Independence copula.

    Copula with independent random variables.

    .. math::

        C_\theta(u,v) = uv

    Parameters
    ----------
    k_dim : int
        Dimension, number of components in the multivariate random variable.

    Notes
    -----
    IndependenceCopula does not have copula parameters.
    If non-empty ``args`` are provided in methods, then a ValueError is raised.
    The ``args`` keyword is provided for a consistent interface across
    copulas.

    """
    def __init__(self, k_dim: int = 2) -> None: ...
    def rvs(self, nobs: int = 1, args=(), random_state: Incomplete | None = None): ...
    def pdf(self, u, args=()): ...
    def cdf(self, u, args=()): ...
    def tau(self): ...
    def plot_pdf(self, *args) -> None: ...

def rvs_kernel(sample, size, bw: int = 1, k_func: Incomplete | None = None, return_extras: bool = False):
    """Random sampling from empirical copula using Beta distribution

    Parameters
    ----------
    sample : ndarray
        Sample of multivariate observations in (o, 1) interval.
    size : int
        Number of observations to simulate.
    bw : float
        Bandwidth for Beta sampling. The beta copula corresponds to a kernel
        estimate of the distribution. bw=1 corresponds to the empirical beta
        copula. A small bandwidth like bw=0.001 corresponds to small noise
        added to the empirical distribution. Larger bw, e.g. bw=10 corresponds
        to kernel estimate with more smoothing.
    k_func : None or callable
        The default kernel function is currently a beta function with 1 added
        to the first beta parameter.
    return_extras : bool
        If this is False, then only the random sample will be returned.
        If true, then extra information is returned that is mainly of interest
        for verification.

    Returns
    -------
    rvs : ndarray
        Multivariate sample with ``size`` observations drawn from the Beta
        Copula.

    Notes
    -----
    Status: experimental, API will change.
    """
