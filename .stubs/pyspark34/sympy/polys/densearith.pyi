from sympy.polys.densebasic import dmp_LC as dmp_LC, dmp_degree as dmp_degree, dmp_ground as dmp_ground, dmp_one as dmp_one, dmp_one_p as dmp_one_p, dmp_strip as dmp_strip, dmp_zero as dmp_zero, dmp_zero_p as dmp_zero_p, dmp_zeros as dmp_zeros, dup_LC as dup_LC, dup_degree as dup_degree, dup_slice as dup_slice, dup_strip as dup_strip
from sympy.polys.polyerrors import ExactQuotientFailed as ExactQuotientFailed, PolynomialDivisionFailed as PolynomialDivisionFailed

def dup_add_term(f, c, i, K):
    '''
    Add ``c*x**i`` to ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_add_term(x**2 - 1, ZZ(2), 4)
    2*x**4 + x**2 - 1

    '''
def dmp_add_term(f, c, i, u, K):
    '''
    Add ``c(x_2..x_u)*x_0**i`` to ``f`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_add_term(x*y + 1, 2, 2)
    2*x**2 + x*y + 1

    '''
def dup_sub_term(f, c, i, K):
    '''
    Subtract ``c*x**i`` from ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sub_term(2*x**4 + x**2 - 1, ZZ(2), 4)
    x**2 - 1

    '''
def dmp_sub_term(f, c, i, u, K):
    '''
    Subtract ``c(x_2..x_u)*x_0**i`` from ``f`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_sub_term(2*x**2 + x*y + 1, 2, 2)
    x*y + 1

    '''
def dup_mul_term(f, c, i, K):
    '''
    Multiply ``f`` by ``c*x**i`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_mul_term(x**2 - 1, ZZ(3), 2)
    3*x**4 - 3*x**2

    '''
def dmp_mul_term(f, c, i, u, K):
    '''
    Multiply ``f`` by ``c(x_2..x_u)*x_0**i`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_mul_term(x**2*y + x, 3*y, 2)
    3*x**4*y**2 + 3*x**3*y

    '''
def dup_add_ground(f, c, K):
    '''
    Add an element of the ground domain to ``f``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_add_ground(x**3 + 2*x**2 + 3*x + 4, ZZ(4))
    x**3 + 2*x**2 + 3*x + 8

    '''
def dmp_add_ground(f, c, u, K):
    '''
    Add an element of the ground domain to ``f``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_add_ground(x**3 + 2*x**2 + 3*x + 4, ZZ(4))
    x**3 + 2*x**2 + 3*x + 8

    '''
def dup_sub_ground(f, c, K):
    '''
    Subtract an element of the ground domain from ``f``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sub_ground(x**3 + 2*x**2 + 3*x + 4, ZZ(4))
    x**3 + 2*x**2 + 3*x

    '''
def dmp_sub_ground(f, c, u, K):
    '''
    Subtract an element of the ground domain from ``f``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_sub_ground(x**3 + 2*x**2 + 3*x + 4, ZZ(4))
    x**3 + 2*x**2 + 3*x

    '''
def dup_mul_ground(f, c, K):
    '''
    Multiply ``f`` by a constant value in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_mul_ground(x**2 + 2*x - 1, ZZ(3))
    3*x**2 + 6*x - 3

    '''
def dmp_mul_ground(f, c, u, K):
    '''
    Multiply ``f`` by a constant value in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_mul_ground(2*x + 2*y, ZZ(3))
    6*x + 6*y

    '''
def dup_quo_ground(f, c, K):
    '''
    Quotient by a constant in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x = ring("x", ZZ)
    >>> R.dup_quo_ground(3*x**2 + 2, ZZ(2))
    x**2 + 1

    >>> R, x = ring("x", QQ)
    >>> R.dup_quo_ground(3*x**2 + 2, QQ(2))
    3/2*x**2 + 1

    '''
