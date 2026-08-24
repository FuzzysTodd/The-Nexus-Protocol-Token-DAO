from _typeshed import Incomplete
from functools import cached_property as cached_property
from mlflow.data.dataset import Dataset as Dataset
from mlflow.data.dataset_source import DatasetSource as DatasetSource
from mlflow.data.digest_utils import compute_tensor_digest as compute_tensor_digest, compute_tensorflow_dataset_digest as compute_tensorflow_dataset_digest
from mlflow.data.pyfunc_dataset_mixin import PyFuncConvertibleDatasetMixin as PyFuncConvertibleDatasetMixin, PyFuncInputsOutputs as PyFuncInputsOutputs
from mlflow.data.schema import TensorDatasetSchema as TensorDatasetSchema
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models.evaluation.base import EvaluationDataset as EvaluationDataset
from mlflow.protos.databricks_pb2 import INTERNAL_ERROR as INTERNAL_ERROR, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.types.schema import Schema as Schema
from mlflow.utils.annotations import experimental as experimental
from typing import Any

class TensorFlowDataset(Dataset, PyFuncConvertibleDatasetMixin):
    """
    Represents a TensorFlow dataset for use with MLflow Tracking.
    """
    def __init__(self, features, source: DatasetSource, targets: Incomplete | None = None, name: str | None = None, digest: str | None = None) -> None:
        '''
        :param features: A TensorFlow dataset or tensor of features.
        :param source: The source of the TensorFlow dataset.
        :param targets: A TensorFlow dataset or tensor of targets. Optional.
        :param name: The name of the dataset. E.g. "wiki_train". If unspecified, a name is
                     automatically generated.
        :param digest: The digest (hash, fingerprint) of the dataset. If unspecified, a digest
                       is automatically computed.
        '''
    @property
    def data(self):
        """
        The underlying TensorFlow data.
        """
    @property
    def source(self) -> DatasetSource:
        """
        The source of the dataset.
        """
    @property
    def targets(self):
        """
        The targets of the dataset.
        """
    @property
    def profile(self) -> Any | None:
        """
        A profile of the dataset. May be None if no profile is available.
        """
    @cached_property
    def schema(self) -> TensorDatasetSchema | None:
        """
        An MLflow TensorSpec schema representing the tensor dataset
        """
    def to_pyfunc(self) -> PyFuncInputsOutputs:
        """
        Converts the dataset to a collection of pyfunc inputs and outputs for model
        evaluation. Required for use with mlflow.evaluate().
        """
    def to_evaluation_dataset(self, path: Incomplete | None = None, feature_names: Incomplete | None = None) -> EvaluationDataset:
        """
        Converts the dataset to an EvaluationDataset for model evaluation. Only supported if the
        dataset is a Tensor. Required for use with mlflow.evaluate().
        """

def from_tensorflow(features, source: str | DatasetSource | None = None, targets: Incomplete | None = None, name: str | None = None, digest: str | None = None) -> TensorFlowDataset:
    """
    Constructs a TensorFlowDataset object from TensorFlow data, optional targets, and source.
    If the source is path like, then this will construct a DatasetSource object from the source
    path. Otherwise, the source is assumed to be a DatasetSource object.

    :param features: A TensorFlow dataset or tensor of features.
    :param source: The source from which the data was derived, e.g. a filesystem
                    path, an S3 URI, an HTTPS URL, a delta table name with version, or
                    spark table etc. If source is not a path like string,
                    pass in a DatasetSource object directly. If no source is specified,
                    a CodeDatasetSource is used, which will source information from the run
                    context.
    :param targets: A TensorFlow dataset or tensor of targets. Optional.
    :param name: The name of the dataset. If unspecified, a name is generated.
    :param digest: A dataset digest (hash). If unspecified, a digest is computed
                    automatically.
    """
