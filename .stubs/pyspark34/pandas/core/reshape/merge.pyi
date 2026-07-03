import numpy as np
from _typeshed import Incomplete
from pandas import ArrowDtype as ArrowDtype, Categorical as Categorical, DataFrame as DataFrame, Index as Index, MultiIndex as MultiIndex, Series as Series
from pandas._libs import Timedelta as Timedelta, lib as lib
from pandas._libs.lib import is_range_indexer as is_range_indexer
from pandas._typing import AnyArrayLike as AnyArrayLike, ArrayLike as ArrayLike, AxisInt as AxisInt, DtypeObj as DtypeObj, IndexLabel as IndexLabel, JoinHow as JoinHow, MergeHow as MergeHow, Shape as Shape, Suffixes as Suffixes, npt as npt
from pandas.core import groupby as groupby
from pandas.core.arrays import ArrowExtensionArray as ArrowExtensionArray, BaseMaskedArray as BaseMaskedArray, DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray as NDArrayBackedExtensionArray
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array
from pandas.core.dtypes.base import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.cast import find_common_type as find_common_type
from pandas.core.dtypes.common import ensure_float64 as ensure_float64, ensure_int64 as ensure_int64, ensure_object as ensure_object, is_array_like as is_array_like, is_bool as is_bool, is_bool_dtype as is_bool_dtype, is_categorical_dtype as is_categorical_dtype, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_float_dtype as is_float_dtype, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_number as is_number, is_numeric_dtype as is_numeric_dtype, is_object_dtype as is_object_dtype, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna, na_value_for_dtype as na_value_for_dtype
from pandas.core.indexes.api import default_index as default_index
from pandas.core.sorting import is_int64_overflow_possible as is_int64_overflow_possible
from pandas.errors import MergeError as MergeError
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, cache_readonly as cache_readonly
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Hashable, Literal, Sequence

def merge(left: DataFrame | Series, right: DataFrame | Series, how: MergeHow = 'inner', on: IndexLabel | None = None, left_on: IndexLabel | None = None, right_on: IndexLabel | None = None, left_index: bool = False, right_index: bool = False, sort: bool = False, suffixes: Suffixes = ('_x', '_y'), copy: bool | None = None, indicator: str | bool = False, validate: str | None = None) -> DataFrame: ...
def merge_ordered(left: DataFrame, right: DataFrame, on: IndexLabel | None = None, left_on: IndexLabel | None = None, right_on: IndexLabel | None = None, left_by: Incomplete | None = None, right_by: Incomplete | None = None, fill_method: str | None = None, suffixes: Suffixes = ('_x', '_y'), how: JoinHow = 'outer') -> DataFrame:
    '''
    Perform a merge for ordered data with optional filling/interpolation.

    Designed for ordered data like time series data. Optionally
    perform group-wise merge (see examples).

    Parameters
    ----------
    left : DataFrame or named Series
    right : DataFrame or named Series
    on : label or list
        Field names to join on. Must be found in both DataFrames.
    left_on : label or list, or array-like
        Field names to join on in left DataFrame. Can be a vector or list of
        vectors of the length of the DataFrame to use a particular vector as
        the join key instead of columns.
    right_on : label or list, or array-like
        Field names to join on in right DataFrame or vector/list of vectors per
        left_on docs.
    left_by : column name or list of column names
        Group left DataFrame by group columns and merge piece by piece with
        right DataFrame. Must be None if either left or right are a Series.
    right_by : column name or list of column names
        Group right DataFrame by group columns and merge piece by piece with
        left DataFrame. Must be None if either left or right are a Series.
    fill_method : {\'ffill\', None}, default None
        Interpolation method for data.
    suffixes : list-like, default is ("_x", "_y")
        A length-2 sequence where each element is optionally a string
        indicating the suffix to add to overlapping column names in
        `left` and `right` respectively. Pass a value of `None` instead
        of a string to indicate that the column name from `left` or
        `right` should be left as-is, with no suffix. At least one of the
        values must not be None.

    how : {\'left\', \'right\', \'outer\', \'inner\'}, default \'outer\'
        * left: use only keys from left frame (SQL: left outer join)
        * right: use only keys from right frame (SQL: right outer join)
        * outer: use union of keys from both frames (SQL: full outer join)
        * inner: use intersection of keys from both frames (SQL: inner join).

    Returns
    -------
    DataFrame
        The merged DataFrame output type will be the same as
        \'left\', if it is a subclass of DataFrame.

    See Also
    --------
    merge : Merge with a database-style join.
    merge_asof : Merge on nearest keys.

    Examples
    --------
    >>> from pandas import merge_ordered
    >>> df1 = pd.DataFrame(
    ...     {
    ...         "key": ["a", "c", "e", "a", "c", "e"],
    ...         "lvalue": [1, 2, 3, 1, 2, 3],
    ...         "group": ["a", "a", "a", "b", "b", "b"]
    ...     }
    ... )
    >>> df1
          key  lvalue group
    0   a       1     a
    1   c       2     a
    2   e       3     a
    3   a       1     b
    4   c       2     b
    5   e       3     b

    >>> df2 = pd.DataFrame({"key": ["b", "c", "d"], "rvalue": [1, 2, 3]})
    >>> df2
          key  rvalue
    0   b       1
    1   c       2
    2   d       3

    >>> merge_ordered(df1, df2, fill_method="ffill", left_by="group")
      key  lvalue group  rvalue
    0   a       1     a     NaN
    1   b       1     a     1.0
    2   c       2     a     2.0
    3   d       2     a     3.0
    4   e       3     a     3.0
    5   a       1     b     NaN
    6   b       1     b     1.0
    7   c       2     b     2.0
    8   d       2     b     3.0
    9   e       3     b     3.0
    '''
