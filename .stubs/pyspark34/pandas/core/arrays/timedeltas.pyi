import numpy as np
from _typeshed import Incomplete
from pandas import DataFrame as DataFrame
from pandas._libs import lib as lib, tslibs as tslibs
from pandas._libs.tslibs import BaseOffset as BaseOffset, NaT as NaT, NaTType as NaTType, Tick as Tick, Timedelta as Timedelta, astype_overflowsafe as astype_overflowsafe, get_supported_reso as get_supported_reso, get_unit_from_dtype as get_unit_from_dtype, iNaT as iNaT, is_supported_unit as is_supported_unit, npy_unit_to_abbrev as npy_unit_to_abbrev, periods_per_second as periods_per_second, to_offset as to_offset
from pandas._libs.tslibs.conversion import precision_from_unit as precision_from_unit
from pandas._libs.tslibs.fields import get_timedelta_days as get_timedelta_days, get_timedelta_field as get_timedelta_field
from pandas._libs.tslibs.timedeltas import array_to_timedelta64 as array_to_timedelta64, floordiv_object_array as floordiv_object_array, ints_to_pytimedelta as ints_to_pytimedelta, parse_timedelta_unit as parse_timedelta_unit, truediv_object_array as truediv_object_array
from pandas._typing import AxisInt as AxisInt, DateTimeErrorChoices as DateTimeErrorChoices, DtypeObj as DtypeObj, NpDtype as NpDtype, npt as npt
from pandas.core import nanops as nanops
from pandas.core.array_algos import datetimelike_accumulations as datetimelike_accumulations
from pandas.core.arrays import datetimelike as dtl
from pandas.core.arrays._ranges import generate_regular_range as generate_regular_range
from pandas.core.dtypes.common import TD64NS_DTYPE as TD64NS_DTYPE, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_float_dtype as is_float_dtype, is_integer_dtype as is_integer_dtype, is_object_dtype as is_object_dtype, is_scalar as is_scalar, is_string_dtype as is_string_dtype, is_timedelta64_dtype as is_timedelta64_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.missing import isna as isna
from pandas.core.ops import roperator as roperator
from pandas.core.ops.common import unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.util._validators import validate_endpoints as validate_endpoints
from typing import Iterator

class TimedeltaArray(dtl.TimelikeOps):
    '''
    Pandas ExtensionArray for timedelta data.

    .. warning::

       TimedeltaArray is currently experimental, and its API may change
       without warning. In particular, :attr:`TimedeltaArray.dtype` is
       expected to change to be an instance of an ``ExtensionDtype``
       subclass.

    Parameters
    ----------
    values : array-like
        The timedelta data.

    dtype : numpy.dtype
        Currently, only ``numpy.dtype("timedelta64[ns]")`` is accepted.
    freq : Offset, optional
    copy : bool, default False
        Whether to copy the underlying array of data.

    Attributes
    ----------
    None

    Methods
    -------
    None
    '''
    __array_priority__: int
    @property
    def dtype(self) -> np.dtype:
        """
        The dtype for the TimedeltaArray.

        .. warning::

           A future version of pandas will change dtype to be an instance
           of a :class:`pandas.api.extensions.ExtensionDtype` subclass,
           not a ``numpy.dtype``.

        Returns
        -------
        numpy.dtype
        """
    def astype(self, dtype, copy: bool = True): ...
    def __iter__(self) -> Iterator: ...
    def sum(self, *, axis: AxisInt | None = None, dtype: NpDtype | None = None, out: Incomplete | None = None, keepdims: bool = False, initial: Incomplete | None = None, skipna: bool = True, min_count: int = 0): ...
    def std(self, *, axis: AxisInt | None = None, dtype: NpDtype | None = None, out: Incomplete | None = None, ddof: int = 1, keepdims: bool = False, skipna: bool = True): ...
    def __mul__(self, other) -> TimedeltaArray: ...
    __rmul__ = __mul__
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    def __floordiv__(self, other): ...
    def __rfloordiv__(self, other): ...
    def __mod__(self, other): ...
    def __rmod__(self, other): ...
    def __divmod__(self, other): ...
    def __rdivmod__(self, other): ...
    def __neg__(self) -> TimedeltaArray: ...
    def __pos__(self) -> TimedeltaArray: ...
    def __abs__(self) -> TimedeltaArray: ...
    def total_seconds(self) -> npt.NDArray[np.float64]:
        """
        Return total duration of each element expressed in seconds.

        This method is available directly on TimedeltaArray, TimedeltaIndex
        and on Series containing timedelta values under the ``.dt`` namespace.

        Returns
        -------
        ndarray, Index or Series
            When the calling object is a TimedeltaArray, the return type
            is ndarray.  When the calling object is a TimedeltaIndex,
            the return type is an Index with a float64 dtype. When the calling object
            is a Series, the return type is Series of type `float64` whose
            index is the same as the original.

        See Also
        --------
        datetime.timedelta.total_seconds : Standard library version
            of this method.
        TimedeltaIndex.components : Return a DataFrame with components of
            each Timedelta.

        Examples
        --------
        **Series**

        >>> s = pd.Series(pd.to_timedelta(np.arange(5), unit='d'))
        >>> s
        0   0 days
        1   1 days
        2   2 days
        3   3 days
        4   4 days
        dtype: timedelta64[ns]

        >>> s.dt.total_seconds()
        0         0.0
        1     86400.0
        2    172800.0
        3    259200.0
        4    345600.0
        dtype: float64

        **TimedeltaIndex**

        >>> idx = pd.to_timedelta(np.arange(5), unit='d')
        >>> idx
        TimedeltaIndex(['0 days', '1 days', '2 days', '3 days', '4 days'],
                       dtype='timedelta64[ns]', freq=None)

        >>> idx.total_seconds()
        Index([0.0, 86400.0, 172800.0, 259200.0, 345600.0], dtype='float64')
        """
    def to_pytimedelta(self) -> npt.NDArray[np.object_]:
        """
        Return an ndarray of datetime.timedelta objects.

        Returns
        -------
        numpy.ndarray
        """
    days: Incomplete
    seconds: Incomplete
    microseconds: Incomplete
    nanoseconds: Incomplete
    @property
    def components(self) -> DataFrame:
        """
        Return a DataFrame of the individual resolution components of the Timedeltas.

        The components (days, hours, minutes seconds, milliseconds, microseconds,
        nanoseconds) are returned as columns in a DataFrame.

        Returns
        -------
        DataFrame
        """

def sequence_to_td64ns(data, copy: bool = False, unit: Incomplete | None = None, errors: DateTimeErrorChoices = 'raise') -> tuple[np.ndarray, Tick | None]:
    '''
    Parameters
    ----------
    data : list-like
    copy : bool, default False
    unit : str, optional
        The timedelta unit to treat integers as multiples of. For numeric
        data this defaults to ``\'ns\'``.
        Must be un-specified if the data contains a str and ``errors=="raise"``.
    errors : {"raise", "coerce", "ignore"}, default "raise"
        How to handle elements that cannot be converted to timedelta64[ns].
        See ``pandas.to_timedelta`` for details.

    Returns
    -------
    converted : numpy.ndarray
        The sequence converted to a numpy array with dtype ``timedelta64[ns]``.
    inferred_freq : Tick or None
        The inferred frequency of the sequence.

    Raises
    ------
    ValueError : Data cannot be converted to timedelta64[ns].

    Notes
    -----
    Unlike `pandas.to_timedelta`, if setting ``errors=ignore`` will not cause
    errors to be ignored; they are caught and subsequently ignored at a
    higher level.
    '''
