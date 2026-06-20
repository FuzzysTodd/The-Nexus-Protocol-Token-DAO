import abc
from ..utils._functions import BaseFunction as BaseFunction
from ..utils._mlflow_convert import is_mlflow_model as is_mlflow_model
from ..utils._model_runtime import ModelRuntime as ModelRuntime
from abc import ABC
from typing import Mapping

class BaseModelLoader(ABC, metaclass=abc.ABCMeta):
    """Base interface for model loaders. All loaders should
    inherit this class and implement abstract methods.
    """
    def __init__(self) -> None: ...
    def load(self, model_uri: str = '', functions={}):
        """
        Load model.

        Parameters
        ----------
        model_uri : str
            Path to the model file.
        functions : Mapping[str, BaseFunction]

        Returns
        -------
        object:
            Model type or None.
        """

class SklearnModelLoader(BaseModelLoader):
    """
    Scikit-learn model loader. Supports scikit-learn classifiers and regressors.
    """
class PytorchModelLoader(BaseModelLoader):
    """
    Pytorch model loader. Supports Pytorch models.
    """
class OnnxModelLoader(BaseModelLoader):
    """
    ONNX model loader. Supports ONNX models.
    """
class TensorflowModelLoader(BaseModelLoader):
    """
    Tensorflow model loader. Supports tensorflow models.
    """
class XGBoostModelLoader(BaseModelLoader):
    """
    XGBoost model loader. Supports XGBoost models.
    """
class LightGBMModelLoader(BaseModelLoader):
    """
    XGBoost model loader. Supports XGBoost models.
    """
class MLFlowModelLoader(BaseModelLoader):
    """
    MLFlow model loader. Supports MLFlow models.
    """

def load_model(runtime: str, model_uri: str = '', functions: Mapping[str, BaseFunction] = {}):
    """
    Load model from file or using UDF

    Parameters
    ----------
    runtime : ModelRuntime type
        Support Onnx, Pytorch and Sklearn model currently.
    model_uri : str
        Path to the model file.
    functions : Mapping[str, BaseFunction]

    Returns
    -------
    object:
        Model type or None.
    """
