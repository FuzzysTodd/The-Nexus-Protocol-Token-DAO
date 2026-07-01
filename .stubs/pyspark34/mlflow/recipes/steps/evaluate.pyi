from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.recipes.cards import BaseCard as BaseCard
from mlflow.recipes.step import BaseStep as BaseStep, StepClass as StepClass
from mlflow.recipes.steps.train import TrainStep as TrainStep
from mlflow.recipes.utils.execution import get_step_output_path as get_step_output_path
from mlflow.recipes.utils.metrics import transform_multiclass_metric as transform_multiclass_metric
from mlflow.recipes.utils.step import get_merged_eval_metrics as get_merged_eval_metrics, validate_classification_config as validate_classification_config
from mlflow.recipes.utils.tracking import TrackingConfig as TrackingConfig, apply_recipe_tracking_config as apply_recipe_tracking_config, get_recipe_tracking_config as get_recipe_tracking_config, get_run_tags_env_vars as get_run_tags_env_vars
from mlflow.utils.databricks_utils import get_databricks_env_vars as get_databricks_env_vars, get_databricks_run_url as get_databricks_run_url
from mlflow.utils.string_utils import strip_prefix as strip_prefix
from typing import Any, Dict, NamedTuple

class MetricValidationResult(NamedTuple):
    metric: Incomplete
    greater_is_better: Incomplete
    value: Incomplete
    threshold: Incomplete
    validated: Incomplete

class EvaluateStep(BaseStep):
    tracking_config: Incomplete
    def __init__(self, step_config: Dict[str, Any], recipe_root: str) -> None: ...
    @classmethod
    def from_recipe_config(cls, recipe_config, recipe_root): ...
    @property
    def name(self): ...
    @property
    def environment(self): ...
    def step_class(self): ...
