from sympy.polys.densearith import dmp_add as dmp_add, dmp_div as dmp_div, dmp_max_norm as dmp_max_norm, dmp_mul as dmp_mul, dmp_mul_ground as dmp_mul_ground, dmp_mul_term as dmp_mul_term, dmp_neg as dmp_neg, dmp_pow as dmp_pow, dmp_prem as dmp_prem, dmp_quo as dmp_quo, dmp_quo_ground as dmp_quo_ground, dmp_sub as dmp_sub, dup_div as dup_div, dup_max_norm as dup_max_norm, dup_mul as dup_mul, dup_mul_ground as dup_mul_ground, dup_neg as dup_neg, dup_prem as dup_prem, dup_quo as dup_quo, dup_quo_ground as dup_quo_ground, dup_rem as dup_rem, dup_sub_mul as dup_sub_mul
from sympy.polys.densebasic import dmp_LC as dmp_LC, dmp_apply_pairs as dmp_apply_pairs, dmp_convert as dmp_convert, dmp_degree as dmp_degree, dmp_degree_in as dmp_degree_in, dmp_ground as dmp_ground, dmp_ground_LC as dmp_ground_LC, dmp_inflate as dmp_inflate, dmp_multi_deflate as dmp_multi_deflate, dmp_one as dmp_one, dmp_one_p as dmp_one_p, dmp_raise as dmp_raise, dmp_zero as dmp_zero, dmp_zero_p as dmp_zero_p, dmp_zeros as dmp_zeros, dup_LC as dup_LC, dup_convert as dup_convert, dup_degree as dup_degree, dup_strip as dup_strip
from sympy.polys.densetools import dmp_clear_denoms as dmp_clear_denoms, dmp_diff as dmp_diff, dmp_eval as dmp_eval, dmp_eval_in as dmp_eval_in, dmp_ground_extract as dmp_ground_extract, dmp_ground_monic as dmp_ground_monic, dmp_ground_primitive as dmp_ground_primitive, dmp_ground_trunc as dmp_ground_trunc, dup_clear_denoms as dup_clear_denoms, dup_diff as dup_diff, dup_eval as dup_eval, dup_extract as dup_extract, dup_monic as dup_monic, dup_primitive as dup_primitive, dup_trunc as dup_trunc
from sympy.polys.galoistools import gf_crt as gf_crt, gf_int as gf_int
from sympy.polys.polyconfig import query as query
from sympy.polys.polyerrors import DomainError as DomainError, HeuristicGCDFailed as HeuristicGCDFailed, HomomorphismFailed as HomomorphismFailed, MultivariatePolynomialError as MultivariatePolynomialError, NotInvertible as NotInvertible

def dup_half_gcdex(f, g, K):
    '''
    Half extended Euclidean algorithm in `F[x]`.

    Returns ``(s, h)`` such that ``h = gcd(f, g)`` and ``s*f = h (mod g)``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> f = x**4 - 2*x**3 - 6*x**2 + 12*x + 15
    >>> g = x**3 + x**2 - 4*x - 4

    >>> R.dup_half_gcdex(f, g)
    (-1/5*x + 3/5, x + 1)

    '''
def dmp_half_gcdex(f, g, u, K):
    '''
    Half extended Euclidean algorithm in `F[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    '''
def dup_gcdex(f, g, K):
    '''
    Extended Euclidean algorithm in `F[x]`.

    Returns ``(s, t, h)`` such that ``h = gcd(f, g)`` and ``s*f + t*g = h``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> f = x**4 - 2*x**3 - 6*x**2 + 12*x + 15
    >>> g = x**3 + x**2 - 4*x - 4

    >>> R.dup_gcdex(f, g)
    (-1/5*x + 3/5, 1/5*x**2 - 6/5*x + 2, x + 1)

    '''
def dmp_gcdex(f, g, u, K):
    '''
    Extended Euclidean algorithm in `F[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    '''
def dup_invert(f, g, K):
    '''
    Compute multiplicative inverse of `f` modulo `g` in `F[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> f = x**2 - 1
    >>> g = 2*x - 1
    >>> h = x - 1

    >>> R.dup_invert(f, g)
    -4/3

    >>> R.dup_invert(f, h)
    Traceback (most recent call last):
    ...
    NotInvertible: zero divisor

    '''
