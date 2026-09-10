from _typeshed import Incomplete
from sympy import SYMPY_DEBUG as SYMPY_DEBUG
from sympy.core.add import Add as Add
from sympy.core.expr import Expr as Expr
from sympy.core.exprtools import Factors as Factors, factor_terms as factor_terms, gcd_terms as gcd_terms
from sympy.core.function import expand_mul as expand_mul
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import I as I, pi as pi
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy
from sympy.core.sympify import sympify as sympify
from sympy.core.traversal import bottom_up as bottom_up
from sympy.functions.combinatorial.factorials import binomial as binomial
from sympy.functions.elementary.hyperbolic import HyperbolicFunction as HyperbolicFunction, cosh as cosh, coth as coth, csch as csch, sech as sech, sinh as sinh, tanh as tanh
from sympy.functions.elementary.trigonometric import TrigonometricFunction as TrigonometricFunction, cos as cos, cot as cot, csc as csc, sec as sec, sin as sin, sqrt as sqrt, tan as tan
from sympy.ntheory.factor_ import perfect_power as perfect_power
from sympy.polys.polytools import factor as factor
from sympy.strategies.core import debug as debug, identity as identity
from sympy.strategies.tree import greedy as greedy

def TR0(rv):
    """Simplification of rational polynomials, trying to simplify
    the expression, e.g. combine things like 3*x + 2*x, etc....
    """
def TR1(rv):
    """Replace sec, csc with 1/cos, 1/sin

    Examples
    ========

    >>> from sympy.simplify.fu import TR1, sec, csc
    >>> from sympy.abc import x
    >>> TR1(2*csc(x) + sec(x))
    1/cos(x) + 2/sin(x)
    """
def TR2(rv):
    """Replace tan and cot with sin/cos and cos/sin

    Examples
    ========

    >>> from sympy.simplify.fu import TR2
    >>> from sympy.abc import x
    >>> from sympy import tan, cot, sin, cos
    >>> TR2(tan(x))
    sin(x)/cos(x)
    >>> TR2(cot(x))
    cos(x)/sin(x)
    >>> TR2(tan(tan(x) - sin(x)/cos(x)))
    0

    """
def TR2i(rv, half: bool = False):
    """Converts ratios involving sin and cos as follows::
        sin(x)/cos(x) -> tan(x)
        sin(x)/(cos(x) + 1) -> tan(x/2) if half=True

    Examples
    ========

    >>> from sympy.simplify.fu import TR2i
    >>> from sympy.abc import x, a
    >>> from sympy import sin, cos
    >>> TR2i(sin(x)/cos(x))
    tan(x)

    Powers of the numerator and denominator are also recognized

    >>> TR2i(sin(x)**2/(cos(x) + 1)**2, half=True)
    tan(x/2)**2

    The transformation does not take place unless assumptions allow
    (i.e. the base must be positive or the exponent must be an integer
    for both numerator and denominator)

    >>> TR2i(sin(x)**a/(cos(x) + 1)**a)
    sin(x)**a/(cos(x) + 1)**a

    """
def TR3(rv):
    """Induced formula: example sin(-a) = -sin(a)

    Examples
    ========

    >>> from sympy.simplify.fu import TR3
    >>> from sympy.abc import x, y
    >>> from sympy import pi
    >>> from sympy import cos
    >>> TR3(cos(y - x*(y - x)))
    cos(x*(x - y) + y)
    >>> cos(pi/2 + x)
    -sin(x)
    >>> cos(30*pi/2 + x)
    -cos(x)

    """
def TR4(rv):
    """Identify values of special angles.

        a=  0   pi/6        pi/4        pi/3        pi/2
    ----------------------------------------------------
    sin(a)  0   1/2         sqrt(2)/2   sqrt(3)/2   1
    cos(a)  1   sqrt(3)/2   sqrt(2)/2   1/2         0
    tan(a)  0   sqt(3)/3    1           sqrt(3)     --

    Examples
    ========

    >>> from sympy import pi
    >>> from sympy import cos, sin, tan, cot
    >>> for s in (0, pi/6, pi/4, pi/3, pi/2):
    ...    print('%s %s %s %s' % (cos(s), sin(s), tan(s), cot(s)))
    ...
    1 0 0 zoo
    sqrt(3)/2 1/2 sqrt(3)/3 sqrt(3)
    sqrt(2)/2 sqrt(2)/2 1 1
    1/2 sqrt(3)/2 sqrt(3) sqrt(3)/3
    0 1 zoo 0
    """
