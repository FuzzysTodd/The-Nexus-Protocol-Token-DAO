from _typeshed import Incomplete
from mlflow.store.artifact.artifact_repo import ArtifactRepository as ArtifactRepository, verify_artifact_path as verify_artifact_path
from mlflow.utils.file_utils import get_file_info as get_file_info, list_all as list_all, local_file_uri_to_path as local_file_uri_to_path, mkdir as mkdir, relative_path_to_artifact_path as relative_path_to_artifact_path

class LocalArtifactRepository(ArtifactRepository):
    """Stores artifacts as files in a local directory."""
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def artifact_dir(self): ...
    def log_artifact(self, local_file, artifact_path: Incomplete | None = None) -> None: ...
    def log_artifacts(self, local_dir, artifact_path: Incomplete | None = None) -> None: ...
    def download_artifacts(self, artifact_path, dst_path: Incomplete | None = None):
        """
        Artifacts tracked by ``LocalArtifactRepository`` already exist on the local filesystem.
        If ``dst_path`` is ``None``, the absolute filesystem path of the specified artifact is
        returned. If ``dst_path`` is not ``None``, the local artifact is copied to ``dst_path``.

        :param artifact_path: Relative source path to the desired artifacts.
        :param dst_path: Absolute path of the local filesystem destination directory to which to
                         download the specified artifacts. This directory must already exist. If
                         unspecified, the absolute path of the local artifact will be returned.

        :return: Absolute path of the local filesystem location containing the desired artifacts.
        """
    def list_artifacts(self, path: Incomplete | None = None): ...
    def delete_artifacts(self, artifact_path: Incomplete | None = None) -> None: ...
