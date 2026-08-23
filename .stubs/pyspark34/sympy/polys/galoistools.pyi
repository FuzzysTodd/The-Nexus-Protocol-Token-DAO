from _typeshed import Incomplete
from sympy.core.random import uniform as uniform
from sympy.external.gmpy import SYMPY_INTS as SYMPY_INTS
from sympy.polys.polyconfig import query as query
from sympy.polys.polyerrors import ExactQuotientFailed as ExactQuotientFailed

def gf_crt(U, M, K: Incomplete | None = None):
    """
    Chinese Remainder Theorem.

    Given a set of integer residues ``u_0,...,u_n`` and a set of
    co-prime integer moduli ``m_0,...,m_n``, returns an integer
    ``u``, such that ``u = u_i mod m_i`` for ``i = ``0,...,n``.

    Examples
    ========

    Consider a set of residues ``U = [49, 76, 65]``
    and a set of moduli ``M = [99, 97, 95]``. Then we have::

       >>> from sympy.polys.domains import ZZ
       >>> from sympy.polys.galoistools import gf_crt

       >>> gf_crt([49, 76, 65], [99, 97, 95], ZZ)
       639985

    This is the correct result because::

       >>> [639985 % m for m in [99, 97, 95]]
       [49, 76, 65]

    Note: this is a low-level routine with no error checking.

    See Also
    ========

    sympy.ntheory.modular.crt : a higher level crt routine
    sympy.ntheory.modular.solve_congruence

    """
def gf_crt1(M, K):
    """
    First part of the Chinese Remainder Theorem.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_crt1

    >>> gf_crt1([99, 97, 95], ZZ)
    (912285, [9215, 9405, 9603], [62, 24, 12])

    """
def gf_crt2(U, M, p, E, S, K):
    """
    Second part of the Chinese Remainder Theorem.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_crt2

    >>> U = [49, 76, 65]
    >>> M = [99, 97, 95]
    >>> p = 912285
    >>> E = [9215, 9405, 9603]
    >>> S = [62, 24, 12]

    >>> gf_crt2(U, M, p, E, S, ZZ)
    639985

    """
def gf_int(a, p):
    """
    Coerce ``a mod p`` to an integer in the range ``[-p/2, p/2]``.

    Examples
    ========

    >>> from sympy.polys.galoistools import gf_int

    >>> gf_int(2, 7)
    2
    >>> gf_int(5, 7)
    -2

    """
def gf_degree(f):
    """
    Return the leading degree of ``f``.

    Examples
    ========

    >>> from sympy.polys.galoistools import gf_degree

    >>> gf_degree([1, 1, 2, 0])
    3
    >>> gf_degree([])
    -1

    """
def gf_LC(f, K):
    """
    Return the leading coefficient of ``f``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_LC

    >>> gf_LC([3, 0, 1], ZZ)
    3

    """
def gf_TC(f, K):
    """
    Return the trailing coefficient of ``f``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_TC

    >>> gf_TC([3, 0, 1], ZZ)
    1

    """
def gf_strip(f):
    """
    Remove leading zeros from ``f``.


    Examples
    ========

    >>> from sympy.polys.galoistools import gf_strip

    >>> gf_strip([0, 0, 0, 3, 0, 1])
    [3, 0, 1]

    """
def gf_trunc(f, p):
    """
    Reduce all coefficients modulo ``p``.

    Examples
    ========

    >>> from sympy.polys.galoistools import gf_trunc

    >>> gf_trunc([7, -2, 3], 5)
    [2, 3, 3]

    """
def gf_normal(f, p, K):
    """
    Normalize all coefficients in ``K``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_normal

    >>> gf_normal([5, 10, 21, -3], 5, ZZ)
    [1, 2]

    """
def gf_from_dict(f, p, K):
    """
    Create a ``GF(p)[x]`` polynomial from a dict.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_from_dict

    >>> gf_from_dict({10: ZZ(4), 4: ZZ(33), 0: ZZ(-1)}, 5, ZZ)
    [4, 0, 0, 0, 0, 0, 3, 0, 0, 0, 4]

    """
