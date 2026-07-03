from delta._typing import ColumnMapping as ColumnMapping, ExpressionOrColumn as ExpressionOrColumn, OptionalColumnMapping as OptionalColumnMapping, OptionalExpressionOrColumn as OptionalExpressionOrColumn
from py4j.java_collections import JavaMap as JavaMap
from py4j.java_gateway import JVMView as JVMView, JavaObject as JavaObject
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import DataType, StructField, StructType
from typing import Any, Dict, List, Optional, Tuple, Union, overload

class DeltaTable:
    '''
        Main class for programmatically interacting with Delta tables.
        You can create DeltaTable instances using the path of the Delta table.::

            deltaTable = DeltaTable.forPath(spark, "/path/to/table")

        In addition, you can convert an existing Parquet table in place into a Delta table.::

            deltaTable = DeltaTable.convertToDelta(spark, "parquet.`/path/to/table`")

        .. versionadded:: 0.4
    '''
    def __init__(self, spark: SparkSession, jdt: JavaObject) -> None: ...
    def toDF(self) -> DataFrame:
        """
        Get a DataFrame representation of this Delta table.
        """
    def alias(self, aliasName: str) -> DeltaTable:
        """
        Apply an alias to the Delta table.
        """
    def generate(self, mode: str) -> None:
        '''
        Generate manifest files for the given delta table.

        :param mode: mode for the type of manifest file to be generated
                     The valid modes are as follows (not case sensitive):

                     - "symlink_format_manifest": This will generate manifests in symlink format
                                                  for Presto and Athena read support.

                     See the online documentation for more information.
        '''
    def delete(self, condition: OptionalExpressionOrColumn = ...) -> None:
        '''
        Delete data from the table that match the given ``condition``.

        Example::

            deltaTable.delete("date < \'2017-01-01\'")        # predicate using SQL formatted string

            deltaTable.delete(col("date") < "2017-01-01")   # predicate using Spark SQL functions

        :param condition: condition of the update
        :type condition: str or pyspark.sql.Column
        '''
    @overload
    def update(self, condition: ExpressionOrColumn, set: ColumnMapping) -> None: ...
    @overload
    def update(self, *, set: ColumnMapping) -> None: ...
    def merge(self, source: DataFrame, condition: ExpressionOrColumn) -> DeltaMergeBuilder:
        '''
        Merge data from the `source` DataFrame based on the given merge `condition`. This returns
        a :class:`DeltaMergeBuilder` object that can be used to specify the update, delete, or
        insert actions to be performed on rows based on whether the rows matched the condition or
        not. See :class:`DeltaMergeBuilder` for a full description of this operation and what
        combinations of update, delete and insert operations are allowed.

        Example 1 with conditions and update expressions as SQL formatted string::

            deltaTable.alias("events").merge(
                source = updatesDF.alias("updates"),
                condition = "events.eventId = updates.eventId"
              ).whenMatchedUpdate(set =
                {
                  "data": "updates.data",
                  "count": "events.count + 1"
                }
              ).whenNotMatchedInsert(values =
                {
                  "date": "updates.date",
                  "eventId": "updates.eventId",
                  "data": "updates.data",
                  "count": "1"
                }
              ).execute()

        Example 2 with conditions and update expressions as Spark SQL functions::

            from pyspark.sql.functions import *

            deltaTable.alias("events").merge(
                source = updatesDF.alias("updates"),
                condition = expr("events.eventId = updates.eventId")
              ).whenMatchedUpdate(set =
                {
                  "data" : col("updates.data"),
                  "count": col("events.count") + 1
                }
              ).whenNotMatchedInsert(values =
                {
                  "date": col("updates.date"),
                  "eventId": col("updates.eventId"),
                  "data": col("updates.data"),
                  "count": lit("1")
                }
              ).execute()

        :param source: Source DataFrame
        :type source: pyspark.sql.DataFrame
        :param condition: Condition to match sources rows with the Delta table rows.
        :type condition: str or pyspark.sql.Column

        :return: builder object to specify whether to update, delete or insert rows based on
                 whether the condition matched or not
        :rtype: :py:class:`delta.tables.DeltaMergeBuilder`
        '''
    def vacuum(self, retentionHours: Optional[float] = ..., subDirs: Any = ..., dryRun: bool = ...) -> DataFrame:
        """
        Recursively delete files and directories in the table that are not needed by the table for
        maintaining older versions up to the given retention threshold. This method will return an
        empty DataFrame on successful completion. If subDirs are given, delete only under
        the directories.

        Example::

            deltaTable.vacuum()     # vacuum files not required by versions more than 7 days old

            deltaTable.vacuum(100)  # vacuum files not required by versions more than 100 hours old

            deltaTable.vacuum(['YM=202201']) # vacuum files under tableLocation/YM=202201,
                                             #   not required by versions more than 7 days old

        :param retentionHours: Optional number of hours retain history. If not specified, then the
                               default retention period of 168 hours (7 days) will be used.
        """
    def history(self, limit: Optional[int] = ...) -> DataFrame:
        """
        Get the information of the latest `limit` commits on this table as a Spark DataFrame.
        The information is in reverse chronological order.

        Example::

            fullHistoryDF = deltaTable.history()    # get the full history of the table

            lastOperationDF = deltaTable.history(1) # get the last operation

        :param limit: Optional, number of latest commits to returns in the history.
        :return: Table's commit history. See the online Delta Lake documentation for more details.
        :rtype: pyspark.sql.DataFrame
        """
    def detail(self) -> DataFrame:
        """
        Get the details of a Delta table such as the format, name, and size.

        Example::

            detailDF = deltaTable.detail() # get the full details of the table

        :return Information of the table (format, name, size, etc.)
        :rtype: pyspark.sql.DataFrame

        .. note:: Evolving
        """
    @classmethod
    def convertToDelta(cls, sparkSession: SparkSession, identifier: str, partitionSchema: Optional[Union[str, StructType]] = ...) -> DeltaTable:
        '''
        Create a DeltaTable from the given parquet table. Takes an existing parquet table and
        constructs a delta transaction log in the base path of the table.
        Note: Any changes to the table during the conversion process may not result in a consistent
        state at the end of the conversion. Users should stop any changes to the table before the
        conversion is started.

        Example::

            # Convert unpartitioned parquet table at path \'path/to/table\'
            deltaTable = DeltaTable.convertToDelta(
                spark, "parquet.`path/to/table`")

            # Convert partitioned parquet table at path \'path/to/table\' and partitioned by
            # integer column named \'part\'
            partitionedDeltaTable = DeltaTable.convertToDelta(
                spark, "parquet.`path/to/table`", "part int")

        :param sparkSession: SparkSession to use for the conversion
        :type sparkSession: pyspark.sql.SparkSession
        :param identifier: Parquet table identifier formatted as "parquet.`path`"
        :type identifier: str
        :param partitionSchema: Hive DDL formatted string, or pyspark.sql.types.StructType
        :return: DeltaTable representing the converted Delta table
        :rtype: :py:class:`~delta.tables.DeltaTable`
        '''
    @classmethod
    def forPath(cls, sparkSession: SparkSession, path: str, hadoopConf: Dict[str, str] = ...) -> DeltaTable:
        '''
        Instantiate a :class:`DeltaTable` object representing the data at the given path,
        If the given path is invalid (i.e. either no table exists or an existing table is
        not a Delta table), it throws a `not a Delta table` error.

        :param sparkSession: SparkSession to use for loading the table
        :type sparkSession: pyspark.sql.SparkSession
        :param hadoopConf: Hadoop configuration starting with "fs." or "dfs." will be picked
                           up by `DeltaTable` to access the file system when executing queries.
                           Other configurations will not be allowed.
        :type hadoopConf: optional dict with str as key and str as value.
        :return: loaded Delta table
        :rtype: :py:class:`~delta.tables.DeltaTable`

        Example::

            hadoopConf = {"fs.s3a.access.key" : "<access-key>",
                       "fs.s3a.secret.key": "secret-key"}
            deltaTable = DeltaTable.forPath(
                           spark,
                           "/path/to/table",
                           hadoopConf)
        '''
    @classmethod
    def forName(cls, sparkSession: SparkSession, tableOrViewName: str) -> DeltaTable:
        '''
        Instantiate a :class:`DeltaTable` object using the given table or view name. If the given
        tableOrViewName is invalid (i.e. either no table exists or an existing table is not a
        Delta table), it throws a `not a Delta table` error.

        The given tableOrViewName can also be the absolute path of a delta datasource (i.e.
        delta.`path`), If so, instantiate a :class:`DeltaTable` object representing the data at
        the given path (consistent with the `forPath`).

        :param sparkSession: SparkSession to use for loading the table
        :param tableOrViewName: name of the table or view
        :return: loaded Delta table
        :rtype: :py:class:`~delta.tables.DeltaTable`

        Example::

            deltaTable = DeltaTable.forName(spark, "tblName")
        '''
    @classmethod
    def create(cls, sparkSession: Optional[SparkSession] = ...) -> DeltaTableBuilder:
        """
        Return :class:`DeltaTableBuilder` object that can be used to specify
        the table name, location, columns, partitioning columns, table comment,
        and table properties to create a Delta table, error if the table exists
        (the same as SQL `CREATE TABLE`).

        See :class:`DeltaTableBuilder` for a full description and examples
        of this operation.

        :param sparkSession: SparkSession to use for creating the table
        :return: an instance of DeltaTableBuilder
        :rtype: :py:class:`~delta.tables.DeltaTableBuilder`

        .. note:: Evolving
        """
    @classmethod
    def createIfNotExists(cls, sparkSession: Optional[SparkSession] = ...) -> DeltaTableBuilder:
        """
        Return :class:`DeltaTableBuilder` object that can be used to specify
        the table name, location, columns, partitioning columns, table comment,
        and table properties to create a Delta table,
        if it does not exists (the same as SQL `CREATE TABLE IF NOT EXISTS`).

        See :class:`DeltaTableBuilder` for a full description and examples
        of this operation.

        :param sparkSession: SparkSession to use for creating the table
        :return: an instance of DeltaTableBuilder
        :rtype: :py:class:`~delta.tables.DeltaTableBuilder`

        .. note:: Evolving
        """
    @classmethod
    def replace(cls, sparkSession: Optional[SparkSession] = ...) -> DeltaTableBuilder:
        """
        Return :class:`DeltaTableBuilder` object that can be used to specify
        the table name, location, columns, partitioning columns, table comment,
        and table properties to replace a Delta table,
        error if the table doesn't exist (the same as SQL `REPLACE TABLE`).

        See :class:`DeltaTableBuilder` for a full description and examples
        of this operation.

        :param sparkSession: SparkSession to use for creating the table
        :return: an instance of DeltaTableBuilder
        :rtype: :py:class:`~delta.tables.DeltaTableBuilder`

        .. note:: Evolving
        """
    @classmethod
    def createOrReplace(cls, sparkSession: Optional[SparkSession] = ...) -> DeltaTableBuilder:
        """
        Return :class:`DeltaTableBuilder` object that can be used to specify
        the table name, location, columns, partitioning columns, table comment,
        and table properties replace a Delta table,
        error if the table doesn't exist (the same as SQL `REPLACE TABLE`).

        See :class:`DeltaTableBuilder` for a full description and examples
        of this operation.

        :param sparkSession: SparkSession to use for creating the table
        :return: an instance of DeltaTableBuilder
        :rtype: :py:class:`~delta.tables.DeltaTableBuilder`

        .. note:: Evolving
        """
    @classmethod
    def isDeltaTable(cls, sparkSession: SparkSession, identifier: str) -> bool:
        '''
        Check if the provided `identifier` string, in this case a file path,
        is the root of a Delta table using the given SparkSession.

        :param sparkSession: SparkSession to use to perform the check
        :param path: location of the table
        :return: If the table is a delta table or not
        :rtype: bool

        Example::

            DeltaTable.isDeltaTable(spark, "/path/to/table")
        '''
    def upgradeTableProtocol(self, readerVersion: int, writerVersion: int) -> None:
        """
        Updates the protocol version of the table to leverage new features. Upgrading the reader
        version will prevent all clients that have an older version of Delta Lake from accessing
        this table. Upgrading the writer version will prevent older versions of Delta Lake to write
        to this table. The reader or writer version cannot be downgraded.

        See online documentation and Delta's protocol specification at PROTOCOL.md for more details.
        """
    def restoreToVersion(self, version: int) -> DataFrame:
        """
        Restore the DeltaTable to an older version of the table specified by version number.

        Example::

            io.delta.tables.DeltaTable.restoreToVersion(1)

        :param version: target version of restored table
        :return: Dataframe with metrics of restore operation.
        :rtype: pyspark.sql.DataFrame
        """
    def restoreToTimestamp(self, timestamp: str) -> DataFrame:
        """
        Restore the DeltaTable to an older version of the table specified by a timestamp.
        Timestamp can be of the format yyyy-MM-dd or yyyy-MM-dd HH:mm:ss

        Example::

            io.delta.tables.DeltaTable.restoreToTimestamp('2021-01-01')
            io.delta.tables.DeltaTable.restoreToTimestamp('2021-01-01 01:01:01')

        :param timestamp: target timestamp of restored table
        :return: Dataframe with metrics of restore operation.
        :rtype: pyspark.sql.DataFrame
        """
    def optimize(self) -> DeltaOptimizeBuilder:
        '''
        Optimize the data layout of the table. This returns
        a :py:class:`~delta.tables.DeltaOptimizeBuilder` object that can
        be used to specify the partition filter to limit the scope of
        optimize and also execute different optimization techniques
        such as file compaction or order data using Z-Order curves.

        See the :py:class:`~delta.tables.DeltaOptimizeBuilder` for a
        full description of this operation.

        Example::

            deltaTable.optimize().where("date=\'2021-11-18\'").executeCompaction()

        :return: an instance of DeltaOptimizeBuilder.
        :rtype: :py:class:`~delta.tables.DeltaOptimizeBuilder`
        '''

