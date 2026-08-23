from _typeshed import Incomplete
from sympy.core import Derivative as Derivative, Mul as Mul, Pow as Pow, S as S, sympify as sympify
from sympy.core.add import Add as Add
from sympy.core.assumptions import assumptions as assumptions
from sympy.core.exprtools import Factors as Factors, gcd_terms as gcd_terms
from sympy.core.function import expand_mul as expand_mul, expand_power_base as expand_power_base
from sympy.core.numbers import Rational as Rational, nan as nan, zoo as zoo
from sympy.core.parameters import global_parameters as global_parameters
from sympy.core.sorting import default_sort_key as default_sort_key, ordered as ordered
from sympy.core.symbol import Dummy as Dummy, Wild as Wild, symbols as symbols
from sympy.functions import exp as exp, log as log, sqrt as sqrt
from sympy.functions.elementary.complexes import Abs as Abs
from sympy.polys import gcd as gcd
from sympy.simplify.sqrtdenest import sqrtdenest as sqrtdenest
from sympy.utilities.iterables import iterable as iterable, sift as sift

def collect(expr, syms, func: Incomplete | None = None, evaluate: Incomplete | None = None, exact: bool = False, distribute_order_term: bool = True):
    """
    Collect additive terms of an expression.

    Explanation
    ===========

    This function collects additive terms of an expression with respect
    to a list of expression up to powers with rational exponents. By the
    term symbol here are meant arbitrary expressions, which can contain
    powers, products, sums etc. In other words symbol is a pattern which
    will be searched for in the expression's terms.

    The input expression is not expanded by :func:`collect`, so user is
    expected to provide an expression in an appropriate form. This makes
    :func:`collect` more predictable as there is no magic happening behind the
    scenes. However, it is important to note, that powers of products are
    converted to products of powers using the :func:`~.expand_power_base`
    function.

    There are two possible types of output. First, if ``evaluate`` flag is
    set, this function will return an expression with collected terms or
    else it will return a dictionary with expressions up to rational powers
    as keys and collected coefficients as values.

    Examples
    ========

    >>> from sympy import S, collect, expand, factor, Wild
    >>> from sympy.abc import a, b, c, x, y

    This function can collect symbolic coefficients in polynomials or
    rational expressions. It will manage to find all integer or rational
    powers of collection variable::

        >>> collect(a*x**2 + b*x**2 + a*x - b*x + c, x)
        c + x**2*(a + b) + x*(a - b)

    The same result can be achieved in dictionary form::

        >>> d = collect(a*x**2 + b*x**2 + a*x - b*x + c, x, evaluate=False)
        >>> d[x**2]
        a + b
        >>> d[x]
        a - b
        >>> d[S.One]
        c

    You can also work with multivariate polynomials. However, remember that
    this function is greedy so it will care only about a single symbol at time,
    in specification order::

        >>> collect(x**2 + y*x**2 + x*y + y + a*y, [x, y])
        x**2*(y + 1) + x*y + y*(a + 1)

    Also more complicated expressions can be used as patterns::

        >>> from sympy import sin, log
        >>> collect(a*sin(2*x) + b*sin(2*x), sin(2*x))
        (a + b)*sin(2*x)

        >>> collect(a*x*log(x) + b*(x*log(x)), x*log(x))
        x*(a + b)*log(x)

    You can use wildcards in the pattern::

        >>> w = Wild('w1')
        >>> collect(a*x**y - b*x**y, w**y)
        x**y*(a - b)

    It is also possible to work with symbolic powers, although it has more
    complicated behavior, because in this case power's base and symbolic part
    of the exponent are treated as a single symbol::

        >>> collect(a*x**c + b*x**c, x)
        a*x**c + b*x**c
        >>> collect(a*x**c + b*x**c, x**c)
        x**c*(a + b)

    However if you incorporate rationals to the exponents, then you will get
    well known behavior::

        >>> collect(a*x**(2*c) + b*x**(2*c), x**c)
        x**(2*c)*(a + b)

    Note also that all previously stated facts about :func:`collect` function
    apply to the exponential function, so you can get::

        >>> from sympy import exp
        >>> collect(a*exp(2*x) + b*exp(2*x), exp(x))
        (a + b)*exp(2*x)

    If you are interested only in collecting specific powers of some symbols
    then set ``exact`` flag to True::

        >>> collect(a*x**7 + b*x**7, x, exact=True)
        a*x**7 + b*x**7
        >>> collect(a*x**7 + b*x**7, x**7, exact=True)
        x**7*(a + b)

    If you want to collect on any object containing symbols, set
    ``exact`` to None:

        >>> collect(x*exp(x) + sin(x)*y + sin(x)*2 + 3*x, x, exact=None)
        x*exp(x) + 3*x + (y + 2)*sin(x)
        >>> collect(a*x*y + x*y + b*x + x, [x, y], exact=None)
        x*y*(a + 1) + x*(b + 1)

    You can also apply this function to differential equations, where
    derivatives of arbitrary order can be collected. Note that if you
    collect with respect to a function or a derivative of a function, all
    derivatives of that function will also be collected. Use
    ``exact=True`` to prevent this from happening::

        >>> from sympy import Derivative as D, collect, Function
        >>> f = Function('f') (x)

        >>> collect(a*D(f,x) + b*D(f,x), D(f,x))
        (a + b)*Derivative(f(x), x)

        >>> collect(a*D(D(f,x),x) + b*D(D(f,x),x), f)
        (a + b)*Derivative(f(x), (x, 2))

        >>> collect(a*D(D(f,x),x) + b*D(D(f,x),x), D(f,x), exact=True)
        a*Derivative(f(x), (x, 2)) + b*Derivative(f(x), (x, 2))

        >>> collect(a*D(f,x) + b*D(f,x) + a*f + b*f, f)
        (a + b)*f(x) + (a + b)*Derivative(f(x), x)

    Or you can even match both derivative order and exponent at the same time::

        >>> collect(a*D(D(f,x),x)**2 + b*D(D(f,x),x)**2, D(f,x))
        (a + b)*Derivative(f(x), (x, 2))**2

    Finally, you can apply a function to each of the collected coefficients.
    For example you can factorize symbolic coefficients of polynomial::

        >>> f = expand((x + a + 1)**3)

        >>> collect(f, x, factor)
        x**3 + 3*x**2*(a + 1) + 3*x*(a + 1)**2 + (a + 1)**3

    .. note:: Arguments are expected to be in expanded form, so you might have
              to call :func:`~.expand` prior to calling this function.

    See Also
    ========

    collect_const, collect_sqrt, rcollect
    """
