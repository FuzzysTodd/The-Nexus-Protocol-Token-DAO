from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.store.artifact.artifact_repository_registry import get_artifact_repository as get_artifact_repository
from mlflow.store.artifact.dbfs_artifact_repo import DbfsRestArtifactRepository as DbfsRestArtifactRepository
from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository as ModelsArtifactRepository
from mlflow.utils.file_utils import path_to_local_file_uri as path_to_local_file_uri
from mlflow.utils.uri import add_databricks_profile_info_to_artifact_uri as add_databricks_profile_info_to_artifact_uri, append_to_uri_path as append_to_uri_path

def get_artifact_uri(run_id, artifact_path: Incomplete | None = None, tracking_uri: Incomplete | None = None):
    """
    Get the absolute URI of the specified artifact in the specified run. If `path` is not specified,
    the artifact root URI of the specified run will be returned; calls to ``log_artifact``
    and ``log_artifacts`` write artifact(s) to subdirectories of the artifact root URI.

    :param run_id: The ID of the run for which to obtain an absolute artifact URI.
    :param artifact_path: The run-relative artifact path. For example,
                          ``path/to/artifact``. If unspecified, the artifact root URI for the
                          specified run will be returned.
    :param tracking_uri: The tracking URI from which to get the run and its artifact location. If
                         not given, the current default tracking URI is used.
    :return: An *absolute* URI referring to the specified artifact or the specified run's artifact
             root. For example, if an artifact path is provided and the specified run uses an
             S3-backed  store, this may be a uri of the form
             ``s3://<bucket_name>/path/to/artifact/root/path/to/artifact``. If an artifact path
             is not provided and the specified run uses an S3-backed store, this may be a URI of
             the form ``s3://<bucket_name>/path/to/artifact/root``.
    """
