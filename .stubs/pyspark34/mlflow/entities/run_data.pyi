from _typeshed import Incomplete
from mlflow.entities._mlflow_object import _MLflowObject
from mlflow.entities.metric import Metric as Metric
from mlflow.entities.param import Param as Param
from mlflow.entities.run_tag import RunTag as RunTag

class RunData(_MLflowObject):
    """
    Run data (metrics and parameters).
    """
    def __init__(self, metrics: Incomplete | None = None, params: Incomplete | None = None, tags: Incomplete | None = None) -> None:
        """
        Construct a new :py:class:`mlflow.entities.RunData` instance.
        :param metrics: List of :py:class:`mlflow.entities.Metric`.
        :param params: List of :py:class:`mlflow.entities.Param`.
        :param tags: List of :py:class:`mlflow.entities.RunTag`.
        """
    @property
    def metrics(self):
        """
        Dictionary of string key -> metric value for the current run.
        For each metric key, the metric value with the latest timestamp is returned. In case there
        are multiple values with the same latest timestamp, the maximum of these values is returned.
        """
    @property
    def params(self):
        """Dictionary of param key (string) -> param value for the current run."""
    @property
    def tags(self):
        """Dictionary of tag key (string) -> tag value for the current run."""
    def to_proto(self): ...
    def to_dictionary(self): ...
    @classmethod
    def from_proto(cls, proto): ...
