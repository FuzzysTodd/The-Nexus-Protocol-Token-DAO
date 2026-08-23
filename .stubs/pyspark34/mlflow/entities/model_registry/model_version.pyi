from _typeshed import Incomplete
from mlflow.entities.model_registry._model_registry_entity import _ModelRegistryEntity
from mlflow.entities.model_registry.model_version_status import ModelVersionStatus as ModelVersionStatus
from mlflow.entities.model_registry.model_version_tag import ModelVersionTag as ModelVersionTag

class ModelVersion(_ModelRegistryEntity):
    """
    MLflow entity for Model Version.
    """
    def __init__(self, name, version, creation_timestamp, last_updated_timestamp: Incomplete | None = None, description: Incomplete | None = None, user_id: Incomplete | None = None, current_stage: Incomplete | None = None, source: Incomplete | None = None, run_id: Incomplete | None = None, status=..., status_message: Incomplete | None = None, tags: Incomplete | None = None, run_link: Incomplete | None = None, aliases: Incomplete | None = None) -> None: ...
    @property
    def name(self):
        """String. Unique name within Model Registry."""
    @name.setter
    def name(self, new_name) -> None: ...
    @property
    def version(self):
        """version"""
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
    def user_id(self):
        """String. User ID that created this model version."""
    @property
    def current_stage(self):
        """String. Current stage of this model version."""
    @current_stage.setter
    def current_stage(self, stage) -> None: ...
    @property
    def source(self):
        """String. Source path for the model."""
    @property
    def run_id(self):
        """String. MLflow run ID that generated this model."""
    @property
    def run_link(self):
        """String. MLflow run link referring to the exact run that generated this model version."""
    @property
    def status(self):
        """String. Current Model Registry status for this model."""
    @property
    def status_message(self):
        """String. Descriptive message for error status conditions."""
    @property
    def tags(self):
        """Dictionary of tag key (string) -> tag value for the current model version."""
    @property
    def aliases(self):
        """List of aliases (string) for the current model version."""
    @aliases.setter
    def aliases(self, aliases) -> None: ...
    @classmethod
    def from_proto(cls, proto): ...
    def to_proto(self): ...
