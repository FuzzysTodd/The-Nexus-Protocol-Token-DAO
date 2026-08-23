import abc
from _typeshed import Incomplete
from abc import abstractmethod
from mlflow.artifacts import download_artifacts as download_artifacts
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import BAD_REQUEST as BAD_REQUEST, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.utils.file_utils import TempDir as TempDir, download_file_using_http_uri as download_file_using_http_uri, get_local_path_or_none as get_local_path_or_none, local_file_uri_to_path as local_file_uri_to_path, read_parquet_as_pandas_df as read_parquet_as_pandas_df, write_pandas_df_as_parquet as write_pandas_df_as_parquet
from typing import Any, Dict, List

class _Dataset(metaclass=abc.ABCMeta):
    """
    Base class representing an ingestable dataset.
    """
    dataset_format: Incomplete
    def __init__(self, dataset_format: str) -> None:
        """
        :param dataset_format: The format of the dataset (e.g. 'csv', 'parquet', ...).
        """
    @abstractmethod
    def resolve_to_parquet(self, dst_path: str):
        """
        Fetches the dataset, converts it to parquet, and stores it at the specified `dst_path`.

        :param dst_path: The local filesystem path at which to store the resolved parquet dataset
                         (e.g. `<execution_directory_path>/steps/ingest/outputs/dataset.parquet`).
        """
    @classmethod
    def from_config(cls, dataset_config: Dict[str, Any], recipe_root: str) -> _Dataset:
        """
        Constructs a dataset instance from the specified dataset configuration
        and recipe root path.

        :param dataset_config: Dictionary representation of the recipe dataset configuration
                               (i.e. the `data` section of recipe.yaml).
        :param recipe_root: The absolute path of the associated recipe root directory on the
                              local filesystem.
        :return: A `_Dataset` instance representing the configured dataset.
        """
    @staticmethod
    @abstractmethod
    def handles_format(dataset_format: str) -> bool:
        """
        Determines whether or not the dataset class is a compatible representation of the
        specified dataset format.

        :param dataset_format: The format of the dataset (e.g. 'csv', 'parquet', ...).
        :return: `True` if the dataset class is a compatible representation of the specified
                 dataset format, `False` otherwise.
        """

class _LocationBasedDataset(_Dataset, metaclass=abc.ABCMeta):
    """
    Base class representing an ingestable dataset with a configurable `location` attribute.
    """
    location: Incomplete
    def __init__(self, location: str | List[str], dataset_format: str, recipe_root: str) -> None:
        """
        :param location: The location of the dataset
                         (one dataset as a string or list of multiple datasets)
                         (e.g. '/tmp/myfile.parquet', './mypath', 's3://mybucket/mypath',
                         or YAML list:
                            location:
                                - http://www.myserver.com/dataset/df1.csv
                                - http://www.myserver.com/dataset/df1.csv
                        )

        :param dataset_format: The format of the dataset (e.g. 'csv', 'parquet', ...).
        :param recipe_root: The absolute path of the associated recipe root directory on the
                              local filesystem.
        """
    @abstractmethod
    def resolve_to_parquet(self, dst_path: str): ...
    @staticmethod
    @abstractmethod
    def handles_format(dataset_format: str) -> bool: ...

class _DownloadThenConvertDataset(_LocationBasedDataset, metaclass=abc.ABCMeta):
    """
    Base class representing a location-based ingestible dataset that is resolved in two distinct
    phases: 1. Download the dataset files to the local filesystem. 2. Convert the dataset files to
    parquet format, aggregating them together as a single parquet file.
    `_DownloadThenConvertDataset` implements phase (1) and provides an abstract method
    for phase (2).
    """
    def resolve_to_parquet(self, dst_path: str): ...

class _PandasConvertibleDataset(_DownloadThenConvertDataset, metaclass=abc.ABCMeta):
    """
    Base class representing a location-based ingestable dataset that can be parsed and converted to
    parquet using a series of Pandas DataFrame ``read_*`` and ``concat`` operations.
    """
    @staticmethod
    @abstractmethod
    def handles_format(dataset_format: str) -> bool: ...

class ParquetDataset(_PandasConvertibleDataset):
    """
    Representation of a dataset in parquet format with files having the `.parquet` extension.
    """
    @staticmethod
    def handles_format(dataset_format: str) -> bool: ...

class CustomDataset(_PandasConvertibleDataset):
    """
    Representation of a location-based dataset with files containing a consistent, custom
    extension (e.g. 'csv', 'csv.gz', 'json', ...), as well as a custom function used to load
    and convert the dataset to parquet format.
    """
    recipe_root: Incomplete
    loader_method: Incomplete
    def __init__(self, location: str, dataset_format: str, loader_method: str, recipe_root: str) -> None:
        """
        :param location: The location of the dataset
                         (e.g. '/tmp/myfile.parquet', './mypath', 's3://mybucket/mypath', ...).
        :param dataset_format: The format of the dataset (e.g. 'csv', 'parquet', ...).
        :param loader_method: The custom loader method used to load and convert the dataset
                              to parquet format, e.g.`load_file_as_dataframe`.
        :param recipe_root: The absolute path of the associated recipe root directory on the
                              local filesystem.
        """
    @staticmethod
    def handles_format(dataset_format: str) -> bool: ...

class _SparkDatasetMixin:
    """
    Mixin class providing Spark-related utilities for Datasets that use Spark for resolution
    and conversion to parquet format.
    """

class DeltaTableDataset(_SparkDatasetMixin, _LocationBasedDataset):
    """
    Representation of a dataset in delta format with files having the `.delta` extension.
    """
    version: Incomplete
    timestamp: Incomplete
    def __init__(self, location: str, dataset_format: str, recipe_root: str, version: int | None = None, timestamp: str | None = None) -> None:
        """
        :param location: The location of the dataset
                         (e.g. '/tmp/myfile.parquet', './mypath', 's3://mybucket/mypath', ...).
        :param dataset_format: The format of the dataset (e.g. 'csv', 'parquet', ...).
        :param recipe_root: The absolute path of the associated recipe root directory on the
                              local filesystem.
        :param version: The version of the Delta table to read.
        :param timestamp: The timestamp at which to read the Delta table.
        """
    def resolve_to_parquet(self, dst_path: str): ...
    @staticmethod
    def handles_format(dataset_format: str) -> bool: ...

class SparkSqlDataset(_SparkDatasetMixin, _Dataset):
    """
    Representation of a Spark SQL dataset defined by a Spark SQL query string
    (e.g. `SELECT * FROM my_spark_table`).
    """
    sql: Incomplete
    location: Incomplete
    def __init__(self, sql: str, location: str, dataset_format: str) -> None:
        """
        :param sql: The Spark SQL query string that defines the dataset
                    (e.g. 'SELECT * FROM my_spark_table').
        :param location: The location of the dataset
                    (e.g. 'catalog.schema.table', 'schema.table', 'table').
        :param dataset_format: The format of the dataset (e.g. 'csv', 'parquet', ...).
        """
    def resolve_to_parquet(self, dst_path: str): ...
    @staticmethod
    def handles_format(dataset_format: str) -> bool: ...
