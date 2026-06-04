from . import DistlibException as DistlibException
from .util import Cache as Cache, cached_property as cached_property, get_cache_base as get_cache_base
from _typeshed import Incomplete
from collections.abc import Generator

logger: Incomplete
cache: Incomplete

class ResourceCache(Cache):
    def __init__(self, base: Incomplete | None = None) -> None: ...
    def is_stale(self, resource, path):
        """
        Is the cache stale for the given resource?

        :param resource: The :class:`Resource` being cached.
        :param path: The path of the resource in the cache.
        :return: True if the cache is stale.
        """
    def get(self, resource):
        """
        Get a resource into the cache,

        :param resource: A :class:`Resource` instance.
        :return: The pathname of the resource in the cache.
        """

class ResourceBase:
    finder: Incomplete
    name: Incomplete
    def __init__(self, finder, name) -> None: ...

class Resource(ResourceBase):
    """
    A class representing an in-package resource, such as a data file. This is
    not normally instantiated by user code, but rather by a
    :class:`ResourceFinder` which manages the resource.
    """
    is_container: bool
    def as_stream(self):
        """
        Get the resource as a stream.

        This is not a property to make it obvious that it returns a new stream
        each time.
        """
    def file_path(self): ...
    def bytes(self): ...
    def size(self): ...

class ResourceContainer(ResourceBase):
    is_container: bool
    def resources(self): ...

class ResourceFinder:
    """
    Resource finder for file system resources.
    """
    skipped_extensions: Incomplete
    module: Incomplete
    loader: Incomplete
    base: Incomplete
    def __init__(self, module) -> None: ...
    def get_cache_info(self, resource): ...
    def find(self, resource_name): ...
    def get_stream(self, resource): ...
    def get_bytes(self, resource): ...
    def get_size(self, resource): ...
    def get_resources(self, resource): ...
    def is_container(self, resource): ...
    def iterator(self, resource_name) -> Generator[Incomplete, None, None]: ...

class ZipResourceFinder(ResourceFinder):
    """
    Resource finder for resources in .zip files.
    """
    prefix_len: Incomplete
    index: Incomplete
    def __init__(self, module) -> None: ...
    def get_cache_info(self, resource): ...
    def get_bytes(self, resource): ...
    def get_stream(self, resource): ...
    def get_size(self, resource): ...
    def get_resources(self, resource): ...

def register_finder(loader, finder_maker) -> None: ...
def finder(package):
    """
    Return a resource finder for a package.
    :param package: The name of the package.
    :return: A :class:`ResourceFinder` instance for the package.
    """
def finder_for_path(path):
    """
    Return a resource finder for a path, which should represent a container.

    :param path: The path.
    :return: A :class:`ResourceFinder` instance for the path.
    """
