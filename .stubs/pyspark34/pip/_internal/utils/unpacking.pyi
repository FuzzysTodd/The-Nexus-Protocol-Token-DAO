from _typeshed import Incomplete
from pip._internal.exceptions import InstallationError as InstallationError
from pip._internal.utils.filetypes import BZ2_EXTENSIONS as BZ2_EXTENSIONS, TAR_EXTENSIONS as TAR_EXTENSIONS, XZ_EXTENSIONS as XZ_EXTENSIONS, ZIP_EXTENSIONS as ZIP_EXTENSIONS
from pip._internal.utils.misc import ensure_dir as ensure_dir
from typing import Iterable, List
from zipfile import ZipInfo

logger: Incomplete
SUPPORTED_EXTENSIONS: Incomplete

def current_umask() -> int:
    """Get the current umask which involves having to set it temporarily."""
def split_leading_dir(path: str) -> List[str]: ...
def has_leading_dir(paths: Iterable[str]) -> bool:
    """Returns true if all the paths have the same leading path name
    (i.e., everything is in one subdirectory in an archive)"""
def is_within_directory(directory: str, target: str) -> bool:
    """
    Return true if the absolute path of target is within the directory
    """
def set_extracted_file_to_default_mode_plus_executable(path: str) -> None:
    """
    Make file present at path have execute for user/group/world
    (chmod +x) is no-op on windows per python docs
    """
def zip_item_is_executable(info: ZipInfo) -> bool: ...
def unzip_file(filename: str, location: str, flatten: bool = True) -> None:
    '''
    Unzip the file (with path `filename`) to the destination `location`.  All
    files are written based on system defaults and umask (i.e. permissions are
    not preserved), except that regular file members with any execute
    permissions (user, group, or world) have "chmod +x" applied after being
    written. Note that for windows, any execute changes using os.chmod are
    no-ops per the python docs.
    '''
def untar_file(filename: str, location: str) -> None:
    '''
    Untar the file (with path `filename`) to the destination `location`.
    All files are written based on system defaults and umask (i.e. permissions
    are not preserved), except that regular file members with any execute
    permissions (user, group, or world) have "chmod +x" applied after being
    written.  Note that for windows, any execute changes using os.chmod are
    no-ops per the python docs.
    '''
def unpack_file(filename: str, location: str, content_type: str | None = None) -> None: ...
