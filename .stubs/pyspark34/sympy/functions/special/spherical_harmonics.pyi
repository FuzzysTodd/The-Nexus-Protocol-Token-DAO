from sympy.core.expr import Expr as Expr
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.numbers import I as I, pi as pi
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy
from sympy.functions import assoc_legendre as assoc_legendre
from sympy.functions.combinatorial.factorials import factorial as factorial
from sympy.functions.elementary.complexes import Abs as Abs, conjugate as conjugate
from sympy.functions.elementary.exponential import exp as exp
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.trigonometric import cos as cos, cot as cot, sin as sin

class Ynm(Function):
    '''
    Spherical harmonics defined as

    .. math::
        Y_n^m(\\theta, \\varphi) := \\sqrt{\\frac{(2n+1)(n-m)!}{4\\pi(n+m)!}}
                                  \\exp(i m \\varphi)
                                  \\mathrm{P}_n^m\\left(\\cos(\\theta)\\right)

    Explanation
    ===========

    ``Ynm()`` gives the spherical harmonic function of order $n$ and $m$
    in $\\theta$ and $\\varphi$, $Y_n^m(\\theta, \\varphi)$. The four
    parameters are as follows: $n \\geq 0$ an integer and $m$ an integer
    such that $-n \\leq m \\leq n$ holds. The two angles are real-valued
    with $\\theta \\in [0, \\pi]$ and $\\varphi \\in [0, 2\\pi]$.

    Examples
    ========

    >>> from sympy import Ynm, Symbol, simplify
    >>> from sympy.abc import n,m
    >>> theta = Symbol("theta")
    >>> phi = Symbol("phi")

    >>> Ynm(n, m, theta, phi)
    Ynm(n, m, theta, phi)

    Several symmetries are known, for the order:

    >>> Ynm(n, -m, theta, phi)
    (-1)**m*exp(-2*I*m*phi)*Ynm(n, m, theta, phi)

    As well as for the angles:

    >>> Ynm(n, m, -theta, phi)
    Ynm(n, m, theta, phi)

    >>> Ynm(n, m, theta, -phi)
    exp(-2*I*m*phi)*Ynm(n, m, theta, phi)

    For specific integers $n$ and $m$ we can evaluate the harmonics
    to more useful expressions:

    >>> simplify(Ynm(0, 0, theta, phi).expand(func=True))
    1/(2*sqrt(pi))

    >>> simplify(Ynm(1, -1, theta, phi).expand(func=True))
    sqrt(6)*exp(-I*phi)*sin(theta)/(4*sqrt(pi))

    >>> simplify(Ynm(1, 0, theta, phi).expand(func=True))
    sqrt(3)*cos(theta)/(2*sqrt(pi))

    >>> simplify(Ynm(1, 1, theta, phi).expand(func=True))
    -sqrt(6)*exp(I*phi)*sin(theta)/(4*sqrt(pi))

    >>> simplify(Ynm(2, -2, theta, phi).expand(func=True))
    sqrt(30)*exp(-2*I*phi)*sin(theta)**2/(8*sqrt(pi))

    >>> simplify(Ynm(2, -1, theta, phi).expand(func=True))
    sqrt(30)*exp(-I*phi)*sin(2*theta)/(8*sqrt(pi))

    >>> simplify(Ynm(2, 0, theta, phi).expand(func=True))
    sqrt(5)*(3*cos(theta)**2 - 1)/(4*sqrt(pi))

    >>> simplify(Ynm(2, 1, theta, phi).expand(func=True))
    -sqrt(30)*exp(I*phi)*sin(2*theta)/(8*sqrt(pi))

    >>> simplify(Ynm(2, 2, theta, phi).expand(func=True))
    sqrt(30)*exp(2*I*phi)*sin(theta)**2/(8*sqrt(pi))

    We can differentiate the functions with respect
    to both angles:

    >>> from sympy import Ynm, Symbol, diff
    >>> from sympy.abc import n,m
    >>> theta = Symbol("theta")
    >>> phi = Symbol("phi")

    >>> diff(Ynm(n, m, theta, phi), theta)
    m*cot(theta)*Ynm(n, m, theta, phi) + sqrt((-m + n)*(m + n + 1))*exp(-I*phi)*Ynm(n, m + 1, theta, phi)

    >>> diff(Ynm(n, m, theta, phi), phi)
    I*m*Ynm(n, m, theta, phi)

    Further we can compute the complex conjugation:

    >>> from sympy import Ynm, Symbol, conjugate
    >>> from sympy.abc import n,m
    >>> theta = Symbol("theta")
    >>> phi = Symbol("phi")

    >>> conjugate(Ynm(n, m, theta, phi))
    (-1)**(2*m)*exp(-2*I*m*phi)*Ynm(n, m, theta, phi)

    To get back the well known expressions in spherical
    coordinates, we use full expansion:

    >>> from sympy import Ynm, Symbol, expand_func
    >>> from sympy.abc import n,m
    >>> theta = Symbol("theta")
    >>> phi = Symbol("phi")

    >>> expand_func(Ynm(n, m, theta, phi))
    sqrt((2*n + 1)*factorial(-m + n)/factorial(m + n))*exp(I*m*phi)*assoc_legendre(n, m, cos(theta))/(2*sqrt(pi))

    See Also
    ========

    Ynm_c, Znm

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Spherical_harmonics
    .. [2] https://mathworld.wolfram.com/SphericalHarmonic.html
    .. [3] https://functions.wolfram.com/Polynomials/SphericalHarmonicY/
    .. [4] https://dlmf.nist.gov/14.30

    '''
    @classmethod
    def eval(cls, n, m, theta, phi): ...
    def fdiff(self, argindex: int = 4): ...
    def as_real_imag(self, deep: bool = True, **hints): ...

