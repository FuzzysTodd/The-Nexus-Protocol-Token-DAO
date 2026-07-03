from _typeshed import Incomplete
from mlflow.entities import FileInfo as FileInfo
from mlflow.environment_variables import MLFLOW_ARTIFACT_UPLOAD_DOWNLOAD_TIMEOUT as MLFLOW_ARTIFACT_UPLOAD_DOWNLOAD_TIMEOUT, MLFLOW_GCS_DEFAULT_TIMEOUT as MLFLOW_GCS_DEFAULT_TIMEOUT, MLFLOW_GCS_DOWNLOAD_CHUNK_SIZE as MLFLOW_GCS_DOWNLOAD_CHUNK_SIZE, MLFLOW_GCS_UPLOAD_CHUNK_SIZE as MLFLOW_GCS_UPLOAD_CHUNK_SIZE
from mlflow.store.artifact.artifact_repo import ArtifactRepository as ArtifactRepository
from mlflow.utils.file_utils import relative_path_to_artifact_path as relative_path_to_artifact_path

class GCSArtifactRepository(ArtifactRepository):
    """
    Stores artifacts on Google Cloud Storage.

    :param artifact_uri: URI of GCS bucket
    :param client: Optional. The client to use for GCS operations; a default
                       client object will be created if unspecified, using default
                       credentials as described in https://google-cloud.readthedocs.io/en/latest/core/auth.html
    """
    client: Incomplete
    def __init__(self, artifact_uri, client: Incomplete | None = None) -> None: ...
    @staticmethod
    def parse_gcs_uri(uri):
        """Parse an GCS URI, returning (bucket, path)"""
    def log_artifact(self, local_file, artifact_path: Incomplete | None = None) -> None: ...
    def log_artifacts(self, local_dir, artifact_path: Incomplete | None = None) -> None: ...
    def list_artifacts(self, path: Incomplete | None = None): ...
    def delete_artifacts(self, artifact_path: Incomplete | None = None) -> None: ...
