from _typeshed import Incomplete
from pandas import Categorical as Categorical, DataFrame as DataFrame, DatetimeIndex as DatetimeIndex, Index as Index, IntervalIndex as IntervalIndex, MultiIndex as MultiIndex, PeriodIndex as PeriodIndex, RangeIndex as RangeIndex, Series as Series, TimedeltaIndex as TimedeltaIndex
from pandas._libs.missing import is_matching_na as is_matching_na
from pandas._libs.sparse import SparseIndex as SparseIndex
from pandas._libs.tslibs.np_datetime import compare_mismatched_resolutions as compare_mismatched_resolutions
from pandas.core.algorithms import take_nd as take_nd
from pandas.core.arrays import DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray, IntervalArray as IntervalArray, PeriodArray as PeriodArray, TimedeltaArray as TimedeltaArray
from pandas.core.arrays.datetimelike import DatetimeLikeArrayMixin as DatetimeLikeArrayMixin
from pandas.core.arrays.string_ import StringDtype as StringDtype
from pandas.core.dtypes.common import is_bool as is_bool, is_categorical_dtype as is_categorical_dtype, is_extension_array_dtype as is_extension_array_dtype, is_integer_dtype as is_integer_dtype, is_interval_dtype as is_interval_dtype, is_number as is_number, is_numeric_dtype as is_numeric_dtype, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype, DatetimeTZDtype as DatetimeTZDtype, PandasDtype as PandasDtype
from pandas.core.dtypes.missing import array_equivalent as array_equivalent
from pandas.core.indexes.api import safe_sort_index as safe_sort_index
from pandas.io.formats.printing import pprint_thing as pprint_thing
from typing import Literal

def assert_almost_equal(left, right, check_dtype: bool | Literal['equiv'] = 'equiv', rtol: float = 1e-05, atol: float = 1e-08, **kwargs) -> None:
    """
    Check that the left and right objects are approximately equal.

    By approximately equal, we refer to objects that are numbers or that
    contain numbers which may be equivalent to specific levels of precision.

    Parameters
    ----------
    left : object
    right : object
    check_dtype : bool or {'equiv'}, default 'equiv'
        Check dtype if both a and b are the same type. If 'equiv' is passed in,
        then `RangeIndex` and `Index` with int64 dtype are also considered
        equivalent when doing type checking.
    rtol : float, default 1e-5
        Relative tolerance.

        .. versionadded:: 1.1.0
    atol : float, default 1e-8
        Absolute tolerance.

        .. versionadded:: 1.1.0
    """
def assert_dict_equal(left, right, compare_keys: bool = True) -> None: ...
def assert_index_equal(left: Index, right: Index, exact: bool | str = 'equiv', check_names: bool = True, check_exact: bool = True, check_categorical: bool = True, check_order: bool = True, rtol: float = 1e-05, atol: float = 1e-08, obj: str = 'Index') -> None:
    """
    Check that left and right Index are equal.

    Parameters
    ----------
    left : Index
    right : Index
    exact : bool or {'equiv'}, default 'equiv'
        Whether to check the Index class, dtype and inferred_type
        are identical. If 'equiv', then RangeIndex can be substituted for
        Index with an int64 dtype as well.
    check_names : bool, default True
        Whether to check the names attribute.
    check_exact : bool, default True
        Whether to compare number exactly.
    check_categorical : bool, default True
        Whether to compare internal Categorical exactly.
    check_order : bool, default True
        Whether to compare the order of index entries as well as their values.
        If True, both indexes must contain the same elements, in the same order.
        If False, both indexes must contain the same elements, but in any order.

        .. versionadded:: 1.2.0
    rtol : float, default 1e-5
        Relative tolerance. Only used when check_exact is False.

        .. versionadded:: 1.1.0
    atol : float, default 1e-8
        Absolute tolerance. Only used when check_exact is False.

        .. versionadded:: 1.1.0
    obj : str, default 'Index'
        Specify object name being compared, internally used to show appropriate
        assertion message.

    Examples
    --------
    >>> from pandas import testing as tm
    >>> a = pd.Index([1, 2, 3])
    >>> b = pd.Index([1, 2, 3])
    >>> tm.assert_index_equal(a, b)
    """
