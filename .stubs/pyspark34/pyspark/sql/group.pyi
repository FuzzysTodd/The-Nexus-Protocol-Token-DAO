from _typeshed import Incomplete
from py4j.java_gateway import JavaObject
from pyspark.sql._typing import LiteralType
from pyspark.sql.column import Column
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.pandas.group_ops import PandasGroupedOpsMixin
from typing import Dict, List, overload

__all__ = ['GroupedData']

class GroupedData(PandasGroupedOpsMixin):
    """
    A set of methods for aggregations on a :class:`DataFrame`,
    created by :func:`DataFrame.groupBy`.

    .. versionadded:: 1.3.0

    .. versionchanged:: 3.4.0
        Supports Spark Connect.
    """
    session: Incomplete
    def __init__(self, jgd: JavaObject, df: DataFrame) -> None: ...
    @overload
    def agg(self, *exprs: Column) -> DataFrame: ...
    @overload
    def agg(self, __exprs: Dict[str, str]) -> DataFrame: ...
    def count(self) -> DataFrame:
        '''Counts the number of records for each group.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...      [(2, "Alice"), (3, "Alice"), (5, "Bob"), (10, "Bob")], ["age", "name"])
        >>> df.show()
        +---+-----+
        |age| name|
        +---+-----+
        |  2|Alice|
        |  3|Alice|
        |  5|  Bob|
        | 10|  Bob|
        +---+-----+

        Group-by name, and count each group.

        >>> df.groupBy(df.name).count().sort("name").show()
        +-----+-----+
        | name|count|
        +-----+-----+
        |Alice|    2|
        |  Bob|    2|
        +-----+-----+
        '''
    def mean(self, *cols: str) -> DataFrame:
        """Computes average values for each numeric columns for each group.

        :func:`mean` is an alias for :func:`avg`.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        cols : str
            column names. Non-numeric columns are ignored.
        """
    def avg(self, *cols: str) -> DataFrame:
        '''Computes average values for each numeric columns for each group.

        :func:`mean` is an alias for :func:`avg`.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        cols : str
            column names. Non-numeric columns are ignored.

        Examples
        --------
        >>> df = spark.createDataFrame([
        ...     (2, "Alice", 80), (3, "Alice", 100),
        ...     (5, "Bob", 120), (10, "Bob", 140)], ["age", "name", "height"])
        >>> df.show()
        +---+-----+------+
        |age| name|height|
        +---+-----+------+
        |  2|Alice|    80|
        |  3|Alice|   100|
        |  5|  Bob|   120|
        | 10|  Bob|   140|
        +---+-----+------+

        Group-by name, and calculate the mean of the age in each group.

        >>> df.groupBy("name").avg(\'age\').sort("name").show()
        +-----+--------+
        | name|avg(age)|
        +-----+--------+
        |Alice|     2.5|
        |  Bob|     7.5|
        +-----+--------+

        Calculate the mean of the age and height in all data.

        >>> df.groupBy().avg(\'age\', \'height\').show()
        +--------+-----------+
        |avg(age)|avg(height)|
        +--------+-----------+
        |     5.0|      110.0|
        +--------+-----------+
        '''
    def max(self, *cols: str) -> DataFrame:
        '''Computes the max value for each numeric columns for each group.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Examples
        --------
        >>> df = spark.createDataFrame([
        ...     (2, "Alice", 80), (3, "Alice", 100),
        ...     (5, "Bob", 120), (10, "Bob", 140)], ["age", "name", "height"])
        >>> df.show()
        +---+-----+------+
        |age| name|height|
        +---+-----+------+
        |  2|Alice|    80|
        |  3|Alice|   100|
        |  5|  Bob|   120|
        | 10|  Bob|   140|
        +---+-----+------+

        Group-by name, and calculate the max of the age in each group.

        >>> df.groupBy("name").max("age").sort("name").show()
        +-----+--------+
        | name|max(age)|
        +-----+--------+
        |Alice|       3|
        |  Bob|      10|
        +-----+--------+

        Calculate the max of the age and height in all data.

        >>> df.groupBy().max("age", "height").show()
        +--------+-----------+
        |max(age)|max(height)|
        +--------+-----------+
        |      10|        140|
        +--------+-----------+
        '''
    def min(self, *cols: str) -> DataFrame:
        '''Computes the min value for each numeric column for each group.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        cols : str
            column names. Non-numeric columns are ignored.

        Examples
        --------
        >>> df = spark.createDataFrame([
        ...     (2, "Alice", 80), (3, "Alice", 100),
        ...     (5, "Bob", 120), (10, "Bob", 140)], ["age", "name", "height"])
        >>> df.show()
        +---+-----+------+
        |age| name|height|
        +---+-----+------+
        |  2|Alice|    80|
        |  3|Alice|   100|
        |  5|  Bob|   120|
        | 10|  Bob|   140|
        +---+-----+------+

        Group-by name, and calculate the min of the age in each group.

        >>> df.groupBy("name").min("age").sort("name").show()
        +-----+--------+
        | name|min(age)|
        +-----+--------+
        |Alice|       2|
        |  Bob|       5|
        +-----+--------+

        Calculate the min of the age and height in all data.

        >>> df.groupBy().min("age", "height").show()
        +--------+-----------+
        |min(age)|min(height)|
        +--------+-----------+
        |       2|         80|
        +--------+-----------+
        '''
    def sum(self, *cols: str) -> DataFrame:
        '''Computes the sum for each numeric columns for each group.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        cols : str
            column names. Non-numeric columns are ignored.

        Examples
        --------
        >>> df = spark.createDataFrame([
        ...     (2, "Alice", 80), (3, "Alice", 100),
        ...     (5, "Bob", 120), (10, "Bob", 140)], ["age", "name", "height"])
        >>> df.show()
        +---+-----+------+
        |age| name|height|
        +---+-----+------+
        |  2|Alice|    80|
        |  3|Alice|   100|
        |  5|  Bob|   120|
        | 10|  Bob|   140|
        +---+-----+------+

        Group-by name, and calculate the sum of the age in each group.

        >>> df.groupBy("name").sum("age").sort("name").show()
        +-----+--------+
        | name|sum(age)|
        +-----+--------+
        |Alice|       5|
        |  Bob|      15|
        +-----+--------+

        Calculate the sum of the age and height in all data.

        >>> df.groupBy().sum("age", "height").show()
        +--------+-----------+
        |sum(age)|sum(height)|
        +--------+-----------+
        |      20|        440|
        +--------+-----------+
        '''
    def pivot(self, pivot_col: str, values: List['LiteralType'] | None = None) -> GroupedData:
        '''
        Pivots a column of the current :class:`DataFrame` and perform the specified aggregation.
        There are two versions of the pivot function: one that requires the caller
        to specify the list of distinct values to pivot on, and one that does not.
        The latter is more concise but less efficient,
        because Spark needs to first compute the list of distinct values internally.

        .. versionadded:: 1.6.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        pivot_col : str
            Name of the column to pivot.
        values : list, optional
            List of values that will be translated to columns in the output DataFrame.

        Examples
        --------
        >>> from pyspark.sql import Row
        >>> df1 = spark.createDataFrame([
        ...     Row(course="dotNET", year=2012, earnings=10000),
        ...     Row(course="Java", year=2012, earnings=20000),
        ...     Row(course="dotNET", year=2012, earnings=5000),
        ...     Row(course="dotNET", year=2013, earnings=48000),
        ...     Row(course="Java", year=2013, earnings=30000),
        ... ])
        >>> df1.show()
        +------+----+--------+
        |course|year|earnings|
        +------+----+--------+
        |dotNET|2012|   10000|
        |  Java|2012|   20000|
        |dotNET|2012|    5000|
        |dotNET|2013|   48000|
        |  Java|2013|   30000|
        +------+----+--------+
        >>> df2 = spark.createDataFrame([
        ...     Row(training="expert", sales=Row(course="dotNET", year=2012, earnings=10000)),
        ...     Row(training="junior", sales=Row(course="Java", year=2012, earnings=20000)),
        ...     Row(training="expert", sales=Row(course="dotNET", year=2012, earnings=5000)),
        ...     Row(training="junior", sales=Row(course="dotNET", year=2013, earnings=48000)),
        ...     Row(training="expert", sales=Row(course="Java", year=2013, earnings=30000)),
        ... ])  # doctest: +SKIP
        >>> df2.show()  # doctest: +SKIP
        +--------+--------------------+
        |training|               sales|
        +--------+--------------------+
        |  expert|{dotNET, 2012, 10...|
        |  junior| {Java, 2012, 20000}|
        |  expert|{dotNET, 2012, 5000}|
        |  junior|{dotNET, 2013, 48...|
        |  expert| {Java, 2013, 30000}|
        +--------+--------------------+

        Compute the sum of earnings for each year by course with each course as a separate column

        >>> df1.groupBy("year").pivot("course", ["dotNET", "Java"]).sum("earnings").show()
        +----+------+-----+
        |year|dotNET| Java|
        +----+------+-----+
        |2012| 15000|20000|
        |2013| 48000|30000|
        +----+------+-----+

        Or without specifying column values (less efficient)

        >>> df1.groupBy("year").pivot("course").sum("earnings").show()
        +----+-----+------+
        |year| Java|dotNET|
        +----+-----+------+
        |2012|20000| 15000|
        |2013|30000| 48000|
        +----+-----+------+
        >>> df2.groupBy("sales.year").pivot("sales.course").sum("sales.earnings").show()
        ... # doctest: +SKIP
        +----+-----+------+
        |year| Java|dotNET|
        +----+-----+------+
        |2012|20000| 15000|
        |2013|30000| 48000|
        +----+-----+------+
        '''
