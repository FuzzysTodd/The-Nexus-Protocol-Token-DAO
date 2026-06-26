from _typeshed import Incomplete
from mlflow.exceptions import ExecutionException as ExecutionException
from mlflow.projects import env_type as env_type
from mlflow.tracking import artifact_utils as artifact_utils
from mlflow.utils import data_utils as data_utils
from mlflow.utils.file_utils import get_local_path_or_none as get_local_path_or_none
from mlflow.utils.string_utils import is_string_type as is_string_type, quote as quote

MLPROJECT_FILE_NAME: str
DEFAULT_CONDA_FILE_NAME: str

def load_project(directory): ...

class Project:
    """A project specification loaded from an MLproject file in the passed-in directory."""
    env_type: Incomplete
    env_config_path: Incomplete
    docker_env: Incomplete
    name: Incomplete
    def __init__(self, env_type, env_config_path, entry_points, docker_env, name) -> None: ...
    def get_entry_point(self, entry_point): ...

class EntryPoint:
    """An entry point in an MLproject specification."""
    name: Incomplete
    parameters: Incomplete
    command: Incomplete
    def __init__(self, name, parameters, command) -> None: ...
    def compute_parameters(self, user_parameters, storage_dir):
        """
        Given a dict mapping user-specified param names to values, computes parameters to
        substitute into the command for this entry point. Returns a tuple (params, extra_params)
        where `params` contains key-value pairs for parameters specified in the entry point
        definition, and `extra_params` contains key-value pairs for additional parameters passed
        by the user.

        Note that resolving parameter values can be a heavy operation, e.g. if a remote URI is
        passed for a parameter of type `path`, we download the URI to a local path within
        `storage_dir` and substitute in the local path as the parameter value.

        If `storage_dir` is `None`, report path will be return as parameter.
        """
    def compute_command(self, user_parameters, storage_dir): ...

class Parameter:
    """A parameter in an MLproject entry point."""
    name: Incomplete
    type: Incomplete
    default: Incomplete
    def __init__(self, name, yaml_obj) -> None: ...
    def compute_value(self, param_value, storage_dir, key_position): ...
