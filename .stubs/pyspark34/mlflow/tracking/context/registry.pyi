from _typeshed import Incomplete
from mlflow.tracking.context.databricks_cluster_context import DatabricksClusterRunContext as DatabricksClusterRunContext
from mlflow.tracking.context.databricks_command_context import DatabricksCommandRunContext as DatabricksCommandRunContext
from mlflow.tracking.context.databricks_job_context import DatabricksJobRunContext as DatabricksJobRunContext
from mlflow.tracking.context.databricks_notebook_context import DatabricksNotebookRunContext as DatabricksNotebookRunContext
from mlflow.tracking.context.databricks_repo_context import DatabricksRepoRunContext as DatabricksRepoRunContext
from mlflow.tracking.context.default_context import DefaultRunContext as DefaultRunContext
from mlflow.tracking.context.git_context import GitRunContext as GitRunContext
from mlflow.tracking.context.system_environment_context import SystemEnvironmentContext as SystemEnvironmentContext

class RunContextProviderRegistry:
    """Registry for run context provider implementations

    This class allows the registration of a run context provider which can be used to infer meta
    information about the context of an MLflow experiment run. Implementations declared though the
    entrypoints `mlflow.run_context_provider` group can be automatically registered through the
    `register_entrypoints` method.

    Registered run context providers can return tags that override those implemented in the core
    library, however the order in which plugins are resolved is undefined.
    """
    def __init__(self) -> None: ...
    def register(self, run_context_provider_cls) -> None: ...
    def register_entrypoints(self) -> None:
        """Register tracking stores provided by other packages"""
    def __iter__(self): ...

def resolve_tags(tags: Incomplete | None = None):
    """Generate a set of tags for the current run context. Tags are resolved in the order,
    contexts are registered. Argument tags are applied last.

    This function iterates through all run context providers in the registry. Additional context
    providers can be registered as described in
    :py:class:`mlflow.tracking.context.RunContextProvider`.

    :param tags: A dictionary of tags to override. If specified, tags passed in this argument will
                 override those inferred from the context.
    :return: A dictionary of resolved tags.
    """
