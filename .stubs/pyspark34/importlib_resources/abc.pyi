import abc
import io
from ._compat import Protocol, StrPath
from typing import Any, BinaryIO, Iterable, Iterator, NoReturn, Text

__all__ = ['ResourceReader', 'Traversable', 'TraversableResources']

class ResourceReader(metaclass=abc.ABCMeta):
    """Abstract base class for loaders to provide resource reading support."""
    @abc.abstractmethod
    def open_resource(self, resource: Text) -> BinaryIO:
        """Return an opened, file-like object for binary reading.

        The 'resource' argument is expected to represent only a file name.
        If the resource cannot be found, FileNotFoundError is raised.
        """
    @abc.abstractmethod
    def resource_path(self, resource: Text) -> Text:
        """Return the file system path to the specified resource.

        The 'resource' argument is expected to represent only a file name.
        If the resource does not exist on the file system, raise
        FileNotFoundError.
        """
    @abc.abstractmethod
    def is_resource(self, path: Text) -> bool:
        """Return True if the named 'path' is a resource.

        Files are resources, directories are not.
        """
    @abc.abstractmethod
    def contents(self) -> Iterable[str]:
        """Return an iterable of entries in `package`."""

class TraversalError(Exception): ...

class Traversable(Protocol):
    """
    An object with a subset of pathlib.Path methods suitable for
    traversing directories and opening files.

    Any exceptions that occur when accessing the backing resource
    may propagate unaltered.
    """
    @abc.abstractmethod
    def iterdir(self) -> Iterator['Traversable']:
        """
        Yield Traversable objects in self
        """
    def read_bytes(self) -> bytes:
        """
        Read contents of self as bytes
        """
    def read_text(self, encoding: str | None = None) -> str:
        """
        Read contents of self as text
        """
    @abc.abstractmethod
    def is_dir(self) -> bool:
        """
        Return True if self is a directory
        """
    @abc.abstractmethod
    def is_file(self) -> bool:
        """
        Return True if self is a file
        """
    def joinpath(self, *descendants: StrPath) -> Traversable:
        """
        Return Traversable resolved with any descendants applied.

        Each descendant should be a path segment relative to self
        and each may contain multiple levels separated by
        ``posixpath.sep`` (``/``).
        """
    def __truediv__(self, child: StrPath) -> Traversable:
        """
        Return Traversable child in self
        """
    @abc.abstractmethod
    def open(self, mode: str = 'r', *args, **kwargs):
        """
        mode may be 'r' or 'rb' to open as text or binary. Return a handle
        suitable for reading (same as pathlib.Path.open).

        When opening as text, accepts encoding parameters such as those
        accepted by io.TextIOWrapper.
        """
    @property
    @abc.abstractmethod
    def name(self) -> str:
        """
        The base name of this object without any parent references.
        """

class TraversableResources(ResourceReader, metaclass=abc.ABCMeta):
    """
    The required interface for providing traversable
    resources.
    """
    @abc.abstractmethod
    def files(self) -> Traversable:
        """Return a Traversable object for the loaded package."""
    def open_resource(self, resource: StrPath) -> io.BufferedReader: ...
    def resource_path(self, resource: Any) -> NoReturn: ...
    def is_resource(self, path: StrPath) -> bool: ...
    def contents(self) -> Iterator[str]: ...
