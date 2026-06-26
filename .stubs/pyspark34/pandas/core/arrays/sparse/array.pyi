import numpy as np
from _typeshed import Incomplete
from enum import Enum
from pandas import Series as Series
from pandas._libs import lib as lib
from pandas._libs.sparse import BlockIndex as BlockIndex, IntIndex as IntIndex, SparseIndex as SparseIndex
from pandas._libs.tslibs import NaT as NaT
from pandas._typing import ArrayLike as ArrayLike, AstypeArg as AstypeArg, Axis as Axis, AxisInt as AxisInt, Dtype as Dtype, FillnaOptions as FillnaOptions, NpDtype as NpDtype, NumpySorter as NumpySorter, PositionalIndexer as PositionalIndexer, Scalar as Scalar, ScalarIndexer as ScalarIndexer, SequenceIndexer as SequenceIndexer, npt as npt
from pandas.core import arraylike as arraylike, ops as ops
from pandas.core.arraylike import OpsMixin as OpsMixin
from pandas.core.arrays import ExtensionArray as ExtensionArray
from pandas.core.arrays.sparse.dtype import SparseDtype as SparseDtype
from pandas.core.base import PandasObject as PandasObject
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array, sanitize_array as sanitize_array
from pandas.core.dtypes.astype import astype_array as astype_array
from pandas.core.dtypes.cast import construct_1d_arraylike_from_scalar as construct_1d_arraylike_from_scalar, find_common_type as find_common_type, maybe_box_datetimelike as maybe_box_datetimelike
from pandas.core.dtypes.common import is_array_like as is_array_like, is_bool_dtype as is_bool_dtype, is_datetime64_any_dtype as is_datetime64_any_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_dtype_equal as is_dtype_equal, is_integer as is_integer, is_list_like as is_list_like, is_object_dtype as is_object_dtype, is_scalar as is_scalar, is_string_dtype as is_string_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.generic import ABCIndex as ABCIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna, na_value_for_dtype as na_value_for_dtype, notna as notna
from pandas.core.indexers import check_array_indexer as check_array_indexer, unpack_tuple_and_ellipses as unpack_tuple_and_ellipses
from pandas.core.missing import interpolate_2d as interpolate_2d
from pandas.core.nanops import check_below_min_count as check_below_min_count
from pandas.errors import PerformanceWarning as PerformanceWarning
from pandas.io.formats import printing as printing
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg, validate_insert_loc as validate_insert_loc
from scipy.sparse import spmatrix as spmatrix
from typing import Any, Literal, TypeVar, overload

class ellipsis(Enum):
    Ellipsis: str

Ellipsis: Incomplete
SparseIndexKind: Incomplete
SparseArrayT = TypeVar('SparseArrayT', bound='SparseArray')

