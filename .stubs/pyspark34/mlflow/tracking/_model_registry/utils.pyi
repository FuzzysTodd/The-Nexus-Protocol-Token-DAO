from mlflow.environment_variables import MLFLOW_REGISTRY_URI as MLFLOW_REGISTRY_URI, MLFLOW_TRACKING_AWS_SIGV4 as MLFLOW_TRACKING_AWS_SIGV4, MLFLOW_TRACKING_CLIENT_CERT_PATH as MLFLOW_TRACKING_CLIENT_CERT_PATH, MLFLOW_TRACKING_INSECURE_TLS as MLFLOW_TRACKING_INSECURE_TLS, MLFLOW_TRACKING_PASSWORD as MLFLOW_TRACKING_PASSWORD, MLFLOW_TRACKING_SERVER_CERT_PATH as MLFLOW_TRACKING_SERVER_CERT_PATH, MLFLOW_TRACKING_TOKEN as MLFLOW_TRACKING_TOKEN, MLFLOW_TRACKING_USERNAME as MLFLOW_TRACKING_USERNAME
from mlflow.store._unity_catalog.registry.rest_store import UcModelRegistryStore as UcModelRegistryStore
from mlflow.store.db.db_types import DATABASE_ENGINES as DATABASE_ENGINES
from mlflow.store.model_registry.databricks_workspace_model_registry_rest_store import DatabricksWorkspaceModelRegistryRestStore as DatabricksWorkspaceModelRegistryRestStore
from mlflow.store.model_registry.file_store import FileStore as FileStore
from mlflow.store.model_registry.rest_store import RestStore as RestStore
from mlflow.tracking._model_registry.registry import ModelRegistryStoreRegistry as ModelRegistryStoreRegistry
from mlflow.tracking._tracking_service.utils import get_tracking_uri as get_tracking_uri
from mlflow.utils import rest_utils as rest_utils
from mlflow.utils.databricks_utils import get_databricks_host_creds as get_databricks_host_creds, warn_on_deprecated_cross_workspace_registry_uri as warn_on_deprecated_cross_workspace_registry_uri

def set_registry_uri(uri: str) -> None:
    '''
    Set the registry server URI. This method is especially useful if you have a registry server
    that\'s different from the tracking server.

    :param uri:

                - An empty string, or a local file path, prefixed with ``file:/``. Data is stored
                  locally at the provided file (or ``./mlruns`` if empty).
                - An HTTP URI like ``https://my-tracking-server:5000``.
                - A Databricks workspace, provided as the string "databricks" or, to use a
                  Databricks CLI
                  `profile <https://github.com/databricks/databricks-cli#installation>`_,
                  "databricks://<profileName>".

    .. code-block:: python
        :caption: Example

        import mflow

        # Set model registry uri, fetch the set uri, and compare
        # it with the tracking uri. They should be different
        mlflow.set_registry_uri("sqlite:////tmp/registry.db")
        mr_uri = mlflow.get_registry_uri()
        print("Current registry uri: {}".format(mr_uri))
        tracking_uri = mlflow.get_tracking_uri()
        print("Current tracking uri: {}".format(tracking_uri))

        # They should be different
        assert tracking_uri != mr_uri

    .. code-block:: text
        :caption: Output

        Current registry uri: sqlite:////tmp/registry.db
        Current tracking uri: file:///.../mlruns
    '''
def get_registry_uri() -> str:
    '''
    Get the current registry URI. If none has been specified, defaults to the tracking URI.

    :return: The registry URI.

    .. code-block:: python
        :caption: Example

        # Get the current model registry uri
        mr_uri = mlflow.get_registry_uri()
        print("Current model registry uri: {}".format(mr_uri))

        # Get the current tracking uri
        tracking_uri = mlflow.get_tracking_uri()
        print("Current tracking uri: {}".format(tracking_uri))

        # They should be the same
        assert mr_uri == tracking_uri

    .. code-block:: text
        :caption: Output

        Current model registry uri: file:///.../mlruns
        Current tracking uri: file:///.../mlruns
    '''
def get_default_host_creds(store_uri): ...
