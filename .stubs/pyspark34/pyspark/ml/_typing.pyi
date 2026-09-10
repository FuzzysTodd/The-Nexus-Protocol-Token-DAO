import pyspark
from _typeshed import Incomplete
from numpy import ndarray
from py4j.java_gateway import JavaObject
from pyspark.ml.linalg import Vector as Vector
from typing import Any, Dict, List, Tuple, TypeVar

ParamMap = Dict[pyspark.ml.param.Param, Any]
PipelineStage = pyspark.ml.base.Estimator | pyspark.ml.base.Transformer
T = TypeVar('T')
P = TypeVar('P', bound=pyspark.ml.param.Params)
M = TypeVar('M', bound=pyspark.ml.base.Transformer)
JM = TypeVar('JM', bound=pyspark.ml.wrapper.JavaTransformer)
C = TypeVar('C', bound=type)
JavaObjectOrPickleDump = JavaObject | bytearray | bytes
BinaryClassificationEvaluatorMetricType: Incomplete
RegressionEvaluatorMetricType: Incomplete
MulticlassClassificationEvaluatorMetricType: Incomplete
MultilabelClassificationEvaluatorMetricType: Incomplete
ClusteringEvaluatorMetricType: Incomplete
ClusteringEvaluatorDistanceMeasureType: Incomplete
RankingEvaluatorMetricType: Incomplete
VectorLike = ndarray | Vector | List[float] | Tuple[float, ...]
