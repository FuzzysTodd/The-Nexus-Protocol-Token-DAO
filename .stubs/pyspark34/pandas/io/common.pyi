import abc
import dataclasses
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from io import BytesIO, StringIO, TextIOBase
from pandas._typing import BaseBuffer as BaseBuffer, CompressionDict as CompressionDict, CompressionOptions as CompressionOptions, FilePath as FilePath, ReadBuffer as ReadBuffer, ReadCsvBuffer as ReadCsvBuffer, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.compat import get_lzma_file as get_lzma_file
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.dtypes.common import is_bool as is_bool, is_file_like as is_file_like, is_integer as is_integer, is_list_like as is_list_like
from pandas.core.indexes.api import MultiIndex as MultiIndex
from pandas.util._decorators import doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from pathlib import Path
from typing import Any, AnyStr, Generic, Hashable, IO, Literal, Sequence, TypeVar, overload

BaseBufferT = TypeVar('BaseBufferT', bound=BaseBuffer)

@dataclasses.dataclass
class IOArgs:
    """
    Return value of io/common.py:_get_filepath_or_buffer.
    """
    filepath_or_buffer: str | BaseBuffer
    encoding: str
    mode: str
    compression: CompressionDict
    should_close: bool = ...
    def __init__(self, filepath_or_buffer, encoding, mode, compression, should_close) -> None: ...

@dataclasses.dataclass
class IOHandles(Generic[AnyStr]):
    """
    Return value of io/common.py:get_handle

    Can be used as a context manager.

    This is used to easily close created buffers and to handle corner cases when
    TextIOWrapper is inserted.

    handle: The file handle to be used.
    created_handles: All file handles that are created by get_handle
    is_wrapped: Whether a TextIOWrapper needs to be detached.
    """
    handle: IO[AnyStr]
    compression: CompressionDict
    created_handles: list[IO[bytes] | IO[str]] = ...
    is_wrapped: bool = ...
    def close(self) -> None:
        """
        Close all created buffers.

        Note: If a TextIOWrapper was inserted, it is flushed and detached to
        avoid closing the potentially user-created buffer.
        """
    def __enter__(self) -> IOHandles[AnyStr]: ...
    def __exit__(self, *args: Any) -> None: ...
    def __init__(self, handle, compression, created_handles, is_wrapped) -> None: ...

def is_url(url: object) -> bool:
    """
    Check to see if a URL has a valid protocol.

    Parameters
    ----------
    url : str or unicode

    Returns
    -------
    isurl : bool
        If `url` has a valid protocol return True otherwise False.
    """
def validate_header_arg(header: object) -> None: ...
@overload
def stringify_path(filepath_or_buffer: FilePath, convert_file_like: bool = ...) -> str: ...
@overload
def stringify_path(filepath_or_buffer: BaseBufferT, convert_file_like: bool = ...) -> BaseBufferT: ...
def urlopen(*args, **kwargs):
    """
    Lazy-import wrapper for stdlib urlopen, as that imports a big chunk of
    the stdlib.
    """
def is_fsspec_url(url: FilePath | BaseBuffer) -> bool:
    """
    Returns true if the given URL looks like
    something fsspec can handle
    """
def file_path_to_url(path: str) -> str:
    """
    converts an absolute native path to a FILE URL.

    Parameters
    ----------
    path : a path in native format

    Returns
    -------
    a valid FILE URL
    """

extension_to_compression: Incomplete

def get_compression_method(compression: CompressionOptions) -> tuple[str | None, CompressionDict]:
    """
    Simplifies a compression argument to a compression method string and
    a mapping containing additional arguments.

    Parameters
    ----------
    compression : str or mapping
        If string, specifies the compression method. If mapping, value at key
        'method' specifies compression method.

    Returns
    -------
    tuple of ({compression method}, Optional[str]
              {compression arguments}, Dict[str, Any])

    Raises
    ------
    ValueError on mapping missing 'method' key
    """
def infer_compression(filepath_or_buffer: FilePath | BaseBuffer, compression: str | None) -> str | None:
    """
    Get the compression method for filepath_or_buffer. If compression='infer',
    the inferred compression method is returned. Otherwise, the input
    compression method is returned unchanged, unless it's invalid, in which
    case an error is raised.

    Parameters
    ----------
    filepath_or_buffer : str or file handle
        File path or object.
    {compression_options}

        .. versionchanged:: 1.4.0 Zstandard support.

    Returns
    -------
    string or None

    Raises
    ------
    ValueError on invalid compression specified.
    """