def dmp_quo_ground(f, c, u, K):
    '''
    Quotient by a constant in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x,y = ring("x,y", ZZ)
    >>> R.dmp_quo_ground(2*x**2*y + 3*x, ZZ(2))
    x**2*y + x

    >>> R, x,y = ring("x,y", QQ)
    >>> R.dmp_quo_ground(2*x**2*y + 3*x, QQ(2))
    x**2*y + 3/2*x

    '''
def dup_exquo_ground(f, c, K):
    '''
    Exact quotient by a constant in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> R.dup_exquo_ground(x**2 + 2, QQ(2))
    1/2*x**2 + 1

    '''
def dmp_exquo_ground(f, c, u, K):
    '''
    Exact quotient by a constant in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x,y = ring("x,y", QQ)

    >>> R.dmp_exquo_ground(x**2*y + 2*x, QQ(2))
    1/2*x**2*y + x

    '''
def dup_lshift(f, n, K):
    '''
    Efficiently multiply ``f`` by ``x**n`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_lshift(x**2 + 1, 2)
    x**4 + x**2

    '''
def dup_rshift(f, n, K):
    '''
    Efficiently divide ``f`` by ``x**n`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_rshift(x**4 + x**2, 2)
    x**2 + 1
    >>> R.dup_rshift(x**4 + x**2 + 2, 2)
    x**2 + 1

    '''
def dup_abs(f, K):
    '''
    Make all coefficients positive in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_abs(x**2 - 1)
    x**2 + 1

    '''
def dmp_abs(f, u, K):
    '''
    Make all coefficients positive in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_abs(x**2*y - x)
    x**2*y + x

    '''
def dup_neg(f, K):
    '''
    Negate a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_neg(x**2 - 1)
    -x**2 + 1

    '''
def dmp_neg(f, u, K):
    '''
    Negate a polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_neg(x**2*y - x)
    -x**2*y + x

    '''
def dup_add(f, g, K):
    '''
    Add dense polynomials in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_add(x**2 - 1, x - 2)
    x**2 + x - 3

    '''
def dmp_add(f, g, u, K):
    '''
    Add dense polynomials in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_add(x**2 + y, x**2*y + x)
    x**2*y + x**2 + x + y

    '''
def dup_sub(f, g, K):
    '''
    Subtract dense polynomials in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sub(x**2 - 1, x - 2)
    x**2 - x + 1

    '''
def dmp_sub(f, g, u, K):
    '''
    Subtract dense polynomials in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_sub(x**2 + y, x**2*y + x)
    -x**2*y + x**2 - x + y

    '''
def dup_add_mul(f, g, h, K):
    '''
    Returns ``f + g*h`` where ``f, g, h`` are in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_add_mul(x**2 - 1, x - 2, x + 2)
    2*x**2 - 5

    '''
def dmp_add_mul(f, g, h, u, K):
    '''
    Returns ``f + g*h`` where ``f, g, h`` are in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_add_mul(x**2 + y, x, x + 2)
    2*x**2 + 2*x + y

    '''
def dup_sub_mul(f, g, h, K):
    '''
    Returns ``f - g*h`` where ``f, g, h`` are in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sub_mul(x**2 - 1, x - 2, x + 2)
    3

    '''
def dmp_sub_mul(f, g, h, u, K):
    '''
    Returns ``f - g*h`` where ``f, g, h`` are in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_sub_mul(x**2 + y, x, x + 2)
    -2*x + y

    '''
def dup_mul(f, g, K):
    '''
    Multiply dense polynomials in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_mul(x - 2, x + 2)
    x**2 - 4

    '''
def dmp_mul(f, g, u, K):
    '''
    Multiply dense polynomials in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_mul(x*y + 1, x)
    x**2*y + x

    '''
def dup_sqr(f, K):
    '''
    Square dense polynomials in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sqr(x**2 + 1)
    x**4 + 2*x**2 + 1

    '''
def dmp_sqr(f, u, K):
    '''
    Square dense polynomials in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_sqr(x**2 + x*y + y**2)
    x**4 + 2*x**3*y + 3*x**2*y**2 + 2*x*y**3 + y**4

    '''
