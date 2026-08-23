from .shared_platform_utils import list_workspace_artifacts as list_workspace_artifacts
from .synapse_mlflow_utils import get_mlflow_env_config as get_mlflow_env_config, record_all_public_functions as record_all_public_functions
from _typeshed import Incomplete
from mlflow.tracking.default_experiment.abstract_context import DefaultExperimentProvider as DefaultExperimentProvider

logger: Incomplete

class SynapseNotebookDefaultExperimentProvider(DefaultExperimentProvider):
    def in_context(self): ...
    def get_experiment_id(self): ...
