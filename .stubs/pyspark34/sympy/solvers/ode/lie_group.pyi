from .ode import checkinfsol as checkinfsol
from _typeshed import Incomplete
from sympy.core import Add as Add, Mul as Mul, Pow as Pow, S as S
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.function import AppliedUndef as AppliedUndef, Function as Function, expand as expand
from sympy.core.relational import Eq as Eq, Equality as Equality
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, Wild as Wild, symbols as symbols
from sympy.functions import exp as exp, log as log
from sympy.integrals.integrals import integrate as integrate
from sympy.polys import Poly as Poly
from sympy.polys.polytools import cancel as cancel, div as div
from sympy.simplify import collect as collect, powsimp as powsimp, separatevars as separatevars, simplify as simplify
from sympy.solvers import solve as solve
from sympy.solvers.deutils import ode_order as ode_order
from sympy.solvers.pde import pdsolve as pdsolve
from sympy.utilities import numbered_symbols as numbered_symbols

lie_heuristics: Incomplete

def infinitesimals(eq, func: Incomplete | None = None, order: Incomplete | None = None, hint: str = 'default', match: Incomplete | None = None):
    """
    The infinitesimal functions of an ordinary differential equation, `\\xi(x,y)`
    and `\\eta(x,y)`, are the infinitesimals of the Lie group of point transformations
    for which the differential equation is invariant. So, the ODE `y'=f(x,y)`
    would admit a Lie group `x^*=X(x,y;\\varepsilon)=x+\\varepsilon\\xi(x,y)`,
    `y^*=Y(x,y;\\varepsilon)=y+\\varepsilon\\eta(x,y)` such that `(y^*)'=f(x^*, y^*)`.
    A change of coordinates, to `r(x,y)` and `s(x,y)`, can be performed so this Lie group
    becomes the translation group, `r^*=r` and `s^*=s+\\varepsilon`.
    They are tangents to the coordinate curves of the new system.

    Consider the transformation `(x, y) \\to (X, Y)` such that the
    differential equation remains invariant. `\\xi` and `\\eta` are the tangents to
    the transformed coordinates `X` and `Y`, at `\\varepsilon=0`.

    .. math:: \\left(\\frac{\\partial X(x,y;\\varepsilon)}{\\partial\\varepsilon
                }\\right)|_{\\varepsilon=0} = \\xi,
              \\left(\\frac{\\partial Y(x,y;\\varepsilon)}{\\partial\\varepsilon
                }\\right)|_{\\varepsilon=0} = \\eta,

    The infinitesimals can be found by solving the following PDE:

        >>> from sympy import Function, Eq, pprint
        >>> from sympy.abc import x, y
        >>> xi, eta, h = map(Function, ['xi', 'eta', 'h'])
        >>> h = h(x, y)  # dy/dx = h
        >>> eta = eta(x, y)
        >>> xi = xi(x, y)
        >>> genform = Eq(eta.diff(x) + (eta.diff(y) - xi.diff(x))*h
        ... - (xi.diff(y))*h**2 - xi*(h.diff(x)) - eta*(h.diff(y)), 0)
        >>> pprint(genform)
        /d               d           \\                     d              2       d
        |--(eta(x, y)) - --(xi(x, y))|*h(x, y) - eta(x, y)*--(h(x, y)) - h (x, y)*--(x
        \\dy              dx          /                     dy                     dy
        <BLANKLINE>
                            d             d
        i(x, y)) - xi(x, y)*--(h(x, y)) + --(eta(x, y)) = 0
                            dx            dx

    Solving the above mentioned PDE is not trivial, and can be solved only by
    making intelligent assumptions for `\\xi` and `\\eta` (heuristics). Once an
    infinitesimal is found, the attempt to find more heuristics stops. This is done to
    optimise the speed of solving the differential equation. If a list of all the
    infinitesimals is needed, ``hint`` should be flagged as ``all``, which gives
    the complete list of infinitesimals. If the infinitesimals for a particular
    heuristic needs to be found, it can be passed as a flag to ``hint``.

    Examples
    ========

    >>> from sympy import Function
    >>> from sympy.solvers.ode.lie_group import infinitesimals
    >>> from sympy.abc import x
    >>> f = Function('f')
    >>> eq = f(x).diff(x) - x**2*f(x)
    >>> infinitesimals(eq)
    [{eta(x, f(x)): exp(x**3/3), xi(x, f(x)): 0}]

    References
    ==========

    - Solving differential equations by Symmetry Groups,
      John Starrett, pp. 1 - pp. 14

    """
