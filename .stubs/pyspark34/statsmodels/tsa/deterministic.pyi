import abc
import numpy as np
import pandas as pd
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from statsmodels.compat.pandas import Appender as Appender, is_int_index as is_int_index, to_numpy as to_numpy
from statsmodels.iolib.summary import d_or_f as d_or_f
from statsmodels.tools.validation import bool_like as bool_like, float_like as float_like, required_int_like as required_int_like, string_like as string_like
from statsmodels.tsa.tsatools import freq_to_period as freq_to_period
from typing import Hashable, List, Sequence

DateLike: Incomplete
IntLike = int | np.integer
START_BEFORE_INDEX_ERR: str

class DeterministicTerm(ABC, metaclass=abc.ABCMeta):
    """Abstract Base Class for all Deterministic Terms"""
    @property
    def is_dummy(self) -> bool:
        """Flag indicating whether the values produced are dummy variables"""
    @abstractmethod
    def in_sample(self, index: Sequence[Hashable]) -> pd.DataFrame:
        """
        Produce deterministic trends for in-sample fitting.

        Parameters
        ----------
        index : index_like
            An index-like object. If not an index, it is converted to an
            index.

        Returns
        -------
        DataFrame
            A DataFrame containing the deterministic terms.
        """
    @abstractmethod
    def out_of_sample(self, steps: int, index: Sequence[Hashable], forecast_index: Sequence[Hashable] | None = None) -> pd.DataFrame:
        """
        Produce deterministic trends for out-of-sample forecasts

        Parameters
        ----------
        steps : int
            The number of steps to forecast
        index : index_like
            An index-like object. If not an index, it is converted to an
            index.
        forecast_index : index_like
            An Index or index-like object to use for the forecasts. If
            provided must have steps elements.

        Returns
        -------
        DataFrame
            A DataFrame containing the deterministic terms.
        """
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...

class TimeTrendDeterministicTerm(DeterministicTerm, ABC, metaclass=abc.ABCMeta):
    """Abstract Base Class for all Time Trend Deterministic Terms"""
    def __init__(self, constant: bool = True, order: int = 0) -> None: ...
    @property
    def constant(self) -> bool:
        """Flag indicating that a constant is included"""
    @property
    def order(self) -> int:
        """Order of the time trend"""

class TimeTrend(TimeTrendDeterministicTerm):
    """
    Constant and time trend determinstic terms

    Parameters
    ----------
    constant : bool
        Flag indicating whether a constant should be included.
    order : int
        A non-negative int containing the powers to include (1, 2, ..., order).

    See Also
    --------
    DeterministicProcess
    Seasonality
    Fourier
    CalendarTimeTrend

    Examples
    --------
    >>> from statsmodels.datasets import sunspots
    >>> from statsmodels.tsa.deterministic import TimeTrend
    >>> data = sunspots.load_pandas().data
    >>> trend_gen = TimeTrend(True, 3)
    >>> trend_gen.in_sample(data.index)
    """
    def __init__(self, constant: bool = True, order: int = 0) -> None: ...
    @classmethod
    def from_string(cls, trend: str) -> TimeTrend:
        '''
        Create a TimeTrend from a string description.

        Provided for compatibility with common string names.

        Parameters
        ----------
        trend : {"n", "c", "t", "ct", "ctt"}
            The string representation of the time trend. The terms are:

            * "n": No trend terms
            * "c": A constant only
            * "t": Linear time trend only
            * "ct": A constant and a time trend
            * "ctt": A constant, a time trend and a quadratic time trend

        Returns
        -------
        TimeTrend
            The TimeTrend instance.
        '''
    def in_sample(self, index: Sequence[Hashable] | pd.Index) -> pd.DataFrame: ...
    def out_of_sample(self, steps: int, index: Sequence[Hashable] | pd.Index, forecast_index: Sequence[Hashable] | None = None) -> pd.DataFrame: ...

