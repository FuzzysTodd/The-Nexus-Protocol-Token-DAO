import numpy as np
from _typeshed import Incomplete
from pandas import Categorical as Categorical, Index as Index, Series as Series
from pandas._libs import algos as algos, iNaT as iNaT, lib as lib
from pandas._typing import AnyArrayLike as AnyArrayLike, ArrayLike as ArrayLike, AxisInt as AxisInt, DtypeObj as DtypeObj, NumpySorter as NumpySorter, NumpyValueArrayLike as NumpyValueArrayLike, TakeIndexer as TakeIndexer, npt as npt
from pandas.core.array_algos.take import take_nd as take_nd
from pandas.core.arrays import BaseMaskedArray as BaseMaskedArray, ExtensionArray as ExtensionArray
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array
from pandas.core.dtypes.cast import construct_1d_object_array_from_listlike as construct_1d_object_array_from_listlike, infer_dtype_from_array as infer_dtype_from_array, np_find_common_type as np_find_common_type
from pandas.core.dtypes.common import ensure_float64 as ensure_float64, ensure_object as ensure_object, ensure_platform_int as ensure_platform_int, is_array_like as is_array_like, is_bool_dtype as is_bool_dtype, is_categorical_dtype as is_categorical_dtype, is_complex_dtype as is_complex_dtype, is_extension_array_dtype as is_extension_array_dtype, is_float_dtype as is_float_dtype, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_numeric_dtype as is_numeric_dtype, is_object_dtype as is_object_dtype, is_scalar as is_scalar, is_signed_integer_dtype as is_signed_integer_dtype, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.concat import concat_compat as concat_compat
from pandas.core.dtypes.dtypes import BaseMaskedDtype as BaseMaskedDtype, ExtensionDtype as ExtensionDtype, PandasDtype as PandasDtype
from pandas.core.dtypes.generic import ABCDatetimeArray as ABCDatetimeArray, ABCExtensionArray as ABCExtensionArray, ABCIndex as ABCIndex, ABCMultiIndex as ABCMultiIndex, ABCSeries as ABCSeries, ABCTimedeltaArray as ABCTimedeltaArray
from pandas.core.dtypes.missing import isna as isna, na_value_for_dtype as na_value_for_dtype
from pandas.core.indexers import validate_indices as validate_indices
from pandas.util._decorators import doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Literal

def unique(values):
    '''
    Return unique values based on a hash table.

    Uniques are returned in order of appearance. This does NOT sort.

    Significantly faster than numpy.unique for long enough sequences.
    Includes NA values.

    Parameters
    ----------
    values : 1d array-like

    Returns
    -------
    numpy.ndarray or ExtensionArray

        The return can be:

        * Index : when the input is an Index
        * Categorical : when the input is a Categorical dtype
        * ndarray : when the input is a Series/ndarray

        Return numpy.ndarray or ExtensionArray.

    See Also
    --------
    Index.unique : Return unique values from an Index.
    Series.unique : Return unique values of Series object.

    Examples
    --------
    >>> pd.unique(pd.Series([2, 1, 3, 3]))
    array([2, 1, 3])

    >>> pd.unique(pd.Series([2] + [1] * 5))
    array([2, 1])

    >>> pd.unique(pd.Series([pd.Timestamp("20160101"), pd.Timestamp("20160101")]))
    array([\'2016-01-01T00:00:00.000000000\'], dtype=\'datetime64[ns]\')

    >>> pd.unique(
    ...     pd.Series(
    ...         [
    ...             pd.Timestamp("20160101", tz="US/Eastern"),
    ...             pd.Timestamp("20160101", tz="US/Eastern"),
    ...         ]
    ...     )
    ... )
    <DatetimeArray>
    [\'2016-01-01 00:00:00-05:00\']
    Length: 1, dtype: datetime64[ns, US/Eastern]

    >>> pd.unique(
    ...     pd.Index(
    ...         [
    ...             pd.Timestamp("20160101", tz="US/Eastern"),
    ...             pd.Timestamp("20160101", tz="US/Eastern"),
    ...         ]
    ...     )
    ... )
    DatetimeIndex([\'2016-01-01 00:00:00-05:00\'],
            dtype=\'datetime64[ns, US/Eastern]\',
            freq=None)

    >>> pd.unique(list("baabc"))
    array([\'b\', \'a\', \'c\'], dtype=object)

    An unordered Categorical will return categories in the
    order of appearance.

    >>> pd.unique(pd.Series(pd.Categorical(list("baabc"))))
    [\'b\', \'a\', \'c\']
    Categories (3, object): [\'a\', \'b\', \'c\']

    >>> pd.unique(pd.Series(pd.Categorical(list("baabc"), categories=list("abc"))))
    [\'b\', \'a\', \'c\']
    Categories (3, object): [\'a\', \'b\', \'c\']

    An ordered Categorical preserves the category ordering.

    >>> pd.unique(
    ...     pd.Series(
    ...         pd.Categorical(list("baabc"), categories=list("abc"), ordered=True)
    ...     )
    ... )
    [\'b\', \'a\', \'c\']
    Categories (3, object): [\'a\' < \'b\' < \'c\']

    An array of tuples

    >>> pd.unique([("a", "b"), ("b", "a"), ("a", "c"), ("b", "a")])
    array([(\'a\', \'b\'), (\'b\', \'a\'), (\'a\', \'c\')], dtype=object)
    '''
