from mlflow.entities._mlflow_object import _MLflowObject
from mlflow.entities.dataset import Dataset as Dataset
from mlflow.entities.input_tag import InputTag as InputTag
from mlflow.utils.annotations import experimental as experimental
from typing import List

class DatasetInput(_MLflowObject):
    """DatasetInput object associated with an experiment."""
    def __init__(self, dataset: Dataset, tags: List[InputTag] | None = None) -> None: ...
    def __eq__(self, other: _MLflowObject) -> bool: ...
    @property
    def tags(self) -> List[InputTag]:
        """Array of input tags."""
    @property
    def dataset(self) -> Dataset:
        """Dataset."""
    def to_proto(self): ...
    @classmethod
    def from_proto(cls, proto): ...
