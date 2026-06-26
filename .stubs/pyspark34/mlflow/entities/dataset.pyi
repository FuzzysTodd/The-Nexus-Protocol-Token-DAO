from mlflow.entities._mlflow_object import _MLflowObject
from mlflow.utils.annotations import experimental as experimental

class Dataset(_MLflowObject):
    """Dataset object associated with an experiment."""
    def __init__(self, name: str, digest: str, source_type: str, source: str, schema: str | None = None, profile: str | None = None) -> None: ...
    def __eq__(self, other: _MLflowObject) -> bool: ...
    @property
    def name(self) -> str:
        """String name of the dataset."""
    @property
    def digest(self) -> str:
        """String digest of the dataset."""
    @property
    def source_type(self) -> str:
        """String source_type of the dataset."""
    @property
    def source(self) -> str:
        """String source of the dataset."""
    @property
    def schema(self) -> str:
        """String schema of the dataset."""
    @property
    def profile(self) -> str:
        """String profile of the dataset."""
    def to_proto(self): ...
    @classmethod
    def from_proto(cls, proto): ...
