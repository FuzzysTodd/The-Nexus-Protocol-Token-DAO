from _typeshed import Incomplete
from sympy.core.numbers import I as I
from sympy.polys.domains.algebraicfield import AlgebraicField as AlgebraicField
from sympy.polys.domains.domain import Domain as Domain
from sympy.polys.domains.domainelement import DomainElement as DomainElement
from sympy.polys.domains.field import Field as Field
from sympy.polys.domains.integerring import ZZ as ZZ
from sympy.polys.domains.rationalfield import QQ as QQ
from sympy.polys.domains.ring import Ring as Ring
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed

class GaussianElement(DomainElement):
    """Base class for elements of Gaussian type domains."""
    base: Domain
    def __new__(cls, x, y: int = 0): ...
    @classmethod
    def new(cls, x, y):
        """Create a new GaussianElement of the same domain."""
    def parent(self):
        """The domain that this is an element of (ZZ_I or QQ_I)"""
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __pos__(self): ...
    def __neg__(self): ...
    def __add__(self, other): ...
    __radd__ = __add__
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    __rmul__ = __mul__
    def __pow__(self, exp): ...
    def __bool__(self) -> bool: ...
    def quadrant(self):
        """Return quadrant index 0-3.

        0 is included in quadrant 0.
        """
    def __rdivmod__(self, other): ...
    def __rtruediv__(self, other): ...
    def __floordiv__(self, other): ...
    def __rfloordiv__(self, other): ...
    def __mod__(self, other): ...
    def __rmod__(self, other): ...

class GaussianInteger(GaussianElement):
    """Gaussian integer: domain element for :ref:`ZZ_I`

        >>> from sympy import ZZ_I
        >>> z = ZZ_I(2, 3)
        >>> z
        (2 + 3*I)
        >>> type(z)
        <class 'sympy.polys.domains.gaussiandomains.GaussianInteger'>
    """
    base = ZZ
    def __truediv__(self, other):
        """Return a Gaussian rational."""
    def __divmod__(self, other): ...

class GaussianRational(GaussianElement):
    """Gaussian rational: domain element for :ref:`QQ_I`

        >>> from sympy import QQ_I, QQ
        >>> z = QQ_I(QQ(2, 3), QQ(4, 5))
        >>> z
        (2/3 + 4/5*I)
        >>> type(z)
        <class 'sympy.polys.domains.gaussiandomains.GaussianRational'>
    """
    base = QQ
    def __truediv__(self, other):
        """Return a Gaussian rational."""
    def __divmod__(self, other): ...

class GaussianDomain:
    """Base class for Gaussian domains."""
    dom: Domain
    is_Numerical: bool
    is_Exact: bool
    has_assoc_Ring: bool
    has_assoc_Field: bool
    def to_sympy(self, a):
        """Convert ``a`` to a SymPy object. """
    def from_sympy(self, a):
        """Convert a SymPy object to ``self.dtype``."""
    def inject(self, *gens):
        """Inject generators into this domain. """
    def canonical_unit(self, d): ...
    def is_negative(self, element):
        """Returns ``False`` for any ``GaussianElement``. """
    def is_positive(self, element):
        """Returns ``False`` for any ``GaussianElement``. """
    def is_nonnegative(self, element):
        """Returns ``False`` for any ``GaussianElement``. """
    def is_nonpositive(self, element):
        """Returns ``False`` for any ``GaussianElement``. """
    def from_ZZ_gmpy(K1, a, K0):
        """Convert a GMPY mpz to ``self.dtype``."""
    def from_ZZ(K1, a, K0):
        """Convert a ZZ_python element to ``self.dtype``."""
    def from_ZZ_python(K1, a, K0):
        """Convert a ZZ_python element to ``self.dtype``."""
    def from_QQ(K1, a, K0):
        """Convert a GMPY mpq to ``self.dtype``."""
    def from_QQ_gmpy(K1, a, K0):
        """Convert a GMPY mpq to ``self.dtype``."""
    def from_QQ_python(K1, a, K0):
        """Convert a QQ_python element to ``self.dtype``."""
    def from_AlgebraicField(K1, a, K0):
        """Convert an element from ZZ<I> or QQ<I> to ``self.dtype``."""

