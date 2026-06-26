from mlflow.entities._mlflow_object import _MLflowObject
from mlflow.utils.annotations import experimental as experimental

class InputTag(_MLflowObject):
    """Input tag object associated with a dataset."""
    def __init__(self, key: str, value: str) -> None: ...
    def __eq__(self, other: _MLflowObject) -> bool: ...
    @property
    def key(self) -> str:
        """String name of the input tag."""
    @property
    def value(self) -> str:
        """String value of the input tag."""
    def to_proto(self): ...
    @classmethod
    def from_proto(cls, proto): ...
