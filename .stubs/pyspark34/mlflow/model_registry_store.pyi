from .shared_platform_utils import create_artifact as create_artifact, delete_artifact as delete_artifact, is_artifact_name_in_use as is_artifact_name_in_use, list_workspace_artifacts as list_workspace_artifacts
from .synapse_mlflow_utils import check_model_name as check_model_name, get_mlflow_env_config as get_mlflow_env_config, record_all_public_functions as record_all_public_functions, timed as timed
from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import RESOURCE_ALREADY_EXISTS as RESOURCE_ALREADY_EXISTS
from mlflow.store.model_registry.rest_store import RestStore as RestStore
from mlflow.utils.rest_utils import MlflowHostCreds as MlflowHostCreds
from urllib.parse import urlparse as urlparse

logger: Incomplete

class TridentMLflowModelRegistryStore(Incomplete):
    def __init__(self) -> None: ...
    @staticmethod
    def get_host_credentials(): ...
    def delete_registered_model(self, name) -> None: ...
    def create_registered_model(self, name, tags: Incomplete | None = None, description: Incomplete | None = None): ...
