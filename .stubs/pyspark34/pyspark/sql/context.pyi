from _typeshed import Incomplete
from py4j.java_gateway import JavaObject
from pyspark._globals import _NoValueType
from pyspark.context import SparkContext
from pyspark.rdd import RDD
from pyspark.sql._typing import AtomicValue, RowLike, UserDefinedFunctionLike
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.pandas._typing import DataFrameLike as PandasDataFrameLike
from pyspark.sql.readwriter import DataFrameReader
from pyspark.sql.session import SparkSession
from pyspark.sql.streaming import DataStreamReader, StreamingQueryManager
from pyspark.sql.types import AtomicType, DataType, StructType
from pyspark.sql.udf import UDFRegistration
from typing import Any, Callable, Iterable, List, Tuple, overload

__all__ = ['SQLContext', 'HiveContext']

class SQLContext:
    '''The entry point for working with structured data (rows and columns) in Spark, in Spark 1.x.

    As of Spark 2.0, this is replaced by :class:`SparkSession`. However, we are keeping the class
    here for backward compatibility.

    A SQLContext can be used to create :class:`DataFrame`, register :class:`DataFrame` as
    tables, execute SQL over tables, cache tables, and read parquet files.

    .. deprecated:: 3.0.0
        Use :func:`SparkSession.builder.getOrCreate()` instead.

    Parameters
    ----------
    sparkContext : :class:`SparkContext`
        The :class:`SparkContext` backing this SQLContext.
    sparkSession : :class:`SparkSession`
        The :class:`SparkSession` around which this SQLContext wraps.
    jsqlContext : optional
        An optional JVM Scala SQLContext. If set, we do not instantiate a new
        SQLContext in the JVM, instead we make all calls to this object.
        This is only for internal.

    Examples
    --------
    >>> from datetime import datetime
    >>> from pyspark.sql import Row
    >>> sqlContext = SQLContext(sc)
    >>> allTypes = sc.parallelize([Row(i=1, s="string", d=1.0, l=1,
    ...     b=True, list=[1, 2, 3], dict={"s": 0}, row=Row(a=1),
    ...     time=datetime(2014, 8, 1, 14, 1, 5))])
    >>> df = allTypes.toDF()
    >>> df.createOrReplaceTempView("allTypes")
    >>> sqlContext.sql(\'select i+1, d+1, not b, list[1], dict["s"], time, row.a \'
    ...            \'from allTypes where b and i > 0\').collect()
    [Row((i + 1)=2, (d + 1)=2.0, (NOT b)=False, list[1]=2,         dict[s]=0, time=datetime.datetime(2014, 8, 1, 14, 1, 5), a=1)]
    >>> df.rdd.map(lambda x: (x.i, x.s, x.d, x.l, x.b, x.time, x.row.a, x.list)).collect()
    [(1, \'string\', 1.0, 1, True, datetime.datetime(2014, 8, 1, 14, 1, 5), 1, [1, 2, 3])]
    '''
    sparkSession: Incomplete
    def __init__(self, sparkContext: SparkContext, sparkSession: SparkSession | None = None, jsqlContext: JavaObject | None = None) -> None: ...
    @classmethod
    def getOrCreate(cls, sc: SparkContext) -> SQLContext:
        """
        Get the existing SQLContext or create a new one with given SparkContext.

        .. versionadded:: 1.6.0

        .. deprecated:: 3.0.0
            Use :func:`SparkSession.builder.getOrCreate()` instead.

        Parameters
        ----------
        sc : :class:`SparkContext`
        """
    def newSession(self) -> SQLContext:
        """
        Returns a new SQLContext as new session, that has separate SQLConf,
        registered temporary views and UDFs, but shared SparkContext and
        table cache.

        .. versionadded:: 1.6.0
        """
    def setConf(self, key: str, value: bool | int | str) -> None:
        """Sets the given Spark SQL configuration property.

        .. versionadded:: 1.3.0
        """
    def getConf(self, key: str, defaultValue: str | None | _NoValueType = ...) -> str | None:
        '''Returns the value of Spark SQL configuration property for the given key.

        If the key is not set and defaultValue is set, return
        defaultValue. If the key is not set and defaultValue is not set, return
        the system default value.

        .. versionadded:: 1.3.0

        Examples
        --------
        >>> sqlContext.getConf("spark.sql.shuffle.partitions")
        \'200\'
        >>> sqlContext.getConf("spark.sql.shuffle.partitions", "10")
        \'10\'
        >>> sqlContext.setConf("spark.sql.shuffle.partitions", "50")
        >>> sqlContext.getConf("spark.sql.shuffle.partitions", "10")
        \'50\'
        '''
    @property
    def udf(self) -> UDFRegistration:
        """Returns a :class:`UDFRegistration` for UDF registration.

        .. versionadded:: 1.3.1

        Returns
        -------
        :class:`UDFRegistration`
        """
    def range(self, start: int, end: int | None = None, step: int = 1, numPartitions: int | None = None) -> DataFrame:
        """
        Create a :class:`DataFrame` with single :class:`pyspark.sql.types.LongType` column named
        ``id``, containing elements in a range from ``start`` to ``end`` (exclusive) with
        step value ``step``.

        .. versionadded:: 1.4.0

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
        >>> sqlContext.range(1, 7, 2).collect()
        [Row(id=1), Row(id=3), Row(id=5)]

        If only one argument is specified, it will be used as the end value.

        >>> sqlContext.range(3).collect()
        [Row(id=0), Row(id=1), Row(id=2)]
        """
    def registerFunction(self, name: str, f: Callable[..., Any], returnType: DataType | None = None) -> UserDefinedFunctionLike:
        """An alias for :func:`spark.udf.register`.
        See :meth:`pyspark.sql.UDFRegistration.register`.

        .. versionadded:: 1.2.0

        .. deprecated:: 2.3.0
            Use :func:`spark.udf.register` instead.
        """
    def registerJavaFunction(self, name: str, javaClassName: str, returnType: DataType | None = None) -> None:
        """An alias for :func:`spark.udf.registerJavaFunction`.
        See :meth:`pyspark.sql.UDFRegistration.registerJavaFunction`.

        .. versionadded:: 2.1.0

        .. deprecated:: 2.3.0
            Use :func:`spark.udf.registerJavaFunction` instead.
        """
    @overload
    def createDataFrame(self, data: RDD[RowLike] | Iterable['RowLike'], schema: List[str] | Tuple[str, ...] = ..., samplingRatio: float | None = ...) -> DataFrame: ...
    @overload
    def createDataFrame(self, data: RDD[RowLike] | Iterable['RowLike'], schema: StructType | str, *, verifySchema: bool = ...) -> DataFrame: ...
    @overload
    def createDataFrame(self, data: RDD[AtomicValue] | Iterable['AtomicValue'], schema: AtomicType | str, verifySchema: bool = ...) -> DataFrame: ...
    @overload
    def createDataFrame(self, data: PandasDataFrameLike, samplingRatio: float | None = ...) -> DataFrame: ...
    @overload
    def createDataFrame(self, data: PandasDataFrameLike, schema: StructType | str, verifySchema: bool = ...) -> DataFrame: ...
    def registerDataFrameAsTable(self, df: DataFrame, tableName: str) -> None:
        '''Registers the given :class:`DataFrame` as a temporary table in the catalog.

        Temporary tables exist only during the lifetime of this instance of :class:`SQLContext`.

        .. versionadded:: 1.3.0

        Examples
        --------
        >>> sqlContext.registerDataFrameAsTable(df, "table1")
        '''
    def dropTempTable(self, tableName: str) -> None:
        '''Remove the temporary table from catalog.

        .. versionadded:: 1.6.0

        Examples
        --------
        >>> sqlContext.registerDataFrameAsTable(df, "table1")
        >>> sqlContext.dropTempTable("table1")
        '''
    def createExternalTable(self, tableName: str, path: str | None = None, source: str | None = None, schema: StructType | None = None, **options: str) -> DataFrame:
        """Creates an external table based on the dataset in a data source.

        It returns the DataFrame associated with the external table.

        The data source is specified by the ``source`` and a set of ``options``.
        If ``source`` is not specified, the default data source configured by
        ``spark.sql.sources.default`` will be used.

        Optionally, a schema can be provided as the schema of the returned :class:`DataFrame` and
        created external table.

        .. versionadded:: 1.3.0

        Returns
        -------
        :class:`DataFrame`
        """
    def sql(self, sqlQuery: str) -> DataFrame:
        '''Returns a :class:`DataFrame` representing the result of the given query.

        .. versionadded:: 1.0.0

        Returns
        -------
        :class:`DataFrame`

        Examples
        --------
        >>> sqlContext.registerDataFrameAsTable(df, "table1")
        >>> df2 = sqlContext.sql("SELECT field1 AS f1, field2 as f2 from table1")
        >>> df2.collect()
        [Row(f1=1, f2=\'row1\'), Row(f1=2, f2=\'row2\'), Row(f1=3, f2=\'row3\')]
        '''
    def table(self, tableName: str) -> DataFrame:
        '''Returns the specified table or view as a :class:`DataFrame`.

        .. versionadded:: 1.0.0

        Returns
        -------
        :class:`DataFrame`

        Examples
        --------
        >>> sqlContext.registerDataFrameAsTable(df, "table1")
        >>> df2 = sqlContext.table("table1")
        >>> sorted(df.collect()) == sorted(df2.collect())
        True
        '''
    def tables(self, dbName: str | None = None) -> DataFrame:
        '''Returns a :class:`DataFrame` containing names of tables in the given database.

        If ``dbName`` is not specified, the current database will be used.

        The returned DataFrame has two columns: ``tableName`` and ``isTemporary``
        (a column with :class:`BooleanType` indicating if a table is a temporary one or not).

        .. versionadded:: 1.3.0

        Parameters
        ----------
        dbName: str, optional
            name of the database to use.

        Returns
        -------
        :class:`DataFrame`

        Examples
        --------
        >>> sqlContext.registerDataFrameAsTable(df, "table1")
        >>> df2 = sqlContext.tables()
        >>> df2.filter("tableName = \'table1\'").first()
        Row(namespace=\'\', tableName=\'table1\', isTemporary=True)
        '''
    def tableNames(self, dbName: str | None = None) -> List[str]:
        '''Returns a list of names of tables in the database ``dbName``.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        dbName: str
            name of the database to use. Default to the current database.

        Returns
        -------
        list
            list of table names, in string

        >>> sqlContext.registerDataFrameAsTable(df, "table1")
        >>> "table1" in sqlContext.tableNames()
        True
        >>> "table1" in sqlContext.tableNames("default")
        True
        '''
    def cacheTable(self, tableName: str) -> None:
        """Caches the specified table in-memory."""
    def uncacheTable(self, tableName: str) -> None:
        """Removes the specified table from the in-memory cache."""
    def clearCache(self) -> None:
        """Removes all cached tables from the in-memory cache."""
    @property
    def read(self) -> DataFrameReader:
        """
        Returns a :class:`DataFrameReader` that can be used to read data
        in as a :class:`DataFrame`.

        .. versionadded:: 1.4.0

        Returns
        -------
        :class:`DataFrameReader`
        """
    @property
    def readStream(self) -> DataStreamReader:
        """
        Returns a :class:`DataStreamReader` that can be used to read data streams
        as a streaming :class:`DataFrame`.

        .. versionadded:: 2.0.0

        Notes
        -----
        This API is evolving.

        Returns
        -------
        :class:`DataStreamReader`

        >>> text_sdf = sqlContext.readStream.text(tempfile.mkdtemp())
        >>> text_sdf.isStreaming
        True
        """
    @property
    def streams(self) -> StreamingQueryManager:
        """Returns a :class:`StreamingQueryManager` that allows managing all the
        :class:`StreamingQuery` StreamingQueries active on `this` context.

        .. versionadded:: 2.0.0

        Notes
        -----
        This API is evolving.
        """

class HiveContext(SQLContext):
    """A variant of Spark SQL that integrates with data stored in Hive.

    Configuration for Hive is read from ``hive-site.xml`` on the classpath.
    It supports running both SQL and HiveQL commands.

    .. deprecated:: 2.0.0
        Use SparkSession.builder.enableHiveSupport().getOrCreate().

    Parameters
    ----------
    sparkContext : :class:`SparkContext`
        The SparkContext to wrap.
    jhiveContext : optional
        An optional JVM Scala HiveContext. If set, we do not instantiate a new
        :class:`HiveContext` in the JVM, instead we make all calls to this object.
        This is only for internal use.

    """
    def __init__(self, sparkContext: SparkContext, sparkSession: SparkSession | None = None, jhiveContext: JavaObject | None = None) -> None: ...
    def refreshTable(self, tableName: str) -> None:
        """Invalidate and refresh all the cached metadata of the given
        table. For performance reasons, Spark SQL or the external data source
        library it uses might cache certain metadata about a table, such as the
        location of blocks. When those change outside of Spark SQL, users should
        call this function to invalidate the cache.
        """