def merge_asof(left: DataFrame | Series, right: DataFrame | Series, on: IndexLabel | None = None, left_on: IndexLabel | None = None, right_on: IndexLabel | None = None, left_index: bool = False, right_index: bool = False, by: Incomplete | None = None, left_by: Incomplete | None = None, right_by: Incomplete | None = None, suffixes: Suffixes = ('_x', '_y'), tolerance: Incomplete | None = None, allow_exact_matches: bool = True, direction: str = 'backward') -> DataFrame:
    '''
    Perform a merge by key distance.

    This is similar to a left-join except that we match on nearest
    key rather than equal keys. Both DataFrames must be sorted by the key.

    For each row in the left DataFrame:

      - A "backward" search selects the last row in the right DataFrame whose
        \'on\' key is less than or equal to the left\'s key.

      - A "forward" search selects the first row in the right DataFrame whose
        \'on\' key is greater than or equal to the left\'s key.

      - A "nearest" search selects the row in the right DataFrame whose \'on\'
        key is closest in absolute distance to the left\'s key.

    The default is "backward" and is compatible in versions below 0.20.0.
    The direction parameter was added in version 0.20.0 and introduces
    "forward" and "nearest".

    Optionally match on equivalent keys with \'by\' before searching with \'on\'.

    Parameters
    ----------
    left : DataFrame or named Series
    right : DataFrame or named Series
    on : label
        Field name to join on. Must be found in both DataFrames.
        The data MUST be ordered. Furthermore this must be a numeric column,
        such as datetimelike, integer, or float. On or left_on/right_on
        must be given.
    left_on : label
        Field name to join on in left DataFrame.
    right_on : label
        Field name to join on in right DataFrame.
    left_index : bool
        Use the index of the left DataFrame as the join key.
    right_index : bool
        Use the index of the right DataFrame as the join key.
    by : column name or list of column names
        Match on these columns before performing merge operation.
    left_by : column name
        Field names to match on in the left DataFrame.
    right_by : column name
        Field names to match on in the right DataFrame.
    suffixes : 2-length sequence (tuple, list, ...)
        Suffix to apply to overlapping column names in the left and right
        side, respectively.
    tolerance : int or Timedelta, optional, default None
        Select asof tolerance within this range; must be compatible
        with the merge index.
    allow_exact_matches : bool, default True

        - If True, allow matching with the same \'on\' value
          (i.e. less-than-or-equal-to / greater-than-or-equal-to)
        - If False, don\'t match the same \'on\' value
          (i.e., strictly less-than / strictly greater-than).

    direction : \'backward\' (default), \'forward\', or \'nearest\'
        Whether to search for prior, subsequent, or closest matches.

    Returns
    -------
    DataFrame

    See Also
    --------
    merge : Merge with a database-style join.
    merge_ordered : Merge with optional filling/interpolation.

    Examples
    --------
    >>> left = pd.DataFrame({"a": [1, 5, 10], "left_val": ["a", "b", "c"]})
    >>> left
        a left_val
    0   1        a
    1   5        b
    2  10        c

    >>> right = pd.DataFrame({"a": [1, 2, 3, 6, 7], "right_val": [1, 2, 3, 6, 7]})
    >>> right
       a  right_val
    0  1          1
    1  2          2
    2  3          3
    3  6          6
    4  7          7

    >>> pd.merge_asof(left, right, on="a")
        a left_val  right_val
    0   1        a          1
    1   5        b          3
    2  10        c          7

    >>> pd.merge_asof(left, right, on="a", allow_exact_matches=False)
        a left_val  right_val
    0   1        a        NaN
    1   5        b        3.0
    2  10        c        7.0

    >>> pd.merge_asof(left, right, on="a", direction="forward")
        a left_val  right_val
    0   1        a        1.0
    1   5        b        6.0
    2  10        c        NaN

    >>> pd.merge_asof(left, right, on="a", direction="nearest")
        a left_val  right_val
    0   1        a          1
    1   5        b          6
    2  10        c          7

    We can use indexed DataFrames as well.

    >>> left = pd.DataFrame({"left_val": ["a", "b", "c"]}, index=[1, 5, 10])
    >>> left
       left_val
    1         a
    5         b
    10        c

    >>> right = pd.DataFrame({"right_val": [1, 2, 3, 6, 7]}, index=[1, 2, 3, 6, 7])
    >>> right
       right_val
    1          1
    2          2
    3          3
    6          6
    7          7

    >>> pd.merge_asof(left, right, left_index=True, right_index=True)
       left_val  right_val
    1         a          1
    5         b          3
    10        c          7

    Here is a real-world times-series example

    >>> quotes = pd.DataFrame(
    ...     {
    ...         "time": [
    ...             pd.Timestamp("2016-05-25 13:30:00.023"),
    ...             pd.Timestamp("2016-05-25 13:30:00.023"),
    ...             pd.Timestamp("2016-05-25 13:30:00.030"),
    ...             pd.Timestamp("2016-05-25 13:30:00.041"),
    ...             pd.Timestamp("2016-05-25 13:30:00.048"),
    ...             pd.Timestamp("2016-05-25 13:30:00.049"),
    ...             pd.Timestamp("2016-05-25 13:30:00.072"),
    ...             pd.Timestamp("2016-05-25 13:30:00.075")
    ...         ],
    ...         "ticker": [
    ...                "GOOG",
    ...                "MSFT",
    ...                "MSFT",
    ...                "MSFT",
    ...                "GOOG",
    ...                "AAPL",
    ...                "GOOG",
    ...                "MSFT"
    ...            ],
    ...            "bid": [720.50, 51.95, 51.97, 51.99, 720.50, 97.99, 720.50, 52.01],
    ...            "ask": [720.93, 51.96, 51.98, 52.00, 720.93, 98.01, 720.88, 52.03]
    ...     }
    ... )
    >>> quotes
                         time ticker     bid     ask
    0 2016-05-25 13:30:00.023   GOOG  720.50  720.93
    1 2016-05-25 13:30:00.023   MSFT   51.95   51.96
    2 2016-05-25 13:30:00.030   MSFT   51.97   51.98
    3 2016-05-25 13:30:00.041   MSFT   51.99   52.00
    4 2016-05-25 13:30:00.048   GOOG  720.50  720.93
    5 2016-05-25 13:30:00.049   AAPL   97.99   98.01
    6 2016-05-25 13:30:00.072   GOOG  720.50  720.88
    7 2016-05-25 13:30:00.075   MSFT   52.01   52.03

    >>> trades = pd.DataFrame(
    ...        {
    ...            "time": [
    ...                pd.Timestamp("2016-05-25 13:30:00.023"),
    ...                pd.Timestamp("2016-05-25 13:30:00.038"),
    ...                pd.Timestamp("2016-05-25 13:30:00.048"),
    ...                pd.Timestamp("2016-05-25 13:30:00.048"),
    ...                pd.Timestamp("2016-05-25 13:30:00.048")
    ...            ],
    ...            "ticker": ["MSFT", "MSFT", "GOOG", "GOOG", "AAPL"],
    ...            "price": [51.95, 51.95, 720.77, 720.92, 98.0],
    ...            "quantity": [75, 155, 100, 100, 100]
    ...        }
    ...    )
    >>> trades
                         time ticker   price  quantity
    0 2016-05-25 13:30:00.023   MSFT   51.95        75
    1 2016-05-25 13:30:00.038   MSFT   51.95       155
    2 2016-05-25 13:30:00.048   GOOG  720.77       100
    3 2016-05-25 13:30:00.048   GOOG  720.92       100
    4 2016-05-25 13:30:00.048   AAPL   98.00       100

    By default we are taking the asof of the quotes

    >>> pd.merge_asof(trades, quotes, on="time", by="ticker")
                         time ticker   price  quantity     bid     ask
    0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
    1 2016-05-25 13:30:00.038   MSFT   51.95       155   51.97   51.98
    2 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
    3 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93
    4 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN

    We only asof within 2ms between the quote time and the trade time

    >>> pd.merge_asof(
    ...     trades, quotes, on="time", by="ticker", tolerance=pd.Timedelta("2ms")
    ... )
                         time ticker   price  quantity     bid     ask
    0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
    1 2016-05-25 13:30:00.038   MSFT   51.95       155     NaN     NaN
    2 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
    3 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93
    4 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN

    We only asof within 10ms between the quote time and the trade time
    and we exclude exact matches on time. However *prior* data will
    propagate forward

    >>> pd.merge_asof(
    ...     trades,
    ...     quotes,
    ...     on="time",
    ...     by="ticker",
    ...     tolerance=pd.Timedelta("10ms"),
    ...     allow_exact_matches=False
    ... )
                         time ticker   price  quantity     bid     ask
    0 2016-05-25 13:30:00.023   MSFT   51.95        75     NaN     NaN
    1 2016-05-25 13:30:00.038   MSFT   51.95       155   51.97   51.98
    2 2016-05-25 13:30:00.048   GOOG  720.77       100     NaN     NaN
    3 2016-05-25 13:30:00.048   GOOG  720.92       100     NaN     NaN
    4 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN
    '''

