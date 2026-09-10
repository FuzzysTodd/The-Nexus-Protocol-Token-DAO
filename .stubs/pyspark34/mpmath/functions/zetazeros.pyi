from .functions import defun as defun, defun_wrapped as defun_wrapped
from _typeshed import Incomplete

def find_rosser_block_zero(ctx, n):
    """for n<400 000 000 determines a block were one find our zero"""
def wpzeros(t):
    """Precision needed to compute higher zeros"""
def separate_zeros_in_block(ctx, zero_number_block, T, V, limitloop: Incomplete | None = None, fp_tolerance: Incomplete | None = None):
    """Separate the zeros contained in the block T, limitloop
    determines how long one must search"""
def separate_my_zero(ctx, my_zero_number, zero_number_block, T, V, prec):
    """If we know which zero of this block is mine,
    the function separates the zero"""
def sure_number_block(ctx, n):
    """The number of good Rosser blocks needed to apply
    Turing method
    References:
    R. P. Brent, On the Zeros of the Riemann Zeta Function
    in the Critical Strip, Math. Comp. 33 (1979) 1361--1372
    T. Trudgian, Improvements to Turing Method, Math. Comp."""
def compute_triple_tvb(ctx, n): ...

ITERATION_LIMIT: int

def search_supergood_block(ctx, n, fp_tolerance):
    """To use for n>400 000 000"""
def count_variations(V): ...
def pattern_construct(ctx, block, T, V): ...
def zetazero(ctx, n, info: bool = False, round: bool = True):
    """
    Computes the `n`-th nontrivial zero of `\\zeta(s)` on the critical line,
    i.e. returns an approximation of the `n`-th largest complex number
    `s = \\frac{1}{2} + ti` for which `\\zeta(s) = 0`. Equivalently, the
    imaginary part `t` is a zero of the Z-function (:func:`~mpmath.siegelz`).

    **Examples**

    The first few zeros::

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> zetazero(1)
        (0.5 + 14.13472514173469379045725j)
        >>> zetazero(2)
        (0.5 + 21.02203963877155499262848j)
        >>> zetazero(20)
        (0.5 + 77.14484006887480537268266j)

    Verifying that the values are zeros::

        >>> for n in range(1,5):
        ...     s = zetazero(n)
        ...     chop(zeta(s)), chop(siegelz(s.imag))
        ...
        (0.0, 0.0)
        (0.0, 0.0)
        (0.0, 0.0)
        (0.0, 0.0)

    Negative indices give the conjugate zeros (`n = 0` is undefined)::

        >>> zetazero(-1)
        (0.5 - 14.13472514173469379045725j)

    :func:`~mpmath.zetazero` supports arbitrarily large `n` and arbitrary precision::

        >>> mp.dps = 15
        >>> zetazero(1234567)
        (0.5 + 727690.906948208j)
        >>> mp.dps = 50
        >>> zetazero(1234567)
        (0.5 + 727690.9069482075392389420041147142092708393819935j)
        >>> chop(zeta(_)/_)
        0.0

    with *info=True*, :func:`~mpmath.zetazero` gives additional information::

        >>> mp.dps = 15
        >>> zetazero(542964976,info=True)
        ((0.5 + 209039046.578535j), [542964969, 542964978], 6, '(013111110)')

    This means that the zero is between Gram points 542964969 and 542964978;
    it is the 6-th zero between them. Finally (01311110) is the pattern
    of zeros in this interval. The numbers indicate the number of zeros
    in each Gram interval (Rosser blocks between parenthesis). In this case
    there is only one Rosser block of length nine.
    """
def gram_index(ctx, t): ...
def count_to(ctx, t, T, V): ...
def comp_fp_tolerance(ctx, n): ...
def nzeros(ctx, t):
    """
    Computes the number of zeros of the Riemann zeta function in
    `(0,1) \\times (0,t]`, usually denoted by `N(t)`.

    **Examples**

    The first zero has imaginary part between 14 and 15::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> nzeros(14)
        0
        >>> nzeros(15)
        1
        >>> zetazero(1)
        (0.5 + 14.1347251417347j)

    Some closely spaced zeros::

        >>> nzeros(10**7)
        21136125
        >>> zetazero(21136125)
        (0.5 + 9999999.32718175j)
        >>> zetazero(21136126)
        (0.5 + 10000000.2400236j)
        >>> nzeros(545439823.215)
        1500000001
        >>> zetazero(1500000001)
        (0.5 + 545439823.201985j)
        >>> zetazero(1500000002)
        (0.5 + 545439823.325697j)

    This confirms the data given by J. van de Lune,
    H. J. J. te Riele and D. T. Winter in 1986.
    """
def backlunds(ctx, t):
    """
    Computes the function
    `S(t) = \\operatorname{arg} \\zeta(\\frac{1}{2} + it) / \\pi`.

    See Titchmarsh Section 9.3 for details of the definition.

    **Examples**

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> backlunds(217.3)
        0.16302205431184

    Generally, the value is a small number. At Gram points it is an integer,
    frequently equal to 0::

        >>> chop(backlunds(grampoint(200)))
        0.0
        >>> backlunds(extraprec(10)(grampoint)(211))
        1.0
        >>> backlunds(extraprec(10)(grampoint)(232))
        -1.0

    The number of zeros of the Riemann zeta function up to height `t`
    satisfies `N(t) = \\theta(t)/\\pi + 1 + S(t)` (see :func:nzeros` and
    :func:`siegeltheta`)::

        >>> t = 1234.55
        >>> nzeros(t)
        842
        >>> siegeltheta(t)/pi+1+backlunds(t)
        842.0

    """
