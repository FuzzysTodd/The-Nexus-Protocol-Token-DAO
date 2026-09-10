from enum import Enum

class ModelRuntime(Enum):
    """ An enumeration for all supported native model runtimes. """
    AUTO: str
    MLFLOW: str
    ONNX: str
    PYTORCH: str
    SKLEARN: str
    TENSORFLOW: str
    XGBOOST: str
    LIGHTGBM: str
    DEPLOYED: str
    UNSUPPORTED: str
