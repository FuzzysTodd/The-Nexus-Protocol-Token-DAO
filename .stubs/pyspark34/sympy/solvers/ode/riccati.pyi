from _typeshed import Incomplete
from sympy.core import S as S
from sympy.core.add import Add as Add
from sympy.core.function import count_ops as count_ops
from sympy.core.numbers import Float as Float, oo as oo
from sympy.core.relational import Eq as Eq
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, symbols as symbols
from sympy.functions import exp as exp, sqrt as sqrt
from sympy.functions.elementary.complexes import sign as sign
from sympy.integrals.integrals import Integral as Integral
from sympy.polys.domains import ZZ as ZZ
from sympy.polys.polyroots import roots as roots
from sympy.polys.polytools import Poly as Poly
from sympy.solvers.solveset import linsolve as linsolve

def riccati_normal(w, x, b1, b2):
    """
    Given a solution `w(x)` to the equation

    .. math:: w'(x) = b_0(x) + b_1(x)*w(x) + b_2(x)*w(x)^2

    and rational function coefficients `b_1(x)` and
    `b_2(x)`, this function transforms the solution to
    give a solution `y(x)` for its corresponding normal
    Riccati ODE

    .. math:: y'(x) + y(x)^2 = a(x)

    using the transformation

    .. math:: y(x) = -b_2(x)*w(x) - b'_2(x)/(2*b_2(x)) - b_1(x)/2
    """
def riccati_inverse_normal(y, x, b1, b2, bp: Incomplete | None = None):
    """
    Inverse transforming the solution to the normal
    Riccati ODE to get the solution to the Riccati ODE.
    """
def riccati_reduced(eq, f, x):
    """
    Convert a Riccati ODE into its corresponding
    normal Riccati ODE.
    """
def linsolve_dict(eq, syms):
    """
    Get the output of linsolve as a dict
    """
def match_riccati(eq, f, x):
    """
    A function that matches and returns the coefficients
    if an equation is a Riccati ODE

    Parameters
    ==========

    eq: Equation to be matched
    f: Dependent variable
    x: Independent variable

    Returns
    =======

    match: True if equation is a Riccati ODE, False otherwise
    funcs: [b0, b1, b2] if match is True, [] otherwise. Here,
    b0, b1 and b2 are rational functions which match the equation.
    """
def val_at_inf(num, den, x): ...
def check_necessary_conds(val_inf, muls):
    """
    The necessary conditions for a rational solution
    to exist are as follows -

    i) Every pole of a(x) must be either a simple pole
    or a multiple pole of even order.

    ii) The valuation of a(x) at infinity must be even
    or be greater than or equal to 2.

    Here, a simple pole is a pole with multiplicity 1
    and a multiple pole is a pole with multiplicity
    greater than 1.
    """
def inverse_transform_poly(num, den, x):
    """
    A function to make the substitution
    x -> 1/x in a rational function that
    is represented using Poly objects for
    numerator and denominator.
    """
def limit_at_inf(num, den, x):
    """
    Find the limit of a rational function
    at oo
    """
def construct_c_case_1(num, den, x, pole): ...
def construct_c_case_2(num, den, x, pole, mul): ...
def construct_c_case_3(): ...
def construct_c(num, den, x, poles, muls):
    """
    Helper function to calculate the coefficients
    in the c-vector for each pole.
    """
def construct_d_case_4(ser, N): ...
def construct_d_case_5(ser): ...
def construct_d_case_6(num, den, x): ...
def construct_d(num, den, x, val_inf):
    """
    Helper function to calculate the coefficients
    in the d-vector based on the valuation of the
    function at oo.
    """
def rational_laurent_series(num, den, x, r, m, n):
    """
    The function computes the Laurent series coefficients
    of a rational function.

    Parameters
    ==========

    num: A Poly object that is the numerator of `f(x)`.
    den: A Poly object that is the denominator of `f(x)`.
    x: The variable of expansion of the series.
    r: The point of expansion of the series.
    m: Multiplicity of r if r is a pole of `f(x)`. Should
    be zero otherwise.
    n: Order of the term upto which the series is expanded.

    Returns
    =======

    series: A dictionary that has power of the term as key
    and coefficient of that term as value.

    Below is a basic outline of how the Laurent series of a
    rational function `f(x)` about `x_0` is being calculated -

    1. Substitute `x + x_0` in place of `x`. If `x_0`
    is a pole of `f(x)`, multiply the expression by `x^m`
    where `m` is the multiplicity of `x_0`. Denote the
    the resulting expression as g(x). We do this substitution
    so that we can now find the Laurent series of g(x) about
    `x = 0`.

    2. We can then assume that the Laurent series of `g(x)`
    takes the following form -

    .. math:: g(x) = \\frac{num(x)}{den(x)} = \\sum_{m = 0}^{\\infty} a_m x^m

    where `a_m` denotes the Laurent series coefficients.

    3. Multiply the denominator to the RHS of the equation
    and form a recurrence relation for the coefficients `a_m`.
    """
def compute_m_ybar(x, poles, choice, N):
    """
    Helper function to calculate -

    1. m - The degree bound for the polynomial
    solution that must be found for the auxiliary
    differential equation.

    2. ybar - Part of the solution which can be
    computed using the poles, c and d vectors.
    """
def solve_aux_eq(numa, dena, numy, deny, x, m):
    """
    Helper function to find a polynomial solution
    of degree m for the auxiliary differential
    equation.
    """
def remove_redundant_sols(sol1, sol2, x):
    """
    Helper function to remove redundant
    solutions to the differential equation.
    """
def get_gen_sol_from_part_sol(part_sols, a, x):
    '''"
    Helper function which computes the general
    solution for a Riccati ODE from its particular
    solutions.

    There are 3 cases to find the general solution
    from the particular solutions for a Riccati ODE
    depending on the number of particular solution(s)
    we have - 1, 2 or 3.

    For more information, see Section 6 of
    "Methods of Solution of the Riccati Differential Equation"
    by D. R. Haaheim and F. M. Stein
    '''
def solve_riccati(fx, x, b0, b1, b2, gensol: bool = False):
    """
    The main function that gives particular/general
    solutions to Riccati ODEs that have atleast 1
    rational particular solution.
    """
