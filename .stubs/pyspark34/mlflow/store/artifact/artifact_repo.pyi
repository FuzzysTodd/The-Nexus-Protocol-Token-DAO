import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from mlflow.entities.file_info import FileInfo as FileInfo
from mlflow.environment_variables import MLFLOW_ENABLE_ARTIFACTS_PROGRESS_BAR as MLFLOW_ENABLE_ARTIFACTS_PROGRESS_BAR
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, RESOURCE_DOES_NOT_EXIST as RESOURCE_DOES_NOT_EXIST
from mlflow.utils.annotations import developer_stable as developer_stable
from mlflow.utils.file_utils import ArtifactProgressBar as ArtifactProgressBar
from mlflow.utils.validation import bad_path_message as bad_path_message, path_not_unique as path_not_unique

class ArtifactRepository(metaclass=abc.ABCMeta):
    """
    Abstract artifact repo that defines how to upload (log) and download potentially large
    artifacts from different storage backends.
    """
    __metaclass__ = ABCMeta
    artifact_uri: Incomplete
    thread_pool: Incomplete
    def __init__(self, artifact_uri) -> None: ...
    @abstractmethod
    def log_artifact(self, local_file, artifact_path: Incomplete | None = None):
        """
        Log a local file as an artifact, optionally taking an ``artifact_path`` to place it in
        within the run's artifacts. Run artifacts can be organized into directories, so you can
        place the artifact in a directory this way.

        :param local_file: Path to artifact to log
        :param artifact_path: Directory within the run's artifact directory in which to log the
                              artifact.
        """
    @abstractmethod
    def log_artifacts(self, local_dir, artifact_path: Incomplete | None = None):
        """
        Log the files in the specified local directory as artifacts, optionally taking
        an ``artifact_path`` to place them in within the run's artifacts.

        :param local_dir: Directory of local artifacts to log
        :param artifact_path: Directory within the run's artifact directory in which to log the
                              artifacts
        """
    @abstractmethod
    def list_artifacts(self, path):
        """
        Return all the artifacts for this run_id directly under path. If path is a file, returns
        an empty list. Will error if path is neither a file nor directory.

        :param path: Relative source path that contains desired artifacts

        :return: List of artifacts as FileInfo listed directly under path.
        """
    def download_artifacts(self, artifact_path, dst_path: Incomplete | None = None):
        """
        Download an artifact file or directory to a local directory if applicable, and return a
        local path for it.
        The caller is responsible for managing the lifecycle of the downloaded artifacts.

        :param artifact_path: Relative source path to the desired artifacts.
        :param dst_path: Absolute path of the local filesystem destination directory to which to
                         download the specified artifacts. This directory must already exist.
                         If unspecified, the artifacts will either be downloaded to a new
                         uniquely-named directory on the local filesystem or will be returned
                         directly in the case of the LocalArtifactRepository.

        :return: Absolute path of the local filesystem location containing the desired artifacts.
        """
    def delete_artifacts(self, artifact_path: Incomplete | None = None) -> None:
        """
        Delete the artifacts at the specified location.
        Supports the deletion of a single file or of a directory. Deletion of a directory
        is recursive.
        :param artifact_path: Path of the artifact to delete
        """
    @property
    def max_workers(self) -> int:
        """Compute the number of workers to use for multi-threading."""

def verify_artifact_path(artifact_path) -> None: ...
