import abc
from _typeshed import Incomplete
from abc import ABC
from pyspark.ml import Estimator, Transformer
from pyspark.ml.param.shared import HasInputCol as HasInputCol, HasOutputCol as HasOutputCol
from pyspark.sql import DataFrame
from synapse.ml.cyber.utils.spark_utils import HasSetInputCol, HasSetOutputCol
from typing import Dict

class PerPartitionScalarScalerModel(ABC, Transformer, HasSetInputCol, HasSetOutputCol, metaclass=abc.ABCMeta):
    partitionKey: Incomplete
    def __init__(self, input_col: str, partition_key: str | None, output_col: str, per_group_stats: DataFrame | Dict[str, float], use_pandas: bool = True) -> None: ...
    @property
    def per_group_stats(self): ...
    @property
    def use_pandas(self): ...
    def is_partitioned(self) -> bool: ...

class PerPartitionScalarScalerEstimator(ABC, Estimator, HasSetInputCol, HasSetOutputCol, metaclass=abc.ABCMeta):
    partitionKey: Incomplete
    def __init__(self, input_col: str, partition_key: str | None, output_col: str, use_pandas: bool = True) -> None: ...
    @property
    def use_pandas(self): ...

class StandardScalarScalerConfig:
    """
    The tokens to use for temporary representation of mean and standard deviation
    """
    mean_token: str
    std_token: str

class StandardScalarScalerModel(PerPartitionScalarScalerModel):
    coefficientFactor: Incomplete
    coefficient_factor: Incomplete
    def __init__(self, input_col: str, partition_key: str | None, output_col: str, per_group_stats: DataFrame | Dict[str, float], coefficient_factor: float = 1.0, use_pandas: bool = True) -> None: ...

class StandardScalarScaler(PerPartitionScalarScalerEstimator):
    coefficientFactor: Incomplete
    coefficient_factor: Incomplete
    def __init__(self, input_col: str, partition_key: str | None, output_col: str, coefficient_factor: float = 1.0, use_pandas: bool = True) -> None: ...

class LinearScalarScalerConfig:
    min_actual_value_token: str
    max_actual_value_token: str

class LinearScalarScalerModel(PerPartitionScalarScalerModel):
    min_required_value: Incomplete
    max_required_value: Incomplete
    def __init__(self, input_col: str, partition_key: str | None, output_col: str, per_group_stats: DataFrame | Dict[str, float], min_required_value: float, max_required_value: float, use_pandas: bool = True) -> None: ...

class LinearScalarScaler(PerPartitionScalarScalerEstimator):
    minRequiredValue: Incomplete
    maxRequiredValue: Incomplete
    min_required_value: Incomplete
    max_required_value: Incomplete
    def __init__(self, input_col: str, partition_key: str | None, output_col: str, min_required_value: float = 0.0, max_required_value: float = 1.0, use_pandas: bool = True) -> None: ...