def lie_heuristic_abaco1_simple(match, comp: bool = False):
    """
    The first heuristic uses the following four sets of
    assumptions on `\\xi` and `\\eta`

    .. math:: \\xi = 0, \\eta = f(x)

    .. math:: \\xi = 0, \\eta = f(y)

    .. math:: \\xi = f(x), \\eta = 0

    .. math:: \\xi = f(y), \\eta = 0

    The success of this heuristic is determined by algebraic factorisation.
    For the first assumption `\\xi = 0` and `\\eta` to be a function of `x`, the PDE

    .. math:: \\frac{\\partial \\eta}{\\partial x} + (\\frac{\\partial \\eta}{\\partial y}
                - \\frac{\\partial \\xi}{\\partial x})*h
                - \\frac{\\partial \\xi}{\\partial y}*h^{2}
                - \\xi*\\frac{\\partial h}{\\partial x} - \\eta*\\frac{\\partial h}{\\partial y} = 0

    reduces to `f'(x) - f\\frac{\\partial h}{\\partial y} = 0`
    If `\\frac{\\partial h}{\\partial y}` is a function of `x`, then this can usually
    be integrated easily. A similar idea is applied to the other 3 assumptions as well.


    References
    ==========

    - E.S Cheb-Terrab, L.G.S Duarte and L.A,C.P da Mota, Computer Algebra
      Solving of First Order ODEs Using Symmetry Methods, pp. 8


    """
def lie_heuristic_abaco1_product(match, comp: bool = False):
    """
    The second heuristic uses the following two assumptions on `\\xi` and `\\eta`

    .. math:: \\eta = 0, \\xi = f(x)*g(y)

    .. math:: \\eta = f(x)*g(y), \\xi = 0

    The first assumption of this heuristic holds good if
    `\\frac{1}{h^{2}}\\frac{\\partial^2}{\\partial x \\partial y}\\log(h)` is
    separable in `x` and `y`, then the separated factors containing `x`
    is `f(x)`, and `g(y)` is obtained by

    .. math:: e^{\\int f\\frac{\\partial}{\\partial x}\\left(\\frac{1}{f*h}\\right)\\,dy}

    provided `f\\frac{\\partial}{\\partial x}\\left(\\frac{1}{f*h}\\right)` is a function
    of `y` only.

    The second assumption holds good if `\\frac{dy}{dx} = h(x, y)` is rewritten as
    `\\frac{dy}{dx} = \\frac{1}{h(y, x)}` and the same properties of the first assumption
    satisfies. After obtaining `f(x)` and `g(y)`, the coordinates are again
    interchanged, to get `\\eta` as `f(x)*g(y)`


    References
    ==========
    - E.S. Cheb-Terrab, A.D. Roche, Symmetries and First Order
      ODE Patterns, pp. 7 - pp. 8

    """
def lie_heuristic_bivariate(match, comp: bool = False):
    """
    The third heuristic assumes the infinitesimals `\\xi` and `\\eta`
    to be bi-variate polynomials in `x` and `y`. The assumption made here
    for the logic below is that `h` is a rational function in `x` and `y`
    though that may not be necessary for the infinitesimals to be
    bivariate polynomials. The coefficients of the infinitesimals
    are found out by substituting them in the PDE and grouping similar terms
    that are polynomials and since they form a linear system, solve and check
    for non trivial solutions. The degree of the assumed bivariates
    are increased till a certain maximum value.

    References
    ==========
    - Lie Groups and Differential Equations
      pp. 327 - pp. 329

    """
def lie_heuristic_chi(match, comp: bool = False):
    """
    The aim of the fourth heuristic is to find the function `\\chi(x, y)`
    that satisfies the PDE `\\frac{d\\chi}{dx} + h\\frac{d\\chi}{dx}
    - \\frac{\\partial h}{\\partial y}\\chi = 0`.

    This assumes `\\chi` to be a bivariate polynomial in `x` and `y`. By intuition,
    `h` should be a rational function in `x` and `y`. The method used here is
    to substitute a general binomial for `\\chi` up to a certain maximum degree
    is reached. The coefficients of the polynomials, are calculated by by collecting
    terms of the same order in `x` and `y`.

    After finding `\\chi`, the next step is to use `\\eta = \\xi*h + \\chi`, to
    determine `\\xi` and `\\eta`. This can be done by dividing `\\chi` by `h`
    which would give `-\\xi` as the quotient and `\\eta` as the remainder.


    References
    ==========
    - E.S Cheb-Terrab, L.G.S Duarte and L.A,C.P da Mota, Computer Algebra
      Solving of First Order ODEs Using Symmetry Methods, pp. 8

    """
def lie_heuristic_function_sum(match, comp: bool = False):
    """
    This heuristic uses the following two assumptions on `\\xi` and `\\eta`

    .. math:: \\eta = 0, \\xi = f(x) + g(y)

    .. math:: \\eta = f(x) + g(y), \\xi = 0

    The first assumption of this heuristic holds good if

    .. math:: \\frac{\\partial}{\\partial y}[(h\\frac{\\partial^{2}}{
                \\partial x^{2}}(h^{-1}))^{-1}]

    is separable in `x` and `y`,

    1. The separated factors containing `y` is `\\frac{\\partial g}{\\partial y}`.
       From this `g(y)` can be determined.
    2. The separated factors containing `x` is `f''(x)`.
    3. `h\\frac{\\partial^{2}}{\\partial x^{2}}(h^{-1})` equals
       `\\frac{f''(x)}{f(x) + g(y)}`. From this `f(x)` can be determined.

    The second assumption holds good if `\\frac{dy}{dx} = h(x, y)` is rewritten as
    `\\frac{dy}{dx} = \\frac{1}{h(y, x)}` and the same properties of the first
    assumption satisfies. After obtaining `f(x)` and `g(y)`, the coordinates
    are again interchanged, to get `\\eta` as `f(x) + g(y)`.

    For both assumptions, the constant factors are separated among `g(y)`
    and `f''(x)`, such that `f''(x)` obtained from 3] is the same as that
    obtained from 2]. If not possible, then this heuristic fails.


    References
    ==========
    - E.S. Cheb-Terrab, A.D. Roche, Symmetries and First Order
      ODE Patterns, pp. 7 - pp. 8

    """
