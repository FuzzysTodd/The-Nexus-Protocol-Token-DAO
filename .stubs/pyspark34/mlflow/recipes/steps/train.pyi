from _typeshed import Incomplete
from mlflow.entities import SourceType as SourceType, ViewType as ViewType
from mlflow.environment_variables import MLFLOW_RECIPES_EXECUTION_TARGET_STEP_NAME as MLFLOW_RECIPES_EXECUTION_TARGET_STEP_NAME
from mlflow.exceptions import BAD_REQUEST as BAD_REQUEST, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, MlflowException as MlflowException
from mlflow.models import Model as Model
from mlflow.recipes.artifacts import DataframeArtifact as DataframeArtifact, HyperParametersArtifact as HyperParametersArtifact, ModelArtifact as ModelArtifact, RunArtifact as RunArtifact
from mlflow.recipes.cards import BaseCard as BaseCard
from mlflow.recipes.step import BaseStep as BaseStep, StepClass as StepClass
from mlflow.recipes.utils.execution import get_step_output_path as get_step_output_path
from mlflow.recipes.utils.metrics import transform_multiclass_metrics_dict as transform_multiclass_metrics_dict
from mlflow.recipes.utils.step import get_merged_eval_metrics as get_merged_eval_metrics, get_pandas_data_profiles as get_pandas_data_profiles, validate_classification_config as validate_classification_config
from mlflow.recipes.utils.tracking import TrackingConfig as TrackingConfig, apply_recipe_tracking_config as apply_recipe_tracking_config, get_recipe_tracking_config as get_recipe_tracking_config, get_run_tags_env_vars as get_run_tags_env_vars, log_code_snapshot as log_code_snapshot
from mlflow.recipes.utils.wrapped_recipe_model import WrappedRecipeModel as WrappedRecipeModel
from mlflow.tracking import MlflowClient as MlflowClient
from mlflow.utils.databricks_utils import get_databricks_env_vars as get_databricks_env_vars, get_databricks_run_url as get_databricks_run_url
from mlflow.utils.file_utils import TempDir as TempDir
from mlflow.utils.mlflow_tags import MLFLOW_RECIPE_PROFILE_NAME as MLFLOW_RECIPE_PROFILE_NAME, MLFLOW_RECIPE_STEP_NAME as MLFLOW_RECIPE_STEP_NAME, MLFLOW_RECIPE_TEMPLATE_NAME as MLFLOW_RECIPE_TEMPLATE_NAME, MLFLOW_SOURCE_TYPE as MLFLOW_SOURCE_TYPE
from mlflow.utils.string_utils import strip_prefix as strip_prefix

class TrainStep(BaseStep):
    MODEL_ARTIFACT_RELATIVE_PATH: str
    SKLEARN_MODEL_ARTIFACT_RELATIVE_PATH: str
    PREDICTED_TRAINING_DATA_RELATIVE_PATH: str
    tracking_config: Incomplete
    recipe_config: Incomplete
    def __init__(self, step_config, recipe_root, recipe_config: Incomplete | None = None) -> None: ...
    @classmethod
    def construct_search_space_from_yaml(cls, params): ...
    @classmethod
    def is_tuning_param_equal(cls, tuning_param, logged_param): ...
    @classmethod
    def from_recipe_config(cls, recipe_config, recipe_root): ...
    @property
    def name(self): ...
    @property
    def environment(self): ...
    def get_artifacts(self): ...
    def step_class(self): ...
