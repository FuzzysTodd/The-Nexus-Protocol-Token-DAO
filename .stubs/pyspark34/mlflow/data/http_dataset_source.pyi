from _typeshed import Incomplete
from mlflow.data.dataset_source import DatasetSource as DatasetSource
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.utils.rest_utils import augmented_raise_for_status as augmented_raise_for_status, cloud_storage_http_request as cloud_storage_http_request

class HTTPDatasetSource(DatasetSource):
    """
    Represents the source of a dataset stored at a web location and referred to
    by an HTTP or HTTPS URL.
    """
    def __init__(self, url) -> None: ...
    @property
    def url(self):
        """
        The HTTP/S URL referring to the dataset source location.

        :return: The HTTP/S URL referring to the dataset source location.
        """
    def load(self, dst_path: Incomplete | None = None) -> str:
        """
        Downloads the dataset source to the local filesystem.

        :param dst_path: Path of the local filesystem destination directory to which to download the
                         dataset source. If the directory does not exist, it is created. If
                         unspecified, the dataset source is downloaded to a new uniquely-named
                         directory on the local filesystem.
        :return: The path to the downloaded dataset source on the local filesystem.
        """
