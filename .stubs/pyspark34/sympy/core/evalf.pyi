from .numbers import AlgebraicNumber as AlgebraicNumber, Float as Float, Integer as Integer, Number as Number, Rational as Rational
from .singleton import S as S
from .sympify import sympify as sympify
from _typeshed import Incomplete
from mpmath import mpc, mpf
from mpmath.libmp import round_nearest
from sympy.concrete.products import Product as Product
from sympy.concrete.summations import Sum as Sum
from sympy.core.add import Add as Add
from sympy.core.expr import Expr as Expr
from sympy.core.mul import Mul as Mul
from sympy.core.power import Pow as Pow
from sympy.core.symbol import Symbol as Symbol
from sympy.external.gmpy import SYMPY_INTS as SYMPY_INTS
from sympy.functions.elementary.complexes import Abs as Abs, im as im, re as re
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.integers import ceiling as ceiling, floor as floor
from sympy.functions.elementary.trigonometric import atan as atan
from sympy.integrals.integrals import Integral as Integral
from sympy.utilities.iterables import is_sequence as is_sequence
from sympy.utilities.lambdify import lambdify as lambdify
from sympy.utilities.misc import as_int as as_int
from typing import Any, Callable, Dict as tDict, List, Tuple as tTuple, Type, overload

LG10: Incomplete
rnd = round_nearest

def bitcount(n):
    """Return smallest integer, b, such that |n|/2**b < 1.
    """

INF: Incomplete
MINUS_INF: Incomplete
DEFAULT_MAXPREC: int

class PrecisionExhausted(ArithmeticError): ...
MPF_TUP = tTuple[int, int, int, int]
TMP_RES = Any
OPT_DICT = tDict[str, Any]

def fastlog(x: MPF_TUP | None) -> int | Any:
    '''Fast approximation of log2(x) for an mpf value tuple x.

    Explanation
    ===========

    Calculated as exponent + width of mantissa. This is an
    approximation for two reasons: 1) it gives the ceil(log2(abs(x)))
    value and 2) it is too high by 1 in the case that x is an exact
    power of 2. Although this is easy to remedy by testing to see if
    the odd mpf mantissa is 1 (indicating that one was dealing with
    an exact power of 2) that would decrease the speed and is not
    necessary as this is only being used as an approximation for the
    number of bits in x. The correct return value could be written as
    "x[2] + (x[3] if x[1] != 1 else 0)".
        Since mpf tuples always have an odd mantissa, no check is done
    to see if the mantissa is a multiple of 2 (in which case the
    result would be too large by 1).

    Examples
    ========

    >>> from sympy import log
    >>> from sympy.core.evalf import fastlog, bitcount
    >>> s, m, e = 0, 5, 1
    >>> bc = bitcount(m)
    >>> n = [1, -1][s]*m*2**e
    >>> n, (log(n)/log(2)).evalf(2), fastlog((s, m, e, bc))
    (10, 3.3, 4)
    '''
def pure_complex(v: Expr, or_real: bool = False) -> tuple['Number', 'Number'] | None:
    """Return a and b if v matches a + I*b where b is not zero and
    a and b are Numbers, else None. If `or_real` is True then 0 will
    be returned for `b` if `v` is a real number.

    Examples
    ========

    >>> from sympy.core.evalf import pure_complex
    >>> from sympy import sqrt, I, S
    >>> a, b, surd = S(2), S(3), sqrt(2)
    >>> pure_complex(a)
    >>> pure_complex(a, or_real=True)
    (2, 0)
    >>> pure_complex(surd)
    >>> pure_complex(a + b*I)
    (2, 3)
    >>> pure_complex(I)
    (0, 1)
    """
SCALED_ZERO_TUP = tTuple[List[int], int, int, int]

@overload
def scaled_zero(mag: SCALED_ZERO_TUP, sign: int = 1) -> MPF_TUP: ...
@overload
def scaled_zero(mag: int, sign: int = 1) -> tTuple[SCALED_ZERO_TUP, int]: ...
def iszero(mpf: MPF_TUP | SCALED_ZERO_TUP | None, scaled: bool = False) -> bool | None: ...
def complex_accuracy(result: TMP_RES) -> int | Any:
    """
    Returns relative accuracy of a complex number with given accuracies
    for the real and imaginary parts. The relative accuracy is defined
    in the complex norm sense as ||z|+|error|| / |z| where error
    is equal to (real absolute error) + (imag absolute error)*i.

    The full expression for the (logarithmic) error can be approximated
    easily by using the max norm to approximate the complex norm.

    In the worst case (re and im equal), this is wrong by a factor
    sqrt(2), or by log2(sqrt(2)) = 0.5 bit.
    """
