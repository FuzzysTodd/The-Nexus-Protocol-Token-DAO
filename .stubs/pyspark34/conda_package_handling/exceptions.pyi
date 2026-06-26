from _typeshed import Incomplete

class InvalidArchiveError(Exception):
    """Raised when libarchive can't open a file"""
    errno: Incomplete
    def __init__(self, fn, msg, *args, **kw) -> None: ...

class ArchiveCreationError(Exception):
    """Raised when an archive fails during creation"""

class CaseInsensitiveFileSystemError(InvalidArchiveError):
    package_location: Incomplete
    extract_location: Incomplete
    def __init__(self, package_location, extract_location, **kwargs) -> None: ...

class ConversionError(Exception):
    missing_files: Incomplete
    mismatching_sizes: Incomplete
    def __init__(self, missing_files, mismatching_sizes, *args, **kw) -> None: ...