class GaussianIntegerRing(GaussianDomain, Ring):
    """Ring of Gaussian integers ``ZZ_I``

    The :ref:`ZZ_I` domain represents the `Gaussian integers`_ `\\mathbb{Z}[i]`
    as a :py:class:`~.Domain` in the domain system (see
    :ref:`polys-domainsintro`).

    By default a :py:class:`~.Poly` created from an expression with
    coefficients that are combinations of integers and ``I`` (`\\sqrt{-1}`)
    will have the domain :ref:`ZZ_I`.

    >>> from sympy import Poly, Symbol, I
    >>> x = Symbol('x')
    >>> p = Poly(x**2 + I)
    >>> p
    Poly(x**2 + I, x, domain='ZZ_I')
    >>> p.domain
    ZZ_I

    The :ref:`ZZ_I` domain can be used to factorise polynomials that are
    reducible over the Gaussian integers.

    >>> from sympy import factor
    >>> factor(x**2 + 1)
    x**2 + 1
    >>> factor(x**2 + 1, domain='ZZ_I')
    (x - I)*(x + I)

    The corresponding `field of fractions`_ is the domain of the Gaussian
    rationals :ref:`QQ_I`. Conversely :ref:`ZZ_I` is the `ring of integers`_
    of :ref:`QQ_I`.

    >>> from sympy import ZZ_I, QQ_I
    >>> ZZ_I.get_field()
    QQ_I
    >>> QQ_I.get_ring()
    ZZ_I

    When using the domain directly :ref:`ZZ_I` can be used as a constructor.

    >>> ZZ_I(3, 4)
    (3 + 4*I)
    >>> ZZ_I(5)
    (5 + 0*I)

    The domain elements of :ref:`ZZ_I` are instances of
    :py:class:`~.GaussianInteger` which support the rings operations
    ``+,-,*,**``.

    >>> z1 = ZZ_I(5, 1)
    >>> z2 = ZZ_I(2, 3)
    >>> z1
    (5 + 1*I)
    >>> z2
    (2 + 3*I)
    >>> z1 + z2
    (7 + 4*I)
    >>> z1 * z2
    (7 + 17*I)
    >>> z1 ** 2
    (24 + 10*I)

    Both floor (``//``) and modulo (``%``) division work with
    :py:class:`~.GaussianInteger` (see the :py:meth:`~.Domain.div` method).

    >>> z3, z4 = ZZ_I(5), ZZ_I(1, 3)
    >>> z3 // z4  # floor division
    (1 + -1*I)
    >>> z3 % z4   # modulo division (remainder)
    (1 + -2*I)
    >>> (z3//z4)*z4 + z3%z4 == z3
    True

    True division (``/``) in :ref:`ZZ_I` gives an element of :ref:`QQ_I`. The
    :py:meth:`~.Domain.exquo` method can be used to divide in :ref:`ZZ_I` when
    exact division is possible.

    >>> z1 / z2
    (1 + -1*I)
    >>> ZZ_I.exquo(z1, z2)
    (1 + -1*I)
    >>> z3 / z4
    (1/2 + -3/2*I)
    >>> ZZ_I.exquo(z3, z4)
    Traceback (most recent call last):
        ...
    ExactQuotientFailed: (1 + 3*I) does not divide (5 + 0*I) in ZZ_I

    The :py:meth:`~.Domain.gcd` method can be used to compute the `gcd`_ of any
    two elements.

    >>> ZZ_I.gcd(ZZ_I(10), ZZ_I(2))
    (2 + 0*I)
    >>> ZZ_I.gcd(ZZ_I(5), ZZ_I(2, 1))
    (2 + 1*I)

    .. _Gaussian integers: https://en.wikipedia.org/wiki/Gaussian_integer
    .. _gcd: https://en.wikipedia.org/wiki/Greatest_common_divisor

    """
    dom = ZZ
    dtype = GaussianInteger
    zero: Incomplete
    one: Incomplete
    imag_unit: Incomplete
    units: Incomplete
    rep: str
    is_GaussianRing: bool
    is_ZZ_I: bool
    def __init__(self) -> None:
        """For constructing ZZ_I."""
    def get_ring(self):
        """Returns a ring associated with ``self``. """
    def get_field(self):
        """Returns a field associated with ``self``. """
    def normalize(self, d, *args):
        """Return first quadrant element associated with ``d``.

        Also multiply the other arguments by the same power of i.
        """
    def gcd(self, a, b):
        """Greatest common divisor of a and b over ZZ_I."""
    def lcm(self, a, b):
        """Least common multiple of a and b over ZZ_I."""
    def from_GaussianIntegerRing(K1, a, K0):
        """Convert a ZZ_I element to ZZ_I."""
    def from_GaussianRationalField(K1, a, K0):
        """Convert a QQ_I element to ZZ_I."""

ZZ_I: Incomplete

