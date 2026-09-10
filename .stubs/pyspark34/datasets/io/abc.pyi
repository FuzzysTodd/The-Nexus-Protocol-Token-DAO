import abc
from .. import Dataset as Dataset, DatasetDict as DatasetDict, Features as Features, IterableDataset as IterableDataset, IterableDatasetDict as IterableDatasetDict, NamedSplit as NamedSplit
from ..utils.typing import NestedDataStructureLike as NestedDataStructureLike, PathLike as PathLike
from _typeshed import Incomplete
from abc import ABC, abstractmethod

class AbstractDatasetReader(ABC, metaclass=abc.ABCMeta):
    path_or_paths: Incomplete
    split: Incomplete
    features: Incomplete
    cache_dir: Incomplete
    keep_in_memory: Incomplete
    streaming: Incomplete
    num_proc: Incomplete
    kwargs: Incomplete
    def __init__(self, path_or_paths: NestedDataStructureLike[PathLike] | None = None, split: NamedSplit | None = None, features: Features | None = None, cache_dir: str = None, keep_in_memory: bool = False, streaming: bool = False, num_proc: int | None = None, **kwargs) -> None: ...
    @abstractmethod
    def read(self) -> Dataset | DatasetDict | IterableDataset | IterableDatasetDict: ...

class AbstractDatasetInputStream(ABC, metaclass=abc.ABCMeta):
    features: Incomplete
    cache_dir: Incomplete
    keep_in_memory: Incomplete
    streaming: Incomplete
    num_proc: Incomplete
    kwargs: Incomplete
    def __init__(self, features: Features | None = None, cache_dir: str = None, keep_in_memory: bool = False, streaming: bool = False, num_proc: int | None = None, **kwargs) -> None: ...
    @abstractmethod
    def read(self) -> Dataset | IterableDataset: ...