def get_abs(expr: Expr, prec: int, options: OPT_DICT) -> TMP_RES: ...
def get_complex_part(expr: Expr, no: int, prec: int, options: OPT_DICT) -> TMP_RES:
    """no = 0 for real part, no = 1 for imaginary part"""
def evalf_abs(expr: Abs, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_re(expr: re, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_im(expr: im, prec: int, options: OPT_DICT) -> TMP_RES: ...
def finalize_complex(re: MPF_TUP, im: MPF_TUP, prec: int) -> TMP_RES: ...
def chop_parts(value: TMP_RES, prec: int) -> TMP_RES:
    """
    Chop off tiny real or complex parts.
    """
def check_target(expr: Expr, result: TMP_RES, prec: int): ...
def get_integer_part(expr: Expr, no: int, options: OPT_DICT, return_ints: bool = False) -> TMP_RES | tTuple[int, int]:
    """
    With no = 1, computes ceiling(expr)
    With no = -1, computes floor(expr)

    Note: this function either gives the exact result or signals failure.
    """
def evalf_ceiling(expr: ceiling, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_floor(expr: floor, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_float(expr: Float, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_rational(expr: Rational, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_integer(expr: Integer, prec: int, options: OPT_DICT) -> TMP_RES: ...
def add_terms(terms: list, prec: int, target_prec: int) -> tTuple[MPF_TUP | SCALED_ZERO_TUP | None, int | None]:
    """
    Helper for evalf_add. Adds a list of (mpfval, accuracy) terms.

    Returns
    =======

    - None, None if there are no non-zero terms;
    - terms[0] if there is only 1 term;
    - scaled_zero if the sum of the terms produces a zero by cancellation
      e.g. mpfs representing 1 and -1 would produce a scaled zero which need
      special handling since they are not actually zero and they are purposely
      malformed to ensure that they cannot be used in anything but accuracy
      calculations;
    - a tuple that is scaled to target_prec that corresponds to the
      sum of the terms.

    The returned mpf tuple will be normalized to target_prec; the input
    prec is used to define the working precision.

    XXX explain why this is needed and why one cannot just loop using mpf_add
    """
def evalf_add(v: Add, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_mul(v: Mul, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_pow(v: Pow, prec: int, options) -> TMP_RES: ...
def evalf_exp(expr: exp, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_trig(v: Expr, prec: int, options: OPT_DICT) -> TMP_RES:
    """
    This function handles sin and cos of complex arguments.

    TODO: should also handle tan of complex arguments.
    """
def evalf_log(expr: log, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_atan(v: atan, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_subs(prec: int, subs: dict) -> dict:
    """ Change all Float entries in `subs` to have precision prec. """
def evalf_piecewise(expr: Expr, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_alg_num(a: AlgebraicNumber, prec: int, options: OPT_DICT) -> TMP_RES: ...
def as_mpmath(x: Any, prec: int, options: OPT_DICT) -> mpc | mpf: ...
def do_integral(expr: Integral, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_integral(expr: Integral, prec: int, options: OPT_DICT) -> TMP_RES: ...
def check_convergence(numer: Expr, denom: Expr, n: Symbol) -> tTuple[int, Any, Any]:
    """
    Returns
    =======

    (h, g, p) where
    -- h is:
        > 0 for convergence of rate 1/factorial(n)**h
        < 0 for divergence of rate factorial(n)**(-h)
        = 0 for geometric or polynomial convergence or divergence

    -- abs(g) is:
        > 1 for geometric convergence of rate 1/h**n
        < 1 for geometric divergence of rate h**n
        = 1 for polynomial convergence or divergence

        (g < 0 indicates an alternating series)

    -- p is:
        > 1 for polynomial convergence of rate 1/n**h
        <= 1 for polynomial divergence of rate n**(-h)

    """
def hypsum(expr: Expr, n: Symbol, start: int, prec: int) -> mpf:
    """
    Sum a rapidly convergent infinite hypergeometric series with
    given general term, e.g. e = hypsum(1/factorial(n), n). The
    quotient between successive terms must be a quotient of integer
    polynomials.
    """
def evalf_prod(expr: Product, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_sum(expr: Sum, prec: int, options: OPT_DICT) -> TMP_RES: ...
def evalf_symbol(x: Expr, prec: int, options: OPT_DICT) -> TMP_RES: ...

evalf_table: tDict[Type['Expr'], Callable[[Expr, int, OPT_DICT], TMP_RES]]

def evalf(x: Expr, prec: int, options: OPT_DICT) -> TMP_RES:
    """
    Evaluate the ``Expr`` instance, ``x``
    to a binary precision of ``prec``. This
    function is supposed to be used internally.

    Parameters
    ==========

    x : Expr
        The formula to evaluate to a float.
    prec : int
        The binary precision that the output should have.
    options : dict
        A dictionary with the same entries as
        ``EvalfMixin.evalf`` and in addition,
        ``maxprec`` which is the maximum working precision.

    Returns
    =======

    An optional tuple, ``(re, im, re_acc, im_acc)``
    which are the real, imaginary, real accuracy
    and imaginary accuracy respectively. ``re`` is
    an mpf value tuple and so is ``im``. ``re_acc``
    and ``im_acc`` are ints.

    NB: all these return values can be ``None``.
    If all values are ``None``, then that represents 0.
    Note that 0 is also represented as ``fzero = (0, 0, 0, 0)``.
    """
def quad_to_mpmath(q, ctx: Incomplete | None = None):
    """Turn the quad returned by ``evalf`` into an ``mpf`` or ``mpc``. """

class EvalfMixin:
    """Mixin class adding evalf capability."""
    def evalf(self, n: int = 15, subs: Incomplete | None = None, maxn: int = 100, chop: bool = False, strict: bool = False, quad: Incomplete | None = None, verbose: bool = False):
        '''
        Evaluate the given formula to an accuracy of *n* digits.

        Parameters
        ==========

        subs : dict, optional
            Substitute numerical values for symbols, e.g.
            ``subs={x:3, y:1+pi}``. The substitutions must be given as a
            dictionary.

        maxn : int, optional
            Allow a maximum temporary working precision of maxn digits.

        chop : bool or number, optional
            Specifies how to replace tiny real or imaginary parts in
            subresults by exact zeros.

            When ``True`` the chop value defaults to standard precision.

            Otherwise the chop value is used to determine the
            magnitude of "small" for purposes of chopping.

            >>> from sympy import N
            >>> x = 1e-4
            >>> N(x, chop=True)
            0.000100000000000000
            >>> N(x, chop=1e-5)
            0.000100000000000000
            >>> N(x, chop=1e-4)
            0

        strict : bool, optional
            Raise ``PrecisionExhausted`` if any subresult fails to
            evaluate to full accuracy, given the available maxprec.

        quad : str, optional
            Choose algorithm for numerical quadrature. By default,
            tanh-sinh quadrature is used. For oscillatory
            integrals on an infinite interval, try ``quad=\'osc\'``.

        verbose : bool, optional
            Print debug information.

        Notes
        =====

        When Floats are naively substituted into an expression,
        precision errors may adversely affect the result. For example,
        adding 1e16 (a Float) to 1 will truncate to 1e16; if 1e16 is
        then subtracted, the result will be 0.
        That is exactly what happens in the following:

        >>> from sympy.abc import x, y, z
        >>> values = {x: 1e16, y: 1, z: 1e16}
        >>> (x + y - z).subs(values)
        0

        Using the subs argument for evalf is the accurate way to
        evaluate such an expression:

        >>> (x + y - z).evalf(subs=values)
        1.00000000000000
        '''
    n = evalf

def N(x, n: int = 15, **options):
    """
    Calls x.evalf(n, \\*\\*options).

    Explanations
    ============

    Both .n() and N() are equivalent to .evalf(); use the one that you like better.
    See also the docstring of .evalf() for information on the options.

    Examples
    ========

    >>> from sympy import Sum, oo, N
    >>> from sympy.abc import k
    >>> Sum(1/k**k, (k, 1, oo))
    Sum(k**(-k), (k, 1, oo))
    >>> N(_, 4)
    1.291

    """