def check_parent_directory(path: Path | str) -> None:
    """
    Check if parent directory of a file exists, raise OSError if it does not

    Parameters
    ----------
    path: Path or str
        Path to check parent directory of
    """
@overload
def get_handle(path_or_buf: FilePath | BaseBuffer, mode: str, *, encoding: str | None = ..., compression: CompressionOptions = ..., memory_map: bool = ..., is_text: Literal[False], errors: str | None = ..., storage_options: StorageOptions = ...) -> IOHandles[bytes]: ...
@overload
def get_handle(path_or_buf: FilePath | BaseBuffer, mode: str, *, encoding: str | None = ..., compression: CompressionOptions = ..., memory_map: bool = ..., is_text: Literal[True] = ..., errors: str | None = ..., storage_options: StorageOptions = ...) -> IOHandles[str]: ...
@overload
def get_handle(path_or_buf: FilePath | BaseBuffer, mode: str, *, encoding: str | None = ..., compression: CompressionOptions = ..., memory_map: bool = ..., is_text: bool = ..., errors: str | None = ..., storage_options: StorageOptions = ...) -> IOHandles[str] | IOHandles[bytes]: ...

class _BufferedWriter(BytesIO, ABC, metaclass=abc.ABCMeta):
    """
    Some objects do not support multiple .write() calls (TarFile and ZipFile).
    This wrapper writes to the underlying buffer on close.
    """
    @abstractmethod
    def write_to_buffer(self) -> None: ...
    def close(self) -> None: ...

class _BytesTarFile(_BufferedWriter):
    archive_name: Incomplete
    name: Incomplete
    buffer: Incomplete
    def __init__(self, name: str | None = None, mode: Literal['r', 'a', 'w', 'x'] = 'r', fileobj: ReadBuffer[bytes] | WriteBuffer[bytes] | None = None, archive_name: str | None = None, **kwargs) -> None: ...
    def extend_mode(self, mode: str) -> str: ...
    def infer_filename(self) -> str | None:
        """
        If an explicit archive_name is not given, we still want the file inside the zip
        file not to be named something.tar, because that causes confusion (GH39465).
        """
    def write_to_buffer(self) -> None: ...

class _BytesZipFile(_BufferedWriter):
    archive_name: Incomplete
    buffer: Incomplete
    def __init__(self, file: FilePath | ReadBuffer[bytes] | WriteBuffer[bytes], mode: str, archive_name: str | None = None, **kwargs) -> None: ...
    def infer_filename(self) -> str | None:
        """
        If an explicit archive_name is not given, we still want the file inside the zip
        file not to be named something.zip, because that causes confusion (GH39465).
        """
    def write_to_buffer(self) -> None: ...

class _IOWrapper:
    buffer: Incomplete
    def __init__(self, buffer: BaseBuffer) -> None: ...
    def __getattr__(self, name: str): ...
    def readable(self) -> bool: ...
    def seekable(self) -> bool: ...
    def writable(self) -> bool: ...

class _BytesIOWrapper:
    buffer: Incomplete
    encoding: Incomplete
    overflow: bytes
    def __init__(self, buffer: StringIO | TextIOBase, encoding: str = 'utf-8') -> None: ...
    def __getattr__(self, attr: str): ...
    def read(self, n: int | None = -1) -> bytes: ...

def file_exists(filepath_or_buffer: FilePath | BaseBuffer) -> bool:
    """Test whether file exists."""
def is_potential_multi_index(columns: Sequence[Hashable] | MultiIndex, index_col: bool | Sequence[int] | None = None) -> bool:
    """
    Check whether or not the `columns` parameter
    could be converted into a MultiIndex.

    Parameters
    ----------
    columns : array-like
        Object which may or may not be convertible into a MultiIndex
    index_col : None, bool or list, optional
        Column or columns to use as the (possibly hierarchical) index

    Returns
    -------
    bool : Whether or not columns could become a MultiIndex
    """
def dedup_names(names: Sequence[Hashable], is_potential_multiindex: bool) -> Sequence[Hashable]:
    '''
    Rename column names if duplicates exist.

    Currently the renaming is done by appending a period and an autonumeric,
    but a custom pattern may be supported in the future.

    Examples
    --------
    >>> dedup_names(["x", "y", "x", "x"], is_potential_multiindex=False)
    [\'x\', \'y\', \'x.1\', \'x.2\']
    '''
