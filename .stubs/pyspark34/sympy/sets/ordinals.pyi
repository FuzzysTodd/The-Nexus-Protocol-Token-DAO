from _typeshed import Incomplete
from sympy.core import Basic as Basic, Integer as Integer

class OmegaPower(Basic):
    """
    Represents ordinal exponential and multiplication terms one of the
    building blocks of the :class:`Ordinal` class.
    In ``OmegaPower(a, b)``, ``a`` represents exponent and ``b`` represents multiplicity.
    """
    def __new__(cls, a, b): ...
    @property
    def exp(self): ...
    @property
    def mult(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def __lt__(self, other): ...

class Ordinal(Basic):
    """
    Represents ordinals in Cantor normal form.

    Internally, this class is just a list of instances of OmegaPower.

    Examples
    ========
    >>> from sympy import Ordinal, OmegaPower
    >>> from sympy.sets.ordinals import omega
    >>> w = omega
    >>> w.is_limit_ordinal
    True
    >>> Ordinal(OmegaPower(w + 1, 1), OmegaPower(3, 2))
    w**(w + 1) + w**3*2
    >>> 3 + w
    w
    >>> (w + 1) * w
    w**2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Ordinal_arithmetic
    """
    def __new__(cls, *terms): ...
    @property
    def terms(self): ...
    @property
    def leading_term(self): ...
    @property
    def trailing_term(self): ...
    @property
    def is_successor_ordinal(self): ...
    @property
    def is_limit_ordinal(self): ...
    @property
    def degree(self): ...
    @classmethod
    def convert(cls, integer_value): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __pow__(self, other): ...

class OrdinalZero(Ordinal):
    """The ordinal zero.

    OrdinalZero can be imported as ``ord0``.
    """

class OrdinalOmega(Ordinal):
    """The ordinal omega which forms the base of all ordinals in cantor normal form.

    OrdinalOmega can be imported as ``omega``.

    Examples
    ========

    >>> from sympy.sets.ordinals import omega
    >>> omega + omega
    w*2
    """
    def __new__(cls): ...
    @property
    def terms(self): ...

ord0: Incomplete
omega: Incomplete