class DeltaMergeBuilder:
    '''
    Builder to specify how to merge data from source DataFrame into the target Delta table.
    Use :py:meth:`delta.tables.DeltaTable.merge` to create an object of this class.
    Using this builder, you can specify any number of ``whenMatched``, ``whenNotMatched`` and
    ``whenNotMatchedBySource`` clauses. Here are the constraints on these clauses.

    - Constraints in the ``whenMatched`` clauses:

      - The condition in a ``whenMatched`` clause is optional. However, if there are multiple
        ``whenMatched`` clauses, then only the last one may omit the condition.

      - When there are more than one ``whenMatched`` clauses and there are conditions (or the lack
        of) such that a row satisfies multiple clauses, then the action for the first clause
        satisfied is executed. In other words, the order of the ``whenMatched`` clauses matters.

      - If none of the ``whenMatched`` clauses match a source-target row pair that satisfy
        the merge condition, then the target rows will not be updated or deleted.

      - If you want to update all the columns of the target Delta table with the
        corresponding column of the source DataFrame, then you can use the
        ``whenMatchedUpdateAll()``. This is equivalent to::

            whenMatchedUpdate(set = {
              "col1": "source.col1",
              "col2": "source.col2",
              ...    # for all columns in the delta table
            })

    - Constraints in the ``whenNotMatched`` clauses:

      - The condition in a ``whenNotMatched`` clause is optional. However, if there are
        multiple ``whenNotMatched`` clauses, then only the last one may omit the condition.

      - When there are more than one ``whenNotMatched`` clauses and there are conditions (or the
        lack of) such that a row satisfies multiple clauses, then the action for the first clause
        satisfied is executed. In other words, the order of the ``whenNotMatched`` clauses matters.

      - If no ``whenNotMatched`` clause is present or if it is present but the non-matching source
        row does not satisfy the condition, then the source row is not inserted.

      - If you want to insert all the columns of the target Delta table with the
        corresponding column of the source DataFrame, then you can use
        ``whenNotMatchedInsertAll()``. This is equivalent to::

            whenNotMatchedInsert(values = {
              "col1": "source.col1",
              "col2": "source.col2",
              ...    # for all columns in the delta table
            })

    - Constraints in the ``whenNotMatchedBySource`` clauses:

      - The condition in a ``whenNotMatchedBySource`` clause is optional. However, if there are
        multiple ``whenNotMatchedBySource`` clauses, then only the last ``whenNotMatchedBySource``
        clause may omit the condition.

      - Conditions and update expressions  in ``whenNotMatchedBySource`` clauses may only refer to
        columns from the target Delta table.

      - When there are more than one ``whenNotMatchedBySource`` clauses and there are conditions (or
        the lack of) such that a row satisfies multiple clauses, then the action for the first
        clause satisfied is executed. In other words, the order of the ``whenNotMatchedBySource``
        clauses matters.

      - If no ``whenNotMatchedBySource`` clause is present or if it is present but the
        non-matching target row does not satisfy any of the ``whenNotMatchedBySource`` clause
        condition, then the target row will not be updated or deleted.

    Example 1 with conditions and update expressions as SQL formatted string::

        deltaTable.alias("events").merge(
            source = updatesDF.alias("updates"),
            condition = "events.eventId = updates.eventId"
          ).whenMatchedUpdate(set =
            {
              "data": "updates.data",
              "count": "events.count + 1"
            }
          ).whenNotMatchedInsert(values =
            {
              "date": "updates.date",
              "eventId": "updates.eventId",
              "data": "updates.data",
              "count": "1",
              "missed_count": "0"
            }
          ).whenNotMatchedBySourceUpdate(set =
            {
              "missed_count": "events.missed_count + 1"
            }
          ).execute()

    Example 2 with conditions and update expressions as Spark SQL functions::

        from pyspark.sql.functions import *

        deltaTable.alias("events").merge(
            source = updatesDF.alias("updates"),
            condition = expr("events.eventId = updates.eventId")
          ).whenMatchedUpdate(set =
            {
              "data" : col("updates.data"),
              "count": col("events.count") + 1
            }
          ).whenNotMatchedInsert(values =
            {
              "date": col("updates.date"),
              "eventId": col("updates.eventId"),
              "data": col("updates.data"),
              "count": lit("1"),
              "missed_count": lit("0")
            }
          ).whenNotMatchedBySourceUpdate(set =
            {
              "missed_count": col("events.missed_count") + 1
            }
          ).execute()

    .. versionadded:: 0.4
    '''
    def __init__(self, spark: SparkSession, jbuilder: JavaObject) -> None: ...
    @overload
    def whenMatchedUpdate(self, condition: OptionalExpressionOrColumn, set: ColumnMapping) -> DeltaMergeBuilder: ...
    @overload
    def whenMatchedUpdate(self, *, set: ColumnMapping) -> DeltaMergeBuilder: ...
    def whenMatchedUpdateAll(self, condition: OptionalExpressionOrColumn = ...) -> DeltaMergeBuilder:
        """
        Update all the columns of the matched table row with the values of the  corresponding
        columns in the source row. If a ``condition`` is specified, then it must be
        true for the new row to be updated.

        See :py:class:`~delta.tables.DeltaMergeBuilder` for complete usage details.

        :param condition: Optional condition of the insert
        :type condition: str or pyspark.sql.Column
        :return: this builder
        """
    def whenMatchedDelete(self, condition: OptionalExpressionOrColumn = ...) -> DeltaMergeBuilder:
        """
        Delete a matched row from the table only if the given ``condition`` (if specified) is
        true for the matched row.

        See :py:class:`~delta.tables.DeltaMergeBuilder` for complete usage details.

        :param condition: Optional condition of the delete
        :type condition: str or pyspark.sql.Column
        :return: this builder
        """
    @overload
    def whenNotMatchedInsert(self, condition: ExpressionOrColumn, values: ColumnMapping) -> DeltaMergeBuilder: ...
    @overload
    def whenNotMatchedInsert(self, *, values: ColumnMapping = ...) -> DeltaMergeBuilder: ...
    def whenNotMatchedInsertAll(self, condition: OptionalExpressionOrColumn = ...) -> DeltaMergeBuilder:
        """
        Insert a new target Delta table row by assigning the target columns to the values of the
        corresponding columns in the source row. If a ``condition`` is specified, then it must
        evaluate to true for the new row to be inserted.

        See :py:class:`~delta.tables.DeltaMergeBuilder` for complete usage details.

        :param condition: Optional condition of the insert
        :type condition: str or pyspark.sql.Column
        :return: this builder
        """
    @overload
    def whenNotMatchedBySourceUpdate(self, condition: OptionalExpressionOrColumn, set: ColumnMapping) -> DeltaMergeBuilder: ...
    @overload
    def whenNotMatchedBySourceUpdate(self, *, set: ColumnMapping) -> DeltaMergeBuilder: ...
    def whenNotMatchedBySourceDelete(self, condition: OptionalExpressionOrColumn = ...) -> DeltaMergeBuilder:
        """
        Delete a target row that has no matches in the source from the table only if the given
        ``condition`` (if specified) is true for the target row.

        See :py:class:`~delta.tables.DeltaMergeBuilder` for complete usage details.

        :param condition: Optional condition of the delete
        :type condition: str or pyspark.sql.Column
        :return: this builder
        """
    def execute(self) -> None:
        """
        Execute the merge operation based on the built matched and not matched actions.

        See :py:class:`~delta.tables.DeltaMergeBuilder` for complete usage details.
        """

