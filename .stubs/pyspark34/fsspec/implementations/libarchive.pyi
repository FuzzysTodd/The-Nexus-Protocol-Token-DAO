from _typeshed import Incomplete
from collections.abc import Generator
from fsspec import open_files as open_files
from fsspec.archive import AbstractArchiveFileSystem as AbstractArchiveFileSystem
from fsspec.implementations.memory import MemoryFile as MemoryFile
from fsspec.utils import DEFAULT_BLOCK_SIZE as DEFAULT_BLOCK_SIZE

SEEK_CALLBACK: Incomplete
read_set_seek_callback: Incomplete
new_api: Incomplete

def custom_reader(file, format_name: str = 'all', filter_name: str = 'all', block_size=...) -> Generator[Incomplete, None, Incomplete]:
    """Read an archive from a seekable file-like object.

    The `file` object must support the standard `readinto` and 'seek' methods.
    """

class LibArchiveFileSystem(AbstractArchiveFileSystem):
    """Compressed archives as a file-system (read-only)

    Supports the following formats:
    tar, pax , cpio, ISO9660, zip, mtree, shar, ar, raw, xar, lha/lzh, rar
    Microsoft CAB, 7-Zip, WARC

    See the libarchive documentation for further restrictions.
    https://www.libarchive.org/

    Keeps file object open while instance lives. It only works in seekable
    file-like objects. In case the filesystem does not support this kind of
    file object, it is recommended to cache locally.

    This class is pickleable, but not necessarily thread-safe (depends on the
    platform). See libarchive documentation for details.
    """
    root_marker: str
    protocol: str
    cachable: bool
    of: Incomplete
    fo: Incomplete
    block_size: Incomplete
    dir_cache: Incomplete
    def __init__(self, fo: str = '', mode: str = 'r', target_protocol: Incomplete | None = None, target_options: Incomplete | None = None, block_size=..., **kwargs) -> None:
        """
        Parameters
        ----------
        fo: str or file-like
            Contains ZIP, and must exist. If a str, will fetch file using
            :meth:`~fsspec.open_files`, which must return one file exactly.
        mode: str
            Currently, only 'r' accepted
        target_protocol: str (optional)
            If ``fo`` is a string, this value can be used to override the
            FS protocol inferred from a URL
        target_options: dict (optional)
            Kwargs passed when instantiating the target FS, if ``fo`` is
            a string.
        """
