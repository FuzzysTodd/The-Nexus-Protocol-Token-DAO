from _typeshed import Incomplete
from sympy.core.symbol import Dummy as Dummy
from sympy.polys.densearith import dup_add as dup_add, dup_lshift as dup_lshift, dup_mul as dup_mul, dup_mul_ground as dup_mul_ground, dup_sub as dup_sub
from sympy.polys.domains import QQ as QQ, ZZ as ZZ
from sympy.polys.polytools import named_poly as named_poly
from sympy.utilities import public as public

def dup_jacobi(n, a, b, K):
    """Low-level implementation of Jacobi polynomials."""
def jacobi_poly(n, a, b, x: Incomplete | None = None, polys: bool = False):
    """Generates the Jacobi polynomial `P_n^{(a,b)}(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    a
        Lower limit of minimal domain for the list of coefficients.
    b
        Upper limit of minimal domain for the list of coefficients.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
def dup_gegenbauer(n, a, K):
    """Low-level implementation of Gegenbauer polynomials."""
def gegenbauer_poly(n, a, x: Incomplete | None = None, polys: bool = False):
    """Generates the Gegenbauer polynomial `C_n^{(a)}(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    a
        Decides minimal domain for the list of coefficients.
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
def dup_chebyshevt(n, K):
    """Low-level implementation of Chebyshev polynomials of the first kind."""
def dup_chebyshevu(n, K):
    """Low-level implementation of Chebyshev polynomials of the second kind."""
def chebyshevt_poly(n, x: Incomplete | None = None, polys: bool = False):
    """Generates the Chebyshev polynomial of the first kind `T_n(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
def chebyshevu_poly(n, x: Incomplete | None = None, polys: bool = False):
    """Generates the Chebyshev polynomial of the second kind `U_n(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
def dup_hermite(n, K):
    """Low-level implementation of Hermite polynomials."""
def dup_hermite_prob(n, K):
    """Low-level implementation of probabilist's Hermite polynomials."""
def hermite_poly(n, x: Incomplete | None = None, polys: bool = False):
    """Generates the Hermite polynomial `H_n(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
def hermite_prob_poly(n, x: Incomplete | None = None, polys: bool = False):
    """Generates the probabilist's Hermite polynomial `He_n(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
def dup_legendre(n, K):
    """Low-level implementation of Legendre polynomials."""
def legendre_poly(n, x: Incomplete | None = None, polys: bool = False):
    """Generates the Legendre polynomial `P_n(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
def dup_laguerre(n, alpha, K):
    """Low-level implementation of Laguerre polynomials."""
def laguerre_poly(n, x: Incomplete | None = None, alpha: int = 0, polys: bool = False):
    """Generates the Laguerre polynomial `L_n^{(\\alpha)}(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    alpha : optional
        Decides minimal domain for the list of coefficients.
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
def dup_spherical_bessel_fn(n, K):
    """Low-level implementation of fn(n, x)."""
def dup_spherical_bessel_fn_minus(n, K):
    """Low-level implementation of fn(-n, x)."""
def spherical_bessel_fn(n, x: Incomplete | None = None, polys: bool = False):
    '''
    Coefficients for the spherical Bessel functions.

    These are only needed in the jn() function.

    The coefficients are calculated from:

    fn(0, z) = 1/z
    fn(1, z) = 1/z**2
    fn(n-1, z) + fn(n+1, z) == (2*n+1)/z * fn(n, z)

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.

    Examples
    ========

    >>> from sympy.polys.orthopolys import spherical_bessel_fn as fn
    >>> from sympy import Symbol
    >>> z = Symbol("z")
    >>> fn(1, z)
    z**(-2)
    >>> fn(2, z)
    -1/z + 3/z**3
    >>> fn(3, z)
    -6/z**2 + 15/z**4
    >>> fn(4, z)
    1/z - 45/z**3 + 105/z**5

    '''
