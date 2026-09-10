from mlflow.entities.model_registry import ModelVersion as ModelVersion, ModelVersionTag as ModelVersionTag, RegisteredModel as RegisteredModel, RegisteredModelAlias as RegisteredModelAlias, RegisteredModelTag as RegisteredModelTag
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_uc_registry_messages_pb2 import ModelVersion as ProtoModelVersion, ModelVersionTag as ProtoModelVersionTag, RegisteredModel as ProtoRegisteredModel, RegisteredModelTag as ProtoRegisteredModelTag, TemporaryCredentials as TemporaryCredentials
from mlflow.store.artifact.artifact_repo import ArtifactRepository as ArtifactRepository
from typing import List

def uc_model_version_status_to_string(status): ...
def model_version_from_uc_proto(uc_proto: ProtoModelVersion) -> ModelVersion: ...
def registered_model_from_uc_proto(uc_proto: ProtoRegisteredModel) -> RegisteredModel: ...
def uc_registered_model_tag_from_mlflow_tags(tags: List[RegisteredModelTag] | None) -> List[ProtoRegisteredModelTag]: ...
def uc_model_version_tag_from_mlflow_tags(tags: List[ModelVersionTag] | None) -> List[ProtoModelVersionTag]: ...
def get_artifact_repo_from_storage_info(storage_location: str, scoped_token: TemporaryCredentials) -> ArtifactRepository:
    """
    Get an ArtifactRepository instance capable of reading/writing to a UC model version's
    file storage location
    :param storage_location: Storage location of the model version
    :param scoped_token: Protobuf scoped token to use to authenticate to blob storage
    """
def get_full_name_from_sc(name, spark) -> str:
    """
    Constructs the full name of a registered model using the active catalog and schema in a spark
    session / context.
    :param name: the model name provided by the user
    :param spark: the active spark session
    """
