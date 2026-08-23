from _typeshed import Incomplete
from sympy.core.numbers import mod_inverse as mod_inverse
from sympy.core.power import integer_log as integer_log
from sympy.ntheory import isprime as isprime, sieve as sieve
from sympy.utilities.misc import as_int as as_int

rgen: Incomplete

class Point:
    """Montgomery form of Points in an elliptic curve.
    In this form, the addition and doubling of points
    does not need any y-coordinate information thus
    decreasing the number of operations.
    Using Montgomery form we try to perform point addition
    and doubling in least amount of multiplications.

    The elliptic curve used here is of the form
    (E : b*y**2*z = x**3 + a*x**2*z + x*z**2).
    The a_24 parameter is equal to (a + 2)/4.

    References
    ==========

    .. [1]  https://www.hyperelliptic.org/tanja/SHARCS/talks06/Gaj.pdf
    """
    x_cord: Incomplete
    z_cord: Incomplete
    a_24: Incomplete
    mod: Incomplete
    def __init__(self, x_cord, z_cord, a_24, mod) -> None:
        """
        Initial parameters for the Point class.

        Parameters
        ==========

        x_cord : X coordinate of the Point
        z_cord : Z coordinate of the Point
        a_24 : Parameter of the elliptic curve in Montgomery form
        mod : modulus
        """
    def __eq__(self, other):
        """Two points are equal if X/Z of both points are equal
        """
    def add(self, Q, diff):
        """
        Add two points self and Q where diff = self - Q. Moreover the assumption
        is self.x_cord*Q.x_cord*(self.x_cord - Q.x_cord) != 0. This algorithm
        requires 6 multiplications. Here the difference between the points
        is already known and using this algorithm speeds up the addition
        by reducing the number of multiplication required. Also in the
        mont_ladder algorithm is constructed in a way so that the difference
        between intermediate points is always equal to the initial point.
        So, we always know what the difference between the point is.


        Parameters
        ==========

        Q : point on the curve in Montgomery form
        diff : self - Q

        Examples
        ========

        >>> from sympy.ntheory.ecm import Point
        >>> p1 = Point(11, 16, 7, 29)
        >>> p2 = Point(13, 10, 7, 29)
        >>> p3 = p2.add(p1, p1)
        >>> p3.x_cord
        23
        >>> p3.z_cord
        17
        """
    def double(self):
        """
        Doubles a point in an elliptic curve in Montgomery form.
        This algorithm requires 5 multiplications.

        Examples
        ========

        >>> from sympy.ntheory.ecm import Point
        >>> p1 = Point(11, 16, 7, 29)
        >>> p2 = p1.double()
        >>> p2.x_cord
        13
        >>> p2.z_cord
        10
        """
    def mont_ladder(self, k):
        """
        Scalar multiplication of a point in Montgomery form
        using Montgomery Ladder Algorithm.
        A total of 11 multiplications are required in each step of this
        algorithm.

        Parameters
        ==========

        k : The positive integer multiplier

        Examples
        ========

        >>> from sympy.ntheory.ecm import Point
        >>> p1 = Point(11, 16, 7, 29)
        >>> p3 = p1.mont_ladder(3)
        >>> p3.x_cord
        23
        >>> p3.z_cord
        17
        """

def ecm(n, B1: int = 10000, B2: int = 100000, max_curve: int = 200, seed: int = 1234):
    """Performs factorization using Lenstra's Elliptic curve method.

    This function repeatedly calls `ecm_one_factor` to compute the factors
    of n. First all the small factors are taken out using trial division.
    Then `ecm_one_factor` is used to compute one factor at a time.

    Parameters
    ==========

    n : Number to be Factored
    B1 : Stage 1 Bound
    B2 : Stage 2 Bound
    max_curve : Maximum number of curves generated
    seed : Initialize pseudorandom generator

    Examples
    ========

    >>> from sympy.ntheory import ecm
    >>> ecm(25645121643901801)
    {5394769, 4753701529}
    >>> ecm(9804659461513846513)
    {4641991, 2112166839943}
    """
