from _typeshed import Incomplete
from mlflow.data.artifact_dataset_sources import register_artifact_dataset_sources as register_artifact_dataset_sources
from mlflow.data.code_dataset_source import CodeDatasetSource as CodeDatasetSource
from mlflow.data.dataset_source import DatasetSource as DatasetSource
from mlflow.data.delta_dataset_source import DeltaDatasetSource as DeltaDatasetSource
from mlflow.data.http_dataset_source import HTTPDatasetSource as HTTPDatasetSource
from mlflow.data.huggingface_dataset_source import HuggingFaceDatasetSource as HuggingFaceDatasetSource
from mlflow.data.spark_dataset_source import SparkDatasetSource as SparkDatasetSource
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import RESOURCE_DOES_NOT_EXIST as RESOURCE_DOES_NOT_EXIST
from typing import Any, List

class DatasetSourceRegistry:
    sources: Incomplete
    def __init__(self) -> None: ...
    def register(self, source: DatasetSource):
        """
        Registers a DatasetSource for use with MLflow Tracking.

        :param source: The DatasetSource to register.
        """
    def register_entrypoints(self) -> None:
        """
        Registers dataset sources defined as Python entrypoints. For reference, see
        https://mlflow.org/docs/latest/plugins.html#defining-a-plugin.
        """
    def resolve(self, raw_source: Any, candidate_sources: List[DatasetSource] = None) -> DatasetSource:
        '''
        Resolves a raw source object, such as a string URI, to a DatasetSource for use with
        MLflow Tracking.

        :param raw_source: The raw source, e.g. a string like "s3://mybucket/path/to/iris/data" or a
                           HuggingFace :py:class:`datasets.Dataset` object.
        :param candidate_sources: A list of DatasetSource classes to consider as potential sources
                                  when resolving the raw source. Subclasses of the specified
                                  candidate sources are also considered. If unspecified, all
                                  registered sources are considered.
        :throws: MlflowException if no DatasetSource class can resolve the raw source.
        :return: The resolved DatasetSource.
        '''
    def get_source_from_json(self, source_json: str, source_type: str) -> DatasetSource:
        """
        Parses and returns a DatasetSource object from its JSON representation.

        :param source_json: The JSON representation of the DatasetSource.
        :param source_type: The string type of the DatasetSource, which indicates how to parse the
                            source JSON.
        """

def register_dataset_source(source: DatasetSource):
    """
    Registers a DatasetSource for use with MLflow Tracking.

    :param source: The DatasetSource to register.
    """
def resolve_dataset_source(raw_source: Any, candidate_sources: List[DatasetSource] = None) -> DatasetSource:
    '''
    Resolves a raw source object, such as a string URI, to a DatasetSource for use with
    MLflow Tracking.

    :param raw_source: The raw source, e.g. a string like "s3://mybucket/path/to/iris/data" or a
                       HuggingFace :py:class:`datasets.Dataset` object.
    :param candidate_sources: A list of DatasetSource classes to consider as potential sources
                              when resolving the raw source. Subclasses of the specified candidate
                              sources are also considered. If unspecified, all registered sources
                              are considered.
    :throws: MlflowException if no DatasetSource class can resolve the raw source.
    :return: The resolved DatasetSource.
    '''
def get_dataset_source_from_json(source_json: str, source_type: str) -> DatasetSource:
    """
    Parses and returns a DatasetSource object from its JSON representation.

    :param source_json: The JSON representation of the DatasetSource.
    :param source_type: The string type of the DatasetSource, which indicates how to parse the
                        source JSON.
    """
def get_registered_sources() -> List[DatasetSource]:
    """
    Obtains the registered dataset sources.

    :return: A list of registered dataset sources.
    """