def dmp_invert(f, g, u, K):
    '''
    Compute multiplicative inverse of `f` modulo `g` in `F[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    '''
def dup_euclidean_prs(f, g, K):
    '''
    Euclidean polynomial remainder sequence (PRS) in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> f = x**8 + x**6 - 3*x**4 - 3*x**3 + 8*x**2 + 2*x - 5
    >>> g = 3*x**6 + 5*x**4 - 4*x**2 - 9*x + 21

    >>> prs = R.dup_euclidean_prs(f, g)

    >>> prs[0]
    x**8 + x**6 - 3*x**4 - 3*x**3 + 8*x**2 + 2*x - 5
    >>> prs[1]
    3*x**6 + 5*x**4 - 4*x**2 - 9*x + 21
    >>> prs[2]
    -5/9*x**4 + 1/9*x**2 - 1/3
    >>> prs[3]
    -117/25*x**2 - 9*x + 441/25
    >>> prs[4]
    233150/19773*x - 102500/6591
    >>> prs[5]
    -1288744821/543589225

    '''
def dmp_euclidean_prs(f, g, u, K):
    '''
    Euclidean polynomial remainder sequence (PRS) in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    '''
def dup_primitive_prs(f, g, K):
    '''
    Primitive polynomial remainder sequence (PRS) in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> f = x**8 + x**6 - 3*x**4 - 3*x**3 + 8*x**2 + 2*x - 5
    >>> g = 3*x**6 + 5*x**4 - 4*x**2 - 9*x + 21

    >>> prs = R.dup_primitive_prs(f, g)

    >>> prs[0]
    x**8 + x**6 - 3*x**4 - 3*x**3 + 8*x**2 + 2*x - 5
    >>> prs[1]
    3*x**6 + 5*x**4 - 4*x**2 - 9*x + 21
    >>> prs[2]
    -5*x**4 + x**2 - 3
    >>> prs[3]
    13*x**2 + 25*x - 49
    >>> prs[4]
    4663*x - 6150
    >>> prs[5]
    1

    '''
def dmp_primitive_prs(f, g, u, K):
    '''
    Primitive polynomial remainder sequence (PRS) in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    '''
def dup_inner_subresultants(f, g, K):
    '''
    Subresultant PRS algorithm in `K[x]`.

    Computes the subresultant polynomial remainder sequence (PRS)
    and the non-zero scalar subresultants of `f` and `g`.
    By [1] Thm. 3, these are the constants \'-c\' (- to optimize
    computation of sign).
    The first subdeterminant is set to 1 by convention to match
    the polynomial and the scalar subdeterminants.
    If \'deg(f) < deg(g)\', the subresultants of \'(g,f)\' are computed.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_inner_subresultants(x**2 + 1, x**2 - 1)
    ([x**2 + 1, x**2 - 1, -2], [1, 1, 4])

    References
    ==========

    .. [1] W.S. Brown, The Subresultant PRS Algorithm.
           ACM Transaction of Mathematical Software 4 (1978) 237-249

    '''
def dup_subresultants(f, g, K):
    '''
    Computes subresultant PRS of two polynomials in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_subresultants(x**2 + 1, x**2 - 1)
    [x**2 + 1, x**2 - 1, -2]

    '''
def dup_prs_resultant(f, g, K):
    '''
    Resultant algorithm in `K[x]` using subresultant PRS.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_prs_resultant(x**2 + 1, x**2 - 1)
    (4, [x**2 + 1, x**2 - 1, -2])

    '''
def dup_resultant(f, g, K, includePRS: bool = False):
    '''
    Computes resultant of two polynomials in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_resultant(x**2 + 1, x**2 - 1)
    4

    '''
def dmp_inner_subresultants(f, g, u, K):
    '''
    Subresultant PRS algorithm in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = 3*x**2*y - y**3 - 4
    >>> g = x**2 + x*y**3 - 9

    >>> a = 3*x*y**4 + y**3 - 27*y + 4
    >>> b = -3*y**10 - 12*y**7 + y**6 - 54*y**4 + 8*y**3 + 729*y**2 - 216*y + 16

    >>> prs = [f, g, a, b]
    >>> sres = [[1], [1], [3, 0, 0, 0, 0], [-3, 0, 0, -12, 1, 0, -54, 8, 729, -216, 16]]

    >>> R.dmp_inner_subresultants(f, g) == (prs, sres)
    True

    '''
