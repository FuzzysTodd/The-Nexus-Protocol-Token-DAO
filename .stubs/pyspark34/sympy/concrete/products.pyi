from .expr_with_intlimits import ExprWithIntLimits as ExprWithIntLimits
from .summations import Sum as Sum, summation as summation
from sympy.core.expr import Expr as Expr
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.function import Derivative as Derivative
from sympy.core.mul import Mul as Mul
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.functions.combinatorial.factorials import RisingFactorial as RisingFactorial
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.special.tensor_functions import KroneckerDelta as KroneckerDelta
from sympy.polys import quo as quo, roots as roots
from typing import Tuple as tTuple

class Product(ExprWithIntLimits):
    '''
    Represents unevaluated products.

    Explanation
    ===========

    ``Product`` represents a finite or infinite product, with the first
    argument being the general form of terms in the series, and the second
    argument being ``(dummy_variable, start, end)``, with ``dummy_variable``
    taking all integer values from ``start`` through ``end``. In accordance
    with long-standing mathematical convention, the end term is included in
    the product.

    Finite products
    ===============

    For finite products (and products with symbolic limits assumed to be finite)
    we follow the analogue of the summation convention described by Karr [1],
    especially definition 3 of section 1.4. The product:

    .. math::

        \\prod_{m \\leq i < n} f(i)

    has *the obvious meaning* for `m < n`, namely:

    .. math::

        \\prod_{m \\leq i < n} f(i) = f(m) f(m+1) \\cdot \\ldots \\cdot f(n-2) f(n-1)

    with the upper limit value `f(n)` excluded. The product over an empty set is
    one if and only if `m = n`:

    .. math::

        \\prod_{m \\leq i < n} f(i) = 1  \\quad \\mathrm{for} \\quad  m = n

    Finally, for all other products over empty sets we assume the following
    definition:

    .. math::

        \\prod_{m \\leq i < n} f(i) = \\frac{1}{\\prod_{n \\leq i < m} f(i)}  \\quad \\mathrm{for} \\quad  m > n

    It is important to note that above we define all products with the upper
    limit being exclusive. This is in contrast to the usual mathematical notation,
    but does not affect the product convention. Indeed we have:

    .. math::

        \\prod_{m \\leq i < n} f(i) = \\prod_{i = m}^{n - 1} f(i)

    where the difference in notation is intentional to emphasize the meaning,
    with limits typeset on the top being inclusive.

    Examples
    ========

    >>> from sympy.abc import a, b, i, k, m, n, x
    >>> from sympy import Product, oo
    >>> Product(k, (k, 1, m))
    Product(k, (k, 1, m))
    >>> Product(k, (k, 1, m)).doit()
    factorial(m)
    >>> Product(k**2,(k, 1, m))
    Product(k**2, (k, 1, m))
    >>> Product(k**2,(k, 1, m)).doit()
    factorial(m)**2

    Wallis\' product for pi:

    >>> W = Product(2*i/(2*i-1) * 2*i/(2*i+1), (i, 1, oo))
    >>> W
    Product(4*i**2/((2*i - 1)*(2*i + 1)), (i, 1, oo))

    Direct computation currently fails:

    >>> W.doit()
    Product(4*i**2/((2*i - 1)*(2*i + 1)), (i, 1, oo))

    But we can approach the infinite product by a limit of finite products:

    >>> from sympy import limit
    >>> W2 = Product(2*i/(2*i-1)*2*i/(2*i+1), (i, 1, n))
    >>> W2
    Product(4*i**2/((2*i - 1)*(2*i + 1)), (i, 1, n))
    >>> W2e = W2.doit()
    >>> W2e
    4**n*factorial(n)**2/(2**(2*n)*RisingFactorial(1/2, n)*RisingFactorial(3/2, n))
    >>> limit(W2e, n, oo)
    pi/2

    By the same formula we can compute sin(pi/2):

    >>> from sympy import combsimp, pi, gamma, simplify
    >>> P = pi * x * Product(1 - x**2/k**2, (k, 1, n))
    >>> P = P.subs(x, pi/2)
    >>> P
    pi**2*Product(1 - pi**2/(4*k**2), (k, 1, n))/2
    >>> Pe = P.doit()
    >>> Pe
    pi**2*RisingFactorial(1 - pi/2, n)*RisingFactorial(1 + pi/2, n)/(2*factorial(n)**2)
    >>> limit(Pe, n, oo).gammasimp()
    sin(pi**2/2)
    >>> Pe.rewrite(gamma)
    (-1)**n*pi**2*gamma(pi/2)*gamma(n + 1 + pi/2)/(2*gamma(1 + pi/2)*gamma(-n + pi/2)*gamma(n + 1)**2)

    Products with the lower limit being larger than the upper one:

    >>> Product(1/i, (i, 6, 1)).doit()
    120
    >>> Product(i, (i, 2, 5)).doit()
    120

    The empty product:

    >>> Product(i, (i, n, n-1)).doit()
    1

    An example showing that the symbolic result of a product is still
    valid for seemingly nonsensical values of the limits. Then the Karr
    convention allows us to give a perfectly valid interpretation to
    those products by interchanging the limits according to the above rules:

    >>> P = Product(2, (i, 10, n)).doit()
    >>> P
    2**(n - 9)
    >>> P.subs(n, 5)
    1/16
    >>> Product(2, (i, 10, 5)).doit()
    1/16
    >>> 1/Product(2, (i, 6, 9)).doit()
    1/16

    An explicit example of the Karr summation convention applied to products:

    >>> P1 = Product(x, (i, a, b)).doit()
    >>> P1
    x**(-a + b + 1)
    >>> P2 = Product(x, (i, b+1, a-1)).doit()
    >>> P2
    x**(a - b - 1)
    >>> simplify(P1 * P2)
    1

    And another one:

    >>> P1 = Product(i, (i, b, a)).doit()
    >>> P1
    RisingFactorial(b, a - b + 1)
    >>> P2 = Product(i, (i, a+1, b-1)).doit()
    >>> P2
    RisingFactorial(a + 1, -a + b - 1)
    >>> P1 * P2
    RisingFactorial(b, a - b + 1)*RisingFactorial(a + 1, -a + b - 1)
    >>> combsimp(P1 * P2)
    1

    See Also
    ========

    Sum, summation
    product

    References
    ==========

    .. [1] Michael Karr, "Summation in Finite Terms", Journal of the ACM,
           Volume 28 Issue 2, April 1981, Pages 305-350
           https://dl.acm.org/doi/10.1145/322248.322255
    .. [2] https://en.wikipedia.org/wiki/Multiplication#Capital_Pi_notation
    .. [3] https://en.wikipedia.org/wiki/Empty_product
    '''
    limits: tTuple[tTuple[Symbol, Expr, Expr]]
    def __new__(cls, function, *symbols, **assumptions): ...
    @property
    def term(self): ...
    function = term
    def doit(self, **hints): ...
    def is_convergent(self):
        """
        See docs of :obj:`.Sum.is_convergent()` for explanation of convergence
        in SymPy.

        Explanation
        ===========

        The infinite product:

        .. math::

            \\prod_{1 \\leq i < \\infty} f(i)

        is defined by the sequence of partial products:

        .. math::

            \\prod_{i=1}^{n} f(i) = f(1) f(2) \\cdots f(n)

        as n increases without bound. The product converges to a non-zero
        value if and only if the sum:

        .. math::

            \\sum_{1 \\leq i < \\infty} \\log{f(n)}

        converges.

        Examples
        ========

        >>> from sympy import Product, Symbol, cos, pi, exp, oo
        >>> n = Symbol('n', integer=True)
        >>> Product(n/(n + 1), (n, 1, oo)).is_convergent()
        False
        >>> Product(1/n**2, (n, 1, oo)).is_convergent()
        False
        >>> Product(cos(pi/n), (n, 1, oo)).is_convergent()
        True
        >>> Product(exp(-n**2), (n, 1, oo)).is_convergent()
        False

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Infinite_product
        """
    def reverse_order(expr, *indices):
        '''
        Reverse the order of a limit in a Product.

        Explanation
        ===========

        ``reverse_order(expr, *indices)`` reverses some limits in the expression
        ``expr`` which can be either a ``Sum`` or a ``Product``. The selectors in
        the argument ``indices`` specify some indices whose limits get reversed.
        These selectors are either variable names or numerical indices counted
        starting from the inner-most limit tuple.

        Examples
        ========

        >>> from sympy import gamma, Product, simplify, Sum
        >>> from sympy.abc import x, y, a, b, c, d
        >>> P = Product(x, (x, a, b))
        >>> Pr = P.reverse_order(x)
        >>> Pr
        Product(1/x, (x, b + 1, a - 1))
        >>> Pr = Pr.doit()
        >>> Pr
        1/RisingFactorial(b + 1, a - b - 1)
        >>> simplify(Pr.rewrite(gamma))
        Piecewise((gamma(b + 1)/gamma(a), b > -1), ((-1)**(-a + b + 1)*gamma(1 - a)/gamma(-b), True))
        >>> P = P.doit()
        >>> P
        RisingFactorial(a, -a + b + 1)
        >>> simplify(P.rewrite(gamma))
        Piecewise((gamma(b + 1)/gamma(a), a > 0), ((-1)**(-a + b + 1)*gamma(1 - a)/gamma(-b), True))

        While one should prefer variable names when specifying which limits
        to reverse, the index counting notation comes in handy in case there
        are several symbols with the same name.

        >>> S = Sum(x*y, (x, a, b), (y, c, d))
        >>> S
        Sum(x*y, (x, a, b), (y, c, d))
        >>> S0 = S.reverse_order(0)
        >>> S0
        Sum(-x*y, (x, b + 1, a - 1), (y, c, d))
        >>> S1 = S0.reverse_order(1)
        >>> S1
        Sum(x*y, (x, b + 1, a - 1), (y, d + 1, c - 1))

        Of course we can mix both notations:

        >>> Sum(x*y, (x, a, b), (y, 2, 5)).reverse_order(x, 1)
        Sum(x*y, (x, b + 1, a - 1), (y, 6, 1))
        >>> Sum(x*y, (x, a, b), (y, 2, 5)).reverse_order(y, x)
        Sum(x*y, (x, b + 1, a - 1), (y, 6, 1))

        See Also
        ========

        sympy.concrete.expr_with_intlimits.ExprWithIntLimits.index,
        reorder_limit,
        sympy.concrete.expr_with_intlimits.ExprWithIntLimits.reorder

        References
        ==========

        .. [1] Michael Karr, "Summation in Finite Terms", Journal of the ACM,
               Volume 28 Issue 2, April 1981, Pages 305-350
               https://dl.acm.org/doi/10.1145/322248.322255

        '''

def product(*args, **kwargs):
    """
    Compute the product.

    Explanation
    ===========

    The notation for symbols is similar to the notation used in Sum or
    Integral. product(f, (i, a, b)) computes the product of f with
    respect to i from a to b, i.e.,

    ::

                                     b
                                   _____
        product(f(n), (i, a, b)) = |   | f(n)
                                   |   |
                                   i = a

    If it cannot compute the product, it returns an unevaluated Product object.
    Repeated products can be computed by introducing additional symbols tuples::

    Examples
    ========

    >>> from sympy import product, symbols
    >>> i, n, m, k = symbols('i n m k', integer=True)

    >>> product(i, (i, 1, k))
    factorial(k)
    >>> product(m, (i, 1, k))
    m**k
    >>> product(i, (i, 1, k), (k, 1, n))
    Product(factorial(k), (k, 1, n))

    """
