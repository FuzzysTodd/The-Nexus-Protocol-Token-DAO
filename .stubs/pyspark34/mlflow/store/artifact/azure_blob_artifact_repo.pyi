from _typeshed import Incomplete
from mlflow.entities import FileInfo as FileInfo
from mlflow.environment_variables import MLFLOW_ARTIFACT_UPLOAD_DOWNLOAD_TIMEOUT as MLFLOW_ARTIFACT_UPLOAD_DOWNLOAD_TIMEOUT
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.store.artifact.artifact_repo import ArtifactRepository as ArtifactRepository

class AzureBlobArtifactRepository(ArtifactRepository):
    """
    Stores artifacts on Azure Blob Storage.

    This repository is used with URIs of the form
    ``wasbs://<container-name>@<ystorage-account-name>.blob.core.windows.net/<path>``,
    following the same URI scheme as Hadoop on Azure blob storage. It requires either that:
    - Azure storage connection string is in the env var ``AZURE_STORAGE_CONNECTION_STRING``
    - Azure storage access key is in the env var ``AZURE_STORAGE_ACCESS_KEY``
    - DefaultAzureCredential is configured
    """
    write_timeout: Incomplete
    client: Incomplete
    def __init__(self, artifact_uri, client: Incomplete | None = None) -> None: ...
    @staticmethod
    def parse_wasbs_uri(uri):
        """Parse a wasbs:// URI, returning (container, storage_account, path, api_uri_suffix)."""
    def log_artifact(self, local_file, artifact_path: Incomplete | None = None) -> None: ...
    def log_artifacts(self, local_dir, artifact_path: Incomplete | None = None) -> None: ...
    def list_artifacts(self, path: Incomplete | None = None): ...
    def delete_artifacts(self, artifact_path: Incomplete | None = None) -> None: ...