def gf_to_dict(f, p, symmetric: bool = True):
    """
    Convert a ``GF(p)[x]`` polynomial to a dict.

    Examples
    ========

    >>> from sympy.polys.galoistools import gf_to_dict

    >>> gf_to_dict([4, 0, 0, 0, 0, 0, 3, 0, 0, 0, 4], 5)
    {0: -1, 4: -2, 10: -1}
    >>> gf_to_dict([4, 0, 0, 0, 0, 0, 3, 0, 0, 0, 4], 5, symmetric=False)
    {0: 4, 4: 3, 10: 4}

    """
def gf_from_int_poly(f, p):
    """
    Create a ``GF(p)[x]`` polynomial from ``Z[x]``.

    Examples
    ========

    >>> from sympy.polys.galoistools import gf_from_int_poly

    >>> gf_from_int_poly([7, -2, 3], 5)
    [2, 3, 3]

    """
def gf_to_int_poly(f, p, symmetric: bool = True):
    """
    Convert a ``GF(p)[x]`` polynomial to ``Z[x]``.


    Examples
    ========

    >>> from sympy.polys.galoistools import gf_to_int_poly

    >>> gf_to_int_poly([2, 3, 3], 5)
    [2, -2, -2]
    >>> gf_to_int_poly([2, 3, 3], 5, symmetric=False)
    [2, 3, 3]

    """
def gf_neg(f, p, K):
    """
    Negate a polynomial in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_neg

    >>> gf_neg([3, 2, 1, 0], 5, ZZ)
    [2, 3, 4, 0]

    """
def gf_add_ground(f, a, p, K):
    """
    Compute ``f + a`` where ``f`` in ``GF(p)[x]`` and ``a`` in ``GF(p)``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_add_ground

    >>> gf_add_ground([3, 2, 4], 2, 5, ZZ)
    [3, 2, 1]

    """
def gf_sub_ground(f, a, p, K):
    """
    Compute ``f - a`` where ``f`` in ``GF(p)[x]`` and ``a`` in ``GF(p)``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_sub_ground

    >>> gf_sub_ground([3, 2, 4], 2, 5, ZZ)
    [3, 2, 2]

    """
def gf_mul_ground(f, a, p, K):
    """
    Compute ``f * a`` where ``f`` in ``GF(p)[x]`` and ``a`` in ``GF(p)``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_mul_ground

    >>> gf_mul_ground([3, 2, 4], 2, 5, ZZ)
    [1, 4, 3]

    """
def gf_quo_ground(f, a, p, K):
    """
    Compute ``f/a`` where ``f`` in ``GF(p)[x]`` and ``a`` in ``GF(p)``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_quo_ground

    >>> gf_quo_ground(ZZ.map([3, 2, 4]), ZZ(2), 5, ZZ)
    [4, 1, 2]

    """
def gf_add(f, g, p, K):
    """
    Add polynomials in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_add

    >>> gf_add([3, 2, 4], [2, 2, 2], 5, ZZ)
    [4, 1]

    """
def gf_sub(f, g, p, K):
    """
    Subtract polynomials in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_sub

    >>> gf_sub([3, 2, 4], [2, 2, 2], 5, ZZ)
    [1, 0, 2]

    """
def gf_mul(f, g, p, K):
    """
    Multiply polynomials in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_mul

    >>> gf_mul([3, 2, 4], [2, 2, 2], 5, ZZ)
    [1, 0, 3, 2, 3]

    """
def gf_sqr(f, p, K):
    """
    Square polynomials in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_sqr

    >>> gf_sqr([3, 2, 4], 5, ZZ)
    [4, 2, 3, 1, 1]

    """
def gf_add_mul(f, g, h, p, K):
    """
    Returns ``f + g*h`` where ``f``, ``g``, ``h`` in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_add_mul
    >>> gf_add_mul([3, 2, 4], [2, 2, 2], [1, 4], 5, ZZ)
    [2, 3, 2, 2]
    """
def gf_sub_mul(f, g, h, p, K):
    """
    Compute ``f - g*h`` where ``f``, ``g``, ``h`` in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_sub_mul

    >>> gf_sub_mul([3, 2, 4], [2, 2, 2], [1, 4], 5, ZZ)
    [3, 3, 2, 1]

    """
