import datasets
from _typeshed import Incomplete
from functools import cached_property as cached_property
from mlflow.data.dataset import Dataset as Dataset
from mlflow.data.digest_utils import compute_pandas_digest as compute_pandas_digest
from mlflow.data.huggingface_dataset_source import HuggingFaceDatasetSource as HuggingFaceDatasetSource
from mlflow.data.pyfunc_dataset_mixin import PyFuncConvertibleDatasetMixin as PyFuncConvertibleDatasetMixin, PyFuncInputsOutputs as PyFuncInputsOutputs
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models.evaluation.base import EvaluationDataset as EvaluationDataset
from mlflow.protos.databricks_pb2 import INTERNAL_ERROR as INTERNAL_ERROR, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.types import Schema as Schema
from mlflow.utils.annotations import experimental as experimental
from typing import Any, Mapping, Sequence

class HuggingFaceDataset(Dataset, PyFuncConvertibleDatasetMixin):
    """
    Represents a HuggingFace dataset for use with MLflow Tracking.
    """
    def __init__(self, ds: datasets.Dataset, source: HuggingFaceDatasetSource, targets: str | None = None, name: str | None = None, digest: str | None = None) -> None:
        '''
        :param ds: A Hugging Face dataset. Must be an instance of `datasets.Dataset`.
                   Other types, such as :py:class:`datasets.DatasetDict`, are not supported.
        :param source: The source of the Hugging Face dataset.
        :param name: The name of the dataset. E.g. "wiki_train". If unspecified, a name is
                     automatically generated.
        :param digest: The digest (hash, fingerprint) of the dataset. If unspecified, a digest
                       is automatically computed.
        '''
    @property
    def ds(self) -> datasets.Dataset:
        """
        The Hugging Face ``datasets.Dataset`` instance.

        :return: The Hugging Face ``datasets.Dataset`` instance.
        """
    @property
    def targets(self) -> str | None:
        """
        The name of the Hugging Face dataset column containing targets (labels) for supervised
        learning.

        :return: The string name of the Hugging Face dataset column containing targets.
        """
    @property
    def source(self) -> HuggingFaceDatasetSource:
        """
        Hugging Face dataset source information.

        :return: A :py:class:`mlflow.data.huggingface_dataset_source.HuggingFaceDatasetSource`
                 instance.
        """
    @property
    def profile(self) -> Any | None:
        """
        Summary statistics for the Hugging Face dataset, including the number of rows,
        size, and size in bytes.
        """
    @cached_property
    def schema(self) -> Schema | None:
        """
        The MLflow ColSpec schema of the Hugging Face dataset.
        """
    def to_pyfunc(self) -> PyFuncInputsOutputs: ...
    def to_evaluation_dataset(self, path: Incomplete | None = None, feature_names: Incomplete | None = None) -> EvaluationDataset:
        """
        Converts the dataset to an EvaluationDataset for model evaluation. Required
        for use with mlflow.evaluate().
        """

def from_huggingface(ds, path: str = None, targets: str | None = None, data_dir: str | None = None, data_files: str | Sequence[str] | Mapping[str, str | Sequence[str]] | None = None, revision: Incomplete | None = None, task: Incomplete | None = None, name: str | None = None, digest: str | None = None) -> HuggingFaceDataset:
    '''
    Given a Hugging Face ``datasets.Dataset``, constructs an MLflow :py:class:`HuggingFaceDataset`
    object for use with MLflow Tracking.

    :param ds: A Hugging Face dataset. Must be an instance of ``datasets.Dataset``.
               Other types, such as ``datasets.DatasetDict``, are not supported.
    :param path: The path of the Hugging Face dataset used to construct the source. This is used by
                 the ``datasets.load_dataset()`` function to reload the dataset upon request via
                 :py:func:`HuggingFaceDataset.source.load()
                 <mlflow.data.huggingface_dataset_source.HuggingFaceDatasetSource.load>`.
                 If no path is specified, a CodeDatasetSource is used, which will source
                 information from the run context.
    :param targets: The name of the Hugging Face ``dataset.Dataset`` column containing targets
                    (labels) for supervised learning.
    :param data_dir: The `data_dir` of the Hugging Face dataset configuration. This is used by the
                     ``datasets.load_dataset()`` function to reload the dataset upon request via
                     :py:func:`HuggingFaceDataset.source.load()
                     <mlflow.data.huggingface_dataset_source.HuggingFaceDatasetSource.load>`.
    :param data_files: Paths to source data file(s) for the Hugging Face dataset configuration.
                       This is used by the ``datasets.load_dataset()`` function to reload the
                       dataset upon request via :py:func:`HuggingFaceDataset.source.load()
                       <mlflow.data.huggingface_dataset_source.HuggingFaceDatasetSource.load>`.
    :param revision: Version of the dataset script to load. This is used by the
                     ``datasets.load_dataset()`` function to reload the dataset upon request via
                     :py:func:`HuggingFaceDataset.source.load()
                     <mlflow.data.huggingface_dataset_source.HuggingFaceDatasetSource.load>`.
    :param task: The task to prepare the Hugging Face dataset for during training and evaluation.
                 This is used by the ``datasets.load_dataset()`` function to reload the dataset
                 upon request via :py:func:`HuggingFaceDataset.source.load()
                 <mlflow.data.huggingface_dataset_source.HuggingFaceDatasetSource.load>`.
    :param name: The name of the dataset. E.g. "wiki_train". If unspecified, a name is
                 automatically generated.
    :param digest: The digest (hash, fingerprint) of the dataset. If unspecified, a digest
                   is automatically computed.
    '''
