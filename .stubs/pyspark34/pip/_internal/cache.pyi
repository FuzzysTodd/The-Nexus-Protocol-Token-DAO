from _typeshed import Incomplete
from pip._internal.exceptions import InvalidWheelFilename as InvalidWheelFilename
from pip._internal.models.direct_url import DirectUrl as DirectUrl
from pip._internal.models.link import Link as Link
from pip._internal.models.wheel import Wheel as Wheel
from pip._internal.utils.temp_dir import TempDirectory as TempDirectory, tempdir_kinds as tempdir_kinds
from pip._internal.utils.urls import path_to_url as path_to_url
from pip._vendor.packaging.tags import Tag as Tag, interpreter_name as interpreter_name, interpreter_version as interpreter_version
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name
from typing import List

logger: Incomplete
ORIGIN_JSON_NAME: str

class Cache:
    """An abstract class - provides cache directories for data from links

    :param cache_dir: The root of the cache.
    """
    cache_dir: Incomplete
    def __init__(self, cache_dir: str) -> None: ...
    def get_path_for_link(self, link: Link) -> str:
        """Return a directory to store cached items in for link."""
    def get(self, link: Link, package_name: str | None, supported_tags: List[Tag]) -> Link:
        """Returns a link to a cached item if it exists, otherwise returns the
        passed link.
        """

class SimpleWheelCache(Cache):
    """A cache of wheels for future installs."""
    def __init__(self, cache_dir: str) -> None: ...
    def get_path_for_link(self, link: Link) -> str:
        """Return a directory to store cached wheels for link

        Because there are M wheels for any one sdist, we provide a directory
        to cache them in, and then consult that directory when looking up
        cache hits.

        We only insert things into the cache if they have plausible version
        numbers, so that we don't contaminate the cache with things that were
        not unique. E.g. ./package might have dozens of installs done for it
        and build a version of 0.0...and if we built and cached a wheel, we'd
        end up using the same wheel even if the source has been edited.

        :param link: The link of the sdist for which this will cache wheels.
        """
    def get(self, link: Link, package_name: str | None, supported_tags: List[Tag]) -> Link: ...

class EphemWheelCache(SimpleWheelCache):
    """A SimpleWheelCache that creates it's own temporary cache directory"""
    def __init__(self) -> None: ...

class CacheEntry:
    link: Incomplete
    persistent: Incomplete
    origin: Incomplete
    def __init__(self, link: Link, persistent: bool) -> None: ...

class WheelCache(Cache):
    """Wraps EphemWheelCache and SimpleWheelCache into a single Cache

    This Cache allows for gracefully degradation, using the ephem wheel cache
    when a certain link is not found in the simple wheel cache first.
    """
    def __init__(self, cache_dir: str) -> None: ...
    def get_path_for_link(self, link: Link) -> str: ...
    def get_ephem_path_for_link(self, link: Link) -> str: ...
    def get(self, link: Link, package_name: str | None, supported_tags: List[Tag]) -> Link: ...
    def get_cache_entry(self, link: Link, package_name: str | None, supported_tags: List[Tag]) -> CacheEntry | None:
        """Returns a CacheEntry with a link to a cached item if it exists or
        None. The cache entry indicates if the item was found in the persistent
        or ephemeral cache.
        """
    @staticmethod
    def record_download_origin(cache_dir: str, download_info: DirectUrl) -> None: ...
