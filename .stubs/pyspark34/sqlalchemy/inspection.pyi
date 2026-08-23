from . import exc as exc
from .util.typing import Literal as Literal, Protocol as Protocol
from typing import Any, Generic, Type, overload

class Inspectable(Generic[_T]):
    """define a class as inspectable.

    This allows typing to set up a linkage between an object that
    can be inspected and the type of inspection it returns.

    Unfortunately we cannot at the moment get all classes that are
    returned by inspection to suit this interface as we get into
    MRO issues.

    """
class _InspectableTypeProtocol(Protocol[_TCov]):
    """a protocol defining a method that's used when a type (ie the class
    itself) is passed to inspect().

    """
class _InspectableProtocol(Protocol[_TCov]):
    """a protocol defining a method that's used when an instance is
    passed to inspect().

    """

@overload
def inspect(subject: Type[_InspectableTypeProtocol[_IN]], raiseerr: bool = True) -> _IN: ...
@overload
def inspect(subject: _InspectableProtocol[_IN], raiseerr: bool = True) -> _IN: ...
@overload
def inspect(subject: Inspectable[_IN], raiseerr: bool = True) -> _IN: ...
@overload
def inspect(subject: Any, raiseerr: Literal[False] = ...) -> Any | None: ...
@overload
def inspect(subject: Any, raiseerr: bool = True) -> Any: ...