def nunique_ints(values: ArrayLike) -> int:
    """
    Return the number of unique values for integer array-likes.

    Significantly faster than pandas.unique for long enough sequences.
    No checks are done to ensure input is integral.

    Parameters
    ----------
    values : 1d array-like

    Returns
    -------
    int : The number of unique values in ``values``
    """
def unique_with_mask(values, mask: npt.NDArray[np.bool_] | None = None):
    """See algorithms.unique for docs. Takes a mask for masked arrays."""
unique1d = unique

def isin(comps: AnyArrayLike, values: AnyArrayLike) -> npt.NDArray[np.bool_]:
    """
    Compute the isin boolean array.

    Parameters
    ----------
    comps : array-like
    values : array-like

    Returns
    -------
    ndarray[bool]
        Same length as `comps`.
    """
def factorize_array(values: np.ndarray, use_na_sentinel: bool = True, size_hint: int | None = None, na_value: object = None, mask: npt.NDArray[np.bool_] | None = None) -> tuple[npt.NDArray[np.intp], np.ndarray]:
    '''
    Factorize a numpy array to codes and uniques.

    This doesn\'t do any coercion of types or unboxing before factorization.

    Parameters
    ----------
    values : ndarray
    use_na_sentinel : bool, default True
        If True, the sentinel -1 will be used for NaN values. If False,
        NaN values will be encoded as non-negative integers and will not drop the
        NaN from the uniques of the values.
    size_hint : int, optional
        Passed through to the hashtable\'s \'get_labels\' method
    na_value : object, optional
        A value in `values` to consider missing. Note: only use this
        parameter when you know that you don\'t have any values pandas would
        consider missing in the array (NaN for float data, iNaT for
        datetimes, etc.).
    mask : ndarray[bool], optional
        If not None, the mask is used as indicator for missing values
        (True = missing, False = valid) instead of `na_value` or
        condition "val != val".

    Returns
    -------
    codes : ndarray[np.intp]
    uniques : ndarray
    '''