def dmp_subresultants(f, g, u, K):
    '''
    Computes subresultant PRS of two polynomials in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = 3*x**2*y - y**3 - 4
    >>> g = x**2 + x*y**3 - 9

    >>> a = 3*x*y**4 + y**3 - 27*y + 4
    >>> b = -3*y**10 - 12*y**7 + y**6 - 54*y**4 + 8*y**3 + 729*y**2 - 216*y + 16

    >>> R.dmp_subresultants(f, g) == [f, g, a, b]
    True

    '''
def dmp_prs_resultant(f, g, u, K):
    '''
    Resultant algorithm in `K[X]` using subresultant PRS.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = 3*x**2*y - y**3 - 4
    >>> g = x**2 + x*y**3 - 9

    >>> a = 3*x*y**4 + y**3 - 27*y + 4
    >>> b = -3*y**10 - 12*y**7 + y**6 - 54*y**4 + 8*y**3 + 729*y**2 - 216*y + 16

    >>> res, prs = R.dmp_prs_resultant(f, g)

    >>> res == b             # resultant has n-1 variables
    False
    >>> res == b.drop(x)
    True
    >>> prs == [f, g, a, b]
    True

    '''
def dmp_zz_modular_resultant(f, g, p, u, K):
    '''
    Compute resultant of `f` and `g` modulo a prime `p`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = x + y + 2
    >>> g = 2*x*y + x + 3

    >>> R.dmp_zz_modular_resultant(f, g, 5)
    -2*y**2 + 1

    '''
def dmp_zz_collins_resultant(f, g, u, K):
    '''
    Collins\'s modular resultant algorithm in `Z[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = x + y + 2
    >>> g = 2*x*y + x + 3

    >>> R.dmp_zz_collins_resultant(f, g)
    -2*y**2 - 5*y + 1

    '''
def dmp_qq_collins_resultant(f, g, u, K0):
    '''
    Collins\'s modular resultant algorithm in `Q[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x,y = ring("x,y", QQ)

    >>> f = QQ(1,2)*x + y + QQ(2,3)
    >>> g = 2*x*y + x + 3

    >>> R.dmp_qq_collins_resultant(f, g)
    -2*y**2 - 7/3*y + 5/6

    '''
def dmp_resultant(f, g, u, K, includePRS: bool = False):
    '''
    Computes resultant of two polynomials in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = 3*x**2*y - y**3 - 4
    >>> g = x**2 + x*y**3 - 9

    >>> R.dmp_resultant(f, g)
    -3*y**10 - 12*y**7 + y**6 - 54*y**4 + 8*y**3 + 729*y**2 - 216*y + 16

    '''
def dup_discriminant(f, K):
    '''
    Computes discriminant of a polynomial in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_discriminant(x**2 + 2*x + 3)
    -8

    '''
def dmp_discriminant(f, u, K):
    '''
    Computes discriminant of a polynomial in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y,z,t = ring("x,y,z,t", ZZ)

    >>> R.dmp_discriminant(x**2*y + x*z + t)
    -4*y*t + z**2

    '''
def dup_rr_prs_gcd(f, g, K):
    '''
    Computes polynomial GCD using subresultants over a ring.

    Returns ``(h, cff, cfg)`` such that ``a = gcd(f, g)``, ``cff = quo(f, h)``,
    and ``cfg = quo(g, h)``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_rr_prs_gcd(x**2 - 1, x**2 - 3*x + 2)
    (x - 1, x + 1, x - 2)

    '''
def dup_ff_prs_gcd(f, g, K):
    '''
    Computes polynomial GCD using subresultants over a field.

    Returns ``(h, cff, cfg)`` such that ``a = gcd(f, g)``, ``cff = quo(f, h)``,
    and ``cfg = quo(g, h)``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> R.dup_ff_prs_gcd(x**2 - 1, x**2 - 3*x + 2)
    (x - 1, x + 1, x - 2)

    '''
def dmp_rr_prs_gcd(f, g, u, K):
    '''
    Computes polynomial GCD using subresultants over a ring.

    Returns ``(h, cff, cfg)`` such that ``a = gcd(f, g)``, ``cff = quo(f, h)``,
    and ``cfg = quo(g, h)``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y, = ring("x,y", ZZ)

    >>> f = x**2 + 2*x*y + y**2
    >>> g = x**2 + x*y

    >>> R.dmp_rr_prs_gcd(f, g)
    (x + y, x + y, x)

    '''
