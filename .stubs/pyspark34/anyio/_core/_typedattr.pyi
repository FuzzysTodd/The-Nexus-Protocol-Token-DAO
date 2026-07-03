from ._exceptions import TypedAttributeLookupError as TypedAttributeLookupError
from _typeshed import Incomplete
from typing import Any, Callable, Mapping, TypeVar, overload

T_Attr = TypeVar('T_Attr')
T_Default = TypeVar('T_Default')
undefined: Incomplete

def typed_attribute() -> Any:
    """Return a unique object, used to mark typed attributes."""

class TypedAttributeSet:
    """
    Superclass for typed attribute collections.

    Checks that every public attribute of every subclass has a type annotation.
    """
    def __init_subclass__(cls) -> None: ...

class TypedAttributeProvider:
    """Base class for classes that wish to provide typed extra attributes."""
    @property
    def extra_attributes(self) -> Mapping[T_Attr, Callable[[], T_Attr]]:
        """
        A mapping of the extra attributes to callables that return the corresponding values.

        If the provider wraps another provider, the attributes from that wrapper should also be
        included in the returned mapping (but the wrapper may override the callables from the
        wrapped instance).

        """
    @overload
    def extra(self, attribute: T_Attr) -> T_Attr: ...
    @overload
    def extra(self, attribute: T_Attr, default: T_Default) -> T_Attr | T_Default: ...
