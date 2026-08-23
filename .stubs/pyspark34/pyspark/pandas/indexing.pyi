from abc import ABCMeta
from pyspark.errors import AnalysisException as AnalysisException
from pyspark.pandas._typing import Label as Label, Name as Name, Scalar as Scalar
from pyspark.pandas.exceptions import SparkPandasIndexingError as SparkPandasIndexingError, SparkPandasNotImplementedError as SparkPandasNotImplementedError
from pyspark.pandas.frame import DataFrame as DataFrame
from pyspark.pandas.generic import Frame as Frame
from pyspark.pandas.internal import DEFAULT_SERIES_NAME as DEFAULT_SERIES_NAME, InternalField as InternalField, InternalFrame as InternalFrame, NATURAL_ORDER_COLUMN_NAME as NATURAL_ORDER_COLUMN_NAME, SPARK_DEFAULT_SERIES_NAME as SPARK_DEFAULT_SERIES_NAME
from pyspark.pandas.series import Series as Series
from pyspark.pandas.utils import is_name_like_tuple as is_name_like_tuple, is_name_like_value as is_name_like_value, lazy_property as lazy_property, name_like_string as name_like_string, same_anchor as same_anchor, scol_for as scol_for, spark_column_equals as spark_column_equals, verify_temp_column_name as verify_temp_column_name
from pyspark.sql import Column as Column
from pyspark.sql.types import BooleanType as BooleanType, DataType as DataType, LongType as LongType
from typing import Any

class IndexerLike:
    def __init__(self, psdf_or_psser: Frame) -> None: ...

class AtIndexer(IndexerLike):
    """
    Access a single value for a row/column label pair.
    If the index is not unique, all matching pairs are returned as an array.
    Like ``loc``, in that both provide label-based lookups. Use ``at`` if you only need to
    get a single value in a DataFrame or Series.

    .. note:: Unlike pandas, pandas-on-Spark only allows using ``at`` to get values but not to
        set them.

    .. note:: Warning: If ``row_index`` matches a lot of rows, large amounts of data will be
        fetched, potentially causing your machine to run out of memory.

    Raises
    ------
    KeyError
        When label does not exist in DataFrame

    Examples
    --------
    >>> psdf = ps.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
    ...                    index=[4, 5, 5], columns=['A', 'B', 'C'])
    >>> psdf
        A   B   C
    4   0   2   3
    5   0   4   1
    5  10  20  30

    Get value at specified row/column pair

    >>> psdf.at[4, 'B']
    2

    Get array if an index occurs multiple times

    >>> psdf.at[5, 'B']
    array([ 4, 20])
    """
    def __getitem__(self, key: Any) -> Series | DataFrame | Scalar: ...

class iAtIndexer(IndexerLike):
    """
    Access a single value for a row/column pair by integer position.

    Like ``iloc``, in that both provide integer-based lookups. Use
    ``iat`` if you only need to get or set a single value in a DataFrame
    or Series.

    Raises
    ------
    KeyError
        When label does not exist in DataFrame

    Examples
    --------
    >>> df = ps.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
    ...                   columns=['A', 'B', 'C'])
    >>> df
        A   B   C
    0   0   2   3
    1   0   4   1
    2  10  20  30

    Get value at specified row/column pair

    >>> df.iat[1, 2]
    1

    Get value within a series

    >>> psser = ps.Series([1, 2, 3], index=[10, 20, 30])
    >>> psser
    10    1
    20    2
    30    3
    dtype: int64

    >>> psser.iat[1]
    2
    """
    def __getitem__(self, key: Any) -> Series | DataFrame | Scalar: ...

class LocIndexerLike(IndexerLike, metaclass=ABCMeta):
    def __getitem__(self, key: Any) -> Series | DataFrame: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...

