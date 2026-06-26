from mlflow.entities._mlflow_object import _MLflowObject

class Param(_MLflowObject):
    """
    Parameter object.
    """
    def __init__(self, key, value) -> None: ...
    @property
    def key(self):
        """String key corresponding to the parameter name."""
    @property
    def value(self):
        """String value of the parameter."""
    def to_proto(self): ...
    @classmethod
    def from_proto(cls, proto): ...
    def __eq__(self, __o): ...
    def __hash__(self): ...
