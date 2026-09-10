from mlflow.exceptions import MlflowException as MlflowException
from mlflow.store.artifact.azure_blob_artifact_repo import AzureBlobArtifactRepository as AzureBlobArtifactRepository
from mlflow.store.artifact.dbfs_artifact_repo import dbfs_artifact_repo_factory as dbfs_artifact_repo_factory
from mlflow.store.artifact.ftp_artifact_repo import FTPArtifactRepository as FTPArtifactRepository
from mlflow.store.artifact.gcs_artifact_repo import GCSArtifactRepository as GCSArtifactRepository
from mlflow.store.artifact.hdfs_artifact_repo import HdfsArtifactRepository as HdfsArtifactRepository
from mlflow.store.artifact.http_artifact_repo import HttpArtifactRepository as HttpArtifactRepository
from mlflow.store.artifact.local_artifact_repo import LocalArtifactRepository as LocalArtifactRepository
from mlflow.store.artifact.mlflow_artifacts_repo import MlflowArtifactsRepository as MlflowArtifactsRepository
from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository as ModelsArtifactRepository
from mlflow.store.artifact.runs_artifact_repo import RunsArtifactRepository as RunsArtifactRepository
from mlflow.store.artifact.s3_artifact_repo import S3ArtifactRepository as S3ArtifactRepository
from mlflow.store.artifact.sftp_artifact_repo import SFTPArtifactRepository as SFTPArtifactRepository
from mlflow.utils.uri import get_uri_scheme as get_uri_scheme

class ArtifactRepositoryRegistry:
    """Scheme-based registry for artifact repository implementations

    This class allows the registration of a function or class to provide an implementation for a
    given scheme of `artifact_uri` through the `register` method. Implementations declared though
    the entrypoints `mlflow.artifact_repository` group can be automatically registered through the
    `register_entrypoints` method.

    When instantiating an artifact repository through the `get_artifact_repository` method, the
    scheme of the artifact URI provided will be used to select which implementation to instantiate,
    which will be called with same arguments passed to the `get_artifact_repository` method.
    """
    def __init__(self) -> None: ...
    def register(self, scheme, repository) -> None:
        """Register artifact repositories provided by other packages"""
    def register_entrypoints(self) -> None: ...
    def get_artifact_repository(self, artifact_uri):
        """Get an artifact repository from the registry based on the scheme of artifact_uri

        :param artifact_uri: The artifact store URI. This URI is used to select which artifact
                             repository implementation to instantiate and is passed to the
                             constructor of the implementation.

        :return: An instance of `mlflow.store.ArtifactRepository` that fulfills the artifact URI
                 requirements.
        """
    def get_registered_artifact_repositories(self):
        """
        Get all registered artifact repositories.

        :return: A dictionary mapping string artifact URI schemes to artifact repositories.
        """

def get_artifact_repository(artifact_uri):
    """Get an artifact repository from the registry based on the scheme of artifact_uri

    :param artifact_uri: The artifact store URI. This URI is used to select which artifact
                         repository implementation to instantiate and is passed to the
                         constructor of the implementation.

    :return: An instance of `mlflow.store.ArtifactRepository` that fulfills the artifact URI
             requirements.
    """
def get_registered_artifact_repositories():
    """
    Get all registered artifact repositories.

    :return: A dictionary mapping string artifact URI schemes to artifact repositories.
    """
