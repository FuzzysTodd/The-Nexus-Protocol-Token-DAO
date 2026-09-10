from mlflow.entities._mlflow_object import _MLflowObject

class Metric(_MLflowObject):
    """
    Metric object.
    """
    def __init__(self, key, value, timestamp, step) -> None: ...
    @property
    def key(self):
        """String key corresponding to the metric name."""
    @property
    def value(self):
        """Float value of the metric."""
    @property
    def timestamp(self):
        """Metric timestamp as an integer (milliseconds since the Unix epoch)."""
    @property
    def step(self):
        """Integer metric step (x-coordinate)."""
    def to_proto(self): ...
    @classmethod
    def from_proto(cls, proto): ...
    def __eq__(self, __o): ...
    def __hash__(self): ...