def factorize(values, sort: bool = False, use_na_sentinel: bool = True, size_hint: int | None = None) -> tuple[np.ndarray, np.ndarray | Index]:
    """
    Encode the object as an enumerated type or categorical variable.

    This method is useful for obtaining a numeric representation of an
    array when all that matters is identifying distinct values. `factorize`
    is available as both a top-level function :func:`pandas.factorize`,
    and as a method :meth:`Series.factorize` and :meth:`Index.factorize`.

    Parameters
    ----------
    {values}{sort}
    use_na_sentinel : bool, default True
        If True, the sentinel -1 will be used for NaN values. If False,
        NaN values will be encoded as non-negative integers and will not drop the
        NaN from the uniques of the values.

        .. versionadded:: 1.5.0
    {size_hint}
    Returns
    -------
    codes : ndarray
        An integer ndarray that's an indexer into `uniques`.
        ``uniques.take(codes)`` will have the same values as `values`.
    uniques : ndarray, Index, or Categorical
        The unique valid values. When `values` is Categorical, `uniques`
        is a Categorical. When `values` is some other pandas object, an
        `Index` is returned. Otherwise, a 1-D ndarray is returned.

        .. note::

           Even if there's a missing value in `values`, `uniques` will
           *not* contain an entry for it.

    See Also
    --------
    cut : Discretize continuous-valued array.
    unique : Find the unique value in an array.

    Notes
    -----
    Reference :ref:`the user guide <reshaping.factorize>` for more examples.

    Examples
    --------
    These examples all show factorize as a top-level method like
    ``pd.factorize(values)``. The results are identical for methods like
    :meth:`Series.factorize`.

    >>> codes, uniques = pd.factorize(['b', 'b', 'a', 'c', 'b'])
    >>> codes
    array([0, 0, 1, 2, 0])
    >>> uniques
    array(['b', 'a', 'c'], dtype=object)

    With ``sort=True``, the `uniques` will be sorted, and `codes` will be
    shuffled so that the relationship is the maintained.

    >>> codes, uniques = pd.factorize(['b', 'b', 'a', 'c', 'b'], sort=True)
    >>> codes
    array([1, 1, 0, 2, 1])
    >>> uniques
    array(['a', 'b', 'c'], dtype=object)

    When ``use_na_sentinel=True`` (the default), missing values are indicated in
    the `codes` with the sentinel value ``-1`` and missing values are not
    included in `uniques`.

    >>> codes, uniques = pd.factorize(['b', None, 'a', 'c', 'b'])
    >>> codes
    array([ 0, -1,  1,  2,  0])
    >>> uniques
    array(['b', 'a', 'c'], dtype=object)

    Thus far, we've only factorized lists (which are internally coerced to
    NumPy arrays). When factorizing pandas objects, the type of `uniques`
    will differ. For Categoricals, a `Categorical` is returned.

    >>> cat = pd.Categorical(['a', 'a', 'c'], categories=['a', 'b', 'c'])
    >>> codes, uniques = pd.factorize(cat)
    >>> codes
    array([0, 0, 1])
    >>> uniques
    ['a', 'c']
    Categories (3, object): ['a', 'b', 'c']

    Notice that ``'b'`` is in ``uniques.categories``, despite not being
    present in ``cat.values``.

    For all other pandas objects, an Index of the appropriate type is
    returned.

    >>> cat = pd.Series(['a', 'a', 'c'])
    >>> codes, uniques = pd.factorize(cat)
    >>> codes
    array([0, 0, 1])
    >>> uniques
    Index(['a', 'c'], dtype='object')

    If NaN is in the values, and we want to include NaN in the uniques of the
    values, it can be achieved by setting ``use_na_sentinel=False``.

    >>> values = np.array([1, 2, 1, np.nan])
    >>> codes, uniques = pd.factorize(values)  # default: use_na_sentinel=True
    >>> codes
    array([ 0,  1,  0, -1])
    >>> uniques
    array([1., 2.])

    >>> codes, uniques = pd.factorize(values, use_na_sentinel=False)
    >>> codes
    array([0, 1, 0, 2])
    >>> uniques
    array([ 1.,  2., nan])
    """
def value_counts(values, sort: bool = True, ascending: bool = False, normalize: bool = False, bins: Incomplete | None = None, dropna: bool = True) -> Series:
    """
    Compute a histogram of the counts of non-null values.

    Parameters
    ----------
    values : ndarray (1-d)
    sort : bool, default True
        Sort by values
    ascending : bool, default False
        Sort in ascending order
    normalize: bool, default False
        If True then compute a relative histogram
    bins : integer, optional
        Rather than count values, group them into half-open bins,
        convenience for pd.cut, only works with numeric data
    dropna : bool, default True
        Don't include counts of NaN

    Returns
    -------
    Series
    """
def value_counts_arraylike(values: np.ndarray, dropna: bool, mask: npt.NDArray[np.bool_] | None = None) -> tuple[ArrayLike, npt.NDArray[np.int64]]:
    """
    Parameters
    ----------
    values : np.ndarray
    dropna : bool
    mask : np.ndarray[bool] or None, default None

    Returns
    -------
    uniques : np.ndarray
    counts : np.ndarray[np.int64]
    """
def duplicated(values: ArrayLike, keep: Literal['first', 'last', False] = 'first') -> npt.NDArray[np.bool_]:
    """
    Return boolean ndarray denoting duplicate values.

    Parameters
    ----------
    values : nd.array, ExtensionArray or Series
        Array over which to check for duplicate values.
    keep : {'first', 'last', False}, default 'first'
        - ``first`` : Mark duplicates as ``True`` except for the first
          occurrence.
        - ``last`` : Mark duplicates as ``True`` except for the last
          occurrence.
        - False : Mark all duplicates as ``True``.

    Returns
    -------
    duplicated : ndarray[bool]
    """
