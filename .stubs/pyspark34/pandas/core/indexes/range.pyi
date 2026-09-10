import numpy as np
from _typeshed import Incomplete
from pandas._libs import lib as lib
from pandas._libs.algos import unique_deltas as unique_deltas
from pandas._libs.lib import no_default as no_default
from pandas._typing import Dtype as Dtype, npt as npt
from pandas.core import ops as ops
from pandas.core.construction import extract_array as extract_array
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, ensure_python_int as ensure_python_int, is_float as is_float, is_integer as is_integer, is_scalar as is_scalar, is_signed_integer_dtype as is_signed_integer_dtype, is_timedelta64_dtype as is_timedelta64_dtype
from pandas.core.dtypes.generic import ABCTimedeltaIndex as ABCTimedeltaIndex
from pandas.core.indexes.base import Index as Index, maybe_extract_name as maybe_extract_name
from pandas.core.ops.common import unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.util._decorators import cache_readonly as cache_readonly, doc as doc
from typing import Any, Callable, Hashable, Iterator

class RangeIndex(Index):
    '''
    Immutable Index implementing a monotonic integer range.

    RangeIndex is a memory-saving special case of an Index limited to representing
    monotonic ranges with a 64-bit dtype. Using RangeIndex may in some instances
    improve computing speed.

    This is the default index type used
    by DataFrame and Series when no explicit index is provided by the user.

    Parameters
    ----------
    start : int (default: 0), range, or other RangeIndex instance
        If int and "stop" is not given, interpreted as "stop" instead.
    stop : int (default: 0)
    step : int (default: 1)
    dtype : np.int64
        Unused, accepted for homogeneity with other index types.
    copy : bool, default False
        Unused, accepted for homogeneity with other index types.
    name : object, optional
        Name to be stored in the index.

    Attributes
    ----------
    start
    stop
    step

    Methods
    -------
    from_range

    See Also
    --------
    Index : The base pandas Index type.
    '''
    def __new__(cls, start: Incomplete | None = None, stop: Incomplete | None = None, step: Incomplete | None = None, dtype: Dtype | None = None, copy: bool = False, name: Hashable = None) -> RangeIndex: ...
    @classmethod
    def from_range(cls, data: range, name: Incomplete | None = None, dtype: Dtype | None = None) -> RangeIndex:
        """
        Create RangeIndex from a range object.

        Returns
        -------
        RangeIndex
        """
    def __reduce__(self): ...
    @property
    def start(self) -> int:
        """
        The value of the `start` parameter (``0`` if this was not supplied).
        """
    @property
    def stop(self) -> int:
        """
        The value of the `stop` parameter.
        """
    @property
    def step(self) -> int:
        """
        The value of the `step` parameter (``1`` if this was not supplied).
        """
    def nbytes(self) -> int:
        """
        Return the number of bytes in the underlying data.
        """
    def memory_usage(self, deep: bool = False) -> int:
        """
        Memory usage of my values

        Parameters
        ----------
        deep : bool
            Introspect the data deeply, interrogate
            `object` dtypes for system-level memory consumption

        Returns
        -------
        bytes used

        Notes
        -----
        Memory usage does not include memory consumed by elements that
        are not components of the array if deep=False

        See Also
        --------
        numpy.ndarray.nbytes
        """
    @property
    def dtype(self) -> np.dtype: ...
    @property
    def is_unique(self) -> bool:
        """return if the index has unique values"""
    def is_monotonic_increasing(self) -> bool: ...
    def is_monotonic_decreasing(self) -> bool: ...
    def __contains__(self, key: Any) -> bool: ...
    @property
    def inferred_type(self) -> str: ...
    def get_loc(self, key): ...
    def tolist(self) -> list[int]: ...
    def __iter__(self) -> Iterator[int]: ...
    def copy(self, name: Hashable = None, deep: bool = False): ...
    def min(self, axis: Incomplete | None = None, skipna: bool = True, *args, **kwargs) -> int:
        """The minimum value of the RangeIndex"""
    def max(self, axis: Incomplete | None = None, skipna: bool = True, *args, **kwargs) -> int:
        """The maximum value of the RangeIndex"""
    def argsort(self, *args, **kwargs) -> npt.NDArray[np.intp]:
        """
        Returns the indices that would sort the index and its
        underlying data.

        Returns
        -------
        np.ndarray[np.intp]

        See Also
        --------
        numpy.ndarray.argsort
        """
    def factorize(self, sort: bool = False, use_na_sentinel: bool = True) -> tuple[npt.NDArray[np.intp], RangeIndex]: ...
    def equals(self, other: object) -> bool:
        """
        Determines if two Index objects contain the same elements.
        """
    def sort_values(self, return_indexer: bool = False, ascending: bool = True, na_position: str = 'last', key: Callable | None = None): ...
    def symmetric_difference(self, other, result_name: Hashable = None, sort: Incomplete | None = None): ...
    def delete(self, loc) -> Index: ...
    def insert(self, loc: int, item) -> Index: ...
    def __len__(self) -> int:
        """
        return the length of the RangeIndex
        """
    @property
    def size(self) -> int: ...
    def __getitem__(self, key):
        """
        Conserve RangeIndex type for scalar and slice keys.
        """
    def __floordiv__(self, other): ...
    def all(self, *args, **kwargs) -> bool: ...
    def any(self, *args, **kwargs) -> bool: ...