def dmp_ff_prs_gcd(f, g, u, K):
    '''
    Computes polynomial GCD using subresultants over a field.

    Returns ``(h, cff, cfg)`` such that ``a = gcd(f, g)``, ``cff = quo(f, h)``,
    and ``cfg = quo(g, h)``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x,y, = ring("x,y", QQ)

    >>> f = QQ(1,2)*x**2 + x*y + QQ(1,2)*y**2
    >>> g = x**2 + x*y

    >>> R.dmp_ff_prs_gcd(f, g)
    (x + y, 1/2*x + 1/2*y, x)

    '''

HEU_GCD_MAX: int

def dup_zz_heu_gcd(f, g, K):
    '''
    Heuristic polynomial GCD in `Z[x]`.

    Given univariate polynomials `f` and `g` in `Z[x]`, returns
    their GCD and cofactors, i.e. polynomials ``h``, ``cff`` and ``cfg``
    such that::

          h = gcd(f, g), cff = quo(f, h) and cfg = quo(g, h)

    The algorithm is purely heuristic which means it may fail to compute
    the GCD. This will be signaled by raising an exception. In this case
    you will need to switch to another GCD method.

    The algorithm computes the polynomial GCD by evaluating polynomials
    f and g at certain points and computing (fast) integer GCD of those
    evaluations. The polynomial GCD is recovered from the integer image
    by interpolation.  The final step is to verify if the result is the
    correct GCD. This gives cofactors as a side effect.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_zz_heu_gcd(x**2 - 1, x**2 - 3*x + 2)
    (x - 1, x + 1, x - 2)

    References
    ==========

    .. [1] [Liao95]_

    '''
def dmp_zz_heu_gcd(f, g, u, K):
    '''
    Heuristic polynomial GCD in `Z[X]`.

    Given univariate polynomials `f` and `g` in `Z[X]`, returns
    their GCD and cofactors, i.e. polynomials ``h``, ``cff`` and ``cfg``
    such that::

          h = gcd(f, g), cff = quo(f, h) and cfg = quo(g, h)

    The algorithm is purely heuristic which means it may fail to compute
    the GCD. This will be signaled by raising an exception. In this case
    you will need to switch to another GCD method.

    The algorithm computes the polynomial GCD by evaluating polynomials
    f and g at certain points and computing (fast) integer GCD of those
    evaluations. The polynomial GCD is recovered from the integer image
    by interpolation. The evaluation process reduces f and g variable by
    variable into a large integer.  The final step is to verify if the
    interpolated polynomial is the correct GCD. This gives cofactors of
    the input polynomials as a side effect.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y, = ring("x,y", ZZ)

    >>> f = x**2 + 2*x*y + y**2
    >>> g = x**2 + x*y

    >>> R.dmp_zz_heu_gcd(f, g)
    (x + y, x + y, x)

    References
    ==========

    .. [1] [Liao95]_

    '''
def dup_qq_heu_gcd(f, g, K0):
    '''
    Heuristic polynomial GCD in `Q[x]`.

    Returns ``(h, cff, cfg)`` such that ``a = gcd(f, g)``,
    ``cff = quo(f, h)``, and ``cfg = quo(g, h)``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> f = QQ(1,2)*x**2 + QQ(7,4)*x + QQ(3,2)
    >>> g = QQ(1,2)*x**2 + x

    >>> R.dup_qq_heu_gcd(f, g)
    (x + 2, 1/2*x + 3/4, 1/2*x)

    '''
def dmp_qq_heu_gcd(f, g, u, K0):
    '''
    Heuristic polynomial GCD in `Q[X]`.

    Returns ``(h, cff, cfg)`` such that ``a = gcd(f, g)``,
    ``cff = quo(f, h)``, and ``cfg = quo(g, h)``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x,y, = ring("x,y", QQ)

    >>> f = QQ(1,4)*x**2 + x*y + y**2
    >>> g = QQ(1,2)*x**2 + x*y

    >>> R.dmp_qq_heu_gcd(f, g)
    (x + 2*y, 1/4*x + 1/2*y, 1/2*x)

    '''
