from _typeshed import Incomplete
from sympy.core.add import Add as Add
from sympy.core.basic import Basic as Basic, sympify as sympify
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import I as I, Rational as Rational, pi as pi
from sympy.core.relational import Eq as Eq, Ne as Ne
from sympy.core.singleton import S as S
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, Wild as Wild
from sympy.core.traversal import iterfreeargs as iterfreeargs
from sympy.functions import Ei as Ei, asin as asin, asinh as asinh, atan as atan, besseli as besseli, besselj as besselj, besselk as besselk, bessely as bessely, cos as cos, cosh as cosh, cot as cot, coth as coth, erf as erf, erfi as erfi, exp as exp, hankel1 as hankel1, hankel2 as hankel2, jn as jn, li as li, log as log, sin as sin, sinh as sinh, sqrt as sqrt, tan as tan, tanh as tanh, yn as yn
from sympy.functions.elementary.complexes import Abs as Abs, arg as arg, im as im, re as re, sign as sign
from sympy.functions.elementary.exponential import LambertW as LambertW
from sympy.functions.elementary.integers import ceiling as ceiling, floor as floor
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.functions.special.delta_functions import DiracDelta as DiracDelta, Heaviside as Heaviside
from sympy.integrals.integrals import integrate as integrate
from sympy.logic.boolalg import And as And, Or as Or
from sympy.polys import PolynomialError as PolynomialError, cancel as cancel, factor_list as factor_list, gcd as gcd, lcm as lcm, quo as quo
from sympy.polys.constructor import construct_domain as construct_domain
from sympy.polys.monomials import itermonomials as itermonomials
from sympy.polys.polyroots import root_factors as root_factors
from sympy.polys.rings import PolyRing as PolyRing
from sympy.polys.solvers import solve_lin_sys as solve_lin_sys
from sympy.simplify.radsimp import collect as collect
from sympy.utilities.iterables import uniq as uniq

def components(f, x):
    """
    Returns a set of all functional components of the given expression
    which includes symbols, function applications and compositions and
    non-integer powers. Fractional powers are collected with
    minimal, positive exponents.

    Examples
    ========

    >>> from sympy import cos, sin
    >>> from sympy.abc import x
    >>> from sympy.integrals.heurisch import components

    >>> components(sin(x)*cos(x)**2, x)
    {x, sin(x), cos(x)}

    See Also
    ========

    heurisch
    """
def heurisch_wrapper(f, x, rewrite: bool = False, hints: Incomplete | None = None, mappings: Incomplete | None = None, retries: int = 3, degree_offset: int = 0, unnecessary_permutations: Incomplete | None = None, _try_heurisch: Incomplete | None = None):
    """
    A wrapper around the heurisch integration algorithm.

    Explanation
    ===========

    This method takes the result from heurisch and checks for poles in the
    denominator. For each of these poles, the integral is reevaluated, and
    the final integration result is given in terms of a Piecewise.

    Examples
    ========

    >>> from sympy import cos, symbols
    >>> from sympy.integrals.heurisch import heurisch, heurisch_wrapper
    >>> n, x = symbols('n x')
    >>> heurisch(cos(n*x), x)
    sin(n*x)/n
    >>> heurisch_wrapper(cos(n*x), x)
    Piecewise((sin(n*x)/n, Ne(n, 0)), (x, True))

    See Also
    ========

    heurisch
    """

class BesselTable:
    """
    Derivatives of Bessel functions of orders n and n-1
    in terms of each other.

    See the docstring of DiffCache.
    """
    table: Incomplete
    n: Incomplete
    z: Incomplete
    def __init__(self) -> None: ...
    def diffs(t, f, n, z): ...
    def has(t, f): ...

class DiffCache:
    """
    Store for derivatives of expressions.

    Explanation
    ===========

    The standard form of the derivative of a Bessel function of order n
    contains two Bessel functions of orders n-1 and n+1, respectively.
    Such forms cannot be used in parallel Risch algorithm, because
    there is a linear recurrence relation between the three functions
    while the algorithm expects that functions and derivatives are
    represented in terms of algebraically independent transcendentals.

    The solution is to take two of the functions, e.g., those of orders
    n and n-1, and to express the derivatives in terms of the pair.
    To guarantee that the proper form is used the two derivatives are
    cached as soon as one is encountered.

    Derivatives of other functions are also cached at no extra cost.
    All derivatives are with respect to the same variable `x`.
    """
    cache: Incomplete
    x: Incomplete
    def __init__(self, x) -> None: ...
    def get_diff(self, f): ...

def heurisch(f, x, rewrite: bool = False, hints: Incomplete | None = None, mappings: Incomplete | None = None, retries: int = 3, degree_offset: int = 0, unnecessary_permutations: Incomplete | None = None, _try_heurisch: Incomplete | None = None):
    '''
    Compute indefinite integral using heuristic Risch algorithm.

    Explanation
    ===========

    This is a heuristic approach to indefinite integration in finite
    terms using the extended heuristic (parallel) Risch algorithm, based
    on Manuel Bronstein\'s "Poor Man\'s Integrator".

    The algorithm supports various classes of functions including
    transcendental elementary or special functions like Airy,
    Bessel, Whittaker and Lambert.

    Note that this algorithm is not a decision procedure. If it isn\'t
    able to compute the antiderivative for a given function, then this is
    not a proof that such a functions does not exist.  One should use
    recursive Risch algorithm in such case.  It\'s an open question if
    this algorithm can be made a full decision procedure.

    This is an internal integrator procedure. You should use top level
    \'integrate\' function in most cases, as this procedure needs some
    preprocessing steps and otherwise may fail.

    Specification
    =============

     heurisch(f, x, rewrite=False, hints=None)

       where
         f : expression
         x : symbol

         rewrite -> force rewrite \'f\' in terms of \'tan\' and \'tanh\'
         hints   -> a list of functions that may appear in anti-derivate

          - hints = None          --> no suggestions at all
          - hints = [ ]           --> try to figure out
          - hints = [f1, ..., fn] --> we know better

    Examples
    ========

    >>> from sympy import tan
    >>> from sympy.integrals.heurisch import heurisch
    >>> from sympy.abc import x, y

    >>> heurisch(y*tan(x), x)
    y*log(tan(x)**2 + 1)/2

    See Manuel Bronstein\'s "Poor Man\'s Integrator":

    References
    ==========

    .. [1] https://www-sop.inria.fr/cafe/Manuel.Bronstein/pmint/index.html

    For more information on the implemented algorithm refer to:

    .. [2] K. Geddes, L. Stefanus, On the Risch-Norman Integration
       Method and its Implementation in Maple, Proceedings of
       ISSAC\'89, ACM Press, 212-217.

    .. [3] J. H. Davenport, On the Parallel Risch Algorithm (I),
       Proceedings of EUROCAM\'82, LNCS 144, Springer, 144-157.

    .. [4] J. H. Davenport, On the Parallel Risch Algorithm (III):
       Use of Tangents, SIGSAM Bulletin 16 (1982), 3-6.

    .. [5] J. H. Davenport, B. M. Trager, On the Parallel Risch
       Algorithm (II), ACM Transactions on Mathematical
       Software 11 (1985), 356-362.

    See Also
    ========

    sympy.integrals.integrals.Integral.doit
    sympy.integrals.integrals.Integral
    sympy.integrals.heurisch.components
    '''
