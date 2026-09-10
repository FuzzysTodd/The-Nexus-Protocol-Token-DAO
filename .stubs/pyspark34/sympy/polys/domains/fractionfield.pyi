from _typeshed import Incomplete
from sympy.polys.domains.compositedomain import CompositeDomain as CompositeDomain
from sympy.polys.domains.field import Field as Field
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed, GeneratorsError as GeneratorsError
from sympy.utilities import public as public

class FractionField(Field, CompositeDomain):
    """A class for representing multivariate rational function fields. """
    is_FractionField: bool
    is_Frac: bool
    has_assoc_Ring: bool
    has_assoc_Field: bool
    field: Incomplete
    dtype: Incomplete
    gens: Incomplete
    ngens: Incomplete
    symbols: Incomplete
    domain: Incomplete
    dom: Incomplete
    def __init__(self, domain_or_field, symbols: Incomplete | None = None, order: Incomplete | None = None) -> None: ...
    def new(self, element): ...
    @property
    def zero(self): ...
    @property
    def one(self): ...
    @property
    def order(self): ...
    @property
    def is_Exact(self): ...
    def get_exact(self): ...
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
    def from_QQ(K1, a, K0):
        """Convert a Python ``Fraction`` object to ``dtype``. """
    def from_QQ_python(K1, a, K0):
        """Convert a Python ``Fraction`` object to ``dtype``. """
    def from_ZZ_gmpy(K1, a, K0):
        """Convert a GMPY ``mpz`` object to ``dtype``. """
    def from_QQ_gmpy(K1, a, K0):
        """Convert a GMPY ``mpq`` object to ``dtype``. """
    def from_GaussianRationalField(K1, a, K0):
        """Convert a ``GaussianRational`` object to ``dtype``. """
    def from_GaussianIntegerRing(K1, a, K0):
        """Convert a ``GaussianInteger`` object to ``dtype``. """
    def from_RealField(K1, a, K0):
        """Convert a mpmath ``mpf`` object to ``dtype``. """
    def from_ComplexField(K1, a, K0):
        """Convert a mpmath ``mpf`` object to ``dtype``. """
    def from_AlgebraicField(K1, a, K0):
        """Convert an algebraic number to ``dtype``. """
    def from_PolynomialRing(K1, a, K0):
        """Convert a polynomial to ``dtype``. """
    def from_FractionField(K1, a, K0):
        """Convert a rational function to ``dtype``. """
    def get_ring(self):
        """Returns a field associated with ``self``. """
    def is_positive(self, a):
        """Returns True if ``LC(a)`` is positive. """
    def is_negative(self, a):
        """Returns True if ``LC(a)`` is negative. """
    def is_nonpositive(self, a):
        """Returns True if ``LC(a)`` is non-positive. """
    def is_nonnegative(self, a):
        """Returns True if ``LC(a)`` is non-negative. """
    def numer(self, a):
        """Returns numerator of ``a``. """
    def denom(self, a):
        """Returns denominator of ``a``. """
    def factorial(self, a):
        """Returns factorial of ``a``. """
