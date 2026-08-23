from ..libmp.backend import xrange as xrange
from .functions import defun as defun, defun_static as defun_static, defun_wrapped as defun_wrapped
from _typeshed import Incomplete

def stieltjes(ctx, n, a: int = 1): ...
def siegeltheta(ctx, t, derivative: int = 0): ...
def grampoint(ctx, n): ...
def siegelz(ctx, t, **kwargs): ...
def oldzetazero(ctx, n, url: str = 'http://www.dtc.umn.edu/~odlyzko/zeta_tables/zeros1'): ...
def riemannr(ctx, x): ...
def primepi(ctx, x): ...
def primepi2(ctx, x): ...
def primezeta(ctx, s): ...
def bernpoly(ctx, n, z): ...
def eulerpoly(ctx, n, z): ...
def eulernum(ctx, n, exact: bool = False): ...
def polylog_series(ctx, s, z): ...
def polylog_continuation(ctx, n, z): ...
def polylog_unitcircle(ctx, n, z): ...
def polylog_general(ctx, s, z): ...
def polylog(ctx, s, z): ...
def clsin(ctx, s, z, pi: bool = False): ...
def clcos(ctx, s, z, pi: bool = False): ...
def altzeta(ctx, s, **kwargs): ...
def zeta(ctx, s, a: int = 1, derivative: int = 0, method: Incomplete | None = None, **kwargs): ...
def dirichlet(ctx, s, chi=[1], derivative: int = 0): ...
def secondzeta_main_term(ctx, s, a, **kwargs): ...
def secondzeta_prime_term(ctx, s, a, **kwargs): ...
def secondzeta_exp_term(ctx, s, a): ...
def secondzeta_singular_term(ctx, s, a, **kwargs): ...
def secondzeta(ctx, s, a: float = 0.015, **kwargs):
    """
    Evaluates the secondary zeta function `Z(s)`, defined for
    `\\mathrm{Re}(s)>1` by

    .. math ::

        Z(s) = \\sum_{n=1}^{\\infty} \\frac{1}{\\tau_n^s}

    where `\\frac12+i\\tau_n` runs through the zeros of `\\zeta(s)` with
    imaginary part positive.

    `Z(s)` extends to a meromorphic function on `\\mathbb{C}`  with a
    double pole at `s=1` and  simple poles at the points `-2n` for
    `n=0`,  1, 2, ...

    **Examples**

        >>> from mpmath import *
        >>> mp.pretty = True; mp.dps = 15
        >>> secondzeta(2)
        0.023104993115419
        >>> xi = lambda s: 0.5*s*(s-1)*pi**(-0.5*s)*gamma(0.5*s)*zeta(s)
        >>> Xi = lambda t: xi(0.5+t*j)
        >>> chop(-0.5*diff(Xi,0,n=2)/Xi(0))
        0.023104993115419

    We may ask for an approximate error value::

        >>> secondzeta(0.5+100j, error=True)
        ((-0.216272011276718 - 0.844952708937228j), 2.22044604925031e-16)

    The function has poles at the negative odd integers,
    and dyadic rational values at the negative even integers::

        >>> mp.dps = 30
        >>> secondzeta(-8)
        -0.67236328125
        >>> secondzeta(-7)
        +inf

    **Implementation notes**

    The function is computed as sum of four terms `Z(s)=A(s)-P(s)+E(s)-S(s)`
    respectively main, prime, exponential and singular terms.
    The main term `A(s)` is computed from the zeros of zeta.
    The prime term depends on the von Mangoldt function.
    The singular term is responsible for the poles of the function.

    The four terms depends on a small parameter `a`. We may change the
    value of `a`. Theoretically this has no effect on the sum of the four
    terms, but in practice may be important.

    A smaller value of the parameter `a` makes `A(s)` depend on
    a smaller number of zeros of zeta, but `P(s)`  uses more values of
    von Mangoldt function.

    We may also add a verbose option to obtain data about the
    values of the four terms.

        >>> mp.dps = 10
        >>> secondzeta(0.5 + 40j, error=True, verbose=True)
        main term = (-30190318549.138656312556 - 13964804384.624622876523j)
            computed using 19 zeros of zeta
        prime term = (132717176.89212754625045 + 188980555.17563978290601j)
            computed using 9 values of the von Mangoldt function
        exponential term = (542447428666.07179812536 + 362434922978.80192435203j)
        singular term = (512124392939.98154322355 + 348281138038.65531023921j)
        ((0.059471043 + 0.3463514534j), 1.455191523e-11)

        >>> secondzeta(0.5 + 40j, a=0.04, error=True, verbose=True)
        main term = (-151962888.19606243907725 - 217930683.90210294051982j)
            computed using 9 zeros of zeta
        prime term = (2476659342.3038722372461 + 28711581821.921627163136j)
            computed using 37 values of the von Mangoldt function
        exponential term = (178506047114.7838188264 + 819674143244.45677330576j)
        singular term = (175877424884.22441310708 + 790744630738.28669174871j)
        ((0.059471043 + 0.3463514534j), 1.455191523e-11)

    Notice the great cancellation between the four terms. Changing `a`, the
    four terms are very different numbers but the cancellation gives
    the good value of Z(s).

    **References**

    A. Voros, Zeta functions for the Riemann zeros, Ann. Institute Fourier,
    53, (2003) 665--699.

    A. Voros, Zeta functions over Zeros of Zeta Functions, Lecture Notes
    of the Unione Matematica Italiana, Springer, 2009.
    """
