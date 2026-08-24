from .functions import defun as defun, defun_wrapped as defun_wrapped

def hermite(ctx, n, z, **kwargs): ...
def pcfd(ctx, n, z, **kwargs):
    """
    Gives the parabolic cylinder function in Whittaker's notation
    `D_n(z) = U(-n-1/2, z)` (see :func:`~mpmath.pcfu`).
    It solves the differential equation

    .. math ::

        y'' + \\left(n + \\frac{1}{2} - \\frac{1}{4} z^2\\right) y = 0.

    and can be represented in terms of Hermite polynomials
    (see :func:`~mpmath.hermite`) as

    .. math ::

        D_n(z) = 2^{-n/2} e^{-z^2/4} H_n\\left(\\frac{z}{\\sqrt{2}}\\right).

    **Plots**

    .. literalinclude :: /plots/pcfd.py
    .. image :: /plots/pcfd.png

    **Examples**

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> pcfd(0,0); pcfd(1,0); pcfd(2,0); pcfd(3,0)
        1.0
        0.0
        -1.0
        0.0
        >>> pcfd(4,0); pcfd(-3,0)
        3.0
        0.6266570686577501256039413
        >>> pcfd('1/2', 2+3j)
        (-5.363331161232920734849056 - 3.858877821790010714163487j)
        >>> pcfd(2, -10)
        1.374906442631438038871515e-9

    Verifying the differential equation::

        >>> n = mpf(2.5)
        >>> y = lambda z: pcfd(n,z)
        >>> z = 1.75
        >>> chop(diff(y,z,2) + (n+0.5-0.25*z**2)*y(z))
        0.0

    Rational Taylor series expansion when `n` is an integer::

        >>> taylor(lambda z: pcfd(5,z), 0, 7)
        [0.0, 15.0, 0.0, -13.75, 0.0, 3.96875, 0.0, -0.6015625]

    """
def pcfu(ctx, a, z, **kwargs):
    """
    Gives the parabolic cylinder function `U(a,z)`, which may be
    defined for `\\Re(z) > 0` in terms of the confluent
    U-function (see :func:`~mpmath.hyperu`) by

    .. math ::

        U(a,z) = 2^{-\\frac{1}{4}-\\frac{a}{2}} e^{-\\frac{1}{4} z^2}
            U\\left(\\frac{a}{2}+\\frac{1}{4},
            \\frac{1}{2}, \\frac{1}{2}z^2\\right)

    or, for arbitrary `z`,

    .. math ::

        e^{-\\frac{1}{4}z^2} U(a,z) =
            U(a,0) \\,_1F_1\\left(-\\tfrac{a}{2}+\\tfrac{1}{4};
            \\tfrac{1}{2}; -\\tfrac{1}{2}z^2\\right) +
            U'(a,0) z \\,_1F_1\\left(-\\tfrac{a}{2}+\\tfrac{3}{4};
            \\tfrac{3}{2}; -\\tfrac{1}{2}z^2\\right).

    **Examples**

    Connection to other functions::

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> z = mpf(3)
        >>> pcfu(0.5,z)
        0.03210358129311151450551963
        >>> sqrt(pi/2)*exp(z**2/4)*erfc(z/sqrt(2))
        0.03210358129311151450551963
        >>> pcfu(0.5,-z)
        23.75012332835297233711255
        >>> sqrt(pi/2)*exp(z**2/4)*erfc(-z/sqrt(2))
        23.75012332835297233711255
        >>> pcfu(0.5,-z)
        23.75012332835297233711255
        >>> sqrt(pi/2)*exp(z**2/4)*erfc(-z/sqrt(2))
        23.75012332835297233711255

    """
def pcfv(ctx, a, z, **kwargs):
    """
    Gives the parabolic cylinder function `V(a,z)`, which can be
    represented in terms of :func:`~mpmath.pcfu` as

    .. math ::

        V(a,z) = \\frac{\\Gamma(a+\\tfrac{1}{2}) (U(a,-z)-\\sin(\\pi a) U(a,z)}{\\pi}.

    **Examples**

    Wronskian relation between `U` and `V`::

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a, z = 2, 3
        >>> pcfu(a,z)*diff(pcfv,(a,z),(0,1))-diff(pcfu,(a,z),(0,1))*pcfv(a,z)
        0.7978845608028653558798921
        >>> sqrt(2/pi)
        0.7978845608028653558798921
        >>> a, z = 2.5, 3
        >>> pcfu(a,z)*diff(pcfv,(a,z),(0,1))-diff(pcfu,(a,z),(0,1))*pcfv(a,z)
        0.7978845608028653558798921
        >>> a, z = 0.25, -1
        >>> pcfu(a,z)*diff(pcfv,(a,z),(0,1))-diff(pcfu,(a,z),(0,1))*pcfv(a,z)
        0.7978845608028653558798921
        >>> a, z = 2+1j, 2+3j
        >>> chop(pcfu(a,z)*diff(pcfv,(a,z),(0,1))-diff(pcfu,(a,z),(0,1))*pcfv(a,z))
        0.7978845608028653558798921

    """
def pcfw(ctx, a, z, **kwargs):
    """
    Gives the parabolic cylinder function `W(a,z)` defined in (DLMF 12.14).

    **Examples**

    Value at the origin::

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a = mpf(0.25)
        >>> pcfw(a,0)
        0.9722833245718180765617104
        >>> power(2,-0.75)*sqrt(abs(gamma(0.25+0.5j*a)/gamma(0.75+0.5j*a)))
        0.9722833245718180765617104
        >>> diff(pcfw,(a,0),(0,1))
        -0.5142533944210078966003624
        >>> -power(2,-0.25)*sqrt(abs(gamma(0.75+0.5j*a)/gamma(0.25+0.5j*a)))
        -0.5142533944210078966003624

    """
def gegenbauer(ctx, n, a, z, **kwargs): ...
def jacobi(ctx, n, a, b, x, **kwargs): ...
def laguerre(ctx, n, a, z, **kwargs): ...
def legendre(ctx, n, x, **kwargs): ...
def legenp(ctx, n, m, z, type: int = 2, **kwargs): ...
def legenq(ctx, n, m, z, type: int = 2, **kwargs): ...
def chebyt(ctx, n, x, **kwargs): ...
def chebyu(ctx, n, x, **kwargs): ...
def spherharm(ctx, l, m, theta, phi, **kwargs): ...
