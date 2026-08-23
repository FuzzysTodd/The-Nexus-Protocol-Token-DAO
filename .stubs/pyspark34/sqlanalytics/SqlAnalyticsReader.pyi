from pyspark.sql import DataFrame, DataFrameReader as DataFrameReader, SparkSession as SparkSession

def synapsesql(self, table_name: str = '') -> DataFrame:
    '''
     Construct a `DataFrame` representing the database table in Azure Synapse Analytics
     Dedicated SQL pool.

     The `DataFrameReader` instance must have option
     [[com.microsoft.spark.sqlanalytics.utils.Constants]].SERVER. If using SQL authentication
     with options `Constants.USER` and `Constants.PASSWORD`, the `DataFrameReader` instance
     would also require option `Constants.DATA_SOURCE`. This specifies the name of an existing
     [[https://docs.microsoft.com/sql/t-sql/statements/create-external-data-source-transact-sql external data source]],
     whose
     [[https://docs.microsoft.com/sql/t-sql/statements/create-database-scoped-credential-transact-sql database scoped credential]]
     secret is the access key to an Azure Storage Account.

     {{{
         df = spark.read.
          option(Constants.SERVER, "servername.database.windows.net").
          option(Constants.USER, "username").
          option(Constants.PASSWORD, "PlaceHolder123").
          option(Constants.DATA_SOURCE, "datasource").
         synapsesql("databasename.schemaname.tablename")

       df.show()
      }}}

    :param self: DataFrameReader
    :param table_name: str
           Name of the table in the external database in the format "database.schema.table"
    :return: DataFrame
    '''
