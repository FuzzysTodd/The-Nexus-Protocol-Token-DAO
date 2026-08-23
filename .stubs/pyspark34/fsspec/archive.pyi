from fsspec import AbstractFileSystem as AbstractFileSystem
from fsspec.utils import tokenize as tokenize

class AbstractArchiveFileSystem(AbstractFileSystem):
    """
    A generic superclass for implementing Archive-based filesystems.

    Currently, it is shared amongst
    :class:`~fsspec.implementations.zip.ZipFileSystem`,
    :class:`~fsspec.implementations.libarchive.LibArchiveFileSystem` and
    :class:`~fsspec.implementations.tar.TarFileSystem`.
    """
    def ukey(self, path): ...
    def info(self, path, **kwargs): ...
    def ls(self, path, detail: bool = True, **kwargs): ...
