import logging
import os
import pathlib
from _typeshed import Incomplete
from fsspec.spec import AbstractFileSystem as AbstractFileSystem
from typing import Any, Callable, IO, Iterable, Iterator, Sequence, TypeVar
from typing_extensions import TypeGuard

DEFAULT_BLOCK_SIZE: Incomplete
T = TypeVar('T')

def infer_storage_options(urlpath: str, inherit_storage_options: dict[str, Any] | None = None) -> dict[str, Any]:
    '''Infer storage options from URL path and merge it with existing storage
    options.

    Parameters
    ----------
    urlpath: str or unicode
        Either local absolute file path or URL (hdfs://namenode:8020/file.csv)
    inherit_storage_options: dict (optional)
        Its contents will get merged with the inferred information from the
        given path

    Returns
    -------
    Storage options dict.

    Examples
    --------
    >>> infer_storage_options(\'/mnt/datasets/test.csv\')  # doctest: +SKIP
    {"protocol": "file", "path", "/mnt/datasets/test.csv"}
    >>> infer_storage_options(
    ...     \'hdfs://username:pwd@node:123/mnt/datasets/test.csv?q=1\',
    ...     inherit_storage_options={\'extra\': \'value\'},
    ... )  # doctest: +SKIP
    {"protocol": "hdfs", "username": "username", "password": "pwd",
    "host": "node", "port": 123, "path": "/mnt/datasets/test.csv",
    "url_query": "q=1", "extra": "value"}
    '''
def update_storage_options(options: dict[str, Any], inherited: dict[str, Any] | None = None) -> None: ...

compressions: dict[str, str]

def infer_compression(filename: str) -> str | None:
    """Infer compression, if available, from filename.

    Infer a named compression type, if registered and available, from filename
    extension. This includes builtin (gz, bz2, zip) compressions, as well as
    optional compressions. See fsspec.compression.register_compression.
    """
def build_name_function(max_int: float) -> Callable[[int], str]:
    """Returns a function that receives a single integer
    and returns it as a string padded by enough zero characters
    to align with maximum possible integer

    >>> name_f = build_name_function(57)

    >>> name_f(7)
    '07'
    >>> name_f(31)
    '31'
    >>> build_name_function(1000)(42)
    '0042'
    >>> build_name_function(999)(42)
    '042'
    >>> build_name_function(0)(0)
    '0'
    """
def seek_delimiter(file: IO[bytes], delimiter: bytes, blocksize: int) -> bool:
    """Seek current file to file start, file end, or byte after delimiter seq.

    Seeks file to next chunk delimiter, where chunks are defined on file start,
    a delimiting sequence, and file end. Use file.tell() to see location afterwards.
    Note that file start is a valid split, so must be at offset > 0 to seek for
    delimiter.

    Parameters
    ----------
    file: a file
    delimiter: bytes
        a delimiter like ``b'\\n'`` or message sentinel, matching file .read() type
    blocksize: int
        Number of bytes to read from the file at once.


    Returns
    -------
    Returns True if a delimiter was found, False if at file start or end.

    """
def read_block(f: IO[bytes], offset: int, length: int | None, delimiter: bytes | None = None, split_before: bool = False) -> bytes:
    """Read a block of bytes from a file

    Parameters
    ----------
    f: File
        Open file
    offset: int
        Byte offset to start read
    length: int
        Number of bytes to read, read through end of file if None
    delimiter: bytes (optional)
        Ensure reading starts and stops at delimiter bytestring
    split_before: bool (optional)
        Start/stop read *before* delimiter bytestring.


    If using the ``delimiter=`` keyword argument we ensure that the read
    starts and stops at delimiter boundaries that follow the locations
    ``offset`` and ``offset + length``.  If ``offset`` is zero then we
    start at zero, regardless of delimiter.  The bytestring returned WILL
    include the terminating delimiter string.

    Examples
    --------

    >>> from io import BytesIO  # doctest: +SKIP
    >>> f = BytesIO(b'Alice, 100\\nBob, 200\\nCharlie, 300')  # doctest: +SKIP
    >>> read_block(f, 0, 13)  # doctest: +SKIP
    b'Alice, 100\\nBo'

    >>> read_block(f, 0, 13, delimiter=b'\\n')  # doctest: +SKIP
    b'Alice, 100\\nBob, 200\\n'

    >>> read_block(f, 10, 10, delimiter=b'\\n')  # doctest: +SKIP
    b'Bob, 200\\nCharlie, 300'
    """
