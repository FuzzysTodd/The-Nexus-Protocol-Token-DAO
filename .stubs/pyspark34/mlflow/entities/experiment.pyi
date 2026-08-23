from _typeshed import Incomplete
from mlflow.entities._mlflow_object import _MLflowObject
from mlflow.entities.experiment_tag import ExperimentTag as ExperimentTag

class Experiment(_MLflowObject):
    """
    Experiment object.
    """
    DEFAULT_EXPERIMENT_NAME: str
    def __init__(self, experiment_id, name, artifact_location, lifecycle_stage, tags: Incomplete | None = None, creation_time: Incomplete | None = None, last_update_time: Incomplete | None = None) -> None: ...
    @property
    def experiment_id(self):
        """String ID of the experiment."""
    @property
    def name(self):
        """String name of the experiment."""
    @property
    def artifact_location(self):
        """String corresponding to the root artifact URI for the experiment."""
    @property
    def lifecycle_stage(self):
        """Lifecycle stage of the experiment. Can either be 'active' or 'deleted'."""
    @property
    def tags(self):
        """Tags that have been set on the experiment."""
    @property
    def creation_time(self): ...
    @property
    def last_update_time(self): ...
    @classmethod
    def from_proto(cls, proto): ...
    def to_proto(self): ...
