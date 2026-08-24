from _typeshed import Incomplete
from sympy.polys.agca.modules import FreeModuleQuotientRing as FreeModuleQuotientRing
from sympy.polys.domains.ring import Ring as Ring
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed, NotReversible as NotReversible
from sympy.utilities import public as public

class QuotientRingElement:
    """
    Class representing elements of (commutative) quotient rings.

    Attributes:

    - ring - containing ring
    - data - element of ring.ring (i.e. base ring) representing self
    """
    ring: Incomplete
    data: Incomplete
    def __init__(self, ring, data) -> None: ...
    def __bool__(self) -> bool: ...
    def __add__(self, om): ...
    __radd__ = __add__
    def __neg__(self): ...
    def __sub__(self, om): ...
    def __rsub__(self, om): ...
    def __mul__(self, o): ...
    __rmul__ = __mul__
    def __rtruediv__(self, o): ...
    def __truediv__(self, o): ...
    def __pow__(self, oth): ...
    def __eq__(self, om): ...
    def __ne__(self, om): ...

class QuotientRing(Ring):
    """
    Class representing (commutative) quotient rings.

    You should not usually instantiate this by hand, instead use the constructor
    from the base ring in the construction.

    >>> from sympy.abc import x
    >>> from sympy import QQ
    >>> I = QQ.old_poly_ring(x).ideal(x**3 + 1)
    >>> QQ.old_poly_ring(x).quotient_ring(I)
    QQ[x]/<x**3 + 1>

    Shorter versions are possible:

    >>> QQ.old_poly_ring(x)/I
    QQ[x]/<x**3 + 1>

    >>> QQ.old_poly_ring(x)/[x**3 + 1]
    QQ[x]/<x**3 + 1>

    Attributes:

    - ring - the base ring
    - base_ideal - the ideal used to form the quotient
    """
    has_assoc_Ring: bool
    has_assoc_Field: bool
    dtype = QuotientRingElement
    ring: Incomplete
    base_ideal: Incomplete
    zero: Incomplete
    one: Incomplete
    def __init__(self, ring, ideal) -> None: ...
    def __hash__(self): ...
    def new(self, a):
        """Construct an element of ``self`` domain from ``a``. """
    def __eq__(self, other):
        """Returns ``True`` if two domains are equivalent. """
    def from_ZZ(K1, a, K0):
        """Convert a Python ``int`` object to ``dtype``. """
    from_ZZ_python = from_ZZ
    from_QQ_python = from_ZZ_python
    from_ZZ_gmpy = from_ZZ_python
    from_QQ_gmpy = from_ZZ_python
    from_RealField = from_ZZ_python
    from_GlobalPolynomialRing = from_ZZ_python
    from_FractionField = from_ZZ_python
    def from_sympy(self, a): ...
    def to_sympy(self, a): ...
    def from_QuotientRing(self, a, K0): ...
    def poly_ring(self, *gens) -> None:
        """Returns a polynomial ring, i.e. ``K[X]``. """
    def frac_field(self, *gens) -> None:
        """Returns a fraction field, i.e. ``K(X)``. """
    def revert(self, a):
        """
        Compute a**(-1), if possible.
        """
    def is_zero(self, a): ...
    def free_module(self, rank):
        """
        Generate a free module of rank ``rank`` over ``self``.

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> (QQ.old_poly_ring(x)/[x**2 + 1]).free_module(2)
        (QQ[x]/<x**2 + 1>)**2
        """