def dup_pow(f, n, K):
    '''
    Raise ``f`` to the ``n``-th power in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_pow(x - 2, 3)
    x**3 - 6*x**2 + 12*x - 8

    '''
def dmp_pow(f, n, u, K):
    '''
    Raise ``f`` to the ``n``-th power in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_pow(x*y + 1, 3)
    x**3*y**3 + 3*x**2*y**2 + 3*x*y + 1

    '''
def dup_pdiv(f, g, K):
    '''
    Polynomial pseudo-division in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_pdiv(x**2 + 1, 2*x - 4)
    (2*x + 4, 20)

    '''
def dup_prem(f, g, K):
    '''
    Polynomial pseudo-remainder in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_prem(x**2 + 1, 2*x - 4)
    20

    '''
def dup_pquo(f, g, K):
    '''
    Polynomial exact pseudo-quotient in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_pquo(x**2 - 1, 2*x - 2)
    2*x + 2

    >>> R.dup_pquo(x**2 + 1, 2*x - 4)
    2*x + 4

    '''
def dup_pexquo(f, g, K):
    '''
    Polynomial pseudo-quotient in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_pexquo(x**2 - 1, 2*x - 2)
    2*x + 2

    >>> R.dup_pexquo(x**2 + 1, 2*x - 4)
    Traceback (most recent call last):
    ...
    ExactQuotientFailed: [2, -4] does not divide [1, 0, 1]

    '''
def dmp_pdiv(f, g, u, K):
    '''
    Polynomial pseudo-division in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_pdiv(x**2 + x*y, 2*x + 2)
    (2*x + 2*y - 2, -4*y + 4)

    '''
def dmp_prem(f, g, u, K):
    '''
    Polynomial pseudo-remainder in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_prem(x**2 + x*y, 2*x + 2)
    -4*y + 4

    '''
def dmp_pquo(f, g, u, K):
    '''
    Polynomial exact pseudo-quotient in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = x**2 + x*y
    >>> g = 2*x + 2*y
    >>> h = 2*x + 2

    >>> R.dmp_pquo(f, g)
    2*x

    >>> R.dmp_pquo(f, h)
    2*x + 2*y - 2

    '''
def dmp_pexquo(f, g, u, K):
    '''
    Polynomial pseudo-quotient in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = x**2 + x*y
    >>> g = 2*x + 2*y
    >>> h = 2*x + 2

    >>> R.dmp_pexquo(f, g)
    2*x

    >>> R.dmp_pexquo(f, h)
    Traceback (most recent call last):
    ...
    ExactQuotientFailed: [[2], [2]] does not divide [[1], [1, 0], []]

    '''
def dup_rr_div(f, g, K):
    '''
    Univariate division with remainder over a ring.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_rr_div(x**2 + 1, 2*x - 4)
    (0, x**2 + 1)

    '''
def dmp_rr_div(f, g, u, K):
    '''
    Multivariate division with remainder over a ring.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_rr_div(x**2 + x*y, 2*x + 2)
    (0, x**2 + x*y)

    '''
def dup_ff_div(f, g, K):
    '''
    Polynomial division with remainder over a field.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> R.dup_ff_div(x**2 + 1, 2*x - 4)
    (1/2*x + 1, 5)

    '''
def dmp_ff_div(f, g, u, K):
    '''
    Polynomial division with remainder over a field.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x,y = ring("x,y", QQ)

    >>> R.dmp_ff_div(x**2 + x*y, 2*x + 2)
    (1/2*x + 1/2*y - 1/2, -y + 1)

    '''
def dup_div(f, g, K):
    '''
    Polynomial division with remainder in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x = ring("x", ZZ)
    >>> R.dup_div(x**2 + 1, 2*x - 4)
    (0, x**2 + 1)

    >>> R, x = ring("x", QQ)
    >>> R.dup_div(x**2 + 1, 2*x - 4)
    (1/2*x + 1, 5)

    '''
