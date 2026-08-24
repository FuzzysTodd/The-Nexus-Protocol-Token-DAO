from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from typing import Any, List

MAX_ROWS: int

def compute_pandas_digest(df) -> str:
    """
    Computes a digest for the given Pandas DataFrame.

    :param df: A Pandas DataFrame.
    :return: A string digest.
    """
def compute_numpy_digest(features, targets: Incomplete | None = None) -> str:
    """
    Computes a digest for the given numpy array.

    :param features: A numpy array containing dataset features.
    :param targets: A numpy array containing dataset targets. Optional.
    :return: A string digest.
    """
def compute_tensorflow_dataset_digest(dataset, targets: Incomplete | None = None) -> str:
    """
    Computes a digest for the given Tensorflow dataset.

    :param dataset: A Tensorflow dataset.
    :return: A string digest.
    """
def compute_tensor_digest(tensor_data, tensor_targets) -> str:
    """
    Computes a digest for the given Tensorflow tensor.

    :param tensor: A Tensorflow tensor.
    :return: A string digest.
    """
def compute_spark_df_digest(df) -> str:
    """
    Computes a digest for the given Spark DataFrame. Retrieve a semantic hash of the
    DataFrame's logical plan, which is much more efficient and deterministic than hashing
    DataFrame records

    :param df: A Spark DataFrame.
    :return: A string digest.
    """
def get_normalized_md5_digest(elements: List[Any]) -> str:
    """
    Computes a normalized digest for a list of hashable elements.

    :param elements: A list of hashable elements for inclusion in the md5 digest.
    :return: An 8-character, truncated md5 digest.
    """
