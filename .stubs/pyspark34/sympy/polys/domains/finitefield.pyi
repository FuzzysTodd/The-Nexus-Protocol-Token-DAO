from _typeshed import Incomplete
from sympy.polys.domains.field import Field as Field
from sympy.polys.domains.groundtypes import SymPyInteger as SymPyInteger
from sympy.polys.domains.modularinteger import ModularIntegerFactory as ModularIntegerFactory
from sympy.polys.domains.simpledomain import SimpleDomain as SimpleDomain
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed
from sympy.utilities import public as public

class FiniteField(Field, SimpleDomain):
    """Finite field of prime order :ref:`GF(p)`

    A :ref:`GF(p)` domain represents a `finite field`_ `\\mathbb{F}_p` of prime
    order as :py:class:`~.Domain` in the domain system (see
    :ref:`polys-domainsintro`).

    A :py:class:`~.Poly` created from an expression with integer
    coefficients will have the domain :ref:`ZZ`. However, if the ``modulus=p``
    option is given then the domain will be a finite field instead.

    >>> from sympy import Poly, Symbol
    >>> x = Symbol('x')
    >>> p = Poly(x**2 + 1)
    >>> p
    Poly(x**2 + 1, x, domain='ZZ')
    >>> p.domain
    ZZ
    >>> p2 = Poly(x**2 + 1, modulus=2)
    >>> p2
    Poly(x**2 + 1, x, modulus=2)
    >>> p2.domain
    GF(2)

    It is possible to factorise a polynomial over :ref:`GF(p)` using the
    modulus argument to :py:func:`~.factor` or by specifying the domain
    explicitly. The domain can also be given as a string.

    >>> from sympy import factor, GF
    >>> factor(x**2 + 1)
    x**2 + 1
    >>> factor(x**2 + 1, modulus=2)
    (x + 1)**2
    >>> factor(x**2 + 1, domain=GF(2))
    (x + 1)**2
    >>> factor(x**2 + 1, domain='GF(2)')
    (x + 1)**2

    It is also possible to use :ref:`GF(p)` with the :py:func:`~.cancel`
    and :py:func:`~.gcd` functions.

    >>> from sympy import cancel, gcd
    >>> cancel((x**2 + 1)/(x + 1))
    (x**2 + 1)/(x + 1)
    >>> cancel((x**2 + 1)/(x + 1), domain=GF(2))
    x + 1
    >>> gcd(x**2 + 1, x + 1)
    1
    >>> gcd(x**2 + 1, x + 1, domain=GF(2))
    x + 1

    When using the domain directly :ref:`GF(p)` can be used as a constructor
    to create instances which then support the operations ``+,-,*,**,/``

    >>> from sympy import GF
    >>> K = GF(5)
    >>> K
    GF(5)
    >>> x = K(3)
    >>> y = K(2)
    >>> x
    3 mod 5
    >>> y
    2 mod 5
    >>> x * y
    1 mod 5
    >>> x / y
    4 mod 5

    Notes
    =====

    It is also possible to create a :ref:`GF(p)` domain of **non-prime**
    order but the resulting ring is **not** a field: it is just the ring of
    the integers modulo ``n``.

    >>> K = GF(9)
    >>> z = K(3)
    >>> z
    3 mod 9
    >>> z**2
    0 mod 9

    It would be good to have a proper implementation of prime power fields
    (``GF(p**n)``) but these are not yet implemented in SymPY.

    .. _finite field: https://en.wikipedia.org/wiki/Finite_field
    """
    rep: str
    alias: str
    is_FiniteField: bool
    is_FF: bool
    is_Numerical: bool
    has_assoc_Ring: bool
    has_assoc_Field: bool
    dom: Incomplete
    mod: Incomplete
    dtype: Incomplete
    zero: Incomplete
    one: Incomplete
    def __init__(self, mod, symmetric: bool = True) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other):
        """Returns ``True`` if two domains are equivalent. """
    def characteristic(self):
        """Return the characteristic of this domain. """
    def get_field(self):
        """Returns a field associated with ``self``. """
    def to_sympy(self, a):
        """Convert ``a`` to a SymPy object. """
    def from_sympy(self, a):
        """Convert SymPy's Integer to SymPy's ``Integer``. """
    def from_FF(K1, a, K0: Incomplete | None = None):
        """Convert ``ModularInteger(int)`` to ``dtype``. """
    def from_FF_python(K1, a, K0: Incomplete | None = None):
        """Convert ``ModularInteger(int)`` to ``dtype``. """
    def from_ZZ(K1, a, K0: Incomplete | None = None):
        """Convert Python's ``int`` to ``dtype``. """
    def from_ZZ_python(K1, a, K0: Incomplete | None = None):
        """Convert Python's ``int`` to ``dtype``. """
    def from_QQ(K1, a, K0: Incomplete | None = None):
        """Convert Python's ``Fraction`` to ``dtype``. """
    def from_QQ_python(K1, a, K0: Incomplete | None = None):
        """Convert Python's ``Fraction`` to ``dtype``. """
    def from_FF_gmpy(K1, a, K0: Incomplete | None = None):
        """Convert ``ModularInteger(mpz)`` to ``dtype``. """
    def from_ZZ_gmpy(K1, a, K0: Incomplete | None = None):
        """Convert GMPY's ``mpz`` to ``dtype``. """
    def from_QQ_gmpy(K1, a, K0: Incomplete | None = None):
        """Convert GMPY's ``mpq`` to ``dtype``. """
    def from_RealField(K1, a, K0):
        """Convert mpmath's ``mpf`` to ``dtype``. """
FF = FiniteField
GF = FiniteField
