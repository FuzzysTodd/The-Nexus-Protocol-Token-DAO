from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException, RestException as RestException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.recipes.utils import get_recipe_name as get_recipe_name
from mlflow.tracking.client import MlflowClient as MlflowClient
from mlflow.tracking.context.registry import resolve_tags as resolve_tags
from mlflow.tracking.context.system_environment_context import MLFLOW_RUN_CONTEXT_ENV_VAR as MLFLOW_RUN_CONTEXT_ENV_VAR
from mlflow.tracking.default_experiment import DEFAULT_EXPERIMENT_ID as DEFAULT_EXPERIMENT_ID
from mlflow.utils.databricks_utils import is_in_databricks_runtime as is_in_databricks_runtime
from mlflow.utils.file_utils import path_to_local_file_uri as path_to_local_file_uri, path_to_local_sqlite_uri as path_to_local_sqlite_uri
from mlflow.utils.git_utils import get_git_branch as get_git_branch, get_git_commit as get_git_commit, get_git_repo_url as get_git_repo_url
from mlflow.utils.mlflow_tags import LEGACY_MLFLOW_GIT_REPO_URL as LEGACY_MLFLOW_GIT_REPO_URL, MLFLOW_GIT_BRANCH as MLFLOW_GIT_BRANCH, MLFLOW_GIT_COMMIT as MLFLOW_GIT_COMMIT, MLFLOW_GIT_REPO_URL as MLFLOW_GIT_REPO_URL, MLFLOW_SOURCE_NAME as MLFLOW_SOURCE_NAME
from typing import Any, Dict

class TrackingConfig:
    """
    The MLflow Tracking configuration associated with an MLflow Recipe, including the
    Tracking URI and information about the destination Experiment for writing results.
    """
    tracking_uri: Incomplete
    experiment_name: Incomplete
    experiment_id: Incomplete
    run_name: Incomplete
    artifact_location: Incomplete
    def __init__(self, tracking_uri: str, experiment_name: str = None, experiment_id: str = None, run_name: str = None, artifact_location: str = None) -> None:
        """
        :param tracking_uri: The MLflow Tracking URI.
        :param experiment_name: The MLflow Experiment name. At least one of ``experiment_name`` or
                                ``experiment_id`` must be specified. If both are specified, they
                                must be consistent with Tracking server state. Note that this
                                Experiment may not exist prior to recipe execution.
        :param experiment_id: The MLflow Experiment ID. At least one of ``experiment_name`` or
                              ``experiment_id`` must be specified. If both are specified, they
                              must be consistent with Tracking server state. Note that this
                              Experiment may not exist prior to recipe execution.
        :param run_name: The MLFlow Run Name. If the run name is not specified, then a random
                                name is set for the run.
        :param artifact_location: The artifact location to use for the Experiment, if the Experiment
                                  does not already exist. If the Experiment already exists, this
                                  location is ignored.
        """
    def to_dict(self) -> Dict[str, str]:
        """
        Obtains a dictionary representation of the MLflow Tracking configuration.

        :return: A dictionary representation of the MLflow Tracking configuration.
        """
    @classmethod
    def from_dict(cls, config_dict: Dict[str, str]) -> TrackingConfig:
        """
        Creates a ``TrackingConfig`` instance from a dictionary representation.

        :param config_dict: A dictionary representation of the MLflow Tracking configuration.
        :return: A ``TrackingConfig`` instance.
        """

def get_recipe_tracking_config(recipe_root_path: str, recipe_config: Dict[str, Any]) -> TrackingConfig:
    """
    Obtains the MLflow Tracking configuration for the specified recipe.

    :param recipe_root_path: The absolute path of the recipe root directory on the local
                               filesystem.
    :param recipe_config: The configuration of the specified recipe.
    :return: A ``TrackingConfig`` instance containing MLflow Tracking information for the
             specified recipe, including Tracking URI, Experiment name, and more.
    """
def apply_recipe_tracking_config(tracking_config: TrackingConfig):
    """
    Applies the specified ``TrackingConfig`` in the current context by setting the associated
    MLflow Tracking URI (via ``mlflow.set_tracking_uri()``) and setting the associated MLflow
    Experiment (via ``mlflow.set_experiment()``), creating it if necessary.

    :param tracking_config: The MLflow Recipe ``TrackingConfig`` to apply.
    """
def get_run_tags_env_vars(recipe_root_path: str) -> Dict[str, str]:
    """
    Returns environment variables that should be set during step execution to ensure that MLflow
    Run Tags from the current context are applied to any MLflow Runs that are created during
    recipe execution.

    :param recipe_root_path: The absolute path of the recipe root directory on the local
                               filesystem.
    :return: A dictionary of environment variable names and values.
    """
def log_code_snapshot(recipe_root: str, run_id: str, artifact_path: str = 'recipe_snapshot', recipe_config: Dict[str, Any] = None) -> None:
    '''
    Logs a recipe code snapshot as mlflow artifacts.

    :param recipe_root_path: String file path to the directory where the recipe is defined.
    :param run_id: Run ID to which the code snapshot is logged.
    :param artifact_path: Directory within the run\'s artifact director (default: "snapshots").
    :param recipe_config: Dict containing the full recipe configuration at runtime.
    '''
