from _typeshed import Incomplete
from mlflow.entities import FileInfo as FileInfo
from mlflow.environment_variables import MLFLOW_ENABLE_MULTIPART_DOWNLOAD as MLFLOW_ENABLE_MULTIPART_DOWNLOAD
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.store.artifact.artifact_repo import ArtifactRepository as ArtifactRepository
from mlflow.store.artifact.utils.models import get_model_name_and_version as get_model_name_and_version, is_using_databricks_registry as is_using_databricks_registry
from mlflow.utils.databricks_utils import get_databricks_host_creds as get_databricks_host_creds, warn_on_deprecated_cross_workspace_registry_uri as warn_on_deprecated_cross_workspace_registry_uri
from mlflow.utils.file_utils import download_file_using_http_uri as download_file_using_http_uri, parallelized_download_file_using_http_uri as parallelized_download_file_using_http_uri
from mlflow.utils.request_utils import download_chunk as download_chunk
from mlflow.utils.rest_utils import http_request as http_request
from mlflow.utils.uri import get_databricks_profile_uri_from_artifact_uri as get_databricks_profile_uri_from_artifact_uri

REGISTRY_LIST_ARTIFACTS_ENDPOINT: str
REGISTRY_ARTIFACT_PRESIGNED_URI_ENDPOINT: str

class DatabricksModelsArtifactRepository(ArtifactRepository):
    """
    Performs storage operations on artifacts controlled by a Databricks-hosted model registry.

    Signed access URIs for the appropriate cloud storage locations are fetched from the
    MLflow service and used to download model artifacts.

    The artifact_uri is expected to be of the form
    - `models:/<model_name>/<model_version>`
    - `models:/<model_name>/<stage>`  (refers to the latest model version in the given stage)
    - `models:/<model_name>/latest`  (refers to the latest of all model versions)
    - `models://<profile>/<model_name>/<model_version or stage or 'latest'>`

    Note : This artifact repository is meant is to be instantiated by the ModelsArtifactRepository
    when the client is pointing to a Databricks-hosted model registry.
    """
    databricks_profile_uri: Incomplete
    chunk_thread_pool: Incomplete
    def __init__(self, artifact_uri) -> None: ...
    def list_artifacts(self, path: Incomplete | None = None): ...
    def log_artifact(self, local_file, artifact_path: Incomplete | None = None) -> None: ...
    def log_artifacts(self, local_dir, artifact_path: Incomplete | None = None) -> None: ...
    def delete_artifacts(self, artifact_path: Incomplete | None = None) -> None: ...
