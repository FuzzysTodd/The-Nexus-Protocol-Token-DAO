from _typeshed import Incomplete

class _Grid:
    """Create Grid values and indices, grid in [0, 1]^d

    This class creates a regular grid in a d dimensional hyper cube.

    Intended for internal use, implementation might change without warning.


    Parameters
    ----------
    k_grid : tuple or array_like
        number of elements for axes, this defines k_grid - 1 equal sized
        intervals of [0, 1] for each axis.
    eps : float
        If eps is not zero, then x values will be clipped to [eps, 1 - eps],
        i.e. to the interior of the unit interval or hyper cube.


    Attributes
    ----------
    k_grid : list of number of grid points
    x_marginal: list of 1-dimensional marginal values
    idx_flat: integer array with indices
    x_flat: flattened grid values,
        rows are grid points, columns represent variables or axis.
        ``x_flat`` is currently also 2-dim in the univariate 1-dim grid case.

    """
    k_grid: Incomplete
    x_marginal: Incomplete
    idx_flat: Incomplete
    x_flat: Incomplete
    def __init__(self, k_grid, eps: int = 0) -> None: ...

def prob2cdf_grid(probs):
    """Cumulative probabilities from cell provabilites on a grid

    Parameters
    ----------
    probs : array_like
        Rectangular grid of cell probabilities.

    Returns
    -------
    cdf : ndarray
        Grid of cumulative probabilities with same shape as probs.
    """
def cdf2prob_grid(cdf, prepend: int = 0):
    """Cell probabilities from cumulative probabilities on a grid.

    Parameters
    ----------
    cdf : array_like
        Grid of cumulative probabilities with same shape as probs.

    Returns
    -------
    probs : ndarray
        Rectangular grid of cell probabilities.

    """
def average_grid(values, coords: Incomplete | None = None, _method: str = 'slicing'):
    '''Compute average for each cell in grid using endpoints

    Parameters
    ----------
    values : array_like
        Values on a grid that will average over corner points of each cell.
    coords : None or list of array_like
        Grid coordinates for each axis use to compute volumne of cell.
        If None, then averaged values are not rescaled.
    _method : {"slicing", "convolve"}
        Grid averaging is implemented using numpy "slicing" or using
        scipy.signal "convolve".

    Returns
    -------
    Grid with averaged cell values.
    '''
def nearest_matrix_margins(mat, maxiter: int = 100, tol: float = 1e-08):
    """nearest matrix with uniform margins

    Parameters
    ----------
    mat : array_like, 2-D
        Matrix that will be converted to have uniform margins.
        Currently, `mat` has to be two dimensional.
    maxiter : in
        Maximum number of iterations.
    tol : float
        Tolerance for convergence, defined for difference between largest and
        smallest margin in each dimension.

    Returns
    -------
    ndarray, nearest matrix with uniform margins.

    Notes
    -----
    This function is intended for internal use and will be generalized in
    future. API will change.

    changed in 0.14 to support k_dim > 2.


    """
def frequencies_fromdata(data, k_bins, use_ranks: bool = True):
    """count of observations in bins (histogram)

    currently only for bivariate data

    Parameters
    ----------
    data : array_like
        Bivariate data with observations in rows and two columns. Binning is
        in unit rectangle [0, 1]^2. If use_rank is False, then data should be
        in unit interval.
    k_bins : int
        Number of bins along each dimension in the histogram
    use_ranks : bool
        If use_rank is True, then data will be converted to ranks without
        tie handling.

    Returns
    -------
    bin counts : ndarray
        Frequencies are the number of observations in a given bin.
        Bin counts are a 2-dim array with k_bins rows and k_bins columns.

    Notes
    -----
    This function is intended for internal use and will be generalized in
    future. API will change.
    """
def approx_copula_pdf(copula, k_bins: int = 10, force_uniform: bool = True, use_pdf: bool = False):
    """Histogram probabilities as approximation to a copula density.

    Parameters
    ----------
    copula : instance
        Instance of a copula class. Only the ``pdf`` method is used.
    k_bins : int
        Number of bins along each dimension in the approximating histogram.
    force_uniform : bool
        If true, then the pdf grid will be adjusted to have uniform margins
        using `nearest_matrix_margin`.
        If false, then no adjustment is done and the margins may not be exactly
        uniform.
    use_pdf : bool
        If false, then the grid cell probabilities will be computed from the
        copula cdf.
        If true, then the density, ``pdf``, is used and cell probabilities
        are approximated by averaging the pdf of the cell corners. This is
        only useful if the cdf is not available.

    Returns
    -------
    bin probabilites : ndarray
        Probability that random variable falls in given bin. This corresponds
        to a discrete distribution, and is not scaled to bin size to form a
        piecewise uniform, histogram density.
        Bin probabilities are a k-dim array with k_bins segments in each
        dimensionrows.

    Notes
    -----
    This function is intended for internal use and will be generalized in
    future. API will change.
    """
