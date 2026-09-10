import abc
from _typeshed import Incomplete
from enum import Enum
from mlflow.recipes.cards import BaseCard as BaseCard, CARD_HTML_NAME as CARD_HTML_NAME, CARD_PICKLE_NAME as CARD_PICKLE_NAME, FailureCard as FailureCard
from mlflow.recipes.utils import get_recipe_name as get_recipe_name
from mlflow.recipes.utils.step import display_html as display_html
from mlflow.tracking import MlflowClient as MlflowClient
from mlflow.utils.databricks_utils import is_in_databricks_runtime as is_in_databricks_runtime
from typing import Any, Dict, List

class StepStatus(Enum):
    """
    Represents the execution status of a step.
    """
    UNKNOWN: str
    RUNNING: str
    SUCCEEDED: str
    FAILED: str

class StepClass(Enum):
    """
    Represents the class of a step.
    """
    UNKNOWN: str
    TRAINING: str
    PREDICTION: str

class StepExecutionState:
    """
    Represents execution state for a step, including the current status and
    the time of the last status update.
    """
    status: Incomplete
    last_updated_timestamp: Incomplete
    stack_trace: Incomplete
    def __init__(self, status: StepStatus, last_updated_timestamp: int, stack_trace: str) -> None:
        """
        :param status: The execution status of the step.
        :param last_updated_timestamp: The timestamp of the last execution status update, measured
                                       in seconds since the UNIX epoch.
        :param stack_trace: The stack trace of the last execution. None if the step execution
                            succeeds.
        """
    def to_dict(self) -> Dict[str, Any]:
        """
        Creates a dictionary representation of the step execution state.
        """
    @classmethod
    def from_dict(cls, state_dict) -> StepExecutionState:
        """
        Creates a ``StepExecutionState`` instance from the specified execution state dictionary.
        """

class BaseStep(metaclass=abc.ABCMeta):
    """
    Base class representing a step in an MLflow Recipe
    """
    step_config: Incomplete
    recipe_root: Incomplete
    recipe_name: Incomplete
    task: Incomplete
    step_card: Incomplete
    def __init__(self, step_config: Dict[str, Any], recipe_root: str) -> None:
        """
        :param step_config: dictionary of the config needed to
                            run/implement the step.
        :param recipe_root: String file path to the directory where step
                              are defined.
        """
    def run(self, output_directory: str):
        """
        Executes the step by running common setup operations and invoking
        step-specific code (as defined in ``_run()``).

        :param output_directory: String file path to the directory where step
                                 outputs should be stored.
        :return: None
        """
    def inspect(self, output_directory: str):
        """
        Inspect the step output state by running the generic inspect information here and
        running the step specific inspection code in the step's _inspect() method.

        :param output_directory: String file path where to the directory where step
                                 outputs are located.
        :return: None
        """
    @classmethod
    @abc.abstractmethod
    def from_recipe_config(cls, recipe_config: Dict[str, Any], recipe_root: str) -> BaseStep:
        """
        Constructs a step class instance by creating a step config using the recipe
        config.
        Subclasses must implement this method to produce the config required to correctly
        run the corresponding step.

        :param recipe_config: Dictionary representation of the full recipe config.
        :param recipe_root: String file path to the recipe root directory.
        :return: class instance of the step.
        """
    @classmethod
    def from_step_config_path(cls, step_config_path: str, recipe_root: str) -> BaseStep:
        """
        Constructs a step class instance using the config specified in the
        configuration file.

        :param step_config_path: String path to the step-specific configuration
                                 on the local filesystem.
        :param recipe_root: String path to the recipe root directory on
                              the local filesystem.
        :return: class instance of the step.
        """
    @property
    @abc.abstractmethod
    def name(self) -> str:
        """
        Returns back the name of the step for the current class instance. This is used
        downstream by the execution engine to create step-specific directory structures.
        """
    @property
    def environment(self) -> Dict[str, str]:
        """
        Returns environment variables associated with step that should be set when the
        step is executed.
        """
    def get_artifacts(self) -> List[Any]:
        """
        Returns the named artifacts produced by the step for the current class instance.
        """
    @abc.abstractmethod
    def step_class(self) -> StepClass:
        """
        Returns the step class.
        """
    def get_execution_state(self, output_directory: str) -> StepExecutionState:
        """
        Returns the execution state of the step, which provides information about its
        status (succeeded, failed, unknown), last update time, and, if applicable, encountered
        stacktraces.

        :param output_directory: String file path to the directory where step
                                 outputs are stored.
        :return: A ``StepExecutionState`` instance containing the step execution state.
        """
