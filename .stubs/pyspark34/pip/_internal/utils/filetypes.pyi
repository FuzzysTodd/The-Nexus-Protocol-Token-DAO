from _typeshed import Incomplete
from pip._internal.utils.misc import splitext as splitext
from typing import Tuple

WHEEL_EXTENSION: str
BZ2_EXTENSIONS: Tuple[str, ...]
XZ_EXTENSIONS: Tuple[str, ...]
ZIP_EXTENSIONS: Tuple[str, ...]
TAR_EXTENSIONS: Tuple[str, ...]
ARCHIVE_EXTENSIONS: Incomplete

def is_archive_file(name: str) -> bool:
    """Return True if `name` is a considered as an archive file."""