def gf_expand(F, p, K):
    """
    Expand results of :func:`~.factor` in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_expand

    >>> gf_expand([([3, 2, 4], 1), ([2, 2], 2), ([3, 1], 3)], 5, ZZ)
    [4, 3, 0, 3, 0, 1, 4, 1]

    """
def gf_div(f, g, p, K):
    """
    Division with remainder in ``GF(p)[x]``.

    Given univariate polynomials ``f`` and ``g`` with coefficients in a
    finite field with ``p`` elements, returns polynomials ``q`` and ``r``
    (quotient and remainder) such that ``f = q*g + r``.

    Consider polynomials ``x**3 + x + 1`` and ``x**2 + x`` in GF(2)::

       >>> from sympy.polys.domains import ZZ
       >>> from sympy.polys.galoistools import gf_div, gf_add_mul

       >>> gf_div(ZZ.map([1, 0, 1, 1]), ZZ.map([1, 1, 0]), 2, ZZ)
       ([1, 1], [1])

    As result we obtained quotient ``x + 1`` and remainder ``1``, thus::

       >>> gf_add_mul(ZZ.map([1]), ZZ.map([1, 1]), ZZ.map([1, 1, 0]), 2, ZZ)
       [1, 0, 1, 1]

    References
    ==========

    .. [1] [Monagan93]_
    .. [2] [Gathen99]_

    """
def gf_rem(f, g, p, K):
    """
    Compute polynomial remainder in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_rem

    >>> gf_rem(ZZ.map([1, 0, 1, 1]), ZZ.map([1, 1, 0]), 2, ZZ)
    [1]

    """
def gf_quo(f, g, p, K):
    """
    Compute exact quotient in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_quo

    >>> gf_quo(ZZ.map([1, 0, 1, 1]), ZZ.map([1, 1, 0]), 2, ZZ)
    [1, 1]
    >>> gf_quo(ZZ.map([1, 0, 3, 2, 3]), ZZ.map([2, 2, 2]), 5, ZZ)
    [3, 2, 4]

    """
def gf_exquo(f, g, p, K):
    """
    Compute polynomial quotient in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_exquo

    >>> gf_exquo(ZZ.map([1, 0, 3, 2, 3]), ZZ.map([2, 2, 2]), 5, ZZ)
    [3, 2, 4]

    >>> gf_exquo(ZZ.map([1, 0, 1, 1]), ZZ.map([1, 1, 0]), 2, ZZ)
    Traceback (most recent call last):
    ...
    ExactQuotientFailed: [1, 1, 0] does not divide [1, 0, 1, 1]

    """
def gf_lshift(f, n, K):
    """
    Efficiently multiply ``f`` by ``x**n``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_lshift

    >>> gf_lshift([3, 2, 4], 4, ZZ)
    [3, 2, 4, 0, 0, 0, 0]

    """
def gf_rshift(f, n, K):
    """
    Efficiently divide ``f`` by ``x**n``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_rshift

    >>> gf_rshift([1, 2, 3, 4, 0], 3, ZZ)
    ([1, 2], [3, 4, 0])

    """
def gf_pow(f, n, p, K):
    """
    Compute ``f**n`` in ``GF(p)[x]`` using repeated squaring.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_pow

    >>> gf_pow([3, 2, 4], 3, 5, ZZ)
    [2, 4, 4, 2, 2, 1, 4]

    """
def gf_frobenius_monomial_base(g, p, K):
    """
    return the list of ``x**(i*p) mod g in Z_p`` for ``i = 0, .., n - 1``
    where ``n = gf_degree(g)``

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_frobenius_monomial_base
    >>> g = ZZ.map([1, 0, 2, 1])
    >>> gf_frobenius_monomial_base(g, 5, ZZ)
    [[1], [4, 4, 2], [1, 2]]

    """
def gf_frobenius_map(f, g, b, p, K):
    """
    compute gf_pow_mod(f, p, g, p, K) using the Frobenius map

    Parameters
    ==========

    f, g : polynomials in ``GF(p)[x]``
    b : frobenius monomial base
    p : prime number
    K : domain

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_frobenius_monomial_base, gf_frobenius_map
    >>> f = ZZ.map([2, 1, 0, 1])
    >>> g = ZZ.map([1, 0, 2, 1])
    >>> p = 5
    >>> b = gf_frobenius_monomial_base(g, p, ZZ)
    >>> r = gf_frobenius_map(f, g, b, p, ZZ)
    >>> gf_frobenius_map(f, g, b, p, ZZ)
    [4, 0, 3]
    """
