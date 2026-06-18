import numpy as np
from pandas._libs.lib import i8max as i8max
from pandas._libs.tslibs import BaseOffset as BaseOffset, OutOfBoundsDatetime as OutOfBoundsDatetime, Timedelta as Timedelta, Timestamp as Timestamp, iNaT as iNaT
from pandas._typing import npt as npt

def generate_regular_range(start: Timestamp | Timedelta | None, end: Timestamp | Timedelta | None, periods: int | None, freq: BaseOffset, unit: str = 'ns') -> npt.NDArray[np.intp]:
    '''
    Generate a range of dates or timestamps with the spans between dates
    described by the given `freq` DateOffset.

    Parameters
    ----------
    start : Timedelta, Timestamp or None
        First point of produced date range.
    end : Timedelta, Timestamp or None
        Last point of produced date range.
    periods : int or None
        Number of periods in produced date range.
    freq : Tick
        Describes space between dates in produced date range.
    unit : str, default "ns"
        The resolution the output is meant to represent.

    Returns
    -------
    ndarray[np.int64]
        Representing the given resolution.
    '''
