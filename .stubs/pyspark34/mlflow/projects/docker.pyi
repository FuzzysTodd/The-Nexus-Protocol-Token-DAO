from mlflow import tracking as tracking
from mlflow.environment_variables import MLFLOW_TRACKING_URI as MLFLOW_TRACKING_URI
from mlflow.exceptions import ExecutionException as ExecutionException
from mlflow.projects.utils import MLFLOW_DOCKER_WORKDIR_PATH as MLFLOW_DOCKER_WORKDIR_PATH
from mlflow.utils import file_utils as file_utils, process as process
from mlflow.utils.databricks_utils import get_databricks_env_vars as get_databricks_env_vars
from mlflow.utils.git_utils import get_git_commit as get_git_commit
from mlflow.utils.mlflow_tags import MLFLOW_DOCKER_IMAGE_ID as MLFLOW_DOCKER_IMAGE_ID, MLFLOW_DOCKER_IMAGE_URI as MLFLOW_DOCKER_IMAGE_URI

def validate_docker_installation() -> None:
    """
    Verify if Docker is installed and running on host machine.
    """
def validate_docker_env(project) -> None: ...
def build_docker_image(work_dir, repository_uri, base_image, run_id, build_image, docker_auth):
    """
    Build a docker image containing the project in `work_dir`, using the base image.
    """
def get_docker_tracking_cmd_and_envs(tracking_uri): ...