class LocIndexer(LocIndexerLike):
    """
    Access a group of rows and columns by label(s) or a boolean Series.

    ``.loc[]`` is primarily label based, but may also be used with a
    conditional boolean Series derived from the DataFrame or Series.

    Allowed inputs are:

    - A single label, e.g. ``5`` or ``'a'``, (note that ``5`` is
      interpreted as a *label* of the index, and **never** as an
      integer position along the index) for column selection.

    - A list or array of labels, e.g. ``['a', 'b', 'c']``.

    - A slice object with labels, e.g. ``'a':'f'``.

    - A conditional boolean Series derived from the DataFrame or Series

    - A boolean array of the same length as the column axis being sliced,
      e.g. ``[True, False, True]``.

    - An alignable boolean pandas Series to the column axis being sliced.
      The index of the key will be aligned before masking.

    Not allowed inputs which pandas allows are:

    - A boolean array of the same length as the row axis being sliced,
      e.g. ``[True, False, True]``.
    - A ``callable`` function with one argument (the calling Series, DataFrame
      or Panel) and that returns valid output for indexing (one of the above)

    .. note:: MultiIndex is not supported yet.

    .. note:: Note that contrary to usual python slices, **both** the
        start and the stop are included, and the step of the slice is not allowed.

    .. note:: With a list or array of labels for row selection,
        pandas-on-Spark behaves as a filter without reordering by the labels.

    See Also
    --------
    Series.loc : Access group of values using labels.

    Examples
    --------
    **Getting values**

    >>> df = ps.DataFrame([[1, 2], [4, 5], [7, 8]],
    ...                   index=['cobra', 'viper', 'sidewinder'],
    ...                   columns=['max_speed', 'shield'])
    >>> df
                max_speed  shield
    cobra               1       2
    viper               4       5
    sidewinder          7       8

    Single label. Note this returns the row as a Series.

    >>> df.loc['viper']
    max_speed    4
    shield       5
    Name: viper, dtype: int64

    List of labels. Note using ``[[]]`` returns a DataFrame.
    Also note that pandas-on-Spark behaves just a filter without reordering by the labels.

    >>> df.loc[['viper', 'sidewinder']]
                max_speed  shield
    viper               4       5
    sidewinder          7       8

    >>> df.loc[['sidewinder', 'viper']]
                max_speed  shield
    viper               4       5
    sidewinder          7       8

    Single label for column.

    >>> df.loc['cobra', 'shield']
    2

    List of labels for row.

    >>> df.loc[['cobra'], 'shield']
    cobra    2
    Name: shield, dtype: int64

    List of labels for column.

    >>> df.loc['cobra', ['shield']]
    shield    2
    Name: cobra, dtype: int64

    List of labels for both row and column.

    >>> df.loc[['cobra'], ['shield']]
           shield
    cobra       2

    Slice with labels for row and single label for column.
    Note that both the start and stop of the slice are included.

    >>> df.loc['cobra':'viper', 'max_speed']
    cobra    1
    viper    4
    Name: max_speed, dtype: int64

    Conditional that returns a boolean Series

    >>> df.loc[df['shield'] > 6]
                max_speed  shield
    sidewinder          7       8

    Conditional that returns a boolean Series with column labels specified

    >>> df.loc[df['shield'] > 6, ['max_speed']]
                max_speed
    sidewinder          7

    A boolean array of the same length as the column axis being sliced.

    >>> df.loc[:, [False, True]]
                shield
    cobra            2
    viper            5
    sidewinder       8

    An alignable boolean Series to the column axis being sliced.

    >>> df.loc[:, pd.Series([False, True], index=['max_speed', 'shield'])]
                shield
    cobra            2
    viper            5
    sidewinder       8

    **Setting values**

    Setting value for all items matching the list of labels.

    >>> df.loc[['viper', 'sidewinder'], ['shield']] = 50
    >>> df
                max_speed  shield
    cobra               1       2
    viper               4      50
    sidewinder          7      50

    Setting value for an entire row

    >>> df.loc['cobra'] = 10
    >>> df
                max_speed  shield
    cobra              10      10
    viper               4      50
    sidewinder          7      50

    Set value for an entire column

    >>> df.loc[:, 'max_speed'] = 30
    >>> df
                max_speed  shield
    cobra              30      10
    viper              30      50
    sidewinder         30      50

    Set value for an entire list of columns

    >>> df.loc[:, ['max_speed', 'shield']] = 100
    >>> df
                max_speed  shield
    cobra             100     100
    viper             100     100
    sidewinder        100     100

    Set value with Series

    >>> df.loc[:, 'shield'] = df['shield'] * 2
    >>> df
                max_speed  shield
    cobra             100     200
    viper             100     200
    sidewinder        100     200

    **Getting values on a DataFrame with an index that has integer labels**

    Another example using integers for the index

    >>> df = ps.DataFrame([[1, 2], [4, 5], [7, 8]],
    ...                   index=[7, 8, 9],
    ...                   columns=['max_speed', 'shield'])
    >>> df
       max_speed  shield
    7          1       2
    8          4       5
    9          7       8

    Slice with integer labels for rows. Note that both
    the start and stop of the slice are included.

    >>> df.loc[7:9]
       max_speed  shield
    7          1       2
    8          4       5
    9          7       8
    """

