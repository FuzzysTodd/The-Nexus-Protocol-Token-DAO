from pyspark import RDD
from pyspark.sql._typing import OptionalPrimitiveType
from pyspark.sql.column import Column
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType
from typing import Dict, List, Tuple, overload

__all__ = ['DataFrameReader', 'DataFrameWriter', 'DataFrameWriterV2']

PathOrPaths = str | List[str]
TupleOrListOfString = List[str] | Tuple[str, ...]

class OptionUtils: ...

class DataFrameReader(OptionUtils):
    """
    Interface used to load a :class:`DataFrame` from external storage systems
    (e.g. file systems, key-value stores, etc). Use :attr:`SparkSession.read`
    to access this.

    .. versionadded:: 1.4.0

    .. versionchanged:: 3.4.0
        Supports Spark Connect.
    """
    def __init__(self, spark: SparkSession) -> None: ...
    def format(self, source: str) -> DataFrameReader:
        '''Specifies the input data source format.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        source : str
            string, name of the data source, e.g. \'json\', \'parquet\'.

        Examples
        --------
        >>> spark.read.format(\'json\')
        <...readwriter.DataFrameReader object ...>

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
    def schema(self, schema: StructType | str) -> DataFrameReader:
        '''Specifies the input schema.

        Some data sources (e.g. JSON) can infer the input schema automatically from data.
        By specifying the schema here, the underlying data source can skip the schema
        inference step, and thus speed up data loading.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        schema : :class:`pyspark.sql.types.StructType` or str
            a :class:`pyspark.sql.types.StructType` object or a DDL-formatted string
            (For example ``col0 INT, col1 DOUBLE``).

        Examples
        --------
        >>> spark.read.schema("col0 INT, col1 DOUBLE")
        <...readwriter.DataFrameReader object ...>

        Specify the schema with reading a CSV file.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     spark.read.schema("col0 INT, col1 DOUBLE").format("csv").load(d).printSchema()
        root
         |-- col0: integer (nullable = true)
         |-- col1: double (nullable = true)
        '''
    def option(self, key: str, value: OptionalPrimitiveType) -> DataFrameReader:
        '''
        Adds an input option for the underlying data source.

        .. versionadded:: 1.5.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        key : str
            The key for the option to set.
        value
            The value for the option to set.

        Examples
        --------
        >>> spark.read.option("key", "value")
        <...readwriter.DataFrameReader object ...>

        Specify the option \'nullValue\' with reading a CSV file.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a CSV file
        ...     df = spark.createDataFrame([{"age": 100, "name": "Hyukjin Kwon"}])
        ...     df.write.mode("overwrite").format("csv").save(d)
        ...
        ...     # Read the CSV file as a DataFrame with \'nullValue\' option set to \'Hyukjin Kwon\'.
        ...     spark.read.schema(df.schema).option(
        ...         "nullValue", "Hyukjin Kwon").format(\'csv\').load(d).show()
        +---+----+
        |age|name|
        +---+----+
        |100|null|
        +---+----+
        '''
    def options(self, **options: OptionalPrimitiveType) -> DataFrameReader:
        '''
        Adds input options for the underlying data source.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        **options : dict
            The dictionary of string keys and prmitive-type values.

        Examples
        --------
        >>> spark.read.option("key", "value")
        <...readwriter.DataFrameReader object ...>

        Specify the option \'nullValue\' and \'header\' with reading a CSV file.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a CSV file with a header.
        ...     df = spark.createDataFrame([{"age": 100, "name": "Hyukjin Kwon"}])
        ...     df.write.option("header", True).mode("overwrite").format("csv").save(d)
        ...
        ...     # Read the CSV file as a DataFrame with \'nullValue\' option set to \'Hyukjin Kwon\',
        ...     # and \'header\' option set to `True`.
        ...     spark.read.options(
        ...         nullValue="Hyukjin Kwon",
        ...         header=True
        ...     ).format(\'csv\').load(d).show()
        +---+----+
        |age|name|
        +---+----+
        |100|null|
        +---+----+
        '''
    def load(self, path: PathOrPaths | None = None, format: str | None = None, schema: StructType | str | None = None, **options: OptionalPrimitiveType) -> DataFrame:
        '''Loads data from a data source and returns it as a :class:`DataFrame`.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        path : str or list, optional
            optional string or a list of string for file-system backed data sources.
        format : str, optional
            optional string for format of the data source. Default to \'parquet\'.
        schema : :class:`pyspark.sql.types.StructType` or str, optional
            optional :class:`pyspark.sql.types.StructType` for the input schema
            or a DDL-formatted string (For example ``col0 INT, col1 DOUBLE``).
        **options : dict
            all other string options

        Examples
        --------
        Load a CSV file with format, schema and options specified.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a CSV file with a header
        ...     df = spark.createDataFrame([{"age": 100, "name": "Hyukjin Kwon"}])
        ...     df.write.option("header", True).mode("overwrite").format("csv").save(d)
        ...
        ...     # Read the CSV file as a DataFrame with \'nullValue\' option set to \'Hyukjin Kwon\',
        ...     # and \'header\' option set to `True`.
        ...     df = spark.read.load(
        ...         d, schema=df.schema, format="csv", nullValue="Hyukjin Kwon", header=True)
        ...     df.printSchema()
        ...     df.show()
        root
         |-- age: long (nullable = true)
         |-- name: string (nullable = true)
        +---+----+
        |age|name|
        +---+----+
        |100|null|
        +---+----+
        '''
    def json(self, path: str | List[str] | RDD[str], schema: StructType | str | None = None, primitivesAsString: bool | str | None = None, prefersDecimal: bool | str | None = None, allowComments: bool | str | None = None, allowUnquotedFieldNames: bool | str | None = None, allowSingleQuotes: bool | str | None = None, allowNumericLeadingZero: bool | str | None = None, allowBackslashEscapingAnyCharacter: bool | str | None = None, mode: str | None = None, columnNameOfCorruptRecord: str | None = None, dateFormat: str | None = None, timestampFormat: str | None = None, multiLine: bool | str | None = None, allowUnquotedControlChars: bool | str | None = None, lineSep: str | None = None, samplingRatio: float | str | None = None, dropFieldIfAllNull: bool | str | None = None, encoding: str | None = None, locale: str | None = None, pathGlobFilter: bool | str | None = None, recursiveFileLookup: bool | str | None = None, modifiedBefore: bool | str | None = None, modifiedAfter: bool | str | None = None, allowNonNumericNumbers: bool | str | None = None) -> DataFrame:
        '''
        Loads JSON files and returns the results as a :class:`DataFrame`.

        `JSON Lines <http://jsonlines.org/>`_ (newline-delimited JSON) is supported by default.
        For JSON (one record per file), set the ``multiLine`` parameter to ``true``.

        If the ``schema`` parameter is not specified, this function goes
        through the input once to determine the input schema.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        path : str, list or :class:`RDD`
            string represents path to the JSON dataset, or a list of paths,
            or RDD of Strings storing JSON objects.
        schema : :class:`pyspark.sql.types.StructType` or str, optional
            an optional :class:`pyspark.sql.types.StructType` for the input schema or
            a DDL-formatted string (For example ``col0 INT, col1 DOUBLE``).

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option>`_
            for the version you use.

            .. # noqa

        Examples
        --------
        Write a DataFrame into a JSON file and read it back.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a JSON file
        ...     spark.createDataFrame(
        ...         [{"age": 100, "name": "Hyukjin Kwon"}]
        ...     ).write.mode("overwrite").format("json").save(d)
        ...
        ...     # Read the JSON file as a DataFrame.
        ...     spark.read.json(d).show()
        +---+------------+
        |age|        name|
        +---+------------+
        |100|Hyukjin Kwon|
        +---+------------+
        '''
    def table(self, tableName: str) -> DataFrame:
        '''Returns the specified table as a :class:`DataFrame`.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        tableName : str
            string, name of the table.

        Examples
        --------
        >>> df = spark.range(10)
        >>> df.createOrReplaceTempView(\'tblA\')
        >>> spark.read.table(\'tblA\').show()
        +---+
        | id|
        +---+
        |  0|
        |  1|
        |  2|
        |  3|
        |  4|
        |  5|
        |  6|
        |  7|
        |  8|
        |  9|
        +---+
        >>> _ = spark.sql("DROP TABLE tblA")
        '''
    def parquet(self, *paths: str, **options: OptionalPrimitiveType) -> DataFrame:
        '''
        Loads Parquet files, returning the result as a :class:`DataFrame`.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        paths : str

        Other Parameters
        ----------------
        **options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#data-source-option>`_
            for the version you use.

            .. # noqa

        Examples
        --------
        Write a DataFrame into a Parquet file and read it back.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a Parquet file
        ...     spark.createDataFrame(
        ...         [{"age": 100, "name": "Hyukjin Kwon"}]
        ...     ).write.mode("overwrite").format("parquet").save(d)
        ...
        ...     # Read the Parquet file as a DataFrame.
        ...     spark.read.parquet(d).show()
        +---+------------+
        |age|        name|
        +---+------------+
        |100|Hyukjin Kwon|
        +---+------------+
        '''
    def text(self, paths: PathOrPaths, wholetext: bool = False, lineSep: str | None = None, pathGlobFilter: bool | str | None = None, recursiveFileLookup: bool | str | None = None, modifiedBefore: bool | str | None = None, modifiedAfter: bool | str | None = None) -> DataFrame:
        '''
        Loads text files and returns a :class:`DataFrame` whose schema starts with a
        string column named "value", and followed by partitioned columns if there
        are any.
        The text files must be encoded as UTF-8.

        By default, each line in the text file is a new row in the resulting DataFrame.

        .. versionadded:: 1.6.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        paths : str or list
            string, or list of strings, for input path(s).

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-text.html#data-source-option>`_
            for the version you use.

            .. # noqa

        Examples
        --------
        Write a DataFrame into a text file and read it back.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a text file
        ...     df = spark.createDataFrame([("a",), ("b",), ("c",)], schema=["alphabets"])
        ...     df.write.mode("overwrite").format("text").save(d)
        ...
        ...     # Read the text file as a DataFrame.
        ...     spark.read.schema(df.schema).text(d).sort("alphabets").show()
        +---------+
        |alphabets|
        +---------+
        |        a|
        |        b|
        |        c|
        +---------+
        '''
    def csv(self, path: PathOrPaths, schema: StructType | str | None = None, sep: str | None = None, encoding: str | None = None, quote: str | None = None, escape: str | None = None, comment: str | None = None, header: bool | str | None = None, inferSchema: bool | str | None = None, ignoreLeadingWhiteSpace: bool | str | None = None, ignoreTrailingWhiteSpace: bool | str | None = None, nullValue: str | None = None, nanValue: str | None = None, positiveInf: str | None = None, negativeInf: str | None = None, dateFormat: str | None = None, timestampFormat: str | None = None, maxColumns: int | str | None = None, maxCharsPerColumn: int | str | None = None, maxMalformedLogPerPartition: int | str | None = None, mode: str | None = None, columnNameOfCorruptRecord: str | None = None, multiLine: bool | str | None = None, charToEscapeQuoteEscaping: str | None = None, samplingRatio: float | str | None = None, enforceSchema: bool | str | None = None, emptyValue: str | None = None, locale: str | None = None, lineSep: str | None = None, pathGlobFilter: bool | str | None = None, recursiveFileLookup: bool | str | None = None, modifiedBefore: bool | str | None = None, modifiedAfter: bool | str | None = None, unescapedQuoteHandling: str | None = None) -> DataFrame:
        '''Loads a CSV file and returns the result as a  :class:`DataFrame`.

        This function will go through the input once to determine the input schema if
        ``inferSchema`` is enabled. To avoid going through the entire data once, disable
        ``inferSchema`` option or specify the schema explicitly using ``schema``.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        path : str or list
            string, or list of strings, for input path(s),
            or RDD of Strings storing CSV rows.
        schema : :class:`pyspark.sql.types.StructType` or str, optional
            an optional :class:`pyspark.sql.types.StructType` for the input schema
            or a DDL-formatted string (For example ``col0 INT, col1 DOUBLE``).

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option>`_
            for the version you use.

            .. # noqa

        Examples
        --------
        Write a DataFrame into a CSV file and read it back.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a CSV file
        ...     df = spark.createDataFrame([{"age": 100, "name": "Hyukjin Kwon"}])
        ...     df.write.mode("overwrite").format("csv").save(d)
        ...
        ...     # Read the CSV file as a DataFrame with \'nullValue\' option set to \'Hyukjin Kwon\'.
        ...     spark.read.csv(d, schema=df.schema, nullValue="Hyukjin Kwon").show()
        +---+----+
        |age|name|
        +---+----+
        |100|null|
        +---+----+
        '''
    def orc(self, path: PathOrPaths, mergeSchema: bool | None = None, pathGlobFilter: bool | str | None = None, recursiveFileLookup: bool | str | None = None, modifiedBefore: bool | str | None = None, modifiedAfter: bool | str | None = None) -> DataFrame:
        '''Loads ORC files, returning the result as a :class:`DataFrame`.

        .. versionadded:: 1.5.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        path : str or list

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-orc.html#data-source-option>`_
            for the version you use.

            .. # noqa

        Examples
        --------
        Write a DataFrame into a ORC file and read it back.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a ORC file
        ...     spark.createDataFrame(
        ...         [{"age": 100, "name": "Hyukjin Kwon"}]
        ...     ).write.mode("overwrite").format("orc").save(d)
        ...
        ...     # Read the Parquet file as a DataFrame.
        ...     spark.read.orc(d).show()
        +---+------------+
        |age|        name|
        +---+------------+
        |100|Hyukjin Kwon|
        +---+------------+
        '''
    @overload
    def jdbc(self, url: str, table: str, *, properties: Dict[str, str] | None = None) -> DataFrame: ...
    @overload
    def jdbc(self, url: str, table: str, column: str, lowerBound: int | str, upperBound: int | str, numPartitions: int, *, properties: Dict[str, str] | None = None) -> DataFrame: ...
    @overload
    def jdbc(self, url: str, table: str, *, predicates: List[str], properties: Dict[str, str] | None = None) -> DataFrame: ...

class DataFrameWriter(OptionUtils):
    """
    Interface used to write a :class:`DataFrame` to external storage systems
    (e.g. file systems, key-value stores, etc). Use :attr:`DataFrame.write`
    to access this.

    .. versionadded:: 1.4.0

    .. versionchanged:: 3.4.0
        Supports Spark Connect.
    """
    def __init__(self, df: DataFrame) -> None: ...
    def mode(self, saveMode: str | None) -> DataFrameWriter:
        '''Specifies the behavior when data or table already exists.

        Options include:

        * `append`: Append contents of this :class:`DataFrame` to existing data.
        * `overwrite`: Overwrite existing data.
        * `error` or `errorifexists`: Throw an exception if data already exists.
        * `ignore`: Silently ignore this operation if data already exists.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Examples
        --------
        Raise an error when writing to an existing path.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     spark.createDataFrame(
        ...         [{"age": 80, "name": "Xinrong Meng"}]
        ...     ).write.mode("error").format("parquet").save(d) # doctest: +SKIP
        Traceback (most recent call last):
            ...
        ...AnalysisException: ...

        Write a Parquet file back with various options, and read it back.

        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Overwrite the path with a new Parquet file
        ...     spark.createDataFrame(
        ...         [{"age": 100, "name": "Hyukjin Kwon"}]
        ...     ).write.mode("overwrite").format("parquet").save(d)
        ...
        ...     # Append another DataFrame into the Parquet file
        ...     spark.createDataFrame(
        ...         [{"age": 120, "name": "Takuya Ueshin"}]
        ...     ).write.mode("append").format("parquet").save(d)
        ...
        ...     # Append another DataFrame into the Parquet file
        ...     spark.createDataFrame(
        ...         [{"age": 140, "name": "Haejoon Lee"}]
        ...     ).write.mode("ignore").format("parquet").save(d)
        ...
        ...     # Read the Parquet file as a DataFrame.
        ...     spark.read.parquet(d).show()
        +---+-------------+
        |age|         name|
        +---+-------------+
        |120|Takuya Ueshin|
        |100| Hyukjin Kwon|
        +---+-------------+
        '''
    def format(self, source: str) -> DataFrameWriter:
        '''Specifies the underlying output data source.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        source : str
            string, name of the data source, e.g. \'json\', \'parquet\'.

        Examples
        --------
        >>> spark.range(1).write.format(\'parquet\')
        <...readwriter.DataFrameWriter object ...>

        Write a DataFrame into a Parquet file and read it back.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a Parquet file
        ...     spark.createDataFrame(
        ...         [{"age": 100, "name": "Hyukjin Kwon"}]
        ...     ).write.mode("overwrite").format("parquet").save(d)
        ...
        ...     # Read the Parquet file as a DataFrame.
        ...     spark.read.format(\'parquet\').load(d).show()
        +---+------------+
        |age|        name|
        +---+------------+
        |100|Hyukjin Kwon|
        +---+------------+
        '''
    def option(self, key: str, value: OptionalPrimitiveType) -> DataFrameWriter:
        '''
        Adds an output option for the underlying data source.

        .. versionadded:: 1.5.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        key : str
            The key for the option to set.
        value
            The value for the option to set.

        Examples
        --------
        >>> spark.range(1).write.option("key", "value")
        <...readwriter.DataFrameWriter object ...>

        Specify the option \'nullValue\' with writing a CSV file.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a CSV file with \'nullValue\' option set to \'Hyukjin Kwon\'.
        ...     df = spark.createDataFrame([(100, None)], "age INT, name STRING")
        ...     df.write.option("nullValue", "Hyukjin Kwon").mode("overwrite").format("csv").save(d)
        ...
        ...     # Read the CSV file as a DataFrame.
        ...     spark.read.schema(df.schema).format(\'csv\').load(d).show()
        +---+------------+
        |age|        name|
        +---+------------+
        |100|Hyukjin Kwon|
        +---+------------+
        '''
    def options(self, **options: OptionalPrimitiveType) -> DataFrameWriter:
        '''
        Adds output options for the underlying data source.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        **options : dict
            The dictionary of string keys and primitive-type values.

        Examples
        --------
        >>> spark.range(1).write.option("key", "value")
        <...readwriter.DataFrameWriter object ...>

        Specify the option \'nullValue\' and \'header\' with writing a CSV file.

        >>> from pyspark.sql.types import StructType,StructField, StringType, IntegerType
        >>> schema = StructType([
        ...     StructField("age",IntegerType(),True),
        ...     StructField("name",StringType(),True),
        ... ])
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a CSV file with \'nullValue\' option set to \'Hyukjin Kwon\',
        ...     # and \'header\' option set to `True`.
        ...     df = spark.createDataFrame([(100, None)], schema=schema)
        ...     df.write.options(nullValue="Hyukjin Kwon", header=True).mode(
        ...         "overwrite").format("csv").save(d)
        ...
        ...     # Read the CSV file as a DataFrame.
        ...     spark.read.option("header", True).format(\'csv\').load(d).show()
        +---+------------+
        |age|        name|
        +---+------------+
        |100|Hyukjin Kwon|
        +---+------------+
        '''
    @overload
    def partitionBy(self, *cols: str) -> DataFrameWriter: ...
    @overload
    def partitionBy(self, *cols: List[str]) -> DataFrameWriter: ...
    @overload
    def bucketBy(self, numBuckets: int, col: str, *cols: str) -> DataFrameWriter: ...
    @overload
    def bucketBy(self, numBuckets: int, col: TupleOrListOfString) -> DataFrameWriter: ...
    @overload
    def sortBy(self, col: str, *cols: str) -> DataFrameWriter: ...
    @overload
    def sortBy(self, col: TupleOrListOfString) -> DataFrameWriter: ...
    def save(self, path: str | None = None, format: str | None = None, mode: str | None = None, partitionBy: str | List[str] | None = None, **options: OptionalPrimitiveType) -> None:
        '''Saves the contents of the :class:`DataFrame` to a data source.

        The data source is specified by the ``format`` and a set of ``options``.
        If ``format`` is not specified, the default data source configured by
        ``spark.sql.sources.default`` will be used.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        path : str, optional
            the path in a Hadoop supported file system
        format : str, optional
            the format used to save
        mode : str, optional
            specifies the behavior of the save operation when data already exists.

            * ``append``: Append contents of this :class:`DataFrame` to existing data.
            * ``overwrite``: Overwrite existing data.
            * ``ignore``: Silently ignore this operation if data already exists.
            * ``error`` or ``errorifexists`` (default case): Throw an exception if data already                 exists.
        partitionBy : list, optional
            names of partitioning columns
        **options : dict
            all other string options

        Examples
        --------
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
    def insertInto(self, tableName: str, overwrite: bool | None = None) -> None:
        '''Inserts the content of the :class:`DataFrame` to the specified table.

        It requires that the schema of the :class:`DataFrame` is the same as the
        schema of the table.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        overwrite : bool, optional
            If true, overwrites existing data. Disabled by default

        Notes
        -----
        Unlike :meth:`DataFrameWriter.saveAsTable`, :meth:`DataFrameWriter.insertInto` ignores
        the column names and just uses position-based resolution.

        Examples
        --------
        >>> _ = spark.sql("DROP TABLE IF EXISTS tblA")
        >>> df = spark.createDataFrame([
        ...     (100, "Hyukjin Kwon"), (120, "Hyukjin Kwon"), (140, "Haejoon Lee")],
        ...     schema=["age", "name"]
        ... )
        >>> df.write.saveAsTable("tblA")

        Insert the data into \'tblA\' table but with different column names.

        >>> df.selectExpr("age AS col1", "name AS col2").write.insertInto("tblA")
        >>> spark.read.table("tblA").sort("age").show()
        +---+------------+
        |age|        name|
        +---+------------+
        |100|Hyukjin Kwon|
        |100|Hyukjin Kwon|
        |120|Hyukjin Kwon|
        |120|Hyukjin Kwon|
        |140| Haejoon Lee|
        |140| Haejoon Lee|
        +---+------------+
        >>> _ = spark.sql("DROP TABLE tblA")
        '''
    def saveAsTable(self, name: str, format: str | None = None, mode: str | None = None, partitionBy: str | List[str] | None = None, **options: OptionalPrimitiveType) -> None:
        '''Saves the content of the :class:`DataFrame` as the specified table.

        In the case the table already exists, behavior of this function depends on the
        save mode, specified by the `mode` function (default to throwing an exception).
        When `mode` is `Overwrite`, the schema of the :class:`DataFrame` does not need to be
        the same as that of the existing table.

        * `append`: Append contents of this :class:`DataFrame` to existing data.
        * `overwrite`: Overwrite existing data.
        * `error` or `errorifexists`: Throw an exception if data already exists.
        * `ignore`: Silently ignore this operation if data already exists.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Notes
        -----
        When `mode` is `Append`, if there is an existing table, we will use the format and
        options of the existing table. The column order in the schema of the :class:`DataFrame`
        doesn\'t need to be the same as that of the existing table. Unlike
        :meth:`DataFrameWriter.insertInto`, :meth:`DataFrameWriter.saveAsTable` will use the
        column names to find the correct column positions.

        Parameters
        ----------
        name : str
            the table name
        format : str, optional
            the format used to save
        mode : str, optional
            one of `append`, `overwrite`, `error`, `errorifexists`, `ignore`             (default: error)
        partitionBy : str or list
            names of partitioning columns
        **options : dict
            all other string options

        Examples
        --------
        Creates a table from a DataFrame, and read it back.

        >>> _ = spark.sql("DROP TABLE IF EXISTS tblA")
        >>> spark.createDataFrame([
        ...     (100, "Hyukjin Kwon"), (120, "Hyukjin Kwon"), (140, "Haejoon Lee")],
        ...     schema=["age", "name"]
        ... ).write.saveAsTable("tblA")
        >>> spark.read.table("tblA").sort("age").show()
        +---+------------+
        |age|        name|
        +---+------------+
        |100|Hyukjin Kwon|
        |120|Hyukjin Kwon|
        |140| Haejoon Lee|
        +---+------------+
        >>> _ = spark.sql("DROP TABLE tblA")
        '''
    def json(self, path: str, mode: str | None = None, compression: str | None = None, dateFormat: str | None = None, timestampFormat: str | None = None, lineSep: str | None = None, encoding: str | None = None, ignoreNullFields: bool | str | None = None) -> None:
        '''Saves the content of the :class:`DataFrame` in JSON format
        (`JSON Lines text format or newline-delimited JSON <http://jsonlines.org/>`_) at the
        specified path.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        path : str
            the path in any Hadoop supported file system
        mode : str, optional
            specifies the behavior of the save operation when data already exists.

            * ``append``: Append contents of this :class:`DataFrame` to existing data.
            * ``overwrite``: Overwrite existing data.
            * ``ignore``: Silently ignore this operation if data already exists.
            * ``error`` or ``errorifexists`` (default case): Throw an exception if data already                 exists.

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option>`_
            for the version you use.

            .. # noqa

        Examples
        --------
        Write a DataFrame into a JSON file and read it back.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a JSON file
        ...     spark.createDataFrame(
        ...         [{"age": 100, "name": "Hyukjin Kwon"}]
        ...     ).write.json(d, mode="overwrite")
        ...
        ...     # Read the JSON file as a DataFrame.
        ...     spark.read.format("json").load(d).show()
        +---+------------+
        |age|        name|
        +---+------------+
        |100|Hyukjin Kwon|
        +---+------------+
        '''
    def parquet(self, path: str, mode: str | None = None, partitionBy: str | List[str] | None = None, compression: str | None = None) -> None:
        '''Saves the content of the :class:`DataFrame` in Parquet format at the specified path.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        path : str
            the path in any Hadoop supported file system
        mode : str, optional
            specifies the behavior of the save operation when data already exists.

            * ``append``: Append contents of this :class:`DataFrame` to existing data.
            * ``overwrite``: Overwrite existing data.
            * ``ignore``: Silently ignore this operation if data already exists.
            * ``error`` or ``errorifexists`` (default case): Throw an exception if data already                 exists.
        partitionBy : str or list, optional
            names of partitioning columns

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#data-source-option>`_
            for the version you use.

            .. # noqa

        Examples
        --------
        Write a DataFrame into a Parquet file and read it back.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a Parquet file
        ...     spark.createDataFrame(
        ...         [{"age": 100, "name": "Hyukjin Kwon"}]
        ...     ).write.parquet(d, mode="overwrite")
        ...
        ...     # Read the Parquet file as a DataFrame.
        ...     spark.read.format("parquet").load(d).show()
        +---+------------+
        |age|        name|
        +---+------------+
        |100|Hyukjin Kwon|
        +---+------------+
        '''
    def text(self, path: str, compression: str | None = None, lineSep: str | None = None) -> None:
        '''Saves the content of the DataFrame in a text file at the specified path.
        The text files will be encoded as UTF-8.

        .. versionadded:: 1.6.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        path : str
            the path in any Hadoop supported file system

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-text.html#data-source-option>`_
            for the version you use.

            .. # noqa

        Notes
        -----
        The DataFrame must have only one column that is of string type.
        Each row becomes a new line in the output file.

        Examples
        --------
        Write a DataFrame into a text file and read it back.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a text file
        ...     df = spark.createDataFrame([("a",), ("b",), ("c",)], schema=["alphabets"])
        ...     df.write.mode("overwrite").text(d)
        ...
        ...     # Read the text file as a DataFrame.
        ...     spark.read.schema(df.schema).format("text").load(d).sort("alphabets").show()
        +---------+
        |alphabets|
        +---------+
        |        a|
        |        b|
        |        c|
        +---------+
        '''
    def csv(self, path: str, mode: str | None = None, compression: str | None = None, sep: str | None = None, quote: str | None = None, escape: str | None = None, header: bool | str | None = None, nullValue: str | None = None, escapeQuotes: bool | str | None = None, quoteAll: bool | str | None = None, dateFormat: str | None = None, timestampFormat: str | None = None, ignoreLeadingWhiteSpace: bool | str | None = None, ignoreTrailingWhiteSpace: bool | str | None = None, charToEscapeQuoteEscaping: str | None = None, encoding: str | None = None, emptyValue: str | None = None, lineSep: str | None = None) -> None:
        '''Saves the content of the :class:`DataFrame` in CSV format at the specified path.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        path : str
            the path in any Hadoop supported file system
        mode : str, optional
            specifies the behavior of the save operation when data already exists.

            * ``append``: Append contents of this :class:`DataFrame` to existing data.
            * ``overwrite``: Overwrite existing data.
            * ``ignore``: Silently ignore this operation if data already exists.
            * ``error`` or ``errorifexists`` (default case): Throw an exception if data already \\\n                exists.

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option>`_
            for the version you use.

            .. # noqa

        Examples
        --------
        Write a DataFrame into a CSV file and read it back.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a CSV file
        ...     df = spark.createDataFrame([{"age": 100, "name": "Hyukjin Kwon"}])
        ...     df.write.csv(d, mode="overwrite")
        ...
        ...     # Read the CSV file as a DataFrame with \'nullValue\' option set to \'Hyukjin Kwon\'.
        ...     spark.read.schema(df.schema).format("csv").option(
        ...         "nullValue", "Hyukjin Kwon").load(d).show()
        +---+----+
        |age|name|
        +---+----+
        |100|null|
        +---+----+
        '''
    def orc(self, path: str, mode: str | None = None, partitionBy: str | List[str] | None = None, compression: str | None = None) -> None:
        '''Saves the content of the :class:`DataFrame` in ORC format at the specified path.

        .. versionadded:: 1.5.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        path : str
            the path in any Hadoop supported file system
        mode : str, optional
            specifies the behavior of the save operation when data already exists.

            * ``append``: Append contents of this :class:`DataFrame` to existing data.
            * ``overwrite``: Overwrite existing data.
            * ``ignore``: Silently ignore this operation if data already exists.
            * ``error`` or ``errorifexists`` (default case): Throw an exception if data already                 exists.
        partitionBy : str or list, optional
            names of partitioning columns

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-orc.html#data-source-option>`_
            for the version you use.

            .. # noqa

        Examples
        --------
        Write a DataFrame into a ORC file and read it back.

        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a DataFrame into a ORC file
        ...     spark.createDataFrame(
        ...         [{"age": 100, "name": "Hyukjin Kwon"}]
        ...     ).write.orc(d, mode="overwrite")
        ...
        ...     # Read the Parquet file as a DataFrame.
        ...     spark.read.format("orc").load(d).show()
        +---+------------+
        |age|        name|
        +---+------------+
        |100|Hyukjin Kwon|
        +---+------------+
        '''
    def jdbc(self, url: str, table: str, mode: str | None = None, properties: Dict[str, str] | None = None) -> None:
        '''Saves the content of the :class:`DataFrame` to an external database table via JDBC.

        .. versionadded:: 1.4.0

        .. versionchanged:: 3.4.0
            Supports Spark Connect.

        Parameters
        ----------
        table : str
            Name of the table in the external database.
        mode : str, optional
            specifies the behavior of the save operation when data already exists.

            * ``append``: Append contents of this :class:`DataFrame` to existing data.
            * ``overwrite``: Overwrite existing data.
            * ``ignore``: Silently ignore this operation if data already exists.
            * ``error`` or ``errorifexists`` (default case): Throw an exception if data already                 exists.
        properties : dict
            a dictionary of JDBC database connection arguments. Normally at
            least properties "user" and "password" with their corresponding values.
            For example { \'user\' : \'SYSTEM\', \'password\' : \'mypassword\' }

        Other Parameters
        ----------------
        Extra options
            For the extra options, refer to
            `Data Source Option <https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html#data-source-option>`_
            for the version you use.

            .. # noqa

        Notes
        -----
        Don\'t create too many partitions in parallel on a large cluster;
        otherwise Spark might crash your external database systems.
        '''

class DataFrameWriterV2:
    """
    Interface used to write a class:`pyspark.sql.dataframe.DataFrame`
    to external storage using the v2 API.

    .. versionadded:: 3.1.0

    .. versionchanged:: 3.4.0
        Supports Spark Connect.
    """
    def __init__(self, df: DataFrame, table: str) -> None: ...
    def using(self, provider: str) -> DataFrameWriterV2:
        '''
        Specifies a provider for the underlying output data source.
        Spark\'s default catalog supports "parquet", "json", etc.
        '''
    def option(self, key: str, value: OptionalPrimitiveType) -> DataFrameWriterV2:
        """
        Add a write option.
        """
    def options(self, **options: OptionalPrimitiveType) -> DataFrameWriterV2:
        """
        Add write options.
        """
    def tableProperty(self, property: str, value: str) -> DataFrameWriterV2:
        """
        Add table property.
        """
    def partitionedBy(self, col: Column, *cols: Column) -> DataFrameWriterV2:
        """
        Partition the output table created by `create`, `createOrReplace`, or `replace` using
        the given columns or transforms.

        When specified, the table data will be stored by these values for efficient reads.

        For example, when a table is partitioned by day, it may be stored
        in a directory layout like:

        * `table/day=2019-06-01/`
        * `table/day=2019-06-02/`

        Partitioning is one of the most widely used techniques to optimize physical data layout.
        It provides a coarse-grained index for skipping unnecessary data reads when queries have
        predicates on the partitioned columns. In order for partitioning to work well, the number
        of distinct values in each column should typically be less than tens of thousands.

        `col` and `cols` support only the following functions:

        * :py:func:`pyspark.sql.functions.years`
        * :py:func:`pyspark.sql.functions.months`
        * :py:func:`pyspark.sql.functions.days`
        * :py:func:`pyspark.sql.functions.hours`
        * :py:func:`pyspark.sql.functions.bucket`

        """
    def create(self) -> None:
        """
        Create a new table from the contents of the data frame.

        The new table's schema, partition layout, properties, and other configuration will be
        based on the configuration set on this writer.
        """
    def replace(self) -> None:
        """
        Replace an existing table with the contents of the data frame.

        The existing table's schema, partition layout, properties, and other configuration will be
        replaced with the contents of the data frame and the configuration set on this writer.
        """
    def createOrReplace(self) -> None:
        """
        Create a new table or replace an existing table with the contents of the data frame.

        The output table's schema, partition layout, properties,
        and other configuration will be based on the contents of the data frame
        and the configuration set on this writer.
        If the table exists, its configuration and data will be replaced.
        """
    def append(self) -> None:
        """
        Append the contents of the data frame to the output table.
        """
    def overwrite(self, condition: Column) -> None:
        """
        Overwrite rows matching the given filter condition with the contents of the data frame in
        the output table.
        """
    def overwritePartitions(self) -> None:
        """
        Overwrite all partition for which the data frame contains at least one row with the contents
        of the data frame in the output table.

        This operation is equivalent to Hive's `INSERT OVERWRITE ... PARTITION`, which replaces
        partitions dynamically depending on the contents of the data frame.
        """
