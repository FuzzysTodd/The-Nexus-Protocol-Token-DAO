from .algorithms import bootstrap as bootstrap
from .external.kde import gaussian_kde as gaussian_kde
from _typeshed import Incomplete

class KDE:
    """Univariate and bivariate kernel density estimator."""
    bw_method: Incomplete
    bw_adjust: Incomplete
    gridsize: Incomplete
    cut: Incomplete
    clip: Incomplete
    cumulative: Incomplete
    support: Incomplete
    def __init__(self, *, bw_method: Incomplete | None = None, bw_adjust: int = 1, gridsize: int = 200, cut: int = 3, clip: Incomplete | None = None, cumulative: bool = False) -> None:
        """Initialize the estimator with its parameters.

        Parameters
        ----------
        bw_method : string, scalar, or callable, optional
            Method for determining the smoothing bandwidth to use; passed to
            :class:`scipy.stats.gaussian_kde`.
        bw_adjust : number, optional
            Factor that multiplicatively scales the value chosen using
            ``bw_method``. Increasing will make the curve smoother. See Notes.
        gridsize : int, optional
            Number of points on each dimension of the evaluation grid.
        cut : number, optional
            Factor, multiplied by the smoothing bandwidth, that determines how
            far the evaluation grid extends past the extreme datapoints. When
            set to 0, truncate the curve at the data limits.
        clip : pair of numbers or None, or a pair of such pairs
            Do not evaluate the density outside of these limits.
        cumulative : bool, optional
            If True, estimate a cumulative distribution function. Requires scipy.

        """
    def define_support(self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None, cache: bool = True):
        """Create the evaluation grid for a given data set."""
    def __call__(self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None):
        """Fit and evaluate on univariate or bivariate data."""

class Histogram:
    """Univariate and bivariate histogram estimator."""
    stat: Incomplete
    bins: Incomplete
    binwidth: Incomplete
    binrange: Incomplete
    discrete: Incomplete
    cumulative: Incomplete
    bin_kws: Incomplete
    def __init__(self, stat: str = 'count', bins: str = 'auto', binwidth: Incomplete | None = None, binrange: Incomplete | None = None, discrete: bool = False, cumulative: bool = False) -> None:
        """Initialize the estimator with its parameters.

        Parameters
        ----------
        stat : str
            Aggregate statistic to compute in each bin.

            - `count`: show the number of observations in each bin
            - `frequency`: show the number of observations divided by the bin width
            - `probability` or `proportion`: normalize such that bar heights sum to 1
            - `percent`: normalize such that bar heights sum to 100
            - `density`: normalize such that the total area of the histogram equals 1

        bins : str, number, vector, or a pair of such values
            Generic bin parameter that can be the name of a reference rule,
            the number of bins, or the breaks of the bins.
            Passed to :func:`numpy.histogram_bin_edges`.
        binwidth : number or pair of numbers
            Width of each bin, overrides ``bins`` but can be used with
            ``binrange``.
        binrange : pair of numbers or a pair of pairs
            Lowest and highest value for bin edges; can be used either
            with ``bins`` or ``binwidth``. Defaults to data extremes.
        discrete : bool or pair of bools
            If True, set ``binwidth`` and ``binrange`` such that bin
            edges cover integer values in the dataset.
        cumulative : bool
            If True, return the cumulative statistic.

        """
    def define_bin_params(self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None, cache: bool = True):
        """Given data, return numpy.histogram parameters to define bins."""
    def __call__(self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None):
        """Count the occurrences in each bin, maybe normalize."""

class ECDF:
    """Univariate empirical cumulative distribution estimator."""
    stat: Incomplete
    complementary: Incomplete
    def __init__(self, stat: str = 'proportion', complementary: bool = False) -> None:
        '''Initialize the class with its parameters

        Parameters
        ----------
        stat : {{"proportion", "count"}}
            Distribution statistic to compute.
        complementary : bool
            If True, use the complementary CDF (1 - CDF)

        '''
    def __call__(self, x1, x2: Incomplete | None = None, weights: Incomplete | None = None):
        """Return proportion or count of observations below each sorted datapoint."""

class EstimateAggregator:
    estimator: Incomplete
    error_method: Incomplete
    error_level: Incomplete
    boot_kws: Incomplete
    def __init__(self, estimator, errorbar: Incomplete | None = None, **boot_kws) -> None:
        '''
        Data aggregator that produces an estimate and error bar interval.

        Parameters
        ----------
        estimator : callable or string
            Function (or method name) that maps a vector to a scalar.
        errorbar : string, (string, number) tuple, or callable
            Name of errorbar method (either "ci", "pi", "se", or "sd"), or a tuple
            with a method name and a level parameter, or a function that maps from a
            vector to a (min, max) interval.
        boot_kws
            Additional keywords are passed to bootstrap when error_method is "ci".

        '''
    def __call__(self, data, var):
        """Aggregate over `var` column of `data` with estimate and error interval."""
