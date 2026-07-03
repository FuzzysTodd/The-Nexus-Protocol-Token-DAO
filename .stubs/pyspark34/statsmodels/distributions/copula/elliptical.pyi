from _typeshed import Incomplete
from statsmodels.compat.scipy import multivariate_t as multivariate_t
from statsmodels.distributions.copula.copulas import Copula as Copula

class EllipticalCopula(Copula):
    """Base class for elliptical copula

    This class requires subclassing and currently does not have generic
    methods based on an elliptical generator.

    Notes
    -----
    Elliptical copulas require that copula parameters are set when the
    instance is created. Those parameters currently cannot be provided in the
    call to methods. (This will most likely change in future versions.)
    If non-empty ``args`` are provided in methods, then a ValueError is raised.
    The ``args`` keyword is provided for a consistent interface across
    copulas.

    """
    def rvs(self, nobs: int = 1, args=(), random_state: Incomplete | None = None): ...
    def pdf(self, u, args=()): ...
    def cdf(self, u, args=()): ...
    def tau(self, corr: Incomplete | None = None):
        """Bivariate kendall's tau based on correlation coefficient.

        Parameters
        ----------
        corr : None or float
            Pearson correlation. If corr is None, then the correlation will be
            taken from the copula attribute.

        Returns
        -------
        Kendall's tau that corresponds to pearson correlation in the
        elliptical copula.
        """
    def corr_from_tau(self, tau):
        """Pearson correlation from kendall's tau.

        Parameters
        ----------
        tau : array_like
            Kendall's tau correlation coefficient.

        Returns
        -------
        Pearson correlation coefficient for given tau in elliptical
        copula. This can be used as parameter for an elliptical copula.
        """
    def fit_corr_param(self, data):
        """Copula correlation parameter using Kendall's tau of sample data.

        Parameters
        ----------
        data : array_like
            Sample data used to fit `theta` using Kendall's tau.

        Returns
        -------
        corr_param : float
            Correlation parameter of the copula, ``theta`` in Archimedean and
            pearson correlation in elliptical.
            If k_dim > 2, then average tau is used.
        """

class GaussianCopula(EllipticalCopula):
    """Gaussian copula.

    It is constructed from a multivariate normal distribution over
    :math:`\\mathbb{R}^d` by using the probability integral transform.

    For a given correlation matrix :math:`R \\in[-1, 1]^{d \\times d}`,
    the Gaussian copula with parameter matrix :math:`R` can be written
    as:

    .. math::

        C_R^{\\text{Gauss}}(u) = \\Phi_R\\left(\\Phi^{-1}(u_1),\\dots,
        \\Phi^{-1}(u_d) \\right),

    where :math:`\\Phi^{-1}` is the inverse cumulative distribution function
    of a standard normal and :math:`\\Phi_R` is the joint cumulative
    distribution function of a multivariate normal distribution with mean
    vector zero and covariance matrix equal to the correlation
    matrix :math:`R`.

    Parameters
    ----------
    corr : scalar or array_like
        Correlation or scatter matrix for the elliptical copula. In the
        bivariate case, ``corr` can be a scalar and is then considered as
        the correlation coefficient. If ``corr`` is None, then the scatter
        matrix is the identity matrix.
    k_dim : int
        Dimension, number of components in the multivariate random variable.
    allow_singular : bool
        Allow singular correlation matrix.
        The behavior when the correlation matrix is singular is determined by
        `scipy.stats.multivariate_normal`` and might not be appropriate for
        all copula or copula distribution metnods. Behavior might change in
        future versions.

    Notes
    -----
    Elliptical copulas require that copula parameters are set when the
    instance is created. Those parameters currently cannot be provided in the
    call to methods. (This will most likely change in future versions.)
    If non-empty ``args`` are provided in methods, then a ValueError is raised.
    The ``args`` keyword is provided for a consistent interface across
    copulas.

    References
    ----------
    .. [1] Joe, Harry, 2014, Dependence modeling with copulas. CRC press.
        p. 163

    """
    corr: Incomplete
    args: Incomplete
    distr_uv: Incomplete
    distr_mv: Incomplete
    def __init__(self, corr: Incomplete | None = None, k_dim: int = 2, allow_singular: bool = False) -> None: ...
    def dependence_tail(self, corr: Incomplete | None = None):
        """
        Bivariate tail dependence parameter.

        Joe (2014) p. 182

        Parameters
        ----------
        corr : any
            Tail dependence for Gaussian copulas is always zero.
            Argument will be ignored

        Returns
        -------
        Lower and upper tail dependence coefficients of the copula with given
        Pearson correlation coefficient.
        """

class StudentTCopula(EllipticalCopula):
    """Student t copula.

    Parameters
    ----------
    corr : scalar or array_like
        Correlation or scatter matrix for the elliptical copula. In the
        bivariate case, ``corr` can be a scalar and is then considered as
        the correlation coefficient. If ``corr`` is None, then the scatter
        matrix is the identity matrix.
    df : float (optional)
        Degrees of freedom of the multivariate t distribution.
    k_dim : int
        Dimension, number of components in the multivariate random variable.

    Notes
    -----
    Elliptical copulas require that copula parameters are set when the
    instance is created. Those parameters currently cannot be provided in the
    call to methods. (This will most likely change in future versions.)
    If non-empty ``args`` are provided in methods, then a ValueError is raised.
    The ``args`` keyword is provided for a consistent interface across
    copulas.

    References
    ----------
    .. [1] Joe, Harry, 2014, Dependence modeling with copulas. CRC press.
        p. 181
    """
    df: Incomplete
    corr: Incomplete
    args: Incomplete
    distr_uv: Incomplete
    distr_mv: Incomplete
    def __init__(self, corr: Incomplete | None = None, df: Incomplete | None = None, k_dim: int = 2) -> None: ...
    def cdf(self, u, args=()) -> None: ...
    def spearmans_rho(self, corr: Incomplete | None = None):
        """
        Bivariate Spearman's rho based on correlation coefficient.

        Joe (2014) p. 182

        Parameters
        ----------
        corr : None or float
            Pearson correlation. If corr is None, then the correlation will be
            taken from the copula attribute.

        Returns
        -------
        Spearman's rho that corresponds to pearson correlation in the
        elliptical copula.
        """
    def dependence_tail(self, corr: Incomplete | None = None):
        """
        Bivariate tail dependence parameter.

        Joe (2014) p. 182

        Parameters
        ----------
        corr : None or float
            Pearson correlation. If corr is None, then the correlation will be
            taken from the copula attribute.

        Returns
        -------
        Lower and upper tail dependence coefficients of the copula with given
        Pearson correlation coefficient.
        """
