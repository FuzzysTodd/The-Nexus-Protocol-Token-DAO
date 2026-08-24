from _typeshed import Incomplete
from ctypes import Structure
from send2trash.compat import text_type as text_type
from send2trash.util import preprocess_paths as preprocess_paths

kernel32: Incomplete
GetShortPathNameW: Incomplete
shell32: Incomplete
SHFileOperationW: Incomplete

class SHFILEOPSTRUCTW(Structure): ...

FO_MOVE: int
FO_COPY: int
FO_DELETE: int
FO_RENAME: int
FOF_MULTIDESTFILES: int
FOF_SILENT: int
FOF_NOCONFIRMATION: int
FOF_ALLOWUNDO: int
FOF_NOERRORUI: int

def convert_sh_file_opt_result(result): ...
def prefix_and_path(path):
    """Guess the long-path prefix based on the kind of *path*.
    Local paths (C:\\folder\\file.ext) and UNC names (\\\\server\\folder\\file.ext)
    are handled.

    Return a tuple of the long-path prefix and the prefixed path.
    """
def get_awaited_path_from_prefix(prefix, path):
    """Guess the correct path to pass to the SHFileOperationW() call.
    The long-path prefix must be removed, so we should take care of
    different long-path prefixes.
    """
def get_short_path_name(long_name): ...
def send2trash(paths) -> None: ...
