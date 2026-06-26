import abc
from abc import abstractmethod
from mlflow.data.dataset_source import DatasetSource as DatasetSource
from mlflow.utils.annotations import experimental as experimental
from typing import Any

class Dataset(metaclass=abc.ABCMeta):
    """
    Represents a dataset for use with MLflow Tracking, including the name, digest (hash),
    schema, and profile of the dataset as well as source information (e.g. the S3 bucket or
    managed Delta table from which the dataset was derived). Most datasets expose features
    and targets for training and evaluation as well.
    """
    def __init__(self, source: DatasetSource, name: str | None = None, digest: str | None = None) -> None:
        """
        Base constructor for a dataset. All subclasses must call this
        constructor.
        """
    def to_json(self) -> str:
        """
        Obtains a JSON string representation of the
        :py:class:`Dataset <mlflow.data.dataset.Dataset>`.

        :return: A JSON string representation of the
                 :py:class:`Dataset <mlflow.data.dataset.Dataset>`.
        """
    @property
    def name(self) -> str:
        '''
        The name of the dataset, e.g. ``"iris_data"``, ``"myschema.mycatalog.mytable@v1"``, etc.
        '''
    @property
    def digest(self) -> str:
        '''
        A unique hash or fingerprint of the dataset, e.g. ``"498c7496"``.
        '''
    @property
    def source(self) -> DatasetSource:
        """
        Information about the dataset's source, represented as an instance of
        :py:class:`DatasetSource <mlflow.data.dataset_source.DatasetSource>`. For example, this
        may be the S3 location or the name of the managed Delta Table from which the dataset
        was derived.
        """
    @property
    @abstractmethod
    def profile(self) -> Any | None:
        """
        Optional summary statistics for the dataset, such as the number of rows in a table, the
        mean / median / std of each table column, etc.
        """
    @property
    @abstractmethod
    def schema(self) -> Any | None:
        """
        Optional dataset schema, such as an instance of :py:class:`mlflow.types.Schema` representing
        the features and targets of the dataset.
        """
