from _typeshed import Incomplete
from mlflow.entities.model_registry._model_registry_entity import _ModelRegistryEntity
from mlflow.entities.model_registry.model_version import ModelVersion as ModelVersion
from mlflow.entities.model_registry.registered_model_alias import RegisteredModelAlias as RegisteredModelAlias
from mlflow.entities.model_registry.registered_model_tag import RegisteredModelTag as RegisteredModelTag

class RegisteredModel(_ModelRegistryEntity):
    """
    MLflow entity for Registered Model.
    """
    def __init__(self, name, creation_timestamp: Incomplete | None = None, last_updated_timestamp: Incomplete | None = None, description: Incomplete | None = None, latest_versions: Incomplete | None = None, tags: Incomplete | None = None, aliases: Incomplete | None = None) -> None: ...
    @property
    def name(self):
        """String. Registered model name."""
    @name.setter
    def name(self, new_name) -> None: ...
    @property
    def creation_timestamp(self):
        """Integer. Model version creation timestamp (milliseconds since the Unix epoch)."""
    @property
    def last_updated_timestamp(self):
        """Integer. Timestamp of last update for this model version (milliseconds since the Unix
        epoch)."""
    @last_updated_timestamp.setter
    def last_updated_timestamp(self, updated_timestamp) -> None: ...
    @property
    def description(self):
        """String. Description"""
    @description.setter
    def description(self, description) -> None: ...
    @property
    def latest_versions(self):
        """List of the latest :py:class:`mlflow.entities.model_registry.ModelVersion` instances
        for each stage"""
    @latest_versions.setter
    def latest_versions(self, latest_versions) -> None: ...
    @property
    def tags(self):
        """Dictionary of tag key (string) -> tag value for the current registered model."""
    @property
    def aliases(self):
        """Dictionary of aliases (string) -> version for the current registered model."""
    @classmethod
    def from_proto(cls, proto): ...
    def to_proto(self): ...
