from mlflow.data.dataset_source import DatasetSource as DatasetSource
from mlflow.utils.annotations import experimental as experimental
from typing import Any, Dict

class CodeDatasetSource(DatasetSource):
    def __init__(self, tags: Dict[Any, Any]) -> None: ...
    def load(self, **kwargs) -> None:
        """
        Load is not implemented for Code Dataset Source.
        """
