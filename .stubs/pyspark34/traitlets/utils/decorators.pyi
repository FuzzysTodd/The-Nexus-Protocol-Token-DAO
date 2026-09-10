from ..traitlets import HasTraits as HasTraits, Undefined as Undefined
from typing import Type, TypeVar

T = TypeVar('T', bound=HasTraits)

def signature_has_traits(cls) -> Type[T]:
    """Return a decorated class with a constructor signature that contain Trait names as kwargs."""