def mode(values: ArrayLike, dropna: bool = True, mask: npt.NDArray[np.bool_] | None = None) -> ArrayLike:
    """
    Returns the mode(s) of an array.

    Parameters
    ----------
    values : array-like
        Array over which to check for duplicate values.
    dropna : bool, default True
        Don't consider counts of NaN/NaT.

    Returns
    -------
    np.ndarray or ExtensionArray
    """
def rank(values: ArrayLike, axis: AxisInt = 0, method: str = 'average', na_option: str = 'keep', ascending: bool = True, pct: bool = False) -> npt.NDArray[np.float64]:
    """
    Rank the values along a given axis.

    Parameters
    ----------
    values : np.ndarray or ExtensionArray
        Array whose values will be ranked. The number of dimensions in this
        array must not exceed 2.
    axis : int, default 0
        Axis over which to perform rankings.
    method : {'average', 'min', 'max', 'first', 'dense'}, default 'average'
        The method by which tiebreaks are broken during the ranking.
    na_option : {'keep', 'top'}, default 'keep'
        The method by which NaNs are placed in the ranking.
        - ``keep``: rank each NaN value with a NaN ranking
        - ``top``: replace each NaN with either +/- inf so that they
                   there are ranked at the top
    ascending : bool, default True
        Whether or not the elements should be ranked in ascending order.
    pct : bool, default False
        Whether or not to the display the returned rankings in integer form
        (e.g. 1, 2, 3) or in percentile form (e.g. 0.333..., 0.666..., 1).
    """
def checked_add_with_arr(arr: npt.NDArray[np.int64], b: int | npt.NDArray[np.int64], arr_mask: npt.NDArray[np.bool_] | None = None, b_mask: npt.NDArray[np.bool_] | None = None) -> npt.NDArray[np.int64]:
    """
    Perform array addition that checks for underflow and overflow.

    Performs the addition of an int64 array and an int64 integer (or array)
    but checks that they do not result in overflow first. For elements that
    are indicated to be NaN, whether or not there is overflow for that element
    is automatically ignored.

    Parameters
    ----------
    arr : np.ndarray[int64] addend.
    b : array or scalar addend.
    arr_mask : np.ndarray[bool] or None, default None
        array indicating which elements to exclude from checking
    b_mask : np.ndarray[bool] or None, default None
        array or scalar indicating which element(s) to exclude from checking

    Returns
    -------
    sum : An array for elements x + b for each element x in arr if b is
          a scalar or an array for elements x + y for each element pair
          (x, y) in (arr, b).

    Raises
    ------
    OverflowError if any x + y exceeds the maximum or minimum int64 value.
    """
def take(arr, indices: TakeIndexer, axis: AxisInt = 0, allow_fill: bool = False, fill_value: Incomplete | None = None):
    """
    Take elements from an array.

    Parameters
    ----------
    arr : array-like or scalar value
        Non array-likes (sequences/scalars without a dtype) are coerced
        to an ndarray.
    indices : sequence of int or one-dimensional np.ndarray of int
        Indices to be taken.
    axis : int, default 0
        The axis over which to select values.
    allow_fill : bool, default False
        How to handle negative values in `indices`.

        * False: negative values in `indices` indicate positional indices
          from the right (the default). This is similar to :func:`numpy.take`.

        * True: negative values in `indices` indicate
          missing values. These values are set to `fill_value`. Any other
          negative values raise a ``ValueError``.

    fill_value : any, optional
        Fill value to use for NA-indices when `allow_fill` is True.
        This may be ``None``, in which case the default NA value for
        the type (``self.dtype.na_value``) is used.

        For multi-dimensional `arr`, each *element* is filled with
        `fill_value`.

    Returns
    -------
    ndarray or ExtensionArray
        Same type as the input.

    Raises
    ------
    IndexError
        When `indices` is out of bounds for the array.
    ValueError
        When the indexer contains negative values other than ``-1``
        and `allow_fill` is True.

    Notes
    -----
    When `allow_fill` is False, `indices` may be whatever dimensionality
    is accepted by NumPy for `arr`.

    When `allow_fill` is True, `indices` should be 1-D.

    See Also
    --------
    numpy.take : Take elements from an array along an axis.

    Examples
    --------
    >>> import pandas as pd

    With the default ``allow_fill=False``, negative numbers indicate
    positional indices from the right.

    >>> pd.api.extensions.take(np.array([10, 20, 30]), [0, 0, -1])
    array([10, 10, 30])

    Setting ``allow_fill=True`` will place `fill_value` in those positions.

    >>> pd.api.extensions.take(np.array([10, 20, 30]), [0, 0, -1], allow_fill=True)
    array([10., 10., nan])

    >>> pd.api.extensions.take(np.array([10, 20, 30]), [0, 0, -1], allow_fill=True,
    ...      fill_value=-10)
    array([ 10,  10, -10])
    """
