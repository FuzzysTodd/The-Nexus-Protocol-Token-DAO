from sympy.core import Add as Add, Basic as Basic, Dummy as Dummy, Mul as Mul, Pow as Pow, S as S, expand_mul as expand_mul, factor_terms as factor_terms, sympify as sympify
from sympy.core.function import count_ops as count_ops, expand_log as expand_log
from sympy.core.numbers import Integer as Integer, Rational as Rational
from sympy.core.rules import Transform as Transform
from sympy.core.sorting import default_sort_key as default_sort_key, ordered as ordered
from sympy.functions import exp as exp, exp_polar as exp_polar, log as log, polarify as polarify, root as root, unpolarify as unpolarify
from sympy.matrices.expressions.matexpr import MatrixSymbol as MatrixSymbol
from sympy.ntheory.factor_ import multiplicity as multiplicity
from sympy.polys import gcd as gcd, lcm as lcm

def powsimp(expr, deep: bool = False, combine: str = 'all', force: bool = False, measure=...):
    """
    Reduce expression by combining powers with similar bases and exponents.

    Explanation
    ===========

    If ``deep`` is ``True`` then powsimp() will also simplify arguments of
    functions. By default ``deep`` is set to ``False``.

    If ``force`` is ``True`` then bases will be combined without checking for
    assumptions, e.g. sqrt(x)*sqrt(y) -> sqrt(x*y) which is not true
    if x and y are both negative.

    You can make powsimp() only combine bases or only combine exponents by
    changing combine='base' or combine='exp'.  By default, combine='all',
    which does both.  combine='base' will only combine::

         a   a          a                          2x      x
        x * y  =>  (x*y)   as well as things like 2   =>  4

    and combine='exp' will only combine
    ::

         a   b      (a + b)
        x * x  =>  x

    combine='exp' will strictly only combine exponents in the way that used
    to be automatic.  Also use deep=True if you need the old behavior.

    When combine='all', 'exp' is evaluated first.  Consider the first
    example below for when there could be an ambiguity relating to this.
    This is done so things like the second example can be completely
    combined.  If you want 'base' combined first, do something like
    powsimp(powsimp(expr, combine='base'), combine='exp').

    Examples
    ========

    >>> from sympy import powsimp, exp, log, symbols
    >>> from sympy.abc import x, y, z, n
    >>> powsimp(x**y*x**z*y**z, combine='all')
    x**(y + z)*y**z
    >>> powsimp(x**y*x**z*y**z, combine='exp')
    x**(y + z)*y**z
    >>> powsimp(x**y*x**z*y**z, combine='base', force=True)
    x**y*(x*y)**z

    >>> powsimp(x**z*x**y*n**z*n**y, combine='all', force=True)
    (n*x)**(y + z)
    >>> powsimp(x**z*x**y*n**z*n**y, combine='exp')
    n**(y + z)*x**(y + z)
    >>> powsimp(x**z*x**y*n**z*n**y, combine='base', force=True)
    (n*x)**y*(n*x)**z

    >>> x, y = symbols('x y', positive=True)
    >>> powsimp(log(exp(x)*exp(y)))
    log(exp(x)*exp(y))
    >>> powsimp(log(exp(x)*exp(y)), deep=True)
    x + y

    Radicals with Mul bases will be combined if combine='exp'

    >>> from sympy import sqrt
    >>> x, y = symbols('x y')

    Two radicals are automatically joined through Mul:

    >>> a=sqrt(x*sqrt(y))
    >>> a*a**3 == a**4
    True

    But if an integer power of that radical has been
    autoexpanded then Mul does not join the resulting factors:

    >>> a**4 # auto expands to a Mul, no longer a Pow
    x**2*y
    >>> _*a # so Mul doesn't combine them
    x**2*y*sqrt(x*sqrt(y))
    >>> powsimp(_) # but powsimp will
    (x*sqrt(y))**(5/2)
    >>> powsimp(x*y*a) # but won't when doing so would violate assumptions
    x*y*sqrt(x*sqrt(y))

    """
def powdenest(eq, force: bool = False, polar: bool = False):
    """
    Collect exponents on powers as assumptions allow.

    Explanation
    ===========

    Given ``(bb**be)**e``, this can be simplified as follows:
        * if ``bb`` is positive, or
        * ``e`` is an integer, or
        * ``|be| < 1`` then this simplifies to ``bb**(be*e)``

    Given a product of powers raised to a power, ``(bb1**be1 *
    bb2**be2...)**e``, simplification can be done as follows:

    - if e is positive, the gcd of all bei can be joined with e;
    - all non-negative bb can be separated from those that are negative
      and their gcd can be joined with e; autosimplification already
      handles this separation.
    - integer factors from powers that have integers in the denominator
      of the exponent can be removed from any term and the gcd of such
      integers can be joined with e

    Setting ``force`` to ``True`` will make symbols that are not explicitly
    negative behave as though they are positive, resulting in more
    denesting.

    Setting ``polar`` to ``True`` will do simplifications on the Riemann surface of
    the logarithm, also resulting in more denestings.

    When there are sums of logs in exp() then a product of powers may be
    obtained e.g. ``exp(3*(log(a) + 2*log(b)))`` - > ``a**3*b**6``.

    Examples
    ========

    >>> from sympy.abc import a, b, x, y, z
    >>> from sympy import Symbol, exp, log, sqrt, symbols, powdenest

    >>> powdenest((x**(2*a/3))**(3*x))
    (x**(2*a/3))**(3*x)
    >>> powdenest(exp(3*x*log(2)))
    2**(3*x)

    Assumptions may prevent expansion:

    >>> powdenest(sqrt(x**2))
    sqrt(x**2)

    >>> p = symbols('p', positive=True)
    >>> powdenest(sqrt(p**2))
    p

    No other expansion is done.

    >>> i, j = symbols('i,j', integer=True)
    >>> powdenest((x**x)**(i + j)) # -X-> (x**x)**i*(x**x)**j
    x**(x*(i + j))

    But exp() will be denested by moving all non-log terms outside of
    the function; this may result in the collapsing of the exp to a power
    with a different base:

    >>> powdenest(exp(3*y*log(x)))
    x**(3*y)
    >>> powdenest(exp(y*(log(a) + log(b))))
    (a*b)**y
    >>> powdenest(exp(3*(log(a) + log(b))))
    a**3*b**3

    If assumptions allow, symbols can also be moved to the outermost exponent:

    >>> i = Symbol('i', integer=True)
    >>> powdenest(((x**(2*i))**(3*y))**x)
    ((x**(2*i))**(3*y))**x
    >>> powdenest(((x**(2*i))**(3*y))**x, force=True)
    x**(6*i*x*y)

    >>> powdenest(((x**(2*a/3))**(3*y/i))**x)
    ((x**(2*a/3))**(3*y/i))**x
    >>> powdenest((x**(2*i)*y**(4*i))**z, force=True)
    (x*y**2)**(2*i*z)

    >>> n = Symbol('n', negative=True)

    >>> powdenest((x**i)**y, force=True)
    x**(i*y)
    >>> powdenest((n**i)**x, force=True)
    (n**i)**x

    """