def gf_pow_mod(f, n, g, p, K):
    """
    Compute ``f**n`` in ``GF(p)[x]/(g)`` using repeated squaring.

    Given polynomials ``f`` and ``g`` in ``GF(p)[x]`` and a non-negative
    integer ``n``, efficiently computes ``f**n (mod g)`` i.e. the remainder
    of ``f**n`` from division by ``g``, using the repeated squaring algorithm.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_pow_mod

    >>> gf_pow_mod(ZZ.map([3, 2, 4]), 3, ZZ.map([1, 1]), 5, ZZ)
    []

    References
    ==========

    .. [1] [Gathen99]_

    """
def gf_gcd(f, g, p, K):
    """
    Euclidean Algorithm in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_gcd

    >>> gf_gcd(ZZ.map([3, 2, 4]), ZZ.map([2, 2, 3]), 5, ZZ)
    [1, 3]

    """
def gf_lcm(f, g, p, K):
    """
    Compute polynomial LCM in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_lcm

    >>> gf_lcm(ZZ.map([3, 2, 4]), ZZ.map([2, 2, 3]), 5, ZZ)
    [1, 2, 0, 4]

    """
def gf_cofactors(f, g, p, K):
    """
    Compute polynomial GCD and cofactors in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_cofactors

    >>> gf_cofactors(ZZ.map([3, 2, 4]), ZZ.map([2, 2, 3]), 5, ZZ)
    ([1, 3], [3, 3], [2, 1])

    """
def gf_gcdex(f, g, p, K):
    """
    Extended Euclidean Algorithm in ``GF(p)[x]``.

    Given polynomials ``f`` and ``g`` in ``GF(p)[x]``, computes polynomials
    ``s``, ``t`` and ``h``, such that ``h = gcd(f, g)`` and ``s*f + t*g = h``.
    The typical application of EEA is solving polynomial diophantine equations.

    Consider polynomials ``f = (x + 7) (x + 1)``, ``g = (x + 7) (x**2 + 1)``
    in ``GF(11)[x]``. Application of Extended Euclidean Algorithm gives::

       >>> from sympy.polys.domains import ZZ
       >>> from sympy.polys.galoistools import gf_gcdex, gf_mul, gf_add

       >>> s, t, g = gf_gcdex(ZZ.map([1, 8, 7]), ZZ.map([1, 7, 1, 7]), 11, ZZ)
       >>> s, t, g
       ([5, 6], [6], [1, 7])

    As result we obtained polynomials ``s = 5*x + 6`` and ``t = 6``, and
    additionally ``gcd(f, g) = x + 7``. This is correct because::

       >>> S = gf_mul(s, ZZ.map([1, 8, 7]), 11, ZZ)
       >>> T = gf_mul(t, ZZ.map([1, 7, 1, 7]), 11, ZZ)

       >>> gf_add(S, T, 11, ZZ) == [1, 7]
       True

    References
    ==========

    .. [1] [Gathen99]_

    """
def gf_monic(f, p, K):
    """
    Compute LC and a monic polynomial in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_monic

    >>> gf_monic(ZZ.map([3, 2, 4]), 5, ZZ)
    (3, [1, 4, 3])

    """
def gf_diff(f, p, K):
    """
    Differentiate polynomial in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_diff

    >>> gf_diff([3, 2, 4], 5, ZZ)
    [1, 2]

    """
def gf_eval(f, a, p, K):
    """
    Evaluate ``f(a)`` in ``GF(p)`` using Horner scheme.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_eval

    >>> gf_eval([3, 2, 4], 2, 5, ZZ)
    0

    """
def gf_multi_eval(f, A, p, K):
    """
    Evaluate ``f(a)`` for ``a`` in ``[a_1, ..., a_n]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_multi_eval

    >>> gf_multi_eval([3, 2, 4], [0, 1, 2, 3, 4], 5, ZZ)
    [4, 4, 0, 2, 0]

    """