def assert_class_equal(left, right, exact: bool | str = True, obj: str = 'Input') -> None:
    """
    Checks classes are equal.
    """
def assert_attr_equal(attr: str, left, right, obj: str = 'Attributes') -> None:
    """
    Check attributes are equal. Both objects must have attribute.

    Parameters
    ----------
    attr : str
        Attribute name being compared.
    left : object
    right : object
    obj : str, default 'Attributes'
        Specify object name being compared, internally used to show appropriate
        assertion message
    """
def assert_is_valid_plot_return_object(objs) -> None: ...
def assert_is_sorted(seq) -> None:
    """Assert that the sequence is sorted."""
def assert_categorical_equal(left, right, check_dtype: bool = True, check_category_order: bool = True, obj: str = 'Categorical') -> None:
    """
    Test that Categoricals are equivalent.

    Parameters
    ----------
    left : Categorical
    right : Categorical
    check_dtype : bool, default True
        Check that integer dtype of the codes are the same.
    check_category_order : bool, default True
        Whether the order of the categories should be compared, which
        implies identical integer codes.  If False, only the resulting
        values are compared.  The ordered attribute is
        checked regardless.
    obj : str, default 'Categorical'
        Specify object name being compared, internally used to show appropriate
        assertion message.
    """
def assert_interval_array_equal(left, right, exact: bool | Literal['equiv'] = 'equiv', obj: str = 'IntervalArray') -> None:
    """
    Test that two IntervalArrays are equivalent.

    Parameters
    ----------
    left, right : IntervalArray
        The IntervalArrays to compare.
    exact : bool or {'equiv'}, default 'equiv'
        Whether to check the Index class, dtype and inferred_type
        are identical. If 'equiv', then RangeIndex can be substituted for
        Index with an int64 dtype as well.
    obj : str, default 'IntervalArray'
        Specify object name being compared, internally used to show appropriate
        assertion message
    """
def assert_period_array_equal(left, right, obj: str = 'PeriodArray') -> None: ...
def assert_datetime_array_equal(left, right, obj: str = 'DatetimeArray', check_freq: bool = True) -> None: ...
def assert_timedelta_array_equal(left, right, obj: str = 'TimedeltaArray', check_freq: bool = True) -> None: ...
def raise_assert_detail(obj, message, left, right, diff: Incomplete | None = None, first_diff: Incomplete | None = None, index_values: Incomplete | None = None) -> None: ...
def assert_numpy_array_equal(left, right, strict_nan: bool = False, check_dtype: bool | Literal['equiv'] = True, err_msg: Incomplete | None = None, check_same: Incomplete | None = None, obj: str = 'numpy array', index_values: Incomplete | None = None) -> None:
    """
    Check that 'np.ndarray' is equivalent.

    Parameters
    ----------
    left, right : numpy.ndarray or iterable
        The two arrays to be compared.
    strict_nan : bool, default False
        If True, consider NaN and None to be different.
    check_dtype : bool, default True
        Check dtype if both a and b are np.ndarray.
    err_msg : str, default None
        If provided, used as assertion message.
    check_same : None|'copy'|'same', default None
        Ensure left and right refer/do not refer to the same memory area.
    obj : str, default 'numpy array'
        Specify object name being compared, internally used to show appropriate
        assertion message.
    index_values : numpy.ndarray, default None
        optional index (shared by both left and right), used in output.
    """
def assert_extension_array_equal(left, right, check_dtype: bool | Literal['equiv'] = True, index_values: Incomplete | None = None, check_exact: bool = False, rtol: float = 1e-05, atol: float = 1e-08, obj: str = 'ExtensionArray') -> None:
    """
    Check that left and right ExtensionArrays are equal.

    Parameters
    ----------
    left, right : ExtensionArray
        The two arrays to compare.
    check_dtype : bool, default True
        Whether to check if the ExtensionArray dtypes are identical.
    index_values : numpy.ndarray, default None
        Optional index (shared by both left and right), used in output.
    check_exact : bool, default False
        Whether to compare number exactly.
    rtol : float, default 1e-5
        Relative tolerance. Only used when check_exact is False.

        .. versionadded:: 1.1.0
    atol : float, default 1e-8
        Absolute tolerance. Only used when check_exact is False.

        .. versionadded:: 1.1.0
    obj : str, default 'ExtensionArray'
        Specify object name being compared, internally used to show appropriate
        assertion message.

        .. versionadded:: 2.0.0

    Notes
    -----
    Missing values are checked separately from valid values.
    A mask of missing values is computed for each and checked to match.
    The remaining all-valid values are cast to object dtype and checked.

    Examples
    --------
    >>> from pandas import testing as tm
    >>> a = pd.Series([1, 2, 3, 4])
    >>> b, c = a.array, a.array
    >>> tm.assert_extension_array_equal(b, c)
    """
