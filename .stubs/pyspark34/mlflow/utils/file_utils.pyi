import os
from _typeshed import Incomplete
from collections.abc import Generator
from mlflow.entities import FileInfo as FileInfo
from mlflow.environment_variables import MLFLOW_ENABLE_ARTIFACTS_PROGRESS_BAR as MLFLOW_ENABLE_ARTIFACTS_PROGRESS_BAR
from mlflow.exceptions import MissingConfigException as MissingConfigException
from mlflow.protos.databricks_artifacts_pb2 import ArtifactCredentialType as ArtifactCredentialType
from mlflow.utils import download_cloud_file_chunk as download_cloud_file_chunk, merge_dicts as merge_dicts
from mlflow.utils.os import is_windows as is_windows
from mlflow.utils.process import cache_return_value_per_process as cache_return_value_per_process
from mlflow.utils.request_utils import cloud_storage_http_request as cloud_storage_http_request, download_chunk as download_chunk
from mlflow.utils.rest_utils import augmented_raise_for_status as augmented_raise_for_status
from yaml import SafeLoader as YamlSafeLoader

ENCODING: str
MAX_PARALLEL_DOWNLOAD_WORKERS: Incomplete

class ArtifactProgressBar:
    desc: Incomplete
    total: Incomplete
    step: Incomplete
    pbar: Incomplete
    progress: int
    kwargs: Incomplete
    def __init__(self, desc, total, step, **kwargs) -> None: ...
    def set_pbar(self) -> None: ...
    @classmethod
    def chunks(cls, file_size, desc, chunk_size): ...
    @classmethod
    def files(cls, desc, total): ...
    def update(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...

def is_directory(name): ...
def is_file(name): ...
def exists(name): ...
def list_all(root, filter_func=..., full_path: bool = False):
    """
    List all entities directly under 'dir_name' that satisfy 'filter_func'

    :param root: Name of directory to start search
    :param filter_func: function or lambda that takes path
    :param full_path: If True will return results as full path including `root`

    :return: list of all files or directories that satisfy the criteria.
    """
def list_subdirs(dir_name, full_path: bool = False):
    """
    Equivalent to UNIX command:
      ``find $dir_name -depth 1 -type d``

    :param dir_name: Name of directory to start search
    :param full_path: If True will return results as full path including `root`

    :return: list of all directories directly under 'dir_name'
    """
def list_files(dir_name, full_path: bool = False):
    """
    Equivalent to UNIX command:
      ``find $dir_name -depth 1 -type f``

    :param dir_name: Name of directory to start search
    :param full_path: If True will return results as full path including `root`

    :return: list of all files directly under 'dir_name'
    """
def find(root, name, full_path: bool = False):
    '''
    Search for a file in a root directory. Equivalent to:
      ``find $root -name "$name" -depth 1``

    :param root: Name of root directory for find
    :param name: Name of file or directory to find directly under root directory
    :param full_path: If True will return results as full path including `root`

    :return: list of matching files or directories
    '''
def mkdir(root, name: Incomplete | None = None):
    '''
    Make directory with name "root/name", or just "root" if name is None.

    :param root: Name of parent directory
    :param name: Optional name of leaf directory

    :return: Path to created directory
    '''
def make_containing_dirs(path) -> None:
    """
    Create the base directory for a given file path if it does not exist; also creates parent
    directories.
    """
def write_yaml(root, file_name, data, overwrite: bool = False, sort_keys: bool = True) -> None:
    """
    Write dictionary data in yaml format.

    :param root: Directory name.
    :param file_name: Desired file name. Will automatically add .yaml extension if not given
    :param data: data to be dumped as yaml format
    :param overwrite: If True, will overwrite existing files
    """
def overwrite_yaml(root, file_name, data) -> None:
    """
    Safely overwrites a preexisting yaml file, ensuring that file contents are not deleted or
    corrupted if the write fails. This is achieved by writing contents to a temporary file
    and moving the temporary file to replace the preexisting file, rather than opening the
    preexisting file for a direct write.

    :param root: Directory name.
    :param file_name: File name. Expects to have '.yaml' extension.
    :param data: The data to write, represented as a dictionary.
    """
def read_yaml(root, file_name):
    """
    Read data from yaml file and return as dictionary

    :param root: Directory name
    :param file_name: File name. Expects to have '.yaml' extension

    :return: Data in yaml file as dictionary
    """

class UniqueKeyLoader(YamlSafeLoader):
    def construct_mapping(self, node, deep: bool = False): ...

def render_and_merge_yaml(root, template_name, context_name):
    """
    Renders a Jinja2-templated YAML file based on a YAML context file, merge them, and return
    result as a dictionary.

    :param root: Root directory of the YAML files
    :param template_name: Name of the template file
    :param context_name: Name of the context file
    :return: Data in yaml file as dictionary
    """
def read_parquet_as_pandas_df(data_parquet_path: str):
    """
    Deserialize and load the specified parquet file as a Pandas DataFrame.

    :param data_parquet_path: String, path object (implementing os.PathLike[str]),
    or file-like object implementing a binary read() function. The string
    could be a URL. Valid URL schemes include http, ftp, s3, gs, and file.
    For file URLs, a host is expected. A local file could
    be: file://localhost/path/to/table.parquet. A file URL can also be a path to a
    directory that contains multiple partitioned parquet files. Pyarrow
    support paths to directories as well as file URLs. A directory
    path could be: file://localhost/path/to/tables or s3://bucket/partition_dir.
    :return: pandas dataframe
    """
def write_pandas_df_as_parquet(df, data_parquet_path: str):
    """
    Write a DataFrame to the binary parquet format.

    :param df: pandas data frame.
    :param data_parquet_path: String, path object (implementing os.PathLike[str]),
    or file-like object implementing a binary write() function.
    """

class TempDir:
    def __init__(self, chdr: bool = False, remove_on_exit: bool = True) -> None: ...
    def __enter__(self): ...
    def __exit__(self, tp: type[BaseException] | None, val: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def path(self, *path): ...

def read_file_lines(parent_path, file_name):
    """
    Return the contents of the file as an array where each element is a separate line.

    :param parent_path: Full path to the directory that contains the file.
    :param file_name: Leaf file name.

    :return: All lines in the file as an array.
    """
def read_file(parent_path, file_name):
    """
    Return the contents of the file.

    :param parent_path: Full path to the directory that contains the file.
    :param file_name: Leaf file name.

    :return: The contents of the file.
    """
def get_file_info(path, rel_path):
    """
    Returns file meta data : location, size, ... etc

    :param path: Path to artifact

    :return: `FileInfo` object
    """
def get_relative_path(root_path, target_path):
    """
    Remove root path common prefix and return part of `path` relative to `root_path`.

    :param root_path: Root path
    :param target_path: Desired path for common prefix removal

    :return: Path relative to root_path
    """
def mv(target, new_parent) -> None: ...
def write_to(filename, data) -> None: ...
def append_to(filename, data) -> None: ...
def make_tarfile(output_filename, source_dir, archive_name, custom_filter: Incomplete | None = None): ...
def get_parent_dir(path): ...
def relative_path_to_artifact_path(path): ...
def path_to_local_file_uri(path):
    """
    Convert local filesystem path to local file uri.
    """
def path_to_local_sqlite_uri(path):
    """
    Convert local filesystem path to sqlite uri.
    """
def local_file_uri_to_path(uri):
    """
    Convert URI to local filesystem path.
    No-op if the uri does not have the expected scheme.
    """
def get_local_path_or_none(path_or_uri):
    """Check if the argument is a local path (no scheme or file:///) and return local path if true,
    None otherwise.
    """
def yield_file_in_chunks(file, chunk_size: int = 100000000) -> Generator[Incomplete, None, None]:
    """
    Generator to chunk-ify the inputted file based on the chunk-size.
    """
def download_file_using_http_uri(http_uri, download_path, chunk_size: int = 100000000, headers: Incomplete | None = None) -> None:
    """
    Downloads a file specified using the `http_uri` to a local `download_path`. This function
    uses a `chunk_size` to ensure an OOM error is not raised a large file is downloaded.

    Note : This function is meant to download files using presigned urls from various cloud
            providers.
    """
def parallelized_download_file_using_http_uri(thread_pool_executor, http_uri, download_path, file_size, uri_type, chunk_size, env, headers: Incomplete | None = None):
    """
    Downloads a file specified using the `http_uri` to a local `download_path`. This function
    sends multiple requests in parallel each specifying its own desired byte range as a header,
    then reconstructs the file from the downloaded chunks. This allows for downloads of large files
    without OOM risk.

    Note : This function is meant to download files using presigned urls from various cloud
            providers.
    Returns a dict of chunk index : exception, if one was thrown for that index.
    """
def get_or_create_tmp_dir():
    """
    Get or create a temporary directory which will be removed once python process exit.
    """
def get_or_create_nfs_tmp_dir():
    """
    Get or create a temporary NFS directory which will be removed once python process exit.
    """
def write_spark_dataframe_to_parquet_on_local_disk(spark_df, output_path) -> None:
    """
    Write spark dataframe in parquet format to local disk.

    :param spark_df: Spark dataframe
    :param output_path: path to write the data to
    """
def shutil_copytree_without_file_permissions(src_dir, dst_dir) -> None:
    """
    Copies the directory src_dir into dst_dir, without preserving filesystem permissions
    """
def contains_path_separator(path):
    """
    Returns True if a path contains a path separator, False otherwise.
    """
def read_chunk(path: os.PathLike, size: int, start_byte: int = 0) -> bytes:
    """
    Read a chunk of bytes from a file.

    :param path: Path to the file.
    :param size: The size of the chunk.
    :param start_byte: The start byte of the chunk.
    :return: The chunk of bytes.
    """
def remove_on_error(path: os.PathLike, onerror: Incomplete | None = None):
    """
    A context manager that removes a file or directory if an exception is raised during execution.

    :param path: Path to the file or directory.
    :param onerror: A callback function that will be called with the captured exception before
                    the file or directory is removed. For example, you can use this callback to
                    log the exception.
    """
def chdir(path: str) -> None:
    """
    Temporarily change the current working directory to the specified path.

    :param path: The path to use as the temporary working directory.
    """
