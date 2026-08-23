from pyspark.sql._typing import OptionalPrimitiveType, SupportsProcess
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.readwriter import OptionUtils
from pyspark.sql.session import SparkSession
from pyspark.sql.streaming.query import StreamingQuery
from pyspark.sql.types import Row, StructType
from typing import Callable, List, overload

__all__ = ['DataStreamReader', 'DataStreamWriter']

class DataStreamReader(OptionUtils):
    '''
    Interface used to load a streaming :class:`DataFrame <pyspark.sql.DataFrame>` from external
    storage systems (e.g. file systems, key-value stores, etc).
    Use :attr:`SparkSession.readStream <pyspark.sql.SparkSession.readStream>` to access this.

    .. versionadded:: 2.0.0

    Notes
    -----
    This API is evolving.

    Examples
    --------
    >>> spark.readStream
    <pyspark.sql.streaming.readwriter.DataStreamReader object ...>

    The example below uses Rate source that generates rows continuously.
    After that, we operate a modulo by 3, and then writes the stream out to the console.
    The streaming query stops in 3 seconds.

    >>> import time
    >>> df = spark.readStream.format("rate").load()
    >>> df = df.selectExpr("value % 3 as v")
    >>> q = df.writeStream.format("console").start()
    >>> time.sleep(3)
    >>> q.stop()
    '''
    def __init__(self, spark: SparkSession) -> None: ...
    def format(self, source: str) -> DataStreamReader:
        '''Specifies the input data source format.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        source : str
            name of the data source, e.g. \'json\', \'parquet\'.

        Notes
        -----
        This API is evolving.

        Examples
        --------
        >>> spark.readStream.format("text")
        <pyspark.sql.streaming.readwriter.DataStreamReader object ...>

        This API allows to configure other sources to read. The example below writes a small text
        file, and reads it back via Text source.

        >>> import tempfile
        >>> import time
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a temporary text file to read it.
        ...     spark.createDataFrame(
        ...         [("hello",), ("this",)]).write.mode("overwrite").format("text").save(d)
        ...
        ...     # Start a streaming query to read the text file.
        ...     q = spark.readStream.format("text").load(d).writeStream.format("console").start()
        ...     time.sleep(3)
        ...     q.stop()
        '''
    def schema(self, schema: StructType | str) -> DataStreamReader:
        '''Specifies the input schema.

        Some data sources (e.g. JSON) can infer the input schema automatically from data.
        By specifying the schema here, the underlying data source can skip the schema
        inference step, and thus speed up data loading.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        schema : :class:`pyspark.sql.types.StructType` or str
            a :class:`pyspark.sql.types.StructType` object or a DDL-formatted string
            (For example ``col0 INT, col1 DOUBLE``).

        Notes
        -----
        This API is evolving.

        Examples
        --------
        >>> from pyspark.sql.types import StructField, StructType, StringType
        >>> spark.readStream.schema(StructType([StructField("data", StringType(), True)]))
        <pyspark.sql.streaming.readwriter.DataStreamReader object ...>
        >>> spark.readStream.schema("col0 INT, col1 DOUBLE")
        <pyspark.sql.streaming.readwriter.DataStreamReader object ...>

        The example below specifies a different schema to CSV file.

        >>> import tempfile
        >>> import time
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Start a streaming query to read the CSV file.
        ...     spark.readStream.schema("col0 INT, col1 STRING").format("csv").load(d).printSchema()
        root
         |-- col0: integer (nullable = true)
         |-- col1: string (nullable = true)
        '''
    def option(self, key: str, value: OptionalPrimitiveType) -> DataStreamReader:
        '''Adds an input option for the underlying data source.

        .. versionadded:: 2.0.0

        Notes
        -----
        This API is evolving.

        Examples
        --------
        >>> spark.readStream.option("x", 1)
        <pyspark.sql.streaming.readwriter.DataStreamReader object ...>

        The example below specifies \'rowsPerSecond\' option to Rate source in order to generate
        10 rows every second.

        >>> import time
        >>> q = spark.readStream.format(
        ...     "rate").option("rowsPerSecond", 10).load().writeStream.format("console").start()
        >>> time.sleep(3)
        >>> q.stop()
        '''
    def options(self, **options: OptionalPrimitiveType) -> DataStreamReader:
        '''Adds input options for the underlying data source.

        .. versionadded:: 2.0.0

        Notes
        -----
        This API is evolving.

        Examples
        --------
        >>> spark.readStream.options(x="1", y=2)
        <pyspark.sql.streaming.readwriter.DataStreamReader object ...>

        The example below specifies \'rowsPerSecond\' and \'numPartitions\' options to
        Rate source in order to generate 10 rows with 10 partitions every second.

        >>> import time
        >>> q = spark.readStream.format("rate").options(
        ...    rowsPerSecond=10, numPartitions=10
        ... ).load().writeStream.format("console").start()
        >>> time.sleep(3)
        >>> q.stop()
        '''
    def load(self, path: str | None = None, format: str | None = None, schema: StructType | str | None = None, **options: OptionalPrimitiveType) -> DataFrame:
        '''Loads a data stream from a data source and returns it as a
        :class:`DataFrame <pyspark.sql.DataFrame>`.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        path : str, optional
            optional string for file-system backed data sources.
        format : str, optional
            optional string for format of the data source. Default to \'parquet\'.
        schema : :class:`pyspark.sql.types.StructType` or str, optional
            optional :class:`pyspark.sql.types.StructType` for the input schema
            or a DDL-formatted string (For example ``col0 INT, col1 DOUBLE``).
        **options : dict
            all other string options

        Notes
        -----
        This API is evolving.

        Examples
        --------
        Load a data stream from a temporary JSON file.

        >>> import tempfile
        >>> import time
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a temporary JSON file to read it.
        ...     spark.createDataFrame(
        ...         [(100, "Hyukjin Kwon"),], ["age", "name"]
        ...     ).write.mode("overwrite").format("json").save(d)
        ...
        ...     # Start a streaming query to read the JSON file.
        ...     q = spark.readStream.schema(
        ...         "age INT, name STRING"
        ...     ).format("json").load(d).writeStream.format("console").start()
        ...     time.sleep(3)
        ...     q.stop()
        '''
    def json(self, path: str, schema: StructType | str | None = None, primitivesAsString: bool | str | None = None, prefersDecimal: bool | str | None = None, allowComments: bool | str | None = None, allowUnquotedFieldNames: bool | str | None = None, allowSingleQuotes: bool | str | None = None, allowNumericLeadingZero: bool | str | None = None, allowBackslashEscapingAnyCharacter: bool | str | None = None, mode: str | None = None, columnNameOfCorruptRecord: str | None = None, dateFormat: str | None = None, timestampFormat: str | None = None, multiLine: bool | str | None = None, allowUnquotedControlChars: bool | str | None = None, lineSep: str | None = None, locale: str | None = None, dropFieldIfAllNull: bool | str | None = None, encoding: str | None = None, pathGlobFilter: bool | str | None = None, recursiveFileLookup: bool | str | None = None, allowNonNumericNumbers: bool | str | None = None) -> DataFrame:
        '''
        Loads a JSON file stream and returns the results as a :class:`DataFrame`.

        `JSON Lines <http://jsonlines.org/>`_ (newline-delimited JSON) is supported by default.
        For JSON (one record per file), set the ``multiLine`` parameter to ``true``.

        If the ``schema`` parameter is not specified, this function goes
        through the input once to determine the input schema.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        path : str
            string represents path to the JSON dataset,
            or RDD of Strings storing JSON objects.
        schema : :class:`pyspark.sql.types.StructType` or str, optional
            an optional :class:`pyspark.sql.types.StructType` for the input schema
            or a DDL-formatted string (For example ``col0 INT, col1 DOUBLE``).

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option>`_
            in the version you use.

            .. # noqa

        Notes
        -----
        This API is evolving.

        Examples
        --------
        Load a data stream from a temporary JSON file.

        >>> import tempfile
        >>> import time
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a temporary JSON file to read it.
        ...     spark.createDataFrame(
        ...         [(100, "Hyukjin Kwon"),], ["age", "name"]
        ...     ).write.mode("overwrite").format("json").save(d)
        ...
        ...     # Start a streaming query to read the JSON file.
        ...     q = spark.readStream.schema(
        ...         "age INT, name STRING"
        ...     ).json(d).writeStream.format("console").start()
        ...     time.sleep(3)
        ...     q.stop()
        '''
    def orc(self, path: str, mergeSchema: bool | None = None, pathGlobFilter: bool | str | None = None, recursiveFileLookup: bool | str | None = None) -> DataFrame:
        '''Loads a ORC file stream, returning the result as a :class:`DataFrame`.

        .. versionadded:: 2.3.0

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-orc.html#data-source-option>`_
            in the version you use.

            .. # noqa

        Examples
        --------
        Load a data stream from a temporary ORC file.

        >>> import tempfile
        >>> import time
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a temporary ORC file to read it.
        ...     spark.range(10).write.mode("overwrite").format("orc").save(d)
        ...
        ...     # Start a streaming query to read the ORC file.
        ...     q = spark.readStream.schema("id LONG").orc(d).writeStream.format("console").start()
        ...     time.sleep(3)
        ...     q.stop()
        '''
    def parquet(self, path: str, mergeSchema: bool | None = None, pathGlobFilter: bool | str | None = None, recursiveFileLookup: bool | str | None = None, datetimeRebaseMode: bool | str | None = None, int96RebaseMode: bool | str | None = None) -> DataFrame:
        '''
        Loads a Parquet file stream, returning the result as a :class:`DataFrame`.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        path : str
            the path in any Hadoop supported file system

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#data-source-option>`_.
            in the version you use.

            .. # noqa

        Examples
        --------
        Load a data stream from a temporary Parquet file.

        >>> import tempfile
        >>> import time
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a temporary Parquet file to read it.
        ...     spark.range(10).write.mode("overwrite").format("parquet").save(d)
        ...
        ...     # Start a streaming query to read the Parquet file.
        ...     q = spark.readStream.schema(
        ...         "id LONG").parquet(d).writeStream.format("console").start()
        ...     time.sleep(3)
        ...     q.stop()
        '''
    def text(self, path: str, wholetext: bool = False, lineSep: str | None = None, pathGlobFilter: bool | str | None = None, recursiveFileLookup: bool | str | None = None) -> DataFrame:
        '''
        Loads a text file stream and returns a :class:`DataFrame` whose schema starts with a
        string column named "value", and followed by partitioned columns if there
        are any.
        The text files must be encoded as UTF-8.

        By default, each line in the text file is a new row in the resulting DataFrame.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        path : str or list
            string, or list of strings, for input path(s).

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-text.html#data-source-option>`_
            in the version you use.

            .. # noqa

        Notes
        -----
        This API is evolving.

        Examples
        --------
        Load a data stream from a temporary text file.

        >>> import tempfile
        >>> import time
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a temporary text file to read it.
        ...     spark.createDataFrame(
        ...         [("hello",), ("this",)]).write.mode("overwrite").format("text").save(d)
        ...
        ...     # Start a streaming query to read the text file.
        ...     q = spark.readStream.text(d).writeStream.format("console").start()
        ...     time.sleep(3)
        ...     q.stop()
        '''
    def csv(self, path: str, schema: StructType | str | None = None, sep: str | None = None, encoding: str | None = None, quote: str | None = None, escape: str | None = None, comment: str | None = None, header: bool | str | None = None, inferSchema: bool | str | None = None, ignoreLeadingWhiteSpace: bool | str | None = None, ignoreTrailingWhiteSpace: bool | str | None = None, nullValue: str | None = None, nanValue: str | None = None, positiveInf: str | None = None, negativeInf: str | None = None, dateFormat: str | None = None, timestampFormat: str | None = None, maxColumns: int | str | None = None, maxCharsPerColumn: int | str | None = None, maxMalformedLogPerPartition: int | str | None = None, mode: str | None = None, columnNameOfCorruptRecord: str | None = None, multiLine: bool | str | None = None, charToEscapeQuoteEscaping: bool | str | None = None, enforceSchema: bool | str | None = None, emptyValue: str | None = None, locale: str | None = None, lineSep: str | None = None, pathGlobFilter: bool | str | None = None, recursiveFileLookup: bool | str | None = None, unescapedQuoteHandling: str | None = None) -> DataFrame:
        '''Loads a CSV file stream and returns the result as a :class:`DataFrame`.

        This function will go through the input once to determine the input schema if
        ``inferSchema`` is enabled. To avoid going through the entire data once, disable
        ``inferSchema`` option or specify the schema explicitly using ``schema``.

        Parameters
        ----------
        path : str or list
            string, or list of strings, for input path(s).
        schema : :class:`pyspark.sql.types.StructType` or str, optional
            an optional :class:`pyspark.sql.types.StructType` for the input schema
            or a DDL-formatted string (For example ``col0 INT, col1 DOUBLE``).

        .. versionadded:: 2.0.0

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option>`_
            in the version you use.

            .. # noqa

        Notes
        -----
        This API is evolving.

        Examples
        --------
        Load a data stream from a temporary CSV file.

        >>> import tempfile
        >>> import time
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a temporary text file to read it.
        ...     spark.createDataFrame([(1, "2"),]).write.mode("overwrite").format("csv").save(d)
        ...
        ...     # Start a streaming query to read the CSV file.
        ...     q = spark.readStream.schema(
        ...         "col0 INT, col1 STRING"
        ...     ).format("csv").load(d).writeStream.format("console").start()
        ...     time.sleep(3)
        ...     q.stop()
        '''
    def table(self, tableName: str) -> DataFrame:
        '''Define a Streaming DataFrame on a Table. The DataSource corresponding to the table should
        support streaming mode.

        .. versionadded:: 3.1.0

        Parameters
        ----------
        tableName : str
            string, for the name of the table.

        Returns
        -------
        :class:`DataFrame`

        Notes
        -----
        This API is evolving.

        Examples
        --------
        Load a data stream from a table.

        >>> import tempfile
        >>> import time
        >>> _ = spark.sql("DROP TABLE IF EXISTS my_table")
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Create a table with Rate source.
        ...     q1 = spark.readStream.format("rate").load().writeStream.toTable(
        ...         "my_table", checkpointLocation=d)
        ...
        ...     # Read the table back and print out in the console.
        ...     q2 = spark.readStream.table("my_table").writeStream.format("console").start()
        ...     time.sleep(3)
        ...     q1.stop()
        ...     q2.stop()
        ...     _ = spark.sql("DROP TABLE my_table")
        '''