def assert_series_equal(left, right, check_dtype: bool | Literal['equiv'] = True, check_index_type: bool | Literal['equiv'] = 'equiv', check_series_type: bool = True, check_names: bool = True, check_exact: bool = False, check_datetimelike_compat: bool = False, check_categorical: bool = True, check_category_order: bool = True, check_freq: bool = True, check_flags: bool = True, rtol: float = 1e-05, atol: float = 1e-08, obj: str = 'Series', *, check_index: bool = True, check_like: bool = False) -> None:
    """
    Check that left and right Series are equal.

    Parameters
    ----------
    left : Series
    right : Series
    check_dtype : bool, default True
        Whether to check the Series dtype is identical.
    check_index_type : bool or {'equiv'}, default 'equiv'
        Whether to check the Index class, dtype and inferred_type
        are identical.
    check_series_type : bool, default True
         Whether to check the Series class is identical.
    check_names : bool, default True
        Whether to check the Series and Index names attribute.
    check_exact : bool, default False
        Whether to compare number exactly.
    check_datetimelike_compat : bool, default False
        Compare datetime-like which is comparable ignoring dtype.
    check_categorical : bool, default True
        Whether to compare internal Categorical exactly.
    check_category_order : bool, default True
        Whether to compare category order of internal Categoricals.

        .. versionadded:: 1.0.2
    check_freq : bool, default True
        Whether to check the `freq` attribute on a DatetimeIndex or TimedeltaIndex.

        .. versionadded:: 1.1.0
    check_flags : bool, default True
        Whether to check the `flags` attribute.

        .. versionadded:: 1.2.0

    rtol : float, default 1e-5
        Relative tolerance. Only used when check_exact is False.

        .. versionadded:: 1.1.0
    atol : float, default 1e-8
        Absolute tolerance. Only used when check_exact is False.

        .. versionadded:: 1.1.0
    obj : str, default 'Series'
        Specify object name being compared, internally used to show appropriate
        assertion message.
    check_index : bool, default True
        Whether to check index equivalence. If False, then compare only values.

        .. versionadded:: 1.3.0
    check_like : bool, default False
        If True, ignore the order of the index. Must be False if check_index is False.
        Note: same labels must be with the same data.

        .. versionadded:: 1.5.0

    Examples
    --------
    >>> from pandas import testing as tm
    >>> a = pd.Series([1, 2, 3, 4])
    >>> b = pd.Series([1, 2, 3, 4])
    >>> tm.assert_series_equal(a, b)
    """
