from mlflow.environment_variables import MLFLOW_TRACKING_AWS_SIGV4 as MLFLOW_TRACKING_AWS_SIGV4, MLFLOW_TRACKING_CLIENT_CERT_PATH as MLFLOW_TRACKING_CLIENT_CERT_PATH, MLFLOW_TRACKING_INSECURE_TLS as MLFLOW_TRACKING_INSECURE_TLS, MLFLOW_TRACKING_SERVER_CERT_PATH as MLFLOW_TRACKING_SERVER_CERT_PATH, MLFLOW_TRACKING_TOKEN as MLFLOW_TRACKING_TOKEN, MLFLOW_TRACKING_URI as MLFLOW_TRACKING_URI
from mlflow.store.db.db_types import DATABASE_ENGINES as DATABASE_ENGINES
from mlflow.store.tracking import DEFAULT_LOCAL_FILE_AND_ARTIFACT_PATH as DEFAULT_LOCAL_FILE_AND_ARTIFACT_PATH
from mlflow.store.tracking.file_store import FileStore as FileStore
from mlflow.store.tracking.rest_store import RestStore as RestStore
from mlflow.tracking._tracking_service.registry import TrackingStoreRegistry as TrackingStoreRegistry
from mlflow.utils import rest_utils as rest_utils
from mlflow.utils.credentials import read_mlflow_creds as read_mlflow_creds
from mlflow.utils.databricks_utils import get_databricks_host_creds as get_databricks_host_creds
from mlflow.utils.file_utils import path_to_local_file_uri as path_to_local_file_uri
from pathlib import Path

def is_tracking_uri_set():
    """Returns True if the tracking URI has been set, False otherwise."""
def set_tracking_uri(uri: str | Path) -> None:
    '''
    Set the tracking server URI. This does not affect the
    currently active run (if one exists), but takes effect for successive runs.

    :param uri:

                - An empty string, or a local file path, prefixed with ``file:/``. Data is stored
                  locally at the provided file (or ``./mlruns`` if empty).
                - An HTTP URI like ``https://my-tracking-server:5000``.
                - A Databricks workspace, provided as the string "databricks" or, to use a
                  Databricks CLI
                  `profile <https://github.com/databricks/databricks-cli#installation>`_,
                  "databricks://<profileName>".
                - A :py:class:`pathlib.Path` instance

    .. test-code-block:: python
        :caption: Example

        import mlflow

        mlflow.set_tracking_uri("file:///tmp/my_tracking")
        tracking_uri = mlflow.get_tracking_uri()
        print("Current tracking uri: {}".format(tracking_uri))

    .. code-block:: text
        :caption: Output

        Current tracking uri: file:///tmp/my_tracking
    '''
def get_tracking_uri() -> str:
    '''
    Get the current tracking URI. This may not correspond to the tracking URI of
    the currently active run, since the tracking URI can be updated via ``set_tracking_uri``.

    :return: The tracking URI.

    .. code-block:: python
        :caption: Example

        import mlflow

        # Get the current tracking uri
        tracking_uri = mlflow.get_tracking_uri()
        print("Current tracking uri: {}".format(tracking_uri))

    .. code-block:: text
        :caption: Output

        Current tracking uri: file:///.../mlruns
    '''
