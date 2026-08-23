import abc
import io
import os
from .metadata import Metadata
from .planner import LoadPlan, LoadPlanner, SavePlan, SavePlanner
from .storage import StorageReader, StorageWriter, WriteResult
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Generator
from dataclasses import dataclass
from torch.futures import Future
from typing import List

__all__ = ['FileSystemWriter', 'SlicedBufferedReader', 'FileSystemReader']

@dataclass
class _StorageInfo:
    """
    This is the per entry storage info
    """
    relative_path: str
    offset: int
    length: int
    def __init__(self, relative_path, offset, length) -> None: ...

@dataclass
class _StoragePrefix:
    prefix: str
    def __init__(self, prefix) -> None: ...

class _TensorLoader(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def add(self, size, obj): ...
    def start_loading(self) -> None: ...
    @abstractmethod
    def values(self): ...

class _SerialCpuLoader(_TensorLoader):
    resolve_fun: Incomplete
    items: Incomplete
    def __init__(self, resolve_fun) -> None: ...
    def add(self, size, obj) -> None: ...
    def start_loading(self) -> None: ...
    def values(self) -> Generator[Incomplete, None, None]: ...

class _OverlappingCpuLoader(_TensorLoader):
    resolve_fun: Incomplete
    items: Incomplete
    inflight_threshhold: Incomplete
    in_flight_data: int
    current_items: Incomplete
    idx: int
    started: bool
    stream: Incomplete
    def __init__(self, resolve_fun, stream: Incomplete | None = None, inflight_threshhold: int = 1000000) -> None: ...
    def add(self, size, obj) -> None: ...
    def start_loading(self): ...
    def values(self) -> Generator[Incomplete, Incomplete, None]: ...

class FileSystemWriter(StorageWriter):
    """
    Basic implementation of StorageWriter using file IO.

    This implementation makes the following assumptions and simplifications:

    * The checkpoint path is an empty or non-existing directory.
    * File creation is atomic

    The checkpoint consist of one file per write request plus
    a `.metadata` file with the serialized metadata.

    """
    path: Incomplete
    single_file_per_rank: Incomplete
    sync_files: Incomplete
    thread_count: Incomplete
    per_thread_copy_ahead: Incomplete
    def __init__(self, path: str | os.PathLike, single_file_per_rank: bool = True, sync_files: bool = True, thread_count: int = 1, per_thread_copy_ahead: int = 10000000) -> None:
        """
        Initialize the writer pointing to `path`

        Args:
            path: diretory where the checkpoint will be writen to.
            single_file_per_rank: Produce one file per rank instead of one file per tensor/blob. Default to True.
            sync_files : force files to be synced to permanent storage. Default to True.
            thread_count: Number of IO threads to use to write. Default to 1.
            per_thread_copy_ahead: How many bytes to copy from the GPU ahead of saving then. Default 10Mb.

        N. B. If sync_files is disabled, there's no guarantee that the checkpoint will be consistent in the case of a failure.
        """
    def set_up_storage_writer(self, is_coordinator: bool) -> None: ...
    def prepare_local_plan(self, plan: SavePlan) -> SavePlan: ...
    def prepare_global_plan(self, global_plan: List[SavePlan]) -> List[SavePlan]: ...
    def write_data(self, plan: SavePlan, planner: SavePlanner) -> Future[List[WriteResult]]: ...
    def finish(self, metadata: Metadata, results: List[List[WriteResult]]) -> None: ...

class SlicedBufferedReader(io.BufferedReader):
    offset: Incomplete
    len: Incomplete
    def __init__(self, base_stream: io.RawIOBase, offset: int, len: int) -> None: ...
    def seek(self, __offset: int, __whence: int = ...) -> int: ...
    def tell(self) -> int: ...

class FileSystemReader(StorageReader):
    path: Incomplete
    storage_data: Incomplete
    def __init__(self, path: str | os.PathLike) -> None: ...
    def read_data(self, plan: LoadPlan, planner: LoadPlanner) -> Future[None]: ...
    def read_metadata(self) -> Metadata: ...
    def set_up_storage_reader(self, metadata: Metadata, is_coordinator: bool) -> None: ...
    def prepare_local_plan(self, plan: LoadPlan) -> LoadPlan: ...
    def prepare_global_plan(self, global_plan: List[LoadPlan]) -> List[LoadPlan]: ...
