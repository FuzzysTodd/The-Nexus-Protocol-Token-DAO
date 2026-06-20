from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.store.artifact.artifact_repo import ArtifactRepository as ArtifactRepository
from mlflow.store.artifact.databricks_models_artifact_repo import DatabricksModelsArtifactRepository as DatabricksModelsArtifactRepository
from mlflow.store.artifact.unity_catalog_models_artifact_repo import UnityCatalogModelsArtifactRepository as UnityCatalogModelsArtifactRepository
from mlflow.store.artifact.utils.models import get_model_name_and_version as get_model_name_and_version, is_using_databricks_registry as is_using_databricks_registry
from mlflow.utils.uri import add_databricks_profile_info_to_artifact_uri as add_databricks_profile_info_to_artifact_uri, get_databricks_profile_uri_from_artifact_uri as get_databricks_profile_uri_from_artifact_uri, is_databricks_unity_catalog_uri as is_databricks_unity_catalog_uri

class ModelsArtifactRepository(ArtifactRepository):
    """
    Handles artifacts associated with a model version in the model registry via URIs of the form:
      - `models:/<model_name>/<model_version>`
      - `models:/<model_name>/<stage>`  (refers to the latest model version in the given stage)
      - `models:/<model_name>/latest` (refers to the latest of all model versions)
    It is a light wrapper that resolves the artifact path to an absolute URI then instantiates
    and uses the artifact repository for that URI.
    """
    repo: Incomplete
    def __init__(self, artifact_uri) -> None: ...
    @staticmethod
    def is_models_uri(uri): ...
    @staticmethod
    def split_models_uri(uri):
        """
        Split 'models:/<name>/<version>/path/to/model' into
        ('models:/<name>/<version>', 'path/to/model').
        """
    @staticmethod
    def get_underlying_uri(uri): ...
    def log_artifact(self, local_file, artifact_path: Incomplete | None = None) -> None:
        """
        Log a local file as an artifact, optionally taking an ``artifact_path`` to place it in
        within the run's artifacts. Run artifacts can be organized into directories, so you can
        place the artifact in a directory this way.

        :param local_file: Path to artifact to log
        :param artifact_path: Directory within the run's artifact directory in which to log the
                              artifact
        """
    def log_artifacts(self, local_dir, artifact_path: Incomplete | None = None) -> None:
        """
        Log the files in the specified local directory as artifacts, optionally taking
        an ``artifact_path`` to place them in within the run's artifacts.

        :param local_dir: Directory of local artifacts to log
        :param artifact_path: Directory within the run's artifact directory in which to log the
                              artifacts
        """
    def list_artifacts(self, path):
        """
        Return all the artifacts for this run_id directly under path. If path is a file, returns
        an empty list. Will error if path is neither a file nor directory.

        :param path: Relative source path that contain desired artifacts

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
    def delete_artifacts(self, artifact_path: Incomplete | None = None) -> None: ...
