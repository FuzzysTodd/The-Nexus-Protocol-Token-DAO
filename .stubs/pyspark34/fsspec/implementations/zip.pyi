from _typeshed import Incomplete
from fsspec.archive import AbstractArchiveFileSystem as AbstractArchiveFileSystem

class ZipFileSystem(AbstractArchiveFileSystem):
    """Read/Write contents of ZIP archive as a file-system

    Keeps file object open while instance lives.

    This class is pickleable, but not necessarily thread-safe
    """
    root_marker: str
    protocol: str
    cachable: bool
    mode: Incomplete
    of: Incomplete
    fo: Incomplete
    zip: Incomplete
    dir_cache: Incomplete
    def __init__(self, fo: str = '', mode: str = 'r', target_protocol: Incomplete | None = None, target_options: Incomplete | None = None, compression=..., allowZip64: bool = True, compresslevel: Incomplete | None = None, **kwargs) -> None:
        '''
        Parameters
        ----------
        fo: str or file-like
            Contains ZIP, and must exist. If a str, will fetch file using
            :meth:`~fsspec.open_files`, which must return one file exactly.
        mode: str
            Accept: "r", "w", "a"
        target_protocol: str (optional)
            If ``fo`` is a string, this value can be used to override the
            FS protocol inferred from a URL
        target_options: dict (optional)
            Kwargs passed when instantiating the target FS, if ``fo`` is
            a string.
        compression, allowZip64, compresslevel: passed to ZipFile
            Only relevant when creating a ZIP
        '''
    def __del__(self) -> None: ...
    def close(self) -> None:
        """Commits any write changes to the file. Done on ``del`` too."""
    def pipe_file(self, path, value, **kwargs) -> None: ...
