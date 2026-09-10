import abc
from .abc import Traversable as Traversable, TraversableResources as TraversableResources
from _typeshed import Incomplete
from typing import BinaryIO, List

class SimpleReader(abc.ABC, metaclass=abc.ABCMeta):
    """
    The minimum, low-level interface required from a resource
    provider.
    """
    @property
    @abc.abstractmethod
    def package(self) -> str:
        """
        The name of the package for which this reader loads resources.
        """
    @abc.abstractmethod
    def children(self) -> List['SimpleReader']:
        """
        Obtain an iterable of SimpleReader for available
        child containers (e.g. directories).
        """
    @abc.abstractmethod
    def resources(self) -> List[str]:
        """
        Obtain available named resources for this virtual package.
        """
    @abc.abstractmethod
    def open_binary(self, resource: str) -> BinaryIO:
        """
        Obtain a File-like for a named resource.
        """
    @property
    def name(self): ...

class ResourceContainer(Traversable, metaclass=abc.ABCMeta):
    """
    Traversable container for a package's resources via its reader.
    """
    reader: Incomplete
    def __init__(self, reader: SimpleReader) -> None: ...
    def is_dir(self): ...
    def is_file(self): ...
    def iterdir(self): ...
    def open(self, *args, **kwargs) -> None: ...

class ResourceHandle(Traversable, metaclass=abc.ABCMeta):
    """
    Handle to a named resource in a ResourceReader.
    """
    parent: Incomplete
    name: Incomplete
    def __init__(self, parent: ResourceContainer, name: str) -> None: ...
    def is_file(self): ...
    def is_dir(self): ...
    def open(self, mode: str = 'r', *args, **kwargs): ...
    def joinpath(self, name) -> None: ...

class TraversableReader(TraversableResources, SimpleReader, metaclass=abc.ABCMeta):
    """
    A TraversableResources based on SimpleReader. Resource providers
    may derive from this class to provide the TraversableResources
    interface by supplying the SimpleReader interface.
    """
    def files(self): ...
