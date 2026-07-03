import abc
from ..utils._model_runtime import ModelRuntime as ModelRuntime
from _typeshed import Incomplete
from abc import ABC
from typing import Any, Mapping

class BaseModelConverter(ABC, metaclass=abc.ABCMeta):
    """Base interface for model converters. All converters should
    inherit this class and implement abstract methods.
    """
    def __init__(self) -> None: ...
    def convert(self, model, meta_data: Incomplete | None = None):
        """
        Convert the model to the MLFlow format.

        Parameters
        ----------
        model : object
        meta_data : Mapping[str, Any]

        Returns
        -------
        str
            Path to the directory with the converted model,
            or None if the converter cannot convert the given model.
        """

class SklearnModelConverter(BaseModelConverter):
    """
    Scikit-learn model converter. Supports scikit-learn classifiers and regressors.
    """
class PytorchModelConverter(BaseModelConverter):
    """
    Pytorch model converter. Supports Pytorch models.
    """
class OnnxModelConverter(BaseModelConverter):
    """
    ONNX model converter. Supports ONNX models.
    """
class TensorflowModelConverter(BaseModelConverter):
    """
    Tensorflow model converter. Supports tensorflow models.
    """
class XGBoostModelConverter(BaseModelConverter):
    """
    XGBoost model converter. Supports ONNX models.
    """
class LightGBMModelConverter(BaseModelConverter):
    """
    Lightgbm model converter. Supports ONNX models.
    """

def is_mlflow_model(path):
    """
    Check if the given directory contains an MLFlow model.

    Parameters
    ----------
    path : str
        Path to the dir.

    Returns
    -------
    boolean
        True if the directory contains an MLFlow model, False otherwise.
    """
def convert_to_mlflow(runtime: str, model, meta_data: Mapping[str, Any] = {}):
    """
    Convert the given model to the MLFlow format.

    Parameters
    ----------
    runtime : ModelRuntime type
        Support Onnx, Pytorch and Sklearn model currently.
    model : object
    meta_data : Mapping[str, Any]

    Returns
    -------
    str
        Path to the directory with the converted model
    """
