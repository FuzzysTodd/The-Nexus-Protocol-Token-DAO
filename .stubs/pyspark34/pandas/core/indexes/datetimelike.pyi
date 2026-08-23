import abc
import numpy as np
from _typeshed import Incomplete
from abc import ABC
from pandas import CategoricalIndex as CategoricalIndex
from pandas._libs import NaT as NaT, Timedelta as Timedelta, lib as lib
from pandas._libs.tslibs import BaseOffset as BaseOffset, Resolution as Resolution, Tick as Tick, parsing as parsing, to_offset as to_offset
from pandas._typing import Axis as Axis, npt as npt
from pandas.core.arrays import DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray, PeriodArray as PeriodArray, TimedeltaArray as TimedeltaArray
from pandas.core.arrays.datetimelike import DatetimeLikeArrayMixin as DatetimeLikeArrayMixin
from pandas.core.dtypes.common import is_categorical_dtype as is_categorical_dtype, is_dtype_equal as is_dtype_equal, is_integer as is_integer, is_list_like as is_list_like
from pandas.core.dtypes.concat import concat_compat as concat_compat
from pandas.core.indexes.base import Index as Index
from pandas.core.indexes.extension import NDArrayBackedExtensionIndex as NDArrayBackedExtensionIndex
from pandas.core.indexes.range import RangeIndex as RangeIndex
from pandas.core.tools.timedeltas import to_timedelta as to_timedelta
from pandas.errors import NullFrequencyError as NullFrequencyError
from pandas.util._decorators import Appender as Appender, cache_readonly as cache_readonly, doc as doc
from typing import Any, Callable

class DatetimeIndexOpsMixin(NDArrayBackedExtensionIndex, ABC, metaclass=abc.ABCMeta):
    """
    Common ops mixin to support a unified interface datetimelike Index.
    """
    def mean(self, *, skipna: bool = True, axis: int | None = 0): ...
    @property
    def freq(self) -> BaseOffset | None: ...
    @freq.setter
    def freq(self, value) -> None: ...
    @property
    def asi8(self) -> npt.NDArray[np.int64]: ...
    @property
    def freqstr(self) -> str | None: ...
    def resolution(self) -> str: ...
    def hasnans(self) -> bool: ...
    def equals(self, other: Any) -> bool:
        """
        Determines if two Index objects contain the same elements.
        """
    def __contains__(self, key: Any) -> bool: ...
    def format(self, name: bool = False, formatter: Callable | None = None, na_rep: str = 'NaT', date_format: str | None = None) -> list[str]:
        """
        Render a string representation of the Index.
        """
    def shift(self, periods: int = 1, freq: Incomplete | None = None) -> _T:
        """
        Shift index by desired number of time frequency increments.

        This method is for shifting the values of datetime-like indexes
        by a specified time increment a given number of times.

        Parameters
        ----------
        periods : int, default 1
            Number of periods (or increments) to shift by,
            can be positive or negative.
        freq : pandas.DateOffset, pandas.Timedelta or string, optional
            Frequency increment to shift by.
            If None, the index is shifted by its own `freq` attribute.
            Offset aliases are valid strings, e.g., 'D', 'W', 'M' etc.

        Returns
        -------
        pandas.DatetimeIndex
            Shifted index.

        See Also
        --------
        Index.shift : Shift values of Index.
        PeriodIndex.shift : Shift values of PeriodIndex.
        """

class DatetimeTimedeltaMixin(DatetimeIndexOpsMixin, ABC, metaclass=abc.ABCMeta):
    """
    Mixin class for methods shared by DatetimeIndex and TimedeltaIndex,
    but not PeriodIndex
    """
    @property
    def unit(self) -> str: ...
    def as_unit(self, unit: str) -> _TDT:
        """
        Convert to a dtype with the given unit resolution.

        Parameters
        ----------
        unit : {'s', 'ms', 'us', 'ns'}

        Returns
        -------
        same type as self
        """
    @property
    def values(self) -> np.ndarray: ...
    def shift(self, periods: int = 1, freq: Incomplete | None = None) -> _TDT: ...
    def inferred_freq(self) -> str | None: ...
    def delete(self, loc) -> DatetimeTimedeltaMixin: ...
    def insert(self, loc: int, item): ...
    def take(self, indices, axis: Axis = 0, allow_fill: bool = True, fill_value: Incomplete | None = None, **kwargs): ...
