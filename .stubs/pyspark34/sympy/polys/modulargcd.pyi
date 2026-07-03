from sympy.core.symbol import Dummy as Dummy
from sympy.ntheory import nextprime as nextprime
from sympy.ntheory.modular import crt as crt
from sympy.polys.domains import PolynomialRing as PolynomialRing
from sympy.polys.galoistools import gf_div as gf_div, gf_from_dict as gf_from_dict, gf_gcd as gf_gcd, gf_gcdex as gf_gcdex, gf_lcm as gf_lcm
from sympy.polys.polyerrors import ModularGCDFailed as ModularGCDFailed

def modgcd_univariate(f, g):
    '''
    Computes the GCD of two polynomials in `\\mathbb{Z}[x]` using a modular
    algorithm.

    The algorithm computes the GCD of two univariate integer polynomials
    `f` and `g` by computing the GCD in `\\mathbb{Z}_p[x]` for suitable
    primes `p` and then reconstructing the coefficients with the Chinese
    Remainder Theorem. Trial division is only made for candidates which
    are very likely the desired GCD.

    Parameters
    ==========

    f : PolyElement
        univariate integer polynomial
    g : PolyElement
        univariate integer polynomial

    Returns
    =======

    h : PolyElement
        GCD of the polynomials `f` and `g`
    cff : PolyElement
        cofactor of `f`, i.e. `\\frac{f}{h}`
    cfg : PolyElement
        cofactor of `g`, i.e. `\\frac{g}{h}`

    Examples
    ========

    >>> from sympy.polys.modulargcd import modgcd_univariate
    >>> from sympy.polys import ring, ZZ

    >>> R, x = ring("x", ZZ)

    >>> f = x**5 - 1
    >>> g = x - 1

    >>> h, cff, cfg = modgcd_univariate(f, g)
    >>> h, cff, cfg
    (x - 1, x**4 + x**3 + x**2 + x + 1, 1)

    >>> cff * h == f
    True
    >>> cfg * h == g
    True

    >>> f = 6*x**2 - 6
    >>> g = 2*x**2 + 4*x + 2

    >>> h, cff, cfg = modgcd_univariate(f, g)
    >>> h, cff, cfg
    (2*x + 2, 3*x - 3, x + 1)

    >>> cff * h == f
    True
    >>> cfg * h == g
    True

    References
    ==========

    1. [Monagan00]_

    '''
def modgcd_bivariate(f, g):
    '''
    Computes the GCD of two polynomials in `\\mathbb{Z}[x, y]` using a
    modular algorithm.

    The algorithm computes the GCD of two bivariate integer polynomials
    `f` and `g` by calculating the GCD in `\\mathbb{Z}_p[x, y]` for
    suitable primes `p` and then reconstructing the coefficients with the
    Chinese Remainder Theorem. To compute the bivariate GCD over
    `\\mathbb{Z}_p`, the polynomials `f \\; \\mathrm{mod} \\, p` and
    `g \\; \\mathrm{mod} \\, p` are evaluated at `y = a` for certain
    `a \\in \\mathbb{Z}_p` and then their univariate GCD in `\\mathbb{Z}_p[x]`
    is computed. Interpolating those yields the bivariate GCD in
    `\\mathbb{Z}_p[x, y]`. To verify the result in `\\mathbb{Z}[x, y]`, trial
    division is done, but only for candidates which are very likely the
    desired GCD.

    Parameters
    ==========

    f : PolyElement
        bivariate integer polynomial
    g : PolyElement
        bivariate integer polynomial

    Returns
    =======

    h : PolyElement
        GCD of the polynomials `f` and `g`
    cff : PolyElement
        cofactor of `f`, i.e. `\\frac{f}{h}`
    cfg : PolyElement
        cofactor of `g`, i.e. `\\frac{g}{h}`

    Examples
    ========

    >>> from sympy.polys.modulargcd import modgcd_bivariate
    >>> from sympy.polys import ring, ZZ

    >>> R, x, y = ring("x, y", ZZ)

    >>> f = x**2 - y**2
    >>> g = x**2 + 2*x*y + y**2

    >>> h, cff, cfg = modgcd_bivariate(f, g)
    >>> h, cff, cfg
    (x + y, x - y, x + y)

    >>> cff * h == f
    True
    >>> cfg * h == g
    True

    >>> f = x**2*y - x**2 - 4*y + 4
    >>> g = x + 2

    >>> h, cff, cfg = modgcd_bivariate(f, g)
    >>> h, cff, cfg
    (x + 2, x*y - x - 2*y + 2, 1)

    >>> cff * h == f
    True
    >>> cfg * h == g
    True

    References
    ==========

    1. [Monagan00]_

    '''