class _MergeOperation:
    """
    Perform a database (SQL) merge operation between two DataFrame or Series
    objects using either columns as keys or their row indexes
    """
    how: MergeHow | Literal['asof']
    on: IndexLabel | None
    left_on: Sequence[Hashable | AnyArrayLike]
    right_on: Sequence[Hashable | AnyArrayLike]
    left_index: bool
    right_index: bool
    axis: AxisInt
    bm_axis: AxisInt
    sort: bool
    suffixes: Suffixes
    copy: bool
    indicator: str | bool
    validate: str | None
    join_names: list[Hashable]
    right_join_keys: list[AnyArrayLike]
    left_join_keys: list[AnyArrayLike]
    left: Incomplete
    right: Incomplete
    def __init__(self, left: DataFrame | Series, right: DataFrame | Series, how: MergeHow | Literal['asof'] = 'inner', on: IndexLabel | None = None, left_on: IndexLabel | None = None, right_on: IndexLabel | None = None, axis: AxisInt = 1, left_index: bool = False, right_index: bool = False, sort: bool = True, suffixes: Suffixes = ('_x', '_y'), indicator: str | bool = False, validate: str | None = None) -> None: ...
    def get_result(self, copy: bool | None = True) -> DataFrame: ...

def get_join_indexers(left_keys, right_keys, sort: bool = False, how: MergeHow | Literal['asof'] = 'inner', **kwargs) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]:
    """

    Parameters
    ----------
    left_keys : ndarray, Index, Series
    right_keys : ndarray, Index, Series
    sort : bool, default False
    how : {'inner', 'outer', 'left', 'right'}, default 'inner'

    Returns
    -------
    np.ndarray[np.intp]
        Indexer into the left_keys.
    np.ndarray[np.intp]
        Indexer into the right_keys.
    """
