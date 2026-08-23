from matplotlib.axes import Axes as Axes
from pandas import DataFrame as DataFrame, DatetimeIndex as DatetimeIndex, Index as Index, Series as Series
from pandas._libs.tslibs import BaseOffset as BaseOffset, Period as Period, to_offset as to_offset
from pandas._libs.tslibs.dtypes import FreqGroup as FreqGroup
from pandas.core.dtypes.generic import ABCDatetimeIndex as ABCDatetimeIndex, ABCPeriodIndex as ABCPeriodIndex, ABCTimedeltaIndex as ABCTimedeltaIndex
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.plotting._matplotlib.converter import TimeSeries_DateFormatter as TimeSeries_DateFormatter, TimeSeries_DateLocator as TimeSeries_DateLocator, TimeSeries_TimedeltaFormatter as TimeSeries_TimedeltaFormatter
from pandas.tseries.frequencies import get_period_alias as get_period_alias, is_subperiod as is_subperiod, is_superperiod as is_superperiod

def maybe_resample(series: Series, ax: Axes, kwargs): ...
def decorate_axes(ax: Axes, freq, kwargs) -> None:
    """Initialize axes for time-series plotting"""
def use_dynamic_x(ax: Axes, data: DataFrame | Series) -> bool: ...
def maybe_convert_index(ax: Axes, data): ...
def format_dateaxis(subplot, freq, index) -> None:
    """
    Pretty-formats the date axis (x-axis).

    Major and minor ticks are automatically set for the frequency of the
    current underlying series.  As the dynamic mode is activated by
    default, changing the limits of the x axis will intelligently change
    the positions of the ticks.
    """
