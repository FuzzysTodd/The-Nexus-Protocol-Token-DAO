from _typeshed import Incomplete
from sympy.polys.domains.characteristiczero import CharacteristicZero as CharacteristicZero
from sympy.polys.domains.compositedomain import CompositeDomain as CompositeDomain
from sympy.polys.domains.field import Field as Field
from sympy.polys.polyclasses import DMF as DMF
from sympy.polys.polyerrors import GeneratorsNeeded as GeneratorsNeeded
from sympy.polys.polyutils import basic_from_dict as basic_from_dict, dict_from_basic as dict_from_basic
from sympy.utilities import public as public

class FractionField(Field, CharacteristicZero, CompositeDomain):
    """A class for representing rational function fields. """
    dtype = DMF
    is_FractionField: bool
    is_Frac: bool
    has_assoc_Ring: bool
    has_assoc_Field: bool
    ngens: Incomplete
    zero: Incomplete
    one: Incomplete
    domain: Incomplete
    symbols: Incomplete
    def __init__(self, dom, *gens) -> None: ...
    def new(self, element): ...
    def __hash__(self): ...
    def __eq__(self, other):
        """Returns ``True`` if two domains are equivalent. """
    def to_sympy(self, a):
        """Convert ``a`` to a SymPy object. """
    def from_sympy(self, a):
        """Convert SymPy's expression to ``dtype``. """
    def from_ZZ(K1, a, K0):
        """Convert a Python ``int`` object to ``dtype``. """
    def from_ZZ_python(K1, a, K0):
        """Convert a Python ``int`` object to ``dtype``. """
    def from_QQ_python(K1, a, K0):
        """Convert a Python ``Fraction`` object to ``dtype``. """
    def from_ZZ_gmpy(K1, a, K0):
        """Convert a GMPY ``mpz`` object to ``dtype``. """
    def from_QQ_gmpy(K1, a, K0):
        """Convert a GMPY ``mpq`` object to ``dtype``. """
    def from_RealField(K1, a, K0):
        """Convert a mpmath ``mpf`` object to ``dtype``. """
    def from_GlobalPolynomialRing(K1, a, K0):
        """Convert a ``DMF`` object to ``dtype``. """
    def from_FractionField(K1, a, K0):
        """
        Convert a fraction field element to another fraction field.

        Examples
        ========

        >>> from sympy.polys.polyclasses import DMF
        >>> from sympy.polys.domains import ZZ, QQ
        >>> from sympy.abc import x

        >>> f = DMF(([ZZ(1), ZZ(2)], [ZZ(1), ZZ(1)]), ZZ)

        >>> QQx = QQ.old_frac_field(x)
        >>> ZZx = ZZ.old_frac_field(x)

        >>> QQx.from_FractionField(f, ZZx)
        (x + 2)/(x + 1)

        """
    def get_ring(self):
        """Returns a ring associated with ``self``. """
    def poly_ring(self, *gens) -> None:
        """Returns a polynomial ring, i.e. `K[X]`. """
    def frac_field(self, *gens) -> None:
        """Returns a fraction field, i.e. `K(X)`. """
    def is_positive(self, a):
        """Returns True if ``a`` is positive. """
    def is_negative(self, a):
        """Returns True if ``a`` is negative. """
    def is_nonpositive(self, a):
        """Returns True if ``a`` is non-positive. """
    def is_nonnegative(self, a):
        """Returns True if ``a`` is non-negative. """
    def numer(self, a):
        """Returns numerator of ``a``. """
    def denom(self, a):
        """Returns denominator of ``a``. """
    def factorial(self, a):
        """Returns factorial of ``a``. """