def Ynm_c(n, m, theta, phi):
    '''
    Conjugate spherical harmonics defined as

    .. math::
        \\overline{Y_n^m(\\theta, \\varphi)} := (-1)^m Y_n^{-m}(\\theta, \\varphi).

    Examples
    ========

    >>> from sympy import Ynm_c, Symbol, simplify
    >>> from sympy.abc import n,m
    >>> theta = Symbol("theta")
    >>> phi = Symbol("phi")
    >>> Ynm_c(n, m, theta, phi)
    (-1)**(2*m)*exp(-2*I*m*phi)*Ynm(n, m, theta, phi)
    >>> Ynm_c(n, m, -theta, phi)
    (-1)**(2*m)*exp(-2*I*m*phi)*Ynm(n, m, theta, phi)

    For specific integers $n$ and $m$ we can evaluate the harmonics
    to more useful expressions:

    >>> simplify(Ynm_c(0, 0, theta, phi).expand(func=True))
    1/(2*sqrt(pi))
    >>> simplify(Ynm_c(1, -1, theta, phi).expand(func=True))
    sqrt(6)*exp(I*(-phi + 2*conjugate(phi)))*sin(theta)/(4*sqrt(pi))

    See Also
    ========

    Ynm, Znm

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Spherical_harmonics
    .. [2] https://mathworld.wolfram.com/SphericalHarmonic.html
    .. [3] https://functions.wolfram.com/Polynomials/SphericalHarmonicY/

    '''

class Znm(Function):
    '''
    Real spherical harmonics defined as

    .. math::

        Z_n^m(\\theta, \\varphi) :=
        \\begin{cases}
          \\frac{Y_n^m(\\theta, \\varphi) + \\overline{Y_n^m(\\theta, \\varphi)}}{\\sqrt{2}} &\\quad m > 0 \\\\\n          Y_n^m(\\theta, \\varphi) &\\quad m = 0 \\\\\n          \\frac{Y_n^m(\\theta, \\varphi) - \\overline{Y_n^m(\\theta, \\varphi)}}{i \\sqrt{2}} &\\quad m < 0 \\\\\n        \\end{cases}

    which gives in simplified form

    .. math::

        Z_n^m(\\theta, \\varphi) =
        \\begin{cases}
          \\frac{Y_n^m(\\theta, \\varphi) + (-1)^m Y_n^{-m}(\\theta, \\varphi)}{\\sqrt{2}} &\\quad m > 0 \\\\\n          Y_n^m(\\theta, \\varphi) &\\quad m = 0 \\\\\n          \\frac{Y_n^m(\\theta, \\varphi) - (-1)^m Y_n^{-m}(\\theta, \\varphi)}{i \\sqrt{2}} &\\quad m < 0 \\\\\n        \\end{cases}

    Examples
    ========

    >>> from sympy import Znm, Symbol, simplify
    >>> from sympy.abc import n, m
    >>> theta = Symbol("theta")
    >>> phi = Symbol("phi")
    >>> Znm(n, m, theta, phi)
    Znm(n, m, theta, phi)

    For specific integers n and m we can evaluate the harmonics
    to more useful expressions:

    >>> simplify(Znm(0, 0, theta, phi).expand(func=True))
    1/(2*sqrt(pi))
    >>> simplify(Znm(1, 1, theta, phi).expand(func=True))
    -sqrt(3)*sin(theta)*cos(phi)/(2*sqrt(pi))
    >>> simplify(Znm(2, 1, theta, phi).expand(func=True))
    -sqrt(15)*sin(2*theta)*cos(phi)/(4*sqrt(pi))

    See Also
    ========

    Ynm, Ynm_c

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Spherical_harmonics
    .. [2] https://mathworld.wolfram.com/SphericalHarmonic.html
    .. [3] https://functions.wolfram.com/Polynomials/SphericalHarmonicY/

    '''
    @classmethod
    def eval(cls, n, m, theta, phi): ...
