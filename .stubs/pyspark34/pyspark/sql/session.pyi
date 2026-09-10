from py4j.java_gateway import JavaObject
from pyspark import SparkConf, SparkContext
from pyspark.rdd import RDD
from pyspark.sql._typing import AtomicValue, OptionalPrimitiveType, RowLike
from pyspark.sql.catalog import Catalog
from pyspark.sql.conf import RuntimeConfig
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.pandas._typing import DataFrameLike as PandasDataFrameLike
from pyspark.sql.pandas.conversion import SparkConversionMixin
from pyspark.sql.readwriter import DataFrameReader
from pyspark.sql.streaming import DataStreamReader, StreamingQueryManager
from pyspark.sql.types import AtomicType, StructType
from pyspark.sql.udf import UDFRegistration
from types import TracebackType
from typing import Any, Dict, Iterable, List, Tuple, Type, overload

__all__ = ['SparkSession']

class classproperty(property):
    '''Same as Python\'s @property decorator, but for class attributes.

    Examples
    --------
    >>> class Builder:
    ...    def build(self):
    ...        return MyClass()
    ...
    >>> class MyClass:
    ...     @classproperty
    ...     def builder(cls):
    ...         print("instantiating new builder")
    ...         return Builder()
    ...
    >>> c1 = MyClass.builder
    instantiating new builder
    >>> c2 = MyClass.builder
    instantiating new builder
    >>> c1 == c2
    False
    >>> isinstance(c1.build(), MyClass)
    True
    '''
    def __get__(self, instance: Any, owner: Any = None) -> SparkSession.Builder: ...

