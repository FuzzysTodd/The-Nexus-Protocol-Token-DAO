from pyspark.ml.base import Transformer as Transformer
from pyspark.ml.pipeline import PipelineModel as PipelineModel
from pyspark.sql import DataFrame as DataFrame
from typing import Set

def cast_spark_df_with_vector_to_array(input_spark_df):
    """
    Finds columns of vector type in a spark dataframe and
    casts them to array<double> type.

    :param input_spark_df:
    :return: a spark dataframe with vector columns transformed to array<double> type
    """
def get_feature_cols(df: DataFrame, transformer: Transformer | PipelineModel) -> Set[str]:
    """
    Finds feature columns from an input dataset. If a dataset
    contains non-feature columns, those columns are not returned, but
    if `input_fields` is set to include non-feature columns those
    will be included in the return set of column names.

    :param df: An input spark dataframe.
    :param transformer: A pipeline/transformer to get the required feature columns
    :return: A set of all the feature columns that are required
             for the pipeline/transformer plus any initial columns passed in.
    """
