from _typeshed import Incomplete
from sympy.utilities.iterables import is_sequence as is_sequence
from sympy.utilities.misc import as_int as as_int

rng: Incomplete
choice: Incomplete
random: Incomplete
randint: Incomplete
randrange: Incomplete
sample: Incomplete
shuffle: Incomplete
uniform: Incomplete

def seed(a: Incomplete | None = None, version: int = 2) -> None: ...
def random_complex_number(a: int = 2, b: int = -1, c: int = 3, d: int = 1, rational: bool = False, tolerance: Incomplete | None = None):
    """
    Return a random complex number.

    To reduce chance of hitting branch cuts or anything, we guarantee
    b <= Im z <= d, a <= Re z <= c

    When rational is True, a rational approximation to a random number
    is obtained within specified tolerance, if any.
    """
def verify_numerically(f, g, z: Incomplete | None = None, tol: float = 1e-06, a: int = 2, b: int = -1, c: int = 3, d: int = 1):
    """
    Test numerically that f and g agree when evaluated in the argument z.

    If z is None, all symbols will be tested. This routine does not test
    whether there are Floats present with precision higher than 15 digits
    so if there are, your results may not be what you expect due to round-
    off errors.

    Examples
    ========

    >>> from sympy import sin, cos
    >>> from sympy.abc import x
    >>> from sympy.core.random import verify_numerically as tn
    >>> tn(sin(x)**2 + cos(x)**2, 1, x)
    True
    """
def test_derivative_numerically(f, z, tol: float = 1e-06, a: int = 2, b: int = -1, c: int = 3, d: int = 1):
    """
    Test numerically that the symbolically computed derivative of f
    with respect to z is correct.

    This routine does not test whether there are Floats present with
    precision higher than 15 digits so if there are, your results may
    not be what you expect due to round-off errors.

    Examples
    ========

    >>> from sympy import sin
    >>> from sympy.abc import x
    >>> from sympy.core.random import test_derivative_numerically as td
    >>> td(sin(x), x)
    True
    """
