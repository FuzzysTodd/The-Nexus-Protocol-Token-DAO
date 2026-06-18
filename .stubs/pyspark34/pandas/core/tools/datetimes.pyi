from datetime import datetime
from pandas import Series
from pandas._libs.tslibs import Timestamp
from pandas._libs.tslibs.parsing import DateParseError as DateParseError
from pandas._typing import AnyArrayLike, ArrayLike, DateTimeErrorChoices
from pandas.core.indexes.base import Index
from pandas.core.indexes.datetimes import DatetimeIndex
from typing import List, Tuple, TypedDict, overload

__all__ = ['DateParseError', 'should_cache', 'to_datetime']

ArrayConvertible = List | Tuple | AnyArrayLike
Scalar = float | str
DatetimeScalar = Scalar | datetime
DatetimeScalarOrArrayConvertible = DatetimeScalar | ArrayConvertible
DatetimeDictArg = List[Scalar] | Tuple[Scalar, ...] | AnyArrayLike

class YearMonthDayDict(TypedDict, total=True):
    year: DatetimeDictArg
    month: DatetimeDictArg
    day: DatetimeDictArg

class FulldatetimeDict(YearMonthDayDict, total=False):
    hour: DatetimeDictArg
    hours: DatetimeDictArg
    minute: DatetimeDictArg
    minutes: DatetimeDictArg
    second: DatetimeDictArg
    seconds: DatetimeDictArg
    ms: DatetimeDictArg
    us: DatetimeDictArg
    ns: DatetimeDictArg

def should_cache(arg: ArrayConvertible, unique_share: float = 0.7, check_count: int | None = None) -> bool:
    """
    Decides whether to do caching.

    If the percent of unique elements among `check_count` elements less
    than `unique_share * 100` then we can do caching.

    Parameters
    ----------
    arg: listlike, tuple, 1-d array, Series
    unique_share: float, default=0.7, optional
        0 < unique_share < 1
    check_count: int, optional
        0 <= check_count <= len(arg)

    Returns
    -------
    do_caching: bool

    Notes
    -----
    By default for a sequence of less than 50 items in size, we don't do
    caching; for the number of elements less than 5000, we take ten percent of
    all elements to check for a uniqueness share; if the sequence size is more
    than 5000, then we check only the first 500 elements.
    All constants were chosen empirically by.
    """
@overload
def to_datetime(arg: DatetimeScalar, errors: DateTimeErrorChoices = ..., dayfirst: bool = ..., yearfirst: bool = ..., utc: bool = ..., format: str | None = ..., exact: bool = ..., unit: str | None = ..., infer_datetime_format: bool = ..., origin=..., cache: bool = ...) -> Timestamp: ...
@overload
def to_datetime(arg: Series | DictConvertible, errors: DateTimeErrorChoices = ..., dayfirst: bool = ..., yearfirst: bool = ..., utc: bool = ..., format: str | None = ..., exact: bool = ..., unit: str | None = ..., infer_datetime_format: bool = ..., origin=..., cache: bool = ...) -> Series: ...
@overload
def to_datetime(arg: list | tuple | Index | ArrayLike, errors: DateTimeErrorChoices = ..., dayfirst: bool = ..., yearfirst: bool = ..., utc: bool = ..., format: str | None = ..., exact: bool = ..., unit: str | None = ..., infer_datetime_format: bool = ..., origin=..., cache: bool = ...) -> DatetimeIndex: ...
