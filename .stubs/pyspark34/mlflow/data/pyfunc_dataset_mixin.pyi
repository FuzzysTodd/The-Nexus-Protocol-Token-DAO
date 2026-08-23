import abc
from _typeshed import Incomplete
from abc import abstractmethod
from dataclasses import dataclass
from mlflow.models.evaluation.base import EvaluationDataset as EvaluationDataset
from mlflow.models.utils import PyFuncInput as PyFuncInput, PyFuncOutput as PyFuncOutput
from typing import List

@dataclass
class PyFuncInputsOutputs:
    inputs: List[PyFuncInput]
    outputs: List[PyFuncOutput] = ...
    def __init__(self, inputs, outputs) -> None: ...

class PyFuncConvertibleDatasetMixin(metaclass=abc.ABCMeta):
    @abstractmethod
    def to_pyfunc(self) -> PyFuncInputsOutputs:
        """
        Converts the dataset to a collection of pyfunc inputs and outputs for model
        evaluation. Required for use with mlflow.evaluate().
        May not be implemented by all datasets.
        """
    @abstractmethod
    def to_evaluation_dataset(self, path: Incomplete | None = None, feature_names: Incomplete | None = None) -> EvaluationDataset:
        """
        Converts the dataset to an EvaluationDataset for model evaluation.
        May not be implemented by all datasets.
        """
