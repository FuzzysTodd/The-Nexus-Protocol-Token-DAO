from _typeshed import Incomplete
from sympy.core import I as I, Rational as Rational, S as S, pi as pi
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.symbol import Dummy as Dummy
from sympy.functions.elementary.complexes import sign as sign
from sympy.functions.elementary.hyperbolic import atanh as atanh
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.trigonometric import sin as sin, tan as tan
from sympy.functions.special.gamma_functions import gamma as gamma
from sympy.functions.special.hyper import hyper as hyper, meijerg as meijerg

class elliptic_k(Function):
    """
    The complete elliptic integral of the first kind, defined by

    .. math:: K(m) = F\\left(\\tfrac{\\pi}{2}\\middle| m\\right)

    where $F\\left(z\\middle| m\\right)$ is the Legendre incomplete
    elliptic integral of the first kind.

    Explanation
    ===========

    The function $K(m)$ is a single-valued function on the complex
    plane with branch cut along the interval $(1, \\infty)$.

    Note that our notation defines the incomplete elliptic integral
    in terms of the parameter $m$ instead of the elliptic modulus
    (eccentricity) $k$.
    In this case, the parameter $m$ is defined as $m=k^2$.

    Examples
    ========

    >>> from sympy import elliptic_k, I
    >>> from sympy.abc import m
    >>> elliptic_k(0)
    pi/2
    >>> elliptic_k(1.0 + I)
    1.50923695405127 + 0.625146415202697*I
    >>> elliptic_k(m).series(n=3)
    pi/2 + pi*m/8 + 9*pi*m**2/128 + O(m**3)

    See Also
    ========

    elliptic_f

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Elliptic_integrals
    .. [2] https://functions.wolfram.com/EllipticIntegrals/EllipticK

    """
    @classmethod
    def eval(cls, m): ...
    def fdiff(self, argindex: int = 1): ...

class elliptic_f(Function):
    """
    The Legendre incomplete elliptic integral of the first
    kind, defined by

    .. math:: F\\left(z\\middle| m\\right) =
              \\int_0^z \\frac{dt}{\\sqrt{1 - m \\sin^2 t}}

    Explanation
    ===========

    This function reduces to a complete elliptic integral of
    the first kind, $K(m)$, when $z = \\pi/2$.

    Note that our notation defines the incomplete elliptic integral
    in terms of the parameter $m$ instead of the elliptic modulus
    (eccentricity) $k$.
    In this case, the parameter $m$ is defined as $m=k^2$.

    Examples
    ========

    >>> from sympy import elliptic_f, I
    >>> from sympy.abc import z, m
    >>> elliptic_f(z, m).series(z)
    z + z**5*(3*m**2/40 - m/30) + m*z**3/6 + O(z**6)
    >>> elliptic_f(3.0 + I/2, 1.0 + I)
    2.909449841483 + 1.74720545502474*I

    See Also
    ========

    elliptic_k

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Elliptic_integrals
    .. [2] https://functions.wolfram.com/EllipticIntegrals/EllipticF

    """
    @classmethod
    def eval(cls, z, m): ...
    def fdiff(self, argindex: int = 1): ...

class elliptic_e(Function):
    """
    Called with two arguments $z$ and $m$, evaluates the
    incomplete elliptic integral of the second kind, defined by

    .. math:: E\\left(z\\middle| m\\right) = \\int_0^z \\sqrt{1 - m \\sin^2 t} dt

    Called with a single argument $m$, evaluates the Legendre complete
    elliptic integral of the second kind

    .. math:: E(m) = E\\left(\\tfrac{\\pi}{2}\\middle| m\\right)

    Explanation
    ===========

    The function $E(m)$ is a single-valued function on the complex
    plane with branch cut along the interval $(1, \\infty)$.

    Note that our notation defines the incomplete elliptic integral
    in terms of the parameter $m$ instead of the elliptic modulus
    (eccentricity) $k$.
    In this case, the parameter $m$ is defined as $m=k^2$.

    Examples
    ========

    >>> from sympy import elliptic_e, I
    >>> from sympy.abc import z, m
    >>> elliptic_e(z, m).series(z)
    z + z**5*(-m**2/40 + m/30) - m*z**3/6 + O(z**6)
    >>> elliptic_e(m).series(n=4)
    pi/2 - pi*m/8 - 3*pi*m**2/128 - 5*pi*m**3/512 + O(m**4)
    >>> elliptic_e(1 + I, 2 - I/2).n()
    1.55203744279187 + 0.290764986058437*I
    >>> elliptic_e(0)
    pi/2
    >>> elliptic_e(2.0 - I)
    0.991052601328069 + 0.81879421395609*I

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Elliptic_integrals
    .. [2] https://functions.wolfram.com/EllipticIntegrals/EllipticE2
    .. [3] https://functions.wolfram.com/EllipticIntegrals/EllipticE

    """
    @classmethod
    def eval(cls, m, z: Incomplete | None = None): ...
    def fdiff(self, argindex: int = 1): ...

class elliptic_pi(Function):
    """
    Called with three arguments $n$, $z$ and $m$, evaluates the
    Legendre incomplete elliptic integral of the third kind, defined by

    .. math:: \\Pi\\left(n; z\\middle| m\\right) = \\int_0^z \\frac{dt}
              {\\left(1 - n \\sin^2 t\\right) \\sqrt{1 - m \\sin^2 t}}

    Called with two arguments $n$ and $m$, evaluates the complete
    elliptic integral of the third kind:

    .. math:: \\Pi\\left(n\\middle| m\\right) =
              \\Pi\\left(n; \\tfrac{\\pi}{2}\\middle| m\\right)

    Explanation
    ===========

    Note that our notation defines the incomplete elliptic integral
    in terms of the parameter $m$ instead of the elliptic modulus
    (eccentricity) $k$.
    In this case, the parameter $m$ is defined as $m=k^2$.

    Examples
    ========

    >>> from sympy import elliptic_pi, I
    >>> from sympy.abc import z, n, m
    >>> elliptic_pi(n, z, m).series(z, n=4)
    z + z**3*(m/6 + n/3) + O(z**4)
    >>> elliptic_pi(0.5 + I, 1.0 - I, 1.2)
    2.50232379629182 - 0.760939574180767*I
    >>> elliptic_pi(0, 0)
    pi/2
    >>> elliptic_pi(1.0 - I/3, 2.0 + I)
    3.29136443417283 + 0.32555634906645*I

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Elliptic_integrals
    .. [2] https://functions.wolfram.com/EllipticIntegrals/EllipticPi3
    .. [3] https://functions.wolfram.com/EllipticIntegrals/EllipticPi

    """
    @classmethod
    def eval(cls, n, m, z: Incomplete | None = None): ...
    def fdiff(self, argindex: int = 1): ...