def assert_frame_equal(left, right, check_dtype: bool | Literal['equiv'] = True, check_index_type: bool | Literal['equiv'] = 'equiv', check_column_type: bool | Literal['equiv'] = 'equiv', check_frame_type: bool = True, check_names: bool = True, by_blocks: bool = False, check_exact: bool = False, check_datetimelike_compat: bool = False, check_categorical: bool = True, check_like: bool = False, check_freq: bool = True, check_flags: bool = True, rtol: float = 1e-05, atol: float = 1e-08, obj: str = 'DataFrame') -> None:
    '''
    Check that left and right DataFrame are equal.

    This function is intended to compare two DataFrames and output any
    differences. It is mostly intended for use in unit tests.
    Additional parameters allow varying the strictness of the
    equality checks performed.

    Parameters
    ----------
    left : DataFrame
        First DataFrame to compare.
    right : DataFrame
        Second DataFrame to compare.
    check_dtype : bool, default True
        Whether to check the DataFrame dtype is identical.
    check_index_type : bool or {\'equiv\'}, default \'equiv\'
        Whether to check the Index class, dtype and inferred_type
        are identical.
    check_column_type : bool or {\'equiv\'}, default \'equiv\'
        Whether to check the columns class, dtype and inferred_type
        are identical. Is passed as the ``exact`` argument of
        :func:`assert_index_equal`.
    check_frame_type : bool, default True
        Whether to check the DataFrame class is identical.
    check_names : bool, default True
        Whether to check that the `names` attribute for both the `index`
        and `column` attributes of the DataFrame is identical.
    by_blocks : bool, default False
        Specify how to compare internal data. If False, compare by columns.
        If True, compare by blocks.
    check_exact : bool, default False
        Whether to compare number exactly.
    check_datetimelike_compat : bool, default False
        Compare datetime-like which is comparable ignoring dtype.
    check_categorical : bool, default True
        Whether to compare internal Categorical exactly.
    check_like : bool, default False
        If True, ignore the order of index & columns.
        Note: index labels must match their respective rows
        (same as in columns) - same labels must be with the same data.
    check_freq : bool, default True
        Whether to check the `freq` attribute on a DatetimeIndex or TimedeltaIndex.

        .. versionadded:: 1.1.0
    check_flags : bool, default True
        Whether to check the `flags` attribute.
    rtol : float, default 1e-5
        Relative tolerance. Only used when check_exact is False.

        .. versionadded:: 1.1.0
    atol : float, default 1e-8
        Absolute tolerance. Only used when check_exact is False.

        .. versionadded:: 1.1.0
    obj : str, default \'DataFrame\'
        Specify object name being compared, internally used to show appropriate
        assertion message.

    See Also
    --------
    assert_series_equal : Equivalent method for asserting Series equality.
    DataFrame.equals : Check DataFrame equality.

    Examples
    --------
    This example shows comparing two DataFrames that are equal
    but with columns of differing dtypes.

    >>> from pandas.testing import assert_frame_equal
    >>> df1 = pd.DataFrame({\'a\': [1, 2], \'b\': [3, 4]})
    >>> df2 = pd.DataFrame({\'a\': [1, 2], \'b\': [3.0, 4.0]})

    df1 equals itself.

    >>> assert_frame_equal(df1, df1)

    df1 differs from df2 as column \'b\' is of a different type.

    >>> assert_frame_equal(df1, df2)
    Traceback (most recent call last):
    ...
    AssertionError: Attributes of DataFrame.iloc[:, 1] (column name="b") are different

    Attribute "dtype" are different
    [left]:  int64
    [right]: float64

    Ignore differing dtypes in columns with check_dtype.

    >>> assert_frame_equal(df1, df2, check_dtype=False)
    '''
def assert_equal(left, right, **kwargs) -> None:
    """
    Wrapper for tm.assert_*_equal to dispatch to the appropriate test function.

    Parameters
    ----------
    left, right : Index, Series, DataFrame, ExtensionArray, or np.ndarray
        The two items to be compared.
    **kwargs
        All keyword arguments are passed through to the underlying assert method.
    """
def assert_sp_array_equal(left, right) -> None:
    """
    Check that the left and right SparseArray are equal.

    Parameters
    ----------
    left : SparseArray
    right : SparseArray
    """
def assert_contains_all(iterable, dic) -> None: ...
def assert_copy(iter1, iter2, **eql_kwargs) -> None:
    """
    iter1, iter2: iterables that produce elements
    comparable with assert_almost_equal

    Checks that the elements are equal, but not
    the same object. (Does not check that items
    in sequences are also not the same object)
    """
def is_extension_array_dtype_and_needs_i8_conversion(left_dtype, right_dtype) -> bool:
    """
    Checks that we have the combination of an ExtensionArraydtype and
    a dtype that should be converted to int64

    Returns
    -------
    bool

    Related to issue #37609
    """
def assert_indexing_slices_equivalent(ser: Series, l_slc: slice, i_slc: slice) -> None:
    """
    Check that ser.iloc[i_slc] matches ser.loc[l_slc] and, if applicable,
    ser[l_slc].
    """
def assert_metadata_equivalent(left: DataFrame | Series, right: DataFrame | Series | None = None) -> None:
    """
    Check that ._metadata attributes are equivalent.
    """
