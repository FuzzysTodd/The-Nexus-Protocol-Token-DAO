import numpy as np
from _typeshed import Incomplete
from flaml.automl.spark import DataFrame as DataFrame, F as F, Series as Series, T as T, ps as ps, psDataFrame as psDataFrame, psSeries as psSeries, set_option as set_option, sparkDataFrame as sparkDataFrame
from typing import List, Tuple

logger: Incomplete
logger_formatter: Incomplete

def to_pandas_on_spark(df: DataFrame | sparkDataFrame | Series | psDataFrame | psSeries, index_col: str | None = None, default_index_type: str | None = 'distributed-sequence') -> psDataFrame | psSeries:
    '''Convert pandas or pyspark dataframe/series to pandas_on_Spark dataframe/series.

    Args:
        df: pandas.DataFrame/series or pyspark dataframe | The input dataframe/series.
        index_col: str, optional | The column name to use as index, default None.
        default_index_type: str, optional | The default index type, default "distributed-sequence".

    Returns:
        pyspark.pandas.DataFrame/Series: The converted pandas-on-Spark dataframe/series.

    ```python
    import pandas as pd
    from flaml.automl.spark.utils import to_pandas_on_spark

    pdf = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    psdf = to_pandas_on_spark(pdf)
    print(psdf)

    from pyspark.sql import SparkSession

    spark = SparkSession.builder.getOrCreate()
    sdf = spark.createDataFrame(pdf)
    psdf = to_pandas_on_spark(sdf)
    print(psdf)

    pds = Series([1, 2, 3])
    pss = to_pandas_on_spark(pds)
    print(pss)
    ```
    '''
def train_test_split_pyspark(df: sparkDataFrame | psDataFrame, stratify_column: str | None = None, test_fraction: float | None = 0.2, seed: int | None = 1234, to_pandas_spark: bool | None = True, index_col: str | None = 'tmp_index_col') -> Tuple[sparkDataFrame | psDataFrame, sparkDataFrame | psDataFrame]:
    """Split a pyspark dataframe into train and test dataframes.

    Args:
        df: pyspark.sql.DataFrame | The input dataframe.
        stratify_column: str | The column name to stratify the split. Default None.
        test_fraction: float | The fraction of the test data. Default 0.2.
        seed: int | The random seed. Default 1234.
        to_pandas_spark: bool | Whether to convert the output to pandas_on_spark. Default True.
        index_col: str | The column name to use as index. Default None.

    Returns:
        pyspark.sql.DataFrame/pandas_on_spark DataFrame | The train dataframe.
        pyspark.sql.DataFrame/pandas_on_spark DataFrame | The test dataframe.
    """
def unique_pandas_on_spark(psds: psSeries | psDataFrame) -> Tuple[np.ndarray, np.ndarray]:
    """Get the unique values and counts of a pandas_on_spark series."""
def len_labels(y: psSeries | np.ndarray, return_labels: bool = False) -> int | np.ndarray | None:
    """Get the number of unique labels in y."""
def unique_value_first_index(y: Series | psSeries | np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Get the unique values and indices of a pandas series,
    pandas_on_spark series or numpy array."""
def iloc_pandas_on_spark(psdf: psDataFrame | psSeries | DataFrame | Series, index: int | slice | list, index_col: str | None = 'tmp_index_col') -> psDataFrame | psSeries:
    """Get the rows of a pandas_on_spark dataframe/series by index."""
def spark_kFold(dataset: sparkDataFrame | psDataFrame, nFolds: int = 3, foldCol: str = '', seed: int = 42, index_col: str | None = 'tmp_index_col') -> List[Tuple[psDataFrame, psDataFrame]]:
    '''Generate k-fold splits for a Spark DataFrame.
    Adopted from https://spark.apache.org/docs/latest/api/python/_modules/pyspark/ml/tuning.html#CrossValidator

    Args:
        dataset: sparkDataFrame / psDataFrame. | The DataFrame to split.
        nFolds: int | The number of folds. Default is 3.
        foldCol: str | The column name to use for fold numbers. If not specified,
            the DataFrame will be randomly split. Default is "".
            The same group will not appear in two different folds (the number of
            distinct groups has to be at least equal to the number of folds).
            The folds are approximately balanced in the sense that the number of
            distinct groups is approximately the same in each fold.
        seed: int | The random seed. Default is 42.
        index_col: str | The name of the index column. Default is "tmp_index_col".

    Returns:
        A list of (train, validation) DataFrames.
    '''
