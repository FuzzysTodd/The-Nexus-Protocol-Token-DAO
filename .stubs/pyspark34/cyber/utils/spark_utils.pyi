from pyspark.ml.param.shared import HasInputCol, HasOutputCol
from pyspark.sql import DataFrame, SparkSession
from typing import Any, List

__all__ = ['DataFrameUtils', 'ExplainBuilder']

class DataFrameUtils:
    """Extension methods over Spark DataFrame"""
    @staticmethod
    def get_spark_session(df: DataFrame) -> SparkSession:
        """get the associated Spark session

        Parameters
        ----------
        df : DataFrame
            the dataframe of which we want to get its Spark session
        """
    @staticmethod
    def make_empty(df: DataFrame) -> DataFrame:
        """make an empty dataframe with the same schema

        Parameters
        ----------
        df the dataframe whose schema we wish to use

        Returns an empty dataframe
        -------

        """
    @staticmethod
    def zip_with_index(df: DataFrame, start_index: int = 0, col_name: str = 'rowId', partition_col: List[str] | str = [], order_by_col: List[str] | str = []) -> DataFrame:
        """add an index to the given dataframe

        Parameters
        ----------
        df : dataframe
            the dataframe to add the index to
        start_index : int
            the value to start the count from
        col_name : str
            the name of the index column which will be added as last column in the output data frame
        partition_col : Union[List[str], str]
            optional column name or list of columns names that define a partitioning to assign indices independently to,
            e.g., assign sequential indices separately to each distinct tenant
        order_by_col : Union[List[str], str]
            optional order by column name or list of columns that are used for sorting
            the data frame or partitions before indexing
        """

class ExplainBuilder:
    @staticmethod
    def get_methods(the_explainable): ...
    @staticmethod
    def get_method(the_explainable, the_method_name): ...
    @staticmethod
    def copy_params(from_explainable: Any, to_explainable: Any): ...
    @staticmethod
    def build(explainable: Any, **kwargs): ...

class HasSetInputCol(HasInputCol):
    def setInputCol(self, value):
        """
        Sets the value of :py:attr:`inputCol`.
        """

class HasSetOutputCol(HasOutputCol):
    def setOutputCol(self, value):
        """
        Sets the value of :py:attr:`outputCol`.
        """