class Seasonality(DeterministicTerm):
    """
    Seasonal dummy deterministic terms

    Parameters
    ----------
    period : int
        The length of a full cycle. Must be >= 2.
    initial_period : int
        The seasonal index of the first observation. 1-indexed so must
        be in {1, 2, ..., period}.

    See Also
    --------
    DeterministicProcess
    TimeTrend
    Fourier
    CalendarSeasonality

    Examples
    --------
    Solar data has an 11-year cycle

    >>> from statsmodels.datasets import sunspots
    >>> from statsmodels.tsa.deterministic import Seasonality
    >>> data = sunspots.load_pandas().data
    >>> seas_gen = Seasonality(11)
    >>> seas_gen.in_sample(data.index)

    To start at a season other than 1

    >>> seas_gen = Seasonality(11, initial_period=4)
    >>> seas_gen.in_sample(data.index)
    """
    def __init__(self, period: int, initial_period: int = 1) -> None: ...
    @property
    def period(self) -> int:
        """The period of the seasonality"""
    @property
    def initial_period(self) -> int:
        """The seasonal index of the first observation"""
    @classmethod
    def from_index(cls, index: Sequence[Hashable] | pd.DatetimeIndex | pd.PeriodIndex) -> Seasonality:
        """
        Construct a seasonality directly from an index using its frequency.

        Parameters
        ----------
        index : {DatetimeIndex, PeriodIndex}
            An index with its frequency (`freq`) set.

        Returns
        -------
        Seasonality
            The initialized Seasonality instance.
        """
    def in_sample(self, index: Sequence[Hashable] | pd.Index) -> pd.DataFrame: ...
    def out_of_sample(self, steps: int, index: Sequence[Hashable] | pd.Index, forecast_index: Sequence[Hashable] | None = None) -> pd.DataFrame: ...

class FourierDeterministicTerm(DeterministicTerm, ABC, metaclass=abc.ABCMeta):
    """Abstract Base Class for all Fourier Deterministic Terms"""
    def __init__(self, order: int) -> None: ...
    @property
    def order(self) -> int:
        """The order of the Fourier terms included"""

class Fourier(FourierDeterministicTerm):
    """
    Fourier series deterministic terms

    Parameters
    ----------
    period : int
        The length of a full cycle. Must be >= 2.
    order : int
        The number of Fourier components to include. Must be <= 2*period.

    See Also
    --------
    DeterministicProcess
    TimeTrend
    Seasonality
    CalendarFourier

    Notes
    -----
    Both a sine and a cosine term are included for each i=1, ..., order

    .. math::

       f_{i,s,t} & = \\sin\\left(2 \\pi i \\times \\frac{t}{m} \\right)  \\\\\n       f_{i,c,t} & = \\cos\\left(2 \\pi i \\times \\frac{t}{m} \\right)

    where m is the length of the period.

    Examples
    --------
    Solar data has an 11-year cycle

    >>> from statsmodels.datasets import sunspots
    >>> from statsmodels.tsa.deterministic import Fourier
    >>> data = sunspots.load_pandas().data
    >>> fourier_gen = Fourier(11, order=2)
    >>> fourier_gen.in_sample(data.index)
    """
    def __init__(self, period: float, order: int) -> None: ...
    @property
    def period(self) -> float:
        """The period of the Fourier terms"""
    def in_sample(self, index: Sequence[Hashable] | pd.Index) -> pd.DataFrame: ...
    def out_of_sample(self, steps: int, index: Sequence[Hashable] | pd.Index, forecast_index: Sequence[Hashable] | None = None) -> pd.DataFrame: ...

class CalendarDeterministicTerm(DeterministicTerm, ABC, metaclass=abc.ABCMeta):
    """Abstract Base Class for calendar deterministic terms"""
    def __init__(self, freq: str) -> None: ...
    @property
    def freq(self) -> str:
        """The frequency of the deterministic terms"""