def TR5(rv, max: int = 4, pow: bool = False):
    """Replacement of sin**2 with 1 - cos(x)**2.

    See _TR56 docstring for advanced use of ``max`` and ``pow``.

    Examples
    ========

    >>> from sympy.simplify.fu import TR5
    >>> from sympy.abc import x
    >>> from sympy import sin
    >>> TR5(sin(x)**2)
    1 - cos(x)**2
    >>> TR5(sin(x)**-2)  # unchanged
    sin(x)**(-2)
    >>> TR5(sin(x)**4)
    (1 - cos(x)**2)**2
    """
def TR6(rv, max: int = 4, pow: bool = False):
    """Replacement of cos**2 with 1 - sin(x)**2.

    See _TR56 docstring for advanced use of ``max`` and ``pow``.

    Examples
    ========

    >>> from sympy.simplify.fu import TR6
    >>> from sympy.abc import x
    >>> from sympy import cos
    >>> TR6(cos(x)**2)
    1 - sin(x)**2
    >>> TR6(cos(x)**-2)  #unchanged
    cos(x)**(-2)
    >>> TR6(cos(x)**4)
    (1 - sin(x)**2)**2
    """
def TR7(rv):
    """Lowering the degree of cos(x)**2.

    Examples
    ========

    >>> from sympy.simplify.fu import TR7
    >>> from sympy.abc import x
    >>> from sympy import cos
    >>> TR7(cos(x)**2)
    cos(2*x)/2 + 1/2
    >>> TR7(cos(x)**2 + 1)
    cos(2*x)/2 + 3/2

    """
def TR8(rv, first: bool = True):
    """Converting products of ``cos`` and/or ``sin`` to a sum or
    difference of ``cos`` and or ``sin`` terms.

    Examples
    ========

    >>> from sympy.simplify.fu import TR8
    >>> from sympy import cos, sin
    >>> TR8(cos(2)*cos(3))
    cos(5)/2 + cos(1)/2
    >>> TR8(cos(2)*sin(3))
    sin(5)/2 + sin(1)/2
    >>> TR8(sin(2)*sin(3))
    -cos(5)/2 + cos(1)/2
    """
def TR9(rv):
    """Sum of ``cos`` or ``sin`` terms as a product of ``cos`` or ``sin``.

    Examples
    ========

    >>> from sympy.simplify.fu import TR9
    >>> from sympy import cos, sin
    >>> TR9(cos(1) + cos(2))
    2*cos(1/2)*cos(3/2)
    >>> TR9(cos(1) + 2*sin(1) + 2*sin(2))
    cos(1) + 4*sin(3/2)*cos(1/2)

    If no change is made by TR9, no re-arrangement of the
    expression will be made. For example, though factoring
    of common term is attempted, if the factored expression
    was not changed, the original expression will be returned:

    >>> TR9(cos(3) + cos(3)*cos(2))
    cos(3) + cos(2)*cos(3)

    """
def TR10(rv, first: bool = True):
    """Separate sums in ``cos`` and ``sin``.

    Examples
    ========

    >>> from sympy.simplify.fu import TR10
    >>> from sympy.abc import a, b, c
    >>> from sympy import cos, sin
    >>> TR10(cos(a + b))
    -sin(a)*sin(b) + cos(a)*cos(b)
    >>> TR10(sin(a + b))
    sin(a)*cos(b) + sin(b)*cos(a)
    >>> TR10(sin(a + b + c))
    (-sin(a)*sin(b) + cos(a)*cos(b))*sin(c) +     (sin(a)*cos(b) + sin(b)*cos(a))*cos(c)
    """
def TR10i(rv):
    """Sum of products to function of sum.

    Examples
    ========

    >>> from sympy.simplify.fu import TR10i
    >>> from sympy import cos, sin, sqrt
    >>> from sympy.abc import x

    >>> TR10i(cos(1)*cos(3) + sin(1)*sin(3))
    cos(2)
    >>> TR10i(cos(1)*sin(3) + sin(1)*cos(3) + cos(3))
    cos(3) + sin(4)
    >>> TR10i(sqrt(2)*cos(x)*x + sqrt(6)*sin(x)*x)
    2*sqrt(2)*x*sin(x + pi/6)

    """
