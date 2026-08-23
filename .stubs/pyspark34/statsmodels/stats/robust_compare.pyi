from _typeshed import Incomplete

def trimboth(a, proportiontocut, axis: int = 0):
    """
    Slices off a proportion of items from both ends of an array.

    Slices off the passed proportion of items from both ends of the passed
    array (i.e., with `proportiontocut` = 0.1, slices leftmost 10% **and**
    rightmost 10% of scores).  You must pre-sort the array if you want
    'proper' trimming.  Slices off less if proportion results in a
    non-integer slice index (i.e., conservatively slices off
    `proportiontocut`).

    Parameters
    ----------
    a : array_like
        Data to trim.
    proportiontocut : float or int
        Proportion of data to trim at each end.
    axis : int or None
        Axis along which the observations are trimmed. The default is to trim
        along axis=0. If axis is None then the array will be flattened before
        trimming.

    Returns
    -------
    out : array-like
        Trimmed version of array `a`.

    Examples
    --------
    >>> from scipy import stats
    >>> a = np.arange(20)
    >>> b = stats.trimboth(a, 0.1)
    >>> b.shape
    (16,)

    """
def trim_mean(a, proportiontocut, axis: int = 0):
    """
    Return mean of array after trimming observations from both tails.

    If `proportiontocut` = 0.1, slices off 'leftmost' and 'rightmost' 10% of
    scores. Slices off LESS if proportion results in a non-integer slice
    index (i.e., conservatively slices off `proportiontocut` ).

    Parameters
    ----------
    a : array_like
        Input array
    proportiontocut : float
        Fraction to cut off at each tail of the sorted observations.
    axis : int or None
        Axis along which the trimmed means are computed. The default is axis=0.
        If axis is None then the trimmed mean will be computed for the
        flattened array.

    Returns
    -------
    trim_mean : ndarray
        Mean of trimmed array.

    """

class TrimmedMean:
    """
    class for trimmed and winsorized one sample statistics

    axis is None, i.e. ravelling, is not supported

    Parameters
    ----------
    data : array-like
        The data, observations to analyze.
    fraction : float in (0, 0.5)
        The fraction of observations to trim at each tail.
        The number of observations trimmed at each tail is
        ``int(fraction * nobs)``
    is_sorted : boolean
        Indicator if data is already sorted. By default the data is sorted
        along ``axis``.
    axis : int
        The axis of reduce operations. By default axis=0, that is observations
        are along the zero dimension, i.e. rows if 2-dim.
    """
    data: Incomplete
    axis: Incomplete
    fraction: Incomplete
    nobs: Incomplete
    lowercut: Incomplete
    uppercut: Incomplete
    nobs_reduced: Incomplete
    sl: Incomplete
    data_sorted: Incomplete
    lowerbound: Incomplete
    upperbound: Incomplete
    def __init__(self, data, fraction, is_sorted: bool = False, axis: int = 0) -> None: ...
    @property
    def data_trimmed(self):
        """numpy array of trimmed and sorted data
        """
    @property
    def data_winsorized(self):
        """winsorized data
        """
    @property
    def mean_trimmed(self):
        """mean of trimmed data
        """
    @property
    def mean_winsorized(self):
        """mean of winsorized data
        """
    @property
    def var_winsorized(self):
        """variance of winsorized data
        """
    @property
    def std_mean_trimmed(self):
        """standard error of trimmed mean
        """
    @property
    def std_mean_winsorized(self):
        """standard error of winsorized mean
        """
    def ttest_mean(self, value: int = 0, transform: str = 'trimmed', alternative: str = 'two-sided'):
        """
        One sample t-test for trimmed or Winsorized mean

        Parameters
        ----------
        value : float
            Value of the mean under the Null hypothesis
        transform : {'trimmed', 'winsorized'}
            Specified whether the mean test is based on trimmed or winsorized
            data.
        alternative : {'two-sided', 'larger', 'smaller'}


        Notes
        -----
        p-value is based on the approximate t-distribution of the test
        statistic. The approximation is valid if the underlying distribution
        is symmetric.
        """
    def reset_fraction(self, frac):
        """create a TrimmedMean instance with a new trimming fraction

        This reuses the sorted array from the current instance.
        """

def scale_transform(data, center: str = 'median', transform: str = 'abs', trim_frac: float = 0.2, axis: int = 0):
    '''Transform data for variance comparison for Levene type tests

    Parameters
    ----------
    data : array_like
        Observations for the data.
    center : "median", "mean", "trimmed" or float
        Statistic used for centering observations. If a float, then this
        value is used to center. Default is median.
    transform : \'abs\', \'square\', \'identity\' or a callable
        The transform for the centered data.
    trim_frac : float in [0, 0.5)
        Fraction of observations that are trimmed on each side of the sorted
        observations. This is only used if center is `trimmed`.
    axis : int
        Axis along which the data are transformed when centering.

    Returns
    -------
    res : ndarray
        transformed data in the same shape as the original data.

    '''
