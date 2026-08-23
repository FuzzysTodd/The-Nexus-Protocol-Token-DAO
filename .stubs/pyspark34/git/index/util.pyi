import struct
from _typeshed import Incomplete
from git.types import PathLike, _T
from types import TracebackType
from typing import Callable, Type

__all__ = ['TemporaryFileSwap', 'post_clear_cache', 'default_index', 'git_working_dir']

pack = struct.pack
unpack = struct.unpack

class TemporaryFileSwap:
    """Utility class moving a file to a temporary location within the same directory
    and moving it back on to where on object deletion."""
    file_path: Incomplete
    tmp_file_path: Incomplete
    def __init__(self, file_path: PathLike) -> None: ...
    def __enter__(self) -> TemporaryFileSwap: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool: ...

def post_clear_cache(func: Callable[..., _T]) -> Callable[..., _T]:
    """Decorator for functions that alter the index using the git command. This would
    invalidate our possibly existing entries dictionary which is why it must be
    deleted to allow it to be lazily reread later.

    :note:
        This decorator will not be required once all functions are implemented
        natively which in fact is possible, but probably not feasible performance wise.
    """
def default_index(func: Callable[..., _T]) -> Callable[..., _T]:
    """Decorator assuring the wrapped method may only run if we are the default
    repository index. This is as we rely on git commands that operate
    on that index only."""
def git_working_dir(func: Callable[..., _T]) -> Callable[..., _T]:
    """Decorator which changes the current working dir to the one of the git
    repository in order to assure relative paths are handled correctly"""