def lie_heuristic_abaco2_similar(match, comp: bool = False):
    """
    This heuristic uses the following two assumptions on `\\xi` and `\\eta`

    .. math:: \\eta = g(x), \\xi = f(x)

    .. math:: \\eta = f(y), \\xi = g(y)

    For the first assumption,

    1. First `\\frac{\\frac{\\partial h}{\\partial y}}{\\frac{\\partial^{2} h}{
       \\partial yy}}` is calculated. Let us say this value is A

    2. If this is constant, then `h` is matched to the form `A(x) + B(x)e^{
       \\frac{y}{C}}` then, `\\frac{e^{\\int \\frac{A(x)}{C} \\,dx}}{B(x)}` gives `f(x)`
       and `A(x)*f(x)` gives `g(x)`

    3. Otherwise `\\frac{\\frac{\\partial A}{\\partial X}}{\\frac{\\partial A}{
       \\partial Y}} = \\gamma` is calculated. If

       a] `\\gamma` is a function of `x` alone

       b] `\\frac{\\gamma\\frac{\\partial h}{\\partial y} - \\gamma'(x) - \\frac{
       \\partial h}{\\partial x}}{h + \\gamma} = G` is a function of `x` alone.
       then, `e^{\\int G \\,dx}` gives `f(x)` and `-\\gamma*f(x)` gives `g(x)`

    The second assumption holds good if `\\frac{dy}{dx} = h(x, y)` is rewritten as
    `\\frac{dy}{dx} = \\frac{1}{h(y, x)}` and the same properties of the first assumption
    satisfies. After obtaining `f(x)` and `g(x)`, the coordinates are again
    interchanged, to get `\\xi` as `f(x^*)` and `\\eta` as `g(y^*)`

    References
    ==========
    - E.S. Cheb-Terrab, A.D. Roche, Symmetries and First Order
      ODE Patterns, pp. 10 - pp. 12

    """
def lie_heuristic_abaco2_unique_unknown(match, comp: bool = False):
    """
    This heuristic assumes the presence of unknown functions or known functions
    with non-integer powers.

    1. A list of all functions and non-integer powers containing x and y
    2. Loop over each element `f` in the list, find `\\frac{\\frac{\\partial f}{\\partial x}}{
       \\frac{\\partial f}{\\partial x}} = R`

       If it is separable in `x` and `y`, let `X` be the factors containing `x`. Then

       a] Check if `\\xi = X` and `\\eta = -\\frac{X}{R}` satisfy the PDE. If yes, then return
          `\\xi` and `\\eta`
       b] Check if `\\xi = \\frac{-R}{X}` and `\\eta = -\\frac{1}{X}` satisfy the PDE.
           If yes, then return `\\xi` and `\\eta`

       If not, then check if

       a] :math:`\\xi = -R,\\eta = 1`

       b] :math:`\\xi = 1, \\eta = -\\frac{1}{R}`

       are solutions.

    References
    ==========
    - E.S. Cheb-Terrab, A.D. Roche, Symmetries and First Order
      ODE Patterns, pp. 10 - pp. 12

    """
def lie_heuristic_abaco2_unique_general(match, comp: bool = False):
    """
    This heuristic finds if infinitesimals of the form `\\eta = f(x)`, `\\xi = g(y)`
    without making any assumptions on `h`.

    The complete sequence of steps is given in the paper mentioned below.

    References
    ==========
    - E.S. Cheb-Terrab, A.D. Roche, Symmetries and First Order
      ODE Patterns, pp. 10 - pp. 12

    """
def lie_heuristic_linear(match, comp: bool = False):
    """
    This heuristic assumes

    1. `\\xi = ax + by + c` and
    2. `\\eta = fx + gy + h`

    After substituting the following assumptions in the determining PDE, it
    reduces to

    .. math:: f + (g - a)h - bh^{2} - (ax + by + c)\\frac{\\partial h}{\\partial x}
                 - (fx + gy + c)\\frac{\\partial h}{\\partial y}

    Solving the reduced PDE obtained, using the method of characteristics, becomes
    impractical. The method followed is grouping similar terms and solving the system
    of linear equations obtained. The difference between the bivariate heuristic is that
    `h` need not be a rational function in this case.

    References
    ==========
    - E.S. Cheb-Terrab, A.D. Roche, Symmetries and First Order
      ODE Patterns, pp. 10 - pp. 12

    """