def gf_compose(f, g, p, K):
    """
    Compute polynomial composition ``f(g)`` in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_compose

    >>> gf_compose([3, 2, 4], [2, 2, 2], 5, ZZ)
    [2, 4, 0, 3, 0]

    """
def gf_compose_mod(g, h, f, p, K):
    """
    Compute polynomial composition ``g(h)`` in ``GF(p)[x]/(f)``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_compose_mod

    >>> gf_compose_mod(ZZ.map([3, 2, 4]), ZZ.map([2, 2, 2]), ZZ.map([4, 3]), 5, ZZ)
    [4]

    """
def gf_trace_map(a, b, c, n, f, p, K):
    """
    Compute polynomial trace map in ``GF(p)[x]/(f)``.

    Given a polynomial ``f`` in ``GF(p)[x]``, polynomials ``a``, ``b``,
    ``c`` in the quotient ring ``GF(p)[x]/(f)`` such that ``b = c**t
    (mod f)`` for some positive power ``t`` of ``p``, and a positive
    integer ``n``, returns a mapping::

       a -> a**t**n, a + a**t + a**t**2 + ... + a**t**n (mod f)

    In factorization context, ``b = x**p mod f`` and ``c = x mod f``.
    This way we can efficiently compute trace polynomials in equal
    degree factorization routine, much faster than with other methods,
    like iterated Frobenius algorithm, for large degrees.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_trace_map

    >>> gf_trace_map([1, 2], [4, 4], [1, 1], 4, [3, 2, 4], 5, ZZ)
    ([1, 3], [1, 3])

    References
    ==========

    .. [1] [Gathen92]_

    """
def gf_random(n, p, K):
    """
    Generate a random polynomial in ``GF(p)[x]`` of degree ``n``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_random
    >>> gf_random(10, 5, ZZ) #doctest: +SKIP
    [1, 2, 3, 2, 1, 1, 1, 2, 0, 4, 2]

    """
def gf_irreducible(n, p, K):
    """
    Generate random irreducible polynomial of degree ``n`` in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_irreducible
    >>> gf_irreducible(10, 5, ZZ) #doctest: +SKIP
    [1, 4, 2, 2, 3, 2, 4, 1, 4, 0, 4]

    """
def gf_irred_p_ben_or(f, p, K):
    """
    Ben-Or's polynomial irreducibility test over finite fields.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_irred_p_ben_or

    >>> gf_irred_p_ben_or(ZZ.map([1, 4, 2, 2, 3, 2, 4, 1, 4, 0, 4]), 5, ZZ)
    True
    >>> gf_irred_p_ben_or(ZZ.map([3, 2, 4]), 5, ZZ)
    False

    """
def gf_irred_p_rabin(f, p, K):
    """
    Rabin's polynomial irreducibility test over finite fields.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_irred_p_rabin

    >>> gf_irred_p_rabin(ZZ.map([1, 4, 2, 2, 3, 2, 4, 1, 4, 0, 4]), 5, ZZ)
    True
    >>> gf_irred_p_rabin(ZZ.map([3, 2, 4]), 5, ZZ)
    False

    """
def gf_irreducible_p(f, p, K):
    """
    Test irreducibility of a polynomial ``f`` in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_irreducible_p

    >>> gf_irreducible_p(ZZ.map([1, 4, 2, 2, 3, 2, 4, 1, 4, 0, 4]), 5, ZZ)
    True
    >>> gf_irreducible_p(ZZ.map([3, 2, 4]), 5, ZZ)
    False

    """
def gf_sqf_p(f, p, K):
    """
    Return ``True`` if ``f`` is square-free in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_sqf_p

    >>> gf_sqf_p(ZZ.map([3, 2, 4]), 5, ZZ)
    True
    >>> gf_sqf_p(ZZ.map([2, 4, 4, 2, 2, 1, 4]), 5, ZZ)
    False

    """
def gf_sqf_part(f, p, K):
    """
    Return square-free part of a ``GF(p)[x]`` polynomial.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_sqf_part

    >>> gf_sqf_part(ZZ.map([1, 1, 3, 0, 1, 0, 2, 2, 1]), 5, ZZ)
    [1, 4, 3]

    """
