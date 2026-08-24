from _typeshed import Incomplete
from collections.abc import Generator
from mlflow.entities import FileInfo as FileInfo
from mlflow.environment_variables import MLFLOW_KERBEROS_TICKET_CACHE as MLFLOW_KERBEROS_TICKET_CACHE, MLFLOW_KERBEROS_USER as MLFLOW_KERBEROS_USER, MLFLOW_PYARROW_EXTRA_CONF as MLFLOW_PYARROW_EXTRA_CONF
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.store.artifact.artifact_repo import ArtifactRepository as ArtifactRepository
from mlflow.utils.file_utils import mkdir as mkdir, relative_path_to_artifact_path as relative_path_to_artifact_path

class HdfsArtifactRepository(ArtifactRepository):
    """
    Stores artifacts on HDFS.

    This repository is used with URIs of the form ``hdfs:/<path>``. The repository can only be used
    together with the RestStore.
    """
    def __init__(self, artifact_uri) -> None: ...
    def log_artifact(self, local_file, artifact_path: Incomplete | None = None) -> None:
        """
            Log artifact in hdfs.
        :param local_file: source file path
        :param artifact_path: when specified will attempt to write under artifact_uri/artifact_path
        """
    def log_artifacts(self, local_dir, artifact_path: Incomplete | None = None) -> None:
        """
            Log artifacts in hdfs.
            Missing remote sub-directories will be created if needed.
        :param local_dir: source dir path
        :param artifact_path: when specified will attempt to write under artifact_uri/artifact_path
        """
    def list_artifacts(self, path: Incomplete | None = None):
        """
        Lists files and directories under artifacts directory for the current run_id.
        (self.path contains the base path - hdfs:/some/path/run_id/artifacts)

        :param path: Relative source path. Possible subdirectory existing under
                     hdfs:/some/path/run_id/artifacts
        :return: List of FileInfos under given path
        """
    def download_artifacts(self, artifact_path, dst_path: Incomplete | None = None):
        """
        Download an artifact file or directory to a local directory/file if applicable, and
        return a local path for it.
        The caller is responsible for managing the lifecycle of the downloaded artifacts.

        (self.path contains the base path - hdfs:/some/path/run_id/artifacts)

        :param artifact_path: Relative source path to the desired artifacts file or directory.
        :param dst_path: Absolute path of the local filesystem destination directory to which
                         to download the specified artifacts. This directory must already
                         exist. If unspecified, the artifacts will be downloaded to a new,
                         uniquely-named
                         directory on the local filesystem.

        :return: Absolute path of the local filesystem location containing the downloaded
        artifacts - file/directory.
        """
    def delete_artifacts(self, artifact_path: Incomplete | None = None) -> None: ...

def hdfs_system(scheme, host, port) -> Generator[Incomplete, None, None]:
    """
        hdfs system context - Attempt to establish the connection to hdfs
        and yields HadoopFileSystem

    :param scheme: scheme or use hdfs:// as default
    :param host: hostname or when relaying on the core-site.xml config use 'default'
    :param port: port or when relaying on the core-site.xml config use 0
    """
