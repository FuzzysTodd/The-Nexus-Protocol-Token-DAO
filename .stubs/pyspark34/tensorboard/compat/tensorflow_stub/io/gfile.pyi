import dataclasses
from _typeshed import Incomplete
from collections.abc import Generator
from tensorboard.compat.tensorflow_stub import compat as compat, errors as errors

S3_ENABLED: bool
FSSPEC_ENABLED: bool

def register_filesystem(prefix, filesystem) -> None: ...
def get_filesystem(filename):
    """Return the registered filesystem for the given file."""

@dataclasses.dataclass(frozen=True)
class StatData:
    """Data returned from the Stat call.

    Attributes:
      length: Length of the data content.
    """
    length: int
    def __init__(self, length) -> None: ...

class LocalFileSystem:
    """Provides local fileystem access."""
    def exists(self, filename):
        """Determines whether a path exists or not."""
    def join(self, path, *paths):
        """Join paths with path delimiter."""
    def read(self, filename, binary_mode: bool = False, size: Incomplete | None = None, continue_from: Incomplete | None = None):
        """Reads contents of a file to a string.

        Args:
            filename: string, a path
            binary_mode: bool, read as binary if True, otherwise text
            size: int, number of bytes or characters to read, otherwise
                read all the contents of the file (from the continuation
                marker, if present).
            continue_from: An opaque value returned from a prior invocation of
                `read(...)` marking the last read position, so that reading
                may continue from there.  Otherwise read from the beginning.

        Returns:
            A tuple of `(data, continuation_token)` where `data' provides either
            bytes read from the file (if `binary_mode == true`) or the decoded
            string representation thereof (otherwise), and `continuation_token`
            is an opaque value that can be passed to the next invocation of
            `read(...) ' in order to continue from the last read position.
        """
    def write(self, filename, file_content, binary_mode: bool = False) -> None:
        """Writes string file contents to a file, overwriting any existing
        contents.

        Args:
            filename: string, a path
            file_content: string, the contents
            binary_mode: bool, write as binary if True, otherwise text
        """
    def append(self, filename, file_content, binary_mode: bool = False) -> None:
        """Append string file contents to a file.

        Args:
            filename: string, a path
            file_content: string, the contents to append
            binary_mode: bool, write as binary if True, otherwise text
        """
    def glob(self, filename):
        """Returns a list of files that match the given pattern(s)."""
    def isdir(self, dirname):
        """Returns whether the path is a directory or not."""
    def listdir(self, dirname):
        """Returns a list of entries contained within a directory."""
    def makedirs(self, path) -> None:
        """Creates a directory and all parent/intermediate directories."""
    def stat(self, filename):
        """Returns file statistics for a given path."""

class S3FileSystem:
    """Provides filesystem access to S3."""
    def __init__(self) -> None: ...
    def bucket_and_path(self, url):
        """Split an S3-prefixed URL into bucket and path."""
    def exists(self, filename):
        """Determines whether a path exists or not."""
    def join(self, path, *paths):
        """Join paths with a slash."""
    def read(self, filename, binary_mode: bool = False, size: Incomplete | None = None, continue_from: Incomplete | None = None):
        """Reads contents of a file to a string.

        Args:
            filename: string, a path
            binary_mode: bool, read as binary if True, otherwise text
            size: int, number of bytes or characters to read, otherwise
                read all the contents of the file (from the continuation
                marker, if present).
            continue_from: An opaque value returned from a prior invocation of
                `read(...)` marking the last read position, so that reading
                may continue from there.  Otherwise read from the beginning.

        Returns:
            A tuple of `(data, continuation_token)` where `data' provides either
            bytes read from the file (if `binary_mode == true`) or the decoded
            string representation thereof (otherwise), and `continuation_token`
            is an opaque value that can be passed to the next invocation of
            `read(...) ' in order to continue from the last read position.
        """
    def write(self, filename, file_content, binary_mode: bool = False) -> None:
        """Writes string file contents to a file.

        Args:
            filename: string, a path
            file_content: string, the contents
            binary_mode: bool, write as binary if True, otherwise text
        """
    def glob(self, filename):
        """Returns a list of files that match the given pattern(s)."""
    def isdir(self, dirname):
        """Returns whether the path is a directory or not."""
    def listdir(self, dirname):
        """Returns a list of entries contained within a directory."""
    def makedirs(self, dirname) -> None:
        """Creates a directory and all parent/intermediate directories."""
    def stat(self, filename):
        """Returns file statistics for a given path."""