def gf_sqf_list(f, p, K, all: bool = False):
    """
    Return the square-free decomposition of a ``GF(p)[x]`` polynomial.

    Given a polynomial ``f`` in ``GF(p)[x]``, returns the leading coefficient
    of ``f`` and a square-free decomposition ``f_1**e_1 f_2**e_2 ... f_k**e_k``
    such that all ``f_i`` are monic polynomials and ``(f_i, f_j)`` for ``i != j``
    are co-prime and ``e_1 ... e_k`` are given in increasing order. All trivial
    terms (i.e. ``f_i = 1``) are not included in the output.

    Consider polynomial ``f = x**11 + 1`` over ``GF(11)[x]``::

       >>> from sympy.polys.domains import ZZ

       >>> from sympy.polys.galoistools import (
       ...     gf_from_dict, gf_diff, gf_sqf_list, gf_pow,
       ... )
       ... # doctest: +NORMALIZE_WHITESPACE

       >>> f = gf_from_dict({11: ZZ(1), 0: ZZ(1)}, 11, ZZ)

    Note that ``f'(x) = 0``::

       >>> gf_diff(f, 11, ZZ)
       []

    This phenomenon does not happen in characteristic zero. However we can
    still compute square-free decomposition of ``f`` using ``gf_sqf()``::

       >>> gf_sqf_list(f, 11, ZZ)
       (1, [([1, 1], 11)])

    We obtained factorization ``f = (x + 1)**11``. This is correct because::

       >>> gf_pow([1, 1], 11, 11, ZZ) == f
       True

    References
    ==========

    .. [1] [Geddes92]_

    """
def gf_Qmatrix(f, p, K):
    """
    Calculate Berlekamp's ``Q`` matrix.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_Qmatrix

    >>> gf_Qmatrix([3, 2, 4], 5, ZZ)
    [[1, 0],
     [3, 4]]

    >>> gf_Qmatrix([1, 0, 0, 0, 1], 5, ZZ)
    [[1, 0, 0, 0],
     [0, 4, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 4]]

    """
def gf_Qbasis(Q, p, K):
    """
    Compute a basis of the kernel of ``Q``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_Qmatrix, gf_Qbasis

    >>> gf_Qbasis(gf_Qmatrix([1, 0, 0, 0, 1], 5, ZZ), 5, ZZ)
    [[1, 0, 0, 0], [0, 0, 1, 0]]

    >>> gf_Qbasis(gf_Qmatrix([3, 2, 4], 5, ZZ), 5, ZZ)
    [[1, 0]]

    """
def gf_berlekamp(f, p, K):
    """
    Factor a square-free ``f`` in ``GF(p)[x]`` for small ``p``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_berlekamp

    >>> gf_berlekamp([1, 0, 0, 0, 1], 5, ZZ)
    [[1, 0, 2], [1, 0, 3]]

    """
def gf_ddf_zassenhaus(f, p, K):
    """
    Cantor-Zassenhaus: Deterministic Distinct Degree Factorization

    Given a monic square-free polynomial ``f`` in ``GF(p)[x]``, computes
    partial distinct degree factorization ``f_1 ... f_d`` of ``f`` where
    ``deg(f_i) != deg(f_j)`` for ``i != j``. The result is returned as a
    list of pairs ``(f_i, e_i)`` where ``deg(f_i) > 0`` and ``e_i > 0``
    is an argument to the equal degree factorization routine.

    Consider the polynomial ``x**15 - 1`` in ``GF(11)[x]``::

       >>> from sympy.polys.domains import ZZ
       >>> from sympy.polys.galoistools import gf_from_dict

       >>> f = gf_from_dict({15: ZZ(1), 0: ZZ(-1)}, 11, ZZ)

    Distinct degree factorization gives::

       >>> from sympy.polys.galoistools import gf_ddf_zassenhaus

       >>> gf_ddf_zassenhaus(f, 11, ZZ)
       [([1, 0, 0, 0, 0, 10], 1), ([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], 2)]

    which means ``x**15 - 1 = (x**5 - 1) (x**10 + x**5 + 1)``. To obtain
    factorization into irreducibles, use equal degree factorization
    procedure (EDF) with each of the factors.

    References
    ==========

    .. [1] [Gathen99]_
    .. [2] [Geddes92]_

    """
