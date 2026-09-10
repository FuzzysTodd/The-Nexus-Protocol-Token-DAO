from .libmp import int_types as int_types, sqrt_fixed as sqrt_fixed
from .libmp.backend import xrange as xrange
from _typeshed import Incomplete

def round_fixed(x, prec): ...

class IdentificationMethods: ...

def pslq(ctx, x, tol: Incomplete | None = None, maxcoeff: int = 1000, maxsteps: int = 100, verbose: bool = False):
    '''
    Given a vector of real numbers `x = [x_0, x_1, ..., x_n]`, ``pslq(x)``
    uses the PSLQ algorithm to find a list of integers
    `[c_0, c_1, ..., c_n]` such that

    .. math ::

        |c_1 x_1 + c_2 x_2 + ... + c_n x_n| < \\mathrm{tol}

    and such that `\\max |c_k| < \\mathrm{maxcoeff}`. If no such vector
    exists, :func:`~mpmath.pslq` returns ``None``. The tolerance defaults to
    3/4 of the working precision.

    **Examples**

    Find rational approximations for `\\pi`::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> pslq([-1, pi], tol=0.01)
        [22, 7]
        >>> pslq([-1, pi], tol=0.001)
        [355, 113]
        >>> mpf(22)/7; mpf(355)/113; +pi
        3.14285714285714
        3.14159292035398
        3.14159265358979

    Pi is not a rational number with denominator less than 1000::

        >>> pslq([-1, pi])
        >>>

    To within the standard precision, it can however be approximated
    by at least one rational number with denominator less than `10^{12}`::

        >>> p, q = pslq([-1, pi], maxcoeff=10**12)
        >>> print(p); print(q)
        238410049439
        75888275702
        >>> mpf(p)/q
        3.14159265358979

    The PSLQ algorithm can be applied to long vectors. For example,
    we can investigate the rational (in)dependence of integer square
    roots::

        >>> mp.dps = 30
        >>> pslq([sqrt(n) for n in range(2, 5+1)])
        >>>
        >>> pslq([sqrt(n) for n in range(2, 6+1)])
        >>>
        >>> pslq([sqrt(n) for n in range(2, 8+1)])
        [2, 0, 0, 0, 0, 0, -1]

    **Machin formulas**

    A famous formula for `\\pi` is Machin\'s,

    .. math ::

        \\frac{\\pi}{4} = 4 \\operatorname{acot} 5 - \\operatorname{acot} 239

    There are actually infinitely many formulas of this type. Two
    others are

    .. math ::

        \\frac{\\pi}{4} = \\operatorname{acot} 1

        \\frac{\\pi}{4} = 12 \\operatorname{acot} 49 + 32 \\operatorname{acot} 57
            + 5 \\operatorname{acot} 239 + 12 \\operatorname{acot} 110443

    We can easily verify the formulas using the PSLQ algorithm::

        >>> mp.dps = 30
        >>> pslq([pi/4, acot(1)])
        [1, -1]
        >>> pslq([pi/4, acot(5), acot(239)])
        [1, -4, 1]
        >>> pslq([pi/4, acot(49), acot(57), acot(239), acot(110443)])
        [1, -12, -32, 5, -12]

    We could try to generate a custom Machin-like formula by running
    the PSLQ algorithm with a few inverse cotangent values, for example
    acot(2), acot(3) ... acot(10). Unfortunately, there is a linear
    dependence among these values, resulting in only that dependence
    being detected, with a zero coefficient for `\\pi`::

        >>> pslq([pi] + [acot(n) for n in range(2,11)])
        [0, 1, -1, 0, 0, 0, -1, 0, 0, 0]

    We get better luck by removing linearly dependent terms::

        >>> pslq([pi] + [acot(n) for n in range(2,11) if n not in (3, 5)])
        [1, -8, 0, 0, 4, 0, 0, 0]

    In other words, we found the following formula::

        >>> 8*acot(2) - 4*acot(7)
        3.14159265358979323846264338328
        >>> +pi
        3.14159265358979323846264338328

    **Algorithm**

    This is a fairly direct translation to Python of the pseudocode given by
    David Bailey, "The PSLQ Integer Relation Algorithm":
    http://www.cecm.sfu.ca/organics/papers/bailey/paper/html/node3.html

    The present implementation uses fixed-point instead of floating-point
    arithmetic, since this is significantly (about 7x) faster.
    '''
