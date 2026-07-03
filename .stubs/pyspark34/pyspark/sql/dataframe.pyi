from _typeshed import Incomplete
from py4j.java_gateway import JavaObject
from pyspark._typing import PrimitiveType
from pyspark.pandas.frame import DataFrame as PandasOnSparkDataFrame
from pyspark.rdd import RDD
from pyspark.sql._typing import ColumnOrName, LiteralType, OptionalPrimitiveType
from pyspark.sql.column import Column
from pyspark.sql.context import SQLContext
from pyspark.sql.group import GroupedData
from pyspark.sql.observation import Observation
from pyspark.sql.pandas.conversion import PandasConversionMixin
from pyspark.sql.pandas.map_ops import PandasMapOpsMixin
from pyspark.sql.readwriter import DataFrameWriter, DataFrameWriterV2
from pyspark.sql.session import SparkSession
from pyspark.sql.streaming import DataStreamWriter
from pyspark.sql.types import Row, StructType
from pyspark.storagelevel import StorageLevel
from typing import Any, Callable, Dict, Iterator, List, Tuple, overload

__all__ = ['DataFrame', 'DataFrameNaFunctions', 'DataFrameStatFunctions']

class DataFrame(PandasMapOpsMixin, PandasConversionMixin):
    '''A distributed collection of data grouped into named columns.

    .. versionadded:: 1.3.0

    .. versionchanged:: 3.4.0
        Supports Spark Connect.

    Examples
    --------
    A :class:`DataFrame` is equivalent to a relational table in Spark SQL,
    and can be created using various functions in :class:`SparkSession`:

    >>> people = spark.createDataFrame([
    ...     {"deptId": 1, "age": 40, "name": "Hyukjin Kwon", "gender": "M", "salary": 50},
    ...     {"deptId": 1, "age": 50, "name": "Takuya Ueshin", "gender": "M", "salary": 100},
    ...     {"deptId": 2, "age": 60, "name": "Xinrong Meng", "gender": "F", "salary": 150},
    ...     {"deptId": 3, "age": 20, "name": "Haejoon Lee", "gender": "M", "salary": 200}
    ... ])

    Once created, it can be manipulated using the various domain-specific-language
    (DSL) functions defined in: :class:`DataFrame`, :class:`Column`.

    To select a column from the :class:`DataFrame`, use the apply method:

    >>> age_col = people.age

    A more concrete example:

    >>> # To create DataFrame using SparkSession
    ... department = spark.createDataFrame([
    ...     {"id": 1, "name": "PySpark"},
    ...     {"id": 2, "name": "ML"},
    ...     {"id": 3, "name": "Spark SQL"}
    ... ])

    >>> people.filter(people.age > 30).join(
    ...     department, people.deptId == department.id).groupBy(
    ...     department.name, "gender").agg({"salary": "avg", "age": "max"}).show()
    +-------+------+-----------+--------+
    |   name|gender|avg(salary)|max(age)|
    +-------+------+-----------+--------+
    |     ML|     F|      150.0|      60|
    |PySpark|     M|       75.0|      50|
    +-------+------+-----------+--------+

    Notes
    -----
    A DataFrame should only be created as described above. It should not be directly
    created via using the constructor.
    '''
    is_cached: bool
    def __init__(self, jdf: JavaObject, sql_ctx: SQLContext | SparkSession) -> None: ...
    @property
    def sql_ctx(self) -> SQLContext: ...
    @property
    def sparkSession(self) -> SparkSession:
        """Returns Spark session that created this :class:`DataFrame`.

        .. versionadded:: 3.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        :class:`SparkSession`

        Examples
        --------
        >>> df = spark.range(1)
        >>> type(df.sparkSession)
        <class '...session.SparkSession'>
        """
    @property
    def rdd(self) -> RDD[Row]:
        """Returns the content as an :class:`pyspark.RDD` of :class:`Row`.

        .. versionadded:: 1.3.0

        Returns
        -------
        :class:`RDD`

        Examples
        --------
        >>> df = spark.range(1)
        >>> type(df.rdd)
        <class 'pyspark.rdd.RDD'>
        """
    @property
    def na(self) -> DataFrameNaFunctions:
        '''Returns a :class:`DataFrameNaFunctions` for handling missing values.

        .. versionadded:: 1.3.1

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        :class:`DataFrameNaFunctions`

        Examples
        --------
        >>> df = spark.sql("SELECT 1 AS c1, int(NULL) AS c2")
        >>> type(df.na)
        <class \'...dataframe.DataFrameNaFunctions\'>

        Replace the missing values as 2.

        >>> df.na.fill(2).show()
        +---+---+
        | c1| c2|
        +---+---+
        |  1|  2|
        +---+---+
        '''
    @property
    def stat(self) -> DataFrameStatFunctions:
        '''Returns a :class:`DataFrameStatFunctions` for statistic functions.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        :class:`DataFrameStatFunctions`

        Examples
        --------
        >>> import pyspark.sql.functions as f
        >>> df = spark.range(3).withColumn("c", f.expr("id + 1"))
        >>> type(df.stat)
        <class \'...dataframe.DataFrameStatFunctions\'>
        >>> df.stat.corr("id", "c")
        1.0
        '''
    def toJSON(self, use_unicode: bool = True) -> RDD[str]:
        '''Converts a :class:`DataFrame` into a :class:`RDD` of string.

        Each row is turned into a JSON document as one element in the returned RDD.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        use_unicode : bool, optional, default True
            Whether to convert to unicode or not.

        Returns
        -------
        :class:`RDD`

        Examples
        --------
        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df.toJSON().first()
        \'{"age":2,"name":"Alice"}\'
        '''
    def registerTempTable(self, name: str) -> None:
        '''Registers this :class:`DataFrame` as a temporary table using the given name.

        The lifetime of this temporary table is tied to the :class:`SparkSession`
        that was used to create this :class:`DataFrame`.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        .. deprecated:: 2.0.0
            Use :meth:`DataFrame.createOrReplaceTempView` instead.

        Parameters
        ----------
        name : str
            Name of the temporary table to register.

        Examples
        --------
        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df.registerTempTable("people")
        >>> df2 = spark.sql("SELECT * FROM people")
        >>> sorted(df.collect()) == sorted(df2.collect())
        True
        >>> spark.catalog.dropTempView("people")
        True

        '''
    def createTempView(self, name: str) -> None:
        '''Creates a local temporary view with this :class:`DataFrame`.

        The lifetime of this temporary table is tied to the :class:`SparkSession`
        that was used to create this :class:`DataFrame`.
        throws :class:`TempTableAlreadyExistsException`, if the view name already exists in the
        catalog.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        name : str
            Name of the view.

        Examples
        --------
        Create a local temporary view.

        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df.createTempView("people")
        >>> df2 = spark.sql("SELECT * FROM people")
        >>> sorted(df.collect()) == sorted(df2.collect())
        True

        Throw an exception if the table already exists.

        >>> df.createTempView("people")  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        AnalysisException: "Temporary table \'people\' already exists;"
        >>> spark.catalog.dropTempView("people")
        True

        '''
    def createOrReplaceTempView(self, name: str) -> None:
        '''Creates or replaces a local temporary view with this :class:`DataFrame`.

        The lifetime of this temporary table is tied to the :class:`SparkSession`
        that was used to create this :class:`DataFrame`.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        name : str
            Name of the view.

        Examples
        --------
        Create a local temporary view named \'people\'.

        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df.createOrReplaceTempView("people")

        Replace the local temporary view.

        >>> df2 = df.filter(df.age > 3)
        >>> df2.createOrReplaceTempView("people")
        >>> df3 = spark.sql("SELECT * FROM people")
        >>> sorted(df3.collect()) == sorted(df2.collect())
        True
        >>> spark.catalog.dropTempView("people")
        True

        '''
    def createGlobalTempView(self, name: str) -> None:
        '''Creates a global temporary view with this :class:`DataFrame`.

        The lifetime of this temporary view is tied to this Spark application.
        throws :class:`TempTableAlreadyExistsException`, if the view name already exists in the
        catalog.

        .. versionadded:: 2.1.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        name : str
            Name of the view.

        Examples
        --------
        Create a global temporary view.

        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df.createGlobalTempView("people")
        >>> df2 = spark.sql("SELECT * FROM global_temp.people")
        >>> sorted(df.collect()) == sorted(df2.collect())
        True

        Throws an exception if the global temporary view already exists.

        >>> df.createGlobalTempView("people")  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        AnalysisException: "Temporary table \'people\' already exists;"
        >>> spark.catalog.dropGlobalTempView("people")
        True

        '''
    def createOrReplaceGlobalTempView(self, name: str) -> None:
        '''Creates or replaces a global temporary view using the given name.

        The lifetime of this temporary view is tied to this Spark application.

        .. versionadded:: 2.2.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        name : str
            Name of the view.

        Examples
        --------
        Create a global temporary view.

        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df.createOrReplaceGlobalTempView("people")

        Replace the global temporary view.

        >>> df2 = df.filter(df.age > 3)
        >>> df2.createOrReplaceGlobalTempView("people")
        >>> df3 = spark.sql("SELECT * FROM global_temp.people")
        >>> sorted(df3.collect()) == sorted(df2.collect())
        True
        >>> spark.catalog.dropGlobalTempView("people")
        True

        '''
    @property
    def write(self) -> DataFrameWriter:
        '''
        Interface for saving the content of the non-streaming :class:`DataFrame` out into external
        storage.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        :class:`DataFrameWriter`

        Examples
        --------
        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> type(df.write)
        <class \'...readwriter.DataFrameWriter\'>

        Write the DataFrame as a table.

        >>> _ = spark.sql("DROP TABLE IF EXISTS tab2")
        >>> df.write.saveAsTable("tab2")
        >>> _ = spark.sql("DROP TABLE tab2")
        '''
    @property
    def writeStream(self) -> DataStreamWriter:
        '''
        Interface for saving the content of the streaming :class:`DataFrame` out into external
        storage.

        .. versionadded:: 2.0.0

        Notes
        -----
        This API is evolving.

        Returns
        -------
        :class:`DataStreamWriter`

        Examples
        --------
        >>> import tempfile
        >>> df = spark.readStream.format("rate").load()
        >>> type(df.writeStream)
        <class \'pyspark.sql.streaming.readwriter.DataStreamWriter\'>

        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Create a table with Rate source.
        ...     df.writeStream.toTable(
        ...         "my_table", checkpointLocation=d) # doctest: +ELLIPSIS
        <pyspark.sql.streaming.query.StreamingQuery object at 0x...>
        '''
    @property
    def schema(self) -> StructType:
        '''Returns the schema of this :class:`DataFrame` as a :class:`pyspark.sql.types.StructType`.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        :class:`StructType`

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])

        Retrieve the schema of the current DataFrame.

        >>> df.schema
        StructType([StructField(\'age\', LongType(), True),
                    StructField(\'name\', StringType(), True)])
        '''
    def printSchema(self) -> None:
        '''Prints out the schema in the tree format.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
        >>> df.printSchema()
        root
         |-- age: long (nullable = true)
         |-- name: string (nullable = true)
        '''
    def explain(self, extended: bool | str | None = None, mode: str | None = None) -> None:
        '''Prints the (logical and physical) plans to the console for debugging purposes.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        extended : bool, optional
            default ``False``. If ``False``, prints only the physical plan.
            When this is a string without specifying the ``mode``, it works as the mode is
            specified.
        mode : str, optional
            specifies the expected output format of plans.

            * ``simple``: Print only a physical plan.
            * ``extended``: Print both logical and physical plans.
            * ``codegen``: Print a physical plan and generated codes if they are available.
            * ``cost``: Print a logical plan and statistics if they are available.
            * ``formatted``: Split explain output into two sections: a physical plan outline                 and node details.

            .. versionchanged:: 3.0.0
               Added optional argument `mode` to specify the expected output format of plans.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])

        Print out the physical plan only (default).

        >>> df.explain()  # doctest: +SKIP
        == Physical Plan ==
        *(1) Scan ExistingRDD[age...,name...]

        Print out all of the parsed, analyzed, optimized and physical plans.

        >>> df.explain(True)
        == Parsed Logical Plan ==
        ...
        == Analyzed Logical Plan ==
        ...
        == Optimized Logical Plan ==
        ...
        == Physical Plan ==
        ...

        Print out the plans with two sections: a physical plan outline and node details

        >>> df.explain(mode="formatted")  # doctest: +SKIP
        == Physical Plan ==
        * Scan ExistingRDD (...)
        (1) Scan ExistingRDD [codegen id : ...]
        Output [2]: [age..., name...]
        ...

        Print a logical plan and statistics if they are available.

        >>> df.explain("cost")
        == Optimized Logical Plan ==
        ...Statistics...
        ...
        '''
    def exceptAll(self, other: DataFrame) -> DataFrame:
        '''Return a new :class:`DataFrame` containing rows in this :class:`DataFrame` but
        not in another :class:`DataFrame` while preserving duplicates.

        This is equivalent to `EXCEPT ALL` in SQL.
        As standard in SQL, this function resolves columns by position (not by name).

        .. versionadded:: 2.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        other : :class:`DataFrame`
            The other :class:`DataFrame` to compare to.

        Returns
        -------
        :class:`DataFrame`

        Examples
        --------
        >>> df1 = spark.createDataFrame(
        ...         [("a", 1), ("a", 1), ("a", 1), ("a", 2), ("b",  3), ("c", 4)], ["C1", "C2"])
        >>> df2 = spark.createDataFrame([("a", 1), ("b", 3)], ["C1", "C2"])
        >>> df1.exceptAll(df2).show()
        +---+---+
        | C1| C2|
        +---+---+
        |  a|  1|
        |  a|  1|
        |  a|  2|
        |  c|  4|
        +---+---+

        '''
    def isLocal(self) -> bool:
        '''Returns ``True`` if the :func:`collect` and :func:`take` methods can be run locally
        (without any Spark executors).

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        bool

        Examples
        --------
        >>> df = spark.sql("SHOW TABLES")
        >>> df.isLocal()
        True
        '''
    @property
    def isStreaming(self) -> bool:
        '''Returns ``True`` if this :class:`DataFrame` contains one or more sources that
        continuously return data as it arrives. A :class:`DataFrame` that reads data from a
        streaming source must be executed as a :class:`StreamingQuery` using the :func:`start`
        method in :class:`DataStreamWriter`.  Methods that return a single answer, (e.g.,
        :func:`count` or :func:`collect`) will throw an :class:`AnalysisException` when there
        is a streaming source present.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Notes
        -----
        This API is evolving.

        Returns
        -------
        bool
            Whether it\'s streaming DataFrame or not.

        Examples
        --------
        >>> df = spark.readStream.format("rate").load()
        >>> df.isStreaming
        True
        '''
    def isEmpty(self) -> bool:
        '''Returns ``True`` if this :class:`DataFrame` is empty.

        .. versionadded:: 3.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        bool
            Whether it\'s empty DataFrame or not.

        Examples
        --------
        >>> df_empty = spark.createDataFrame([], \'a STRING\')
        >>> df_non_empty = spark.createDataFrame(["a"], \'STRING\')
        >>> df_empty.isEmpty()
        True
        >>> df_non_empty.isEmpty()
        False
        '''
    def show(self, n: int = 20, truncate: bool | int = True, vertical: bool = False) -> None:
        '''Prints the first ``n`` rows to the console.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        n : int, optional
            Number of rows to show.
        truncate : bool or int, optional
            If set to ``True``, truncate strings longer than 20 chars by default.
            If set to a number greater than one, truncates long strings to length ``truncate``
            and align cells right.
        vertical : bool, optional
            If set to ``True``, print output rows vertically (one line
            per column value).

        Examples
        --------
        >>> df = spark.createDataFrame([
        ...     (14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])

        Show only top 2 rows.

        >>> df.show(2)
        +---+-----+
        |age| name|
        +---+-----+
        | 14|  Tom|
        | 23|Alice|
        +---+-----+
        only showing top 2 rows

        Show :class:`DataFrame` where the maximum number of characters is 3.

        >>> df.show(truncate=3)
        +---+----+
        |age|name|
        +---+----+
        | 14| Tom|
        | 23| Ali|
        | 16| Bob|
        +---+----+

        Show :class:`DataFrame` vertically.

        >>> df.show(vertical=True)
        -RECORD 0-----
        age  | 14
        name | Tom
        -RECORD 1-----
        age  | 23
        name | Alice
        -RECORD 2-----
        age  | 16
        name | Bob
        '''
    def checkpoint(self, eager: bool = True) -> DataFrame:
        '''Returns a checkpointed version of this :class:`DataFrame`. Checkpointing can be used to
        truncate the logical plan of this :class:`DataFrame`, which is especially useful in
        iterative algorithms where the plan may grow exponentially. It will be saved to files
        inside the checkpoint directory set with :meth:`SparkContext.setCheckpointDir`.

        .. versionadded:: 2.1.0

        Parameters
        ----------
        eager : bool, optional, default True
            Whether to checkpoint this :class:`DataFrame` immediately.

        Returns
        -------
        :class:`DataFrame`
            Checkpointed DataFrame.

        Notes
        -----
        This API is experimental.

        Examples
        --------
        >>> import tempfile
        >>> df = spark.createDataFrame([
        ...     (14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
        >>> with tempfile.TemporaryDirectory() as d:
        ...     spark.sparkContext.setCheckpointDir("/tmp/bb")
        ...     df.checkpoint(False)
        DataFrame[age: bigint, name: string]
        '''
    def localCheckpoint(self, eager: bool = True) -> DataFrame:
        '''Returns a locally checkpointed version of this :class:`DataFrame`. Checkpointing can be
        used to truncate the logical plan of this :class:`DataFrame`, which is especially useful in
        iterative algorithms where the plan may grow exponentially. Local checkpoints are
        stored in the executors using the caching subsystem and therefore they are not reliable.

        .. versionadded:: 2.3.0

        Parameters
        ----------
        eager : bool, optional, default True
            Whether to checkpoint this :class:`DataFrame` immediately.

        Returns
        -------
        :class:`DataFrame`
            Checkpointed DataFrame.

        Notes
        -----
        This API is experimental.

        Examples
        --------
        >>> df = spark.createDataFrame([
        ...     (14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
        >>> df.localCheckpoint(False)
        DataFrame[age: bigint, name: string]
        '''
    def withWatermark(self, eventTime: str, delayThreshold: str) -> DataFrame:
        '''Defines an event time watermark for this :class:`DataFrame`. A watermark tracks a point
        in time before which we assume no more late data is going to arrive.

        Spark will use this watermark for several purposes:
          - To know when a given time window aggregation can be finalized and thus can be emitted
            when using output modes that do not allow updates.

          - To minimize the amount of state that we need to keep for on-going aggregations.

        The current watermark is computed by looking at the `MAX(eventTime)` seen across
        all of the partitions in the query minus a user specified `delayThreshold`.  Due to the cost
        of coordinating this value across partitions, the actual watermark used is only guaranteed
        to be at least `delayThreshold` behind the actual event time.  In some cases we may still
        process records that arrive more than `delayThreshold` late.

        .. versionadded:: 2.1.0

        Parameters
        ----------
        eventTime : str
            the name of the column that contains the event time of the row.
        delayThreshold : str
            the minimum delay to wait to data to arrive late, relative to the
            latest record that has been processed in the form of an interval
            (e.g. "1 minute" or "5 hours").

        Returns
        -------
        :class:`DataFrame`
            Watermarked DataFrame

        Notes
        -----
        This is a feature only for Structured Streaming.

        This API is evolving.

        Examples
        --------
        >>> from pyspark.sql import Row
        >>> from pyspark.sql.functions import timestamp_seconds
        >>> df = spark.readStream.format("rate").load().selectExpr(
        ...     "value % 5 AS value", "timestamp")
        >>> df.select("value", df.timestamp.alias("time")).withWatermark("time", \'10 minutes\')
        DataFrame[value: bigint, time: timestamp]

        Group the data by window and value (0 - 4), and compute the count of each group.

        >>> import time
        >>> from pyspark.sql.functions import window
        >>> query = (df
        ...     .withWatermark("timestamp", "10 minutes")
        ...     .groupBy(
        ...         window(df.timestamp, "10 minutes", "5 minutes"),
        ...         df.value)
        ...     ).count().writeStream.outputMode("complete").format("console").start()
        >>> time.sleep(3)
        >>> query.stop()
        '''
    def hint(self, name: str, *parameters: PrimitiveType | List['PrimitiveType']) -> DataFrame:
        '''Specifies some hint on the current :class:`DataFrame`.

        .. versionadded:: 2.2.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        name : str
            A name of the hint.
        parameters : str, list, float or int
            Optional parameters.

        Returns
        -------
        :class:`DataFrame`
            Hinted DataFrame

        Examples
        --------
        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df2 = spark.createDataFrame([Row(height=80, name="Tom"), Row(height=85, name="Bob")])
        >>> df.join(df2, "name").explain()  # doctest: +SKIP
        == Physical Plan ==
        ...
        ... +- SortMergeJoin ...
        ...

        Explicitly trigger the broadcast hashjoin by providing the hint in ``df2``.

        >>> df.join(df2.hint("broadcast"), "name").explain()
        == Physical Plan ==
        ...
        ... +- BroadcastHashJoin ...
        ...
        '''
    def count(self) -> int:
        '''Returns the number of rows in this :class:`DataFrame`.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        int
            Number of rows.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])

        Return the number of rows in the :class:`DataFrame`.

        >>> df.count()
        3
        '''
    def collect(self) -> List[Row]:
        '''Returns all the records as a list of :class:`Row`.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        list
            List of rows.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
        >>> df.collect()
        [Row(age=14, name=\'Tom\'), Row(age=23, name=\'Alice\'), Row(age=16, name=\'Bob\')]
        '''
    def toLocalIterator(self, prefetchPartitions: bool = False) -> Iterator[Row]:
        '''
        Returns an iterator that contains all of the rows in this :class:`DataFrame`.
        The iterator will consume as much memory as the largest partition in this
        :class:`DataFrame`. With prefetch it may consume up to the memory of the 2 largest
        partitions.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        prefetchPartitions : bool, optional
            If Spark should pre-fetch the next partition before it is needed.

            .. versionchanged:: 3.4.0
                This argument does not take effect for Spark Connect.

        Returns
        -------
        Iterator
            Iterator of rows.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
        >>> list(df.toLocalIterator())
        [Row(age=14, name=\'Tom\'), Row(age=23, name=\'Alice\'), Row(age=16, name=\'Bob\')]
        '''
    def limit(self, num: int) -> DataFrame:
        '''Limits the result count to the number specified.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        num : int
            Number of records to return. Will return this number of records
            or all records if the DataFrame contains less than this number of records.

        Returns
        -------
        :class:`DataFrame`
            Subset of the records

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
        >>> df.limit(1).show()
        +---+----+
        |age|name|
        +---+----+
        | 14| Tom|
        +---+----+
        >>> df.limit(0).show()
        +---+----+
        |age|name|
        +---+----+
        +---+----+
        '''
    def take(self, num: int) -> List[Row]:
        '''Returns the first ``num`` rows as a :class:`list` of :class:`Row`.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        num : int
            Number of records to return. Will return this number of records
            or all records if the DataFrame contains less than this number of records..

        Returns
        -------
        list
            List of rows

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])

        Return the first 2 rows of the :class:`DataFrame`.

        >>> df.take(2)
        [Row(age=14, name=\'Tom\'), Row(age=23, name=\'Alice\')]
        '''
    def tail(self, num: int) -> List[Row]:
        '''
        Returns the last ``num`` rows as a :class:`list` of :class:`Row`.

        Running tail requires moving data into the application\'s driver process, and doing so with
        a very large ``num`` can crash the driver process with OutOfMemoryError.

        .. versionadded:: 3.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        num : int
            Number of records to return. Will return this number of records
            or all records if the DataFrame contains less than this number of records.

        Returns
        -------
        list
            List of rows

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])

        >>> df.tail(2)
        [Row(age=23, name=\'Alice\'), Row(age=16, name=\'Bob\')]
        '''
    def foreach(self, f: Callable[[Row], None]) -> None:
        '''Applies the ``f`` function to all :class:`Row` of this :class:`DataFrame`.

        This is a shorthand for ``df.rdd.foreach()``.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        f : function
            A function that accepts one parameter which will
            receive each row to process.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
        >>> def func(person):
        ...     print(person.name)
        >>> df.foreach(func)
        '''
    def foreachPartition(self, f: Callable[[Iterator[Row]], None]) -> None:
        '''Applies the ``f`` function to each partition of this :class:`DataFrame`.

        This a shorthand for ``df.rdd.foreachPartition()``.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        f : function
            A function that accepts one parameter which will receive
            each partition to process.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
        >>> def func(itr):
        ...     for person in itr:
        ...         print(person.name)
        >>> df.foreachPartition(func)
        '''
    def cache(self) -> DataFrame:
        """Persists the :class:`DataFrame` with the default storage level (`MEMORY_AND_DISK`).

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Notes
        -----
        The default storage level has changed to `MEMORY_AND_DISK` to match Scala in 2.0.

        Returns
        -------
        :class:`DataFrame`
            Cached DataFrame.

        Examples
        --------
        >>> df = spark.range(1)
        >>> df.cache()
        DataFrame[id: bigint]

        >>> df.explain()
        == Physical Plan ==
        InMemoryTableScan ...
        """
    def persist(self, storageLevel: StorageLevel = ...) -> DataFrame:
        """Sets the storage level to persist the contents of the :class:`DataFrame` across
        operations after the first time it is computed. This can only be used to assign
        a new storage level if the :class:`DataFrame` does not have a storage level set yet.
        If no storage level is specified defaults to (`MEMORY_AND_DISK_DESER`)

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Notes
        -----
        The default storage level has changed to `MEMORY_AND_DISK_DESER` to match Scala in 3.0.

        Parameters
        ----------
        storageLevel : :class:`StorageLevel`
            Storage level to set for persistence. Default is MEMORY_AND_DISK_DESER.

        Returns
        -------
        :class:`DataFrame`
            Persisted DataFrame.

        Examples
        --------
        >>> df = spark.range(1)
        >>> df.persist()
        DataFrame[id: bigint]

        >>> df.explain()
        == Physical Plan ==
        InMemoryTableScan ...

        Persists the data in the disk by specifying the storage level.

        >>> from pyspark.storagelevel import StorageLevel
        >>> df.persist(StorageLevel.DISK_ONLY)
        DataFrame[id: bigint]
        """
    @property
    def storageLevel(self) -> StorageLevel:
        """Get the :class:`DataFrame`'s current storage level.

        .. versionadded:: 2.1.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        :class:`StorageLevel`
            Currently defined storage level.

        Examples
        --------
        >>> df1 = spark.range(10)
        >>> df1.storageLevel
        StorageLevel(False, False, False, False, 1)
        >>> df1.cache().storageLevel
        StorageLevel(True, True, False, True, 1)

        >>> df2 = spark.range(5)
        >>> df2.persist(StorageLevel.DISK_ONLY_2).storageLevel
        StorageLevel(True, False, False, False, 2)
        """
    def unpersist(self, blocking: bool = False) -> DataFrame:
        """Marks the :class:`DataFrame` as non-persistent, and remove all blocks for it from
        memory and disk.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Notes
        -----
        `blocking` default has changed to ``False`` to match Scala in 2.0.

        Parameters
        ----------
        blocking : bool
            Whether to block until all blocks are deleted.

        Returns
        -------
        :class:`DataFrame`
            Unpersisted DataFrame.

        Examples
        --------
        >>> df = spark.range(1)
        >>> df.persist()
        DataFrame[id: bigint]
        >>> df.unpersist()
        DataFrame[id: bigint]
        >>> df = spark.range(1)
        >>> df.unpersist(True)
        DataFrame[id: bigint]
        """
    def coalesce(self, numPartitions: int) -> DataFrame:
        """
        Returns a new :class:`DataFrame` that has exactly `numPartitions` partitions.

        Similar to coalesce defined on an :class:`RDD`, this operation results in a
        narrow dependency, e.g. if you go from 1000 partitions to 100 partitions,
        there will not be a shuffle, instead each of the 100 new partitions will
        claim 10 of the current partitions. If a larger number of partitions is requested,
        it will stay at the current number of partitions.

        However, if you're doing a drastic coalesce, e.g. to numPartitions = 1,
        this may result in your computation taking place on fewer nodes than
        you like (e.g. one node in the case of numPartitions = 1). To avoid this,
        you can call repartition(). This will add a shuffle step, but means the
        current upstream partitions will be executed in parallel (per whatever
        the current partitioning is).

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        numPartitions : int
            specify the target number of partitions

        Returns
        -------
        :class:`DataFrame`

        Examples
        --------
        >>> df = spark.range(10)
        >>> df.coalesce(1).rdd.getNumPartitions()
        1
        """
    @overload
    def repartition(self, numPartitions: int, *cols: ColumnOrName) -> DataFrame: ...
    @overload
    def repartition(self, *cols: ColumnOrName) -> DataFrame: ...
    @overload
    def repartitionByRange(self, numPartitions: int, *cols: ColumnOrName) -> DataFrame: ...
    @overload
    def repartitionByRange(self, *cols: ColumnOrName) -> DataFrame: ...
    def distinct(self) -> DataFrame:
        '''Returns a new :class:`DataFrame` containing the distinct rows in this :class:`DataFrame`.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        :class:`DataFrame`
            DataFrame with distinct records.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (23, "Alice")], ["age", "name"])

        Return the number of distinct rows in the :class:`DataFrame`

        >>> df.distinct().count()
        2
        '''
    @overload
    def sample(self, fraction: float, seed: int | None = ...) -> DataFrame: ...
    @overload
    def sample(self, withReplacement: bool | None, fraction: float, seed: int | None = ...) -> DataFrame: ...
    def sampleBy(self, col: ColumnOrName, fractions: Dict[Any, float], seed: int | None = None) -> DataFrame:
        '''
        Returns a stratified sample without replacement based on the
        fraction given on each stratum.

        .. versionadded:: 1.5.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        col : :class:`Column` or str
            column that defines strata

            .. versionchanged:: 3.0.0
               Added sampling by a column of :class:`Column`
        fractions : dict
            sampling fraction for each stratum. If a stratum is not
            specified, we treat its fraction as zero.
        seed : int, optional
            random seed

        Returns
        -------
        a new :class:`DataFrame` that represents the stratified sample

        Examples
        --------
        >>> from pyspark.sql.functions import col
        >>> dataset = spark.range(0, 100).select((col("id") % 3).alias("key"))
        >>> sampled = dataset.sampleBy("key", fractions={0: 0.1, 1: 0.2}, seed=0)
        >>> sampled.groupBy("key").count().orderBy("key").show()
        +---+-----+
        |key|count|
        +---+-----+
        |  0|    3|
        |  1|    6|
        +---+-----+
        >>> dataset.sampleBy(col("key"), fractions={2: 1.0}, seed=0).count()
        33
        '''
    def randomSplit(self, weights: List[float], seed: int | None = None) -> List['DataFrame']:
        '''Randomly splits this :class:`DataFrame` with the provided weights.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        weights : list
            list of doubles as weights with which to split the :class:`DataFrame`.
            Weights will be normalized if they don\'t sum up to 1.0.
        seed : int, optional
            The seed for sampling.

        Returns
        -------
        list
            List of DataFrames.

        Examples
        --------
        >>> from pyspark.sql import Row
        >>> df = spark.createDataFrame([
        ...     Row(age=10, height=80, name="Alice"),
        ...     Row(age=5, height=None, name="Bob"),
        ...     Row(age=None, height=None, name="Tom"),
        ...     Row(age=None, height=None, name=None),
        ... ])

        >>> splits = df.randomSplit([1.0, 2.0], 24)
        >>> splits[0].count()
        2
        >>> splits[1].count()
        2
        '''
    @property
    def dtypes(self) -> List[Tuple[str, str]]:
        '''Returns all column names and their data types as a list.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        list
            List of columns as tuple pairs.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
        >>> df.dtypes
        [(\'age\', \'bigint\'), (\'name\', \'string\')]
        '''
    @property
    def columns(self) -> List[str]:
        '''Returns all column names as a list.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        list
            List of column names.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
        >>> df.columns
        [\'age\', \'name\']
        '''
    def colRegex(self, colName: str) -> Column:
        '''
        Selects column based on the column name specified as a regex and returns it
        as :class:`Column`.

        .. versionadded:: 2.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        colName : str
            string, column name specified as a regex.

        Returns
        -------
        :class:`Column`

        Examples
        --------
        >>> df = spark.createDataFrame([("a", 1), ("b", 2), ("c",  3)], ["Col1", "Col2"])
        >>> df.select(df.colRegex("`(Col1)?+.+`")).show()
        +----+
        |Col2|
        +----+
        |   1|
        |   2|
        |   3|
        +----+
        '''
    def to(self, schema: StructType) -> DataFrame:
        '''
        Returns a new :class:`DataFrame` where each row is reconciled to match the specified
        schema.

        .. versionadded:: 3.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        schema : :class:`StructType`
            Specified schema.

        Returns
        -------
        :class:`DataFrame`
            Reconciled DataFrame.

        Notes
        -----
        * Reorder columns and/or inner fields by name to match the specified schema.

        * Project away columns and/or inner fields that are not needed by the specified schema.
            Missing columns and/or inner fields (present in the specified schema but not input
            DataFrame) lead to failures.

        * Cast the columns and/or inner fields to match the data types in the specified schema,
            if the types are compatible, e.g., numeric to numeric (error if overflows), but
            not string to int.

        * Carry over the metadata from the specified schema, while the columns and/or inner fields
            still keep their own metadata if not overwritten by the specified schema.

        * Fail if the nullability is not compatible. For example, the column and/or inner field
            is nullable but the specified schema requires them to be not nullable.

        Examples
        --------
        >>> from pyspark.sql.types import StructField, StringType
        >>> df = spark.createDataFrame([("a", 1)], ["i", "j"])
        >>> df.schema
        StructType([StructField(\'i\', StringType(), True), StructField(\'j\', LongType(), True)])

        >>> schema = StructType([StructField("j", StringType()), StructField("i", StringType())])
        >>> df2 = df.to(schema)
        >>> df2.schema
        StructType([StructField(\'j\', StringType(), True), StructField(\'i\', StringType(), True)])
        >>> df2.show()
        +---+---+
        |  j|  i|
        +---+---+
        |  1|  a|
        +---+---+
        '''
    def alias(self, alias: str) -> DataFrame:
        '''Returns a new :class:`DataFrame` with an alias set.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        alias : str
            an alias name to be set for the :class:`DataFrame`.

        Returns
        -------
        :class:`DataFrame`
            Aliased DataFrame.

        Examples
        --------
        >>> from pyspark.sql.functions import col, desc
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
        >>> df_as1 = df.alias("df_as1")
        >>> df_as2 = df.alias("df_as2")
        >>> joined_df = df_as1.join(df_as2, col("df_as1.name") == col("df_as2.name"), \'inner\')
        >>> joined_df.select(
        ...     "df_as1.name", "df_as2.name", "df_as2.age").sort(desc("df_as1.name")).show()
        +-----+-----+---+
        | name| name|age|
        +-----+-----+---+
        |  Tom|  Tom| 14|
        |  Bob|  Bob| 16|
        |Alice|Alice| 23|
        +-----+-----+---+
        '''
    def crossJoin(self, other: DataFrame) -> DataFrame:
        '''Returns the cartesian product with another :class:`DataFrame`.

        .. versionadded:: 2.1.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        other : :class:`DataFrame`
            Right side of the cartesian product.

        Returns
        -------
        :class:`DataFrame`
            Joined DataFrame.

        Examples
        --------
        >>> from pyspark.sql import Row
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
        >>> df2 = spark.createDataFrame(
        ...     [Row(height=80, name="Tom"), Row(height=85, name="Bob")])
        >>> df.crossJoin(df2.select("height")).select("age", "name", "height").show()
        +---+-----+------+
        |age| name|height|
        +---+-----+------+
        | 14|  Tom|    80|
        | 14|  Tom|    85|
        | 23|Alice|    80|
        | 23|Alice|    85|
        | 16|  Bob|    80|
        | 16|  Bob|    85|
        +---+-----+------+
        '''
    def join(self, other: DataFrame, on: str | List[str] | Column | List[Column] | None = None, how: str | None = None) -> DataFrame:
        '''Joins with another :class:`DataFrame`, using the given join expression.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        other : :class:`DataFrame`
            Right side of the join
        on : str, list or :class:`Column`, optional
            a string for the join column name, a list of column names,
            a join expression (Column), or a list of Columns.
            If `on` is a string or a list of strings indicating the name of the join column(s),
            the column(s) must exist on both sides, and this performs an equi-join.
        how : str, optional
            default ``inner``. Must be one of: ``inner``, ``cross``, ``outer``,
            ``full``, ``fullouter``, ``full_outer``, ``left``, ``leftouter``, ``left_outer``,
            ``right``, ``rightouter``, ``right_outer``, ``semi``, ``leftsemi``, ``left_semi``,
            ``anti``, ``leftanti`` and ``left_anti``.

        Returns
        -------
        :class:`DataFrame`
            Joined DataFrame.

        Examples
        --------
        The following performs a full outer join between ``df1`` and ``df2``.

        >>> from pyspark.sql import Row
        >>> from pyspark.sql.functions import desc
        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")]).toDF("age", "name")
        >>> df2 = spark.createDataFrame([Row(height=80, name="Tom"), Row(height=85, name="Bob")])
        >>> df3 = spark.createDataFrame([Row(age=2, name="Alice"), Row(age=5, name="Bob")])
        >>> df4 = spark.createDataFrame([
        ...     Row(age=10, height=80, name="Alice"),
        ...     Row(age=5, height=None, name="Bob"),
        ...     Row(age=None, height=None, name="Tom"),
        ...     Row(age=None, height=None, name=None),
        ... ])

        Inner join on columns (default)

        >>> df.join(df2, \'name\').select(df.name, df2.height).show()
        +----+------+
        |name|height|
        +----+------+
        | Bob|    85|
        +----+------+
        >>> df.join(df4, [\'name\', \'age\']).select(df.name, df.age).show()
        +----+---+
        |name|age|
        +----+---+
        | Bob|  5|
        +----+---+

        Outer join for both DataFrames on the \'name\' column.

        >>> df.join(df2, df.name == df2.name, \'outer\').select(
        ...     df.name, df2.height).sort(desc("name")).show()
        +-----+------+
        | name|height|
        +-----+------+
        |  Bob|    85|
        |Alice|  null|
        | null|    80|
        +-----+------+
        >>> df.join(df2, \'name\', \'outer\').select(\'name\', \'height\').sort(desc("name")).show()
        +-----+------+
        | name|height|
        +-----+------+
        |  Tom|    80|
        |  Bob|    85|
        |Alice|  null|
        +-----+------+

        Outer join for both DataFrams with multiple columns.

        >>> df.join(
        ...     df3,
        ...     [df.name == df3.name, df.age == df3.age],
        ...     \'outer\'
        ... ).select(df.name, df3.age).show()
        +-----+---+
        | name|age|
        +-----+---+
        |Alice|  2|
        |  Bob|  5|
        +-----+---+
        '''
    def sortWithinPartitions(self, *cols: str | Column | List[str | Column], **kwargs: Any) -> DataFrame:
        '''Returns a new :class:`DataFrame` with each partition sorted by the specified column(s).

        .. versionadded:: 1.6.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        cols : str, list or :class:`Column`, optional
            list of :class:`Column` or column names to sort by.

        Other Parameters
        ----------------
        ascending : bool or list, optional, default True
            boolean or list of boolean.
            Sort ascending vs. descending. Specify list for multiple sort orders.
            If a list is specified, the length of the list must equal the length of the `cols`.

        Returns
        -------
        :class:`DataFrame`
            DataFrame sorted by partitions.

        Examples
        --------
        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df.sortWithinPartitions("age", ascending=False)
        DataFrame[age: bigint, name: string]
        '''
    def sort(self, *cols: str | Column | List[str | Column], **kwargs: Any) -> DataFrame:
        '''Returns a new :class:`DataFrame` sorted by the specified column(s).

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        cols : str, list, or :class:`Column`, optional
             list of :class:`Column` or column names to sort by.

        Other Parameters
        ----------------
        ascending : bool or list, optional, default True
            boolean or list of boolean.
            Sort ascending vs. descending. Specify list for multiple sort orders.
            If a list is specified, the length of the list must equal the length of the `cols`.

        Returns
        -------
        :class:`DataFrame`
            Sorted DataFrame.

        Examples
        --------
        >>> from pyspark.sql.functions import desc, asc
        >>> df = spark.createDataFrame([
        ...     (2, "Alice"), (5, "Bob")], schema=["age", "name"])

        Sort the DataFrame in ascending order.

        >>> df.sort(asc("age")).show()
        +---+-----+
        |age| name|
        +---+-----+
        |  2|Alice|
        |  5|  Bob|
        +---+-----+

        Sort the DataFrame in descending order.

        >>> df.sort(df.age.desc()).show()
        +---+-----+
        |age| name|
        +---+-----+
        |  5|  Bob|
        |  2|Alice|
        +---+-----+
        >>> df.orderBy(df.age.desc()).show()
        +---+-----+
        |age| name|
        +---+-----+
        |  5|  Bob|
        |  2|Alice|
        +---+-----+
        >>> df.sort("age", ascending=False).show()
        +---+-----+
        |age| name|
        +---+-----+
        |  5|  Bob|
        |  2|Alice|
        +---+-----+

        Specify multiple columns

        >>> df = spark.createDataFrame([
        ...     (2, "Alice"), (2, "Bob"), (5, "Bob")], schema=["age", "name"])
        >>> df.orderBy(desc("age"), "name").show()
        +---+-----+
        |age| name|
        +---+-----+
        |  5|  Bob|
        |  2|Alice|
        |  2|  Bob|
        +---+-----+

        Specify multiple columns for sorting order at `ascending`.

        >>> df.orderBy(["age", "name"], ascending=[False, False]).show()
        +---+-----+
        |age| name|
        +---+-----+
        |  5|  Bob|
        |  2|  Bob|
        |  2|Alice|
        +---+-----+
        '''
    orderBy = sort
    def describe(self, *cols: str | List[str]) -> DataFrame:
        '''Computes basic statistics for numeric and string columns.

        .. versionadded:: 1.3.1

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        This includes count, mean, stddev, min, and max. If no columns are
        given, this function computes statistics for all numerical or string columns.

        Notes
        -----
        This function is meant for exploratory data analysis, as we make no
        guarantee about the backward compatibility of the schema of the resulting
        :class:`DataFrame`.

        Use summary for expanded statistics and control over which statistics to compute.

        Parameters
        ----------
        cols : str, list, optional
             Column name or list of column names to describe by (default All columns).

        Returns
        -------
        :class:`DataFrame`
            A new DataFrame that describes (provides statistics) given DataFrame.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [("Bob", 13, 40.3, 150.5), ("Alice", 12, 37.8, 142.3), ("Tom", 11, 44.1, 142.2)],
        ...     ["name", "age", "weight", "height"],
        ... )
        >>> df.describe([\'age\']).show()
        +-------+----+
        |summary| age|
        +-------+----+
        |  count|   3|
        |   mean|12.0|
        | stddev| 1.0|
        |    min|  11|
        |    max|  13|
        +-------+----+

        >>> df.describe([\'age\', \'weight\', \'height\']).show()
        +-------+----+------------------+-----------------+
        |summary| age|            weight|           height|
        +-------+----+------------------+-----------------+
        |  count|   3|                 3|                3|
        |   mean|12.0| 40.73333333333333|            145.0|
        | stddev| 1.0|3.1722757341273704|4.763402145525822|
        |    min|  11|              37.8|            142.2|
        |    max|  13|              44.1|            150.5|
        +-------+----+------------------+-----------------+

        See Also
        --------
        DataFrame.summary
        '''
    def summary(self, *statistics: str) -> DataFrame:
        '''Computes specified statistics for numeric and string columns. Available statistics are:
        - count
        - mean
        - stddev
        - min
        - max
        - arbitrary approximate percentiles specified as a percentage (e.g., 75%)

        If no statistics are given, this function computes count, mean, stddev, min,
        approximate quartiles (percentiles at 25%, 50%, and 75%), and max.

        .. versionadded:: 2.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        statistics : str, optional
             Column names to calculate statistics by (default All columns).

        Returns
        -------
        :class:`DataFrame`
            A new DataFrame that provides statistics for the given DataFrame.

        Notes
        -----
        This function is meant for exploratory data analysis, as we make no
        guarantee about the backward compatibility of the schema of the resulting
        :class:`DataFrame`.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [("Bob", 13, 40.3, 150.5), ("Alice", 12, 37.8, 142.3), ("Tom", 11, 44.1, 142.2)],
        ...     ["name", "age", "weight", "height"],
        ... )
        >>> df.select("age", "weight", "height").summary().show()
        +-------+----+------------------+-----------------+
        |summary| age|            weight|           height|
        +-------+----+------------------+-----------------+
        |  count|   3|                 3|                3|
        |   mean|12.0| 40.73333333333333|            145.0|
        | stddev| 1.0|3.1722757341273704|4.763402145525822|
        |    min|  11|              37.8|            142.2|
        |    25%|  11|              37.8|            142.2|
        |    50%|  12|              40.3|            142.3|
        |    75%|  13|              44.1|            150.5|
        |    max|  13|              44.1|            150.5|
        +-------+----+------------------+-----------------+

        >>> df.select("age", "weight", "height").summary("count", "min", "25%", "75%", "max").show()
        +-------+---+------+------+
        |summary|age|weight|height|
        +-------+---+------+------+
        |  count|  3|     3|     3|
        |    min| 11|  37.8| 142.2|
        |    25%| 11|  37.8| 142.2|
        |    75%| 13|  44.1| 150.5|
        |    max| 13|  44.1| 150.5|
        +-------+---+------+------+

        See Also
        --------
        DataFrame.display
        '''
    @overload
    def head(self) -> Row | None: ...
    @overload
    def head(self, n: int) -> List[Row]: ...
    def first(self) -> Row | None:
        '''Returns the first row as a :class:`Row`.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        :class:`Row`
            First row if :class:`DataFrame` is not empty, otherwise ``None``.

        Examples
        --------
        >>> df = spark.createDataFrame([
        ...     (2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df.first()
        Row(age=2, name=\'Alice\')
        '''
    @overload
    def __getitem__(self, item: int | str) -> Column: ...
    @overload
    def __getitem__(self, item: Column | List | Tuple) -> DataFrame: ...
    def __getattr__(self, name: str) -> Column:
        '''Returns the :class:`Column` denoted by ``name``.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        name : str
            Column name to return as :class:`Column`.

        Returns
        -------
        :class:`Column`
            Requested column.

        Examples
        --------
        >>> df = spark.createDataFrame([
        ...     (2, "Alice"), (5, "Bob")], schema=["age", "name"])

        Retrieve a column instance.

        >>> df.select(df.age).show()
        +---+
        |age|
        +---+
        |  2|
        |  5|
        +---+
        '''
    @overload
    def select(self, *cols: ColumnOrName) -> DataFrame: ...
    @overload
    def select(self, __cols: List[Column] | List[str]) -> DataFrame: ...
    @overload
    def selectExpr(self, *expr: str) -> DataFrame: ...
    @overload
    def selectExpr(self, *expr: List[str]) -> DataFrame: ...
    def filter(self, condition: ColumnOrName) -> DataFrame:
        '''Filters rows using the given condition.

        :func:`where` is an alias for :func:`filter`.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        condition : :class:`Column` or str
            a :class:`Column` of :class:`types.BooleanType`
            or a string of SQL expressions.

        Returns
        -------
        :class:`DataFrame`
            Filtered DataFrame.

        Examples
        --------
        >>> df = spark.createDataFrame([
        ...     (2, "Alice"), (5, "Bob")], schema=["age", "name"])

        Filter by :class:`Column` instances.

        >>> df.filter(df.age > 3).show()
        +---+----+
        |age|name|
        +---+----+
        |  5| Bob|
        +---+----+
        >>> df.where(df.age == 2).show()
        +---+-----+
        |age| name|
        +---+-----+
        |  2|Alice|
        +---+-----+

        Filter by SQL expression in a string.

        >>> df.filter("age > 3").show()
        +---+----+
        |age|name|
        +---+----+
        |  5| Bob|
        +---+----+
        >>> df.where("age = 2").show()
        +---+-----+
        |age| name|
        +---+-----+
        |  2|Alice|
        +---+-----+
        '''
    @overload
    def groupBy(self, *cols: ColumnOrName) -> GroupedData: ...
    @overload
    def groupBy(self, __cols: List[Column] | List[str]) -> GroupedData: ...
    @overload
    def rollup(self, *cols: ColumnOrName) -> GroupedData: ...
    @overload
    def rollup(self, __cols: List[Column] | List[str]) -> GroupedData: ...
    @overload
    def cube(self, *cols: ColumnOrName) -> GroupedData: ...
    @overload
    def cube(self, __cols: List[Column] | List[str]) -> GroupedData: ...
    def unpivot(self, ids: ColumnOrName | List['ColumnOrName'] | Tuple['ColumnOrName', ...], values: ColumnOrName | List['ColumnOrName'] | Tuple['ColumnOrName', ...] | None, variableColumnName: str, valueColumnName: str) -> DataFrame:
        '''
        Unpivot a DataFrame from wide format to long format, optionally leaving
        identifier columns set. This is the reverse to `groupBy(...).pivot(...).agg(...)`,
        except for the aggregation, which cannot be reversed.

        This function is useful to massage a DataFrame into a format where some
        columns are identifier columns ("ids"), while all other columns ("values")
        are "unpivoted" to the rows, leaving just two non-id columns, named as given
        by `variableColumnName` and `valueColumnName`.

        When no "id" columns are given, the unpivoted DataFrame consists of only the
        "variable" and "value" columns.

        The `values` columns must not be empty so at least one value must be given to be unpivoted.
        When `values` is `None`, all non-id columns will be unpivoted.

        All "value" columns must share a least common data type. Unless they are the same data type,
        all "value" columns are cast to the nearest common data type. For instance, types
        `IntegerType` and `LongType` are cast to `LongType`, while `IntegerType` and `StringType`
        do not have a common data type and `unpivot` fails.

        .. versionadded:: 3.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        ids : str, Column, tuple, list
            Column(s) to use as identifiers. Can be a single column or column name,
            or a list or tuple for multiple columns.
        values : str, Column, tuple, list, optional
            Column(s) to unpivot. Can be a single column or column name, or a list or tuple
            for multiple columns. If specified, must not be empty. If not specified, uses all
            columns that are not set as `ids`.
        variableColumnName : str
            Name of the variable column.
        valueColumnName : str
            Name of the value column.

        Returns
        -------
        :class:`DataFrame`
            Unpivoted DataFrame.

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(1, 11, 1.1), (2, 12, 1.2)],
        ...     ["id", "int", "double"],
        ... )
        >>> df.show()
        +---+---+------+
        | id|int|double|
        +---+---+------+
        |  1| 11|   1.1|
        |  2| 12|   1.2|
        +---+---+------+

        >>> df.unpivot("id", ["int", "double"], "var", "val").show()
        +---+------+----+
        | id|   var| val|
        +---+------+----+
        |  1|   int|11.0|
        |  1|double| 1.1|
        |  2|   int|12.0|
        |  2|double| 1.2|
        +---+------+----+

        See Also
        --------
        DataFrame.melt
        '''
    def melt(self, ids: ColumnOrName | List['ColumnOrName'] | Tuple['ColumnOrName', ...], values: ColumnOrName | List['ColumnOrName'] | Tuple['ColumnOrName', ...] | None, variableColumnName: str, valueColumnName: str) -> DataFrame:
        """
        Unpivot a DataFrame from wide format to long format, optionally leaving
        identifier columns set. This is the reverse to `groupBy(...).pivot(...).agg(...)`,
        except for the aggregation, which cannot be reversed.

        :func:`melt` is an alias for :func:`unpivot`.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        ids : str, Column, tuple, list, optional
            Column(s) to use as identifiers. Can be a single column or column name,
            or a list or tuple for multiple columns.
        values : str, Column, tuple, list, optional
            Column(s) to unpivot. Can be a single column or column name, or a list or tuple
            for multiple columns. If not specified or empty, use all columns that
            are not set as `ids`.
        variableColumnName : str
            Name of the variable column.
        valueColumnName : str
            Name of the value column.

        Returns
        -------
        :class:`DataFrame`
            Unpivoted DataFrame.

        See Also
        --------
        DataFrame.unpivot
        """
    def agg(self, *exprs: Column | Dict[str, str]) -> DataFrame:
        '''Aggregate on the entire :class:`DataFrame` without groups
        (shorthand for ``df.groupBy().agg()``).

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        exprs : :class:`Column` or dict of key and value strings
            Columns or expressions to aggregate DataFrame by.

        Returns
        -------
        :class:`DataFrame`
            Aggregated DataFrame.

        Examples
        --------
        >>> from pyspark.sql import functions as F
        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df.agg({"age": "max"}).show()
        +--------+
        |max(age)|
        +--------+
        |       5|
        +--------+
        >>> df.agg(F.min(df.age)).show()
        +--------+
        |min(age)|
        +--------+
        |       2|
        +--------+
        '''
    def observe(self, observation: Observation | str, *exprs: Column) -> DataFrame:
        '''Define (named) metrics to observe on the DataFrame. This method returns an \'observed\'
        DataFrame that returns the same result as the input, with the following guarantees:

        * It will compute the defined aggregates (metrics) on all the data that is flowing through
            the Dataset at that point.

        * It will report the value of the defined aggregate columns as soon as we reach a completion
            point. A completion point is either the end of a query (batch mode) or the end of a
            streaming epoch. The value of the aggregates only reflects the data processed since
            the previous completion point.

        The metrics columns must either contain a literal (e.g. lit(42)), or should contain one or
        more aggregate functions (e.g. sum(a) or sum(a + b) + avg(c) - lit(1)). Expressions that
        contain references to the input Dataset\'s columns must always be wrapped in an aggregate
        function.

        A user can observe these metrics by adding
        Python\'s :class:`~pyspark.sql.streaming.StreamingQueryListener`,
        Scala/Java\'s ``org.apache.spark.sql.streaming.StreamingQueryListener`` or Scala/Java\'s
        ``org.apache.spark.sql.util.QueryExecutionListener`` to the spark session.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        observation : :class:`Observation` or str
            `str` to specify the name, or an :class:`Observation` instance to obtain the metric.

            .. versionchanged:: 3.4.0
               Added support for `str` in this parameter.
        exprs : :class:`Column`
            column expressions (:class:`Column`).

        Returns
        -------
        :class:`DataFrame`
            the observed :class:`DataFrame`.

        Notes
        -----
        When ``observation`` is :class:`Observation`, this method only supports batch queries.
        When ``observation`` is a string, this method works for both batch and streaming queries.
        Continuous execution is currently not supported yet.

        Examples
        --------
        When ``observation`` is :class:`Observation`, only batch queries work as below.

        >>> from pyspark.sql.functions import col, count, lit, max
        >>> from pyspark.sql import Observation
        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> observation = Observation("my metrics")
        >>> observed_df = df.observe(observation, count(lit(1)).alias("count"), max(col("age")))
        >>> observed_df.count()
        2
        >>> observation.get
        {\'count\': 2, \'max(age)\': 5}

        When ``observation`` is a string, streaming queries also work as below.

        >>> from pyspark.sql.streaming import StreamingQueryListener
        >>> class MyErrorListener(StreamingQueryListener):
        ...    def onQueryStarted(self, event):
        ...        pass
        ...
        ...    def onQueryProgress(self, event):
        ...        row = event.progress.observedMetrics.get("my_event")
        ...        # Trigger if the number of errors exceeds 5 percent
        ...        num_rows = row.rc
        ...        num_error_rows = row.erc
        ...        ratio = num_error_rows / num_rows
        ...        if ratio > 0.05:
        ...            # Trigger alert
        ...            pass
        ...
        ...    def onQueryTerminated(self, event):
        ...        pass
        ...
        >>> spark.streams.addListener(MyErrorListener())
        >>> # Observe row count (rc) and error row count (erc) in the streaming Dataset
        ... observed_ds = df.observe(
        ...     "my_event",
        ...     count(lit(1)).alias("rc"),
        ...     count(col("error")).alias("erc"))  # doctest: +SKIP
        >>> observed_ds.writeStream.format("console").start()  # doctest: +SKIP
        '''
    def union(self, other: DataFrame) -> DataFrame:
        '''Return a new :class:`DataFrame` containing union of rows in this and another
        :class:`DataFrame`.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        other : :class:`DataFrame`
            Another :class:`DataFrame` that needs to be unioned

        Returns
        -------
        :class:`DataFrame`

        See Also
        --------
        DataFrame.unionAll

        Notes
        -----
        This is equivalent to `UNION ALL` in SQL. To do a SQL-style set union
        (that does deduplication of elements), use this function followed by :func:`distinct`.

        Also as standard in SQL, this function resolves columns by position (not by name).

        Examples
        --------
        >>> df1 = spark.createDataFrame([[1, 2, 3]], ["col0", "col1", "col2"])
        >>> df2 = spark.createDataFrame([[4, 5, 6]], ["col1", "col2", "col0"])
        >>> df1.union(df2).show()
        +----+----+----+
        |col0|col1|col2|
        +----+----+----+
        |   1|   2|   3|
        |   4|   5|   6|
        +----+----+----+
        >>> df1.union(df1).show()
        +----+----+----+
        |col0|col1|col2|
        +----+----+----+
        |   1|   2|   3|
        |   1|   2|   3|
        +----+----+----+
        '''
    def unionAll(self, other: DataFrame) -> DataFrame:
        """Return a new :class:`DataFrame` containing union of rows in this and another
        :class:`DataFrame`.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        other : :class:`DataFrame`
            Another :class:`DataFrame` that needs to be combined

        Returns
        -------
        :class:`DataFrame`
            Combined DataFrame

        Notes
        -----
        This is equivalent to `UNION ALL` in SQL. To do a SQL-style set union
        (that does deduplication of elements), use this function followed by :func:`distinct`.

        Also as standard in SQL, this function resolves columns by position (not by name).

        :func:`unionAll` is an alias to :func:`union`

        See Also
        --------
        DataFrame.union
        """
    def unionByName(self, other: DataFrame, allowMissingColumns: bool = False) -> DataFrame:
        '''Returns a new :class:`DataFrame` containing union of rows in this and another
        :class:`DataFrame`.

        This is different from both `UNION ALL` and `UNION DISTINCT` in SQL. To do a SQL-style set
        union (that does deduplication of elements), use this function followed by :func:`distinct`.

        .. versionadded:: 2.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        other : :class:`DataFrame`
            Another :class:`DataFrame` that needs to be combined.
        allowMissingColumns : bool, optional, default False
           Specify whether to allow missing columns.

           .. versionadded:: 3.1.0

        Returns
        -------
        :class:`DataFrame`
            Combined DataFrame.

        Examples
        --------
        The difference between this function and :func:`union` is that this function
        resolves columns by name (not by position):

        >>> df1 = spark.createDataFrame([[1, 2, 3]], ["col0", "col1", "col2"])
        >>> df2 = spark.createDataFrame([[4, 5, 6]], ["col1", "col2", "col0"])
        >>> df1.unionByName(df2).show()
        +----+----+----+
        |col0|col1|col2|
        +----+----+----+
        |   1|   2|   3|
        |   6|   4|   5|
        +----+----+----+

        When the parameter `allowMissingColumns` is ``True``, the set of column names
        in this and other :class:`DataFrame` can differ; missing columns will be filled with null.
        Further, the missing columns of this :class:`DataFrame` will be added at the end
        in the schema of the union result:

        >>> df1 = spark.createDataFrame([[1, 2, 3]], ["col0", "col1", "col2"])
        >>> df2 = spark.createDataFrame([[4, 5, 6]], ["col1", "col2", "col3"])
        >>> df1.unionByName(df2, allowMissingColumns=True).show()
        +----+----+----+----+
        |col0|col1|col2|col3|
        +----+----+----+----+
        |   1|   2|   3|null|
        |null|   4|   5|   6|
        +----+----+----+----+
        '''
    def intersect(self, other: DataFrame) -> DataFrame:
        '''Return a new :class:`DataFrame` containing rows only in
        both this :class:`DataFrame` and another :class:`DataFrame`.
        Note that any duplicates are removed. To preserve duplicates
        use :func:`intersectAll`.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        other : :class:`DataFrame`
            Another :class:`DataFrame` that needs to be combined.

        Returns
        -------
        :class:`DataFrame`
            Combined DataFrame.

        Notes
        -----
        This is equivalent to `INTERSECT` in SQL.

        Examples
        --------
        >>> df1 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3), ("c", 4)], ["C1", "C2"])
        >>> df2 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3)], ["C1", "C2"])
        >>> df1.intersect(df2).sort(df1.C1.desc()).show()
        +---+---+
        | C1| C2|
        +---+---+
        |  b|  3|
        |  a|  1|
        +---+---+
        '''
    def intersectAll(self, other: DataFrame) -> DataFrame:
        '''Return a new :class:`DataFrame` containing rows in both this :class:`DataFrame`
        and another :class:`DataFrame` while preserving duplicates.

        This is equivalent to `INTERSECT ALL` in SQL. As standard in SQL, this function
        resolves columns by position (not by name).

        .. versionadded:: 2.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        other : :class:`DataFrame`
            Another :class:`DataFrame` that needs to be combined.

        Returns
        -------
        :class:`DataFrame`
            Combined DataFrame.

        Examples
        --------
        >>> df1 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3), ("c", 4)], ["C1", "C2"])
        >>> df2 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3)], ["C1", "C2"])
        >>> df1.intersectAll(df2).sort("C1", "C2").show()
        +---+---+
        | C1| C2|
        +---+---+
        |  a|  1|
        |  a|  1|
        |  b|  3|
        +---+---+
        '''
    def subtract(self, other: DataFrame) -> DataFrame:
        '''Return a new :class:`DataFrame` containing rows in this :class:`DataFrame`
        but not in another :class:`DataFrame`.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        other : :class:`DataFrame`
            Another :class:`DataFrame` that needs to be subtracted.

        Returns
        -------
        :class:`DataFrame`
            Subtracted DataFrame.

        Notes
        -----
        This is equivalent to `EXCEPT DISTINCT` in SQL.

        Examples
        --------
        >>> df1 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3), ("c", 4)], ["C1", "C2"])
        >>> df2 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3)], ["C1", "C2"])
        >>> df1.subtract(df2).show()
        +---+---+
        | C1| C2|
        +---+---+
        |  c|  4|
        +---+---+
        '''
    def dropDuplicates(self, subset: List[str] | None = None) -> DataFrame:
        """Return a new :class:`DataFrame` with duplicate rows removed,
        optionally only considering certain columns.

        For a static batch :class:`DataFrame`, it just drops duplicate rows. For a streaming
        :class:`DataFrame`, it will keep all data across triggers as intermediate state to drop
        duplicates rows. You can use :func:`withWatermark` to limit how late the duplicate data can
        be and the system will accordingly limit the state. In addition, data older than
        watermark will be dropped to avoid any possibility of duplicates.

        :func:`drop_duplicates` is an alias for :func:`dropDuplicates`.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        subset : List of column names, optional
            List of columns to use for duplicate comparison (default All columns).

        Returns
        -------
        :class:`DataFrame`
            DataFrame without duplicates.

        Examples
        --------
        >>> from pyspark.sql import Row
        >>> df = spark.createDataFrame([
        ...     Row(name='Alice', age=5, height=80),
        ...     Row(name='Alice', age=5, height=80),
        ...     Row(name='Alice', age=10, height=80)
        ... ])

        Deduplicate the same rows.

        >>> df.dropDuplicates().show()
        +-----+---+------+
        | name|age|height|
        +-----+---+------+
        |Alice|  5|    80|
        |Alice| 10|    80|
        +-----+---+------+

        Deduplicate values on 'name' and 'height' columns.

        >>> df.dropDuplicates(['name', 'height']).show()
        +-----+---+------+
        | name|age|height|
        +-----+---+------+
        |Alice|  5|    80|
        +-----+---+------+
        """
    def dropna(self, how: str = 'any', thresh: int | None = None, subset: str | Tuple[str, ...] | List[str] | None = None) -> DataFrame:
        '''Returns a new :class:`DataFrame` omitting rows with null values.
        :func:`DataFrame.dropna` and :func:`DataFrameNaFunctions.drop` are aliases of each other.

        .. versionadded:: 1.3.1

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        how : str, optional
            \'any\' or \'all\'.
            If \'any\', drop a row if it contains any nulls.
            If \'all\', drop a row only if all its values are null.
        thresh: int, optional
            default None
            If specified, drop rows that have less than `thresh` non-null values.
            This overwrites the `how` parameter.
        subset : str, tuple or list, optional
            optional list of column names to consider.

        Returns
        -------
        :class:`DataFrame`
            DataFrame with null only rows excluded.

        Examples
        --------
        >>> from pyspark.sql import Row
        >>> df = spark.createDataFrame([
        ...     Row(age=10, height=80, name="Alice"),
        ...     Row(age=5, height=None, name="Bob"),
        ...     Row(age=None, height=None, name="Tom"),
        ...     Row(age=None, height=None, name=None),
        ... ])
        >>> df.na.drop().show()
        +---+------+-----+
        |age|height| name|
        +---+------+-----+
        | 10|    80|Alice|
        +---+------+-----+
        '''
    @overload
    def fillna(self, value: LiteralType, subset: str | Tuple[str, ...] | List[str] | None = ...) -> DataFrame: ...
    @overload
    def fillna(self, value: Dict[str, 'LiteralType']) -> DataFrame: ...
    @overload
    def replace(self, to_replace: LiteralType, value: OptionalPrimitiveType, subset: List[str] | None = ...) -> DataFrame: ...
    @overload
    def replace(self, to_replace: List['LiteralType'], value: List['OptionalPrimitiveType'], subset: List[str] | None = ...) -> DataFrame: ...
    @overload
    def replace(self, to_replace: Dict['LiteralType', 'OptionalPrimitiveType'], subset: List[str] | None = ...) -> DataFrame: ...
    @overload
    def replace(self, to_replace: List['LiteralType'], value: OptionalPrimitiveType, subset: List[str] | None = ...) -> DataFrame: ...
    @overload
    def approxQuantile(self, col: str, probabilities: List[float] | Tuple[float], relativeError: float) -> List[float]: ...
    @overload
    def approxQuantile(self, col: List[str] | Tuple[str], probabilities: List[float] | Tuple[float], relativeError: float) -> List[List[float]]: ...
    def corr(self, col1: str, col2: str, method: str | None = None) -> float:
        '''
        Calculates the correlation of two columns of a :class:`DataFrame` as a double value.
        Currently only supports the Pearson Correlation Coefficient.
        :func:`DataFrame.corr` and :func:`DataFrameStatFunctions.corr` are aliases of each other.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        col1 : str
            The name of the first column
        col2 : str
            The name of the second column
        method : str, optional
            The correlation method. Currently only supports "pearson"

        Returns
        -------
        float
            Pearson Correlation Coefficient of two columns.

        Examples
        --------
        >>> df = spark.createDataFrame([(1, 12), (10, 1), (19, 8)], ["c1", "c2"])
        >>> df.corr("c1", "c2")
        -0.3592106040535498
        >>> df = spark.createDataFrame([(11, 12), (10, 11), (9, 10)], ["small", "bigger"])
        >>> df.corr("small", "bigger")
        1.0

        '''
    def cov(self, col1: str, col2: str) -> float:
        '''
        Calculate the sample covariance for the given columns, specified by their names, as a
        double value. :func:`DataFrame.cov` and :func:`DataFrameStatFunctions.cov` are aliases.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        col1 : str
            The name of the first column
        col2 : str
            The name of the second column

        Returns
        -------
        float
            Covariance of two columns.

        Examples
        --------
        >>> df = spark.createDataFrame([(1, 12), (10, 1), (19, 8)], ["c1", "c2"])
        >>> df.cov("c1", "c2")
        -18.0
        >>> df = spark.createDataFrame([(11, 12), (10, 11), (9, 10)], ["small", "bigger"])
        >>> df.cov("small", "bigger")
        1.0

        '''
    def crosstab(self, col1: str, col2: str) -> DataFrame:
        '''
        Computes a pair-wise frequency table of the given columns. Also known as a contingency
        table.
        The first column of each row will be the distinct values of `col1` and the column names
        will be the distinct values of `col2`. The name of the first column will be `$col1_$col2`.
        Pairs that have no occurrences will have zero as their counts.
        :func:`DataFrame.crosstab` and :func:`DataFrameStatFunctions.crosstab` are aliases.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        col1 : str
            The name of the first column. Distinct items will make the first item of
            each row.
        col2 : str
            The name of the second column. Distinct items will make the column names
            of the :class:`DataFrame`.

        Returns
        -------
        :class:`DataFrame`
            Frequency matrix of two columns.

        Examples
        --------
        >>> df = spark.createDataFrame([(1, 11), (1, 11), (3, 10), (4, 8), (4, 8)], ["c1", "c2"])
        >>> df.crosstab("c1", "c2").sort("c1_c2").show()
        +-----+---+---+---+
        |c1_c2| 10| 11|  8|
        +-----+---+---+---+
        |    1|  0|  2|  0|
        |    3|  1|  0|  0|
        |    4|  0|  0|  2|
        +-----+---+---+---+

        '''
    def freqItems(self, cols: List[str] | Tuple[str], support: float | None = None) -> DataFrame:
        '''
        Finding frequent items for columns, possibly with false positives. Using the
        frequent element count algorithm described in
        "https://doi.org/10.1145/762471.762473, proposed by Karp, Schenker, and Papadimitriou".
        :func:`DataFrame.freqItems` and :func:`DataFrameStatFunctions.freqItems` are aliases.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        cols : list or tuple
            Names of the columns to calculate frequent items for as a list or tuple of
            strings.
        support : float, optional
            The frequency with which to consider an item \'frequent\'. Default is 1%.
            The support must be greater than 1e-4.

        Returns
        -------
        :class:`DataFrame`
            DataFrame with frequent items.

        Notes
        -----
        This function is meant for exploratory data analysis, as we make no
        guarantee about the backward compatibility of the schema of the resulting
        :class:`DataFrame`.

        Examples
        --------
        >>> df = spark.createDataFrame([(1, 11), (1, 11), (3, 10), (4, 8), (4, 8)], ["c1", "c2"])
        >>> df.freqItems(["c1", "c2"]).show()  # doctest: +SKIP
        +------------+------------+
        |c1_freqItems|c2_freqItems|
        +------------+------------+
        |   [4, 1, 3]| [8, 11, 10]|
        +------------+------------+
        '''
    def withColumns(self, *colsMap: Dict[str, Column]) -> DataFrame:
        '''
        Returns a new :class:`DataFrame` by adding multiple columns or replacing the
        existing columns that have the same names.

        The colsMap is a map of column name and column, the column must only refer to attributes
        supplied by this Dataset. It is an error to add columns that refer to some other Dataset.

        .. versionadded:: 3.3.0
           Added support for multiple columns adding

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        colsMap : dict
            a dict of column name and :class:`Column`. Currently, only a single map is supported.

        Returns
        -------
        :class:`DataFrame`
            DataFrame with new or replaced columns.

        Examples
        --------
        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df.withColumns({\'age2\': df.age + 2, \'age3\': df.age + 3}).show()
        +---+-----+----+----+
        |age| name|age2|age3|
        +---+-----+----+----+
        |  2|Alice|   4|   5|
        |  5|  Bob|   7|   8|
        +---+-----+----+----+
        '''
    def withColumn(self, colName: str, col: Column) -> DataFrame:
        '''
        Returns a new :class:`DataFrame` by adding a column or replacing the
        existing column that has the same name.

        The column expression must be an expression over this :class:`DataFrame`; attempting to add
        a column from some other :class:`DataFrame` will raise an error.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        colName : str
            string, name of the new column.
        col : :class:`Column`
            a :class:`Column` expression for the new column.

        Returns
        -------
        :class:`DataFrame`
            DataFrame with new or replaced column.

        Notes
        -----
        This method introduces a projection internally. Therefore, calling it multiple
        times, for instance, via loops in order to add multiple columns can generate big
        plans which can cause performance issues and even `StackOverflowException`.
        To avoid this, use :func:`select` with multiple columns at once.

        Examples
        --------
        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df.withColumn(\'age2\', df.age + 2).show()
        +---+-----+----+
        |age| name|age2|
        +---+-----+----+
        |  2|Alice|   4|
        |  5|  Bob|   7|
        +---+-----+----+
        '''
    def withColumnRenamed(self, existing: str, new: str) -> DataFrame:
        '''Returns a new :class:`DataFrame` by renaming an existing column.
        This is a no-op if the schema doesn\'t contain the given column name.

        .. versionadded:: 1.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        existing : str
            string, name of the existing column to rename.
        new : str
            string, new name of the column.

        Returns
        -------
        :class:`DataFrame`
            DataFrame with renamed column.

        Examples
        --------
        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df.withColumnRenamed(\'age\', \'age2\').show()
        +----+-----+
        |age2| name|
        +----+-----+
        |   2|Alice|
        |   5|  Bob|
        +----+-----+
        '''
    def withColumnsRenamed(self, colsMap: Dict[str, str]) -> DataFrame:
        '''
        Returns a new :class:`DataFrame` by renaming multiple columns.
        This is a no-op if the schema doesn\'t contain the given column names.

        .. versionadded:: 3.4.0
           Added support for multiple columns renaming

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        colsMap : dict
            a dict of existing column names and corresponding desired column names.
            Currently, only a single map is supported.

        Returns
        -------
        :class:`DataFrame`
            DataFrame with renamed columns.

        See Also
        --------
        :meth:`withColumnRenamed`

        Examples
        --------
        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df = df.withColumns({\'age2\': df.age + 2, \'age3\': df.age + 3})
        >>> df.withColumnsRenamed({\'age2\': \'age4\', \'age3\': \'age5\'}).show()
        +---+-----+----+----+
        |age| name|age4|age5|
        +---+-----+----+----+
        |  2|Alice|   4|   5|
        |  5|  Bob|   7|   8|
        +---+-----+----+----+
        '''
    def withMetadata(self, columnName: str, metadata: Dict[str, Any]) -> DataFrame:
        '''Returns a new :class:`DataFrame` by updating an existing column with metadata.

        .. versionadded:: 3.3.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        columnName : str
            string, name of the existing column to update the metadata.
        metadata : dict
            dict, new metadata to be assigned to df.schema[columnName].metadata

        Returns
        -------
        :class:`DataFrame`
            DataFrame with updated metadata column.

        Examples
        --------
        >>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
        >>> df_meta = df.withMetadata(\'age\', {\'foo\': \'bar\'})
        >>> df_meta.schema[\'age\'].metadata
        {\'foo\': \'bar\'}
        '''
    @overload
    def drop(self, cols: ColumnOrName) -> DataFrame: ...
    @overload
    def drop(self, *cols: str) -> DataFrame: ...
    def toDF(self, *cols: str) -> DataFrame:
        '''Returns a new :class:`DataFrame` that with new specified column names

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        *cols : tuple
            a tuple of string new column name. The length of the
            list needs to be the same as the number of columns in the initial
            :class:`DataFrame`

        Returns
        -------
        :class:`DataFrame`
            DataFrame with new column names.

        Examples
        --------
        >>> df = spark.createDataFrame([(14, "Tom"), (23, "Alice"),
        ...     (16, "Bob")], ["age", "name"])
        >>> df.toDF(\'f1\', \'f2\').show()
        +---+-----+
        | f1|   f2|
        +---+-----+
        | 14|  Tom|
        | 23|Alice|
        | 16|  Bob|
        +---+-----+
        '''
    def transform(self, func: Callable[..., 'DataFrame'], *args: Any, **kwargs: Any) -> DataFrame:
        '''Returns a new :class:`DataFrame`. Concise syntax for chaining custom transformations.

        .. versionadded:: 3.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        func : function
            a function that takes and returns a :class:`DataFrame`.
        *args
            Positional arguments to pass to func.

            .. versionadded:: 3.3.0
        **kwargs
            Keyword arguments to pass to func.

            .. versionadded:: 3.3.0

        Returns
        -------
        :class:`DataFrame`
            Transformed DataFrame.

        Examples
        --------
        >>> from pyspark.sql.functions import col
        >>> df = spark.createDataFrame([(1, 1.0), (2, 2.0)], ["int", "float"])
        >>> def cast_all_to_int(input_df):
        ...     return input_df.select([col(col_name).cast("int") for col_name in input_df.columns])
        >>> def sort_columns_asc(input_df):
        ...     return input_df.select(*sorted(input_df.columns))
        >>> df.transform(cast_all_to_int).transform(sort_columns_asc).show()
        +-----+---+
        |float|int|
        +-----+---+
        |    1|  1|
        |    2|  2|
        +-----+---+

        >>> def add_n(input_df, n):
        ...     return input_df.select([(col(col_name) + n).alias(col_name)
        ...                             for col_name in input_df.columns])
        >>> df.transform(add_n, 1).transform(add_n, n=10).show()
        +---+-----+
        |int|float|
        +---+-----+
        | 12| 12.0|
        | 13| 13.0|
        +---+-----+
        '''
    def sameSemantics(self, other: DataFrame) -> bool:
        '''
        Returns `True` when the logical query plans inside both :class:`DataFrame`\\s are equal and
        therefore return the same results.

        .. versionadded:: 3.1.0

        Notes
        -----
        The equality comparison here is simplified by tolerating the cosmetic differences
        such as attribute names.

        This API can compare both :class:`DataFrame`\\s very fast but can still return
        `False` on the :class:`DataFrame` that return the same results, for instance, from
        different plans. Such false negative semantic can be useful when caching as an example.

        This API is a developer API.

        Parameters
        ----------
        other : :class:`DataFrame`
            The other DataFrame to compare against.

        Returns
        -------
        bool
            Whether these two DataFrames are similar.

        Examples
        --------
        >>> df1 = spark.range(10)
        >>> df2 = spark.range(10)
        >>> df1.withColumn("col1", df1.id * 2).sameSemantics(df2.withColumn("col1", df2.id * 2))
        True
        >>> df1.withColumn("col1", df1.id * 2).sameSemantics(df2.withColumn("col1", df2.id + 2))
        False
        >>> df1.withColumn("col1", df1.id * 2).sameSemantics(df2.withColumn("col0", df2.id * 2))
        True
        '''
    def semanticHash(self) -> int:
        '''
        Returns a hash code of the logical query plan against this :class:`DataFrame`.

        .. versionadded:: 3.1.0

        Notes
        -----
        Unlike the standard hash code, the hash is calculated against the query plan
        simplified by tolerating the cosmetic differences such as attribute names.

        This API is a developer API.

        Returns
        -------
        int
            Hash value.

        Examples
        --------
        >>> spark.range(10).selectExpr("id as col0").semanticHash()  # doctest: +SKIP
        1855039936
        >>> spark.range(10).selectExpr("id as col1").semanticHash()  # doctest: +SKIP
        1855039936
        '''
    def inputFiles(self) -> List[str]:
        '''
        Returns a best-effort snapshot of the files that compose this :class:`DataFrame`.
        This method simply asks each constituent BaseRelation for its respective files and
        takes the union of all results. Depending on the source relations, this may not find
        all input files. Duplicates are removed.

        .. versionadded:: 3.1.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        list
            List of file paths.

        Examples
        --------
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a single-row DataFrame into a JSON file
        ...     spark.createDataFrame(
        ...         [{"age": 100, "name": "Hyukjin Kwon"}]
        ...     ).repartition(1).write.json(d, mode="overwrite")
        ...
        ...     # Read the JSON file as a DataFrame.
        ...     df = spark.read.format("json").load(d)
        ...
        ...     # Returns the number of input files.
        ...     len(df.inputFiles())
        1
        '''
    where: Incomplete
    groupby: Incomplete
    drop_duplicates: Incomplete
    def writeTo(self, table: str) -> DataFrameWriterV2:
        '''
        Create a write configuration builder for v2 sources.

        This builder is used to configure and execute write operations.

        For example, to append or create or replace existing tables.

        .. versionadded:: 3.1.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        table : str
            Target table name to write to.

        Returns
        -------
        :class:`DataFrameWriterV2`
            DataFrameWriterV2 to use further to specify how to save the data

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
        >>> df.writeTo("catalog.db.table").append()  # doctest: +SKIP
        >>> df.writeTo(                              # doctest: +SKIP
        ...     "catalog.db.table"
        ... ).partitionedBy("col").createOrReplace()
        '''
    def to_pandas_on_spark(self, index_col: str | List[str] | None = None) -> PandasOnSparkDataFrame: ...
    def pandas_api(self, index_col: str | List[str] | None = None) -> PandasOnSparkDataFrame:
        '''
        Converts the existing DataFrame into a pandas-on-Spark DataFrame.

        If a pandas-on-Spark DataFrame is converted to a Spark DataFrame and then back
        to pandas-on-Spark, it will lose the index information and the original index
        will be turned into a normal column.

        This is only available if Pandas is installed and available.

        Parameters
        ----------
        index_col: str or list of str, optional, default: None
            Index column of table in Spark.

        Returns
        -------
        :class:`PandasOnSparkDataFrame`

        See Also
        --------
        pyspark.pandas.frame.DataFrame.to_spark

        Examples
        --------
        >>> df = spark.createDataFrame(
        ...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])

        >>> df.pandas_api()  # doctest: +SKIP
           age   name
        0   14    Tom
        1   23  Alice
        2   16    Bob

        We can specify the index columns.

        >>> df.pandas_api(index_col="age")  # doctest: +SKIP
              name
        age
        14     Tom
        23   Alice
        16     Bob
        '''
    def to_koalas(self, index_col: str | List[str] | None = None) -> PandasOnSparkDataFrame: ...