def restore_dropped_levels_multijoin(left: MultiIndex, right: MultiIndex, dropped_level_names, join_index: Index, lindexer: npt.NDArray[np.intp], rindexer: npt.NDArray[np.intp]) -> tuple[list[Index], npt.NDArray[np.intp], list[Hashable]]:
    """
    *this is an internal non-public method*

    Returns the levels, labels and names of a multi-index to multi-index join.
    Depending on the type of join, this method restores the appropriate
    dropped levels of the joined multi-index.
    The method relies on lindexer, rindexer which hold the index positions of
    left and right, where a join was feasible

    Parameters
    ----------
    left : MultiIndex
        left index
    right : MultiIndex
        right index
    dropped_level_names : str array
        list of non-common level names
    join_index : Index
        the index of the join between the
        common levels of left and right
    lindexer : np.ndarray[np.intp]
        left indexer
    rindexer : np.ndarray[np.intp]
        right indexer

    Returns
    -------
    levels : list of Index
        levels of combined multiindexes
    labels : np.ndarray[np.intp]
        labels of combined multiindexes
    names : List[Hashable]
        names of combined multiindex levels

    """

class _OrderedMerge(_MergeOperation):
    fill_method: Incomplete
    def __init__(self, left: DataFrame | Series, right: DataFrame | Series, on: IndexLabel | None = None, left_on: IndexLabel | None = None, right_on: IndexLabel | None = None, left_index: bool = False, right_index: bool = False, axis: AxisInt = 1, suffixes: Suffixes = ('_x', '_y'), fill_method: str | None = None, how: JoinHow | Literal['asof'] = 'outer') -> None: ...
    def get_result(self, copy: bool | None = True) -> DataFrame: ...

class _AsOfMerge(_OrderedMerge):
    by: Incomplete
    left_by: Incomplete
    right_by: Incomplete
    tolerance: Incomplete
    allow_exact_matches: Incomplete
    direction: Incomplete
    def __init__(self, left: DataFrame | Series, right: DataFrame | Series, on: IndexLabel | None = None, left_on: IndexLabel | None = None, right_on: IndexLabel | None = None, left_index: bool = False, right_index: bool = False, by: Incomplete | None = None, left_by: Incomplete | None = None, right_by: Incomplete | None = None, axis: AxisInt = 1, suffixes: Suffixes = ('_x', '_y'), copy: bool = True, fill_method: str | None = None, how: Literal['asof'] = 'asof', tolerance: Incomplete | None = None, allow_exact_matches: bool = True, direction: str = 'backward') -> None: ...
