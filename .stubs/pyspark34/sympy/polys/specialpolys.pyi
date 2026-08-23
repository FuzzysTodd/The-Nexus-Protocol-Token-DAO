from _typeshed import Incomplete
from sympy.core import Add as Add, Dummy as Dummy, Mul as Mul, Symbol as Symbol, symbols as symbols, sympify as sympify
from sympy.core.containers import Tuple as Tuple
from sympy.core.singleton import S as S
from sympy.ntheory import nextprime as nextprime
from sympy.polys.densearith import dmp_add_term as dmp_add_term, dmp_mul as dmp_mul, dmp_neg as dmp_neg, dmp_sqr as dmp_sqr
from sympy.polys.densebasic import dmp_ground as dmp_ground, dmp_one as dmp_one, dmp_raise as dmp_raise, dmp_zero as dmp_zero, dup_from_raw_dict as dup_from_raw_dict, dup_random as dup_random
from sympy.polys.domains import ZZ as ZZ
from sympy.polys.factortools import dup_zz_cyclotomic_poly as dup_zz_cyclotomic_poly
from sympy.polys.polyclasses import DMP as DMP
from sympy.polys.polytools import Poly as Poly, PurePoly as PurePoly
from sympy.polys.rings import ring as ring
from sympy.utilities import filldedent as filldedent, public as public, subsets as subsets

def swinnerton_dyer_poly(n, x: Incomplete | None = None, polys: bool = False):
    """Generates n-th Swinnerton-Dyer polynomial in `x`.

    Parameters
    ----------
    n : int
        `n` decides the order of polynomial
    x : optional
    polys : bool, optional
        ``polys=True`` returns an expression, otherwise
        (default) returns an expression.
    """
def cyclotomic_poly(n, x: Incomplete | None = None, polys: bool = False):
    """Generates cyclotomic polynomial of order `n` in `x`.

    Parameters
    ----------
    n : int
        `n` decides the order of polynomial
    x : optional
    polys : bool, optional
        ``polys=True`` returns an expression, otherwise
        (default) returns an expression.
    """
def symmetric_poly(n, *gens, polys: bool = False):
    """
    Generates symmetric polynomial of order `n`.

    Parameters
    ==========

    polys: bool, optional (default: False)
        Returns a Poly object when ``polys=True``, otherwise
        (default) returns an expression.
    """
def random_poly(x, n, inf, sup, domain=..., polys: bool = False):
    """Generates a polynomial of degree ``n`` with coefficients in
    ``[inf, sup]``.

    Parameters
    ----------
    x
        `x` is the independent term of polynomial
    n : int
        `n` decides the order of polynomial
    inf
        Lower limit of range in which coefficients lie
    sup
        Upper limit of range in which coefficients lie
    domain : optional
         Decides what ring the coefficients are supposed
         to belong. Default is set to Integers.
    polys : bool, optional
        ``polys=True`` returns an expression, otherwise
        (default) returns an expression.
    """
def interpolating_poly(n, x, X: str = 'x', Y: str = 'y'):
    """Construct Lagrange interpolating polynomial for ``n``
    data points. If a sequence of values are given for ``X`` and ``Y``
    then the first ``n`` values will be used.
    """
def fateman_poly_F_1(n):
    """Fateman's GCD benchmark: trivial GCD """
def dmp_fateman_poly_F_1(n, K):
    """Fateman's GCD benchmark: trivial GCD """
def fateman_poly_F_2(n):
    """Fateman's GCD benchmark: linearly dense quartic inputs """
def dmp_fateman_poly_F_2(n, K):
    """Fateman's GCD benchmark: linearly dense quartic inputs """
def fateman_poly_F_3(n):
    """Fateman's GCD benchmark: sparse inputs (deg f ~ vars f) """
def dmp_fateman_poly_F_3(n, K):
    """Fateman's GCD benchmark: sparse inputs (deg f ~ vars f) """
def f_polys(): ...
def w_polys(): ...
