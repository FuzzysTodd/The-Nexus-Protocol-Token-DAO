import pandas as pd
from _typeshed import Incomplete
from functools import cached_property as cached_property
from mlflow.data.dataset import Dataset as Dataset
from mlflow.data.dataset_source import DatasetSource as DatasetSource
from mlflow.data.digest_utils import compute_pandas_digest as compute_pandas_digest
from mlflow.data.pyfunc_dataset_mixin import PyFuncConvertibleDatasetMixin as PyFuncConvertibleDatasetMixin, PyFuncInputsOutputs as PyFuncInputsOutputs
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models.evaluation.base import EvaluationDataset as EvaluationDataset
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.types import Schema as Schema
from mlflow.utils.annotations import experimental as experimental
from typing import Any

class PandasDataset(Dataset, PyFuncConvertibleDatasetMixin):
    """
    Represents a Pandas DataFrame for use with MLflow Tracking.
    """
    def __init__(self, df: pd.DataFrame, source: DatasetSource, targets: str = None, name: str | None = None, digest: str | None = None) -> None:
        '''
        :param df: A pandas DataFrame.
        :param source: The source of the pandas DataFrame.
        :param targets: The name of the target column. Optional.
        :param name: The name of the dataset. E.g. "wiki_train". If unspecified, a name is
                     automatically generated.
        :param digest: The digest (hash, fingerprint) of the dataset. If unspecified, a digest
                       is automatically computed.
        '''
    @property
    def df(self) -> pd.DataFrame:
        """
        The underlying pandas DataFrame.
        """
    @property
    def source(self) -> DatasetSource:
        """
        The source of the dataset.
        """
    @property
    def targets(self) -> str | None:
        """
        The name of the target column. May be ``None`` if no target column is available.
        """
    @property
    def profile(self) -> Any | None:
        """
        A profile of the dataset. May be ``None`` if a profile cannot be computed.
        """
    @cached_property
    def schema(self) -> Schema | None:
        """
        An instance of :py:class:`mlflow.types.Schema` representing the tabular dataset. May be
        ``None`` if the schema cannot be inferred from the dataset.
        """
    def to_pyfunc(self) -> PyFuncInputsOutputs:
        """
        Converts the dataset to a collection of pyfunc inputs and outputs for model
        evaluation. Required for use with mlflow.evaluate().
        """
    def to_evaluation_dataset(self, path: Incomplete | None = None, feature_names: Incomplete | None = None) -> EvaluationDataset:
        """
        Converts the dataset to an EvaluationDataset for model evaluation. Required
        for use with mlflow.evaluate().
        """

def from_pandas(df: pd.DataFrame, source: str | DatasetSource = None, targets: str | None = None, name: str | None = None, digest: str | None = None) -> PandasDataset:
    """
    Constructs a :py:class:`PandasDataset <mlflow.data.pandas_dataset.PandasDataset>` instance from
    a Pandas DataFrame, optional targets, and source.

    :param df: A Pandas DataFrame.
    :param source: The source from which the DataFrame was derived, e.g. a filesystem
                   path, an S3 URI, an HTTPS URL, a delta table name with version, or
                   spark table etc. ``source`` may be specified as a URI, a path-like string,
                   or an instance of
                   :py:class:`DatasetSource <mlflow.data.dataset_source.DatasetSource>`.
                   If unspecified, the source is assumed to be the code location
                   (e.g. notebook cell, script, etc.) where
                   :py:func:`from_pandas <mlflow.data.from_pandas>` is being called.
    :param targets: An optional target column name for supervised training. This column
                    must be present in the dataframe (``df``).
    :param name: The name of the dataset. If unspecified, a name is generated.
    :param digest: The dataset digest (hash). If unspecified, a digest is computed
                   automatically.
    """
