from enum import Enum
from mlflow.exceptions import BAD_REQUEST as BAD_REQUEST, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, MlflowException as MlflowException
from mlflow.recipes.artifacts import DataframeArtifact as DataframeArtifact
from mlflow.recipes.cards import BaseCard as BaseCard
from mlflow.recipes.step import BaseStep as BaseStep, StepClass as StepClass
from mlflow.recipes.utils.execution import get_step_output_path as get_step_output_path
from mlflow.recipes.utils.step import get_pandas_data_profiles as get_pandas_data_profiles, validate_classification_config as validate_classification_config

class SplitValues(Enum):
    """
    Represents the custom split return values.
    """
    TEST: str
    TRAINING: str
    VALIDATION: str

class SplitStep(BaseStep):
    @classmethod
    def from_recipe_config(cls, recipe_config, recipe_root): ...
    @property
    def name(self): ...
    def get_artifacts(self): ...
    def step_class(self): ...