def gf_edf_zassenhaus(f, n, p, K):
    """
    Cantor-Zassenhaus: Probabilistic Equal Degree Factorization

    Given a monic square-free polynomial ``f`` in ``GF(p)[x]`` and
    an integer ``n``, such that ``n`` divides ``deg(f)``, returns all
    irreducible factors ``f_1,...,f_d`` of ``f``, each of degree ``n``.
    EDF procedure gives complete factorization over Galois fields.

    Consider the square-free polynomial ``f = x**3 + x**2 + x + 1`` in
    ``GF(5)[x]``. Let's compute its irreducible factors of degree one::

       >>> from sympy.polys.domains import ZZ
       >>> from sympy.polys.galoistools import gf_edf_zassenhaus

       >>> gf_edf_zassenhaus([1,1,1,1], 1, 5, ZZ)
       [[1, 1], [1, 2], [1, 3]]

    Notes
    =====

    The case p == 2 is handled by Cohen's Algorithm 3.4.8. The case p odd is
    as in Geddes Algorithm 8.9 (or Cohen's Algorithm 3.4.6).

    References
    ==========

    .. [1] [Gathen99]_
    .. [2] [Geddes92]_ Algorithm 8.9
    .. [3] [Cohen93]_ Algorithm 3.4.8

    """
def gf_ddf_shoup(f, p, K):
    """
    Kaltofen-Shoup: Deterministic Distinct Degree Factorization

    Given a monic square-free polynomial ``f`` in ``GF(p)[x]``, computes
    partial distinct degree factorization ``f_1,...,f_d`` of ``f`` where
    ``deg(f_i) != deg(f_j)`` for ``i != j``. The result is returned as a
    list of pairs ``(f_i, e_i)`` where ``deg(f_i) > 0`` and ``e_i > 0``
    is an argument to the equal degree factorization routine.

    This algorithm is an improved version of Zassenhaus algorithm for
    large ``deg(f)`` and modulus ``p`` (especially for ``deg(f) ~ lg(p)``).

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_ddf_shoup, gf_from_dict

    >>> f = gf_from_dict({6: ZZ(1), 5: ZZ(-1), 4: ZZ(1), 3: ZZ(1), 1: ZZ(-1)}, 3, ZZ)

    >>> gf_ddf_shoup(f, 3, ZZ)
    [([1, 1, 0], 1), ([1, 1, 0, 1, 2], 2)]

    References
    ==========

    .. [1] [Kaltofen98]_
    .. [2] [Shoup95]_
    .. [3] [Gathen92]_

    """
def gf_edf_shoup(f, n, p, K):
    """
    Gathen-Shoup: Probabilistic Equal Degree Factorization

    Given a monic square-free polynomial ``f`` in ``GF(p)[x]`` and integer
    ``n`` such that ``n`` divides ``deg(f)``, returns all irreducible factors
    ``f_1,...,f_d`` of ``f``, each of degree ``n``. This is a complete
    factorization over Galois fields.

    This algorithm is an improved version of Zassenhaus algorithm for
    large ``deg(f)`` and modulus ``p`` (especially for ``deg(f) ~ lg(p)``).

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_edf_shoup

    >>> gf_edf_shoup(ZZ.map([1, 2837, 2277]), 1, 2917, ZZ)
    [[1, 852], [1, 1985]]

    References
    ==========

    .. [1] [Shoup91]_
    .. [2] [Gathen92]_

    """
def gf_zassenhaus(f, p, K):
    """
    Factor a square-free ``f`` in ``GF(p)[x]`` for medium ``p``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_zassenhaus

    >>> gf_zassenhaus(ZZ.map([1, 4, 3]), 5, ZZ)
    [[1, 1], [1, 3]]

    """
def gf_shoup(f, p, K):
    """
    Factor a square-free ``f`` in ``GF(p)[x]`` for large ``p``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_shoup

    >>> gf_shoup(ZZ.map([1, 4, 3]), 5, ZZ)
    [[1, 1], [1, 3]]

    """