class CalendarFourier(CalendarDeterministicTerm, FourierDeterministicTerm):
    '''
    Fourier series deterministic terms based on calendar time

    Parameters
    ----------
    freq : str
        A string convertible to a pandas frequency.
    order : int
        The number of Fourier components to include. Must be <= 2*period.

    See Also
    --------
    DeterministicProcess
    CalendarTimeTrend
    CalendarSeasonality
    Fourier

    Notes
    -----
    Both a sine and a cosine term are included for each i=1, ..., order

    .. math::

       f_{i,s,t} & = \\sin\\left(2 \\pi i \\tau_t \\right)  \\\\\n       f_{i,c,t} & = \\cos\\left(2 \\pi i \\tau_t \\right)

    where m is the length of the period and :math:`\\tau_t` is the frequency
    normalized time.  For example, when freq is "D" then an observation with
    a timestamp of 12:00:00 would have :math:`\\tau_t=0.5`.

    Examples
    --------
    Here we simulate irregularly spaced hourly data and construct the calendar
    Fourier terms for the data.

    >>> import numpy as np
    >>> import pandas as pd
    >>> base = pd.Timestamp("2020-1-1")
    >>> gen = np.random.default_rng()
    >>> gaps = np.cumsum(gen.integers(0, 1800, size=1000))
    >>> times = [base + pd.Timedelta(gap, unit="s") for gap in gaps]
    >>> index = pd.DatetimeIndex(pd.to_datetime(times))

    >>> from statsmodels.tsa.deterministic import CalendarFourier
    >>> cal_fourier_gen = CalendarFourier("D", 2)
    >>> cal_fourier_gen.in_sample(index)
    '''
    def __init__(self, freq: str, order: int) -> None: ...
    def in_sample(self, index: Sequence[Hashable] | pd.Index) -> pd.DataFrame: ...
    def out_of_sample(self, steps: int, index: Sequence[Hashable] | pd.Index, forecast_index: Sequence[Hashable] | None = None) -> pd.DataFrame: ...

class CalendarSeasonality(CalendarDeterministicTerm):
    '''
    Seasonal dummy deterministic terms based on calendar time

    Parameters
    ----------
    freq : str
        The frequency of the seasonal effect.
    period : str
        The pandas frequency string describing the full period.

    See Also
    --------
    DeterministicProcess
    CalendarTimeTrend
    CalendarFourier
    Seasonality

    Examples
    --------
    Here we simulate irregularly spaced data (in time) and hourly seasonal
    dummies for the data.

    >>> import numpy as np
    >>> import pandas as pd
    >>> base = pd.Timestamp("2020-1-1")
    >>> gen = np.random.default_rng()
    >>> gaps = np.cumsum(gen.integers(0, 1800, size=1000))
    >>> times = [base + pd.Timedelta(gap, unit="s") for gap in gaps]
    >>> index = pd.DatetimeIndex(pd.to_datetime(times))

    >>> from statsmodels.tsa.deterministic import CalendarSeasonality
    >>> cal_seas_gen = CalendarSeasonality("H", "D")
    >>> cal_seas_gen.in_sample(index)
    '''
    def __init__(self, freq: str, period: str) -> None: ...
    @property
    def freq(self) -> str:
        """The frequency of the deterministic terms"""
    @property
    def period(self) -> str:
        """The full period"""
    def in_sample(self, index: Sequence[Hashable] | pd.Index) -> pd.DataFrame: ...
    def out_of_sample(self, steps: int, index: Sequence[Hashable] | pd.Index, forecast_index: Sequence[Hashable] | None = None) -> pd.DataFrame: ...

