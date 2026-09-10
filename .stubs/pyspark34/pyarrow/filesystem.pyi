from _typeshed import Incomplete
from collections.abc import Generator
from pyarrow.util import implements as implements

class FileSystem:
    """
    Abstract filesystem interface.
    """
    def cat(self, path):
        """
        Return contents of file as a bytes object.

        Parameters
        ----------
        path : str
            File path to read content from.

        Returns
        -------
        contents : bytes
        """
    def ls(self, path) -> None:
        """
        Return list of file paths.

        Parameters
        ----------
        path : str
            Directory to list contents from.
        """
    def delete(self, path, recursive: bool = False) -> None:
        """
        Delete the indicated file or directory.

        Parameters
        ----------
        path : str
            Path to delete.
        recursive : bool, default False
            If True, also delete child paths for directories.
        """
    def disk_usage(self, path):
        """
        Compute bytes used by all contents under indicated path in file tree.

        Parameters
        ----------
        path : str
            Can be a file path or directory.

        Returns
        -------
        usage : int
        """
    def stat(self, path) -> None:
        """
        Information about a filesystem entry.

        Returns
        -------
        stat : dict
        """
    def rm(self, path, recursive: bool = False):
        """
        Alias for FileSystem.delete.
        """
    def mv(self, path, new_path):
        """
        Alias for FileSystem.rename.
        """
    def rename(self, path, new_path) -> None:
        """
        Rename file, like UNIX mv command.

        Parameters
        ----------
        path : str
            Path to alter.
        new_path : str
            Path to move to.
        """
    def mkdir(self, path, create_parents: bool = True) -> None:
        """
        Create a directory.

        Parameters
        ----------
        path : str
            Path to the directory.
        create_parents : bool, default True
            If the parent directories don't exists create them as well.
        """
    def exists(self, path) -> None:
        """
        Return True if path exists.

        Parameters
        ----------
        path : str
            Path to check.
        """
    def isdir(self, path) -> None:
        """
        Return True if path is a directory.

        Parameters
        ----------
        path : str
            Path to check.
        """
    def isfile(self, path) -> None:
        """
        Return True if path is a file.

        Parameters
        ----------
        path : str
            Path to check.
        """
    def read_parquet(self, path, columns: Incomplete | None = None, metadata: Incomplete | None = None, schema: Incomplete | None = None, use_threads: bool = True, use_pandas_metadata: bool = False):
        """
        Read Parquet data from path in file system. Can read from a single file
        or a directory of files.

        Parameters
        ----------
        path : str
            Single file path or directory
        columns : List[str], optional
            Subset of columns to read.
        metadata : pyarrow.parquet.FileMetaData
            Known metadata to validate files against.
        schema : pyarrow.parquet.Schema
            Known schema to validate files against. Alternative to metadata
            argument.
        use_threads : bool, default True
            Perform multi-threaded column reads.
        use_pandas_metadata : bool, default False
            If True and file has custom pandas schema metadata, ensure that
            index columns are also loaded.

        Returns
        -------
        table : pyarrow.Table
        """
    def open(self, path, mode: str = 'rb') -> None:
        """
        Open file for reading or writing.
        """
    @property
    def pathsep(self): ...

class LocalFileSystem(FileSystem):
    def __init__(self) -> None: ...
    @classmethod
    def get_instance(cls): ...
    def ls(self, path): ...
    def mkdir(self, path, create_parents: bool = True) -> None: ...
    def isdir(self, path): ...
    def isfile(self, path): ...
    def exists(self, path): ...
    def open(self, path, mode: str = 'rb'):
        """
        Open file for reading or writing.
        """
    @property
    def pathsep(self): ...
    def walk(self, path):
        """
        Directory tree generator, see os.walk.
        """

class DaskFileSystem(FileSystem):
    """
    Wraps s3fs Dask filesystem implementation like s3fs, gcsfs, etc.
    """
    fs: Incomplete
    def __init__(self, fs) -> None: ...
    def isdir(self, path) -> None: ...
    def isfile(self, path) -> None: ...
    def delete(self, path, recursive: bool = False): ...
    def exists(self, path): ...
    def mkdir(self, path, create_parents: bool = True): ...
    def open(self, path, mode: str = 'rb'):
        """
        Open file for reading or writing.
        """
    def ls(self, path, detail: bool = False): ...
    def walk(self, path):
        """
        Directory tree generator, like os.walk.
        """

class S3FSWrapper(DaskFileSystem):
    def isdir(self, path): ...
    def isfile(self, path): ...
    def walk(self, path, refresh: bool = False) -> Generator[Incomplete, Incomplete, None]:
        """
        Directory tree generator, like os.walk.

        Generator version of what is in s3fs, which yields a flattened list of
        files.
        """

def resolve_filesystem_and_path(where, filesystem: Incomplete | None = None):
    """
    Return filesystem from path which could be an HDFS URI, a local URI,
    or a plain filesystem path.
    """
