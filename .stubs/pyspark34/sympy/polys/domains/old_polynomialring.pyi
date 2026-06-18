from _typeshed import Incomplete
from sympy.polys.agca.modules import FreeModulePolyRing as FreeModulePolyRing
from sympy.polys.domains.characteristiczero import CharacteristicZero as CharacteristicZero
from sympy.polys.domains.compositedomain import CompositeDomain as CompositeDomain
from sympy.polys.domains.old_fractionfield import FractionField as FractionField
from sympy.polys.domains.ring import Ring as Ring
from sympy.polys.orderings import build_product_order as build_product_order, monomial_key as monomial_key
from sympy.polys.polyclasses import DMF as DMF, DMP as DMP
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed, ExactQuotientFailed as ExactQuotientFailed, GeneratorsNeeded as GeneratorsNeeded, NotReversible as NotReversible, PolynomialError as PolynomialError
from sympy.polys.polyutils import basic_from_dict as basic_from_dict, dict_from_basic as dict_from_basic
from sympy.utilities import public as public
from sympy.utilities.iterables import iterable as iterable

class PolynomialRingBase(Ring, CharacteristicZero, CompositeDomain):
    """
    Base class for generalized polynomial rings.

    This base class should be used for uniform access to generalized polynomial
    rings. Subclasses only supply information about the element storage etc.

    Do not instantiate.
    """
    has_assoc_Ring: bool
    has_assoc_Field: bool
    default_order: str
    ngens: Incomplete
    zero: Incomplete
    one: Incomplete
    domain: Incomplete
    symbols: Incomplete
    order: Incomplete
    def __init__(self, dom, *gens, **opts) -> None: ...
    def new(self, element): ...
    def __hash__(self): ...
    def __eq__(self, other):
        """Returns ``True`` if two domains are equivalent. """
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
    def from_RealField(K1, a, K0):
        """Convert a mpmath ``mpf`` object to ``dtype``. """
    def from_AlgebraicField(K1, a, K0):
        """Convert a ``ANP`` object to ``dtype``. """
    def from_PolynomialRing(K1, a, K0):
        """Convert a ``PolyElement`` object to ``dtype``. """
    def from_GlobalPolynomialRing(K1, a, K0):
        """Convert a ``DMP`` object to ``dtype``. """
    def get_field(self):
        """Returns a field associated with ``self``. """
    def poly_ring(self, *gens) -> None:
        """Returns a polynomial ring, i.e. ``K[X]``. """
    def frac_field(self, *gens) -> None:
        """Returns a fraction field, i.e. ``K(X)``. """
    def revert(self, a): ...
    def gcdex(self, a, b):
        """Extended GCD of ``a`` and ``b``. """
    def gcd(self, a, b):
        """Returns GCD of ``a`` and ``b``. """
    def lcm(self, a, b):
        """Returns LCM of ``a`` and ``b``. """
    def factorial(self, a):
        """Returns factorial of ``a``. """
    def free_module(self, rank):
        """
        Generate a free module of rank ``rank`` over ``self``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> QQ.old_poly_ring(x).free_module(2)
        QQ[x]**2
        """

class GlobalPolynomialRing(PolynomialRingBase):
    """A true polynomial ring, with objects DMP. """
    is_PolynomialRing: bool
    is_Poly: bool
    dtype = DMP
    def from_FractionField(K1, a, K0):
        """
        Convert a ``DMF`` object to ``DMP``.

        Examples
        ========

        >>> from sympy.polys.polyclasses import DMP, DMF
        >>> from sympy.polys.domains import ZZ
        >>> from sympy.abc import x

        >>> f = DMF(([ZZ(1), ZZ(1)], [ZZ(1)]), ZZ)
        >>> K = ZZ.old_frac_field(x)

        >>> F = ZZ.old_poly_ring(x).from_FractionField(f, K)

        >>> F == DMP([ZZ(1), ZZ(1)], ZZ)
        True
        >>> type(F)
        <class 'sympy.polys.polyclasses.DMP'>

        """
    def to_sympy(self, a):
        """Convert ``a`` to a SymPy object. """
    def from_sympy(self, a):
        """Convert SymPy's expression to ``dtype``. """
    def is_positive(self, a):
        """Returns True if ``LC(a)`` is positive. """
    def is_negative(self, a):
        """Returns True if ``LC(a)`` is negative. """
    def is_nonpositive(self, a):
        """Returns True if ``LC(a)`` is non-positive. """
    def is_nonnegative(self, a):
        """Returns True if ``LC(a)`` is non-negative. """

class GeneralizedPolynomialRing(PolynomialRingBase):
    """A generalized polynomial ring, with objects DMF. """
    dtype = DMF
    def new(self, a):
        """Construct an element of ``self`` domain from ``a``. """
    def __contains__(self, a) -> bool: ...
    def from_FractionField(K1, a, K0): ...
    def to_sympy(self, a):
        """Convert ``a`` to a SymPy object. """
    def from_sympy(self, a):
        """Convert SymPy's expression to ``dtype``. """

def PolynomialRing(dom, *gens, **opts):
    '''
    Create a generalized multivariate polynomial ring.

    A generalized polynomial ring is defined by a ground field `K`, a set
    of generators (typically `x_1, \\ldots, x_n`) and a monomial order `<`.
    The monomial order can be global, local or mixed. In any case it induces
    a total ordering on the monomials, and there exists for every (non-zero)
    polynomial `f \\in K[x_1, \\ldots, x_n]` a well-defined "leading monomial"
    `LM(f) = LM(f, >)`. One can then define a multiplicative subset
    `S = S_> = \\{f \\in K[x_1, \\ldots, x_n] | LM(f) = 1\\}`. The generalized
    polynomial ring corresponding to the monomial order is
    `R = S^{-1}K[x_1, \\ldots, x_n]`.

    If `>` is a so-called global order, that is `1` is the smallest monomial,
    then we just have `S = K` and `R = K[x_1, \\ldots, x_n]`.

    Examples
    ========

    A few examples may make this clearer.

    >>> from sympy.abc import x, y
    >>> from sympy import QQ

    Our first ring uses global lexicographic order.

    >>> R1 = QQ.old_poly_ring(x, y, order=(("lex", x, y),))

    The second ring uses local lexicographic order. Note that when using a
    single (non-product) order, you can just specify the name and omit the
    variables:

    >>> R2 = QQ.old_poly_ring(x, y, order="ilex")

    The third and fourth rings use a mixed orders:

    >>> o1 = (("ilex", x), ("lex", y))
    >>> o2 = (("lex", x), ("ilex", y))
    >>> R3 = QQ.old_poly_ring(x, y, order=o1)
    >>> R4 = QQ.old_poly_ring(x, y, order=o2)

    We will investigate what elements of `K(x, y)` are contained in the various
    rings.

    >>> L = [x, 1/x, y/(1 + x), 1/(1 + y), 1/(1 + x*y)]
    >>> test = lambda R: [f in R for f in L]

    The first ring is just `K[x, y]`:

    >>> test(R1)
    [True, False, False, False, False]

    The second ring is R1 localised at the maximal ideal (x, y):

    >>> test(R2)
    [True, False, True, True, True]

    The third ring is R1 localised at the prime ideal (x):

    >>> test(R3)
    [True, False, True, False, True]

    Finally the fourth ring is R1 localised at `S = K[x, y] \\setminus yK[y]`:

    >>> test(R4)
    [True, False, False, True, False]
    '''
