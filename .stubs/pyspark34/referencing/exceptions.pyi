from referencing import Resource as Resource
from referencing._attrs import frozen as frozen
from referencing.typing import URI as URI
from typing import Any

class NoSuchResource(KeyError):
    """
    The given URI is not present in a registry.

    Unlike most exceptions, this class *is* intended to be publicly
    instantiable and *is* part of the public API of the package.
    """
    ref: URI
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class NoInternalID(Exception):
    """
    A resource has no internal ID, but one is needed.

    E.g. in modern JSON Schema drafts, this is the :kw:`$id` keyword.

    One might be needed if a resource was to-be added to a registry but no
    other URI is available, and the resource doesn't declare its canonical URI.
    """
    resource: Resource[Any]
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class Unretrievable(KeyError):
    """
    The given URI is not present in a registry, and retrieving it failed.
    """
    ref: URI
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class CannotDetermineSpecification(Exception):
    """
    Attempting to detect the appropriate `Specification` failed.

    This happens if no discernible information is found in the contents of the
    new resource which would help identify it.
    """
    contents: Any
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class Unresolvable(Exception):
    """
    A reference was unresolvable.
    """
    ref: URI
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, ref) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class PointerToNowhere(Unresolvable):
    """
    A JSON Pointer leads to a part of a document that does not exist.
    """
    resource: Resource[Any]

class NoSuchAnchor(Unresolvable):
    """
    An anchor does not exist within a particular resource.
    """
    resource: Resource[Any]
    anchor: str

class InvalidAnchor(Unresolvable):
    """
    An anchor which could never exist in a resource was dereferenced.

    It is somehow syntactically invalid.
    """
    resource: Resource[Any]
    anchor: str
