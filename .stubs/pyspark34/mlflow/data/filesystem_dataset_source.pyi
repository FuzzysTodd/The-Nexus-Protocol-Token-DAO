import abc
from _typeshed import Incomplete
from abc import abstractmethod
from mlflow.data.dataset_source import DatasetSource as DatasetSource
from mlflow.utils.annotations import experimental as experimental

class FileSystemDatasetSource(DatasetSource, metaclass=abc.ABCMeta):
    """
    Represents the source of a dataset stored on a filesystem, e.g. a local UNIX filesystem,
    blob storage services like S3, etc.
    """
    @property
    @abstractmethod
    def uri(self):
        '''
        The URI referring to the dataset source filesystem location.

        :return: The URI referring to the dataset source filesystem location,
                 e.g "s3://mybucket/path/to/mydataset", "/tmp/path/to/my/dataset" etc.
        '''
    @abstractmethod
    def load(self, dst_path: Incomplete | None = None) -> str:
        """
        Downloads the dataset source to the local filesystem.

        :param dst_path: Path of the local filesystem destination directory to which to download the
                         dataset source. If the directory does not exist, it is created. If
                         unspecified, the dataset source is downloaded to a new uniquely-named
                         directory on the local filesystem, unless the dataset source already
                         exists on the local filesystem, in which case its local path is returned
                         directly.
        :return: The path to the downloaded dataset source on the local filesystem.
        """
