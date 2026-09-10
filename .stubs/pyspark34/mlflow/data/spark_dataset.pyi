from _typeshed import Incomplete
from functools import cached_property as cached_property
from mlflow.data.dataset import Dataset as Dataset
from mlflow.data.dataset_source import DatasetSource as DatasetSource
from mlflow.data.delta_dataset_source import DeltaDatasetSource as DeltaDatasetSource
from mlflow.data.digest_utils import compute_spark_df_digest as compute_spark_df_digest
from mlflow.data.pyfunc_dataset_mixin import PyFuncConvertibleDatasetMixin as PyFuncConvertibleDatasetMixin, PyFuncInputsOutputs as PyFuncInputsOutputs
from mlflow.data.spark_dataset_source import SparkDatasetSource as SparkDatasetSource
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models.evaluation.base import EvaluationDataset as EvaluationDataset
from mlflow.protos.databricks_pb2 import INTERNAL_ERROR as INTERNAL_ERROR, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.types import Schema as Schema
from mlflow.utils.annotations import experimental as experimental
from typing import Any

class SparkDataset(Dataset, PyFuncConvertibleDatasetMixin):
    """
    Represents a Spark dataset (e.g. data derived from a Spark Table / file directory or Delta
    Table) for use with MLflow Tracking.
    """
    def __init__(self, df, source: DatasetSource, targets: str | None = None, name: str | None = None, digest: str | None = None) -> None: ...
    @property
    def df(self):
        """
        The Spark DataFrame instance.

        :return: The Spark DataFrame instance.

        """
    @property
    def targets(self) -> str | None:
        """
        The name of the Spark DataFrame column containing targets (labels) for supervised
        learning.

        :return: The string name of the Spark DataFrame column containing targets.
        """
    @property
    def source(self) -> SparkDatasetSource | DeltaDatasetSource:
        """
        Spark dataset source information.

        :return: An instance of :py:class:`SparkDatasetSource
            <mlflow.data.spark_dataset_source.SparkDatasetSource>`
            or :py:class:`DeltaDatasetSource
            <mlflow.data.delta_dataset_source.DeltaDatasetSource>`.
        """
    @property
    def profile(self) -> Any | None:
        """
        A profile of the dataset. May be None if no profile is available.
        """
    @cached_property
    def schema(self) -> Schema | None:
        """
        The MLflow ColSpec schema of the Spark dataset.
        """
    def to_pyfunc(self) -> PyFuncInputsOutputs:
        """
        Converts the Spark DataFrame to pandas and splits the resulting
        :py:class:`pandas.DataFrame` into: 1. a :py:class:`pandas.DataFrame` of features and
        2. a :py:class:`pandas.Series` of targets.

        To avoid overuse of driver memory, only the first 10,000 DataFrame rows are selected.
        """
    def to_evaluation_dataset(self, path: Incomplete | None = None, feature_names: Incomplete | None = None) -> EvaluationDataset:
        """
        Converts the dataset to an EvaluationDataset for model evaluation. Required
        for use with mlflow.evaluate().
        """

def load_delta(path: str | None = None, table_name: str | None = None, version: str | None = None, targets: str | None = None, name: str | None = None, digest: str | None = None) -> SparkDataset:
    '''
    Loads a :py:class:`SparkDataset <mlflow.data.spark_dataset.SparkDataset>` from a Delta table
    for use with MLflow Tracking.

    :param path: The path to the Delta table. Either ``path`` or ``table_name`` must be specified.
    :param table_name: The name of the Delta table. Either ``path`` or ``table_name`` must be
                       specified.
    :param version: The Delta table version. If not specified, the version will be inferred.
    :param targets: Optional. The name of the Delta table column containing targets (labels) for
                    supervised learning.
    :param name: The name of the dataset. E.g. "wiki_train". If unspecified, a name is
                 automatically generated.
    :param digest: The digest (hash, fingerprint) of the dataset. If unspecified, a digest
                   is automatically computed.
    :return: An instance of :py:class:`SparkDataset <mlflow.data.spark_dataset.SparkDataset>`.
    '''
def from_spark(df, path: str | None = None, table_name: str | None = None, version: str | None = None, sql: str | None = None, targets: str | None = None, name: str | None = None, digest: str | None = None) -> SparkDataset:
    '''
    Given a Spark DataFrame, constructs a
    :py:class:`SparkDataset <mlflow.data.spark_dataset.SparkDataset>` object for use with
    MLflow Tracking.

    :param df: The Spark DataFrame from which to construct a SparkDataset.
    :param path: The path of the Spark or Delta source that the DataFrame originally came from.
                 Note that the path does not have to match the DataFrame exactly, since the
                 DataFrame may have been modified by Spark operations. This is used to reload the
                 dataset upon request via :py:func:`SparkDataset.source.load()
                 <mlflow.data.spark_dataset_source.SparkDatasetSource.load>`. If none of ``path``,
                 ``table_name``, or ``sql`` are specified, a CodeDatasetSource is used, which will
                 source information from the run context.
    :param table_name: The name of the Spark or Delta table that the DataFrame originally came from.
                       Note that the table does not have to match the DataFrame exactly, since the
                       DataFrame may have been modified by Spark operations. This is used to reload
                       the dataset upon request via :py:func:`SparkDataset.source.load()
                       <mlflow.data.spark_dataset_source.SparkDatasetSource.load>`. If none of
                       ``path``, ``table_name``, or ``sql`` are specified, a CodeDatasetSource is
                       used, which will source information from the run context.
    :param version: If the DataFrame originally came from a Delta table, specifies the version
                    of the Delta table. This is used to reload the dataset upon request via
                    :py:func:`SparkDataset.source.load()
                    <mlflow.data.spark_dataset_source.SparkDatasetSource.load>`.  ``version``
                    cannot be specified if ``sql`` is specified.
    :param sql: The Spark SQL statement that was originally used to construct the DataFrame.
                Note that the Spark SQL statement does not have to match the DataFrame exactly,
                since the DataFrame may have been modified by Spark operations. This is used to
                reload the dataset upon request via :py:func:`SparkDataset.source.load()
                <mlflow.data.spark_dataset_source.SparkDatasetSource.load>`. If none of
                ``path``, ``table_name``, or ``sql`` are specified, a CodeDatasetSource is used,
                which will source information from the run context.
    :param targets: Optional. The name of the Data Frame column containing targets (labels) for
                    supervised learning.
    :param name: The name of the dataset. E.g. "wiki_train". If unspecified, a name is
                 automatically generated.
    :param digest: The digest (hash, fingerprint) of the dataset. If unspecified, a digest
                   is automatically computed.
    :return: An instance of :py:class:`SparkDataset <mlflow.data.spark_dataset.SparkDataset>`.
    '''
