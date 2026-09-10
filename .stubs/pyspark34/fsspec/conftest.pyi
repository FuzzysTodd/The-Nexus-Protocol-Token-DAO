from _typeshed import Incomplete
from collections.abc import Generator
from fsspec.implementations.cached import CachingFileSystem as CachingFileSystem

def m() -> Generator[Incomplete, None, None]:
    """
    Fixture providing a memory filesystem.
    """
def ftp_writable(tmpdir) -> Generator[Incomplete, None, None]:
    """
    Fixture providing a writable FTP filesystem.
    """