def rcollect(expr, *vars):
    """
    Recursively collect sums in an expression.

    Examples
    ========

    >>> from sympy.simplify import rcollect
    >>> from sympy.abc import x, y

    >>> expr = (x**2*y + x*y + x + y)/(x + y)

    >>> rcollect(expr, y)
    (x + y*(x**2 + x + 1))/(x + y)

    See Also
    ========

    collect, collect_const, collect_sqrt
    """
def collect_sqrt(expr, evaluate: Incomplete | None = None):
    """Return expr with terms having common square roots collected together.
    If ``evaluate`` is False a count indicating the number of sqrt-containing
    terms will be returned and, if non-zero, the terms of the Add will be
    returned, else the expression itself will be returned as a single term.
    If ``evaluate`` is True, the expression with any collected terms will be
    returned.

    Note: since I = sqrt(-1), it is collected, too.

    Examples
    ========

    >>> from sympy import sqrt
    >>> from sympy.simplify.radsimp import collect_sqrt
    >>> from sympy.abc import a, b

    >>> r2, r3, r5 = [sqrt(i) for i in [2, 3, 5]]
    >>> collect_sqrt(a*r2 + b*r2)
    sqrt(2)*(a + b)
    >>> collect_sqrt(a*r2 + b*r2 + a*r3 + b*r3)
    sqrt(2)*(a + b) + sqrt(3)*(a + b)
    >>> collect_sqrt(a*r2 + b*r2 + a*r3 + b*r5)
    sqrt(3)*a + sqrt(5)*b + sqrt(2)*(a + b)

    If evaluate is False then the arguments will be sorted and
    returned as a list and a count of the number of sqrt-containing
    terms will be returned:

    >>> collect_sqrt(a*r2 + b*r2 + a*r3 + b*r5, evaluate=False)
    ((sqrt(3)*a, sqrt(5)*b, sqrt(2)*(a + b)), 3)
    >>> collect_sqrt(a*sqrt(2) + b, evaluate=False)
    ((b, sqrt(2)*a), 1)
    >>> collect_sqrt(a + b, evaluate=False)
    ((a + b,), 0)

    See Also
    ========

    collect, collect_const, rcollect
    """
