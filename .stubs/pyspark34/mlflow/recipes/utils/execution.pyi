from _typeshed import Incomplete
from mlflow.environment_variables import MLFLOW_RECIPES_EXECUTION_DIRECTORY as MLFLOW_RECIPES_EXECUTION_DIRECTORY, MLFLOW_RECIPES_EXECUTION_TARGET_STEP_NAME as MLFLOW_RECIPES_EXECUTION_TARGET_STEP_NAME
from mlflow.recipes.step import BaseStep as BaseStep, StepStatus as StepStatus
from mlflow.utils.file_utils import read_yaml as read_yaml, write_yaml as write_yaml
from typing import List

def run_recipe_step(recipe_root_path: str, recipe_steps: List[BaseStep], target_step: BaseStep, template: str) -> BaseStep:
    """
    Runs the specified step in the specified recipe, as well as all dependent steps.

    :param recipe_root_path: The absolute path of the recipe root directory on the local
                               filesystem.
    :param recipe_steps: A list of all the steps contained in the subgraph of the specified
                           recipe that contains the target_step. Recipe steps must be
                           provided in the order that they are intended to be executed.
    :param target_step: The step to run.
    :param template: The template to use when selecting a Makefile to load.  If the template is
                     invalid, an exception is thrown.
    :return: The last step that successfully completed during the recipe execution. If execution
             was successful, this always corresponds to the supplied target step. If execution was
             unsuccessful, this corresponds to the step that failed.
    """
def clean_execution_state(recipe_root_path: str, recipe_steps: List[BaseStep]) -> None:
    """
    Removes all execution state for the specified recipe steps from the associated execution
    directory on the local filesystem. This method does *not* remove other execution results, such
    as content logged to MLflow Tracking.

    :param recipe_root_path: The absolute path of the recipe root directory on the local
                               filesystem.
    :param recipe_steps: The recipe steps for which to remove execution state.
    """
def get_step_output_path(recipe_root_path: str, step_name: str, relative_path: str) -> str:
    """
    Obtains the absolute path of the specified step output on the local filesystem. Does
    not check the existence of the output.

    :param recipe_root_path: The absolute path of the recipe root directory on the local
                               filesystem.
    :param step_name: The name of the recipe step containing the specified output.
    :param relative_path: The relative path of the output within the output directory
                          of the specified recipe step.
    :return The absolute path of the step output on the local filesystem, which may or may
            not exist.
    """
def get_or_create_base_execution_directory(recipe_root_path: str) -> str:
    """
    Obtains the path of the execution directory on the local filesystem corresponding to the
    specified recipe. The directory is created if it does not exist.

    :param recipe_root_path: The absolute path of the recipe root directory on the local
                               filesystem.
    :return: The path of the execution directory on the local filesystem corresponding to the
             specified recipe.
    """

class _ExecutionPlan:
    steps_cached: Incomplete
    def __init__(self, rule_name, output_lines_of_make: List[str], recipe_step_names: List[str]) -> None: ...
    def print(self) -> None: ...

class _MakefilePathFormat:
    '''
    Provides platform-agnostic path substitution for execution Makefiles, ensuring that POSIX-style
    relative paths are joined correctly with POSIX-style or Windows-style recipe root paths.

    For example, given a format string `s = "{path:prp/my/subpath.txt}"`, invoking
    `s.format(path=_MakefilePathFormat(recipe_root_path="/my/recipe/root/path", ...))` on
    Unix systems or
    `s.format(path=_MakefilePathFormat(recipe_root_path="C:\\my\\recipe\\root\\path", ...))`` on
    Windows systems will yield "/my/recipe/root/path/my/subpath.txt" or
    "C:/my/recipe/root/path/my/subpath.txt", respectively.

    Additionally, given a format string `s = "{path:exe/my/subpath.txt}"`, invoking
    `s.format(path=_MakefilePathFormat(execution_directory_path="/my/exe/dir/path", ...))` on
    Unix systems or
    `s.format(path=_MakefilePathFormat(execution_directory_path="/my/exe/dir/path", ...))`` on
    Windows systems will yield "/my/exe/dir/path/my/subpath.txt" or
    "C:/my/exe/dir/path/my/subpath.txt", respectively.
    '''
    recipe_root_path: Incomplete
    execution_directory_path: Incomplete
    def __init__(self, recipe_root_path: str, execution_directory_path: str) -> None:
        """
        :param recipe_root_path: The absolute path of the recipe root directory on the local
                                   filesystem.
        :param execution_directory_path: The absolute path of the execution directory on the local
                                         filesystem for the recipe.
        """
    def __format__(self, path_spec: str) -> str:
        """
        :param path_spec: A substitution path spec of the form `<placeholder>/<subpath>`. This
                          method substitutes `<placeholder>` with `<recipe_root_path>`, if
                          `<placeholder>` is `prp`, or `<execution_directory_path>`, if
                          `<placeholder>` is `exe`.
        """