class DeltaTableBuilder:
    '''
    Builder to specify how to create / replace a Delta table.
    You must specify the table name or the path before executing the builder.
    You can specify the table columns, the partitioning columns,
    the location of the data, the table comment and the property,
    and how you want to create / replace the Delta table.

    After executing the builder, a :py:class:`~delta.tables.DeltaTable`
    object is returned.

    Use :py:meth:`delta.tables.DeltaTable.create`,
    :py:meth:`delta.tables.DeltaTable.createIfNotExists`,
    :py:meth:`delta.tables.DeltaTable.replace`,
    :py:meth:`delta.tables.DeltaTable.createOrReplace` to create an object of this class.

    Example 1 to create a Delta table with separate columns, using the table name::

        deltaTable = DeltaTable.create(sparkSession)
            .tableName("testTable")
            .addColumn("c1", dataType = "INT", nullable = False)
            .addColumn("c2", dataType = IntegerType(), generatedAlwaysAs = "c1 + 1")
            .partitionedBy("c1")
            .execute()

    Example 2 to replace a Delta table with existing columns, using the location::

        df = spark.createDataFrame([(\'a\', 1), (\'b\', 2), (\'c\', 3)], ["key", "value"])

        deltaTable = DeltaTable.replace(sparkSession)
            .tableName("testTable")
            .addColumns(df.schema)
            .execute()

    .. versionadded:: 1.0

    .. note:: Evolving
    '''
    def __init__(self, spark: SparkSession, jbuilder: JavaObject) -> None: ...
    def tableName(self, identifier: str) -> DeltaTableBuilder:
        """
        Specify the table name.
        Optionally qualified with a database name [database_name.] table_name.

        :param identifier: the table name
        :type identifier: str
        :return: this builder

        .. note:: Evolving
        """
    def location(self, location: str) -> DeltaTableBuilder:
        """
        Specify the path to the directory where table data is stored,
        which could be a path on distributed storage.

        :param location: the data stored location
        :type location: str
        :return: this builder

        .. note:: Evolving
        """
    def comment(self, comment: str) -> DeltaTableBuilder:
        """
        Comment to describe the table.

        :param comment: the table comment
        :type comment: str
        :return: this builder

        .. note:: Evolving
        """
    def addColumn(self, colName: str, dataType: Union[str, DataType], nullable: bool = ..., generatedAlwaysAs: Optional[str] = ..., comment: Optional[str] = ...) -> DeltaTableBuilder:
        """
        Specify a column in the table

        :param colName: the column name
        :type colName: str
        :param dataType: the column data type
        :type dataType: str or pyspark.sql.types.DataType
        :param nullable: whether column is nullable
        :type nullable: bool
        :param generatedAlwaysAs: a SQL expression if the column is always generated
                                  as a function of other columns.
                                  See online documentation for details on Generated Columns.
        :type generatedAlwaysAs: str
        :param comment: the column comment
        :type comment: str

        :return: this builder

        .. note:: Evolving
        """
    def addColumns(self, cols: Union[StructType, List[StructField]]) -> DeltaTableBuilder:
        """
        Specify columns in the table using an existing schema

        :param cols: the columns in the existing schema
        :type cols: pyspark.sql.types.StructType
                    or a list of pyspark.sql.types.StructType.

        :return: this builder

        .. note:: Evolving
        """
    @overload
    def partitionedBy(self, *cols: str) -> DeltaTableBuilder: ...
    @overload
    def partitionedBy(self, __cols: Union[List[str], Tuple[str, ...]]) -> DeltaTableBuilder: ...
    def property(self, key: str, value: str) -> DeltaTableBuilder:
        """
        Specify a table property

        :param key: the table property key
        :type value: the table property value

        :return: this builder

        .. note:: Evolving
        """
    def execute(self) -> DeltaTable:
        """
        Execute Table Creation.

        :rtype: :py:class:`~delta.tables.DeltaTable`

        .. note:: Evolving
        """