class GaussianRationalField(GaussianDomain, Field):
    """Field of Gaussian rationals ``QQ_I``

    The :ref:`QQ_I` domain represents the `Gaussian rationals`_ `\\mathbb{Q}(i)`
    as a :py:class:`~.Domain` in the domain system (see
    :ref:`polys-domainsintro`).

    By default a :py:class:`~.Poly` created from an expression with
    coefficients that are combinations of rationals and ``I`` (`\\sqrt{-1}`)
    will have the domain :ref:`QQ_I`.

    >>> from sympy import Poly, Symbol, I
    >>> x = Symbol('x')
    >>> p = Poly(x**2 + I/2)
    >>> p
    Poly(x**2 + I/2, x, domain='QQ_I')
    >>> p.domain
    QQ_I

    The polys option ``gaussian=True`` can be used to specify that the domain
    should be :ref:`QQ_I` even if the coefficients do not contain ``I`` or are
    all integers.

    >>> Poly(x**2)
    Poly(x**2, x, domain='ZZ')
    >>> Poly(x**2 + I)
    Poly(x**2 + I, x, domain='ZZ_I')
    >>> Poly(x**2/2)
    Poly(1/2*x**2, x, domain='QQ')
    >>> Poly(x**2, gaussian=True)
    Poly(x**2, x, domain='QQ_I')
    >>> Poly(x**2 + I, gaussian=True)
    Poly(x**2 + I, x, domain='QQ_I')
    >>> Poly(x**2/2, gaussian=True)
    Poly(1/2*x**2, x, domain='QQ_I')

    The :ref:`QQ_I` domain can be used to factorise polynomials that are
    reducible over the Gaussian rationals.

    >>> from sympy import factor, QQ_I
    >>> factor(x**2/4 + 1)
    (x**2 + 4)/4
    >>> factor(x**2/4 + 1, domain='QQ_I')
    (x - 2*I)*(x + 2*I)/4
    >>> factor(x**2/4 + 1, domain=QQ_I)
    (x - 2*I)*(x + 2*I)/4

    It is also possible to specify the :ref:`QQ_I` domain explicitly with
    polys functions like :py:func:`~.apart`.

    >>> from sympy import apart
    >>> apart(1/(1 + x**2))
    1/(x**2 + 1)
    >>> apart(1/(1 + x**2), domain=QQ_I)
    I/(2*(x + I)) - I/(2*(x - I))

    The corresponding `ring of integers`_ is the domain of the Gaussian
    integers :ref:`ZZ_I`. Conversely :ref:`QQ_I` is the `field of fractions`_
    of :ref:`ZZ_I`.

    >>> from sympy import ZZ_I, QQ_I, QQ
    >>> ZZ_I.get_field()
    QQ_I
    >>> QQ_I.get_ring()
    ZZ_I

    When using the domain directly :ref:`QQ_I` can be used as a constructor.

    >>> QQ_I(3, 4)
    (3 + 4*I)
    >>> QQ_I(5)
    (5 + 0*I)
    >>> QQ_I(QQ(2, 3), QQ(4, 5))
    (2/3 + 4/5*I)

    The domain elements of :ref:`QQ_I` are instances of
    :py:class:`~.GaussianRational` which support the field operations
    ``+,-,*,**,/``.

    >>> z1 = QQ_I(5, 1)
    >>> z2 = QQ_I(2, QQ(1, 2))
    >>> z1
    (5 + 1*I)
    >>> z2
    (2 + 1/2*I)
    >>> z1 + z2
    (7 + 3/2*I)
    >>> z1 * z2
    (19/2 + 9/2*I)
    >>> z2 ** 2
    (15/4 + 2*I)

    True division (``/``) in :ref:`QQ_I` gives an element of :ref:`QQ_I` and
    is always exact.

    >>> z1 / z2
    (42/17 + -2/17*I)
    >>> QQ_I.exquo(z1, z2)
    (42/17 + -2/17*I)
    >>> z1 == (z1/z2)*z2
    True

    Both floor (``//``) and modulo (``%``) division can be used with
    :py:class:`~.GaussianRational` (see :py:meth:`~.Domain.div`)
    but division is always exact so there is no remainder.

    >>> z1 // z2
    (42/17 + -2/17*I)
    >>> z1 % z2
    (0 + 0*I)
    >>> QQ_I.div(z1, z2)
    ((42/17 + -2/17*I), (0 + 0*I))
    >>> (z1//z2)*z2 + z1%z2 == z1
    True

    .. _Gaussian rationals: https://en.wikipedia.org/wiki/Gaussian_rational
    """
    dom = QQ
    dtype = GaussianRational
    zero: Incomplete
    one: Incomplete
    imag_unit: Incomplete
    units: Incomplete
    rep: str
    is_GaussianField: bool
    is_QQ_I: bool
    def __init__(self) -> None:
        """For constructing QQ_I."""
    def get_ring(self):
        """Returns a ring associated with ``self``. """
    def get_field(self):
        """Returns a field associated with ``self``. """
    def as_AlgebraicField(self):
        """Get equivalent domain as an ``AlgebraicField``. """
    def numer(self, a):
        """Get the numerator of ``a``."""
    def denom(self, a):
        """Get the denominator of ``a``."""
    def from_GaussianIntegerRing(K1, a, K0):
        """Convert a ZZ_I element to QQ_I."""
    def from_GaussianRationalField(K1, a, K0):
        """Convert a QQ_I element to QQ_I."""

QQ_I: Incomplete
