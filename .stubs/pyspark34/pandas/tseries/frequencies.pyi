import numpy as np
from _typeshed import Incomplete
from pandas._libs.tslibs import Timestamp
from pandas._libs.tslibs.offsets import Day as Day, to_offset as to_offset
from pandas._typing import npt

__all__ = ['Day', 'get_period_alias', 'infer_freq', 'is_subperiod', 'is_superperiod', 'to_offset']

def get_period_alias(offset_str: str) -> str | None:
    """
    Alias to closest period strings BQ->Q etc.
    """
def infer_freq(index) -> str | None:
    """
    Infer the most likely frequency given the input index.

    Parameters
    ----------
    index : DatetimeIndex or TimedeltaIndex
      If passed a Series will use the values of the series (NOT THE INDEX).

    Returns
    -------
    str or None
        None if no discernible frequency.

    Raises
    ------
    TypeError
        If the index is not datetime-like.
    ValueError
        If there are fewer than three values.

    Examples
    --------
    >>> idx = pd.date_range(start='2020/12/01', end='2020/12/30', periods=30)
    >>> pd.infer_freq(idx)
    'D'
    """

class _FrequencyInferer:
    """
    Not sure if I can avoid the state machine here
    """
    index: Incomplete
    i8values: Incomplete
    is_monotonic: Incomplete
    def __init__(self, index) -> None: ...
    def deltas(self) -> npt.NDArray[np.int64]: ...
    def deltas_asi8(self) -> npt.NDArray[np.int64]: ...
    def is_unique(self) -> bool: ...
    def is_unique_asi8(self) -> bool: ...
    def get_freq(self) -> str | None:
        """
        Find the appropriate frequency string to describe the inferred
        frequency of self.i8values

        Returns
        -------
        str or None
        """
    def day_deltas(self) -> list[int]: ...
    def hour_deltas(self) -> list[int]: ...
    def fields(self) -> np.ndarray: ...
    def rep_stamp(self) -> Timestamp: ...
    def month_position_check(self) -> str | None: ...
    def mdiffs(self) -> npt.NDArray[np.int64]: ...
    def ydiffs(self) -> npt.NDArray[np.int64]: ...

class _TimedeltaFrequencyInferer(_FrequencyInferer): ...

def is_subperiod(source, target) -> bool:
    """
    Returns True if downsampling is possible between source and target
    frequencies

    Parameters
    ----------
    source : str or DateOffset
        Frequency converting from
    target : str or DateOffset
        Frequency converting to

    Returns
    -------
    bool
    """
def is_superperiod(source, target) -> bool:
    """
    Returns True if upsampling is possible between source and target
    frequencies

    Parameters
    ----------
    source : str or DateOffset
        Frequency converting from
    target : str or DateOffset
        Frequency converting to

    Returns
    -------
    bool
    """
