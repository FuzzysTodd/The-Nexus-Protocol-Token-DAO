from _typeshed import Incomplete
from mlflow.entities import FileInfo as FileInfo
from mlflow.environment_variables import MLFLOW_S3_ENDPOINT_URL as MLFLOW_S3_ENDPOINT_URL, MLFLOW_S3_IGNORE_TLS as MLFLOW_S3_IGNORE_TLS, MLFLOW_S3_UPLOAD_EXTRA_ARGS as MLFLOW_S3_UPLOAD_EXTRA_ARGS
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.store.artifact.artifact_repo import ArtifactRepository as ArtifactRepository
from mlflow.utils import data_utils as data_utils
from mlflow.utils.file_utils import relative_path_to_artifact_path as relative_path_to_artifact_path

class S3ArtifactRepository(ArtifactRepository):
    """Stores artifacts on Amazon S3."""
    def __init__(self, artifact_uri, access_key_id: Incomplete | None = None, secret_access_key: Incomplete | None = None, session_token: Incomplete | None = None) -> None: ...
    @staticmethod
    def parse_s3_uri(uri):
        """Parse an S3 URI, returning (bucket, path)"""
    @staticmethod
    def get_s3_file_upload_extra_args(): ...
    def log_artifact(self, local_file, artifact_path: Incomplete | None = None) -> None: ...
    def log_artifacts(self, local_dir, artifact_path: Incomplete | None = None) -> None: ...
    def list_artifacts(self, path: Incomplete | None = None): ...
    def delete_artifacts(self, artifact_path: Incomplete | None = None) -> None: ...
