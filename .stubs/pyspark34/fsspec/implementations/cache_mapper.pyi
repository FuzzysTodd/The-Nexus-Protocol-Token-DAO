import abc
from _typeshed import Incomplete
from fsspec.implementations.local import make_path_posix as make_path_posix
from typing import Any

class AbstractCacheMapper(abc.ABC, metaclass=abc.ABCMeta):
    """Abstract super-class for mappers from remote URLs to local cached
    basenames.
    """
    @abc.abstractmethod
    def __call__(self, path: str) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class BasenameCacheMapper(AbstractCacheMapper):
    """Cache mapper that uses the basename of the remote URL and a fixed number
    of directory levels above this.

    The default is zero directory levels, meaning different paths with the same
    basename will have the same cached basename.
    """
    directory_levels: Incomplete
    def __init__(self, directory_levels: int = 0) -> None: ...
    def __call__(self, path: str) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class HashCacheMapper(AbstractCacheMapper):
    """Cache mapper that uses a hash of the remote URL."""
    def __call__(self, path: str) -> str: ...

def create_cache_mapper(same_names: bool) -> AbstractCacheMapper:
    """Factory method to create cache mapper for backward compatibility with
    ``CachingFileSystem`` constructor using ``same_names`` kwarg.
    """
