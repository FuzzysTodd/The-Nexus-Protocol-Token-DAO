from abc import ABCMeta, abstractmethod
from pandas import DataFrame as DataFrame
from pandas._typing import CompressionOptions as CompressionOptions, FilePath as FilePath, ReadBuffer as ReadBuffer
from pandas.io.common import stringify_path as stringify_path
from pandas.util._decorators import doc as doc
from types import TracebackType
from typing import Hashable, overload

class ReaderBase(metaclass=ABCMeta):
    """
    Protocol for XportReader and SAS7BDATReader classes.
    """
    @abstractmethod
    def read(self, nrows: int | None = None) -> DataFrame: ...
    @abstractmethod
    def close(self) -> None: ...
    def __enter__(self) -> ReaderBase: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...

@overload
def read_sas(filepath_or_buffer: FilePath | ReadBuffer[bytes], *, format: str | None = ..., index: Hashable | None = ..., encoding: str | None = ..., chunksize: int = ..., iterator: bool = ..., compression: CompressionOptions = ...) -> ReaderBase: ...
@overload
def read_sas(filepath_or_buffer: FilePath | ReadBuffer[bytes], *, format: str | None = ..., index: Hashable | None = ..., encoding: str | None = ..., chunksize: None = ..., iterator: bool = ..., compression: CompressionOptions = ...) -> DataFrame | ReaderBase: ...