class DataFrameNaFunctions:
    """Functionality for working with missing data in :class:`DataFrame`.

    .. versionadded:: 1.4.0

    .. versionchanged:: 3.4.0
        Supports Spark Connect.
    """
    df: Incomplete
    def __init__(self, df: DataFrame) -> None: ...
    def drop(self, how: str = 'any', thresh: int | None = None, subset: str | Tuple[str, ...] | List[str] | None = None) -> DataFrame: ...
    @overload
    def fill(self, value: LiteralType, subset: List[str] | None = ...) -> DataFrame: ...
    @overload
    def fill(self, value: Dict[str, 'LiteralType']) -> DataFrame: ...
    @overload
    def replace(self, to_replace: List['LiteralType'], value: List['OptionalPrimitiveType'], subset: List[str] | None = ...) -> DataFrame: ...
    @overload
    def replace(self, to_replace: Dict['LiteralType', 'OptionalPrimitiveType'], subset: List[str] | None = ...) -> DataFrame: ...
    @overload
    def replace(self, to_replace: List['LiteralType'], value: OptionalPrimitiveType, subset: List[str] | None = ...) -> DataFrame: ...

class DataFrameStatFunctions:
    """Functionality for statistic functions with :class:`DataFrame`.

    .. versionadded:: 1.4.0

    .. versionchanged:: 3.4.0
        Supports Spark Connect.
    """
    df: Incomplete
    def __init__(self, df: DataFrame) -> None: ...
    @overload
    def approxQuantile(self, col: str, probabilities: List[float] | Tuple[float], relativeError: float) -> List[float]: ...
    @overload
    def approxQuantile(self, col: List[str] | Tuple[str], probabilities: List[float] | Tuple[float], relativeError: float) -> List[List[float]]: ...
    def corr(self, col1: str, col2: str, method: str | None = None) -> float: ...
    def cov(self, col1: str, col2: str) -> float: ...
    def crosstab(self, col1: str, col2: str) -> DataFrame: ...
    def freqItems(self, cols: List[str], support: float | None = None) -> DataFrame: ...
    def sampleBy(self, col: str, fractions: Dict[Any, float], seed: int | None = None) -> DataFrame: ...
