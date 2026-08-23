from _typeshed import Incomplete
from mlflow.environment_variables import MLFLOW_CONDA_CREATE_ENV_CMD as MLFLOW_CONDA_CREATE_ENV_CMD
from mlflow.exceptions import ExecutionException as ExecutionException
from mlflow.utils import process as process
from mlflow.utils.environment import Environment as Environment

MLFLOW_CONDA_HOME: str

def get_conda_command(conda_env_name): ...
def get_conda_bin_executable(executable_name):
    """
    Return path to the specified executable, assumed to be discoverable within the 'bin'
    subdirectory of a conda installation.

    The conda home directory (expected to contain a 'bin' subdirectory) is configurable via the
    ``mlflow.projects.MLFLOW_CONDA_HOME`` environment variable. If
    ``mlflow.projects.MLFLOW_CONDA_HOME`` is unspecified, this method simply returns the passed-in
    executable name.
    """
def get_or_create_conda_env(conda_env_path, env_id: Incomplete | None = None, capture_output: bool = False, env_root_dir: Incomplete | None = None):
    '''
    Given a `Project`, creates a conda environment containing the project\'s dependencies if such a
    conda environment doesn\'t already exist. Returns the name of the conda environment.
    :param conda_env_path: Path to a conda yaml file.
    :param env_id: Optional string that is added to the contents of the yaml file before
                   calculating the hash. It can be used to distinguish environments that have the
                   same conda dependencies but are supposed to be different based on the context.
                   For example, when serving the model we may install additional dependencies to the
                   environment after the environment has been activated.
    :param capture_output: Specify the capture_output argument while executing the
                           "conda env create" command.
    :param env_root_dir: See doc of PyFuncBackend constructor argument `env_root_dir`.
    '''