def collect_abs(expr):
    """Return ``expr`` with arguments of multiple Abs in a term collected
    under a single instance.

    Examples
    ========

    >>> from sympy.simplify.radsimp import collect_abs
    >>> from sympy.abc import x
    >>> collect_abs(abs(x + 1)/abs(x**2 - 1))
    Abs((x + 1)/(x**2 - 1))
    >>> collect_abs(abs(1/x))
    Abs(1/x)
    """
def collect_const(expr, *vars, Numbers: bool = True):
    """A non-greedy collection of terms with similar number coefficients in
    an Add expr. If ``vars`` is given then only those constants will be
    targeted. Although any Number can also be targeted, if this is not
    desired set ``Numbers=False`` and no Float or Rational will be collected.

    Parameters
    ==========

    expr : SymPy expression
        This parameter defines the expression the expression from which
        terms with similar coefficients are to be collected. A non-Add
        expression is returned as it is.

    vars : variable length collection of Numbers, optional
        Specifies the constants to target for collection. Can be multiple in
        number.

    Numbers : bool
        Specifies to target all instance of
        :class:`sympy.core.numbers.Number` class. If ``Numbers=False``, then
        no Float or Rational will be collected.

    Returns
    =======

    expr : Expr
        Returns an expression with similar coefficient terms collected.

    Examples
    ========

    >>> from sympy import sqrt
    >>> from sympy.abc import s, x, y, z
    >>> from sympy.simplify.radsimp import collect_const
    >>> collect_const(sqrt(3) + sqrt(3)*(1 + sqrt(2)))
    sqrt(3)*(sqrt(2) + 2)
    >>> collect_const(sqrt(3)*s + sqrt(7)*s + sqrt(3) + sqrt(7))
    (sqrt(3) + sqrt(7))*(s + 1)
    >>> s = sqrt(2) + 2
    >>> collect_const(sqrt(3)*s + sqrt(3) + sqrt(7)*s + sqrt(7))
    (sqrt(2) + 3)*(sqrt(3) + sqrt(7))
    >>> collect_const(sqrt(3)*s + sqrt(3) + sqrt(7)*s + sqrt(7), sqrt(3))
    sqrt(7) + sqrt(3)*(sqrt(2) + 3) + sqrt(7)*(sqrt(2) + 2)

    The collection is sign-sensitive, giving higher precedence to the
    unsigned values:

    >>> collect_const(x - y - z)
    x - (y + z)
    >>> collect_const(-y - z)
    -(y + z)
    >>> collect_const(2*x - 2*y - 2*z, 2)
    2*(x - y - z)
    >>> collect_const(2*x - 2*y - 2*z, -2)
    2*x - 2*(y + z)

    See Also
    ========

    collect, collect_sqrt, rcollect
    """
def radsimp(expr, symbolic: bool = True, max_terms: int = 4):
    """
    Rationalize the denominator by removing square roots.

    Explanation
    ===========

    The expression returned from radsimp must be used with caution
    since if the denominator contains symbols, it will be possible to make
    substitutions that violate the assumptions of the simplification process:
    that for a denominator matching a + b*sqrt(c), a != +/-b*sqrt(c). (If
    there are no symbols, this assumptions is made valid by collecting terms
    of sqrt(c) so the match variable ``a`` does not contain ``sqrt(c)``.) If
    you do not want the simplification to occur for symbolic denominators, set
    ``symbolic`` to False.

    If there are more than ``max_terms`` radical terms then the expression is
    returned unchanged.

    Examples
    ========

    >>> from sympy import radsimp, sqrt, Symbol, pprint
    >>> from sympy import factor_terms, fraction, signsimp
    >>> from sympy.simplify.radsimp import collect_sqrt
    >>> from sympy.abc import a, b, c

    >>> radsimp(1/(2 + sqrt(2)))
    (2 - sqrt(2))/2
    >>> x,y = map(Symbol, 'xy')
    >>> e = ((2 + 2*sqrt(2))*x + (2 + sqrt(8))*y)/(2 + sqrt(2))
    >>> radsimp(e)
    sqrt(2)*(x + y)

    No simplification beyond removal of the gcd is done. One might
    want to polish the result a little, however, by collecting
    square root terms:

    >>> r2 = sqrt(2)
    >>> r5 = sqrt(5)
    >>> ans = radsimp(1/(y*r2 + x*r2 + a*r5 + b*r5)); pprint(ans)
        ___       ___       ___       ___
      \\/ 5 *a + \\/ 5 *b - \\/ 2 *x - \\/ 2 *y
    ------------------------------------------
       2               2      2              2
    5*a  + 10*a*b + 5*b  - 2*x  - 4*x*y - 2*y

    >>> n, d = fraction(ans)
    >>> pprint(factor_terms(signsimp(collect_sqrt(n))/d, radical=True))
            ___             ___
          \\/ 5 *(a + b) - \\/ 2 *(x + y)
    ------------------------------------------
       2               2      2              2
    5*a  + 10*a*b + 5*b  - 2*x  - 4*x*y - 2*y

    If radicals in the denominator cannot be removed or there is no denominator,
    the original expression will be returned.

    >>> radsimp(sqrt(2)*x + sqrt(2))
    sqrt(2)*x + sqrt(2)

    Results with symbols will not always be valid for all substitutions:

    >>> eq = 1/(a + b*sqrt(c))
    >>> eq.subs(a, b*sqrt(c))
    1/(2*b*sqrt(c))
    >>> radsimp(eq).subs(a, b*sqrt(c))
    nan

    If ``symbolic=False``, symbolic denominators will not be transformed (but
    numeric denominators will still be processed):

    >>> radsimp(eq, symbolic=False)
    1/(a + b*sqrt(c))

    """
