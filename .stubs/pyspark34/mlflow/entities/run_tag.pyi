from mlflow.entities._mlflow_object import _MLflowObject

class RunTag(_MLflowObject):
    """Tag object associated with a run."""
    def __init__(self, key, value) -> None: ...
    def __eq__(self, other): ...
    @property
    def key(self):
        """String name of the tag."""
    @property
    def value(self):
        """String value of the tag."""
    def to_proto(self): ...
    @classmethod
    def from_proto(cls, proto): ...
