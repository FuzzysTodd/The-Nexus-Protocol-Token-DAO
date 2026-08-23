from _typeshed import Incomplete
from fsspec import AbstractFileSystem as AbstractFileSystem, filesystem as filesystem
from fsspec.compression import compr as compr
from fsspec.core import BaseCache as BaseCache, MMapCache as MMapCache
from fsspec.exceptions import BlocksizeMismatchError as BlocksizeMismatchError
from fsspec.implementations.cache_mapper import AbstractCacheMapper as AbstractCacheMapper, create_cache_mapper as create_cache_mapper
from fsspec.implementations.cache_metadata import CacheMetadata as CacheMetadata
from fsspec.spec import AbstractBufferedFile as AbstractBufferedFile
from fsspec.utils import infer_compression as infer_compression
from typing import Any, ClassVar

logger: Incomplete

class CachingFileSystem(AbstractFileSystem):
    """Locally caching filesystem, layer over any other FS

    This class implements chunk-wise local storage of remote files, for quick
    access after the initial download. The files are stored in a given
    directory with hashes of URLs for the filenames. If no directory is given,
    a temporary one is used, which should be cleaned up by the OS after the
    process ends. The files themselves are sparse (as implemented in
    :class:`~fsspec.caching.MMapCache`), so only the data which is accessed
    takes up space.

    Restrictions:

    - the block-size must be the same for each access of a given file, unless
      all blocks of the file have already been read
    - caching can only be applied to file-systems which produce files
      derived from fsspec.spec.AbstractBufferedFile ; LocalFileSystem is also
      allowed, for testing
    """
    protocol: ClassVar[str | tuple[str, ...]]
    storage: Incomplete
    kwargs: Incomplete
    cache_check: Incomplete
    check_files: Incomplete
    expiry: Incomplete
    compression: Incomplete
    target_protocol: Incomplete
    fs: Incomplete
    def __init__(self, target_protocol: Incomplete | None = None, cache_storage: str = 'TMP', cache_check: int = 10, check_files: bool = False, expiry_time: int = 604800, target_options: Incomplete | None = None, fs: Incomplete | None = None, same_names: bool | None = None, compression: Incomplete | None = None, cache_mapper: AbstractCacheMapper | None = None, **kwargs) -> None:
        '''

        Parameters
        ----------
        target_protocol: str (optional)
            Target filesystem protocol. Provide either this or ``fs``.
        cache_storage: str or list(str)
            Location to store files. If "TMP", this is a temporary directory,
            and will be cleaned up by the OS when this process ends (or later).
            If a list, each location will be tried in the order given, but
            only the last will be considered writable.
        cache_check: int
            Number of seconds between reload of cache metadata
        check_files: bool
            Whether to explicitly see if the UID of the remote file matches
            the stored one before using. Warning: some file systems such as
            HTTP cannot reliably give a unique hash of the contents of some
            path, so be sure to set this option to False.
        expiry_time: int
            The time in seconds after which a local copy is considered useless.
            Set to falsy to prevent expiry. The default is equivalent to one
            week.
        target_options: dict or None
            Passed to the instantiation of the FS, if fs is None.
        fs: filesystem instance
            The target filesystem to run against. Provide this or ``protocol``.
        same_names: bool (optional)
            By default, target URLs are hashed using a ``HashCacheMapper`` so
            that files from different backends with the same basename do not
            conflict. If this argument is ``true``, a ``BasenameCacheMapper``
            is used instead. Other cache mapper options are available by using
            the ``cache_mapper`` keyword argument. Only one of this and
            ``cache_mapper`` should be specified.
        compression: str (optional)
            To decompress on download. Can be \'infer\' (guess from the URL name),
            one of the entries in ``fsspec.compression.compr``, or None for no
            decompression.
        cache_mapper: AbstractCacheMapper (optional)
            The object use to map from original filenames to cached filenames.
            Only one of this and ``same_names`` should be specified.
        '''
    def cache_size(self):
        """Return size of cache in bytes.

        If more than one cache directory is in use, only the size of the last
        one (the writable cache directory) is returned.
        """
    last_cache: Incomplete
    def load_cache(self) -> None:
        """Read set of stored blocks from file"""
    def save_cache(self) -> None:
        """Save set of stored blocks from file"""
    def clear_cache(self) -> None:
        """Remove all files and metadata from the cache

        In the case of multiple cache locations, this clears only the last one,
        which is assumed to be the read/write one.
        """
    def clear_expired_cache(self, expiry_time: Incomplete | None = None) -> None:
        """Remove all expired files and metadata from the cache

        In the case of multiple cache locations, this clears only the last one,
        which is assumed to be the read/write one.

        Parameters
        ----------
        expiry_time: int
            The time in seconds after which a local copy is considered useless.
            If not defined the default is equivalent to the attribute from the
            file caching instantiation.
        """
    def pop_from_cache(self, path) -> None:
        """Remove cached version of given file

        Deletes local copy of the given (remote) path. If it is found in a cache
        location which is not the last, it is assumed to be read-only, and
        raises PermissionError
        """
    def hash_name(self, path: str, *args: Any) -> str: ...
    def close_and_update(self, f, close) -> None:
        """Called when a file is closing, so store the set of blocks"""
    def __getattribute__(self, item): ...
    def __eq__(self, other):
        """Test for equality."""
    def __hash__(self):
        """Calculate hash."""
    def to_json(self) -> None:
        """Calculate JSON representation.

        Not implemented yet for CachingFileSystem.
        """

class WholeFileCacheFileSystem(CachingFileSystem):
    """Caches whole remote files on first access

    This class is intended as a layer over any other file system, and
    will make a local copy of each file accessed, so that all subsequent
    reads are local. This is similar to ``CachingFileSystem``, but without
    the block-wise functionality and so can work even when sparse files
    are not allowed. See its docstring for definition of the init
    arguments.

    The class still needs access to the remote store for listing files,
    and may refresh cached files.
    """
    protocol: str
    local_file: bool
    def open_many(self, open_files): ...
    def commit_many(self, open_files) -> None: ...
    def cat(self, path, recursive: bool = False, on_error: str = 'raise', callback=..., **kwargs): ...

class SimpleCacheFileSystem(WholeFileCacheFileSystem):
    """Caches whole remote files on first access

    This class is intended as a layer over any other file system, and
    will make a local copy of each file accessed, so that all subsequent
    reads are local. This implementation only copies whole files, and
    does not keep any metadata about the download time or file details.
    It is therefore safer to use in multi-threaded/concurrent situations.

    This is the only of the caching filesystems that supports write: you will
    be given a real local open file, and upon close and commit, it will be
    uploaded to the target filesystem; the writability or the target URL is
    not checked until that time.

    """
    protocol: str
    local_file: bool
    def __init__(self, **kwargs) -> None: ...
    def save_cache(self) -> None: ...
    def load_cache(self) -> None: ...

class LocalTempFile:
    """A temporary local file, which will be uploaded on commit"""
    fn: Incomplete
    fh: Incomplete
    mode: Incomplete
    path: Incomplete
    fs: Incomplete
    closed: bool
    autocommit: Incomplete
    def __init__(self, fs, path, fn: Incomplete | None = None, mode: str = 'wb', autocommit: bool = True, seek: int = 0) -> None: ...
    def __reduce__(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def close(self) -> None: ...
    def discard(self) -> None: ...
    def commit(self) -> None: ...
    @property
    def name(self): ...
    def __getattr__(self, item): ...
