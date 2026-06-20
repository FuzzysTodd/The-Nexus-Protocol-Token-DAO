from _typeshed import Incomplete
from collections.abc import Generator
from concurrent.futures import Executor

on_win: Incomplete
log: Incomplete
CONDA_TEMP_EXTENSION: str

def which(executable): ...
def make_writable(path): ...

class DummyExecutor(Executor):
    def map(self, func, *iterables) -> Generator[Incomplete, None, None]: ...

def get_executor(processes): ...
def recursive_make_writable(path) -> None: ...
def quote_for_shell(arguments, shell: Incomplete | None = None): ...
def rmtree(path, *args, **kwargs) -> None: ...
def unlink_or_rename_to_trash(path) -> None:
    """If files are in use, especially on windows, we can't remove them.
    The fallback path is to rename them (but keep their folder the same),
    which maintains the file handle validity.  See comments at:
    https://serverfault.com/a/503769
    """
def remove_empty_parent_paths(path) -> None: ...
def rm_rf(path, clean_empty_parents: bool = False, *args, **kw):
    """
    Completely delete path
    max_retries is the number of times to retry on failure. The default is 5. This only applies
    to deleting a directory.
    If removing path fails and trash is True, files will be moved to the trash directory.
    """
try_rmdir_all_empty = rm_rf
move_to_trash = rm_rf
move_path_to_trash = rm_rf

def delete_trash(prefix) -> None: ...
def rmdir(dirpath) -> None: ...

class TemporaryDirectory:
    """Create and return a temporary directory.  This has the same
    behavior as mkdtemp but can be used as a context manager.  For
    example:

        with TemporaryDirectory() as tmpdir:
            ...

    Upon exiting the context, the directory and everything contained
    in it are removed.
    """
    name: Incomplete
    def __init__(self, suffix: str = '', prefix: str = '.cph_tmp', dir=...) -> None: ...
    def __enter__(self): ...
    def cleanup(self, _warn: bool = False, _warnings=...) -> None: ...
    def __exit__(self, exc: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None: ...
    def __del__(self) -> None: ...

def tmp_chdir(dest) -> Generator[None, None, None]: ...
def ensure_list(arg): ...
def filter_files(files_list, prefix, filter_patterns=('(.*[\\\\\\\\/])?\\.git[\\\\\\\\/].*', '(.*[\\\\\\\\/])?\\.git$', '(.*)?\\.DS_Store.*', '.*\\.la$', 'conda-meta.*')):
    """Remove things like the .git directory from the list of files to be copied"""
def filter_info_files(files_list, prefix): ...
def sha256_checksum(fd): ...
def md5_checksum(fd): ...
def checksum(fn, algorithm, buffersize=...):
    """
    Calculate a checksum for a filename (not an open file).
    """
def checksums(fn, algorithms, buffersize=...):
    """
    Calculate multiple checksums for a filename in parallel.
    """
def anonymize_tarinfo(tarinfo):
    """
    Remove user id, name from tarinfo.
    """