def TR11(rv, base: Incomplete | None = None):
    """Function of double angle to product. The ``base`` argument can be used
    to indicate what is the un-doubled argument, e.g. if 3*pi/7 is the base
    then cosine and sine functions with argument 6*pi/7 will be replaced.

    Examples
    ========

    >>> from sympy.simplify.fu import TR11
    >>> from sympy import cos, sin, pi
    >>> from sympy.abc import x
    >>> TR11(sin(2*x))
    2*sin(x)*cos(x)
    >>> TR11(cos(2*x))
    -sin(x)**2 + cos(x)**2
    >>> TR11(sin(4*x))
    4*(-sin(x)**2 + cos(x)**2)*sin(x)*cos(x)
    >>> TR11(sin(4*x/3))
    4*(-sin(x/3)**2 + cos(x/3)**2)*sin(x/3)*cos(x/3)

    If the arguments are simply integers, no change is made
    unless a base is provided:

    >>> TR11(cos(2))
    cos(2)
    >>> TR11(cos(4), 2)
    -sin(2)**2 + cos(2)**2

    There is a subtle issue here in that autosimplification will convert
    some higher angles to lower angles

    >>> cos(6*pi/7) + cos(3*pi/7)
    -cos(pi/7) + cos(3*pi/7)

    The 6*pi/7 angle is now pi/7 but can be targeted with TR11 by supplying
    the 3*pi/7 base:

    >>> TR11(_, 3*pi/7)
    -sin(3*pi/7)**2 + cos(3*pi/7)**2 + cos(3*pi/7)

    """
def TR12(rv, first: bool = True):
    """Separate sums in ``tan``.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy import tan
    >>> from sympy.simplify.fu import TR12
    >>> TR12(tan(x + y))
    (tan(x) + tan(y))/(-tan(x)*tan(y) + 1)
    """
def TR12i(rv):
    """Combine tan arguments as
    (tan(y) + tan(x))/(tan(x)*tan(y) - 1) -> -tan(x + y).

    Examples
    ========

    >>> from sympy.simplify.fu import TR12i
    >>> from sympy import tan
    >>> from sympy.abc import a, b, c
    >>> ta, tb, tc = [tan(i) for i in (a, b, c)]
    >>> TR12i((ta + tb)/(-ta*tb + 1))
    tan(a + b)
    >>> TR12i((ta + tb)/(ta*tb - 1))
    -tan(a + b)
    >>> TR12i((-ta - tb)/(ta*tb - 1))
    tan(a + b)
    >>> eq = (ta + tb)/(-ta*tb + 1)**2*(-3*ta - 3*tc)/(2*(ta*tc - 1))
    >>> TR12i(eq.expand())
    -3*tan(a + b)*tan(a + c)/(2*(tan(a) + tan(b) - 1))
    """
def TR13(rv):
    """Change products of ``tan`` or ``cot``.

    Examples
    ========

    >>> from sympy.simplify.fu import TR13
    >>> from sympy import tan, cot
    >>> TR13(tan(3)*tan(2))
    -tan(2)/tan(5) - tan(3)/tan(5) + 1
    >>> TR13(cot(3)*cot(2))
    cot(2)*cot(5) + 1 + cot(3)*cot(5)
    """
