from _typeshed import Incomplete
from mlflow.data.dataset import Dataset as Dataset
from mlflow.data.huggingface_dataset import from_huggingface as from_huggingface
from mlflow.data.numpy_dataset import from_numpy as from_numpy
from mlflow.data.pandas_dataset import from_pandas as from_pandas
from mlflow.data.spark_dataset import from_spark as from_spark, load_delta as load_delta
from mlflow.data.tensorflow_dataset import from_tensorflow as from_tensorflow
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from typing import Dict

class DatasetRegistry:
    constructors: Incomplete
    def __init__(self) -> None: ...
    def register_constructor(self, constructor_fn: callable, constructor_name: str = None) -> str:
        '''
        Registers a dataset constructor.

        :param constructor_fn: A function that accepts at least the following
                               inputs and returns an instance of a subclass of
                               :py:class:`mlflow.data.dataset.Dataset`:

                               - name: Optional. A string dataset name
                               - digest: Optional. A string dataset digest.

        :param constructor_name: The name of the constructor, e.g.
                                 "from_spark". The name must begin with the
                                 string "from_" or "load_". If unspecified, the `__name__`
                                 attribute of the `constructor_fn` is used instead and must
                                 begin with the string "from_" or "load_".
        :return: The name of the registered constructor, e.g. "from_pandas" or "load_delta".
        '''
    def register_entrypoints(self) -> None:
        """
        Registers dataset sources defined as Python entrypoints. For reference, see
        https://mlflow.org/docs/latest/plugins.html#defining-a-plugin.
        """

def register_constructor(constructor_fn: callable, constructor_name: str = None) -> str:
    '''
    Registers a dataset constructor.

    :param constructor_fn: A function that accepts at least the following
                           inputs and returns an instance of a subclass of
                           :py:class:`mlflow.data.dataset.Dataset`:

                           - name: Optional. A string dataset name
                           - digest: Optional. A string dataset digest.

    :param constructor_name: The name of the constructor, e.g.
                             "from_spark". The name must begin with the
                             string "from_" or "load_". If unspecified, the `__name__`
                             attribute of the `constructor_fn` is used instead and must
                             begin with the string "from_" or "load_".
    :return: The name of the registered constructor, e.g. "from_pandas" or "load_delta".
    '''
def get_registered_constructors() -> Dict[str, callable]:
    """
    Obtains the registered dataset constructors.

    :return: A dictionary mapping constructor names to constructor functions.
    """