def rad_rationalize(num, den):
    """
    Rationalize ``num/den`` by removing square roots in the denominator;
    num and den are sum of terms whose squares are positive rationals.

    Examples
    ========

    >>> from sympy import sqrt
    >>> from sympy.simplify.radsimp import rad_rationalize
    >>> rad_rationalize(sqrt(3), 1 + sqrt(2)/3)
    (-sqrt(3) + sqrt(6)/3, -7/9)
    """
def fraction(expr, exact: bool = False):
    """Returns a pair with expression's numerator and denominator.
       If the given expression is not a fraction then this function
       will return the tuple (expr, 1).

       This function will not make any attempt to simplify nested
       fractions or to do any term rewriting at all.

       If only one of the numerator/denominator pair is needed then
       use numer(expr) or denom(expr) functions respectively.

       >>> from sympy import fraction, Rational, Symbol
       >>> from sympy.abc import x, y

       >>> fraction(x/y)
       (x, y)
       >>> fraction(x)
       (x, 1)

       >>> fraction(1/y**2)
       (1, y**2)

       >>> fraction(x*y/2)
       (x*y, 2)
       >>> fraction(Rational(1, 2))
       (1, 2)

       This function will also work fine with assumptions:

       >>> k = Symbol('k', negative=True)
       >>> fraction(x * y**k)
       (x, y**(-k))

       If we know nothing about sign of some exponent and ``exact``
       flag is unset, then structure this exponent's structure will
       be analyzed and pretty fraction will be returned:

       >>> from sympy import exp, Mul
       >>> fraction(2*x**(-y))
       (2, x**y)

       >>> fraction(exp(-x))
       (1, exp(x))

       >>> fraction(exp(-x), exact=True)
       (exp(-x), 1)

       The ``exact`` flag will also keep any unevaluated Muls from
       being evaluated:

       >>> u = Mul(2, x + 1, evaluate=False)
       >>> fraction(u)
       (2*x + 2, 1)
       >>> fraction(u, exact=True)
       (2*(x  + 1), 1)
    """
def numer(expr): ...
def denom(expr): ...
def fraction_expand(expr, **hints): ...
def numer_expand(expr, **hints): ...
def denom_expand(expr, **hints): ...
expand_numer = numer_expand
expand_denom = denom_expand
expand_fraction = fraction_expand

def split_surds(expr):
    """
    Split an expression with terms whose squares are positive rationals
    into a sum of terms whose surds squared have gcd equal to g
    and a sum of terms with surds squared prime with g.

    Examples
    ========

    >>> from sympy import sqrt
    >>> from sympy.simplify.radsimp import split_surds
    >>> split_surds(3*sqrt(3) + sqrt(5)/7 + sqrt(6) + sqrt(10) + sqrt(15))
    (3, sqrt(2) + sqrt(5) + 3, sqrt(5)/7 + sqrt(10))
    """