def lerchphi(ctx, z, s, a):
    """
    Gives the Lerch transcendent, defined for `|z| < 1` and
    `\\Re{a} > 0` by

    .. math ::

        \\Phi(z,s,a) = \\sum_{k=0}^{\\infty} \\frac{z^k}{(a+k)^s}

    and generally by the recurrence `\\Phi(z,s,a) = z \\Phi(z,s,a+1) + a^{-s}`
    along with the integral representation valid for `\\Re{a} > 0`

    .. math ::

        \\Phi(z,s,a) = \\frac{1}{2 a^s} +
                \\int_0^{\\infty} \\frac{z^t}{(a+t)^s} dt -
                2 \\int_0^{\\infty} \\frac{\\sin(t \\log z - s
                    \\operatorname{arctan}(t/a)}{(a^2 + t^2)^{s/2}
                    (e^{2 \\pi t}-1)} dt.

    The Lerch transcendent generalizes the Hurwitz zeta function :func:`zeta`
    (`z = 1`) and the polylogarithm :func:`polylog` (`a = 1`).

    **Examples**

    Several evaluations in terms of simpler functions::

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> lerchphi(-1,2,0.5); 4*catalan
        3.663862376708876060218414
        3.663862376708876060218414
        >>> diff(lerchphi, (-1,-2,1), (0,1,0)); 7*zeta(3)/(4*pi**2)
        0.2131391994087528954617607
        0.2131391994087528954617607
        >>> lerchphi(-4,1,1); log(5)/4
        0.4023594781085250936501898
        0.4023594781085250936501898
        >>> lerchphi(-3+2j,1,0.5); 2*atanh(sqrt(-3+2j))/sqrt(-3+2j)
        (1.142423447120257137774002 + 0.2118232380980201350495795j)
        (1.142423447120257137774002 + 0.2118232380980201350495795j)

    Evaluation works for complex arguments and `|z| \\ge 1`::

        >>> lerchphi(1+2j, 3-j, 4+2j)
        (0.002025009957009908600539469 + 0.003327897536813558807438089j)
        >>> lerchphi(-2,2,-2.5)
        -12.28676272353094275265944
        >>> lerchphi(10,10,10)
        (-4.462130727102185701817349e-11 - 1.575172198981096218823481e-12j)
        >>> lerchphi(10,10,-10.5)
        (112658784011940.5605789002 - 498113185.5756221777743631j)

    Some degenerate cases::

        >>> lerchphi(0,1,2)
        0.5
        >>> lerchphi(0,1,-2)
        -0.5

    Reduction to simpler functions::

        >>> lerchphi(1, 4.25+1j, 1)
        (1.044674457556746668033975 - 0.04674508654012658932271226j)
        >>> zeta(4.25+1j)
        (1.044674457556746668033975 - 0.04674508654012658932271226j)
        >>> lerchphi(1 - 0.5**10, 4.25+1j, 1)
        (1.044629338021507546737197 - 0.04667768813963388181708101j)
        >>> lerchphi(3, 4, 1)
        (1.249503297023366545192592 - 0.2314252413375664776474462j)
        >>> polylog(4, 3) / 3
        (1.249503297023366545192592 - 0.2314252413375664776474462j)
        >>> lerchphi(3, 4, 1 - 0.5**10)
        (1.253978063946663945672674 - 0.2316736622836535468765376j)

    **References**

    1. [DLMF]_ section 25.14

    """
