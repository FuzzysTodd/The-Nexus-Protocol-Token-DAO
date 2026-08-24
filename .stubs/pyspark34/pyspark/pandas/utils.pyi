import pandas as pd
from pyspark.pandas._typing import Axis as Axis, DataFrameOrSeries as DataFrameOrSeries, Label as Label, Name as Name
from pyspark.pandas.base import IndexOpsMixin as IndexOpsMixin
from pyspark.pandas.frame import DataFrame as DataFrame
from pyspark.pandas.indexes.base import Index as Index
from pyspark.pandas.internal import InternalFrame as InternalFrame
from pyspark.pandas.series import Series as Series
from pyspark.pandas.typedef.typehints import as_spark_type as as_spark_type
from pyspark.sql import Column as Column, DataFrame as SparkDataFrame, SparkSession as SparkSession
from pyspark.sql.types import DoubleType as DoubleType
from typing import Any, Callable, Dict, Iterator, List, Tuple, overload

ERROR_MESSAGE_CANNOT_COMBINE: str
SPARK_CONF_ARROW_ENABLED: str

class PandasAPIOnSparkAdviceWarning(Warning): ...

def same_anchor(this: DataFrame | IndexOpsMixin | InternalFrame, that: DataFrame | IndexOpsMixin | InternalFrame) -> bool:
    """
    Check if the anchors of the given DataFrame or Series are the same or not.
    """
def combine_frames(this: DataFrame, *args: DataFrameOrSeries, how: str = 'full', preserve_order_column: bool = False) -> DataFrame:
    """
    This method combines `this` DataFrame with a different `that` DataFrame or
    Series from a different DataFrame.

    It returns a DataFrame that has prefix `this_` and `that_` to distinct
    the columns names from both DataFrames

    It internally performs a join operation which can be expensive in general.
    So, if `compute.ops_on_diff_frames` option is False,
    this method throws an exception.
    """
def align_diff_frames(resolve_func: Callable[[DataFrame, List[Label], List[Label]], Iterator[Tuple['Series', Label]]], this: DataFrame, that: DataFrame, fillna: bool = True, how: str = 'full', preserve_order_column: bool = False) -> DataFrame:
    '''
    This method aligns two different DataFrames with a given `func`. Columns are resolved and
    handled within the given `func`.
    To use this, `compute.ops_on_diff_frames` should be True, for now.

    :param resolve_func: Takes aligned (joined) DataFrame, the column of the current DataFrame, and
        the column of another DataFrame. It returns an iterable that produces Series.

        >>> from pyspark.pandas.config import set_option, reset_option
        >>>
        >>> set_option("compute.ops_on_diff_frames", True)
        >>>
        >>> psdf1 = ps.DataFrame({\'a\': [9, 8, 7, 6, 5, 4, 3, 2, 1]})
        >>> psdf2 = ps.DataFrame({\'a\': [9, 8, 7, 6, 5, 4, 3, 2, 1]})
        >>>
        >>> def func(psdf, this_column_labels, that_column_labels):
        ...    psdf  # conceptually this is A + B.
        ...
        ...    # Within this function, Series from A or B can be performed against `psdf`.
        ...    this_label = this_column_labels[0]  # this is (\'a\',) from psdf1.
        ...    that_label = that_column_labels[0]  # this is (\'a\',) from psdf2.
        ...    new_series = (psdf[this_label] - psdf[that_label]).rename(str(this_label))
        ...
        ...    # This new series will be placed in new DataFrame.
        ...    yield (new_series, this_label)
        >>>
        >>>
        >>> align_diff_frames(func, psdf1, psdf2).sort_index()
           a
        0  0
        1  0
        2  0
        3  0
        4  0
        5  0
        6  0
        7  0
        8  0
        >>> reset_option("compute.ops_on_diff_frames")

    :param this: a DataFrame to align
    :param that: another DataFrame to align
    :param fillna: If True, it fills missing values in non-common columns in both `this` and `that`.
        Otherwise, it returns as are.
    :param how: join way. In addition, it affects how `resolve_func` resolves the column conflict.
        - full: `resolve_func` should resolve only common columns from \'this\' and \'that\' DataFrames.
            For instance, if \'this\' has columns A, B, C and that has B, C, D, `this_columns` and
            \'that_columns\' in this function are B, C and B, C.
        - left: `resolve_func` should resolve columns including `that` column.
            For instance, if \'this\' has columns A, B, C and that has B, C, D, `this_columns` is
            B, C but `that_columns` are B, C, D.
        - inner: Same as \'full\' mode; however, internally performs inner join instead.
    :return: Aligned DataFrame
    '''
def is_testing() -> bool:
    """Indicates whether Spark is currently running tests."""
def default_session() -> SparkSession: ...
def sql_conf(pairs: Dict[str, Any], *, spark: SparkSession | None = None) -> Iterator[None]:
    """
    A convenient context manager to set `value` to the Spark SQL configuration `key` and
    then restores it back when it exits.
    """
