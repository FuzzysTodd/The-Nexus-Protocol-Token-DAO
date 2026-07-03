from _typeshed import Incomplete
from mlflow.exceptions import BAD_REQUEST as BAD_REQUEST, MlflowException as MlflowException
from mlflow.models import EvaluationMetric as EvaluationMetric, make_metric as make_metric
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from typing import Any, Dict

class RecipeMetric:
    name: Incomplete
    greater_is_better: Incomplete
    custom_function: Incomplete
    def __init__(self, name: str, greater_is_better: bool, custom_function: str | None = None) -> None: ...
    @classmethod
    def from_custom_metric_dict(cls, custom_metric_dict): ...

BUILTIN_BINARY_CLASSIFICATION_RECIPE_METRICS: Incomplete
BUILTIN_MULTICLASS_CLASSIFICATION_RECIPE_METRICS: Incomplete
BUILTIN_REGRESSION_RECIPE_METRICS: Incomplete
DEFAULT_METRICS: Incomplete

def transform_multiclass_metric(metric_name: str, ext_task: str) -> str: ...
def transform_multiclass_metrics_dict(eval_metrics: Dict[str, Any], ext_task) -> Dict[str, Any]: ...
