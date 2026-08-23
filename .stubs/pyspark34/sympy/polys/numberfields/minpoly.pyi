from _typeshed import Incomplete
from sympy.core.add import Add as Add
from sympy.core.exprtools import Factors as Factors
from sympy.core.function import expand_mul as expand_mul, expand_multinomial as expand_multinomial
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import I as I, Rational as Rational, pi as pi
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy
from sympy.core.sympify import sympify as sympify
from sympy.core.traversal import preorder_traversal as preorder_traversal
from sympy.functions.elementary.exponential import exp as exp
from sympy.functions.elementary.miscellaneous import cbrt as cbrt, sqrt as sqrt
from sympy.functions.elementary.trigonometric import cos as cos, sin as sin, tan as tan
from sympy.ntheory.factor_ import divisors as divisors
from sympy.polys.domains import FractionField as FractionField, QQ as QQ, ZZ as ZZ
from sympy.polys.orthopolys import dup_chebyshevt as dup_chebyshevt
from sympy.polys.polyerrors import GeneratorsError as GeneratorsError, NotAlgebraic as NotAlgebraic
from sympy.polys.polytools import Poly as Poly, PurePoly as PurePoly, degree as degree, factor_list as factor_list, groebner as groebner, invert as invert, lcm as lcm, parallel_poly_from_expr as parallel_poly_from_expr, poly_from_expr as poly_from_expr, resultant as resultant
from sympy.polys.polyutils import dict_from_expr as dict_from_expr, expr_from_dict as expr_from_dict
from sympy.polys.ring_series import rs_compose_add as rs_compose_add
from sympy.polys.rings import ring as ring
from sympy.polys.rootoftools import CRootOf as CRootOf
from sympy.polys.specialpolys import cyclotomic_poly as cyclotomic_poly
from sympy.utilities import numbered_symbols as numbered_symbols, public as public, sift as sift
from sympy.utilities.iterables import subsets as subsets

def minimal_polynomial(ex, x: Incomplete | None = None, compose: bool = True, polys: bool = False, domain: Incomplete | None = None):
    """
    Computes the minimal polynomial of an algebraic element.

    Parameters
    ==========

    ex : Expr
        Element or expression whose minimal polynomial is to be calculated.

    x : Symbol, optional
        Independent variable of the minimal polynomial

    compose : boolean, optional (default=True)
        Method to use for computing minimal polynomial. If ``compose=True``
        (default) then ``_minpoly_compose`` is used, if ``compose=False`` then
        groebner bases are used.

    polys : boolean, optional (default=False)
        If ``True`` returns a ``Poly`` object else an ``Expr`` object.

    domain : Domain, optional
        Ground domain

    Notes
    =====

    By default ``compose=True``, the minimal polynomial of the subexpressions of ``ex``
    are computed, then the arithmetic operations on them are performed using the resultant
    and factorization.
    If ``compose=False``, a bottom-up algorithm is used with ``groebner``.
    The default algorithm stalls less frequently.

    If no ground domain is given, it will be generated automatically from the expression.

    Examples
    ========

    >>> from sympy import minimal_polynomial, sqrt, solve, QQ
    >>> from sympy.abc import x, y

    >>> minimal_polynomial(sqrt(2), x)
    x**2 - 2
    >>> minimal_polynomial(sqrt(2), x, domain=QQ.algebraic_field(sqrt(2)))
    x - sqrt(2)
    >>> minimal_polynomial(sqrt(2) + sqrt(3), x)
    x**4 - 10*x**2 + 1
    >>> minimal_polynomial(solve(x**3 + x + 3)[0], x)
    x**3 + x + 3
    >>> minimal_polynomial(sqrt(y), x)
    x**2 - y

    """
def minpoly(ex, x: Incomplete | None = None, compose: bool = True, polys: bool = False, domain: Incomplete | None = None):
    """This is a synonym for :py:func:`~.minimal_polynomial`."""