def tokenize(*args: Any, **kwargs: Any) -> str:
    """Deterministic token

    (modified from dask.base)

    >>> tokenize([1, 2, '3'])
    '9d71491b50023b06fc76928e6eddb952'

    >>> tokenize('Hello') == tokenize('Hello')
    True
    """
def stringify_path(filepath: str | os.PathLike[str] | pathlib.Path) -> str:
    """Attempt to convert a path-like object to a string.

    Parameters
    ----------
    filepath: object to be converted

    Returns
    -------
    filepath_str: maybe a string version of the object

    Notes
    -----
    Objects supporting the fspath protocol are coerced according to its
    __fspath__ method.

    For backwards compatibility with older Python version, pathlib.Path
    objects are specially coerced.

    Any other object is passed through unchanged, which includes bytes,
    strings, buffers, or anything else that's not even path-like.
    """
def make_instance(cls, args: Sequence[Any], kwargs: dict[str, Any]) -> T: ...
def common_prefix(paths: Iterable[str]) -> str:
    """For a list of paths, find the shortest prefix common to all"""
def other_paths(paths: list[str], path2: str | list[str], exists: bool = False, flatten: bool = False) -> list[str]:
    """In bulk file operations, construct a new file tree from a list of files

    Parameters
    ----------
    paths: list of str
        The input file tree
    path2: str or list of str
        Root to construct the new list in. If this is already a list of str, we just
        assert it has the right number of elements.
    exists: bool (optional)
        For a str destination, it is already exists (and is a dir), files should
        end up inside.
    flatten: bool (optional)
        Whether to flatten the input directory tree structure so that the output files
        are in the same directory.

    Returns
    -------
    list of str
    """
def is_exception(obj: Any) -> bool: ...
def isfilelike(f: Any) -> TypeGuard[IO[bytes]]: ...
def get_protocol(url: str) -> str: ...
def can_be_local(path: str) -> bool:
    """Can the given URL be used with open_local?"""
def get_package_version_without_import(name: str) -> str | None:
    """For given package name, try to find the version without importing it

    Import and package.__version__ is still the backup here, so an import
    *might* happen.

    Returns either the version string, or None if the package
    or the version was not readily  found.
    """
def setup_logging(logger: logging.Logger | None = None, logger_name: str | None = None, level: str = 'DEBUG', clear: bool = True) -> logging.Logger: ...
def mirror_from(origin_name: str, methods: Iterable[str]) -> Callable[[type[T]], type[T]]:
    """Mirror attributes and methods from the given
    origin_name attribute of the instance to the
    decorated class"""
def nullcontext(obj: T) -> Iterator[T]: ...
def merge_offset_ranges(paths: list[str], starts: list[int] | int, ends: list[int] | int, max_gap: int = 0, max_block: int | None = None, sort: bool = True) -> tuple[list[str], list[int], list[int]]:
    """Merge adjacent byte-offset ranges when the inter-range
    gap is <= `max_gap`, and when the merged byte range does not
    exceed `max_block` (if specified). By default, this function
    will re-order the input paths and byte ranges to ensure sorted
    order. If the user can guarantee that the inputs are already
    sorted, passing `sort=False` will skip the re-ordering.
    """
def file_size(filelike: IO[bytes]) -> int:
    """Find length of any open read-mode file-like"""
def atomic_write(path: str, mode: str = 'wb'):
    """
    A context manager that opens a temporary file next to `path` and, on exit,
    replaces `path` with the temporary file, thereby updating `path`
    atomically.
    """
