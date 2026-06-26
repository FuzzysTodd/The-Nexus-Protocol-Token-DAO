from .factor_ import divisors as divisors
from .residue_ntheory import polynomial_congruence as polynomial_congruence
from _typeshed import Incomplete
from sympy.core.numbers import oo as oo
from sympy.core.relational import Eq as Eq
from sympy.core.symbol import symbols as symbols
from sympy.polys.domains import FF as FF, FiniteField as FiniteField, QQ as QQ, RationalField as RationalField
from sympy.solvers.solvers import solve as solve
from sympy.utilities.iterables import is_sequence as is_sequence
from sympy.utilities.misc import as_int as as_int

class EllipticCurve:
    '''
    Create the following Elliptic Curve over domain.

    `y^{2} + a_{1} x y + a_{3} y = x^{3} + a_{2} x^{2} + a_{4} x + a_{6}`

    The default domain is ``QQ``. If no coefficient ``a1``, ``a2``, ``a3``,
    it create curve as following form.

    `y^{2} = x^{3} + a_{4} x + a_{6}`

    Examples
    ========

    References
    ==========

    .. [1] J. Silverman "A Friendly Introduction to Number Theory" Third Edition
    .. [2] https://mathworld.wolfram.com/EllipticDiscriminant.html
    .. [3] G. Hardy, E. Wright "An Introduction to the Theory of Numbers" Sixth Edition

    '''
    modulus: Incomplete
    def __init__(self, a4, a6, a1: int = 0, a2: int = 0, a3: int = 0, modulus: int = 0) -> None: ...
    def __call__(self, x, y, z: int = 1): ...
    def __contains__(self, point) -> bool: ...
    def minimal(self):
        """
        Return minimal Weierstrass equation.

        Examples
        ========

        >>> from sympy.ntheory.elliptic_curve import EllipticCurve

        >>> e1 = EllipticCurve(-10, -20, 0, -1, 1)
        >>> e1.minimal()
        E(QQ): Eq(y**2*z, x**3 - 13392*x*z**2 - 1080432*z**3)

        """
    def points(self):
        """
        Return points of curve over Finite Field.

        Examples
        ========

        >>> from sympy.ntheory.elliptic_curve import EllipticCurve
        >>> e2 = EllipticCurve(1, 1, 1, 1, 1, modulus=5)
        >>> e2.points()
        {(0, 2), (1, 4), (2, 0), (2, 2), (3, 0), (3, 1), (4, 0)}

        """
    def points_x(self, x):
        """Returns points on with curve where xcoordinate = x"""
    def torsion_points(self):
        """
        Return torsion points of curve over Rational number.

        Return point objects those are finite order.
        According to Nagell-Lutz theorem, torsion point p(x, y)
        x and y are integers, either y = 0 or y**2 is divisor
        of discriminent. According to Mazur's theorem, there are
        at most 15 points in torsion collection.

        Examples
        ========

        >>> from sympy.ntheory.elliptic_curve import EllipticCurve
        >>> e2 = EllipticCurve(-43, 166)
        >>> sorted(e2.torsion_points())
        [(-5, -16), (-5, 16), O, (3, -8), (3, 8), (11, -32), (11, 32)]

        """
    @property
    def characteristic(self):
        """
        Return domain characteristic.

        Examples
        ========

        >>> from sympy.ntheory.elliptic_curve import EllipticCurve
        >>> e2 = EllipticCurve(-43, 166)
        >>> e2.characteristic
        0

        """
    @property
    def discriminant(self):
        """
        Return curve discriminant.

        Examples
        ========

        >>> from sympy.ntheory.elliptic_curve import EllipticCurve
        >>> e2 = EllipticCurve(0, 17)
        >>> e2.discriminant
        -124848

        """
    @property
    def is_singular(self):
        """
        Return True if curve discriminant is equal to zero.
        """
    @property
    def j_invariant(self):
        """
        Return curve j-invariant.

        Examples
        ========

        >>> from sympy.ntheory.elliptic_curve import EllipticCurve
        >>> e1 = EllipticCurve(-2, 0, 0, 1, 1)
        >>> e1.j_invariant
        1404928/389

        """
    @property
    def order(self):
        """
        Number of points in Finite field.

        Examples
        ========

        >>> from sympy.ntheory.elliptic_curve import EllipticCurve
        >>> e2 = EllipticCurve(1, 0, modulus=19)
        >>> e2.order
        19

        """
    @property
    def rank(self):
        """
        Number of independent points of infinite order.

        For Finite field, it must be 0.
        """

class EllipticCurvePoint:
    """
    Point of Elliptic Curve

    Examples
    ========

    >>> from sympy.ntheory.elliptic_curve import EllipticCurve
    >>> e1 = EllipticCurve(-17, 16)
    >>> p1 = e1(0, -4, 1)
    >>> p2 = e1(1, 0)
    >>> p1 + p2
    (15, -56)
    >>> e3 = EllipticCurve(-1, 9)
    >>> e3(1, -3) * 3
    (664/169, 17811/2197)
    >>> (e3(1, -3) * 3).order()
    oo
    >>> e2 = EllipticCurve(-2, 0, 0, 1, 1)
    >>> p = e2(-1,1)
    >>> q = e2(0, -1)
    >>> p+q
    (4, 8)
    >>> p-q
    (1, 0)
    >>> 3*p-5*q
    (328/361, -2800/6859)
    """
    @staticmethod
    def point_at_infinity(curve): ...
    x: Incomplete
    y: Incomplete
    z: Incomplete
    def __init__(self, x, y, z, curve) -> None: ...
    def __add__(self, p): ...
    def __lt__(self, other): ...
    def __mul__(self, n): ...
    def __rmul__(self, n): ...
    def __neg__(self): ...
    def __sub__(self, other): ...
    def order(self):
        """
        Return point order n where nP = 0.

        """