def findpoly(ctx, x, n: int = 1, **kwargs):
    """
    ``findpoly(x, n)`` returns the coefficients of an integer
    polynomial `P` of degree at most `n` such that `P(x) \\approx 0`.
    If no polynomial having `x` as a root can be found,
    :func:`~mpmath.findpoly` returns ``None``.

    :func:`~mpmath.findpoly` works by successively calling :func:`~mpmath.pslq` with
    the vectors `[1, x]`, `[1, x, x^2]`, `[1, x, x^2, x^3]`, ...,
    `[1, x, x^2, .., x^n]` as input. Keyword arguments given to
    :func:`~mpmath.findpoly` are forwarded verbatim to :func:`~mpmath.pslq`. In
    particular, you can specify a tolerance for `P(x)` with ``tol``
    and a maximum permitted coefficient size with ``maxcoeff``.

    For large values of `n`, it is recommended to run :func:`~mpmath.findpoly`
    at high precision; preferably 50 digits or more.

    **Examples**

    By default (degree `n = 1`), :func:`~mpmath.findpoly` simply finds a linear
    polynomial with a rational root::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> findpoly(0.7)
        [-10, 7]

    The generated coefficient list is valid input to ``polyval`` and
    ``polyroots``::

        >>> nprint(polyval(findpoly(phi, 2), phi), 1)
        -2.0e-16
        >>> for r in polyroots(findpoly(phi, 2)):
        ...     print(r)
        ...
        -0.618033988749895
        1.61803398874989

    Numbers of the form `m + n \\sqrt p` for integers `(m, n, p)` are
    solutions to quadratic equations. As we find here, `1+\\sqrt 2`
    is a root of the polynomial `x^2 - 2x - 1`::

        >>> findpoly(1+sqrt(2), 2)
        [1, -2, -1]
        >>> findroot(lambda x: x**2 - 2*x - 1, 1)
        2.4142135623731

    Despite only containing square roots, the following number results
    in a polynomial of degree 4::

        >>> findpoly(sqrt(2)+sqrt(3), 4)
        [1, 0, -10, 0, 1]

    In fact, `x^4 - 10x^2 + 1` is the *minimal polynomial* of
    `r = \\sqrt 2 + \\sqrt 3`, meaning that a rational polynomial of
    lower degree having `r` as a root does not exist. Given sufficient
    precision, :func:`~mpmath.findpoly` will usually find the correct
    minimal polynomial of a given algebraic number.

    **Non-algebraic numbers**

    If :func:`~mpmath.findpoly` fails to find a polynomial with given
    coefficient size and tolerance constraints, that means no such
    polynomial exists.

    We can verify that `\\pi` is not an algebraic number of degree 3 with
    coefficients less than 1000::

        >>> mp.dps = 15
        >>> findpoly(pi, 3)
        >>>

    It is always possible to find an algebraic approximation of a number
    using one (or several) of the following methods:

        1. Increasing the permitted degree
        2. Allowing larger coefficients
        3. Reducing the tolerance

    One example of each method is shown below::

        >>> mp.dps = 15
        >>> findpoly(pi, 4)
        [95, -545, 863, -183, -298]
        >>> findpoly(pi, 3, maxcoeff=10000)
        [836, -1734, -2658, -457]
        >>> findpoly(pi, 3, tol=1e-7)
        [-4, 22, -29, -2]

    It is unknown whether Euler's constant is transcendental (or even
    irrational). We can use :func:`~mpmath.findpoly` to check that if is
    an algebraic number, its minimal polynomial must have degree
    at least 7 and a coefficient of magnitude at least 1000000::

        >>> mp.dps = 200
        >>> findpoly(euler, 6, maxcoeff=10**6, tol=1e-100, maxsteps=1000)
        >>>

    Note that the high precision and strict tolerance is necessary
    for such high-degree runs, since otherwise unwanted low-accuracy
    approximations will be detected. It may also be necessary to set
    maxsteps high to prevent a premature exit (before the coefficient
    bound has been reached). Running with ``verbose=True`` to get an
    idea what is happening can be useful.
    """
def fracgcd(p, q): ...
def pslqstring(r, constants): ...
def prodstring(r, constants): ...
def quadraticstring(ctx, t, a, b, c): ...

transforms: Incomplete