def TRmorrie(rv):
    """Returns cos(x)*cos(2*x)*...*cos(2**(k-1)*x) -> sin(2**k*x)/(2**k*sin(x))

    Examples
    ========

    >>> from sympy.simplify.fu import TRmorrie, TR8, TR3
    >>> from sympy.abc import x
    >>> from sympy import Mul, cos, pi
    >>> TRmorrie(cos(x)*cos(2*x))
    sin(4*x)/(4*sin(x))
    >>> TRmorrie(7*Mul(*[cos(x) for x in range(10)]))
    7*sin(12)*sin(16)*cos(5)*cos(7)*cos(9)/(64*sin(1)*sin(3))

    Sometimes autosimplification will cause a power to be
    not recognized. e.g. in the following, cos(4*pi/7) automatically
    simplifies to -cos(3*pi/7) so only 2 of the 3 terms are
    recognized:

    >>> TRmorrie(cos(pi/7)*cos(2*pi/7)*cos(4*pi/7))
    -sin(3*pi/7)*cos(3*pi/7)/(4*sin(pi/7))

    A touch by TR8 resolves the expression to a Rational

    >>> TR8(_)
    -1/8

    In this case, if eq is unsimplified, the answer is obtained
    directly:

    >>> eq = cos(pi/9)*cos(2*pi/9)*cos(3*pi/9)*cos(4*pi/9)
    >>> TRmorrie(eq)
    1/16

    But if angles are made canonical with TR3 then the answer
    is not simplified without further work:

    >>> TR3(eq)
    sin(pi/18)*cos(pi/9)*cos(2*pi/9)/2
    >>> TRmorrie(_)
    sin(pi/18)*sin(4*pi/9)/(8*sin(pi/9))
    >>> TR8(_)
    cos(7*pi/18)/(16*sin(pi/9))
    >>> TR3(_)
    1/16

    The original expression would have resolve to 1/16 directly with TR8,
    however:

    >>> TR8(eq)
    1/16

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Morrie%27s_law

    """
def TR14(rv, first: bool = True):
    """Convert factored powers of sin and cos identities into simpler
    expressions.

    Examples
    ========

    >>> from sympy.simplify.fu import TR14
    >>> from sympy.abc import x, y
    >>> from sympy import cos, sin
    >>> TR14((cos(x) - 1)*(cos(x) + 1))
    -sin(x)**2
    >>> TR14((sin(x) - 1)*(sin(x) + 1))
    -cos(x)**2
    >>> p1 = (cos(x) + 1)*(cos(x) - 1)
    >>> p2 = (cos(y) - 1)*2*(cos(y) + 1)
    >>> p3 = (3*(cos(y) - 1))*(3*(cos(y) + 1))
    >>> TR14(p1*p2*p3*(x - 1))
    -18*(x - 1)*sin(x)**2*sin(y)**4

    """
def TR15(rv, max: int = 4, pow: bool = False):
    """Convert sin(x)**-2 to 1 + cot(x)**2.

    See _TR56 docstring for advanced use of ``max`` and ``pow``.

    Examples
    ========

    >>> from sympy.simplify.fu import TR15
    >>> from sympy.abc import x
    >>> from sympy import sin
    >>> TR15(1 - 1/sin(x)**2)
    -cot(x)**2

    """
def TR16(rv, max: int = 4, pow: bool = False):
    """Convert cos(x)**-2 to 1 + tan(x)**2.

    See _TR56 docstring for advanced use of ``max`` and ``pow``.

    Examples
    ========

    >>> from sympy.simplify.fu import TR16
    >>> from sympy.abc import x
    >>> from sympy import cos
    >>> TR16(1 - 1/cos(x)**2)
    -tan(x)**2

    """
def TR111(rv):
    """Convert f(x)**-i to g(x)**i where either ``i`` is an integer
    or the base is positive and f, g are: tan, cot; sin, csc; or cos, sec.

    Examples
    ========

    >>> from sympy.simplify.fu import TR111
    >>> from sympy.abc import x
    >>> from sympy import tan
    >>> TR111(1 - 1/tan(x)**2)
    1 - cot(x)**2

    """
def TR22(rv, max: int = 4, pow: bool = False):
    """Convert tan(x)**2 to sec(x)**2 - 1 and cot(x)**2 to csc(x)**2 - 1.

    See _TR56 docstring for advanced use of ``max`` and ``pow``.

    Examples
    ========

    >>> from sympy.simplify.fu import TR22
    >>> from sympy.abc import x
    >>> from sympy import tan, cot
    >>> TR22(1 + tan(x)**2)
    sec(x)**2
    >>> TR22(1 + cot(x)**2)
    csc(x)**2

    """
def TRpower(rv):
    """Convert sin(x)**n and cos(x)**n with positive n to sums.

    Examples
    ========

    >>> from sympy.simplify.fu import TRpower
    >>> from sympy.abc import x
    >>> from sympy import cos, sin
    >>> TRpower(sin(x)**6)
    -15*cos(2*x)/32 + 3*cos(4*x)/16 - cos(6*x)/32 + 5/16
    >>> TRpower(sin(x)**3*cos(2*x)**4)
    (3*sin(x)/4 - sin(3*x)/4)*(cos(4*x)/2 + cos(8*x)/8 + 3/8)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/List_of_trigonometric_identities#Power-reduction_formulae

    """
