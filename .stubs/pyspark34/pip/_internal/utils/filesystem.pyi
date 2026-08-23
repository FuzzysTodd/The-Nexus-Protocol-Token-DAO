from _typeshed import Incomplete
from pip._internal.utils.compat import get_path_uid as get_path_uid
from pip._internal.utils.misc import format_size as format_size
from pip._vendor.tenacity import retry as retry, stop_after_delay as stop_after_delay, wait_fixed as wait_fixed
from typing import Any, BinaryIO, Generator, List

def check_path_owner(path: str) -> bool: ...
def adjacent_tmp_file(path: str, **kwargs: Any) -> Generator[BinaryIO, None, None]:
    """Return a file-like object pointing to a tmp file next to path.

    The file is created securely and is ensured to be written to disk
    after the context reaches its end.

    kwargs will be passed to tempfile.NamedTemporaryFile to control
    the way the temporary file will be opened.
    """

replace: Incomplete

def test_writable_dir(path: str) -> bool:
    """Check if a directory is writable.

    Uses os.access() on POSIX, tries creating files on Windows.
    """
def find_files(path: str, pattern: str) -> List[str]:
    """Returns a list of absolute paths of files beneath path, recursively,
    with filenames which match the UNIX-style shell glob pattern."""
def file_size(path: str) -> int | float: ...
def format_file_size(path: str) -> str: ...
def directory_size(path: str) -> int | float: ...
def format_directory_size(path: str) -> str: ...
