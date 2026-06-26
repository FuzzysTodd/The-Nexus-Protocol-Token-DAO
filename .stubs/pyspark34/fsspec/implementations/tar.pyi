from _typeshed import Incomplete
from fsspec.archive import AbstractArchiveFileSystem as AbstractArchiveFileSystem
from fsspec.compression import compr as compr
from fsspec.utils import infer_compression as infer_compression

typemap: Incomplete
logger: Incomplete

class TarFileSystem(AbstractArchiveFileSystem):
    """Compressed Tar archives as a file-system (read-only)

    Supports the following formats:
    tar.gz, tar.bz2, tar.xz
    """
    root_marker: str
    protocol: str
    cachable: bool
    of: Incomplete
    fo: Incomplete
    tar: Incomplete
    dir_cache: Incomplete
    index_store: Incomplete
    index: Incomplete
    def __init__(self, fo: str = '', index_store: Incomplete | None = None, target_options: Incomplete | None = None, target_protocol: Incomplete | None = None, compression: Incomplete | None = None, **kwargs) -> None: ...
