from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.store.db.db_types import DATABASE_ENGINES as DATABASE_ENGINES
from mlflow.utils.os import is_windows as is_windows
from typing import Any, Tuple

def is_local_uri(uri, is_tracking_or_registry_uri: bool = True):
    """
    Returns true if the specified URI is a local file path (/foo or file:/foo).

    :param uri: The URI.
    :param is_tracking_uri: Whether or not the specified URI is an MLflow Tracking or MLflow
                            Model Registry URI. Examples of other URIs are MLflow artifact URIs,
                            filesystem paths, etc.
    """
def is_file_uri(uri): ...
def is_http_uri(uri): ...
def is_databricks_uri(uri):
    """
    Databricks URIs look like 'databricks' (default profile) or 'databricks://profile'
    or 'databricks://secret_scope:secret_key_prefix'.
    """
def is_databricks_unity_catalog_uri(uri): ...
def construct_db_uri_from_profile(profile): ...
def validate_db_scope_prefix_info(scope, prefix) -> None: ...
def get_db_info_from_uri(uri):
    """
    Get the Databricks profile specified by the tracking URI (if any), otherwise
    returns None.
    """
def get_databricks_profile_uri_from_artifact_uri(uri, result_scheme: str = 'databricks'):
    """
    Retrieves the netloc portion of the URI as a ``databricks://`` or `databricks-uc://` URI,
    if it is a proper Databricks profile specification, e.g.
    ``profile@databricks`` or ``secret_scope:key_prefix@databricks``.
    """
def remove_databricks_profile_info_from_artifact_uri(artifact_uri):
    """
    Only removes the netloc portion of the URI if it is a Databricks
    profile specification, e.g.
    ``profile@databricks`` or ``secret_scope:key_prefix@databricks``.
    """
def add_databricks_profile_info_to_artifact_uri(artifact_uri, databricks_profile_uri):
    """
    Throws an exception if ``databricks_profile_uri`` is not valid.
    """
def extract_db_type_from_uri(db_uri):
    """
    Parse the specified DB URI to extract the database type. Confirm the database type is
    supported. If a driver is specified, confirm it passes a plausible regex.
    """
def get_uri_scheme(uri_or_path): ...
def extract_and_normalize_path(uri): ...
def append_to_uri_path(uri, *paths):
    '''
    Appends the specified POSIX `paths` to the path component of the specified `uri`.

    :param uri: The input URI, represented as a string.
    :param paths: The POSIX paths to append to the specified `uri`\'s path component.
    :return: A new URI with a path component consisting of the specified `paths` appended to
             the path component of the specified `uri`.

    >>> uri1 = "s3://root/base/path?param=value"
    >>> uri1 = append_to_uri_path(uri1, "some/subpath", "/anotherpath")
    >>> assert uri1 == "s3://root/base/path/some/subpath/anotherpath?param=value"
    >>> uri2 = "a/posix/path"
    >>> uri2 = append_to_uri_path(uri2, "/some", "subpath")
    >>> assert uri2 == "a/posixpath/some/subpath"
    '''
def append_to_uri_query_params(uri, *query_params: Tuple[str, Any]) -> str:
    '''
    Appends the specified query parameters to an existing URI.

    :param uri: The URI to which to append query parameters.
    :param query_params: Query parameters to append. Each parameter should
                         be a 2-element tuple. For example, ``("key", "value")``.
    '''
def is_databricks_acled_artifacts_uri(artifact_uri): ...
def is_databricks_model_registry_artifacts_uri(artifact_uri): ...
def is_valid_dbfs_uri(uri): ...
def dbfs_hdfs_uri_to_fuse_path(dbfs_uri):
    '''
    Converts the provided DBFS URI into a DBFS FUSE path
    :param dbfs_uri: A DBFS URI like "dbfs:/my-directory". Can also be a scheme-less URI like
                     "/my-directory" if running in an environment where the default HDFS filesystem
                     is "dbfs:/" (e.g. Databricks)
    :return A DBFS FUSE-style path, e.g. "/dbfs/my-directory"
    '''
def resolve_uri_if_local(local_uri):
    """
    if `local_uri` is passed in as a relative local path, this function
    resolves it to absolute path relative to current working directory.

    :param local_uri: Relative or absolute path or local file uri

    :return: a fully-formed absolute uri path or an absolute filesystem path
    """
def generate_tmp_dfs_path(dfs_tmp): ...
