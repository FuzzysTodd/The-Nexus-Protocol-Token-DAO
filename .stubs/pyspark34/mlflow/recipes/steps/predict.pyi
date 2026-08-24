from _typeshed import Incomplete
from mlflow.exceptions import BAD_REQUEST as BAD_REQUEST, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, MlflowException as MlflowException
from mlflow.recipes.artifacts import DataframeArtifact as DataframeArtifact, RegisteredModelVersionInfo as RegisteredModelVersionInfo
from mlflow.recipes.cards import BaseCard as BaseCard
from mlflow.recipes.step import BaseStep as BaseStep, StepClass as StepClass
from mlflow.recipes.utils.execution import get_step_output_path as get_step_output_path
from mlflow.recipes.utils.step import get_pandas_data_profiles as get_pandas_data_profiles
from mlflow.recipes.utils.tracking import TrackingConfig as TrackingConfig, apply_recipe_tracking_config as apply_recipe_tracking_config, get_recipe_tracking_config as get_recipe_tracking_config
from mlflow.utils.databricks_utils import get_databricks_env_vars as get_databricks_env_vars
from mlflow.utils.file_utils import write_spark_dataframe_to_parquet_on_local_disk as write_spark_dataframe_to_parquet_on_local_disk
from typing import Any, Dict

class PredictStep(BaseStep):
    tracking_config: Incomplete
    def __init__(self, step_config: Dict[str, Any], recipe_root: str) -> None: ...
    @classmethod
    def from_recipe_config(cls, recipe_config, recipe_root): ...
    @property
    def name(self): ...
    @property
    def environment(self): ...
    def get_artifacts(self): ...
    def step_class(self): ...