class SparkSession(SparkConversionMixin):
    '''The entry point to programming Spark with the Dataset and DataFrame API.

    A SparkSession can be used to create :class:`DataFrame`, register :class:`DataFrame` as
    tables, execute SQL over tables, cache tables, and read parquet files.
    To create a :class:`SparkSession`, use the following builder pattern:

    .. versionchanged:: 3.4.0
        Supports Spark Connect.

    .. autoattribute:: builder
       :annotation:

    Examples
    --------
    Create a Spark session.

    >>> spark = (
    ...     SparkSession.builder
    ...         .master("local")
    ...         .appName("Word Count")
    ...         .config("spark.some.config.option", "some-value")
    ...         .getOrCreate()
    ... )

    Create a Spark session with Spark Connect.

    >>> spark = (
    ...     SparkSession.builder
    ...         .remote("sc://localhost")
    ...         .appName("Word Count")
    ...         .config("spark.some.config.option", "some-value")
    ...         .getOrCreate()
    ... )  # doctest: +SKIP
    '''
    class Builder:
        """Builder for :class:`SparkSession`."""
        def __init__(self) -> None: ...
        @overload
        def config(self, *, conf: SparkConf) -> SparkSession.Builder: ...
        @overload
        def config(self, key: str, value: Any) -> SparkSession.Builder: ...
        @overload
        def config(self, *, map: Dict[str, 'OptionalPrimitiveType']) -> SparkSession.Builder: ...
        def master(self, master: str) -> SparkSession.Builder:
            '''Sets the Spark master URL to connect to, such as "local" to run locally, "local[4]"
            to run locally with 4 cores, or "spark://master:7077" to run on a Spark standalone
            cluster.

            .. versionadded:: 2.0.0

            Parameters
            ----------
            master : str
                a url for spark master

            Returns
            -------
            :class:`SparkSession.Builder`

            Examples
            --------
            >>> SparkSession.builder.master("local")
            <pyspark.sql.session.SparkSession.Builder...
            '''
        def remote(self, url: str) -> SparkSession.Builder:
            '''Sets the Spark remote URL to connect to, such as "sc://host:port" to run
            it via Spark Connect server.

            .. versionadded:: 3.4.0

            Parameters
            ----------
            url : str
                URL to Spark Connect server

            Returns
            -------
            :class:`SparkSession.Builder`

            Examples
            --------
            >>> SparkSession.builder.remote("sc://localhost")  # doctest: +SKIP
            <pyspark.sql.session.SparkSession.Builder...
            '''
        def appName(self, name: str) -> SparkSession.Builder:
            '''Sets a name for the application, which will be shown in the Spark web UI.

            If no application name is set, a randomly generated name will be used.

            .. versionadded:: 2.0.0

            .. versionchanged:: 3.4.0
                Supports Spark Connect.

            Parameters
            ----------
            name : str
                an application name

            Returns
            -------
            :class:`SparkSession.Builder`

            Examples
            --------
            >>> SparkSession.builder.appName("My app")
            <pyspark.sql.session.SparkSession.Builder...
            '''
        def enableHiveSupport(self) -> SparkSession.Builder:
            """Enables Hive support, including connectivity to a persistent Hive metastore, support
            for Hive SerDes, and Hive user-defined functions.

            .. versionadded:: 2.0.0

            Returns
            -------
            :class:`SparkSession.Builder`

            Examples
            --------
            >>> SparkSession.builder.enableHiveSupport()
            <pyspark.sql.session.SparkSession.Builder...
            """
        def getOrCreate(self) -> SparkSession:
            '''Gets an existing :class:`SparkSession` or, if there is no existing one, creates a
            new one based on the options set in this builder.

            .. versionadded:: 2.0.0

            .. versionchanged:: 3.4.0
                Supports Spark Connect.

            Returns
            -------
            :class:`SparkSession`

            Examples
            --------
            This method first checks whether there is a valid global default SparkSession, and if
            yes, return that one. If no valid global default SparkSession exists, the method
            creates a new SparkSession and assigns the newly created SparkSession as the global
            default.

            >>> s1 = SparkSession.builder.config("k1", "v1").getOrCreate()
            >>> s1.conf.get("k1") == "v1"
            True

            The configuration of the SparkSession can be changed afterwards

            >>> s1.conf.set("k1", "v1_new")
            >>> s1.conf.get("k1") == "v1_new"
            True

            In case an existing SparkSession is returned, the config options specified
            in this builder will be applied to the existing SparkSession.

            >>> s2 = SparkSession.builder.config("k2", "v2").getOrCreate()
            >>> s1.conf.get("k1") == s2.conf.get("k1") == "v1_new"
            True
            >>> s1.conf.get("k2") == s2.conf.get("k2") == "v2"
            True
            '''
    def builder(cls) -> Builder:
        """Creates a :class:`Builder` for constructing a :class:`SparkSession`."""
    def __init__(self, sparkContext: SparkContext, jsparkSession: JavaObject | None = None, options: Dict[str, Any] = {}) -> None: ...
    def newSession(self) -> SparkSession:
        """
        Returns a new :class:`SparkSession` as new session, that has separate SQLConf,
        registered temporary views and UDFs, but shared :class:`SparkContext` and
        table cache.

        .. versionadded:: 2.0.0

        Returns
        -------
        :class:`SparkSession`
            Spark session if an active session exists for the current thread

        Examples
        --------
        >>> spark.newSession()
        <...SparkSession object ...>
        """
    @classmethod
    def getActiveSession(cls) -> SparkSession | None:
        '''
        Returns the active :class:`SparkSession` for the current thread, returned by the builder

        .. versionadded:: 3.0.0

        Returns
        -------
        :class:`SparkSession`
            Spark session if an active session exists for the current thread

        Examples
        --------
        >>> s = SparkSession.getActiveSession()
        >>> df = s.createDataFrame([(\'Alice\', 1)], [\'name\', \'age\'])
        >>> df.select("age").show()
        +---+
        |age|
        +---+
        |  1|
        +---+
        '''
    @property
    def sparkContext(self) -> SparkContext:
        """
        Returns the underlying :class:`SparkContext`.

        .. versionadded:: 2.0.0

        Returns
        -------
        :class:`SparkContext`

        Examples
        --------
        >>> spark.sparkContext
        <SparkContext master=... appName=...>

        Create an RDD from the Spark context

        >>> rdd = spark.sparkContext.parallelize([1, 2, 3])
        >>> rdd.collect()
        [1, 2, 3]
        """
    @property
    def version(self) -> str:
        """
        The version of Spark on which this application is running.

        .. versionadded:: 2.0.0

        Returns
        -------
        str
            the version of Spark in string.

        Examples
        --------
        >>> _ = spark.version
        """
    @property
    def conf(self) -> RuntimeConfig:
        '''Runtime configuration interface for Spark.

        This is the interface through which the user can get and set all Spark and Hadoop
        configurations that are relevant to Spark SQL. When getting the value of a config,
        this defaults to the value set in the underlying :class:`SparkContext`, if any.

        .. versionadded:: 2.0.0

        Returns
        -------
        :class:`pyspark.sql.conf.RuntimeConfig`

        Examples
        --------
        >>> spark.conf
        <pyspark.sql.conf.RuntimeConfig object ...>

        Set a runtime configuration for the session

        >>> spark.conf.set("key", "value")
        >>> spark.conf.get("key")
        \'value\'
        '''
    @property
    def catalog(self) -> Catalog:
        '''Interface through which the user may create, drop, alter or query underlying
        databases, tables, functions, etc.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        :class:`Catalog`

        Examples
        --------
        >>> spark.catalog
        <...Catalog object ...>

        Create a temp view, show the list, and drop it.

        >>> spark.range(1).createTempView("test_view")
        >>> spark.catalog.listTables()
        [Table(name=\'test_view\', catalog=None, namespace=[], description=None, ...
        >>> _ = spark.catalog.dropTempView("test_view")
        '''
    @property
    def udf(self) -> UDFRegistration:
        '''Returns a :class:`UDFRegistration` for UDF registration.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        :class:`UDFRegistration`

        Examples
        --------
        Register a Python UDF, and use it in SQL.

        >>> strlen = spark.udf.register("strlen", lambda x: len(x))
        >>> spark.sql("SELECT strlen(\'test\')").show()
        +------------+
        |strlen(test)|
        +------------+
        |           4|
        +------------+
        '''
    def range(self, start: int, end: int | None = None, step: int = 1, numPartitions: int | None = None) -> DataFrame:
        """
        Create a :class:`DataFrame` with single :class:`pyspark.sql.types.LongType` column named
        ``id``, containing elements in a range from ``start`` to ``end`` (exclusive) with
        step value ``step``.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        start : int
            the start value
        end : int, optional
            the end value (exclusive)
        step : int, optional
            the incremental step (default: 1)
        numPartitions : int, optional
            the number of partitions of the DataFrame

        Returns
        -------
        :class:`DataFrame`

        Examples
        --------
        >>> spark.range(1, 7, 2).show()
        +---+
        | id|
        +---+
        |  1|
        |  3|
        |  5|
        +---+

        If only one argument is specified, it will be used as the end value.

        >>> spark.range(3).show()
        +---+
        | id|
        +---+
        |  0|
        |  1|
        |  2|
        +---+
        """
    @overload
    def createDataFrame(self, data: Iterable['RowLike'], schema: List[str] | Tuple[str, ...] = ..., samplingRatio: float | None = ...) -> DataFrame: ...
    @overload
    def createDataFrame(self, data: RDD[RowLike], schema: List[str] | Tuple[str, ...] = ..., samplingRatio: float | None = ...) -> DataFrame: ...
    @overload
    def createDataFrame(self, data: Iterable['RowLike'], schema: StructType | str, *, verifySchema: bool = ...) -> DataFrame: ...
    @overload
    def createDataFrame(self, data: RDD[RowLike], schema: StructType | str, *, verifySchema: bool = ...) -> DataFrame: ...
    @overload
    def createDataFrame(self, data: RDD[AtomicValue], schema: AtomicType | str, verifySchema: bool = ...) -> DataFrame: ...
    @overload
    def createDataFrame(self, data: Iterable['AtomicValue'], schema: AtomicType | str, verifySchema: bool = ...) -> DataFrame: ...
    @overload
    def createDataFrame(self, data: PandasDataFrameLike, samplingRatio: float | None = ...) -> DataFrame: ...
    @overload
    def createDataFrame(self, data: PandasDataFrameLike, schema: StructType | str, verifySchema: bool = ...) -> DataFrame: ...
    def sql(self, sqlQuery: str, args: Dict[str, Any] | None = None, **kwargs: Any) -> DataFrame:
        '''Returns a :class:`DataFrame` representing the result of the given query.
        When ``kwargs`` is specified, this method formats the given string by using the Python
        standard formatter. The method binds named parameters to SQL literals from `args`.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect and parameterized SQL.

        Parameters
        ----------
        sqlQuery : str
            SQL query string.
        args : dict
            A dictionary of parameter names to Python objects that can be converted to
            SQL literal expressions. See
            <a href="https://spark.apache.org/docs/latest/sql-ref-datatypes.html">
            Supported Data Types</a> for supported value types in Python.
            For example, dictionary keys: "rank", "name", "birthdate";
            dictionary values: 1, "Steven", datetime.date(2023, 4, 2).
            Map value can be also a `Column` of literal expression, in that case it is taken as is.

            .. versionadded:: 3.4.0

        kwargs : dict
            Other variables that the user wants to set that can be referenced in the query

            .. versionchanged:: 3.3.0
               Added optional argument ``kwargs`` to specify the mapping of variables in the query.
               This feature is experimental and unstable.

        Returns
        -------
        :class:`DataFrame`

        Examples
        --------
        Executing a SQL query.

        >>> spark.sql("SELECT * FROM range(10) where id > 7").show()
        +---+
        | id|
        +---+
        |  8|
        |  9|
        +---+

        Executing a SQL query with variables as Python formatter standard.

        >>> spark.sql(
        ...     "SELECT * FROM range(10) WHERE id > {bound1} AND id < {bound2}", bound1=7, bound2=9
        ... ).show()
        +---+
        | id|
        +---+
        |  8|
        +---+

        >>> mydf = spark.range(10)
        >>> spark.sql(
        ...     "SELECT {col} FROM {mydf} WHERE id IN {x}",
        ...     col=mydf.id, mydf=mydf, x=tuple(range(4))).show()
        +---+
        | id|
        +---+
        |  0|
        |  1|
        |  2|
        |  3|
        +---+

        >>> spark.sql(\'\'\'
        ...   SELECT m1.a, m2.b
        ...   FROM {table1} m1 INNER JOIN {table2} m2
        ...   ON m1.key = m2.key
        ...   ORDER BY m1.a, m2.b\'\'\',
        ...   table1=spark.createDataFrame([(1, "a"), (2, "b")], ["a", "key"]),
        ...   table2=spark.createDataFrame([(3, "a"), (4, "b"), (5, "b")], ["b", "key"])).show()
        +---+---+
        |  a|  b|
        +---+---+
        |  1|  3|
        |  2|  4|
        |  2|  5|
        +---+---+

        Also, it is possible to query using class:`Column` from :class:`DataFrame`.

        >>> mydf = spark.createDataFrame([(1, 4), (2, 4), (3, 6)], ["A", "B"])
        >>> spark.sql("SELECT {df.A}, {df[B]} FROM {df}", df=mydf).show()
        +---+---+
        |  A|  B|
        +---+---+
        |  1|  4|
        |  2|  4|
        |  3|  6|
        +---+---+

        And substitude named parameters with the `:` prefix by SQL literals.

        >>> spark.sql("SELECT * FROM {df} WHERE {df[B]} > :minB", {"minB" : 5}, df=mydf).show()
        +---+---+
        |  A|  B|
        +---+---+
        |  3|  6|
        +---+---+
        '''
    def table(self, tableName: str) -> DataFrame:
        '''Returns the specified table as a :class:`DataFrame`.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        tableName : str
            the table name to retrieve.

        Returns
        -------
        :class:`DataFrame`

        Examples
        --------
        >>> spark.range(5).createOrReplaceTempView("table1")
        >>> spark.table("table1").sort("id").show()
        +---+
        | id|
        +---+
        |  0|
        |  1|
        |  2|
        |  3|
        |  4|
        +---+
        '''
    @property
    def read(self) -> DataFrameReader:
        '''
        Returns a :class:`DataFrameReader` that can be used to read data
        in as a :class:`DataFrame`.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Returns
        -------
        :class:`DataFrameReader`

        Examples
        --------
        >>> spark.read
        <...DataFrameReader object ...>

        Write a DataFrame into a JSON file and read it back.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a JSON file
        ...     spark.createDataFrame(
        ...         [{"age": 100, "name": "Hyukjin Kwon"}]
        ...     ).write.mode("overwrite").format("json").save(d)
        ...
        ...     # Read the JSON file as a DataFrame.
        ...     spark.read.format(\'json\').load(d).show()
        +---+------------+
        |age|        name|
        +---+------------+
        |100|Hyukjin Kwon|
        +---+------------+
        '''
    @property
    def readStream(self) -> DataStreamReader:
        '''
        Returns a :class:`DataStreamReader` that can be used to read data streams
        as a streaming :class:`DataFrame`.

        .. versionadded:: 2.0.0

        Notes
        -----
        This API is evolving.

        Returns
        -------
        :class:`DataStreamReader`

        Examples
        --------
        >>> spark.readStream
        <pyspark.sql.streaming.readwriter.DataStreamReader object ...>

        The example below uses Rate source that generates rows continuously.
        After that, we operate a modulo by 3, and then write the stream out to the console.
        The streaming query stops in 3 seconds.

        >>> import time
        >>> df = spark.readStream.format("rate").load()
        >>> df = df.selectExpr("value % 3 as v")
        >>> q = df.writeStream.format("console").start()
        >>> time.sleep(3)
        >>> q.stop()
        '''
    @property
    def streams(self) -> StreamingQueryManager:
        '''Returns a :class:`StreamingQueryManager` that allows managing all the
        :class:`StreamingQuery` instances active on `this` context.

        .. versionadded:: 2.0.0

        Notes
        -----
        This API is evolving.

        Returns
        -------
        :class:`StreamingQueryManager`

        Examples
        --------
        >>> spark.streams
        <pyspark.sql.streaming.query.StreamingQueryManager object ...>

        Get the list of active streaming queries

        >>> sq = spark.readStream.format(
        ...     "rate").load().writeStream.format(\'memory\').queryName(\'this_query\').start()
        >>> sqm = spark.streams
        >>> [q.name for q in sqm.active]
        [\'this_query\']
        >>> sq.stop()
        '''
    def stop(self) -> None:
        """
        Stop the underlying :class:`SparkContext`.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Examples
        --------
        >>> spark.stop()  # doctest: +SKIP
        """
    def __enter__(self) -> SparkSession:
        '''
        Enable \'with SparkSession.builder.(...).getOrCreate() as session: app\' syntax.

        .. versionadded:: 2.0.0

        Examples
        --------
        >>> with SparkSession.builder.master("local").getOrCreate() as session:
        ...     session.range(5).show()  # doctest: +SKIP
        +---+
        | id|
        +---+
        |  0|
        |  1|
        |  2|
        |  3|
        |  4|
        +---+
        '''
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None:
        '''
        Enable \'with SparkSession.builder.(...).getOrCreate() as session: app\' syntax.

        Specifically stop the SparkSession on exit of the with block.

        .. versionadded:: 2.0.0

        Examples
        --------
        >>> with SparkSession.builder.master("local").getOrCreate() as session:
        ...     session.range(5).show()  # doctest: +SKIP
        +---+
        | id|
        +---+
        |  0|
        |  1|
        |  2|
        |  3|
        |  4|
        +---+
        '''