class DeltaOptimizeBuilder:
    """
    Builder class for constructing OPTIMIZE command and executing.

    Use :py:meth:`delta.tables.DeltaTable.optimize` to create an instance of this class.

    .. versionadded:: 2.0.0
    """
    def __init__(self, spark: SparkSession, jbuilder: JavaObject) -> None: ...
    def where(self, partitionFilter: str) -> DeltaOptimizeBuilder:
        """
        Apply partition filter on this optimize command builder to limit
        the operation on selected partitions.

        :param partitionFilter: The partition filter to apply
        :type partitionFilter: str
        :return: DeltaOptimizeBuilder with partition filter applied
        :rtype: :py:class:`~delta.tables.DeltaOptimizeBuilder`
        """
    def executeCompaction(self, vOrder: bool = ..., dryRun: bool = ...) -> DataFrame:
        """
        Compact the small files in selected partitions.

        :return: DataFrame containing the OPTIMIZE execution metrics
        :rtype: pyspark.sql.DataFrame
        """
    def executeZOrderBy(self, *cols: Union[str, List[str], Tuple[str, ...]]) -> DataFrame:
        """
        Z-Order the data in selected partitions using the given columns.

        :param cols: the Z-Order cols
        :type cols: str or list name of columns

        :return: DataFrame containing the OPTIMIZE execution metrics
        :rtype: pyspark.sql.DataFrame
        """
