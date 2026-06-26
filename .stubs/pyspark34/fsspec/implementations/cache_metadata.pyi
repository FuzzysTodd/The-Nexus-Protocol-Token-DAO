from .cached import CachingFileSystem as CachingFileSystem
from _typeshed import Incomplete
from fsspec.utils import atomic_write as atomic_write
from typing import Any, Literal
from typing_extensions import TypeAlias

Detail: TypeAlias

class CacheMetadata:
    """Cache metadata.

    All reading and writing of cache metadata is performed by this class,
    accessing the cached files and blocks is not.

    Metadata is stored in a single file per storage directory in JSON format.
    For backward compatibility, also reads metadata stored in pickle format
    which is converted to JSON when next saved.
    """
    cached_files: Incomplete
    def __init__(self, storage: list[str]) -> None:
        """

        Parameters
        ----------
        storage: list[str]
            Directories containing cached files, must be at least one. Metadata
            is stored in the last of these directories by convention.
        """
    def check_file(self, path: str, cfs: CachingFileSystem | None) -> Literal[False] | tuple[Detail, str]:
        """If path is in cache return its details, otherwise return ``False``.

        If the optional CachingFileSystem is specified then it is used to
        perform extra checks to reject possible matches, such as if they are
        too old.
        """
    def clear_expired(self, expiry_time: int) -> tuple[list[str], bool]:
        """Remove expired metadata from the cache.

        Returns names of files corresponding to expired metadata and a boolean
        flag indicating whether the writable cache is empty. Caller is
        responsible for deleting the expired files.
        """
    def load(self) -> None:
        """Load all metadata from disk and store in ``self.cached_files``"""
    def on_close_cached_file(self, f: Any, path: str) -> None:
        """Perform side-effect actions on closing a cached file.

        The actual closing of the file is the responsibility of the caller.
        """
    def pop_file(self, path: str) -> str | None:
        """Remove metadata of cached file.

        If path is in the cache, return the filename of the cached file,
        otherwise return ``None``.  Caller is responsible for deleting the
        cached file.
        """
    def save(self) -> None:
        """Save metadata to disk"""
    def update_file(self, path: str, detail: Detail) -> None:
        """Update metadata for specific file in memory, do not save"""
