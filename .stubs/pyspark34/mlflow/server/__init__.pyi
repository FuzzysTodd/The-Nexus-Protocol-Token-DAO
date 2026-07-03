from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.server import handlers as handlers
from mlflow.server.handlers import STATIC_PREFIX_ENV_VAR as STATIC_PREFIX_ENV_VAR, get_artifact_handler as get_artifact_handler, get_metric_history_bulk_handler as get_metric_history_bulk_handler, get_model_version_artifact_handler as get_model_version_artifact_handler, search_datasets_handler as search_datasets_handler
from mlflow.server.prometheus_exporter import activate_prometheus_exporter as activate_prometheus_exporter
from mlflow.utils.os import is_windows as is_windows
from mlflow.version import VERSION as VERSION

BACKEND_STORE_URI_ENV_VAR: str
REGISTRY_STORE_URI_ENV_VAR: str
ARTIFACT_ROOT_ENV_VAR: str
ARTIFACTS_DESTINATION_ENV_VAR: str
PROMETHEUS_EXPORTER_ENV_VAR: str
SERVE_ARTIFACTS_ENV_VAR: str
ARTIFACTS_ONLY_ENV_VAR: str
REL_STATIC_DIR: str
app: Incomplete
IS_FLASK_V1: Incomplete
prometheus_metrics_path: Incomplete

def health(): ...
def version(): ...
def serve_artifacts(): ...
def serve_model_version_artifact(): ...
def serve_get_metric_history_bulk(): ...
def serve_search_datasets(): ...
def serve_static_file(path): ...
def serve(): ...
def get_app_client(app_name: str, *args, **kwargs):
    '''
    Instantiate a client provided by an app.

    :param app_name: The app name defined in `setup.py`, e.g., "basic-auth".
    :param args: Additional arguments passed to the app client constructor.
    :param kwargs: Additional keyword arguments passed to the app client constructor.
    :return: An app client instance.
    '''
