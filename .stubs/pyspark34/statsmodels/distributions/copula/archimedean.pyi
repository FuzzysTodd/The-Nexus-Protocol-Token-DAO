from . import transforms as transforms
from .copulas import Copula as Copula
from _typeshed import Incomplete
from statsmodels.tools.rng_qrng import check_random_state as check_random_state

def tau_frank(theta):
    """Kendall's tau for Frank Copula

    This uses Taylor series expansion for theta <= 1.

    Parameters
    ----------
    theta : float
        Parameter of the Frank copula. (not vectorized)

    Returns
    -------
    tau : float, tau for given theta
    """

class ArchimedeanCopula(Copula):
    """Base class for Archimedean copulas

    Parameters
    ----------
    transform : instance of transformation class
        Archimedean generator with required methods including first and second
        derivatives
    args : tuple
        Optional copula parameters. Copula parameters can be either provided
        when creating the instance or as arguments when calling methods.
    k_dim : int
        Dimension, number of components in the multivariate random variable.
        Currently only bivariate copulas are verified. Support for more than
        2 dimension is incomplete.
    """
    args: Incomplete
    transform: Incomplete
    k_args: int
    def __init__(self, transform, args=(), k_dim: int = 2) -> None: ...
    def cdf(self, u, args=()):
        """Evaluate cdf of Archimedean copula."""
    def pdf(self, u, args=()):
        """Evaluate pdf of Archimedean copula."""
    def logpdf(self, u, args=()):
        """Evaluate log pdf of multivariate Archimedean copula."""

class ClaytonCopula(ArchimedeanCopula):
    """Clayton copula.

    Dependence is greater in the negative tail than in the positive.

    .. math::

        C_\\theta(u,v) = \\left[ \\max\\left\\{ u^{-\\theta} + v^{-\\theta} -1 ;
        0 \\right\\} \\right]^{-1/\\theta}

    with :math:`\\theta\\in[-1,\\infty)\\backslash\\{0\\}`.

    """
    theta: Incomplete
    def __init__(self, theta: Incomplete | None = None, k_dim: int = 2) -> None: ...
    def rvs(self, nobs: int = 1, args=(), random_state: Incomplete | None = None): ...
    def pdf(self, u, args=()): ...
    def logpdf(self, u, args=()): ...
    def cdf(self, u, args=()): ...
    def tau(self, theta: Incomplete | None = None): ...
    def theta_from_tau(self, tau): ...

class FrankCopula(ArchimedeanCopula):
    """Frank copula.

    Dependence is symmetric.

    .. math::

        C_\\theta(\\mathbf{u}) = -\\frac{1}{\\theta} \\log \\left[ 1-
        \\frac{ \\prod_j (1-\\exp(- \\theta u_j)) }{ (1 - \\exp(-\\theta)-1)^{d -
        1} } \\right]

    with :math:`\\theta\\in \\mathbb{R}\\backslash\\{0\\}, \\mathbf{u} \\in [0, 1]^d`.

    """
    theta: Incomplete
    def __init__(self, theta: Incomplete | None = None, k_dim: int = 2) -> None: ...
    def rvs(self, nobs: int = 1, args=(), random_state: Incomplete | None = None): ...
    def pdf(self, u, args=()): ...
    def cdf(self, u, args=()): ...
    def logpdf(self, u, args=()): ...
    def cdfcond_2g1(self, u, args=()):
        """Conditional cdf of second component given the value of first.
        """
    def ppfcond_2g1(self, q, u1, args=()):
        """Conditional pdf of second component given the value of first.
        """
    def tau(self, theta: Incomplete | None = None): ...
    def theta_from_tau(self, tau): ...

class GumbelCopula(ArchimedeanCopula):
    """Gumbel copula.

    Dependence is greater in the positive tail than in the negative.

    .. math::

        C_\\theta(u,v) = \\exp\\!\\left[ -\\left( (-\\log(u))^\\theta +
        (-\\log(v))^\\theta \\right)^{1/\\theta} \\right]

    with :math:`\\theta\\in[1,\\infty)`.

    """
    theta: Incomplete
    def __init__(self, theta: Incomplete | None = None, k_dim: int = 2) -> None: ...
    def rvs(self, nobs: int = 1, args=(), random_state: Incomplete | None = None): ...
    def pdf(self, u, args=()): ...
    def cdf(self, u, args=()): ...
    def logpdf(self, u, args=()): ...
    def tau(self, theta: Incomplete | None = None): ...
    def theta_from_tau(self, tau): ...