def L(rv):
    """Return count of trigonometric functions in expression.

    Examples
    ========

    >>> from sympy.simplify.fu import L
    >>> from sympy.abc import x
    >>> from sympy import cos, sin
    >>> L(cos(x)+sin(x))
    2
    """

TR0: Incomplete
TR1: Incomplete
TR2: Incomplete
TR3: Incomplete
TR4: Incomplete
TR5: Incomplete
TR6: Incomplete
TR7: Incomplete
TR8: Incomplete
TR9: Incomplete
TR10: Incomplete
TR11: Incomplete
TR12: Incomplete
TR13: Incomplete
TR2i: Incomplete
TRmorrie: Incomplete
TR14: Incomplete
TR15: Incomplete
TR16: Incomplete
TR12i: Incomplete
TR111: Incomplete
TR22: Incomplete
CTR1: Incomplete
CTR2: Incomplete
CTR3: Incomplete
CTR4: Incomplete
RL1: Incomplete
RL2: Incomplete

def fu(rv, measure=...):
    """Attempt to simplify expression by using transformation rules given
    in the algorithm by Fu et al.

    :func:`fu` will try to minimize the objective function ``measure``.
    By default this first minimizes the number of trig terms and then minimizes
    the number of total operations.

    Examples
    ========

    >>> from sympy.simplify.fu import fu
    >>> from sympy import cos, sin, tan, pi, S, sqrt
    >>> from sympy.abc import x, y, a, b

    >>> fu(sin(50)**2 + cos(50)**2 + sin(pi/6))
    3/2
    >>> fu(sqrt(6)*cos(x) + sqrt(2)*sin(x))
    2*sqrt(2)*sin(x + pi/3)

    CTR1 example

    >>> eq = sin(x)**4 - cos(y)**2 + sin(y)**2 + 2*cos(x)**2
    >>> fu(eq)
    cos(x)**4 - 2*cos(y)**2 + 2

    CTR2 example

    >>> fu(S.Half - cos(2*x)/2)
    sin(x)**2

    CTR3 example

    >>> fu(sin(a)*(cos(b) - sin(b)) + cos(a)*(sin(b) + cos(b)))
    sqrt(2)*sin(a + b + pi/4)

    CTR4 example

    >>> fu(sqrt(3)*cos(x)/2 + sin(x)/2)
    sin(x + pi/3)

    Example 1

    >>> fu(1-sin(2*x)**2/4-sin(y)**2-cos(x)**4)
    -cos(x)**2 + cos(y)**2

    Example 2

    >>> fu(cos(4*pi/9))
    sin(pi/18)
    >>> fu(cos(pi/9)*cos(2*pi/9)*cos(3*pi/9)*cos(4*pi/9))
    1/16

    Example 3

    >>> fu(tan(7*pi/18)+tan(5*pi/18)-sqrt(3)*tan(5*pi/18)*tan(7*pi/18))
    -sqrt(3)

    Objective function example

    >>> fu(sin(x)/cos(x))  # default objective function
    tan(x)
    >>> fu(sin(x)/cos(x), measure=lambda x: -x.count_ops()) # maximize op count
    sin(x)/cos(x)

    References
    ==========

    .. [1] https://www.sciencedirect.com/science/article/pii/S0895717706001609
    """
def process_common_addends(rv, do, key2: Incomplete | None = None, key1: bool = True):
    """Apply ``do`` to addends of ``rv`` that (if ``key1=True``) share at least
    a common absolute value of their coefficient and the value of ``key2`` when
    applied to the argument. If ``key1`` is False ``key2`` must be supplied and
    will be the only key applied.
    """

fufuncs: Incomplete
FU: Incomplete