class iLocIndexer(LocIndexerLike):
    """
    Purely integer-location based indexing for selection by position.

    ``.iloc[]`` is primarily integer position based (from ``0`` to
    ``length-1`` of the axis), but may also be used with a conditional boolean Series.

    Allowed inputs are:

    - An integer for column selection, e.g. ``5``.
    - A list or array of integers for row selection with distinct index values,
      e.g. ``[3, 4, 0]``
    - A list or array of integers for column selection, e.g. ``[4, 3, 0]``.
    - A boolean array for column selection.
    - A slice object with ints for row and column selection, e.g. ``1:7``.

    Not allowed inputs which pandas allows are:

    - A list or array of integers for row selection with duplicated indexes,
      e.g. ``[4, 4, 0]``.
    - A boolean array for row selection.
    - A ``callable`` function with one argument (the calling Series, DataFrame
      or Panel) and that returns valid output for indexing (one of the above).
      This is useful in method chains when you don't have a reference to the
      calling object but would like to base your selection on some value.

    ``.iloc`` will raise ``IndexError`` if a requested indexer is
    out-of-bounds, except *slice* indexers which allow out-of-bounds
    indexing (this conforms with python/numpy *slice* semantics).

    See Also
    --------
    DataFrame.loc : Purely label-location based indexer for selection by label.
    Series.iloc : Purely integer-location based indexing for
                   selection by position.

    Examples
    --------

    >>> mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
    ...           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
    ...           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
    >>> df = ps.DataFrame(mydict, columns=['a', 'b', 'c', 'd'])
    >>> df
          a     b     c     d
    0     1     2     3     4
    1   100   200   300   400
    2  1000  2000  3000  4000

    **Indexing just the rows**

    A scalar integer for row selection.

    >>> df.iloc[1]
    a    100
    b    200
    c    300
    d    400
    Name: 1, dtype: int64

    >>> df.iloc[[0]]
       a  b  c  d
    0  1  2  3  4

    With a `slice` object.

    >>> df.iloc[:3]
          a     b     c     d
    0     1     2     3     4
    1   100   200   300   400
    2  1000  2000  3000  4000

    **Indexing both axes**

    You can mix the indexer types for the index and columns. Use ``:`` to
    select the entire axis.

    With scalar integers.

    >>> df.iloc[:1, 1]
    0    2
    Name: b, dtype: int64

    With lists of integers.

    >>> df.iloc[:2, [1, 3]]
         b    d
    0    2    4
    1  200  400

    With `slice` objects.

    >>> df.iloc[:2, 0:3]
         a    b    c
    0    1    2    3
    1  100  200  300

    With a boolean array whose length matches the columns.

    >>> df.iloc[:, [True, False, True, False]]
          a     c
    0     1     3
    1   100   300
    2  1000  3000

    **Setting values**

    Setting value for all items matching the list of labels.

    >>> df.iloc[[1, 2], [1]] = 50
    >>> df
          a   b     c     d
    0     1   2     3     4
    1   100  50   300   400
    2  1000  50  3000  4000

    Setting value for an entire row

    >>> df.iloc[0] = 10
    >>> df
          a   b     c     d
    0    10  10    10    10
    1   100  50   300   400
    2  1000  50  3000  4000

    Set value for an entire column

    >>> df.iloc[:, 2] = 30
    >>> df
          a   b   c     d
    0    10  10  30    10
    1   100  50  30   400
    2  1000  50  30  4000

    Set value for an entire list of columns

    >>> df.iloc[:, [2, 3]] = 100
    >>> df
          a   b    c    d
    0    10  10  100  100
    1   100  50  100  100
    2  1000  50  100  100

    Set value with Series

    >>> df.iloc[:, 3] = df.iloc[:, 3] * 2
    >>> df
          a   b    c    d
    0    10  10  100  200
    1   100  50  100  200
    2  1000  50  100  200
    """
    def __setitem__(self, key: Any, value: Any) -> None: ...
