from _typeshed import Incomplete
from pyarrow._fs import FileInfo as FileInfo, FileSelector as FileSelector, FileSystem as FileSystem, FileSystemHandler as FileSystemHandler, FileType as FileType, LocalFileSystem as LocalFileSystem, PyFileSystem as PyFileSystem, SubTreeFileSystem as SubTreeFileSystem
from pyarrow._gcsfs import GcsFileSystem as GcsFileSystem
from pyarrow._hdfs import HadoopFileSystem as HadoopFileSystem
from pyarrow._s3fs import AwsDefaultS3RetryStrategy as AwsDefaultS3RetryStrategy, AwsStandardS3RetryStrategy as AwsStandardS3RetryStrategy, S3FileSystem as S3FileSystem, S3LogLevel as S3LogLevel, S3RetryStrategy as S3RetryStrategy, ensure_s3_initialized as ensure_s3_initialized, finalize_s3 as finalize_s3, initialize_s3 as initialize_s3, resolve_s3_region as resolve_s3_region

FileStats = FileInfo

def __getattr__(name) -> None: ...
def copy_files(source, destination, source_filesystem: Incomplete | None = None, destination_filesystem: Incomplete | None = None, *, chunk_size=..., use_threads: bool = True) -> None:
    '''
    Copy files between FileSystems.

    This functions allows you to recursively copy directories of files from
    one file system to another, such as from S3 to your local machine.

    Parameters
    ----------
    source : string
        Source file path or URI to a single file or directory.
        If a directory, files will be copied recursively from this path.
    destination : string
        Destination file path or URI. If `source` is a file, `destination`
        is also interpreted as the destination file (not directory).
        Directories will be created as necessary.
    source_filesystem : FileSystem, optional
        Source filesystem, needs to be specified if `source` is not a URI,
        otherwise inferred.
    destination_filesystem : FileSystem, optional
        Destination filesystem, needs to be specified if `destination` is not
        a URI, otherwise inferred.
    chunk_size : int, default 1MB
        The maximum size of block to read before flushing to the
        destination file. A larger chunk_size will use more memory while
        copying but may help accommodate high latency FileSystems.
    use_threads : bool, default True
        Whether to use multiple threads to accelerate copying.

    Examples
    --------
    Inspect an S3 bucket\'s files:

    >>> s3, path = fs.FileSystem.from_uri(
    ...            "s3://registry.opendata.aws/roda/ndjson/")
    >>> selector = fs.FileSelector(path)
    >>> s3.get_file_info(selector)
    [<FileInfo for \'registry.opendata.aws/roda/ndjson/index.ndjson\':...]

    Copy one file from S3 bucket to a local directory:

    >>> fs.copy_files("s3://registry.opendata.aws/roda/ndjson/index.ndjson",
    ...               "file:///{}/index_copy.ndjson".format(local_path))

    >>> fs.LocalFileSystem().get_file_info(str(local_path)+
    ...                                    \'/index_copy.ndjson\')
    <FileInfo for \'.../index_copy.ndjson\': type=FileType.File, size=...>

    Copy file using a FileSystem object:

    >>> fs.copy_files("registry.opendata.aws/roda/ndjson/index.ndjson",
    ...               "file:///{}/index_copy.ndjson".format(local_path),
    ...               source_filesystem=fs.S3FileSystem())
    '''

class FSSpecHandler(FileSystemHandler):
    """
    Handler for fsspec-based Python filesystems.

    https://filesystem-spec.readthedocs.io/en/latest/index.html

    Parameters
    ----------
    fs : FSSpec-compliant filesystem instance

    Examples
    --------
    >>> PyFileSystem(FSSpecHandler(fsspec_fs)) # doctest: +SKIP
    """
    fs: Incomplete
    def __init__(self, fs) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def get_type_name(self): ...
    def normalize_path(self, path): ...
    def get_file_info(self, paths): ...
    def get_file_info_selector(self, selector): ...
    def create_dir(self, path, recursive) -> None: ...
    def delete_dir(self, path) -> None: ...
    def delete_dir_contents(self, path, missing_dir_ok) -> None: ...
    def delete_root_dir_contents(self) -> None: ...
    def delete_file(self, path) -> None: ...
    def move(self, src, dest) -> None: ...
    def copy_file(self, src, dest) -> None: ...
    def open_input_stream(self, path): ...
    def open_input_file(self, path): ...
    def open_output_stream(self, path, metadata): ...
    def open_append_stream(self, path, metadata): ...