def modgcd_multivariate(f, g):
    '''
    Compute the GCD of two polynomials in `\\mathbb{Z}[x_0, \\ldots, x_{k-1}]`
    using a modular algorithm.

    The algorithm computes the GCD of two multivariate integer polynomials
    `f` and `g` by calculating the GCD in
    `\\mathbb{Z}_p[x_0, \\ldots, x_{k-1}]` for suitable primes `p` and then
    reconstructing the coefficients with the Chinese Remainder Theorem. To
    compute the multivariate GCD over `\\mathbb{Z}_p` the recursive
    subroutine :func:`_modgcd_multivariate_p` is used. To verify the result in
    `\\mathbb{Z}[x_0, \\ldots, x_{k-1}]`, trial division is done, but only for
    candidates which are very likely the desired GCD.

    Parameters
    ==========

    f : PolyElement
        multivariate integer polynomial
    g : PolyElement
        multivariate integer polynomial

    Returns
    =======

    h : PolyElement
        GCD of the polynomials `f` and `g`
    cff : PolyElement
        cofactor of `f`, i.e. `\\frac{f}{h}`
    cfg : PolyElement
        cofactor of `g`, i.e. `\\frac{g}{h}`

    Examples
    ========

    >>> from sympy.polys.modulargcd import modgcd_multivariate
    >>> from sympy.polys import ring, ZZ

    >>> R, x, y = ring("x, y", ZZ)

    >>> f = x**2 - y**2
    >>> g = x**2 + 2*x*y + y**2

    >>> h, cff, cfg = modgcd_multivariate(f, g)
    >>> h, cff, cfg
    (x + y, x - y, x + y)

    >>> cff * h == f
    True
    >>> cfg * h == g
    True

    >>> R, x, y, z = ring("x, y, z", ZZ)

    >>> f = x*z**2 - y*z**2
    >>> g = x**2*z + z

    >>> h, cff, cfg = modgcd_multivariate(f, g)
    >>> h, cff, cfg
    (z, x*z - y*z, x**2 + 1)

    >>> cff * h == f
    True
    >>> cfg * h == g
    True

    References
    ==========

    1. [Monagan00]_
    2. [Brown71]_

    See also
    ========

    _modgcd_multivariate_p

    '''
def func_field_modgcd(f, g):
    """
    Compute the GCD of two polynomials `f` and `g` in
    `\\mathbb Q(\\alpha)[x_0, \\ldots, x_{n-1}]` using a modular algorithm.

    The algorithm first computes the primitive associate
    `\\check m_{\\alpha}(z)` of the minimal polynomial `m_{\\alpha}` in
    `\\mathbb{Z}[z]` and the primitive associates of `f` and `g` in
    `\\mathbb{Z}[x_1, \\ldots, x_{n-1}][z]/(\\check m_{\\alpha})[x_0]`. Then it
    computes the GCD in
    `\\mathbb Q(x_1, \\ldots, x_{n-1})[z]/(m_{\\alpha}(z))[x_0]`.
    This is done by calculating the GCD in
    `\\mathbb{Z}_p(x_1, \\ldots, x_{n-1})[z]/(\\check m_{\\alpha}(z))[x_0]` for
    suitable primes `p` and then reconstructing the coefficients with the
    Chinese Remainder Theorem and Rational Reconstuction. The GCD over
    `\\mathbb{Z}_p(x_1, \\ldots, x_{n-1})[z]/(\\check m_{\\alpha}(z))[x_0]` is
    computed with a recursive subroutine, which evaluates the polynomials at
    `x_{n-1} = a` for suitable evaluation points `a \\in \\mathbb Z_p` and
    then calls itself recursively until the ground domain does no longer
    contain any parameters. For
    `\\mathbb{Z}_p[z]/(\\check m_{\\alpha}(z))[x_0]` the Euclidean Algorithm is
    used. The results of those recursive calls are then interpolated and
    Rational Function Reconstruction is used to obtain the correct
    coefficients. The results, both in
    `\\mathbb Q(x_1, \\ldots, x_{n-1})[z]/(m_{\\alpha}(z))[x_0]` and
    `\\mathbb{Z}_p(x_1, \\ldots, x_{n-1})[z]/(\\check m_{\\alpha}(z))[x_0]`, are
    verified by a fraction free trial division.

    Apart from the above GCD computation some GCDs in
    `\\mathbb Q(\\alpha)[x_1, \\ldots, x_{n-1}]` have to be calculated,
    because treating the polynomials as univariate ones can result in
    a spurious content of the GCD. For this ``func_field_modgcd`` is
    called recursively.

    Parameters
    ==========

    f, g : PolyElement
        polynomials in `\\mathbb Q(\\alpha)[x_0, \\ldots, x_{n-1}]`

    Returns
    =======

    h : PolyElement
        monic GCD of the polynomials `f` and `g`
    cff : PolyElement
        cofactor of `f`, i.e. `\\frac f h`
    cfg : PolyElement
        cofactor of `g`, i.e. `\\frac g h`

    Examples
    ========

    >>> from sympy.polys.modulargcd import func_field_modgcd
    >>> from sympy.polys import AlgebraicField, QQ, ring
    >>> from sympy import sqrt

    >>> A = AlgebraicField(QQ, sqrt(2))
    >>> R, x = ring('x', A)

    >>> f = x**2 - 2
    >>> g = x + sqrt(2)

    >>> h, cff, cfg = func_field_modgcd(f, g)

    >>> h == x + sqrt(2)
    True
    >>> cff * h == f
    True
    >>> cfg * h == g
    True

    >>> R, x, y = ring('x, y', A)

    >>> f = x**2 + 2*sqrt(2)*x*y + 2*y**2
    >>> g = x + sqrt(2)*y

    >>> h, cff, cfg = func_field_modgcd(f, g)

    >>> h == x + sqrt(2)*y
    True
    >>> cff * h == f
    True
    >>> cfg * h == g
    True

    >>> f = x + sqrt(2)*y
    >>> g = x + y

    >>> h, cff, cfg = func_field_modgcd(f, g)

    >>> h == R.one
    True
    >>> cff * h == f
    True
    >>> cfg * h == g
    True

    References
    ==========

    1. [Hoeij04]_

    """
