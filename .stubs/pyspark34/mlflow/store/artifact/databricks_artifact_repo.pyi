from _typeshed import Incomplete
from mlflow.azure.client import patch_adls_file_upload as patch_adls_file_upload, patch_adls_flush as patch_adls_flush, put_adls_file_creation as put_adls_file_creation, put_block as put_block, put_block_list as put_block_list
from mlflow.entities import FileInfo as FileInfo
from mlflow.environment_variables import MLFLOW_ENABLE_ARTIFACTS_PROGRESS_BAR as MLFLOW_ENABLE_ARTIFACTS_PROGRESS_BAR, MLFLOW_ENABLE_MULTIPART_DOWNLOAD as MLFLOW_ENABLE_MULTIPART_DOWNLOAD
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_artifacts_pb2 import ArtifactCredentialType as ArtifactCredentialType, CompleteMultipartUpload as CompleteMultipartUpload, CreateMultipartUpload as CreateMultipartUpload, DatabricksMlflowArtifactsService as DatabricksMlflowArtifactsService, GetCredentialsForRead as GetCredentialsForRead, GetCredentialsForWrite as GetCredentialsForWrite, GetPresignedUploadPartUrl as GetPresignedUploadPartUrl, PartEtag as PartEtag
from mlflow.protos.databricks_pb2 import INTERNAL_ERROR as INTERNAL_ERROR, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.protos.service_pb2 import GetRun as GetRun, ListArtifacts as ListArtifacts, MlflowService as MlflowService
from mlflow.store.artifact.artifact_repo import ArtifactRepository as ArtifactRepository
from mlflow.utils import chunk_list as chunk_list
from mlflow.utils.databricks_utils import get_databricks_host_creds as get_databricks_host_creds
from mlflow.utils.file_utils import ArtifactProgressBar as ArtifactProgressBar, download_file_using_http_uri as download_file_using_http_uri, parallelized_download_file_using_http_uri as parallelized_download_file_using_http_uri, read_chunk as read_chunk, relative_path_to_artifact_path as relative_path_to_artifact_path
from mlflow.utils.proto_json_utils import message_to_json as message_to_json
from mlflow.utils.request_utils import cloud_storage_http_request as cloud_storage_http_request, download_chunk as download_chunk
from mlflow.utils.rest_utils import augmented_raise_for_status as augmented_raise_for_status, call_endpoint as call_endpoint, extract_api_info_for_service as extract_api_info_for_service
from mlflow.utils.uri import extract_and_normalize_path as extract_and_normalize_path, get_databricks_profile_uri_from_artifact_uri as get_databricks_profile_uri_from_artifact_uri, is_databricks_acled_artifacts_uri as is_databricks_acled_artifacts_uri, is_valid_dbfs_uri as is_valid_dbfs_uri, remove_databricks_profile_info_from_artifact_uri as remove_databricks_profile_info_from_artifact_uri

class DatabricksArtifactRepository(ArtifactRepository):
    """
    Performs storage operations on artifacts in the access-controlled
    `dbfs:/databricks/mlflow-tracking` location.

    Signed access URIs for S3 / Azure Blob Storage are fetched from the MLflow service and used to
    read and write files from/to this location.

    The artifact_uri is expected to be of the form
    dbfs:/databricks/mlflow-tracking/<EXP_ID>/<RUN_ID>/
    """
    databricks_profile_uri: Incomplete
    run_id: Incomplete
    run_relative_artifact_repo_root_path: Incomplete
    chunk_thread_pool: Incomplete
    def __init__(self, artifact_uri) -> None: ...
    def log_artifact(self, local_file, artifact_path: Incomplete | None = None) -> None: ...
    def log_artifacts(self, local_dir, artifact_path: Incomplete | None = None) -> None:
        """
        Parallelized implementation of `log_artifacts` for Databricks.
        """
    def list_artifacts(self, path: Incomplete | None = None): ...
    def delete_artifacts(self, artifact_path: Incomplete | None = None) -> None: ...