def identify(ctx, x, constants=[], tol: Incomplete | None = None, maxcoeff: int = 1000, full: bool = False, verbose: bool = False):
    '''
    Given a real number `x`, ``identify(x)`` attempts to find an exact
    formula for `x`. This formula is returned as a string. If no match
    is found, ``None`` is returned. With ``full=True``, a list of
    matching formulas is returned.

    As a simple example, :func:`~mpmath.identify` will find an algebraic
    formula for the golden ratio::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> identify(phi)
        \'((1+sqrt(5))/2)\'

    :func:`~mpmath.identify` can identify simple algebraic numbers and simple
    combinations of given base constants, as well as certain basic
    transformations thereof. More specifically, :func:`~mpmath.identify`
    looks for the following:

        1. Fractions
        2. Quadratic algebraic numbers
        3. Rational linear combinations of the base constants
        4. Any of the above after first transforming `x` into `f(x)` where
           `f(x)` is `1/x`, `\\sqrt x`, `x^2`, `\\log x` or `\\exp x`, either
           directly or with `x` or `f(x)` multiplied or divided by one of
           the base constants
        5. Products of fractional powers of the base constants and
           small integers

    Base constants can be given as a list of strings representing mpmath
    expressions (:func:`~mpmath.identify` will ``eval`` the strings to numerical
    values and use the original strings for the output), or as a dict of
    formula:value pairs.

    In order not to produce spurious results, :func:`~mpmath.identify` should
    be used with high precision; preferably 50 digits or more.

    **Examples**

    Simple identifications can be performed safely at standard
    precision. Here the default recognition of rational, algebraic,
    and exp/log of algebraic numbers is demonstrated::

        >>> mp.dps = 15
        >>> identify(0.22222222222222222)
        \'(2/9)\'
        >>> identify(1.9662210973805663)
        \'sqrt(((24+sqrt(48))/8))\'
        >>> identify(4.1132503787829275)
        \'exp((sqrt(8)/2))\'
        >>> identify(0.881373587019543)
        \'log(((2+sqrt(8))/2))\'

    By default, :func:`~mpmath.identify` does not recognize `\\pi`. At standard
    precision it finds a not too useful approximation. At slightly
    increased precision, this approximation is no longer accurate
    enough and :func:`~mpmath.identify` more correctly returns ``None``::

        >>> identify(pi)
        \'(2**(176/117)*3**(20/117)*5**(35/39))/(7**(92/117))\'
        >>> mp.dps = 30
        >>> identify(pi)
        >>>

    Numbers such as `\\pi`, and simple combinations of user-defined
    constants, can be identified if they are provided explicitly::

        >>> identify(3*pi-2*e, [\'pi\', \'e\'])
        \'(3*pi + (-2)*e)\'

    Here is an example using a dict of constants. Note that the
    constants need not be "atomic"; :func:`~mpmath.identify` can just
    as well express the given number in terms of expressions
    given by formulas::

        >>> identify(pi+e, {\'a\':pi+2, \'b\':2*e})
        \'((-2) + 1*a + (1/2)*b)\'

    Next, we attempt some identifications with a set of base constants.
    It is necessary to increase the precision a bit.

        >>> mp.dps = 50
        >>> base = [\'sqrt(2)\',\'pi\',\'log(2)\']
        >>> identify(0.25, base)
        \'(1/4)\'
        >>> identify(3*pi + 2*sqrt(2) + 5*log(2)/7, base)
        \'(2*sqrt(2) + 3*pi + (5/7)*log(2))\'
        >>> identify(exp(pi+2), base)
        \'exp((2 + 1*pi))\'
        >>> identify(1/(3+sqrt(2)), base)
        \'((3/7) + (-1/7)*sqrt(2))\'
        >>> identify(sqrt(2)/(3*pi+4), base)
        \'sqrt(2)/(4 + 3*pi)\'
        >>> identify(5**(mpf(1)/3)*pi*log(2)**2, base)
        \'5**(1/3)*pi*log(2)**2\'

    An example of an erroneous solution being found when too low
    precision is used::

        >>> mp.dps = 15
        >>> identify(1/(3*pi-4*e+sqrt(8)), [\'pi\', \'e\', \'sqrt(2)\'])
        \'((11/25) + (-158/75)*pi + (76/75)*e + (44/15)*sqrt(2))\'
        >>> mp.dps = 50
        >>> identify(1/(3*pi-4*e+sqrt(8)), [\'pi\', \'e\', \'sqrt(2)\'])
        \'1/(3*pi + (-4)*e + 2*sqrt(2))\'

    **Finding approximate solutions**

    The tolerance ``tol`` defaults to 3/4 of the working precision.
    Lowering the tolerance is useful for finding approximate matches.
    We can for example try to generate approximations for pi::

        >>> mp.dps = 15
        >>> identify(pi, tol=1e-2)
        \'(22/7)\'
        >>> identify(pi, tol=1e-3)
        \'(355/113)\'
        >>> identify(pi, tol=1e-10)
        \'(5**(339/269))/(2**(64/269)*3**(13/269)*7**(92/269))\'

    With ``full=True``, and by supplying a few base constants,
    ``identify`` can generate almost endless lists of approximations
    for any number (the output below has been truncated to show only
    the first few)::

        >>> for p in identify(pi, [\'e\', \'catalan\'], tol=1e-5, full=True):
        ...     print(p)
        ...  # doctest: +ELLIPSIS
        e/log((6 + (-4/3)*e))
        (3**3*5*e*catalan**2)/(2*7**2)
        sqrt(((-13) + 1*e + 22*catalan))
        log(((-6) + 24*e + 4*catalan)/e)
        exp(catalan*((-1/5) + (8/15)*e))
        catalan*(6 + (-6)*e + 15*catalan)
        sqrt((5 + 26*e + (-3)*catalan))/e
        e*sqrt(((-27) + 2*e + 25*catalan))
        log(((-1) + (-11)*e + 59*catalan))
        ((3/20) + (21/20)*e + (3/20)*catalan)
        ...

    The numerical values are roughly as close to `\\pi` as permitted by the
    specified tolerance:

        >>> e/log(6-4*e/3)
        3.14157719846001
        >>> 135*e*catalan**2/98
        3.14166950419369
        >>> sqrt(e-13+22*catalan)
        3.14158000062992
        >>> log(24*e-6+4*catalan)-1
        3.14158791577159

    **Symbolic processing**

    The output formula can be evaluated as a Python expression.
    Note however that if fractions (like \'2/3\') are present in
    the formula, Python\'s :func:`~mpmath.eval()` may erroneously perform
    integer division. Note also that the output is not necessarily
    in the algebraically simplest form::

        >>> identify(sqrt(2))
        \'(sqrt(8)/2)\'

    As a solution to both problems, consider using SymPy\'s
    :func:`~mpmath.sympify` to convert the formula into a symbolic expression.
    SymPy can be used to pretty-print or further simplify the formula
    symbolically::

        >>> from sympy import sympify # doctest: +SKIP
        >>> sympify(identify(sqrt(2))) # doctest: +SKIP
        2**(1/2)

    Sometimes :func:`~mpmath.identify` can simplify an expression further than
    a symbolic algorithm::

        >>> from sympy import simplify # doctest: +SKIP
        >>> x = sympify(\'-1/(-3/2+(1/2)*5**(1/2))*(3/2-1/2*5**(1/2))**(1/2)\') # doctest: +SKIP
        >>> x # doctest: +SKIP
        (3/2 - 5**(1/2)/2)**(-1/2)
        >>> x = simplify(x) # doctest: +SKIP
        >>> x # doctest: +SKIP
        2/(6 - 2*5**(1/2))**(1/2)
        >>> mp.dps = 30 # doctest: +SKIP
        >>> x = sympify(identify(x.evalf(30))) # doctest: +SKIP
        >>> x # doctest: +SKIP
        1/2 + 5**(1/2)/2

    (In fact, this functionality is available directly in SymPy as the
    function :func:`~mpmath.nsimplify`, which is essentially a wrapper for
    :func:`~mpmath.identify`.)

    **Miscellaneous issues and limitations**

    The input `x` must be a real number. All base constants must be
    positive real numbers and must not be rationals or rational linear
    combinations of each other.

    The worst-case computation time grows quickly with the number of
    base constants. Already with 3 or 4 base constants,
    :func:`~mpmath.identify` may require several seconds to finish. To search
    for relations among a large number of constants, you should
    consider using :func:`~mpmath.pslq` directly.

    The extended transformations are applied to x, not the constants
    separately. As a result, ``identify`` will for example be able to
    recognize ``exp(2*pi+3)`` with ``pi`` given as a base constant, but
    not ``2*exp(pi)+3``. It will be able to recognize the latter if
    ``exp(pi)`` is given explicitly as a base constant.

    '''
