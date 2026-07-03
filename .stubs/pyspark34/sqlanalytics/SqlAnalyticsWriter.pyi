def synapsesql(self, table_name: str, table_type: str = 'internal', location: str = None) -> None:
    '''
     Saves the content of the `DataFrame` to an external database table in Azure Synapse
     Analytics Dedicated SQL pool.

     The `DataFrameWriter` instance must have option
     [[com.microsoft.spark.sqlanalytics.utils.Constants]].SERVER. If using SQL authentication
     with options `Constants.USER` and `Constants.PASSWORD`, the `DataFrameWriter` instance
     would also require option `Constants.DATA_SOURCE`. This specifies the name of an existing
     [[https://docs.microsoft.com/sql/t-sql/statements/create-external-data-source-transact-sql external data source]],
     whose
     [[https://docs.microsoft.com/sql/t-sql/statements/create-database-scoped-credential-transact-sql database scoped credential]]
     secret is the access key to an Azure Storage Account.

     {{{
      val df = spark.sql("select * from tmpview")

       df.write.
         option(Constants.SERVER, "servername.database.windows.net").
         option(Constants.USER, "username").
         option(Constants.PASSWORD, "PlaceHolder123").
         option(Constants.DATA_SOURCE, "datasource").
          synapsesql("databasename.schemaname.tablename")
      }}}

    :param self: DataFrameWriter
    :param table_name: Name of the table in the external database in the format "database.schema.table"
    :param table_type: Table type, which can be one of "internal", "external"
    :param location:  the external table location: e.g. "abfss://filesystem@accountname.dfs.core.windows.net/path/to/external/table"
    :return: None
    '''
