from _typeshed import Incomplete
from typing import Any, Callable
from typing_extensions import TypeGuard

__all__ = ['Dimension', 'D', 'sum_layout_dimensions', 'max_layout_dimensions', 'AnyDimension', 'to_dimension', 'is_dimension']

class Dimension:
    """
    Specified dimension (width/height) of a user control or window.

    The layout engine tries to honor the preferred size. If that is not
    possible, because the terminal is larger or smaller, it tries to keep in
    between min and max.

    :param min: Minimum size.
    :param max: Maximum size.
    :param weight: For a VSplit/HSplit, the actual size will be determined
                   by taking the proportion of weights from all the children.
                   E.g. When there are two children, one with a weight of 1,
                   and the other with a weight of 2, the second will always be
                   twice as big as the first, if the min/max values allow it.
    :param preferred: Preferred size.
    """
    min_specified: Incomplete
    max_specified: Incomplete
    preferred_specified: Incomplete
    weight_specified: Incomplete
    min: Incomplete
    max: Incomplete
    preferred: Incomplete
    weight: Incomplete
    def __init__(self, min: int | None = None, max: int | None = None, weight: int | None = None, preferred: int | None = None) -> None: ...
    @classmethod
    def exact(cls, amount: int) -> Dimension:
        """
        Return a :class:`.Dimension` with an exact size. (min, max and
        preferred set to ``amount``).
        """
    @classmethod
    def zero(cls) -> Dimension:
        """
        Create a dimension that represents a zero size. (Used for 'invisible'
        controls.)
        """
    def is_zero(self) -> bool:
        """True if this `Dimension` represents a zero size."""

def sum_layout_dimensions(dimensions: list[Dimension]) -> Dimension:
    """
    Sum a list of :class:`.Dimension` instances.
    """
def max_layout_dimensions(dimensions: list[Dimension]) -> Dimension:
    """
    Take the maximum of a list of :class:`.Dimension` instances.
    Used when we have a HSplit/VSplit, and we want to get the best width/height.)
    """
AnyDimension = None | int | Dimension | Callable[[], Any]

def to_dimension(value: AnyDimension) -> Dimension:
    """
    Turn the given object into a `Dimension` object.
    """
def is_dimension(value: object) -> TypeGuard[AnyDimension]:
    """
    Test whether the given value could be a valid dimension.
    (For usage in an assertion. It's not guaranteed in case of a callable.)
    """
D = Dimension
LayoutDimension = Dimension
