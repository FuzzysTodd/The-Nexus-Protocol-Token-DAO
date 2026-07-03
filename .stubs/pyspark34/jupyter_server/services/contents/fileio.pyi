from _typeshed import Incomplete
from collections.abc import Generator
from jupyter_server.utils import ApiPath as ApiPath, to_api_path as to_api_path, to_os_path as to_os_path
from traitlets.config import Configurable

def replace_file(src, dst) -> None:
    """replace dst with src"""
async def async_replace_file(src, dst) -> None:
    """replace dst with src asynchronously"""
def copy2_safe(src, dst, log: Incomplete | None = None) -> None:
    """copy src to dst

    like shutil.copy2, but log errors in copystat instead of raising
    """
async def async_copy2_safe(src, dst, log: Incomplete | None = None) -> None:
    """copy src to dst asynchronously

    like shutil.copy2, but log errors in copystat instead of raising
    """
def path_to_intermediate(path):
    """Name of the intermediate file used in atomic writes.

    The .~ prefix will make Dropbox ignore the temporary file."""
def path_to_invalid(path):
    """Name of invalid file after a failed atomic write and subsequent read."""
def atomic_writing(path, text: bool = True, encoding: str = 'utf-8', log: Incomplete | None = None, **kwargs) -> Generator[Incomplete, None, None]:
    """Context manager to write to a file only if the entire write is successful.

    This works by copying the previous file contents to a temporary file in the
    same directory, and renaming that file back to the target if the context
    exits with an error. If the context is successful, the new data is synced to
    disk and the temporary file is removed.

    Parameters
    ----------
    path : str
        The target file to write to.
    text : bool, optional
        Whether to open the file in text mode (i.e. to write unicode). Default is
        True.
    encoding : str, optional
        The encoding to use for files opened in text mode. Default is UTF-8.
    **kwargs
        Passed to :func:`io.open`.
    """

class FileManagerMixin(Configurable):
    """
    Mixin for ContentsAPI classes that interact with the filesystem.

    Provides facilities for reading, writing, and copying files.

    Shared by FileContentsManager and FileCheckpoints.

    Note
    ----
    Classes using this mixin must provide the following attributes:

    root_dir : unicode
        A directory against against which API-style paths are to be resolved.

    log : logging.Logger
    """
    use_atomic_writing: Incomplete
    def open(self, os_path, *args, **kwargs) -> Generator[Incomplete, None, None]:
        """wrapper around io.open that turns permission errors into 403"""
    def atomic_writing(self, os_path, *args, **kwargs) -> Generator[Incomplete, None, None]:
        """wrapper around atomic_writing that turns permission errors to 403.
        Depending on flag 'use_atomic_writing', the wrapper perform an actual atomic writing or
        simply writes the file (whatever an old exists or not)"""
    def perm_to_403(self, os_path: str = '') -> Generator[None, None, None]:
        """context manager for turning permission errors into 403."""

class AsyncFileManagerMixin(FileManagerMixin):
    """
    Mixin for ContentsAPI classes that interact with the filesystem asynchronously.
    """
