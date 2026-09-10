from _typeshed import Incomplete
from mypy.fscache import FileSystemCache as FileSystemCache
from typing import AbstractSet, Iterable, NamedTuple

class FileData(NamedTuple):
    st_mtime: float
    st_size: int
    hash: str

class FileSystemWatcher:
    """Watcher for file system changes among specific paths.

    All file system access is performed using FileSystemCache. We
    detect changed files by stat()ing them all and comparing hashes
    of potentially changed files. If a file has both size and mtime
    unmodified, the file is assumed to be unchanged.

    An important goal of this class is to make it easier to eventually
    use file system events to detect file changes.

    Note: This class doesn't flush the file system cache. If you don't
    manually flush it, changes won't be seen.
    """
    fs: Incomplete
    def __init__(self, fs: FileSystemCache) -> None: ...
    def dump_file_data(self) -> dict[str, tuple[float, int, str]]: ...
    def set_file_data(self, path: str, data: FileData) -> None: ...
    def add_watched_paths(self, paths: Iterable[str]) -> None: ...
    def remove_watched_paths(self, paths: Iterable[str]) -> None: ...
    def find_changed(self) -> AbstractSet[str]:
        """Return paths that have changes since the last call, in the watched set."""
    def update_changed(self, remove: list[str], update: list[str]) -> AbstractSet[str]:
        """Alternative to find_changed() given explicit changes.

        This only calls self.fs.stat() on added or updated files, not
        on all files.  It believes all other files are unchanged!

        Implies add_watched_paths() for add and update, and
        remove_watched_paths() for remove.
        """