class SparseArray(OpsMixin, PandasObject, ExtensionArray):
    """
    An ExtensionArray for storing sparse data.

    Parameters
    ----------
    data : array-like or scalar
        A dense array of values to store in the SparseArray. This may contain
        `fill_value`.
    sparse_index : SparseIndex, optional
    fill_value : scalar, optional
        Elements in data that are ``fill_value`` are not stored in the
        SparseArray. For memory savings, this should be the most common value
        in `data`. By default, `fill_value` depends on the dtype of `data`:

        =========== ==========
        data.dtype  na_value
        =========== ==========
        float       ``np.nan``
        int         ``0``
        bool        False
        datetime64  ``pd.NaT``
        timedelta64 ``pd.NaT``
        =========== ==========

        The fill value is potentially specified in three ways. In order of
        precedence, these are

        1. The `fill_value` argument
        2. ``dtype.fill_value`` if `fill_value` is None and `dtype` is
           a ``SparseDtype``
        3. ``data.dtype.fill_value`` if `fill_value` is None and `dtype`
           is not a ``SparseDtype`` and `data` is a ``SparseArray``.

    kind : str
        Can be 'integer' or 'block', default is 'integer'.
        The type of storage for sparse locations.

        * 'block': Stores a `block` and `block_length` for each
          contiguous *span* of sparse values. This is best when
          sparse data tends to be clumped together, with large
          regions of ``fill-value`` values between sparse values.
        * 'integer': uses an integer to store the location of
          each sparse value.

    dtype : np.dtype or SparseDtype, optional
        The dtype to use for the SparseArray. For numpy dtypes, this
        determines the dtype of ``self.sp_values``. For SparseDtype,
        this determines ``self.sp_values`` and ``self.fill_value``.
    copy : bool, default False
        Whether to explicitly copy the incoming `data` array.

    Attributes
    ----------
    None

    Methods
    -------
    None

    Examples
    --------
    >>> from pandas.arrays import SparseArray
    >>> arr = SparseArray([0, 0, 1, 2])
    >>> arr
    [0, 0, 1, 2]
    Fill: 0
    IntIndex
    Indices: array([2, 3], dtype=int32)
    """
    def __init__(self, data, sparse_index: Incomplete | None = None, fill_value: Incomplete | None = None, kind: SparseIndexKind = 'integer', dtype: Dtype | None = None, copy: bool = False) -> None: ...
    @classmethod
    def from_spmatrix(cls, data: spmatrix) -> SparseArrayT:
        """
        Create a SparseArray from a scipy.sparse matrix.

        Parameters
        ----------
        data : scipy.sparse.sp_matrix
            This should be a SciPy sparse matrix where the size
            of the second dimension is 1. In other words, a
            sparse matrix with a single column.

        Returns
        -------
        SparseArray

        Examples
        --------
        >>> import scipy.sparse
        >>> mat = scipy.sparse.coo_matrix((4, 1))
        >>> pd.arrays.SparseArray.from_spmatrix(mat)
        [0.0, 0.0, 0.0, 0.0]
        Fill: 0.0
        IntIndex
        Indices: array([], dtype=int32)
        """
    def __array__(self, dtype: NpDtype | None = None) -> np.ndarray: ...
    def __setitem__(self, key, value) -> None: ...
    @property
    def sp_index(self) -> SparseIndex:
        """
        The SparseIndex containing the location of non- ``fill_value`` points.
        """
    @property
    def sp_values(self) -> np.ndarray:
        """
        An ndarray containing the non- ``fill_value`` values.

        Examples
        --------
        >>> from pandas.arrays import SparseArray
        >>> s = SparseArray([0, 0, 1, 0, 2], fill_value=0)
        >>> s.sp_values
        array([1, 2])
        """
    @property
    def dtype(self) -> SparseDtype: ...
    @property
    def fill_value(self):
        """
        Elements in `data` that are `fill_value` are not stored.

        For memory savings, this should be the most common value in the array.
        """
    @fill_value.setter
    def fill_value(self, value) -> None: ...
    @property
    def kind(self) -> SparseIndexKind:
        """
        The kind of sparse index for this array. One of {'integer', 'block'}.
        """
    def __len__(self) -> int: ...
    @property
    def nbytes(self) -> int: ...
    @property
    def density(self) -> float:
        """
        The percent of non- ``fill_value`` points, as decimal.

        Examples
        --------
        >>> from pandas.arrays import SparseArray
        >>> s = SparseArray([0, 0, 1, 1, 1], fill_value=0)
        >>> s.density
        0.6
        """
    @property
    def npoints(self) -> int:
        """
        The number of non- ``fill_value`` points.

        Examples
        --------
        >>> from pandas.arrays import SparseArray
        >>> s = SparseArray([0, 0, 1, 1, 1], fill_value=0)
        >>> s.npoints
        3
        """
    def isna(self): ...
    def fillna(self, value: Incomplete | None = None, method: FillnaOptions | None = None, limit: int | None = None) -> SparseArrayT:
        """
        Fill missing values with `value`.

        Parameters
        ----------
        value : scalar, optional
        method : str, optional

            .. warning::

               Using 'method' will result in high memory use,
               as all `fill_value` methods will be converted to
               an in-memory ndarray

        limit : int, optional

        Returns
        -------
        SparseArray

        Notes
        -----
        When `value` is specified, the result's ``fill_value`` depends on
        ``self.fill_value``. The goal is to maintain low-memory use.

        If ``self.fill_value`` is NA, the result dtype will be
        ``SparseDtype(self.dtype, fill_value=value)``. This will preserve
        amount of memory used before and after filling.

        When ``self.fill_value`` is not NA, the result dtype will be
        ``self.dtype``. Again, this preserves the amount of memory used.
        """
    def shift(self, periods: int = 1, fill_value: Incomplete | None = None) -> SparseArrayT: ...
    def unique(self) -> SparseArrayT: ...
    def factorize(self, use_na_sentinel: bool = True) -> tuple[np.ndarray, SparseArray]: ...
    def value_counts(self, dropna: bool = True) -> Series:
        """
        Returns a Series containing counts of unique values.

        Parameters
        ----------
        dropna : bool, default True
            Don't include counts of NaN, even if NaN is in sp_values.

        Returns
        -------
        counts : Series
        """
    @overload
    def __getitem__(self, key: ScalarIndexer) -> Any: ...
    @overload
    def __getitem__(self, key: SequenceIndexer | tuple[int | ellipsis, ...]) -> SparseArrayT: ...
    def take(self, indices, *, allow_fill: bool = False, fill_value: Incomplete | None = None) -> SparseArrayT: ...
    def searchsorted(self, v: ArrayLike | object, side: Literal['left', 'right'] = 'left', sorter: NumpySorter = None) -> npt.NDArray[np.intp] | np.intp: ...
    def copy(self) -> SparseArrayT: ...
    def astype(self, dtype: AstypeArg | None = None, copy: bool = True):
        '''
        Change the dtype of a SparseArray.

        The output will always be a SparseArray. To convert to a dense
        ndarray with a certain dtype, use :meth:`numpy.asarray`.

        Parameters
        ----------
        dtype : np.dtype or ExtensionDtype
            For SparseDtype, this changes the dtype of
            ``self.sp_values`` and the ``self.fill_value``.

            For other dtypes, this only changes the dtype of
            ``self.sp_values``.

        copy : bool, default True
            Whether to ensure a copy is made, even if not necessary.

        Returns
        -------
        SparseArray

        Examples
        --------
        >>> arr = pd.arrays.SparseArray([0, 0, 1, 2])
        >>> arr
        [0, 0, 1, 2]
        Fill: 0
        IntIndex
        Indices: array([2, 3], dtype=int32)

        >>> arr.astype(SparseDtype(np.dtype(\'int32\')))
        [0, 0, 1, 2]
        Fill: 0
        IntIndex
        Indices: array([2, 3], dtype=int32)

        Using a NumPy dtype with a different kind (e.g. float) will coerce
        just ``self.sp_values``.

        >>> arr.astype(SparseDtype(np.dtype(\'float64\')))
        ... # doctest: +NORMALIZE_WHITESPACE
        [nan, nan, 1.0, 2.0]
        Fill: nan
        IntIndex
        Indices: array([2, 3], dtype=int32)

        Using a SparseDtype, you can also change the fill value as well.

        >>> arr.astype(SparseDtype("float64", fill_value=0.0))
        ... # doctest: +NORMALIZE_WHITESPACE
        [0.0, 0.0, 1.0, 2.0]
        Fill: 0.0
        IntIndex
        Indices: array([2, 3], dtype=int32)
        '''
    def map(self, mapper) -> SparseArrayT:
        """
        Map categories using an input mapping or function.

        Parameters
        ----------
        mapper : dict, Series, callable
            The correspondence from old values to new.

        Returns
        -------
        SparseArray
            The output array will have the same density as the input.
            The output fill value will be the result of applying the
            mapping to ``self.fill_value``

        Examples
        --------
        >>> arr = pd.arrays.SparseArray([0, 1, 2])
        >>> arr.map(lambda x: x + 10)
        [10, 11, 12]
        Fill: 10
        IntIndex
        Indices: array([1, 2], dtype=int32)

        >>> arr.map({0: 10, 1: 11, 2: 12})
        [10, 11, 12]
        Fill: 10
        IntIndex
        Indices: array([1, 2], dtype=int32)

        >>> arr.map(pd.Series([10, 11, 12], index=[0, 1, 2]))
        [10, 11, 12]
        Fill: 10
        IntIndex
        Indices: array([1, 2], dtype=int32)
        """
    def to_dense(self) -> np.ndarray:
        """
        Convert SparseArray to a NumPy array.

        Returns
        -------
        arr : NumPy array
        """
    def nonzero(self) -> tuple[npt.NDArray[np.int32]]: ...
    def all(self, axis: Incomplete | None = None, *args, **kwargs):
        """
        Tests whether all elements evaluate True

        Returns
        -------
        all : bool

        See Also
        --------
        numpy.all
        """
    def any(self, axis: AxisInt = 0, *args, **kwargs):
        """
        Tests whether at least one of elements evaluate True

        Returns
        -------
        any : bool

        See Also
        --------
        numpy.any
        """
    def sum(self, axis: AxisInt = 0, min_count: int = 0, skipna: bool = True, *args, **kwargs) -> Scalar:
        """
        Sum of non-NA/null values

        Parameters
        ----------
        axis : int, default 0
            Not Used. NumPy compatibility.
        min_count : int, default 0
            The required number of valid values to perform the summation. If fewer
            than ``min_count`` valid values are present, the result will be the missing
            value indicator for subarray type.
        *args, **kwargs
            Not Used. NumPy compatibility.

        Returns
        -------
        scalar
        """
    def cumsum(self, axis: AxisInt = 0, *args, **kwargs) -> SparseArray:
        """
        Cumulative sum of non-NA/null values.

        When performing the cumulative summation, any non-NA/null values will
        be skipped. The resulting SparseArray will preserve the locations of
        NaN values, but the fill value will be `np.nan` regardless.

        Parameters
        ----------
        axis : int or None
            Axis over which to perform the cumulative summation. If None,
            perform cumulative summation over flattened array.

        Returns
        -------
        cumsum : SparseArray
        """
    def mean(self, axis: Axis = 0, *args, **kwargs):
        """
        Mean of non-NA/null values

        Returns
        -------
        mean : float
        """
    def max(self, *, axis: AxisInt | None = None, skipna: bool = True):
        """
        Max of array values, ignoring NA values if specified.

        Parameters
        ----------
        axis : int, default 0
            Not Used. NumPy compatibility.
        skipna : bool, default True
            Whether to ignore NA values.

        Returns
        -------
        scalar
        """
    def min(self, *, axis: AxisInt | None = None, skipna: bool = True):
        """
        Min of array values, ignoring NA values if specified.

        Parameters
        ----------
        axis : int, default 0
            Not Used. NumPy compatibility.
        skipna : bool, default True
            Whether to ignore NA values.

        Returns
        -------
        scalar
        """
    def argmax(self, skipna: bool = True) -> int: ...
    def argmin(self, skipna: bool = True) -> int: ...
    def __array_ufunc__(self, ufunc: np.ufunc, method: str, *inputs, **kwargs): ...
    def __pos__(self) -> SparseArray: ...
    def __neg__(self) -> SparseArray: ...
    def __invert__(self) -> SparseArray: ...
    def __abs__(self) -> SparseArray: ...

@overload
def make_sparse_index(length: int, indices, kind: Literal['block']) -> BlockIndex: ...
@overload
def make_sparse_index(length: int, indices, kind: Literal['integer']) -> IntIndex: ...