def validate_arguments_and_invoke_function(pobj: pd.DataFrame | pd.Series, pandas_on_spark_func: Callable, pandas_func: Callable, input_args: Dict) -> Any:
    '''
    Invokes a pandas function.

    This is created because different versions of pandas support different parameters, and as a
    result when we code against the latest version, our users might get a confusing
    "got an unexpected keyword argument" error if they are using an older version of pandas.

    This function validates all the arguments, removes the ones that are not supported if they
    are simply the default value (i.e. most likely the user didn\'t explicitly specify it). It
    throws a TypeError if the user explicitly specifies an argument that is not supported by the
    pandas version available.

    For example usage, look at DataFrame.to_html().

    :param pobj: the pandas DataFrame or Series to operate on
    :param pandas_on_spark_func: pandas-on-Spark function, used to get default parameter values
    :param pandas_func: pandas function, used to check whether pandas supports all the arguments
    :param input_args: arguments to pass to the pandas function, often created by using locals().
                       Make sure locals() call is at the top of the function so it captures only
                       input parameters, rather than local variables.
    :return: whatever pandas_func returns
    '''
def lazy_property(fn):
    """
    Decorator that makes a property lazy-evaluated.

    Copied from https://stevenloria.com/lazy-properties/
    """
def scol_for(sdf: SparkDataFrame, column_name: str) -> Column:
    """Return Spark Column for the given column name."""
def column_labels_level(column_labels: List[Label]) -> int:
    """Return the level of the column index."""
def name_like_string(name: Name | None) -> str:
    """
    Return the name-like strings from str or tuple of str

    Examples
    --------
    >>> name = 'abc'
    >>> name_like_string(name)
    'abc'

    >>> name = ('abc',)
    >>> name_like_string(name)
    'abc'

    >>> name = ('a', 'b', 'c')
    >>> name_like_string(name)
    '(a, b, c)'
    """
def is_name_like_tuple(value: Any, allow_none: bool = True, check_type: bool = False) -> bool:
    """
    Check the given tuple is to be able to be used as a name.

    Examples
    --------
    >>> is_name_like_tuple(('abc',))
    True
    >>> is_name_like_tuple((1,))
    True
    >>> is_name_like_tuple(('abc', 1, None))
    True
    >>> is_name_like_tuple(('abc', 1, None), check_type=True)
    True
    >>> is_name_like_tuple((1.0j,))
    True
    >>> is_name_like_tuple(tuple())
    False
    >>> is_name_like_tuple((list('abc'),))
    False
    >>> is_name_like_tuple(('abc', 1, None), allow_none=False)
    False
    >>> is_name_like_tuple((1.0j,), check_type=True)
    False
    """
def is_name_like_value(value: Any, allow_none: bool = True, allow_tuple: bool = True, check_type: bool = False) -> bool:
    """
    Check the given value is like a name.

    Examples
    --------
    >>> is_name_like_value('abc')
    True
    >>> is_name_like_value(1)
    True
    >>> is_name_like_value(None)
    True
    >>> is_name_like_value(('abc',))
    True
    >>> is_name_like_value(1.0j)
    True
    >>> is_name_like_value(list('abc'))
    False
    >>> is_name_like_value(None, allow_none=False)
    False
    >>> is_name_like_value(('abc',), allow_tuple=False)
    False
    >>> is_name_like_value(1.0j, check_type=True)
    False
    """
def validate_axis(axis: Axis | None = 0, none_axis: int = 0) -> int:
    """Check the given axis is valid."""
def validate_bool_kwarg(value: Any, arg_name: str) -> bool | None:
    """Ensures that argument passed in arg_name is of type bool."""
def validate_how(how: str) -> str:
    """Check the given how for join is valid."""
def validate_mode(mode: str) -> str:
    """Check the given mode for writing is valid."""
@overload
def verify_temp_column_name(df: SparkDataFrame, column_name_or_label: str) -> str: ...
@overload
def verify_temp_column_name(df: DataFrame, column_name_or_label: Name) -> Label: ...
def spark_column_equals(left: Column, right: Column) -> bool:
    '''
    Check both `left` and `right` have the same expressions.

    >>> spark_column_equals(F.lit(0), F.lit(0))
    True
    >>> spark_column_equals(F.lit(0) + 1, F.lit(0) + 1)
    True
    >>> spark_column_equals(F.lit(0) + 1, F.lit(0) + 2)
    False
    >>> sdf1 = ps.DataFrame({"x": [\'a\', \'b\', \'c\']}).to_spark()
    >>> spark_column_equals(sdf1["x"] + 1, sdf1["x"] + 1)
    True
    >>> sdf2 = ps.DataFrame({"x": [\'a\', \'b\', \'c\']}).to_spark()
    >>> spark_column_equals(sdf1["x"] + 1, sdf2["x"] + 1)
    False
    '''
def compare_null_first(left: Column, right: Column, comp: Callable[[Column, Column], Column]) -> Column: ...
def compare_null_last(left: Column, right: Column, comp: Callable[[Column, Column], Column]) -> Column: ...
def compare_disallow_null(left: Column, right: Column, comp: Callable[[Column, Column], Column]) -> Column: ...
def compare_allow_null(left: Column, right: Column, comp: Callable[[Column, Column], Column]) -> Column: ...
def log_advice(message: str) -> None:
    """
    Display advisory logs for functions to be aware of when using pandas API on Spark
    for the existing pandas/PySpark users who may not be familiar with distributed environments
    or the behavior of pandas.
    """
def validate_index_loc(index: Index, loc: int) -> None:
    """
    Raises IndexError if index is out of bounds
    """
