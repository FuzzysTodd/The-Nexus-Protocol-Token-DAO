from pyspark.pandas.frame import DataFrame
from pyspark.sql import SparkSession
from typing import Any, Dict, List

__all__ = ['sql']

def sql(query: str, index_col: str | List[str] | None = None, globals: Dict[str, Any] | None = None, locals: Dict[str, Any] | None = None, **kwargs: Any) -> DataFrame:
    '''
    Execute a SQL query and return the result as a pandas-on-Spark DataFrame.

    This function also supports embedding Python variables (locals, globals, and parameters)
    in the SQL statement by wrapping them in curly braces. See examples section for details.

    In addition to the locals, globals and parameters, the function will also attempt
    to determine if the program currently runs in an IPython (or Jupyter) environment
    and to import the variables from this environment. The variables have the same
    precedence as globals.

    The following variable types are supported:

        * string
        * int
        * float
        * list, tuple, range of above types
        * pandas-on-Spark DataFrame
        * pandas-on-Spark Series
        * pandas DataFrame

    Parameters
    ----------
    query : str
        the SQL query
    index_col : str or list of str, optional
        Column names to be used in Spark to represent pandas-on-Spark\'s index. The index name
        in pandas-on-Spark is ignored. By default, the index is always lost.

        .. note:: If you want to preserve the index, explicitly use :func:`DataFrame.reset_index`,
            and pass it to the SQL statement with `index_col` parameter.

            For example,

            >>> from pyspark.pandas import sql_processor
            >>> # we will call \'sql_processor\' directly in doctests so decrease one level.
            >>> sql_processor._CAPTURE_SCOPES = 2
            >>> sql = sql_processor.sql
            >>> psdf = ps.DataFrame({"A": [1, 2, 3], "B":[4, 5, 6]}, index=[\'a\', \'b\', \'c\'])
            >>> psdf_reset_index = psdf.reset_index()
            >>> sql("SELECT * FROM {psdf_reset_index}", index_col="index")
            ... # doctest: +NORMALIZE_WHITESPACE
                   A  B
            index
            a      1  4
            b      2  5
            c      3  6

            For MultiIndex,

            >>> psdf = ps.DataFrame(
            ...     {"A": [1, 2, 3], "B": [4, 5, 6]},
            ...     index=pd.MultiIndex.from_tuples(
            ...         [("a", "b"), ("c", "d"), ("e", "f")], names=["index1", "index2"]
            ...     ),
            ... )
            >>> psdf_reset_index = psdf.reset_index()
            >>> sql("SELECT * FROM {psdf_reset_index}", index_col=["index1", "index2"])
            ... # doctest: +NORMALIZE_WHITESPACE
                           A  B
            index1 index2
            a      b       1  4
            c      d       2  5
            e      f       3  6

            Also note that the index name(s) should be matched to the existing name.

    globals : dict, optional
        the dictionary of global variables, if explicitly set by the user
    locals : dict, optional
        the dictionary of local variables, if explicitly set by the user
    kwargs
        other variables that the user may want to set manually that can be referenced in the query

    Returns
    -------
    pandas-on-Spark DataFrame

    Examples
    --------

    Calling a built-in SQL function.

    >>> sql("select * from range(10) where id > 7")
       id
    0   8
    1   9

    A query can also reference a local variable or parameter by wrapping them in curly braces:

    >>> bound1 = 7
    >>> sql("select * from range(10) where id > {bound1} and id < {bound2}", bound2=9)
       id
    0   8

    You can also wrap a DataFrame with curly braces to query it directly. Note that when you do
    that, the indexes, if any, automatically become top level columns.

    >>> mydf = ps.range(10)
    >>> x = range(4)
    >>> sql("SELECT * from {mydf} WHERE id IN {x}")
       id
    0   0
    1   1
    2   2
    3   3

    Queries can also be arbitrarily nested in functions:

    >>> def statement():
    ...     mydf2 = ps.DataFrame({"x": range(2)})
    ...     return sql("SELECT * from {mydf2}")
    >>> statement()
       x
    0  0
    1  1

    Mixing pandas-on-Spark and pandas DataFrames in a join operation. Note that the index is
    dropped.

    >>> sql(\'\'\'
    ...   SELECT m1.a, m2.b
    ...   FROM {table1} m1 INNER JOIN {table2} m2
    ...   ON m1.key = m2.key
    ...   ORDER BY m1.a, m2.b\'\'\',
    ...   table1=ps.DataFrame({"a": [1,2], "key": ["a", "b"]}),
    ...   table2=pd.DataFrame({"b": [3,4,5], "key": ["a", "b", "b"]}))
       a  b
    0  1  3
    1  2  4
    2  2  5

    Also, it is possible to query using Series.

    >>> myser = ps.Series({\'a\': [1.0, 2.0, 3.0], \'b\': [15.0, 30.0, 45.0]})
    >>> sql("SELECT * from {myser}")
                        0
    0     [1.0, 2.0, 3.0]
    1  [15.0, 30.0, 45.0]
    '''

class SQLProcessor:
    def __init__(self, scope: Dict[str, Any], statement: str, session: SparkSession) -> None: ...
    def execute(self, index_col: str | List[str] | None) -> DataFrame:
        '''
        Returns a DataFrame for which the SQL statement has been executed by
        the underlying SQL engine.

        >>> from pyspark.pandas import sql_processor
        >>> # we will call \'sql_processor\' directly in doctests so decrease one level.
        >>> sql_processor._CAPTURE_SCOPES = 2
        >>> sql = sql_processor.sql
        >>> str0 = \'abc\'
        >>> sql("select {str0}")
           abc
        0  abc

        >>> str1 = \'abc"abc\'
        >>> str2 = "abc\'abc"
        >>> sql("select {str0}, {str1}, {str2}")
           abc  abc"abc  abc\'abc
        0  abc  abc"abc  abc\'abc

        >>> strs = [\'a\', \'b\']
        >>> sql("select \'a\' in {strs} as cond1, \'c\' in {strs} as cond2")
           cond1  cond2
        0   True  False
        '''
