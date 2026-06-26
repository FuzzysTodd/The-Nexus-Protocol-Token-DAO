import abc
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import BAD_REQUEST as BAD_REQUEST, INTERNAL_ERROR as INTERNAL_ERROR, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.recipes import dag_help_strings as dag_help_strings
from mlflow.recipes.artifacts import Artifact as Artifact
from mlflow.recipes.step import BaseStep as BaseStep, StepClass as StepClass, StepStatus as StepStatus
from mlflow.recipes.utils import get_recipe_config as get_recipe_config, get_recipe_name as get_recipe_name, get_recipe_root_path as get_recipe_root_path
from mlflow.recipes.utils.execution import clean_execution_state as clean_execution_state, get_or_create_base_execution_directory as get_or_create_base_execution_directory, get_step_output_path as get_step_output_path, run_recipe_step as run_recipe_step
from mlflow.recipes.utils.step import display_html as display_html

class BaseRecipe(metaclass=abc.ABCMeta):
    """
    Base Recipe
    """
    def __init__(self, recipe_root_path: str, profile: str) -> None:
        """
        Recipe base class.

        :param recipe_root_path: String path to the directory under which the recipe template
                                   such as recipe.yaml, profiles/{profile}.yaml and
                                   steps/{step_name}.py are defined.
        :param profile: String specifying the profile name, with which
                        {recipe_root_path}/profiles/{profile}.yaml is read and merged with
                        recipe.yaml to generate the configuration to run the recipe.
        """
    @property
    def name(self) -> str:
        """Returns the name of the recipe."""
    @property
    def profile(self) -> str:
        """
        Returns the profile under which the recipe and its steps will execute.
        """
    def run(self, step: str = None) -> None:
        """
        Runs a step in the recipe, or the entire recipe if a step is not specified.

        :param step: String name to run a step within the recipe. The step and its dependencies
                     will be run sequentially. If a step is not specified, the entire recipe is
                     executed.
        :return: None
        """
    def inspect(self, step: str = None) -> None:
        """
        Displays main output from a step, or a recipe DAG if no step is specified.

        :param step: String name to display a step output within the recipe. If a step is not
                     specified, the DAG of the recipe is shown instead.
        :return: None
        """
    def clean(self, step: str = None) -> None:
        """
        Removes the outputs of the specified step from the cache, or removes the cached outputs
        of all steps if no particular step is specified. After cached outputs are cleaned
        for a particular step, the step will be re-executed in its entirety the next time it is
        invoked via ``BaseRecipe.run()``.

        :param step: String name of the step to clean within the recipe. If not specified,
                     cached outputs are removed for all recipe steps.
        """
    def get_artifact(self, artifact_name: str):
        """
        Read an artifact from recipe output. artifact names can be obtained from
        `Recipe.inspect()` or `Recipe.run()` output.

        Returns None if the specified artifact is not found.
        Raise an error if the artifact is not supported.
        """

class Recipe:
    '''
    A factory class that creates an instance of a recipe for a particular ML problem
    (e.g. regression, classification) or MLOps task (e.g. batch scoring) based on the current
    working directory and supplied configuration.

    .. code-block:: python
        :caption: Example

        import os
        from mlflow.recipes import Recipe

        os.chdir("~/recipes-regression-template")
        regression_recipe = Recipe(profile="local")
        regression_recipe.run(step="train")
    '''
    def __new__(cls, profile: str):
        '''
        Creates an instance of an MLflow Recipe for a particular ML problem or MLOps task based
        on the current working directory and supplied configuration. The current working directory
        must be the root directory of an MLflow Recipe repository or a subdirectory of an
        MLflow Recipe repository.

        :param profile: The name of the profile to use for configuring the problem-specific or
                        task-specific recipe. Profiles customize the configuration of
                        one or more recipe steps, and recipe executions with different profiles
                        often produce different results.
        :return: A recipe for a particular ML problem or MLOps task. For example, an instance of
                 `RegressionRecipe <https://github.com/mlflow/recipes-regression-template>`_
                 for regression problems.

        .. code-block:: python
            :caption: Example

            import os
            from mlflow.recipes import Recipe

            os.chdir("~/recipes-regression-template")
            regression_recipe = Recipe(profile="local")
            regression_recipe.run(step="train")
        '''
