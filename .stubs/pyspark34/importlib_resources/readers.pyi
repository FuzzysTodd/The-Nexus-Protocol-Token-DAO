from . import abc as abc
from ._compat import ZipPath as ZipPath, ensure_traversable as ensure_traversable
from ._itertools import only as only
from _typeshed import Incomplete

def remove_duplicates(items): ...

class FileReader(abc.TraversableResources):
    path: Incomplete
    def __init__(self, loader) -> None: ...
    def resource_path(self, resource):
        """
        Return the file system path to prevent
        `resources.path()` from creating a temporary
        copy.
        """
    def files(self): ...

class ZipReader(abc.TraversableResources):
    prefix: Incomplete
    archive: Incomplete
    def __init__(self, loader, module) -> None: ...
    def open_resource(self, resource): ...
    def is_resource(self, path):
        """
        Workaround for `zipfile.Path.is_file` returning true
        for non-existent paths.
        """
    def files(self): ...

class MultiplexedPath(abc.Traversable):
    """
    Given a series of Traversable objects, implement a merged
    version of the interface across all objects. Useful for
    namespace packages which may be multihomed at a single
    name.
    """
    def __init__(self, *paths) -> None: ...
    def iterdir(self): ...
    def read_bytes(self) -> None: ...
    def read_text(self, *args, **kwargs) -> None: ...
    def is_dir(self): ...
    def is_file(self): ...
    def joinpath(self, *descendants): ...
    def open(self, *args, **kwargs) -> None: ...
    @property
    def name(self): ...

class NamespaceReader(abc.TraversableResources):
    path: Incomplete
    def __init__(self, namespace_path) -> None: ...
    def resource_path(self, resource):
        """
        Return the file system path to prevent
        `resources.path()` from creating a temporary
        copy.
        """
    def files(self): ...
