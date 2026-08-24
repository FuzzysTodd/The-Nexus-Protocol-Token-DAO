import numpy as np
from _typeshed import Incomplete
from functools import cached_property as cached_property
from mlflow.data.dataset import Dataset as Dataset
from mlflow.data.dataset_source import DatasetSource as DatasetSource
from mlflow.data.digest_utils import compute_numpy_digest as compute_numpy_digest
from mlflow.data.pyfunc_dataset_mixin import PyFuncConvertibleDatasetMixin as PyFuncConvertibleDatasetMixin, PyFuncInputsOutputs as PyFuncInputsOutputs
from mlflow.data.schema import TensorDatasetSchema as TensorDatasetSchema
from mlflow.models.evaluation.base import EvaluationDataset as EvaluationDataset
from mlflow.utils.annotations import experimental as experimental
from typing import Any, Dict

class NumpyDataset(Dataset, PyFuncConvertibleDatasetMixin):
    """
    Represents a NumPy dataset for use with MLflow Tracking.
    """
    def __init__(self, features: np.ndarray | Dict[str, np.ndarray], source: DatasetSource, targets: np.ndarray | Dict[str, np.ndarray] = None, name: str | None = None, digest: str | None = None) -> None:
        '''
        :param features: A numpy array or dictionary of numpy arrays containing dataset features.
        :param source: The source of the numpy dataset.
        :param targets: A numpy array or dictionary of numpy arrays containing dataset targets.
                        Optional.
        :param name: The name of the dataset. E.g. "wiki_train". If unspecified, a name is
                     automatically generated.
        :param digest: The digest (hash, fingerprint) of the dataset. If unspecified, a digest
                       is automatically computed.
        '''
    @property
    def source(self) -> DatasetSource:
        """
        The source of the dataset.
        """
    @property
    def features(self) -> np.ndarray | Dict[str, np.ndarray]:
        """
        The features of the dataset.
        """
    @property
    def targets(self) -> np.ndarray | Dict[str, np.ndarray] | None:
        """
        The targets of the dataset. May be ``None`` if no targets are available.
        """
    @property
    def profile(self) -> Any | None:
        """
        A profile of the dataset. May be ``None`` if a profile cannot be computed.
        """
    @cached_property
    def schema(self) -> TensorDatasetSchema | None:
        """
        MLflow TensorSpec schema representing the dataset features and targets (optional).
        """
    def to_pyfunc(self) -> PyFuncInputsOutputs:
        """
        Converts the dataset to a collection of pyfunc inputs and outputs for model
        evaluation. Required for use with mlflow.evaluate().
        """
    def to_evaluation_dataset(self, path: Incomplete | None = None, feature_names: Incomplete | None = None) -> EvaluationDataset:
        """
        Converts the dataset to an EvaluationDataset for model evaluation. Required
        for use with mlflow.sklearn.evalute().
        """

def from_numpy(features: np.ndarray | Dict[str, np.ndarray], source: str | DatasetSource = None, targets: np.ndarray | Dict[str, np.ndarray] = None, name: str | None = None, digest: str | None = None) -> NumpyDataset:
    """
    Constructs a :py:class:`NumpyDataset <mlflow.data.numpy_dataset.NumpyDataset>` object from
    NumPy features, optional targets, and source. If the source is path like, then this will
    construct a DatasetSource object from the source path. Otherwise, the source is assumed to
    be a DatasetSource object.

    :param features: NumPy features, represented as an np.ndarray or dictionary of named
                     np.ndarrays.
    :param source: The source from which the numpy data was derived, e.g. a filesystem
                   path, an S3 URI, an HTTPS URL, a delta table name with version, or
                   spark table etc. ``source`` may be specified as a URI, a path-like string,
                   or an instance of
                   :py:class:`DatasetSource <mlflow.data.dataset_source.DatasetSource>`.
                   If unspecified, the source is assumed to be the code location
                   (e.g. notebook cell, script, etc.) where
                   :py:func:`from_numpy <mlflow.data.from_numpy>` is being called.
    :param targets: Optional NumPy targets, represented as an np.ndarray or dictionary of named
                    np.ndarrays.
    :param name: The name of the dataset. If unspecified, a name is generated.
    :param digest: The dataset digest (hash). If unspecified, a digest is computed
                   automatically.
    """
