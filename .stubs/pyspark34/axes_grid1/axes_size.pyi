from _typeshed import Incomplete

class _Base:
    def __rmul__(self, other): ...
    def __add__(self, other): ...

class Add(_Base):
    def __init__(self, a, b) -> None: ...
    def get_size(self, renderer): ...

class AddList(_Base):
    def __init__(self, add_list) -> None: ...
    def get_size(self, renderer): ...

class Fixed(_Base):
    """
    Simple fixed size with absolute part = *fixed_size* and relative part = 0.
    """
    fixed_size: Incomplete
    def __init__(self, fixed_size) -> None: ...
    def get_size(self, renderer): ...

class Scaled(_Base):
    """
    Simple scaled(?) size with absolute part = 0 and
    relative part = *scalable_size*.
    """
    def __init__(self, scalable_size) -> None: ...
    def get_size(self, renderer): ...
Scalable = Scaled

class AxesX(_Base):
    """
    Scaled size whose relative part corresponds to the data width
    of the *axes* multiplied by the *aspect*.
    """
    def __init__(self, axes, aspect: float = 1.0, ref_ax: Incomplete | None = None) -> None: ...
    def get_size(self, renderer): ...

class AxesY(_Base):
    """
    Scaled size whose relative part corresponds to the data height
    of the *axes* multiplied by the *aspect*.
    """
    def __init__(self, axes, aspect: float = 1.0, ref_ax: Incomplete | None = None) -> None: ...
    def get_size(self, renderer): ...

class MaxExtent(_Base):
    """
    Size whose absolute part is either the largest width or the largest height
    of the given *artist_list*.
    """
    def __init__(self, artist_list, w_or_h) -> None: ...
    def add_artist(self, a) -> None: ...
    def get_size(self, renderer): ...

class MaxWidth(MaxExtent):
    """
    Size whose absolute part is the largest width of the given *artist_list*.
    """
    def __init__(self, artist_list) -> None: ...

class MaxHeight(MaxExtent):
    """
    Size whose absolute part is the largest height of the given *artist_list*.
    """
    def __init__(self, artist_list) -> None: ...

class Fraction(_Base):
    """
    An instance whose size is a *fraction* of the *ref_size*.

    >>> s = Fraction(0.3, AxesX(ax))
    """
    def __init__(self, fraction, ref_size) -> None: ...
    def get_size(self, renderer): ...

class Padded(_Base):
    """
    Return an instance where the absolute part of *size* is
    increase by the amount of *pad*.
    """
    def __init__(self, size, pad) -> None: ...
    def get_size(self, renderer): ...

def from_any(size, fraction_ref: Incomplete | None = None):
    '''
    Create a Fixed unit when the first argument is a float, or a
    Fraction unit if that is a string that ends with %. The second
    argument is only meaningful when Fraction unit is created.

    >>> a = Size.from_any(1.2) # => Size.Fixed(1.2)
    >>> Size.from_any("50%", a) # => Size.Fraction(0.5, a)
    '''

class SizeFromFunc(_Base):
    def __init__(self, func) -> None: ...
    def get_size(self, renderer): ...

class GetExtentHelper:
    def __init__(self, ax, direction) -> None: ...
    def __call__(self, renderer): ...

class _AxesDecorationsSize(_Base):
    """
    Fixed size, corresponding to the size of decorations on a given Axes side.
    """
    def __init__(self, ax, direction) -> None: ...
    def get_size(self, renderer): ...
