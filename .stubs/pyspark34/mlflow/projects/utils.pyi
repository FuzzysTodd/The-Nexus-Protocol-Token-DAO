from mlflow import tracking as tracking
from mlflow.entities import Param as Param, SourceType as SourceType
from mlflow.environment_variables import MLFLOW_EXPERIMENT_ID as MLFLOW_EXPERIMENT_ID, MLFLOW_RUN_ID as MLFLOW_RUN_ID, MLFLOW_TRACKING_URI as MLFLOW_TRACKING_URI
from mlflow.exceptions import ExecutionException as ExecutionException
from mlflow.tracking import fluent as fluent
from mlflow.utils.git_utils import get_git_commit as get_git_commit, get_git_repo_url as get_git_repo_url
from mlflow.utils.mlflow_tags import LEGACY_MLFLOW_GIT_BRANCH_NAME as LEGACY_MLFLOW_GIT_BRANCH_NAME, LEGACY_MLFLOW_GIT_REPO_URL as LEGACY_MLFLOW_GIT_REPO_URL, MLFLOW_GIT_BRANCH as MLFLOW_GIT_BRANCH, MLFLOW_GIT_COMMIT as MLFLOW_GIT_COMMIT, MLFLOW_GIT_REPO_URL as MLFLOW_GIT_REPO_URL, MLFLOW_PARENT_RUN_ID as MLFLOW_PARENT_RUN_ID, MLFLOW_PROJECT_ENTRY_POINT as MLFLOW_PROJECT_ENTRY_POINT, MLFLOW_SOURCE_NAME as MLFLOW_SOURCE_NAME, MLFLOW_SOURCE_TYPE as MLFLOW_SOURCE_TYPE, MLFLOW_USER as MLFLOW_USER
from mlflow.utils.rest_utils import augmented_raise_for_status as augmented_raise_for_status

MLFLOW_LOCAL_BACKEND_RUN_ID_CONFIG: str
MLFLOW_DOCKER_WORKDIR_PATH: str
PROJECT_ENV_MANAGER: str
PROJECT_SYNCHRONOUS: str
PROJECT_DOCKER_ARGS: str
PROJECT_STORAGE_DIR: str
PROJECT_BUILD_IMAGE: str
PROJECT_DOCKER_AUTH: str
GIT_FETCH_DEPTH: int

def fetch_and_validate_project(uri, version, entry_point, parameters): ...
def load_project(work_dir): ...
def get_or_create_run(run_id, uri, experiment_id, work_dir, version, entry_point, parameters): ...
def get_entry_point_command(project, entry_point, parameters, storage_dir):
    """
    Returns the shell command to execute in order to run the specified entry point.
    :param project: Project containing the target entry point
    :param entry_point: Entry point to run
    :param parameters: Parameters (dictionary) for the entry point command
    :param storage_dir: Base local directory to use for downloading remote artifacts passed to
                        arguments of type 'path'. If None, a temporary base directory is used.
    """
def get_run_env_vars(run_id, experiment_id):
    """
    Returns a dictionary of environment variable key-value pairs to set in subprocess launched
    to run MLflow projects.
    """
