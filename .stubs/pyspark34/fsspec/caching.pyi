from _typeshed import Incomplete
from typing import Any, Callable, ClassVar, Generic, NamedTuple, TypeVar
from typing_extensions import ParamSpec

P = ParamSpec('P')
T = TypeVar('T')
logger: Incomplete
Fetcher = Callable[[int, int], bytes]

class BaseCache:
    """Pass-though cache: doesn't keep anything, calls every time

    Acts as base class for other cachers

    Parameters
    ----------
    blocksize: int
        How far to read ahead in numbers of bytes
    fetcher: func
        Function of the form f(start, end) which gets bytes from remote as
        specified
    size: int
        How big this file is
    """
    name: ClassVar[str]
    blocksize: Incomplete
    fetcher: Incomplete
    size: Incomplete
    def __init__(self, blocksize: int, fetcher: Fetcher, size: int) -> None: ...

class MMapCache(BaseCache):
    """memory-mapped sparse file cache

    Opens temporary file, which is filled blocks-wise when data is requested.
    Ensure there is enough disc space in the temporary location.

    This cache method might only work on posix
    """
    name: str
    blocks: Incomplete
    location: Incomplete
    cache: Incomplete
    def __init__(self, blocksize: int, fetcher: Fetcher, size: int, location: str | None = None, blocks: set[int] | None = None) -> None: ...

class ReadAheadCache(BaseCache):
    """Cache which reads only when we get beyond a block of data

    This is a much simpler version of BytesCache, and does not attempt to
    fill holes in the cache or keep fragments alive. It is best suited to
    many small reads in a sequential order (e.g., reading lines from a file).
    """
    name: str
    cache: bytes
    start: int
    end: int
    def __init__(self, blocksize: int, fetcher: Fetcher, size: int) -> None: ...

class FirstChunkCache(BaseCache):
    """Caches the first block of a file only

    This may be useful for file types where the metadata is stored in the header,
    but is randomly accessed.
    """
    name: str
    cache: Incomplete
    def __init__(self, blocksize: int, fetcher: Fetcher, size: int) -> None: ...

class BlockCache(BaseCache):
    """
    Cache holding memory as a set of blocks.

    Requests are only ever made ``blocksize`` at a time, and are
    stored in an LRU cache. The least recently accessed block is
    discarded when more than ``maxblocks`` are stored.

    Parameters
    ----------
    blocksize : int
        The number of bytes to store in each block.
        Requests are only ever made for ``blocksize``, so this
        should balance the overhead of making a request against
        the granularity of the blocks.
    fetcher : Callable
    size : int
        The total size of the file being cached.
    maxblocks : int
        The maximum number of blocks to cache for. The maximum memory
        use for this cache is then ``blocksize * maxblocks``.
    """
    name: str
    nblocks: Incomplete
    maxblocks: Incomplete
    def __init__(self, blocksize: int, fetcher: Fetcher, size: int, maxblocks: int = 32) -> None: ...
    def cache_info(self):
        """
        The statistics on the block cache.

        Returns
        -------
        NamedTuple
            Returned directly from the LRU Cache used internally.
        """

class BytesCache(BaseCache):
    """Cache which holds data in a in-memory bytes object

    Implements read-ahead by the block size, for semi-random reads progressing
    through the file.

    Parameters
    ----------
    trim: bool
        As we read more data, whether to discard the start of the buffer when
        we are more than a blocksize ahead of it.
    """
    name: ClassVar[str]
    cache: bytes
    start: Incomplete
    end: Incomplete
    trim: Incomplete
    def __init__(self, blocksize: int, fetcher: Fetcher, size: int, trim: bool = True) -> None: ...
    def __len__(self) -> int: ...

class AllBytes(BaseCache):
    """Cache entire contents of the file"""
    name: ClassVar[str]
    data: Incomplete
    def __init__(self, blocksize: int | None = None, fetcher: Fetcher | None = None, size: int | None = None, data: bytes | None = None) -> None: ...

class KnownPartsOfAFile(BaseCache):
    """
    Cache holding known file parts.

    Parameters
    ----------
    blocksize: int
        How far to read ahead in numbers of bytes
    fetcher: func
        Function of the form f(start, end) which gets bytes from remote as
        specified
    size: int
        How big this file is
    data: dict
        A dictionary mapping explicit `(start, stop)` file-offset tuples
        with known bytes.
    strict: bool, default True
        Whether to fetch reads that go beyond a known byte-range boundary.
        If `False`, any read that ends outside a known part will be zero
        padded. Note that zero padding will not be used for reads that
        begin outside a known byte-range.
    """
    name: ClassVar[str]
    strict: Incomplete
    data: Incomplete
    def __init__(self, blocksize: int, fetcher: Fetcher, size: int, data: dict[tuple[int, int], bytes] = {}, strict: bool = True, **_: Any) -> None: ...

class UpdatableLRU(Generic[P, T]):
    """
    Custom implementation of LRU cache that allows updating keys

    Used by BackgroudBlockCache
    """
    class CacheInfo(NamedTuple):
        hits: int
        misses: int
        maxsize: int
        currsize: int
    def __init__(self, func: Callable[P, T], max_size: int = 128) -> None: ...
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T: ...
    def is_key_cached(self, *args: Any) -> bool: ...
    def add_key(self, result: T, *args: Any) -> None: ...
    def cache_info(self) -> UpdatableLRU.CacheInfo: ...

class BackgroundBlockCache(BaseCache):
    """
    Cache holding memory as a set of blocks with pre-loading of
    the next block in the background.

    Requests are only ever made ``blocksize`` at a time, and are
    stored in an LRU cache. The least recently accessed block is
    discarded when more than ``maxblocks`` are stored. If the
    next block is not in cache, it is loaded in a separate thread
    in non-blocking way.

    Parameters
    ----------
    blocksize : int
        The number of bytes to store in each block.
        Requests are only ever made for ``blocksize``, so this
        should balance the overhead of making a request against
        the granularity of the blocks.
    fetcher : Callable
    size : int
        The total size of the file being cached.
    maxblocks : int
        The maximum number of blocks to cache for. The maximum memory
        use for this cache is then ``blocksize * maxblocks``.
    """
    name: ClassVar[str]
    nblocks: Incomplete
    maxblocks: Incomplete
    def __init__(self, blocksize: int, fetcher: Fetcher, size: int, maxblocks: int = 32) -> None: ...
    def cache_info(self) -> UpdatableLRU.CacheInfo:
        """
        The statistics on the block cache.

        Returns
        -------
        NamedTuple
            Returned directly from the LRU Cache used internally.
        """

caches: dict[str | None, type[BaseCache]]

def register_cache(cls, clobber: bool = False) -> None:
    """'Register' cache implementation.

    Parameters
    ----------
    clobber: bool, optional
        If set to True (default is False) - allow to overwrite existing
        entry.

    Raises
    ------
    ValueError
    """
