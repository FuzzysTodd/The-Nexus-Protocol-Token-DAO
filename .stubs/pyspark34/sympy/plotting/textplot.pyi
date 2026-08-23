from _typeshed import Incomplete
from collections.abc import Generator
from sympy.core.numbers import Float as Float
from sympy.core.symbol import Dummy as Dummy
from sympy.utilities.lambdify import lambdify as lambdify

def is_valid(x):
    """Check if a floating point number is valid"""
def rescale(y, W, H, mi, ma):
    """Rescale the given array `y` to fit into the integer values
    between `0` and `H-1` for the values between ``mi`` and ``ma``.
    """
def linspace(start, stop, num): ...
def textplot_str(expr, a, b, W: int = 55, H: int = 21) -> Generator[Incomplete, None, None]:
    """Generator for the lines of the plot"""
def textplot(expr, a, b, W: int = 55, H: int = 21) -> None:
    """
    Print a crude ASCII art plot of the SymPy expression 'expr' (which
    should contain a single symbol, e.g. x or something else) over the
    interval [a, b].

    Examples
    ========

    >>> from sympy import Symbol, sin
    >>> from sympy.plotting import textplot
    >>> t = Symbol('t')
    >>> textplot(sin(t)*t, 0, 15)
     14 |                                                  ...
        |                                                     .
        |                                                 .
        |                                                      .
        |                                                .
        |                            ...
        |                           /   .               .
        |                          /
        |                         /      .
        |                        .        .            .
    1.5 |----.......--------------------------------------------
        |....       \\           .          .
        |            \\         /                      .
        |             ..      /             .
        |               \\    /                       .
        |                ....
        |                                    .
        |                                     .     .
        |
        |                                      .   .
    -11 |_______________________________________________________
         0                          7.5                        15
    """
