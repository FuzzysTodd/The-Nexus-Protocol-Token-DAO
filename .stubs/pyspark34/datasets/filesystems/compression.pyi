from _typeshed import Incomplete
from fsspec.archive import AbstractArchiveFileSystem

class BaseCompressedFileFileSystem(AbstractArchiveFileSystem):
    """Read contents of compressed file as a filesystem with one file inside."""
    root_marker: str
    protocol: str
    compression: str
    extension: str
    file: Incomplete
    compressed_name: Incomplete
    uncompressed_name: Incomplete
    dir_cache: Incomplete
    def __init__(self, fo: str = '', target_protocol: str | None = None, target_options: dict | None = None, **kwargs) -> None:
        """
        The compressed file system can be instantiated from any compressed file.
        It reads the contents of compressed file as a filesystem with one file inside, as if it was an archive.

        The single file inside the filesystem is named after the compresssed file,
        without the compression extension at the end of the filename.

        Args:
            fo (:obj:``str``): Path to compressed file. Will fetch file using ``fsspec.open()``
            mode (:obj:``str``): Currently, only 'rb' accepted
            target_protocol(:obj:``str``, optional): To override the FS protocol inferred from a URL.
            target_options (:obj:``dict``, optional): Kwargs passed when instantiating the target FS.
        """
    def cat(self, path: str): ...

class Bz2FileSystem(BaseCompressedFileFileSystem):
    """Read contents of BZ2 file as a filesystem with one file inside."""
    protocol: str
    compression: str
    extension: str

class GzipFileSystem(BaseCompressedFileFileSystem):
    """Read contents of GZIP file as a filesystem with one file inside."""
    protocol: str
    compression: str
    extension: str

class Lz4FileSystem(BaseCompressedFileFileSystem):
    """Read contents of LZ4 file as a filesystem with one file inside."""
    protocol: str
    compression: str
    extension: str

class XzFileSystem(BaseCompressedFileFileSystem):
    """Read contents of .xz (LZMA) file as a filesystem with one file inside."""
    protocol: str
    compression: str
    extension: str

class ZstdFileSystem(BaseCompressedFileFileSystem):
    """
    Read contents of zstd file as a filesystem with one file inside.

    Note that reading in binary mode with fsspec isn't supported yet:
    https://github.com/indygreg/python-zstandard/issues/136
    """
    protocol: str
    compression: str
    extension: str
    def __init__(self, fo: str, mode: str = 'rb', target_protocol: str | None = None, target_options: dict | None = None, block_size: int = ..., **kwargs) -> None: ...