class FSSpecFileSystem:
    """Provides filesystem access via fsspec.

    The current gfile interface doesn't map perfectly to the fsspec interface
    leading to some notable inefficiencies.

    * Reads and writes to files cause the file to be reopened each time which
      can cause a performance hit when accessing local file systems.
    * walk doesn't use the native fsspec walk function so performance may be
      slower.

    See https://github.com/tensorflow/tensorboard/issues/5286 for more info on
    limitations.
    """
    SEPARATOR: str
    CHAIN_SEPARATOR: str
    def exists(self, filename):
        """Determines whether a path exists or not."""
    def join(self, path, *paths):
        """Join paths with a slash."""
    def read(self, filename, binary_mode: bool = False, size: Incomplete | None = None, continue_from: Incomplete | None = None):
        """Reads contents of a file to a string.

        Args:
            filename: string, a path
            binary_mode: bool, read as binary if True, otherwise text
            size: int, number of bytes or characters to read, otherwise
                read all the contents of the file (from the continuation
                marker, if present).
            continue_from: An opaque value returned from a prior invocation of
                `read(...)` marking the last read position, so that reading
                may continue from there.  Otherwise read from the beginning.

        Returns:
            A tuple of `(data, continuation_token)` where `data' provides either
            bytes read from the file (if `binary_mode == true`) or the decoded
            string representation thereof (otherwise), and `continuation_token`
            is an opaque value that can be passed to the next invocation of
            `read(...) ' in order to continue from the last read position.
        """
    def write(self, filename, file_content, binary_mode: bool = False) -> None:
        """Writes string file contents to a file.

        Args:
            filename: string, a path
            file_content: string, the contents
            binary_mode: bool, write as binary if True, otherwise text
        """
    def append(self, filename, file_content, binary_mode: bool = False) -> None:
        """Append string file contents to a file.

        Args:
            filename: string, a path
            file_content: string, the contents to append
            binary_mode: bool, write as binary if True, otherwise text
        """
    def glob(self, filename):
        """Returns a list of files that match the given pattern(s)."""
    def isdir(self, dirname):
        """Returns whether the path is a directory or not."""
    def listdir(self, dirname):
        """Returns a list of entries contained within a directory."""
    def makedirs(self, dirname):
        """Creates a directory and all parent/intermediate directories."""
    def stat(self, filename):
        """Returns file statistics for a given path."""

class GFile:
    filename: Incomplete
    fs: Incomplete
    fs_supports_append: Incomplete
    buff: Incomplete
    buff_chunk_size: Incomplete
    buff_offset: int
    continuation_token: Incomplete
    write_temp: Incomplete
    write_started: bool
    binary_mode: Incomplete
    write_mode: Incomplete
    closed: bool
    def __init__(self, filename, mode) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def __iter__(self): ...
    def read(self, n: Incomplete | None = None):
        """Reads contents of file to a string.

        Args:
            n: int, number of bytes or characters to read, otherwise
                read all the contents of the file

        Returns:
            Subset of the contents of the file as a string or bytes.
        """
    def write(self, file_content) -> None:
        """Writes string file contents to file, clearing contents of the file
        on first write and then appending on subsequent calls.

        Args:
            file_content: string, the contents
        """
    def __next__(self): ...
    def next(self): ...
    def flush(self) -> None: ...
    def close(self) -> None: ...

def exists(filename):
    """Determines whether a path exists or not.

    Args:
      filename: string, a path

    Returns:
      True if the path exists, whether its a file or a directory.
      False if the path does not exist and there are no filesystem errors.

    Raises:
      errors.OpError: Propagates any errors reported by the FileSystem API.
    """
def glob(filename):
    """Returns a list of files that match the given pattern(s).

    Args:
      filename: string or iterable of strings. The glob pattern(s).

    Returns:
      A list of strings containing filenames that match the given pattern(s).

    Raises:
      errors.OpError: If there are filesystem / directory listing errors.
    """
def isdir(dirname):
    """Returns whether the path is a directory or not.

    Args:
      dirname: string, path to a potential directory

    Returns:
      True, if the path is a directory; False otherwise
    """
def listdir(dirname):
    '''Returns a list of entries contained within a directory.

    The list is in arbitrary order. It does not contain the special entries "."
    and "..".

    Args:
      dirname: string, path to a directory

    Returns:
      [filename1, filename2, ... filenameN] as strings

    Raises:
      errors.NotFoundError if directory doesn\'t exist
    '''
def makedirs(path):
    """Creates a directory and all parent/intermediate directories.

    It succeeds if path already exists and is writable.

    Args:
      path: string, name of the directory to be created
    """
def walk(top, topdown: bool = True, onerror: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """Recursive directory tree generator for directories.

    Args:
      top: string, a Directory name
      topdown: bool, Traverse pre order if True, post order if False.
      onerror: optional handler for errors. Should be a function, it will be
        called with the error as argument. Rethrowing the error aborts the walk.

    Errors that happen while listing directories are ignored.

    Yields:
      Each yield is a 3-tuple:  the pathname of a directory, followed by lists
      of all its subdirectories and leaf files.
      (dirname, [subdirname, subdirname, ...], [filename, filename, ...])
      as strings
    """
def stat(filename):
    """Returns file statistics for a given path.

    Args:
      filename: string, path to a file

    Returns:
      FileStatistics struct that contains information about the path

    Raises:
      errors.OpError: If the operation fails.
    """