def dup_rem(f, g, K):
    '''
    Returns polynomial remainder in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x = ring("x", ZZ)
    >>> R.dup_rem(x**2 + 1, 2*x - 4)
    x**2 + 1

    >>> R, x = ring("x", QQ)
    >>> R.dup_rem(x**2 + 1, 2*x - 4)
    5

    '''
def dup_quo(f, g, K):
    '''
    Returns exact polynomial quotient in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x = ring("x", ZZ)
    >>> R.dup_quo(x**2 + 1, 2*x - 4)
    0

    >>> R, x = ring("x", QQ)
    >>> R.dup_quo(x**2 + 1, 2*x - 4)
    1/2*x + 1

    '''
def dup_exquo(f, g, K):
    '''
    Returns polynomial quotient in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_exquo(x**2 - 1, x - 1)
    x + 1

    >>> R.dup_exquo(x**2 + 1, 2*x - 4)
    Traceback (most recent call last):
    ...
    ExactQuotientFailed: [2, -4] does not divide [1, 0, 1]

    '''
def dmp_div(f, g, u, K):
    '''
    Polynomial division with remainder in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x,y = ring("x,y", ZZ)
    >>> R.dmp_div(x**2 + x*y, 2*x + 2)
    (0, x**2 + x*y)

    >>> R, x,y = ring("x,y", QQ)
    >>> R.dmp_div(x**2 + x*y, 2*x + 2)
    (1/2*x + 1/2*y - 1/2, -y + 1)

    '''
def dmp_rem(f, g, u, K):
    '''
    Returns polynomial remainder in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x,y = ring("x,y", ZZ)
    >>> R.dmp_rem(x**2 + x*y, 2*x + 2)
    x**2 + x*y

    >>> R, x,y = ring("x,y", QQ)
    >>> R.dmp_rem(x**2 + x*y, 2*x + 2)
    -y + 1

    '''
def dmp_quo(f, g, u, K):
    '''
    Returns exact polynomial quotient in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x,y = ring("x,y", ZZ)
    >>> R.dmp_quo(x**2 + x*y, 2*x + 2)
    0

    >>> R, x,y = ring("x,y", QQ)
    >>> R.dmp_quo(x**2 + x*y, 2*x + 2)
    1/2*x + 1/2*y - 1/2

    '''
def dmp_exquo(f, g, u, K):
    '''
    Returns polynomial quotient in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = x**2 + x*y
    >>> g = x + y
    >>> h = 2*x + 2

    >>> R.dmp_exquo(f, g)
    x

    >>> R.dmp_exquo(f, h)
    Traceback (most recent call last):
    ...
    ExactQuotientFailed: [[2], [2]] does not divide [[1], [1, 0], []]

    '''
def dup_max_norm(f, K):
    '''
    Returns maximum norm of a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_max_norm(-x**2 + 2*x - 3)
    3

    '''
def dmp_max_norm(f, u, K):
    '''
    Returns maximum norm of a polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_max_norm(2*x*y - x - 3)
    3

    '''
def dup_l1_norm(f, K):
    '''
    Returns l1 norm of a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_l1_norm(2*x**3 - 3*x**2 + 1)
    6

    '''
def dmp_l1_norm(f, u, K):
    '''
    Returns l1 norm of a polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_l1_norm(2*x*y - x - 3)
    6

    '''
def dup_l2_norm_squared(f, K):
    '''
    Returns squared l2 norm of a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_l2_norm_squared(2*x**3 - 3*x**2 + 1)
    14

    '''
def dmp_l2_norm_squared(f, u, K):
    '''
    Returns squared l2 norm of a polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_l2_norm_squared(2*x*y - x - 3)
    14

    '''
def dup_expand(polys, K):
    '''
    Multiply together several polynomials in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_expand([x**2 - 1, x, 2])
    2*x**3 - 2*x

    '''
def dmp_expand(polys, u, K):
    '''
    Multiply together several polynomials in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_expand([x**2 + y**2, x + 1])
    x**3 + x**2 + x*y**2 + y**2

    '''
