from sympy.core import S as S, diff as diff, oo as oo
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.logic import fuzzy_not as fuzzy_not
from sympy.core.relational import Eq as Eq
from sympy.functions.elementary.complexes import im as im
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.functions.special.delta_functions import Heaviside as Heaviside

class SingularityFunction(Function):
    """
    Singularity functions are a class of discontinuous functions.

    Explanation
    ===========

    Singularity functions take a variable, an offset, and an exponent as
    arguments. These functions are represented using Macaulay brackets as:

    SingularityFunction(x, a, n) := <x - a>^n

    The singularity function will automatically evaluate to
    ``Derivative(DiracDelta(x - a), x, -n - 1)`` if ``n < 0``
    and ``(x - a)**n*Heaviside(x - a)`` if ``n >= 0``.

    Examples
    ========

    >>> from sympy import SingularityFunction, diff, Piecewise, DiracDelta, Heaviside, Symbol
    >>> from sympy.abc import x, a, n
    >>> SingularityFunction(x, a, n)
    SingularityFunction(x, a, n)
    >>> y = Symbol('y', positive=True)
    >>> n = Symbol('n', nonnegative=True)
    >>> SingularityFunction(y, -10, n)
    (y + 10)**n
    >>> y = Symbol('y', negative=True)
    >>> SingularityFunction(y, 10, n)
    0
    >>> SingularityFunction(x, 4, -1).subs(x, 4)
    oo
    >>> SingularityFunction(x, 10, -2).subs(x, 10)
    oo
    >>> SingularityFunction(4, 1, 5)
    243
    >>> diff(SingularityFunction(x, 1, 5) + SingularityFunction(x, 1, 4), x)
    4*SingularityFunction(x, 1, 3) + 5*SingularityFunction(x, 1, 4)
    >>> diff(SingularityFunction(x, 4, 0), x, 2)
    SingularityFunction(x, 4, -2)
    >>> SingularityFunction(x, 4, 5).rewrite(Piecewise)
    Piecewise(((x - 4)**5, x > 4), (0, True))
    >>> expr = SingularityFunction(x, a, n)
    >>> y = Symbol('y', positive=True)
    >>> n = Symbol('n', nonnegative=True)
    >>> expr.subs({x: y, a: -10, n: n})
    (y + 10)**n

    The methods ``rewrite(DiracDelta)``, ``rewrite(Heaviside)``, and
    ``rewrite('HeavisideDiracDelta')`` returns the same output. One can use any
    of these methods according to their choice.

    >>> expr = SingularityFunction(x, 4, 5) + SingularityFunction(x, -3, -1) - SingularityFunction(x, 0, -2)
    >>> expr.rewrite(Heaviside)
    (x - 4)**5*Heaviside(x - 4) + DiracDelta(x + 3) - DiracDelta(x, 1)
    >>> expr.rewrite(DiracDelta)
    (x - 4)**5*Heaviside(x - 4) + DiracDelta(x + 3) - DiracDelta(x, 1)
    >>> expr.rewrite('HeavisideDiracDelta')
    (x - 4)**5*Heaviside(x - 4) + DiracDelta(x + 3) - DiracDelta(x, 1)

    See Also
    ========

    DiracDelta, Heaviside

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Singularity_function

    """
    is_real: bool
    def fdiff(self, argindex: int = 1):
        """
        Returns the first derivative of a DiracDelta Function.

        Explanation
        ===========

        The difference between ``diff()`` and ``fdiff()`` is: ``diff()`` is the
        user-level function and ``fdiff()`` is an object method. ``fdiff()`` is
        a convenience method available in the ``Function`` class. It returns
        the derivative of the function without considering the chain rule.
        ``diff(function, x)`` calls ``Function._eval_derivative`` which in turn
        calls ``fdiff()`` internally to compute the derivative of the function.

        """
    @classmethod
    def eval(cls, variable, offset, exponent):
        """
        Returns a simplified form or a value of Singularity Function depending
        on the argument passed by the object.

        Explanation
        ===========

        The ``eval()`` method is automatically called when the
        ``SingularityFunction`` class is about to be instantiated and it
        returns either some simplified instance or the unevaluated instance
        depending on the argument passed. In other words, ``eval()`` method is
        not needed to be called explicitly, it is being called and evaluated
        once the object is called.

        Examples
        ========

        >>> from sympy import SingularityFunction, Symbol, nan
        >>> from sympy.abc import x, a, n
        >>> SingularityFunction(x, a, n)
        SingularityFunction(x, a, n)
        >>> SingularityFunction(5, 3, 2)
        4
        >>> SingularityFunction(x, a, nan)
        nan
        >>> SingularityFunction(x, 3, 0).subs(x, 3)
        1
        >>> SingularityFunction(4, 1, 5)
        243
        >>> x = Symbol('x', positive = True)
        >>> a = Symbol('a', negative = True)
        >>> n = Symbol('n', nonnegative = True)
        >>> SingularityFunction(x, a, n)
        (-a + x)**n
        >>> x = Symbol('x', negative = True)
        >>> a = Symbol('a', positive = True)
        >>> SingularityFunction(x, a, n)
        0

        """
