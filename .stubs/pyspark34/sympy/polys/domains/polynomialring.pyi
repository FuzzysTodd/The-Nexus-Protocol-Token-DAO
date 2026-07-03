from _typeshed import Incomplete
from sympy.polys.domains.compositedomain import CompositeDomain as CompositeDomain
from sympy.polys.domains.ring import Ring as Ring
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed, GeneratorsError as GeneratorsError
from sympy.utilities import public as public

class PolynomialRing(Ring, CompositeDomain):
    """A class for representing multivariate polynomial rings. """
    is_PolynomialRing: bool
    is_Poly: bool
    has_assoc_Ring: bool
    has_assoc_Field: bool
    ring: Incomplete
    dtype: Incomplete
    gens: Incomplete
    ngens: Incomplete
    symbols: Incomplete
    domain: Incomplete
    is_PID: bool
    dom: Incomplete
    def __init__(self, domain_or_ring, symbols: Incomplete | None = None, order: Incomplete | None = None) -> None: ...
    def new(self, element): ...
    @property
    def zero(self): ...
    @property
    def one(self): ...
    @property
    def order(self): ...
    def __hash__(self): ...
    def __eq__(self, other):
        """Returns `True` if two domains are equivalent. """
    def is_unit(self, a):
        """Returns ``True`` if ``a`` is a unit of ``self``"""
    def canonical_unit(self, a): ...
    def to_sympy(self, a):
        """Convert `a` to a SymPy object. """
    def from_sympy(self, a):
        """Convert SymPy's expression to `dtype`. """
    def from_ZZ(K1, a, K0):
        """Convert a Python `int` object to `dtype`. """
    def from_ZZ_python(K1, a, K0):
        """Convert a Python `int` object to `dtype`. """
    def from_QQ(K1, a, K0):
        """Convert a Python `Fraction` object to `dtype`. """
    def from_QQ_python(K1, a, K0):
        """Convert a Python `Fraction` object to `dtype`. """
    def from_ZZ_gmpy(K1, a, K0):
        """Convert a GMPY `mpz` object to `dtype`. """
    def from_QQ_gmpy(K1, a, K0):
        """Convert a GMPY `mpq` object to `dtype`. """
    def from_GaussianIntegerRing(K1, a, K0):
        """Convert a `GaussianInteger` object to `dtype`. """
    def from_GaussianRationalField(K1, a, K0):
        """Convert a `GaussianRational` object to `dtype`. """
    def from_RealField(K1, a, K0):
        """Convert a mpmath `mpf` object to `dtype`. """
    def from_ComplexField(K1, a, K0):
        """Convert a mpmath `mpf` object to `dtype`. """
    def from_AlgebraicField(K1, a, K0):
        """Convert an algebraic number to ``dtype``. """
    def from_PolynomialRing(K1, a, K0):
        """Convert a polynomial to ``dtype``. """
    def from_FractionField(K1, a, K0):
        """Convert a rational function to ``dtype``. """
    def from_GlobalPolynomialRing(K1, a, K0):
        """Convert from old poly ring to ``dtype``. """
    def get_field(self):
        """Returns a field associated with `self`. """
    def is_positive(self, a):
        """Returns True if `LC(a)` is positive. """
    def is_negative(self, a):
        """Returns True if `LC(a)` is negative. """
    def is_nonpositive(self, a):
        """Returns True if `LC(a)` is non-positive. """
    def is_nonnegative(self, a):
        """Returns True if `LC(a)` is non-negative. """
    def gcdex(self, a, b):
        """Extended GCD of `a` and `b`. """
    def gcd(self, a, b):
        """Returns GCD of `a` and `b`. """
    def lcm(self, a, b):
        """Returns LCM of `a` and `b`. """
    def factorial(self, a):
        """Returns factorial of `a`. """
