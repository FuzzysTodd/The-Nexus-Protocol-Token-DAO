from pyspark.sql._typing import UserDefinedFunctionLike as UserDefinedFunctionLike
from pyspark.sql.dataframe import DataFrame as DataFrame
from pyspark.sql.session import SparkSession as SparkSession
from pyspark.sql.types import DataType as DataType, StructType as StructType
from typing import Any, Callable, List, NamedTuple

class CatalogMetadata(NamedTuple):
    name: str
    description: str | None

class Database(NamedTuple):
    name: str
    catalog: str | None
    description: str | None
    locationUri: str

class Table(NamedTuple):
    name: str
    catalog: str | None
    namespace: List[str] | None
    description: str | None
    tableType: str
    isTemporary: bool
    @property
    def database(self) -> str | None: ...

class Column(NamedTuple):
    name: str
    description: str | None
    dataType: str
    nullable: bool
    isPartition: bool
    isBucket: bool

class Function(NamedTuple):
    name: str
    catalog: str | None
    namespace: List[str] | None
    description: str | None
    className: str
    isTemporary: bool

class Catalog:
    """User-facing catalog API, accessible through `SparkSession.catalog`.

    This is a thin wrapper around its Scala implementation org.apache.spark.sql.catalog.Catalog.

    .. versionchanged:: 3.4.0
        Supports Spark Connect.
    """
    def __init__(self, sparkSession: SparkSession) -> None:
        """Create a new Catalog that wraps the underlying JVM object."""
    def currentCatalog(self) -> str:
        """Returns the current default catalog in this session.

        .. versionadded:: 3.4.0

        Examples
        --------
        >>> spark.catalog.currentCatalog()
        'spark_catalog'
        """
    def setCurrentCatalog(self, catalogName: str) -> None:
        '''Sets the current default catalog in this session.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        catalogName : str
            name of the catalog to set

        Examples
        --------
        >>> spark.catalog.setCurrentCatalog("spark_catalog")
        '''
    def listCatalogs(self) -> List[CatalogMetadata]:
        """Returns a list of catalogs in this session.

        .. versionadded:: 3.4.0

        Returns
        -------
        list
            A list of :class:`CatalogMetadata`.

        Examples
        --------
        >>> spark.catalog.listCatalogs()
        [CatalogMetadata(name='spark_catalog', description=None)]
        """
    def currentDatabase(self) -> str:
        """
        Returns the current default database in this session.

        .. versionadded:: 2.0.0

        Returns
        -------
        str
            The current default database name.

        Examples
        --------
        >>> spark.catalog.currentDatabase()
        'default'
        """
    def setCurrentDatabase(self, dbName: str) -> None:
        '''
        Sets the current default database in this session.

        .. versionadded:: 2.0.0

        Examples
        --------
        >>> spark.catalog.setCurrentDatabase("default")
        '''
    def listDatabases(self) -> List[Database]:
        """
        Returns a list of databases available across all sessions.

        .. versionadded:: 2.0.0

        Returns
        -------
        list
            A list of :class:`Database`.

        Examples
        --------
        >>> spark.catalog.listDatabases()
        [Database(name='default', catalog='spark_catalog', description='default database', ...
        """
    def getDatabase(self, dbName: str) -> Database:
        '''Get the database with the specified name.
        This throws an :class:`AnalysisException` when the database cannot be found.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        dbName : str
             name of the database to get.

        Returns
        -------
        :class:`Database`
            The database found by the name.

        Examples
        --------
        >>> spark.catalog.getDatabase("default")
        Database(name=\'default\', catalog=\'spark_catalog\', description=\'default database\', ...

        Using the fully qualified name with the catalog name.

        >>> spark.catalog.getDatabase("spark_catalog.default")
        Database(name=\'default\', catalog=\'spark_catalog\', description=\'default database\', ...
        '''
    def databaseExists(self, dbName: str) -> bool:
        '''Check if the database with the specified name exists.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        dbName : str
            name of the database to check existence

            .. versionchanged:: 3.4.0
               Allow ``dbName`` to be qualified with catalog name.

        Returns
        -------
        bool
            Indicating whether the database exists

        Examples
        --------
        Check if \'test_new_database\' database exists

        >>> spark.catalog.databaseExists("test_new_database")
        False
        >>> _ = spark.sql("CREATE DATABASE test_new_database")
        >>> spark.catalog.databaseExists("test_new_database")
        True

        Using the fully qualified name with the catalog name.

        >>> spark.catalog.databaseExists("spark_catalog.test_new_database")
        True
        >>> _ = spark.sql("DROP DATABASE test_new_database")
        '''
    def listTables(self, dbName: str | None = None) -> List[Table]:
        '''Returns a list of tables/views in the specified database.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        dbName : str
            name of the database to list the tables.

            .. versionchanged:: 3.4.0
               Allow ``dbName`` to be qualified with catalog name.

        Returns
        -------
        list
            A list of :class:`Table`.

        Notes
        -----
        If no database is specified, the current database and catalog
        are used. This API includes all temporary views.

        Examples
        --------
        >>> spark.range(1).createTempView("test_view")
        >>> spark.catalog.listTables()
        [Table(name=\'test_view\', catalog=None, namespace=[], description=None, ...

        >>> _ = spark.catalog.dropTempView("test_view")
        >>> spark.catalog.listTables()
        []
        '''
    def getTable(self, tableName: str) -> Table:
        '''Get the table or view with the specified name. This table can be a temporary view or a
        table/view. This throws an :class:`AnalysisException` when no Table can be found.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        tableName : str
            name of the table to get.

            .. versionchanged:: 3.4.0
               Allow `tableName` to be qualified with catalog name.

        Returns
        -------
        :class:`Table`
            The table found by the name.

        Examples
        --------
        >>> _ = spark.sql("DROP TABLE IF EXISTS tbl1")
        >>> _ = spark.sql("CREATE TABLE tbl1 (name STRING, age INT) USING parquet")
        >>> spark.catalog.getTable("tbl1")
        Table(name=\'tbl1\', catalog=\'spark_catalog\', namespace=[\'default\'], ...

        Using the fully qualified name with the catalog name.

        >>> spark.catalog.getTable("default.tbl1")
        Table(name=\'tbl1\', catalog=\'spark_catalog\', namespace=[\'default\'], ...
        >>> spark.catalog.getTable("spark_catalog.default.tbl1")
        Table(name=\'tbl1\', catalog=\'spark_catalog\', namespace=[\'default\'], ...
        >>> _ = spark.sql("DROP TABLE tbl1")

        Throw an analysis exception when the table does not exist.

        >>> spark.catalog.getTable("tbl1")
        Traceback (most recent call last):
            ...
        AnalysisException: ...
        '''
    def listFunctions(self, dbName: str | None = None) -> List[Function]:
        """
        Returns a list of functions registered in the specified database.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        dbName : str
            name of the database to list the functions.
            ``dbName`` can be qualified with catalog name.

        Returns
        -------
        list
            A list of :class:`Function`.

        Notes
        -----
        If no database is specified, the current database and catalog
        are used. This API includes all temporary functions.

        Examples
        --------
        >>> spark.catalog.listFunctions()
        [Function(name=...
        """
    def functionExists(self, functionName: str, dbName: str | None = None) -> bool:
        '''Check if the function with the specified name exists.
        This can either be a temporary function or a function.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        functionName : str
            name of the function to check existence

            .. versionchanged:: 3.4.0
               Allow ``functionName`` to be qualified with catalog name

        dbName : str, optional
            name of the database to check function existence in.

        Returns
        -------
        bool
            Indicating whether the function exists

        Notes
        -----
        If no database is specified, the current database and catalog
        are used. This API includes all temporary functions.

        Examples
        --------
        >>> spark.catalog.functionExists("count")
        True

        Using the fully qualified name for function name.

        >>> spark.catalog.functionExists("default.unexisting_function")
        False
        >>> spark.catalog.functionExists("spark_catalog.default.unexisting_function")
        False
        '''
    def getFunction(self, functionName: str) -> Function:
        '''Get the function with the specified name. This function can be a temporary function or a
        function. This throws an :class:`AnalysisException` when the function cannot be found.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        functionName : str
            name of the function to check existence.

        Returns
        -------
        :class:`Function`
            The function found by the name.

        Examples
        --------
        >>> _ = spark.sql(
        ...     "CREATE FUNCTION my_func1 AS \'test.org.apache.spark.sql.MyDoubleAvg\'")
        >>> spark.catalog.getFunction("my_func1")
        Function(name=\'my_func1\', catalog=\'spark_catalog\', namespace=[\'default\'], ...

        Using the fully qualified name for function name.

        >>> spark.catalog.getFunction("default.my_func1")
        Function(name=\'my_func1\', catalog=\'spark_catalog\', namespace=[\'default\'], ...
        >>> spark.catalog.getFunction("spark_catalog.default.my_func1")
        Function(name=\'my_func1\', catalog=\'spark_catalog\', namespace=[\'default\'], ...

        Throw an analysis exception when the function does not exists.

        >>> spark.catalog.getFunction("my_func2")
        Traceback (most recent call last):
            ...
        AnalysisException: ...
        '''
    def listColumns(self, tableName: str, dbName: str | None = None) -> List[Column]:
        '''Returns a list of columns for the given table/view in the specified database.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        tableName : str
            name of the table to list columns.

            .. versionchanged:: 3.4.0
               Allow ``tableName`` to be qualified with catalog name when ``dbName`` is None.

        dbName : str, optional
            name of the database to find the table to list columns.

        Returns
        -------
        list
            A list of :class:`Column`.

        Notes
        -----
        The order of arguments here is different from that of its JVM counterpart
        because Python does not support method overloading.

        If no database is specified, the current database and catalog
        are used. This API includes all temporary views.

        Examples
        --------
        >>> _ = spark.sql("DROP TABLE IF EXISTS tbl1")
        >>> _ = spark.sql("CREATE TABLE tblA (name STRING, age INT) USING parquet")
        >>> spark.catalog.listColumns("tblA")
        [Column(name=\'name\', description=None, dataType=\'string\', nullable=True, ...
        >>> _ = spark.sql("DROP TABLE tblA")
        '''
    def tableExists(self, tableName: str, dbName: str | None = None) -> bool:
        '''Check if the table or view with the specified name exists.
        This can either be a temporary view or a table/view.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        tableName : str
            name of the table to check existence.
            If no database is specified, first try to treat ``tableName`` as a
            multi-layer-namespace identifier, then try ``tableName`` as a normal table
            name in the current database if necessary.

            .. versionchanged:: 3.4.0
               Allow ``tableName`` to be qualified with catalog name when ``dbName`` is None.

        dbName : str, optional
            name of the database to check table existence in.

        Returns
        -------
        bool
            Indicating whether the table/view exists

        Examples
        --------
        This function can check if a table is defined or not:

        >>> spark.catalog.tableExists("unexisting_table")
        False
        >>> _ = spark.sql("DROP TABLE IF EXISTS tbl1")
        >>> _ = spark.sql("CREATE TABLE tbl1 (name STRING, age INT) USING parquet")
        >>> spark.catalog.tableExists("tbl1")
        True

        Using the fully qualified names for tables.

        >>> spark.catalog.tableExists("default.tbl1")
        True
        >>> spark.catalog.tableExists("spark_catalog.default.tbl1")
        True
        >>> spark.catalog.tableExists("tbl1", "default")
        True
        >>> _ = spark.sql("DROP TABLE tbl1")

        Check if views exist:

        >>> spark.catalog.tableExists("view1")
        False
        >>> _ = spark.sql("CREATE VIEW view1 AS SELECT 1")
        >>> spark.catalog.tableExists("view1")
        True

        Using the fully qualified names for views.

        >>> spark.catalog.tableExists("default.view1")
        True
        >>> spark.catalog.tableExists("spark_catalog.default.view1")
        True
        >>> spark.catalog.tableExists("view1", "default")
        True
        >>> _ = spark.sql("DROP VIEW view1")

        Check if temporary views exist:

        >>> _ = spark.sql("CREATE TEMPORARY VIEW view1 AS SELECT 1")
        >>> spark.catalog.tableExists("view1")
        True
        >>> df = spark.sql("DROP VIEW view1")
        >>> spark.catalog.tableExists("view1")
        False
        '''
    def createExternalTable(self, tableName: str, path: str | None = None, source: str | None = None, schema: StructType | None = None, **options: str) -> DataFrame:
        """Creates a table based on the dataset in a data source.

        It returns the DataFrame associated with the external table.

        The data source is specified by the ``source`` and a set of ``options``.
        If ``source`` is not specified, the default data source configured by
        ``spark.sql.sources.default`` will be used.

        Optionally, a schema can be provided as the schema of the returned :class:`DataFrame` and
        created external table.

        .. versionadded:: 2.0.0

        Returns
        -------
        :class:`DataFrame`
        """
    def createTable(self, tableName: str, path: str | None = None, source: str | None = None, schema: StructType | None = None, description: str | None = None, **options: str) -> DataFrame:
        '''Creates a table based on the dataset in a data source.

        .. versionadded:: 2.2.0

        Parameters
        ----------
        tableName : str
            name of the table to create.

            .. versionchanged:: 3.4.0
               Allow ``tableName`` to be qualified with catalog name.

        path : str, optional
            the path in which the data for this table exists.
            When ``path`` is specified, an external table is
            created from the data at the given path. Otherwise a managed table is created.
        source : str, optional
            the source of this table such as \'parquet, \'orc\', etc.
            If ``source`` is not specified, the default data source configured by
            ``spark.sql.sources.default`` will be used.
        schema : class:`StructType`, optional
            the schema for this table.
        description : str, optional
            the description of this table.

            .. versionchanged:: 3.1.0
                Added the ``description`` parameter.

        **options : dict, optional
            extra options to specify in the table.

        Returns
        -------
        :class:`DataFrame`
            The DataFrame associated with the table.

        Examples
        --------
        Creating a managed table.

        >>> _ = spark.catalog.createTable("tbl1", schema=spark.range(1).schema, source=\'parquet\')
        >>> _ = spark.sql("DROP TABLE tbl1")

        Creating an external table

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     _ = spark.catalog.createTable(
        ...         "tbl2", schema=spark.range(1).schema, path=d, source=\'parquet\')
        >>> _ = spark.sql("DROP TABLE tbl2")
        '''
    def dropTempView(self, viewName: str) -> bool:
        '''Drops the local temporary view with the given view name in the catalog.
        If the view has been cached before, then it will also be uncached.
        Returns true if this view is dropped successfully, false otherwise.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        viewName : str
            name of the temporary view to drop.

        Returns
        -------
        bool
            If the temporary view was successfully dropped or not.

            .. versionadded:: 2.1.0
                The return type of this method was ``None`` in Spark 2.0, but changed to ``bool``
                in Spark 2.1.

        Examples
        --------
        >>> spark.createDataFrame([(1, 1)]).createTempView("my_table")

        Dropping the temporary view.

        >>> spark.catalog.dropTempView("my_table")
        True

        Throw an exception if the temporary view does not exists.

        >>> spark.table("my_table")
        Traceback (most recent call last):
            ...
        AnalysisException: ...
        '''
    def dropGlobalTempView(self, viewName: str) -> bool:
        '''Drops the global temporary view with the given view name in the catalog.

        .. versionadded:: 2.1.0

        Parameters
        ----------
        viewName : str
            name of the global view to drop.

        Returns
        -------
        bool
            If the global view was successfully dropped or not.

        Notes
        -----
        If the view has been cached before, then it will also be uncached.

        Examples
        --------
        >>> spark.createDataFrame([(1, 1)]).createGlobalTempView("my_table")

        Dropping the global view.

        >>> spark.catalog.dropGlobalTempView("my_table")
        True

        Throw an exception if the global view does not exists.

        >>> spark.table("global_temp.my_table")
        Traceback (most recent call last):
            ...
        AnalysisException: ...
        '''
    def registerFunction(self, name: str, f: Callable[..., Any], returnType: DataType | None = None) -> UserDefinedFunctionLike:
        """An alias for :func:`spark.udf.register`.
        See :meth:`pyspark.sql.UDFRegistration.register`.

        .. versionadded:: 2.0.0

        .. deprecated:: 2.3.0
            Use :func:`spark.udf.register` instead.

        .. versionchanged:: 3.4.0
            Supports Spark Connect.
        """
    def isCached(self, tableName: str) -> bool:
        '''
        Returns true if the table is currently cached in-memory.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        tableName : str
            name of the table to get.

            .. versionchanged:: 3.4.0
                Allow ``tableName`` to be qualified with catalog name.

        Returns
        -------
        bool

        Examples
        --------
        >>> _ = spark.sql("DROP TABLE IF EXISTS tbl1")
        >>> _ = spark.sql("CREATE TABLE tbl1 (name STRING, age INT) USING parquet")
        >>> spark.catalog.cacheTable("tbl1")
        >>> spark.catalog.isCached("tbl1")
        True

        Throw an analysis exception when the table does not exist.

        >>> spark.catalog.isCached("not_existing_table")
        Traceback (most recent call last):
            ...
        AnalysisException: ...

        Using the fully qualified name for the table.

        >>> spark.catalog.isCached("spark_catalog.default.tbl1")
        True
        >>> spark.catalog.uncacheTable("tbl1")
        >>> _ = spark.sql("DROP TABLE tbl1")
        '''
    def cacheTable(self, tableName: str) -> None:
        '''Caches the specified table in-memory.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        tableName : str
            name of the table to get.

            .. versionchanged:: 3.4.0
                Allow ``tableName`` to be qualified with catalog name.

        Examples
        --------
        >>> _ = spark.sql("DROP TABLE IF EXISTS tbl1")
        >>> _ = spark.sql("CREATE TABLE tbl1 (name STRING, age INT) USING parquet")
        >>> spark.catalog.cacheTable("tbl1")

        Throw an analysis exception when the table does not exist.

        >>> spark.catalog.cacheTable("not_existing_table")
        Traceback (most recent call last):
            ...
        AnalysisException: ...

        Using the fully qualified name for the table.

        >>> spark.catalog.cacheTable("spark_catalog.default.tbl1")
        >>> spark.catalog.uncacheTable("tbl1")
        >>> _ = spark.sql("DROP TABLE tbl1")
        '''
    def uncacheTable(self, tableName: str) -> None:
        '''Removes the specified table from the in-memory cache.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        tableName : str
            name of the table to get.

            .. versionchanged:: 3.4.0
                Allow ``tableName`` to be qualified with catalog name.

        Examples
        --------
        >>> _ = spark.sql("DROP TABLE IF EXISTS tbl1")
        >>> _ = spark.sql("CREATE TABLE tbl1 (name STRING, age INT) USING parquet")
        >>> spark.catalog.cacheTable("tbl1")
        >>> spark.catalog.uncacheTable("tbl1")
        >>> spark.catalog.isCached("tbl1")
        False

        Throw an analysis exception when the table does not exist.

        >>> spark.catalog.uncacheTable("not_existing_table")
        Traceback (most recent call last):
            ...
        AnalysisException: ...

        Using the fully qualified name for the table.

        >>> spark.catalog.uncacheTable("spark_catalog.default.tbl1")
        >>> spark.catalog.isCached("tbl1")
        False
        >>> _ = spark.sql("DROP TABLE tbl1")
        '''
    def clearCache(self) -> None:
        '''Removes all cached tables from the in-memory cache.

        .. versionadded:: 2.0.0

        Examples
        --------
        >>> _ = spark.sql("DROP TABLE IF EXISTS tbl1")
        >>> _ = spark.sql("CREATE TABLE tbl1 (name STRING, age INT) USING parquet")
        >>> spark.catalog.clearCache()
        >>> spark.catalog.isCached("tbl1")
        False
        >>> _ = spark.sql("DROP TABLE tbl1")
        '''
    def refreshTable(self, tableName: str) -> None:
        '''Invalidates and refreshes all the cached data and metadata of the given table.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        tableName : str
            name of the table to get.

            .. versionchanged:: 3.4.0
                Allow ``tableName`` to be qualified with catalog name.

        Examples
        --------
        The example below caches a table, and then removes the data.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     _ = spark.sql("DROP TABLE IF EXISTS tbl1")
        ...     _ = spark.sql(
        ...         "CREATE TABLE tbl1 (col STRING) USING TEXT LOCATION \'{}\'".format(d))
        ...     _ = spark.sql("INSERT INTO tbl1 SELECT \'abc\'")
        ...     spark.catalog.cacheTable("tbl1")
        ...     spark.table("tbl1").show()
        +---+
        |col|
        +---+
        |abc|
        +---+

        Because the table is cached, it computes from the cached data as below.

        >>> spark.table("tbl1").count()
        1

        After refreshing the table, it shows 0 because the data does not exist anymore.

        >>> spark.catalog.refreshTable("tbl1")
        >>> spark.table("tbl1").count()
        0

        Using the fully qualified name for the table.

        >>> spark.catalog.refreshTable("spark_catalog.default.tbl1")
        >>> _ = spark.sql("DROP TABLE tbl1")
        '''
    def recoverPartitions(self, tableName: str) -> None:
        '''Recovers all the partitions of the given table and updates the catalog.

        .. versionadded:: 2.1.1

        Parameters
        ----------
        tableName : str
            name of the table to get.

        Notes
        -----
        Only works with a partitioned table, and not a view.

        Examples
        --------
        The example below creates a partitioned table against the existing directory of
        the partitioned table. After that, it recovers the partitions.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     _ = spark.sql("DROP TABLE IF EXISTS tbl1")
        ...     spark.range(1).selectExpr(
        ...         "id as key", "id as value").write.partitionBy("key").mode("overwrite").save(d)
        ...     _ = spark.sql(
        ...          "CREATE TABLE tbl1 (key LONG, value LONG)"
        ...          "USING parquet OPTIONS (path \'{}\') PARTITIONED BY (key)".format(d))
        ...     spark.table("tbl1").show()
        ...     spark.catalog.recoverPartitions("tbl1")
        ...     spark.table("tbl1").show()
        +-----+---+
        |value|key|
        +-----+---+
        +-----+---+
        +-----+---+
        |value|key|
        +-----+---+
        |    0|  0|
        +-----+---+
        >>> _ = spark.sql("DROP TABLE tbl1")
        '''
    def refreshByPath(self, path: str) -> None:
        '''Invalidates and refreshes all the cached data (and the associated metadata) for any
        DataFrame that contains the given data source path.

        .. versionadded:: 2.2.0

        Parameters
        ----------
        path : str
            the path to refresh the cache.

        Examples
        --------
        The example below caches a table, and then removes the data.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     _ = spark.sql("DROP TABLE IF EXISTS tbl1")
        ...     _ = spark.sql(
        ...         "CREATE TABLE tbl1 (col STRING) USING TEXT LOCATION \'{}\'".format(d))
        ...     _ = spark.sql("INSERT INTO tbl1 SELECT \'abc\'")
        ...     spark.catalog.cacheTable("tbl1")
        ...     spark.table("tbl1").show()
        +---+
        |col|
        +---+
        |abc|
        +---+

        Because the table is cached, it computes from the cached data as below.

        >>> spark.table("tbl1").count()
        1

        After refreshing the table by path, it shows 0 because the data does not exist anymore.

        >>> spark.catalog.refreshByPath(d)
        >>> spark.table("tbl1").count()
        0

        >>> _ = spark.sql("DROP TABLE tbl1")
        '''
