import string
from pyspark.pandas.frame import DataFrame
from pyspark.sql import SparkSession
from typing import Any, Dict, List, Mapping, Sequence

__all__ = ['sql']

def sql(query: str, index_col: str | List[str] | None = None, args: Dict[str, str] = {}, **kwargs: Any) -> DataFrame:
    '''
    Execute a SQL query and return the result as a pandas-on-Spark DataFrame.

    This function acts as a standard Python string formatter with understanding
    the following variable types:

        * pandas-on-Spark DataFrame
        * pandas-on-Spark Series
        * pandas DataFrame
        * pandas Series
        * string

    Also the method can bind named parameters to SQL literals from `args`.

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

            >>> psdf = ps.DataFrame({"A": [1, 2, 3], "B":[4, 5, 6]}, index=[\'a\', \'b\', \'c\'])
            >>> new_psdf = psdf.reset_index()
            >>> ps.sql("SELECT * FROM {new_psdf}", index_col="index", new_psdf=new_psdf)
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
            >>> new_psdf = psdf.reset_index()
            >>> ps.sql(
            ...     "SELECT * FROM {new_psdf}", index_col=["index1", "index2"], new_psdf=new_psdf)
            ... # doctest: +NORMALIZE_WHITESPACE
                           A  B
            index1 index2
            a      b       1  4
            c      d       2  5
            e      f       3  6

            Also note that the index name(s) should be matched to the existing name.
    args : dict
        A dictionary of parameter names to string values that are parsed as SQL literal
        expressions. For example, dict keys: "rank", "name", "birthdate"; dict values:
        "1", "\'Steven\'", "DATE\'2023-03-21\'". The fragments of string values belonged to SQL
        comments are skipped while parsing.

        .. versionadded:: 3.4.0

    kwargs
        other variables that the user want to set that can be referenced in the query

    Returns
    -------
    pandas-on-Spark DataFrame

    Examples
    --------

    Calling a built-in SQL function.

    >>> ps.sql("SELECT * FROM range(10) where id > 7")
       id
    0   8
    1   9

    >>> ps.sql("SELECT * FROM range(10) WHERE id > {bound1} AND id < {bound2}", bound1=7, bound2=9)
       id
    0   8

    >>> mydf = ps.range(10)
    >>> x = tuple(range(4))
    >>> ps.sql("SELECT {ser} FROM {mydf} WHERE id IN {x}", ser=mydf.id, mydf=mydf, x=x)
       id
    0   0
    1   1
    2   2
    3   3

    Mixing pandas-on-Spark and pandas DataFrames in a join operation. Note that the index is
    dropped.

    >>> ps.sql(\'\'\'
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

    >>> psdf = ps.DataFrame({"A": [1, 2, 3], "B":[4, 5, 6]}, index=[\'a\', \'b\', \'c\'])
    >>> ps.sql("SELECT {mydf.A} FROM {mydf}", mydf=psdf)
       A
    0  1
    1  2
    2  3

    And substitude named parameters with the `:` prefix by SQL literals.

    >>> ps.sql("SELECT * FROM range(10) WHERE id > :bound1", args={"bound1":"7"})
       id
    0   8
    1   9
    '''

class PandasSQLStringFormatter(string.Formatter):
    """
    A standard ``string.Formatter`` in Python that can understand pandas-on-Spark instances
    with basic Python objects. This object must be clear after the use for single SQL
    query; cannot be reused across multiple SQL queries without cleaning.
    """
    def __init__(self, session: SparkSession) -> None: ...
    def vformat(self, format_string: str, args: Sequence[Any], kwargs: Mapping[str, Any]) -> str: ...
    def get_field(self, field_name: str, args: Sequence[Any], kwargs: Mapping[str, Any]) -> Any: ...
    def clear(self) -> None: ...