class CalendarTimeTrend(CalendarDeterministicTerm, TimeTrendDeterministicTerm):
    '''
    Constant and time trend determinstic terms based on calendar time

    Parameters
    ----------
    freq : str
        A string convertible to a pandas frequency.
    constant : bool
        Flag indicating whether a constant should be included.
    order : int
        A non-negative int containing the powers to include (1, 2, ..., order).
    base_period : {str, pd.Timestamp}, default None
        The base period to use when computing the time stamps. This value is
        treated as 1 and so all other time indices are defined as the number
        of periods since or before this time stamp. If not provided, defaults
        to pandas base period for a PeriodIndex.

    See Also
    --------
    DeterministicProcess
    CalendarFourier
    CalendarSeasonality
    TimeTrend

    Notes
    -----
    The time stamp, :math:`\\tau_t`, is the number of periods that have elapsed
    since the base_period. :math:`\\tau_t` may be fractional.

    Examples
    --------
    Here we simulate irregularly spaced hourly data and construct the calendar
    time trend terms for the data.

    >>> import numpy as np
    >>> import pandas as pd
    >>> base = pd.Timestamp("2020-1-1")
    >>> gen = np.random.default_rng()
    >>> gaps = np.cumsum(gen.integers(0, 1800, size=1000))
    >>> times = [base + pd.Timedelta(gap, unit="s") for gap in gaps]
    >>> index = pd.DatetimeIndex(pd.to_datetime(times))

    >>> from statsmodels.tsa.deterministic import CalendarTimeTrend
    >>> cal_trend_gen = CalendarTimeTrend("D", True, order=1)
    >>> cal_trend_gen.in_sample(index)

    Next, we normalize using the first time stamp

    >>> cal_trend_gen = CalendarTimeTrend("D", True, order=1,
    ...                                   base_period=index[0])
    >>> cal_trend_gen.in_sample(index)
    '''
    def __init__(self, freq: str, constant: bool = True, order: int = 0, *, base_period: str | DateLike | None = None) -> None: ...
    @property
    def base_period(self) -> str | None:
        """The base period"""
    @classmethod
    def from_string(cls, freq: str, trend: str, base_period: str | DateLike | None = None) -> CalendarTimeTrend:
        '''
        Create a TimeTrend from a string description.

        Provided for compatibility with common string names.

        Parameters
        ----------
        freq : str
            A string convertible to a pandas frequency.
        trend : {"n", "c", "t", "ct", "ctt"}
            The string representation of the time trend. The terms are:

            * "n": No trend terms
            * "c": A constant only
            * "t": Linear time trend only
            * "ct": A constant and a time trend
            * "ctt": A constant, a time trend and a quadratic time trend
        base_period : {str, pd.Timestamp}, default None
            The base period to use when computing the time stamps. This value
            is treated as 1 and so all other time indices are defined as the
            number of periods since or before this time stamp. If not
            provided, defaults to pandas base period for a PeriodIndex.

        Returns
        -------
        TimeTrend
            The TimeTrend instance.
        '''
    def in_sample(self, index: Sequence[Hashable] | pd.Index) -> pd.DataFrame: ...
    def out_of_sample(self, steps: int, index: Sequence[Hashable] | pd.Index, forecast_index: Sequence[Hashable] | None = None) -> pd.DataFrame: ...

