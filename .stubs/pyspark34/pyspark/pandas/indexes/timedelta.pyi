from _typeshed import Incomplete
from pyspark.pandas.indexes.base import Index as Index
from pyspark.pandas.missing.indexes import MissingPandasLikeTimedeltaIndex as MissingPandasLikeTimedeltaIndex
from pyspark.pandas.series import Series as Series
from typing import Any

HOURS_PER_DAY: int
MINUTES_PER_HOUR: int
SECONDS_PER_MINUTE: int
MILLIS_PER_SECOND: int
MICROS_PER_MILLIS: int
SECONDS_PER_HOUR: Incomplete
SECONDS_PER_DAY: Incomplete
MICROS_PER_SECOND: Incomplete

class TimedeltaIndex(Index):
    """
    Immutable ndarray-like of timedelta64 data, represented internally as int64, and
    which can be boxed to timedelta objects.

    Parameters
    ----------
    data  : array-like (1-dimensional), optional
        Optional timedelta-like data to construct index with.
    unit : unit of the arg (D,h,m,s,ms,us,ns) denote the unit, optional
        Which is an integer/float number.
    freq : str or pandas offset object, optional
        One of pandas date offset strings or corresponding objects. The string
        'infer' can be passed in order to set the frequency of the index as the
        inferred frequency upon creation.
    copy  : bool
        Make a copy of input ndarray.
    name : object
        Name to be stored in the index.

    See Also
    --------
    Index : The base pandas Index type.

    Examples
    --------
    >>> from datetime import timedelta
    >>> ps.TimedeltaIndex([timedelta(1), timedelta(microseconds=2)])
    ... # doctest: +NORMALIZE_WHITESPACE
    TimedeltaIndex(['1 days 00:00:00', '0 days 00:00:00.000002'],
    dtype='timedelta64[ns]', freq=None)

    From an Series:

    >>> s = ps.Series([timedelta(1), timedelta(microseconds=2)], index=[10, 20])
    >>> ps.TimedeltaIndex(s)
    ... # doctest: +NORMALIZE_WHITESPACE
    TimedeltaIndex(['1 days 00:00:00', '0 days 00:00:00.000002'],
    dtype='timedelta64[ns]', freq=None)

    From an Index:

    >>> idx = ps.TimedeltaIndex([timedelta(1), timedelta(microseconds=2)])
    >>> ps.TimedeltaIndex(idx)
    ... # doctest: +NORMALIZE_WHITESPACE
    TimedeltaIndex(['1 days 00:00:00', '0 days 00:00:00.000002'],
    dtype='timedelta64[ns]', freq=None)
    """
    def __new__(cls, data: Incomplete | None = None, unit: Incomplete | None = None, freq=..., closed: Incomplete | None = None, dtype: Incomplete | None = None, copy: bool = False, name: Incomplete | None = None): ...
    def __getattr__(self, item: str) -> Any: ...
    @property
    def days(self) -> Index:
        """
        Number of days for each element.
        """
    @property
    def seconds(self) -> Index:
        """
        Number of seconds (>= 0 and less than 1 day) for each element.
        """
    @property
    def microseconds(self) -> Index:
        """
        Number of microseconds (>= 0 and less than 1 second) for each element.
        """
    def all(self, *args, **kwargs) -> None: ...
