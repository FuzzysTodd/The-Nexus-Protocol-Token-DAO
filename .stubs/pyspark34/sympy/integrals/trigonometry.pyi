from .integrals import integrate as integrate
from sympy.core import Dummy as Dummy, Integer as Integer, Ne as Ne, Rational as Rational, S as S, Wild as Wild, cacheit as cacheit
from sympy.functions import Abs as Abs, Piecewise as Piecewise, binomial as binomial, cos as cos, sin as sin

def trigintegrate(f, x, conds: str = 'piecewise'):
    """
    Integrate f = Mul(trig) over x.

    Examples
    ========

    >>> from sympy import sin, cos, tan, sec
    >>> from sympy.integrals.trigonometry import trigintegrate
    >>> from sympy.abc import x

    >>> trigintegrate(sin(x)*cos(x), x)
    sin(x)**2/2

    >>> trigintegrate(sin(x)**2, x)
    x/2 - sin(x)*cos(x)/2

    >>> trigintegrate(tan(x)*sec(x), x)
    1/cos(x)

    >>> trigintegrate(sin(x)*tan(x), x)
    -log(sin(x) - 1)/2 + log(sin(x) + 1)/2 - sin(x)

    References
    ==========

    .. [1] https://en.wikibooks.org/wiki/Calculus/Integration_techniques

    See Also
    ========

    sympy.integrals.integrals.Integral.doit
    sympy.integrals.integrals.Integral
    """