def dup_inner_gcd(f, g, K):
    '''
    Computes polynomial GCD and cofactors of `f` and `g` in `K[x]`.

    Returns ``(h, cff, cfg)`` such that ``a = gcd(f, g)``,
    ``cff = quo(f, h)``, and ``cfg = quo(g, h)``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_inner_gcd(x**2 - 1, x**2 - 3*x + 2)
    (x - 1, x + 1, x - 2)

    '''
def dmp_inner_gcd(f, g, u, K):
    '''
    Computes polynomial GCD and cofactors of `f` and `g` in `K[X]`.

    Returns ``(h, cff, cfg)`` such that ``a = gcd(f, g)``,
    ``cff = quo(f, h)``, and ``cfg = quo(g, h)``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y, = ring("x,y", ZZ)

    >>> f = x**2 + 2*x*y + y**2
    >>> g = x**2 + x*y

    >>> R.dmp_inner_gcd(f, g)
    (x + y, x + y, x)

    '''
def dup_gcd(f, g, K):
    '''
    Computes polynomial GCD of `f` and `g` in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_gcd(x**2 - 1, x**2 - 3*x + 2)
    x - 1

    '''
def dmp_gcd(f, g, u, K):
    '''
    Computes polynomial GCD of `f` and `g` in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y, = ring("x,y", ZZ)

    >>> f = x**2 + 2*x*y + y**2
    >>> g = x**2 + x*y

    >>> R.dmp_gcd(f, g)
    x + y

    '''
def dup_rr_lcm(f, g, K):
    '''
    Computes polynomial LCM over a ring in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_rr_lcm(x**2 - 1, x**2 - 3*x + 2)
    x**3 - 2*x**2 - x + 2

    '''
def dup_ff_lcm(f, g, K):
    '''
    Computes polynomial LCM over a field in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> f = QQ(1,2)*x**2 + QQ(7,4)*x + QQ(3,2)
    >>> g = QQ(1,2)*x**2 + x

    >>> R.dup_ff_lcm(f, g)
    x**3 + 7/2*x**2 + 3*x

    '''
def dup_lcm(f, g, K):
    '''
    Computes polynomial LCM of `f` and `g` in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_lcm(x**2 - 1, x**2 - 3*x + 2)
    x**3 - 2*x**2 - x + 2

    '''
def dmp_rr_lcm(f, g, u, K):
    '''
    Computes polynomial LCM over a ring in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y, = ring("x,y", ZZ)

    >>> f = x**2 + 2*x*y + y**2
    >>> g = x**2 + x*y

    >>> R.dmp_rr_lcm(f, g)
    x**3 + 2*x**2*y + x*y**2

    '''
def dmp_ff_lcm(f, g, u, K):
    '''
    Computes polynomial LCM over a field in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x,y, = ring("x,y", QQ)

    >>> f = QQ(1,4)*x**2 + x*y + y**2
    >>> g = QQ(1,2)*x**2 + x*y

    >>> R.dmp_ff_lcm(f, g)
    x**3 + 4*x**2*y + 4*x*y**2

    '''
def dmp_lcm(f, g, u, K):
    '''
    Computes polynomial LCM of `f` and `g` in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y, = ring("x,y", ZZ)

    >>> f = x**2 + 2*x*y + y**2
    >>> g = x**2 + x*y

    >>> R.dmp_lcm(f, g)
    x**3 + 2*x**2*y + x*y**2

    '''
def dmp_content(f, u, K):
    '''
    Returns GCD of multivariate coefficients.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y, = ring("x,y", ZZ)

    >>> R.dmp_content(2*x*y + 6*x + 4*y + 12)
    2*y + 6

    '''
def dmp_primitive(f, u, K):
    '''
    Returns multivariate content and a primitive polynomial.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y, = ring("x,y", ZZ)

    >>> R.dmp_primitive(2*x*y + 6*x + 4*y + 12)
    (2*y + 6, x + 2)

    '''
def dup_cancel(f, g, K, include: bool = True):
    '''
    Cancel common factors in a rational function `f/g`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_cancel(2*x**2 - 2, x**2 - 2*x + 1)
    (2*x + 2, x - 1)

    '''
def dmp_cancel(f, g, u, K, include: bool = True):
    '''
    Cancel common factors in a rational function `f/g`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_cancel(2*x**2 - 2, x**2 - 2*x + 1)
    (2*x + 2, x - 1)

    '''
