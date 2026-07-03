from _typeshed import Incomplete
from datetime import datetime
from pip._internal.utils.filesystem import adjacent_tmp_file as adjacent_tmp_file, replace as replace
from pip._internal.utils.misc import ensure_dir as ensure_dir
from pip._vendor.cachecontrol.cache import SeparateBodyBaseCache as SeparateBodyBaseCache
from pip._vendor.cachecontrol.caches import SeparateBodyFileCache as SeparateBodyFileCache
from pip._vendor.requests.models import Response as Response
from typing import BinaryIO, Generator

def is_from_cache(response: Response) -> bool: ...
def suppressed_cache_errors() -> Generator[None, None, None]:
    """If we can't access the cache then we can just skip caching and process
    requests as if caching wasn't enabled.
    """

class SafeFileCache(SeparateBodyBaseCache):
    """
    A file based cache which is safe to use even when the target directory may
    not be accessible or writable.

    There is a race condition when two processes try to write and/or read the
    same entry at the same time, since each entry consists of two separate
    files (https://github.com/psf/cachecontrol/issues/324).  We therefore have
    additional logic that makes sure that both files to be present before
    returning an entry; this fixes the read side of the race condition.

    For the write side, we assume that the server will only ever return the
    same data for the same URL, which ought to be the case for files pip is
    downloading.  PyPI does not have a mechanism to swap out a wheel for
    another wheel, for example.  If this assumption is not true, the
    CacheControl issue will need to be fixed.
    """
    directory: Incomplete
    def __init__(self, directory: str) -> None: ...
    def get(self, key: str) -> bytes | None: ...
    def set(self, key: str, value: bytes, expires: int | datetime | None = None) -> None: ...
    def delete(self, key: str) -> None: ...
    def get_body(self, key: str) -> BinaryIO | None: ...
    def set_body(self, key: str, body: bytes) -> None: ...
