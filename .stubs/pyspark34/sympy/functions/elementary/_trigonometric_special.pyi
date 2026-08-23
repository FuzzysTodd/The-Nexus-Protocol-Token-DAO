from sympy.core.cache import cacheit as cacheit
from sympy.core.expr import Expr as Expr
from sympy.core.numbers import Integer as Integer, igcdex as igcdex
from sympy.core.singleton import S as S
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from typing import Callable

def migcdex(*x: int) -> tuple[tuple[int, ...], int]:
    """Compute extended gcd for multiple integers.

    Explanation
    ===========

    Given the integers $x_1, \\cdots, x_n$ and
    an extended gcd for multiple arguments are defined as a solution
    $(y_1, \\cdots, y_n), g$ for the diophantine equation
    $x_1 y_1 + \\cdots + x_n y_n = g$ such that
    $g = \\gcd(x_1, \\cdots, x_n)$.

    Examples
    ========

    >>> from sympy.functions.elementary._trigonometric_special import migcdex
    >>> migcdex()
    ((), 0)
    >>> migcdex(4)
    ((1,), 4)
    >>> migcdex(4, 6)
    ((-1, 1), 2)
    >>> migcdex(6, 10, 15)
    ((1, 1, -1), 1)
    """
def ipartfrac(*denoms: int) -> tuple[int, ...]:
    """Compute the the partial fraction decomposition.

    Explanation
    ===========

    Given a rational number $\\frac{1}{q_1 \\cdots q_n}$ where all
    $q_1, \\cdots, q_n$ are pairwise coprime,

    A partial fraction decomposition is defined as

    .. math::
        \\frac{1}{q_1 \\cdots q_n} = \\frac{p_1}{q_1} + \\cdots + \\frac{p_n}{q_n}

    And it can be derived from solving the following diophantine equation for
    the $p_1, \\cdots, p_n$

    .. math::
        1 = p_1 \\prod_{i \\ne 1}q_i + \\cdots + p_n \\prod_{i \\ne n}q_i

    Where $q_1, \\cdots, q_n$ being pairwise coprime implies
    $\\gcd(\\prod_{i \\ne 1}q_i, \\cdots, \\prod_{i \\ne n}q_i) = 1$,
    which guarantees the existance of the solution.

    It is sufficient to compute partial fraction decomposition only
    for numerator $1$ because partial fraction decomposition for any
    $\\frac{n}{q_1 \\cdots q_n}$ can be easily computed by multiplying
    the result by $n$ afterwards.

    Parameters
    ==========

    denoms : int
        The pairwise coprime integer denominators $q_i$ which defines the
        rational number $\\frac{1}{q_1 \\cdots q_n}$

    Returns
    =======

    tuple[int, ...]
        The list of numerators which semantically corresponds to $p_i$ of the
        partial fraction decomposition
        $\\frac{1}{q_1 \\cdots q_n} = \\frac{p_1}{q_1} + \\cdots + \\frac{p_n}{q_n}$

    Examples
    ========

    >>> from sympy import Rational, Mul
    >>> from sympy.functions.elementary._trigonometric_special import ipartfrac

    >>> denoms = 2, 3, 5
    >>> numers = ipartfrac(2, 3, 5)
    >>> numers
    (1, 7, -14)

    >>> Rational(1, Mul(*denoms))
    1/30
    >>> out = 0
    >>> for n, d in zip(numers, denoms):
    ...    out += Rational(n, d)
    >>> out
    1/30
    """
def fermat_coords(n: int) -> list[int] | None:
    """If n can be factored in terms of Fermat primes with
    multiplicity of each being 1, return those primes, else
    None
    """
def cos_3() -> Expr:
    """Computes $\\cos \\frac{\\pi}{3}$ in square roots"""
def cos_5() -> Expr:
    """Computes $\\cos \\frac{\\pi}{5}$ in square roots"""
def cos_17() -> Expr:
    """Computes $\\cos \\frac{\\pi}{17}$ in square roots"""
def cos_257() -> Expr:
    """Computes $\\cos \\frac{\\pi}{257}$ in square roots

    References
    ==========

    .. [*] https://math.stackexchange.com/questions/516142/how-does-cos2-pi-257-look-like-in-real-radicals
    .. [*] https://r-knott.surrey.ac.uk/Fibonacci/simpleTrig.html
    """
def cos_table() -> dict[int, Callable[[], Expr]]:
    """Lazily evaluated table for $\\cos \\frac{\\pi}{n}$ in square roots for
    $n \\in \\{3, 5, 17, 257, 65537\\}$.

    Notes
    =====

    65537 is the only other known Fermat prime and it is nearly impossible to
    build in the current SymPy due to performance issues.

    References
    ==========

    https://r-knott.surrey.ac.uk/Fibonacci/simpleTrig.html
    """
