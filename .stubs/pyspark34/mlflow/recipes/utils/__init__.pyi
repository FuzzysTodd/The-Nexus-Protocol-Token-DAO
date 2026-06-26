from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.utils.databricks_utils import is_in_databricks_runtime as is_in_databricks_runtime
from mlflow.utils.file_utils import read_yaml as read_yaml, render_and_merge_yaml as render_and_merge_yaml
from typing import Any, Dict

def get_recipe_name(recipe_root_path: str = None) -> str:
    """
    Obtains the name of the specified recipe or of the recipe corresponding to the current
    working directory.

    :param recipe_root_path: The absolute path of the recipe root directory on the local
                               filesystem. If unspecified, the recipe root directory is
                               resolved from the current working directory.
    :raises MlflowException: If the specified ``recipe_root_path`` is not a recipe root
                             directory or if ``recipe_root_path`` is ``None`` and the current
                             working directory does not correspond to a recipe.
    :return: The name of the specified recipe.
    """
def get_recipe_config(recipe_root_path: str = None, profile: str = None) -> Dict[str, Any]:
    '''
    Obtains a dictionary representation of the configuration for the specified recipe.

    :param recipe_root_path: The absolute path of the recipe root directory on the local
                               filesystem. If unspecified, the recipe root directory is
                               resolved from the current working directory, and an
    :param profile: The name of the profile under the `profiles` directory to use,
                    e.g. "dev" to use configs from "profiles/dev.yaml"
    :raises MlflowException: If the specified ``recipe_root_path`` is not a recipe root
                             directory or if ``recipe_root_path`` is ``None`` and the current
                             working directory does not correspond to a recipe.
    :return: The configuration of the specified recipe.
    '''
def get_recipe_root_path() -> str:
    """
    Obtains the path of the recipe corresponding to the current working directory, throwing an
    ``MlflowException`` if the current working directory does not reside within a recipe
    directory.

    :return: The absolute path of the recipe root directory on the local filesystem.
    """
def get_default_profile() -> str:
    """
    Returns the default profile name under which a recipe is executed. The default
    profile may change depending on runtime environment.

    :return: The default profile name string.
    """