def gf_factor_sqf(f, p, K, method: Incomplete | None = None):
    """
    Factor a square-free polynomial ``f`` in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_factor_sqf

    >>> gf_factor_sqf(ZZ.map([3, 2, 4]), 5, ZZ)
    (3, [[1, 1], [1, 3]])

    """
def gf_factor(f, p, K):
    '''
    Factor (non square-free) polynomials in ``GF(p)[x]``.

    Given a possibly non square-free polynomial ``f`` in ``GF(p)[x]``,
    returns its complete factorization into irreducibles::

                 f_1(x)**e_1 f_2(x)**e_2 ... f_d(x)**e_d

    where each ``f_i`` is a monic polynomial and ``gcd(f_i, f_j) == 1``,
    for ``i != j``.  The result is given as a tuple consisting of the
    leading coefficient of ``f`` and a list of factors of ``f`` with
    their multiplicities.

    The algorithm proceeds by first computing square-free decomposition
    of ``f`` and then iteratively factoring each of square-free factors.

    Consider a non square-free polynomial ``f = (7*x + 1) (x + 2)**2`` in
    ``GF(11)[x]``. We obtain its factorization into irreducibles as follows::

       >>> from sympy.polys.domains import ZZ
       >>> from sympy.polys.galoistools import gf_factor

       >>> gf_factor(ZZ.map([5, 2, 7, 2]), 11, ZZ)
       (5, [([1, 2], 1), ([1, 8], 2)])

    We arrived with factorization ``f = 5 (x + 2) (x + 8)**2``. We did not
    recover the exact form of the input polynomial because we requested to
    get monic factors of ``f`` and its leading coefficient separately.

    Square-free factors of ``f`` can be factored into irreducibles over
    ``GF(p)`` using three very different methods:

    Berlekamp
        efficient for very small values of ``p`` (usually ``p < 25``)
    Cantor-Zassenhaus
        efficient on average input and with "typical" ``p``
    Shoup-Kaltofen-Gathen
        efficient with very large inputs and modulus

    If you want to use a specific factorization method, instead of the default
    one, set ``GF_FACTOR_METHOD`` with one of ``berlekamp``, ``zassenhaus`` or
    ``shoup`` values.

    References
    ==========

    .. [1] [Gathen99]_

    '''
def gf_value(f, a):
    """
    Value of polynomial 'f' at 'a' in field R.

    Examples
    ========

    >>> from sympy.polys.galoistools import gf_value

    >>> gf_value([1, 7, 2, 4], 11)
    2204

    """
def linear_congruence(a, b, m):
    """
    Returns the values of x satisfying a*x congruent b mod(m)

    Here m is positive integer and a, b are natural numbers.
    This function returns only those values of x which are distinct mod(m).

    Examples
    ========

    >>> from sympy.polys.galoistools import linear_congruence

    >>> linear_congruence(3, 12, 15)
    [4, 9, 14]

    There are 3 solutions distinct mod(15) since gcd(a, m) = gcd(3, 15) = 3.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Linear_congruence_theorem

    """
def csolve_prime(f, p, e: int = 1):
    """
    Solutions of f(x) congruent 0 mod(p**e).

    Examples
    ========

    >>> from sympy.polys.galoistools import csolve_prime

    >>> csolve_prime([1, 1, 7], 3, 1)
    [1]
    >>> csolve_prime([1, 1, 7], 3, 2)
    [1, 4, 7]

    Solutions [7, 4, 1] (mod 3**2) are generated by ``_raise_mod_power()``
    from solution [1] (mod 3).
    """
def gf_csolve(f, n):
    """
    To solve f(x) congruent 0 mod(n).

    n is divided into canonical factors and f(x) cong 0 mod(p**e) will be
    solved for each factor. Applying the Chinese Remainder Theorem to the
    results returns the final answers.

    Examples
    ========

    Solve [1, 1, 7] congruent 0 mod(189):

    >>> from sympy.polys.galoistools import gf_csolve
    >>> gf_csolve([1, 1, 7], 189)
    [13, 49, 76, 112, 139, 175]

    References
    ==========

    .. [1] 'An introduction to the Theory of Numbers' 5th Edition by Ivan Niven,
           Zuckerman and Montgomery.

    """
