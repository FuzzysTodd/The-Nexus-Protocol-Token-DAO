from mlflow.tracking.default_experiment import DEFAULT_EXPERIMENT_ID as DEFAULT_EXPERIMENT_ID
from mlflow.tracking.default_experiment.databricks_notebook_experiment_provider import DatabricksNotebookExperimentProvider as DatabricksNotebookExperimentProvider, DatabricksRepoNotebookExperimentProvider as DatabricksRepoNotebookExperimentProvider

class DefaultExperimentProviderRegistry:
    """Registry for default experiment provider implementations

    This class allows the registration of default experiment providers, which are used to provide
    MLflow Experiment IDs based on the current context where the MLflow client is running when
    the user has not explicitly set an experiment. Implementations declared though the entrypoints
    `mlflow.default_experiment_provider` group can be automatically registered through the
    `register_entrypoints` method.
    """
    def __init__(self) -> None: ...
    def register(self, default_experiment_provider_cls) -> None: ...
    def register_entrypoints(self) -> None:
        """Register tracking stores provided by other packages"""
    def __iter__(self): ...

def get_experiment_id():
    """Get an experiment ID for the current context. The experiment ID is fetched by querying
    providers, in the order that they were registered.

    This function iterates through all default experiment context providers in the registry.

    :return: An experiment_id.
    """
