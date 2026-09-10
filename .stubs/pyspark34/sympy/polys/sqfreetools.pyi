from sympy.polys.densearith import dmp_mul_ground as dmp_mul_ground, dmp_neg as dmp_neg, dmp_quo as dmp_quo, dmp_sub as dmp_sub, dup_mul as dup_mul, dup_mul_ground as dup_mul_ground, dup_neg as dup_neg, dup_quo as dup_quo, dup_sub as dup_sub
from sympy.polys.densebasic import dmp_degree as dmp_degree, dmp_ground as dmp_ground, dmp_ground_LC as dmp_ground_LC, dmp_inject as dmp_inject, dmp_raise as dmp_raise, dmp_zero_p as dmp_zero_p, dup_LC as dup_LC, dup_convert as dup_convert, dup_degree as dup_degree, dup_strip as dup_strip
from sympy.polys.densetools import dmp_compose as dmp_compose, dmp_diff as dmp_diff, dmp_diff_in as dmp_diff_in, dmp_ground_monic as dmp_ground_monic, dmp_ground_primitive as dmp_ground_primitive, dup_diff as dup_diff, dup_monic as dup_monic, dup_primitive as dup_primitive, dup_shift as dup_shift
from sympy.polys.euclidtools import dmp_gcd as dmp_gcd, dmp_inner_gcd as dmp_inner_gcd, dmp_resultant as dmp_resultant, dup_gcd as dup_gcd, dup_inner_gcd as dup_inner_gcd
from sympy.polys.galoistools import gf_sqf_list as gf_sqf_list, gf_sqf_part as gf_sqf_part
from sympy.polys.polyerrors import DomainError as DomainError, MultivariatePolynomialError as MultivariatePolynomialError

def dup_sqf_p(f, K):
    '''
    Return ``True`` if ``f`` is a square-free polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sqf_p(x**2 - 2*x + 1)
    False
    >>> R.dup_sqf_p(x**2 - 1)
    True

    '''
def dmp_sqf_p(f, u, K):
    '''
    Return ``True`` if ``f`` is a square-free polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_sqf_p(x**2 + 2*x*y + y**2)
    False
    >>> R.dmp_sqf_p(x**2 + y**2)
    True

    '''
def dup_sqf_norm(f, K):
    '''
    Square-free norm of ``f`` in ``K[x]``, useful over algebraic domains.

    Returns ``s``, ``f``, ``r``, such that ``g(x) = f(x-sa)`` and ``r(x) = Norm(g(x))``
    is a square-free polynomial over K, where ``a`` is the algebraic extension of ``K``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> from sympy import sqrt

    >>> K = QQ.algebraic_field(sqrt(3))
    >>> R, x = ring("x", K)
    >>> _, X = ring("x", QQ)

    >>> s, f, r = R.dup_sqf_norm(x**2 - 2)

    >>> s == 1
    True
    >>> f == x**2 + K([QQ(-2), QQ(0)])*x + 1
    True
    >>> r == X**4 - 10*X**2 + 1
    True

    '''
def dmp_sqf_norm(f, u, K):
    '''
    Square-free norm of ``f`` in ``K[X]``, useful over algebraic domains.

    Returns ``s``, ``f``, ``r``, such that ``g(x) = f(x-sa)`` and ``r(x) = Norm(g(x))``
    is a square-free polynomial over K, where ``a`` is the algebraic extension of ``K``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> from sympy import I

    >>> K = QQ.algebraic_field(I)
    >>> R, x, y = ring("x,y", K)
    >>> _, X, Y = ring("x,y", QQ)

    >>> s, f, r = R.dmp_sqf_norm(x*y + y**2)

    >>> s == 1
    True
    >>> f == x*y + y**2 + K([QQ(-1), QQ(0)])*y
    True
    >>> r == X**2*Y**2 + 2*X*Y**3 + Y**4 + Y**2
    True

    '''
def dmp_norm(f, u, K):
    """
    Norm of ``f`` in ``K[X1, ..., Xn]``, often not square-free.
    """
def dup_gf_sqf_part(f, K):
    """Compute square-free part of ``f`` in ``GF(p)[x]``. """
def dmp_gf_sqf_part(f, u, K) -> None:
    """Compute square-free part of ``f`` in ``GF(p)[X]``. """
def dup_sqf_part(f, K):
    '''
    Returns square-free part of a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sqf_part(x**3 - 3*x - 2)
    x**2 - x - 2

    '''
def dmp_sqf_part(f, u, K):
    '''
    Returns square-free part of a polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_sqf_part(x**3 + 2*x**2*y + x*y**2)
    x**2 + x*y

    '''
def dup_gf_sqf_list(f, K, all: bool = False):
    """Compute square-free decomposition of ``f`` in ``GF(p)[x]``. """
def dmp_gf_sqf_list(f, u, K, all: bool = False) -> None:
    """Compute square-free decomposition of ``f`` in ``GF(p)[X]``. """
def dup_sqf_list(f, K, all: bool = False):
    '''
    Return square-free decomposition of a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> f = 2*x**5 + 16*x**4 + 50*x**3 + 76*x**2 + 56*x + 16

    >>> R.dup_sqf_list(f)
    (2, [(x + 1, 2), (x + 2, 3)])
    >>> R.dup_sqf_list(f, all=True)
    (2, [(1, 1), (x + 1, 2), (x + 2, 3)])

    '''
def dup_sqf_list_include(f, K, all: bool = False):
    '''
    Return square-free decomposition of a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> f = 2*x**5 + 16*x**4 + 50*x**3 + 76*x**2 + 56*x + 16

    >>> R.dup_sqf_list_include(f)
    [(2, 1), (x + 1, 2), (x + 2, 3)]
    >>> R.dup_sqf_list_include(f, all=True)
    [(2, 1), (x + 1, 2), (x + 2, 3)]

    '''
def dmp_sqf_list(f, u, K, all: bool = False):
    '''
    Return square-free decomposition of a polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = x**5 + 2*x**4*y + x**3*y**2

    >>> R.dmp_sqf_list(f)
    (1, [(x + y, 2), (x, 3)])
    >>> R.dmp_sqf_list(f, all=True)
    (1, [(1, 1), (x + y, 2), (x, 3)])

    '''
def dmp_sqf_list_include(f, u, K, all: bool = False):
    '''
    Return square-free decomposition of a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = x**5 + 2*x**4*y + x**3*y**2

    >>> R.dmp_sqf_list_include(f)
    [(1, 1), (x + y, 2), (x, 3)]
    >>> R.dmp_sqf_list_include(f, all=True)
    [(1, 1), (x + y, 2), (x, 3)]

    '''
def dup_gff_list(f, K):
    '''
    Compute greatest factorial factorization of ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_gff_list(x**5 + 2*x**4 - x**3 - 2*x**2)
    [(x, 1), (x + 2, 4)]

    '''
def dmp_gff_list(f, u, K):
    '''
    Compute greatest factorial factorization of ``f`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    '''