def searchsorted(arr: ArrayLike, value: NumpyValueArrayLike | ExtensionArray, side: Literal['left', 'right'] = 'left', sorter: NumpySorter = None) -> npt.NDArray[np.intp] | np.intp:
    """
    Find indices where elements should be inserted to maintain order.

    Find the indices into a sorted array `arr` (a) such that, if the
    corresponding elements in `value` were inserted before the indices,
    the order of `arr` would be preserved.

    Assuming that `arr` is sorted:

    ======  ================================
    `side`  returned index `i` satisfies
    ======  ================================
    left    ``arr[i-1] < value <= self[i]``
    right   ``arr[i-1] <= value < self[i]``
    ======  ================================

    Parameters
    ----------
    arr: np.ndarray, ExtensionArray, Series
        Input array. If `sorter` is None, then it must be sorted in
        ascending order, otherwise `sorter` must be an array of indices
        that sort it.
    value : array-like or scalar
        Values to insert into `arr`.
    side : {'left', 'right'}, optional
        If 'left', the index of the first suitable location found is given.
        If 'right', return the last such index.  If there is no suitable
        index, return either 0 or N (where N is the length of `self`).
    sorter : 1-D array-like, optional
        Optional array of integer indices that sort array a into ascending
        order. They are typically the result of argsort.

    Returns
    -------
    array of ints or int
        If value is array-like, array of insertion points.
        If value is scalar, a single integer.

    See Also
    --------
    numpy.searchsorted : Similar method from NumPy.
    """
def diff(arr, n: int, axis: AxisInt = 0):
    """
    difference of n between self,
    analogous to s-s.shift(n)

    Parameters
    ----------
    arr : ndarray or ExtensionArray
    n : int
        number of periods
    axis : {0, 1}
        axis to shift on
    stacklevel : int, default 3
        The stacklevel for the lost dtype warning.

    Returns
    -------
    shifted
    """
def safe_sort(values, codes: Incomplete | None = None, use_na_sentinel: bool = True, assume_unique: bool = False, verify: bool = True) -> AnyArrayLike | tuple[AnyArrayLike, np.ndarray]:
    '''
    Sort ``values`` and reorder corresponding ``codes``.

    ``values`` should be unique if ``codes`` is not None.
    Safe for use with mixed types (int, str), orders ints before strs.

    Parameters
    ----------
    values : list-like
        Sequence; must be unique if ``codes`` is not None.
    codes : list_like, optional
        Indices to ``values``. All out of bound indices are treated as
        "not found" and will be masked with ``-1``.
    use_na_sentinel : bool, default True
        If True, the sentinel -1 will be used for NaN values. If False,
        NaN values will be encoded as non-negative integers and will not drop the
        NaN from the uniques of the values.
    assume_unique : bool, default False
        When True, ``values`` are assumed to be unique, which can speed up
        the calculation. Ignored when ``codes`` is None.
    verify : bool, default True
        Check if codes are out of bound for the values and put out of bound
        codes equal to ``-1``. If ``verify=False``, it is assumed there
        are no out of bound codes. Ignored when ``codes`` is None.

    Returns
    -------
    ordered : AnyArrayLike
        Sorted ``values``
    new_codes : ndarray
        Reordered ``codes``; returned when ``codes`` is not None.

    Raises
    ------
    TypeError
        * If ``values`` is not list-like or if ``codes`` is neither None
        nor list-like
        * If ``values`` cannot be sorted
    ValueError
        * If ``codes`` is not None and ``values`` contain duplicates.
    '''
def union_with_duplicates(lvals: ArrayLike | Index, rvals: ArrayLike | Index) -> ArrayLike | Index:
    """
    Extracts the union from lvals and rvals with respect to duplicates and nans in
    both arrays.

    Parameters
    ----------
    lvals: np.ndarray or ExtensionArray
        left values which is ordered in front.
    rvals: np.ndarray or ExtensionArray
        right values ordered after lvals.

    Returns
    -------
    np.ndarray or ExtensionArray
        Containing the unsorted union of both arrays.

    Notes
    -----
    Caller is responsible for ensuring lvals.dtype == rvals.dtype.
    """
