import numpy as np
import pandas as pd
from _typeshed import Incomplete
from statsmodels.compat.pandas import Appender as Appender, PD_LT_2 as PD_LT_2, is_numeric_dtype as is_numeric_dtype
from statsmodels.compat.scipy import SP_LT_19 as SP_LT_19
from statsmodels.iolib.table import SimpleTable as SimpleTable
from statsmodels.stats.stattools import jarque_bera as jarque_bera
from statsmodels.tools.decorators import cache_readonly as cache_readonly
from statsmodels.tools.docstring import Docstring as Docstring, Parameter as Parameter
from statsmodels.tools.validation import array_like as array_like, bool_like as bool_like, float_like as float_like, int_like as int_like
from typing import Sequence

PERCENTILES: Incomplete
QUANTILES: Incomplete

def pd_ptp(df): ...
def nancount(x, axis: int = 0): ...
def nanptp(arr, axis: int = 0): ...
def nanuss(arr, axis: int = 0): ...
def nanpercentile(arr, axis: int = 0): ...
def nankurtosis(arr, axis: int = 0): ...
def nanskewness(arr, axis: int = 0): ...

MISSING: Incomplete

def sign_test(samp, mu0: int = 0):
    """
    Signs test

    Parameters
    ----------
    samp : array_like
        1d array. The sample for which you want to perform the sign test.
    mu0 : float
        See Notes for the definition of the sign test. mu0 is 0 by
        default, but it is common to set it to the median.

    Returns
    -------
    M
    p-value

    Notes
    -----
    The signs test returns

    M = (N(+) - N(-))/2

    where N(+) is the number of values above `mu0`, N(-) is the number of
    values below.  Values equal to `mu0` are discarded.

    The p-value for M is calculated using the binomial distribution
    and can be interpreted the same as for a t-test. The test-statistic
    is distributed Binom(min(N(+), N(-)), n_trials, .5) where n_trials
    equals N(+) + N(-).

    See Also
    --------
    scipy.stats.wilcoxon
    """

NUMERIC_STATISTICS: Incomplete
CATEGORICAL_STATISTICS: Incomplete
DEFAULT_STATISTICS: Incomplete

class Description:
    '''
    Extended descriptive statistics for data

    Parameters
    ----------
    data : array_like
        Data to describe. Must be convertible to a pandas DataFrame.
    stats : Sequence[str], optional
        Statistics to include. If not provided the full set of statistics is
        computed. This list may evolve across versions to reflect best
        practices. Supported options are:
        "nobs", "missing", "mean", "std_err", "ci", "ci", "std", "iqr",
        "iqr_normal", "mad", "mad_normal", "coef_var", "range", "max",
        "min", "skew", "kurtosis", "jarque_bera", "mode", "freq",
        "median", "percentiles", "distinct", "top", and "freq". See Notes for
        details.
    numeric : bool, default True
        Whether to include numeric columns in the descriptive statistics.
    categorical : bool, default True
        Whether to include categorical columns in the descriptive statistics.
    alpha : float, default 0.05
        A number between 0 and 1 representing the size used to compute the
        confidence interval, which has coverage 1 - alpha.
    use_t : bool, default False
        Use the Student\'s t distribution to construct confidence intervals.
    percentiles : sequence[float]
        A distinct sequence of floating point values all between 0 and 100.
        The default percentiles are 1, 5, 10, 25, 50, 75, 90, 95, 99.
    ntop : int, default 5
        The number of top categorical labels to report. Default is

    Attributes
    ----------
    numeric_statistics
        The list of supported statistics for numeric data
    categorical_statistics
        The list of supported statistics for categorical data
    default_statistics
        The default list of statistics

    See Also
    --------
    pandas.DataFrame.describe
        Basic descriptive statistics
    describe
        A simplified version that returns a DataFrame

    Notes
    -----
    The selectable statistics include:

    * "nobs" - Number of observations
    * "missing" - Number of missing observations
    * "mean" - Mean
    * "std_err" - Standard Error of the mean assuming no correlation
    * "ci" - Confidence interval with coverage (1 - alpha) using the normal or
      t. This option creates two entries in any tables: lower_ci and upper_ci.
    * "std" - Standard Deviation
    * "iqr" - Interquartile range
    * "iqr_normal" - Interquartile range relative to a Normal
    * "mad" - Mean absolute deviation
    * "mad_normal" - Mean absolute deviation relative to a Normal
    * "coef_var" - Coefficient of variation
    * "range" - Range between the maximum and the minimum
    * "max" - The maximum
    * "min" - The minimum
    * "skew" - The skewness defined as the standardized 3rd central moment
    * "kurtosis" - The kurtosis defined as the standardized 4th central moment
    * "jarque_bera" - The Jarque-Bera test statistic for normality based on
      the skewness and kurtosis. This option creates two entries, jarque_bera
      and jarque_beta_pval.
    * "mode" - The mode of the data. This option creates two entries in all tables,
      mode and mode_freq which is the empirical frequency of the modal value.
    * "median" - The median of the data.
    * "percentiles" - The percentiles. Values included depend on the input value of
      ``percentiles``.
    * "distinct" - The number of distinct categories in a categorical.
    * "top" - The mode common categories. Labeled top_n for n in 1, 2, ..., ``ntop``.
    * "freq" - The frequency of the common categories. Labeled freq_n for n in 1,
      2, ..., ``ntop``.
    '''
    numeric_statistics = NUMERIC_STATISTICS
    categorical_statistics = CATEGORICAL_STATISTICS
    default_statistics = DEFAULT_STATISTICS
    def __init__(self, data: np.ndarray | pd.Series | pd.DataFrame, stats: Sequence[str] = None, *, numeric: bool = True, categorical: bool = True, alpha: float = 0.05, use_t: bool = False, percentiles: Sequence[int | float] = ..., ntop: bool = 5) -> None: ...
    def frame(self) -> pd.DataFrame:
        """
        Descriptive statistics for both numeric and categorical data

        Returns
        -------
        DataFrame
            The statistics
        """
    def numeric(self) -> pd.DataFrame:
        """
        Descriptive statistics for numeric data

        Returns
        -------
        DataFrame
            The statistics of the numeric columns
        """
    def categorical(self) -> pd.DataFrame:
        """
        Descriptive statistics for categorical data

        Returns
        -------
        DataFrame
            The statistics of the categorical columns
        """
    def summary(self) -> SimpleTable:
        """
        Summary table of the descriptive statistics

        Returns
        -------
        SimpleTable
            A table instance supporting export to text, csv and LaTeX
        """

ds: Incomplete

def describe(data: np.ndarray | pd.Series | pd.DataFrame, stats: Sequence[str] = None, *, numeric: bool = True, categorical: bool = True, alpha: float = 0.05, use_t: bool = False, percentiles: Sequence[int | float] = ..., ntop: bool = 5) -> pd.DataFrame: ...

class Describe:
    """
    Removed.
    """
    def __init__(self, dataset) -> None: ...