class DeterministicProcess:
    '''
    Container class for deterministic terms.

    Directly supports constants, time trends, and either seasonal dummies or
    fourier terms for a single cycle. Additional deterministic terms beyond
    the set that can be directly initialized through the constructor can be
    added.

    Parameters
    ----------
    index : {Sequence[Hashable], pd.Index}
        The index of the process. Should usually be the "in-sample" index when
        used in forecasting applications.
    period : {float, int}, default None
        The period of the seasonal or fourier components. Must be an int for
        seasonal dummies. If not provided, freq is read from index if
        available.
    constant : bool, default False
        Whether to include a constant.
    order : int, default 0
        The order of the tim trend to include. For example, 2 will include
        both linear and quadratic terms. 0 exclude time trend terms.
    seasonal : bool = False
        Whether to include seasonal dummies
    fourier : int = 0
        The order of the fourier terms to included.
    additional_terms : Sequence[DeterministicTerm]
        A sequence of additional deterministic terms to include in the process.
    drop : bool, default False
        A flag indicating to check for perfect collinearity and to drop any
        linearly dependent terms.

    See Also
    --------
    TimeTrend
    Seasonality
    Fourier
    CalendarTimeTrend
    CalendarSeasonality
    CalendarFourier

    Notes
    -----
    See the notebook `Deterministic Terms in Time Series Models
    <../examples/notebooks/generated/deterministics.html>`__ for an overview.

    Examples
    --------
    >>> from statsmodels.tsa.deterministic import DeterministicProcess
    >>> from pandas import date_range
    >>> index = date_range("2000-1-1", freq="M", periods=240)

    First a determinstic process with a constant and quadratic time trend.

    >>> dp = DeterministicProcess(index, constant=True, order=2)
    >>> dp.in_sample().head(3)
                const  trend  trend_squared
    2000-01-31    1.0    1.0            1.0
    2000-02-29    1.0    2.0            4.0
    2000-03-31    1.0    3.0            9.0

    Seasonal dummies are included by setting seasonal to True.

    >>> dp = DeterministicProcess(index, constant=True, seasonal=True)
    >>> dp.in_sample().iloc[:3,:5]
                const  s(2,12)  s(3,12)  s(4,12)  s(5,12)
    2000-01-31    1.0      0.0      0.0      0.0      0.0
    2000-02-29    1.0      1.0      0.0      0.0      0.0
    2000-03-31    1.0      0.0      1.0      0.0      0.0

    Fourier components can be used to alternatively capture seasonal patterns,

    >>> dp = DeterministicProcess(index, constant=True, fourier=2)
    >>> dp.in_sample().head(3)
                const  sin(1,12)  cos(1,12)  sin(2,12)  cos(2,12)
    2000-01-31    1.0   0.000000   1.000000   0.000000        1.0
    2000-02-29    1.0   0.500000   0.866025   0.866025        0.5
    2000-03-31    1.0   0.866025   0.500000   0.866025       -0.5

    Multiple Seasonalities can be captured using additional terms.

    >>> from statsmodels.tsa.deterministic import Fourier
    >>> index = date_range("2000-1-1", freq="D", periods=5000)
    >>> fourier = Fourier(period=365.25, order=1)
    >>> dp = DeterministicProcess(index, period=3, constant=True,
    ...                           seasonal=True, additional_terms=[fourier])
    >>> dp.in_sample().head(3)
                const  s(2,3)  s(3,3)  sin(1,365.25)  cos(1,365.25)
    2000-01-01    1.0     0.0     0.0       0.000000       1.000000
    2000-01-02    1.0     1.0     0.0       0.017202       0.999852
    2000-01-03    1.0     0.0     1.0       0.034398       0.999408
    '''
    def __init__(self, index: Sequence[Hashable] | pd.Index, *, period: float | int | None = None, constant: bool = False, order: int = 0, seasonal: bool = False, fourier: int = 0, additional_terms: Sequence[DeterministicTerm] = (), drop: bool = False) -> None: ...
    @property
    def index(self) -> pd.Index:
        """The index of the process"""
    @property
    def terms(self) -> List[DeterministicTerm]:
        """The deterministic terms included in the process"""
    def in_sample(self) -> pd.DataFrame: ...
    def out_of_sample(self, steps: int, forecast_index: Sequence[Hashable] | pd.Index | None = None) -> pd.DataFrame: ...
    def range(self, start: IntLike | DateLike | str, stop: IntLike | DateLike | str) -> pd.DataFrame:
        """
        Deterministic terms spanning a range of observations

        Parameters
        ----------
        start : {int, str, dt.datetime, pd.Timestamp, np.datetime64}
            The first observation.
        stop : {int, str, dt.datetime, pd.Timestamp, np.datetime64}
            The final observation. Inclusive to match most prediction
            function in statsmodels.

        Returns
        -------
        DataFrame
            A data frame of deterministic terms
        """
    def apply(self, index):
        """
        Create an identical determinstic process with a different index

        Parameters
        ----------
        index : index_like
            An index-like object. If not an index, it is converted to an
            index.

        Returns
        -------
        DeterministicProcess
            The deterministic process applied to a different index
        """
