from mlflow.entities._mlflow_object import _MLflowObject
from mlflow.entities.run_data import RunData as RunData
from mlflow.entities.run_info import RunInfo as RunInfo
from mlflow.entities.run_inputs import RunInputs as RunInputs
from mlflow.exceptions import MlflowException as MlflowException
from typing import Any, Dict

class Run(_MLflowObject):
    """
    Run object.
    """
    def __init__(self, run_info: RunInfo, run_data: RunData, run_inputs: RunInputs | None = None) -> None: ...
    @property
    def info(self) -> RunInfo:
        """
        The run metadata, such as the run id, start time, and status.

        :rtype: :py:class:`mlflow.entities.RunInfo`
        """
    @property
    def data(self) -> RunData:
        """
        The run data, including metrics, parameters, and tags.

        :rtype: :py:class:`mlflow.entities.RunData`
        """
    @property
    def inputs(self) -> RunInputs:
        """
        The run inputs, including dataset inputs

        :rtype: :py:class:`mlflow.entities.RunData`
        """
    def to_proto(self): ...
    @classmethod
    def from_proto(cls, proto): ...
    def to_dictionary(self) -> Dict[Any, Any]: ...
