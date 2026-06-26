from _typeshed import Incomplete
from mlflow.entities import FileInfo as FileInfo
from mlflow.environment_variables import MLFLOW_ARTIFACT_UPLOAD_DOWNLOAD_TIMEOUT as MLFLOW_ARTIFACT_UPLOAD_DOWNLOAD_TIMEOUT
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.store.artifact.artifact_repo import ArtifactRepository as ArtifactRepository

class AzureDataLakeArtifactRepository(ArtifactRepository):
    """
    Stores artifacts on Azure Data Lake Storage Gen2.

    This repository is used with URIs of the form
    ``abfs[s]://file_system@account_name.dfs.core.windows.net/<path>/<path>``.

    :param credential: Azure credential (see options in https://learn.microsoft.com/en-us/python/api/azure-core/azure.core.credentials?view=azure-python)
                       to use to authenticate to storage
    """
    write_timeout: Incomplete
    fs_client: Incomplete
    base_data_lake_directory: Incomplete
    def __init__(self, artifact_uri, credential) -> None: ...
    def log_artifact(self, local_file, artifact_path: Incomplete | None = None) -> None: ...
    def log_artifacts(self, local_dir, artifact_path: Incomplete | None = None) -> None: ...
    def list_artifacts(self, path: Incomplete | None = None): ...
    def delete_artifacts(self, artifact_path: Incomplete | None = None) -> None: ...
