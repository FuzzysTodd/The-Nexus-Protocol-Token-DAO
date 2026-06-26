import abc
from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.protos.databricks_uc_registry_messages_pb2 import GenerateTemporaryModelVersionCredentialsRequest as GenerateTemporaryModelVersionCredentialsRequest, GenerateTemporaryModelVersionCredentialsResponse as GenerateTemporaryModelVersionCredentialsResponse, MODEL_VERSION_OPERATION_READ as MODEL_VERSION_OPERATION_READ
from mlflow.protos.databricks_uc_registry_service_pb2 import UcModelRegistryService as UcModelRegistryService
from mlflow.store._unity_catalog.registry.utils import get_artifact_repo_from_storage_info as get_artifact_repo_from_storage_info, get_full_name_from_sc as get_full_name_from_sc
from mlflow.store.artifact.artifact_repo import ArtifactRepository as ArtifactRepository
from mlflow.store.artifact.utils.models import get_model_name_and_version as get_model_name_and_version
from mlflow.utils.databricks_utils import get_databricks_host_creds as get_databricks_host_creds
from mlflow.utils.proto_json_utils import message_to_json as message_to_json
from mlflow.utils.rest_utils import call_endpoint as call_endpoint, extract_api_info_for_service as extract_api_info_for_service
from mlflow.utils.uri import get_databricks_profile_uri_from_artifact_uri as get_databricks_profile_uri_from_artifact_uri, get_db_info_from_uri as get_db_info_from_uri, is_databricks_unity_catalog_uri as is_databricks_unity_catalog_uri

class UnityCatalogModelsArtifactRepository(ArtifactRepository, metaclass=abc.ABCMeta):
    """
    Performs storage operations on artifacts controlled by a Unity Catalog model registry

    Temporary scoped tokens for the appropriate cloud storage locations are fetched from the
    remote backend and used to download model artifacts.

    The artifact_uri is expected to be of the form `models:/<model_name>/<model_version>`

    Note : This artifact repository is meant is to be instantiated by the ModelsArtifactRepository
    when the client is pointing to a Unity Catalog model registry.
    """
    registry_uri: Incomplete
    client: Incomplete
    model_name: Incomplete
    def __init__(self, artifact_uri, registry_uri) -> None: ...
    def list_artifacts(self, path: Incomplete | None = None): ...
    def download_artifacts(self, artifact_path, dst_path: Incomplete | None = None): ...
    def log_artifact(self, local_file, artifact_path: Incomplete | None = None) -> None: ...
    def log_artifacts(self, local_dir, artifact_path: Incomplete | None = None) -> None: ...
    def delete_artifacts(self, artifact_path: Incomplete | None = None) -> None: ...
