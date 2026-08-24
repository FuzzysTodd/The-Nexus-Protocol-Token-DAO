import numpy as np
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.types import DataType as DataType
from mlflow.types.schema import ColSpec as ColSpec, ParamSchema as ParamSchema, ParamSpec as ParamSpec, Schema as Schema, TensorSpec as TensorSpec

class TensorsNotSupportedException(MlflowException):
    def __init__(self, msg) -> None: ...

def clean_tensor_type(dtype: np.dtype):
    """
    This method strips away the size information stored in flexible datatypes such as np.str_ and
    np.bytes_. Other numpy dtypes are returned unchanged.

    :param dtype: Numpy dtype of a tensor
    :return: dtype: Cleaned numpy dtype
    """