def trig_split(a, b, two: bool = False):
    """Return the gcd, s1, s2, a1, a2, bool where

    If two is False (default) then::
        a + b = gcd*(s1*f(a1) + s2*f(a2)) where f = cos if bool else sin
    else:
        if bool, a + b was +/- cos(a1)*cos(a2) +/- sin(a1)*sin(a2) and equals
            n1*gcd*cos(a - b) if n1 == n2 else
            n1*gcd*cos(a + b)
        else a + b was +/- cos(a1)*sin(a2) +/- sin(a1)*cos(a2) and equals
            n1*gcd*sin(a + b) if n1 = n2 else
            n1*gcd*sin(b - a)

    Examples
    ========

    >>> from sympy.simplify.fu import trig_split
    >>> from sympy.abc import x, y, z
    >>> from sympy import cos, sin, sqrt

    >>> trig_split(cos(x), cos(y))
    (1, 1, 1, x, y, True)
    >>> trig_split(2*cos(x), -2*cos(y))
    (2, 1, -1, x, y, True)
    >>> trig_split(cos(x)*sin(y), cos(y)*sin(y))
    (sin(y), 1, 1, x, y, True)

    >>> trig_split(cos(x), -sqrt(3)*sin(x), two=True)
    (2, 1, -1, x, pi/6, False)
    >>> trig_split(cos(x), sin(x), two=True)
    (sqrt(2), 1, 1, x, pi/4, False)
    >>> trig_split(cos(x), -sin(x), two=True)
    (sqrt(2), 1, -1, x, pi/4, False)
    >>> trig_split(sqrt(2)*cos(x), -sqrt(6)*sin(x), two=True)
    (2*sqrt(2), 1, -1, x, pi/6, False)
    >>> trig_split(-sqrt(6)*cos(x), -sqrt(2)*sin(x), two=True)
    (-2*sqrt(2), 1, 1, x, pi/3, False)
    >>> trig_split(cos(x)/sqrt(6), sin(x)/sqrt(2), two=True)
    (sqrt(6)/3, 1, 1, x, pi/6, False)
    >>> trig_split(-sqrt(6)*cos(x)*sin(y), -sqrt(2)*sin(x)*sin(y), two=True)
    (-2*sqrt(2)*sin(y), 1, 1, x, pi/3, False)

    >>> trig_split(cos(x), sin(x))
    >>> trig_split(cos(x), sin(z))
    >>> trig_split(2*cos(x), -sin(x))
    >>> trig_split(cos(x), -sqrt(3)*sin(x))
    >>> trig_split(cos(x)*cos(y), sin(x)*sin(z))
    >>> trig_split(cos(x)*cos(y), sin(x)*sin(y))
    >>> trig_split(-sqrt(6)*cos(x), sqrt(2)*sin(x)*sin(y), two=True)
    """
def as_f_sign_1(e):
    """If ``e`` is a sum that can be written as ``g*(a + s)`` where
    ``s`` is ``+/-1``, return ``g``, ``a``, and ``s`` where ``a`` does
    not have a leading negative coefficient.

    Examples
    ========

    >>> from sympy.simplify.fu import as_f_sign_1
    >>> from sympy.abc import x
    >>> as_f_sign_1(x + 1)
    (1, x, 1)
    >>> as_f_sign_1(x - 1)
    (1, x, -1)
    >>> as_f_sign_1(-x + 1)
    (-1, x, -1)
    >>> as_f_sign_1(-x - 1)
    (-1, x, 1)
    >>> as_f_sign_1(2*x + 2)
    (2, x, 1)
    """
def hyper_as_trig(rv):
    """Return an expression containing hyperbolic functions in terms
    of trigonometric functions. Any trigonometric functions initially
    present are replaced with Dummy symbols and the function to undo
    the masking and the conversion back to hyperbolics is also returned. It
    should always be true that::

        t, f = hyper_as_trig(expr)
        expr == f(t)

    Examples
    ========

    >>> from sympy.simplify.fu import hyper_as_trig, fu
    >>> from sympy.abc import x
    >>> from sympy import cosh, sinh
    >>> eq = sinh(x)**2 + cosh(x)**2
    >>> t, f = hyper_as_trig(eq)
    >>> f(fu(t))
    cosh(2*x)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Hyperbolic_function
    """
def sincos_to_sum(expr):
    """Convert products and powers of sin and cos to sums.

    Explanation
    ===========

    Applied power reduction TRpower first, then expands products, and
    converts products to sums with TR8.

    Examples
    ========

    >>> from sympy.simplify.fu import sincos_to_sum
    >>> from sympy.abc import x
    >>> from sympy import cos, sin
    >>> sincos_to_sum(16*sin(x)**3*cos(2*x)**2)
    7*sin(x) - 5*sin(3*x) + 3*sin(5*x) - sin(7*x)
    """
