from _typeshed import Incomplete
from statsmodels.distributions.tools import cdf2prob_grid as cdf2prob_grid, prob2cdf_grid as prob2cdf_grid
from statsmodels.tools.decorators import cache_readonly as cache_readonly

class BernsteinDistribution:
    """Distribution based on Bernstein Polynomials on unit hypercube.

    Parameters
    ----------
    cdf_grid : array_like
        cdf values on a equal spaced grid of the unit hypercube [0, 1]^d.
        The dimension of the arrays define how many random variables are
        included in the multivariate distribution.

    Attributes
    ----------
    cdf_grid : grid of cdf values
    prob_grid : grid of cell or bin probabilities
    k_dim : (int) number of components, dimension of random variable
    k_grid : (tuple) shape of cdf_grid
    k_grid_product : (int) total number of bins in grid
    _grid : Grid instance with helper methods and attributes
    """
    cdf_grid: Incomplete
    k_dim: Incomplete
    k_grid: Incomplete
    k_grid_product: Incomplete
    def __init__(self, cdf_grid) -> None: ...
    @classmethod
    def from_data(cls, data, k_bins):
        """Create distribution instance from data using histogram binning.

        Classmethod to construct a distribution instance.

        Parameters
        ----------
        data : array_like
            Data with observation in rows and random variables in columns.
            Data can be 1-dimensional in the univariate case.
        k_bins : int or list
            Number or edges of bins to be used in numpy histogramdd.
            If k_bins is a scalar int, then the number of bins of each
            component will be equal to it.

        Returns
        -------
        Instance of a Bernstein distribution
        """
    def prob_grid(self): ...
    def cdf(self, x):
        """cdf values evaluated at x.

        Parameters
        ----------
        x : array_like
            Points of multivariate random variable at which cdf is evaluated.
            This can be a single point with length equal to the dimension of
            the random variable, or two dimensional with points (observations)
            in rows and random variables in columns.
            In the univariate case, a 1-dimensional x will be interpreted as
            different points for evaluation.

        Returns
        -------
        pdf values

        Notes
        -----
        Warning: 2-dim x with many points can be memory intensive because
        currently the bernstein polynomials will be evaluated in a fully
        vectorized computation.
        """
    def pdf(self, x):
        """pdf values evaluated at x.

        Parameters
        ----------
        x : array_like
            Points of multivariate random variable at which pdf is evaluated.
            This can be a single point with length equal to the dimension of
            the random variable, or two dimensional with points (observations)
            in rows and random variables in columns.
            In the univariate case, a 1-dimensional x will be interpreted as
            different points for evaluation.

        Returns
        -------
        cdf values

        Notes
        -----
        Warning: 2-dim x with many points can be memory intensive because
        currently the bernstein polynomials will be evaluated in a fully
        vectorized computation.
        """
    def get_marginal(self, idx):
        """Get marginal BernsteinDistribution.

        Parameters
        ----------
        idx : int or list of int
            Index or indices of the component for which the marginal
            distribution is returned.

        Returns
        -------
        BernsteinDistribution instance for the marginal distribution.
        """
    def rvs(self, nobs):
        """Generate random numbers from distribution.

        Parameters
        ----------
        nobs : int
            Number of random observations to generate.
        """

class BernsteinDistributionBV(BernsteinDistribution):
    def cdf(self, x): ...
    def pdf(self, x): ...

class BernsteinDistributionUV(BernsteinDistribution):
    def cdf(self, x, method: str = 'binom'): ...
    def pdf(self, x, method: str = 'binom'): ...
