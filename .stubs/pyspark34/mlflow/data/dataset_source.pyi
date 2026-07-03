import abc
from abc import abstractmethod
from mlflow.utils.annotations import experimental as experimental
from typing import Any

class DatasetSource(metaclass=abc.ABCMeta):
    """
    Represents the source of a dataset used in MLflow Tracking, providing information such as
    cloud storage location, delta table name / version, etc.
    """
    @abstractmethod
    def load(self) -> Any:
        """
        Loads files / objects referred to by the DatasetSource. For example, depending on the type
        of :py:class:`DatasetSource <mlflow.data.dataset_source.DatasetSource>`, this may download
        source CSV files from S3 to the local filesystem, load a source Delta Table as a Spark
        DataFrame, etc.

        :return: The downloaded source, e.g. a local filesystem path, a Spark DataFrame, etc.
        """
    def to_json(self) -> str:
        """
        Obtains a JSON string representation of the
        :py:class:`DatasetSource <mlflow.data.dataset_source.DatasetSource>`.

        :return: A JSON string representation of the
                 :py:class:`DatasetSource <mlflow.data.dataset_source.DatasetSource>`.

        """
    @classmethod
    def from_json(cls, source_json: str) -> DatasetSource:
        """
        Constructs an instance of the DatasetSource from a JSON string representation.

        :param source_dict: A JSON string representation of the DatasetSource.
        :return: A DatasetSource instance.
        """
