from _typeshed import Incomplete
from pyspark.ml import Estimator, Transformer
from pyspark.ml.param.shared import HasInputCol as HasInputCol, HasOutputCol as HasOutputCol
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.cyber.utils.spark_utils import HasSetInputCol, HasSetOutputCol
from typing import List

class IdIndexerModel(Transformer, HasSetInputCol, HasSetOutputCol):
    partitionKey: Incomplete
    def __init__(self, input_col: str, partition_key: str, output_col: str, vocab_df: DataFrame) -> None: ...
    def undo_transform(self, df: DataFrame) -> DataFrame: ...

class IdIndexer(Estimator, HasSetInputCol, HasSetOutputCol):
    partitionKey: Incomplete
    resetPerPartition: Incomplete
    def __init__(self, input_col: str, partition_key: str, output_col: str, reset_per_partition: bool) -> None: ...

class MultiIndexerModel(Transformer):
    models: Incomplete
    def __init__(self, models: List[IdIndexerModel]) -> None: ...
    def get_model_by_input_col(self, input_col): ...
    def get_model_by_output_col(self, output_col): ...
    def undo_transform(self, df: DataFrame) -> DataFrame: ...

class MultiIndexer(Estimator):
    indexers: Incomplete
    def __init__(self, indexers: List[IdIndexer]) -> None: ...
