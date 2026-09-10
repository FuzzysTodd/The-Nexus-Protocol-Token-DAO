from _typeshed import Incomplete
from collections.abc import MutableMapping
from fontTools.misc import sstruct as sstruct
from fontTools.misc.textTools import bytesjoin as bytesjoin, tostr as tostr

class ResourceError(Exception): ...

class ResourceReader(MutableMapping):
    """Reader for Mac OS resource forks.

    Parses a resource fork and returns resources according to their type.
    If run on OS X, this will open the resource fork in the filesystem.
    Otherwise, it will open the file itself and attempt to read it as
    though it were a resource fork.

    The returned object can be indexed by type and iterated over,
    returning in each case a list of py:class:`Resource` objects
    representing all the resources of a certain type.

    """
    file: Incomplete
    def __init__(self, fileOrPath) -> None:
        """Open a file

        Args:
                fileOrPath: Either an object supporting a ``read`` method, an
                        ``os.PathLike`` object, or a string.
        """
    @staticmethod
    def openResourceFork(path): ...
    @staticmethod
    def openDataFork(path): ...
    def __getitem__(self, resType): ...
    def __delitem__(self, resType) -> None: ...
    def __setitem__(self, resType, resources) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def keys(self): ...
    @property
    def types(self):
        """A list of the types of resources in the resource fork."""
    def countResources(self, resType):
        """Return the number of resources of a given type."""
    def getIndices(self, resType):
        """Returns a list of indices of resources of a given type."""
    def getNames(self, resType):
        """Return list of names of all resources of a given type."""
    def getIndResource(self, resType, index):
        """Return resource of given type located at an index ranging from 1
        to the number of resources for that type, or None if not found.
        """
    def getNamedResource(self, resType, name):
        """Return the named resource of given type, else return None."""
    def close(self) -> None: ...

class Resource:
    """Represents a resource stored within a resource fork.

    Attributes:
            type: resource type.
            data: resource data.
            id: ID.
            name: resource name.
            attr: attributes.
    """
    type: Incomplete
    data: Incomplete
    id: Incomplete
    name: Incomplete
    attr: Incomplete
    def __init__(self, resType: Incomplete | None = None, resData: Incomplete | None = None, resID: Incomplete | None = None, resName: Incomplete | None = None, resAttr: Incomplete | None = None) -> None: ...
    def decompile(self, refData, reader) -> None: ...

ResourceForkHeader: str
ResourceForkHeaderSize: Incomplete
ResourceMapHeader: str
ResourceMapHeaderSize: Incomplete
ResourceTypeItem: str
ResourceTypeItemSize: Incomplete
ResourceRefItem: str
ResourceRefItemSize: Incomplete