class DataStreamWriter:
    '''
    Interface used to write a streaming :class:`DataFrame <pyspark.sql.DataFrame>` to external
    storage systems (e.g. file systems, key-value stores, etc).
    Use :attr:`DataFrame.writeStream <pyspark.sql.DataFrame.writeStream>`
    to access this.

    .. versionadded:: 2.0.0

    Notes
    -----
    This API is evolving.

    Examples
    --------
    The example below uses Rate source that generates rows continuously.
    After that, we operate a modulo by 3, and then writes the stream out to the console.
    The streaming query stops in 3 seconds.

    >>> import time
    >>> df = spark.readStream.format("rate").load()
    >>> df = df.selectExpr("value % 3 as v")
    >>> q = df.writeStream.format("console").start()
    >>> time.sleep(3)
    >>> q.stop()
    '''
    def __init__(self, df: DataFrame) -> None: ...
    def outputMode(self, outputMode: str) -> DataStreamWriter:
        '''Specifies how data of a streaming DataFrame/Dataset is written to a streaming sink.

        .. versionadded:: 2.0.0

        Options include:

        * `append`: Only the new rows in the streaming DataFrame/Dataset will be written to
           the sink
        * `complete`: All the rows in the streaming DataFrame/Dataset will be written to the sink
           every time these are some updates
        * `update`: only the rows that were updated in the streaming DataFrame/Dataset will be
           written to the sink every time there are some updates. If the query doesn\'t contain
           aggregations, it will be equivalent to `append` mode.

        Notes
        -----
        This API is evolving.

        Examples
        --------
        >>> df = spark.readStream.format("rate").load()
        >>> df.writeStream.outputMode(\'append\')
        <pyspark.sql.streaming.readwriter.DataStreamWriter object ...>

        The example below uses Complete mode that the entire aggregated counts are printed out.

        >>> import time
        >>> df = spark.readStream.format("rate").option("rowsPerSecond", 10).load()
        >>> df = df.groupby().count()
        >>> q = df.writeStream.outputMode("complete").format("console").start()
        >>> time.sleep(3)
        >>> q.stop()
        '''
    def format(self, source: str) -> DataStreamWriter:
        '''Specifies the underlying output data source.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        source : str
            string, name of the data source, which for now can be \'parquet\'.

        Notes
        -----
        This API is evolving.

        Examples
        --------
        >>> df = spark.readStream.format("rate").load()
        >>> df.writeStream.format("text")
        <pyspark.sql.streaming.readwriter.DataStreamWriter object ...>

        This API allows to configure the source to write. The example below writes a CSV
        file from Rate source in a streaming manner.

        >>> import tempfile
        >>> import time
        >>> with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as cp:
        ...     df = spark.readStream.format("rate").load()
        ...     q = df.writeStream.format("csv").option("checkpointLocation", cp).start(d)
        ...     time.sleep(5)
        ...     q.stop()
        ...     spark.read.schema("timestamp TIMESTAMP, value STRING").csv(d).show()
        +...---------+-----+
        |...timestamp|value|
        +...---------+-----+
        ...
        '''
    def option(self, key: str, value: OptionalPrimitiveType) -> DataStreamWriter:
        '''Adds an output option for the underlying data source.

        .. versionadded:: 2.0.0

        Notes
        -----
        This API is evolving.

        Examples
        --------
        >>> df = spark.readStream.format("rate").load()
        >>> df.writeStream.option("x", 1)
        <pyspark.sql.streaming.readwriter.DataStreamWriter object ...>

        The example below specifies \'numRows\' option to Console source in order to print
        3 rows for every batch.

        >>> import time
        >>> q = spark.readStream.format(
        ...     "rate").option("rowsPerSecond", 10).load().writeStream.format(
        ...         "console").option("numRows", 3).start()
        >>> time.sleep(3)
        >>> q.stop()
        '''
    def options(self, **options: OptionalPrimitiveType) -> DataStreamWriter:
        '''Adds output options for the underlying data source.

        .. versionadded:: 2.0.0

        Notes
        -----
        This API is evolving.

        Examples
        --------
        >>> df = spark.readStream.format("rate").load()
        >>> df.writeStream.option("x", 1)
        <pyspark.sql.streaming.readwriter.DataStreamWriter object ...>

        The example below specifies \'numRows\' and \'truncate\' options to Console source in order
        to print 3 rows for every batch without truncating the results.

        >>> import time
        >>> q = spark.readStream.format(
        ...     "rate").option("rowsPerSecond", 10).load().writeStream.format(
        ...         "console").options(numRows=3, truncate=False).start()
        >>> time.sleep(3)
        >>> q.stop()
        '''
    @overload
    def partitionBy(self, *cols: str) -> DataStreamWriter: ...
    @overload
    def partitionBy(self, __cols: List[str]) -> DataStreamWriter: ...
    def queryName(self, queryName: str) -> DataStreamWriter:
        '''Specifies the name of the :class:`StreamingQuery` that can be started with
        :func:`start`. This name must be unique among all the currently active queries
        in the associated SparkSession.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        queryName : str
            unique name for the query

        Notes
        -----
        This API is evolving.

        Examples
        --------
        >>> import time
        >>> df = spark.readStream.format("rate").load()
        >>> q = df.writeStream.queryName("streaming_query").format("console").start()
        >>> q.stop()
        >>> q.name
        \'streaming_query\'
        '''
    @overload
    def trigger(self, *, processingTime: str) -> DataStreamWriter: ...
    @overload
    def trigger(self, *, once: bool) -> DataStreamWriter: ...
    @overload
    def trigger(self, *, continuous: str) -> DataStreamWriter: ...
    @overload
    def trigger(self, *, availableNow: bool) -> DataStreamWriter: ...
    @overload
    def foreach(self, f: Callable[[Row], None]) -> DataStreamWriter: ...
    @overload
    def foreach(self, f: SupportsProcess) -> DataStreamWriter: ...
    def foreachBatch(self, func: Callable[[DataFrame, int], None]) -> DataStreamWriter:
        '''
        Sets the output of the streaming query to be processed using the provided
        function. This is supported only the in the micro-batch execution modes (that is, when the
        trigger is not continuous). In every micro-batch, the provided function will be called in
        every micro-batch with (i) the output rows as a DataFrame and (ii) the batch identifier.
        The batchId can be used deduplicate and transactionally write the output
        (that is, the provided Dataset) to external systems. The output DataFrame is guaranteed
        to exactly same for the same batchId (assuming all operations are deterministic in the
        query).

        .. versionadded:: 2.4.0

        Notes
        -----
        This API is evolving.

        Examples
        --------
        >>> import time
        >>> df = spark.readStream.format("rate").load()
        >>> def func(batch_df, batch_id):
        ...     batch_df.collect()
        ...
        >>> q = df.writeStream.foreachBatch(func).start()
        >>> time.sleep(3)
        >>> q.stop()
        '''
    def start(self, path: str | None = None, format: str | None = None, outputMode: str | None = None, partitionBy: str | List[str] | None = None, queryName: str | None = None, **options: OptionalPrimitiveType) -> StreamingQuery:
        '''Streams the contents of the :class:`DataFrame` to a data source.

        The data source is specified by the ``format`` and a set of ``options``.
        If ``format`` is not specified, the default data source configured by
        ``spark.sql.sources.default`` will be used.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        path : str, optional
            the path in a Hadoop supported file system
        format : str, optional
            the format used to save
        outputMode : str, optional
            specifies how data of a streaming DataFrame/Dataset is written to a
            streaming sink.

            * `append`: Only the new rows in the streaming DataFrame/Dataset will be written to the
              sink
            * `complete`: All the rows in the streaming DataFrame/Dataset will be written to the
              sink every time these are some updates
            * `update`: only the rows that were updated in the streaming DataFrame/Dataset will be
              written to the sink every time there are some updates. If the query doesn\'t contain
              aggregations, it will be equivalent to `append` mode.
        partitionBy : str or list, optional
            names of partitioning columns
        queryName : str, optional
            unique name for the query
        **options : dict
            All other string options. You may want to provide a `checkpointLocation`
            for most streams, however it is not required for a `memory` stream.

        Notes
        -----
        This API is evolving.

        Examples
        --------
        >>> df = spark.readStream.format("rate").load()

        Basic example.

        >>> q = df.writeStream.format(\'memory\').queryName(\'this_query\').start()
        >>> q.isActive
        True
        >>> q.name
        \'this_query\'
        >>> q.stop()
        >>> q.isActive
        False

        Example with using other parameters with a trigger.

        >>> q = df.writeStream.trigger(processingTime=\'5 seconds\').start(
        ...     queryName=\'that_query\', outputMode="append", format=\'memory\')
        >>> q.name
        \'that_query\'
        >>> q.isActive
        True
        >>> q.stop()
        '''
    def toTable(self, tableName: str, format: str | None = None, outputMode: str | None = None, partitionBy: str | List[str] | None = None, queryName: str | None = None, **options: OptionalPrimitiveType) -> StreamingQuery:
        '''
        Starts the execution of the streaming query, which will continually output results to the
        given table as new data arrives.

        The returned :class:`StreamingQuery` object can be used to interact with the stream.

        .. versionadded:: 3.1.0

        Parameters
        ----------
        tableName : str
            string, for the name of the table.
        format : str, optional
            the format used to save.
        outputMode : str, optional
            specifies how data of a streaming DataFrame/Dataset is written to a
            streaming sink.

            * `append`: Only the new rows in the streaming DataFrame/Dataset will be written to the
              sink
            * `complete`: All the rows in the streaming DataFrame/Dataset will be written to the
              sink every time these are some updates
            * `update`: only the rows that were updated in the streaming DataFrame/Dataset will be
              written to the sink every time there are some updates. If the query doesn\'t contain
              aggregations, it will be equivalent to `append` mode.
        partitionBy : str or list, optional
            names of partitioning columns
        queryName : str, optional
            unique name for the query
        **options : dict
            All other string options. You may want to provide a `checkpointLocation`.

        Notes
        -----
        This API is evolving.

        For v1 table, partitioning columns provided by `partitionBy` will be respected no matter
        the table exists or not. A new table will be created if the table not exists.

        For v2 table, `partitionBy` will be ignored if the table already exists. `partitionBy` will
        be respected only if the v2 table does not exist. Besides, the v2 table created by this API
        lacks some functionalities (e.g., customized properties, options, and serde info). If you
        need them, please create the v2 table manually before the execution to avoid creating a
        table with incomplete information.

        Examples
        --------
        Save a data stream to a table.

        >>> import tempfile
        >>> import time
        >>> _ = spark.sql("DROP TABLE IF EXISTS my_table2")
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Create a table with Rate source.
        ...     q = spark.readStream.format("rate").option(
        ...         "rowsPerSecond", 10).load().writeStream.toTable(
        ...             "my_table2",
        ...             queryName=\'that_query\',
        ...             outputMode="append",
        ...             format=\'parquet\',
        ...             checkpointLocation=d)
        ...     time.sleep(3)
        ...     q.stop()
        ...     spark.read.table("my_table2").show()
        ...     _ = spark.sql("DROP TABLE my_table2")
        +...---------+-----+
        |...timestamp|value|
        +...---------+-----+
        ...
        '''
