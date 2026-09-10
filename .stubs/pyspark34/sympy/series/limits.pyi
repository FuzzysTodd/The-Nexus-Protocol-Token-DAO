from .gruntz import gruntz as gruntz
from sympy.calculus.accumulationbounds import AccumBounds as AccumBounds
from sympy.core import Add as Add, Expr as Expr, Mul as Mul, PoleError as PoleError, S as S, Symbol as Symbol, sympify as sympify
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.numbers import Float as Float
from sympy.functions.combinatorial.factorials import factorial as factorial
from sympy.functions.elementary.complexes import Abs as Abs, arg as arg, re as re, sign as sign
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.special.gamma_functions import gamma as gamma
from sympy.polys import PolynomialError as PolynomialError, factor as factor
from sympy.series.order import Order as Order

def limit(e, z, z0, dir: str = '+'):
    '''Computes the limit of ``e(z)`` at the point ``z0``.

    Parameters
    ==========

    e : expression, the limit of which is to be taken

    z : symbol representing the variable in the limit.
        Other symbols are treated as constants. Multivariate limits
        are not supported.

    z0 : the value toward which ``z`` tends. Can be any expression,
        including ``oo`` and ``-oo``.

    dir : string, optional (default: "+")
        The limit is bi-directional if ``dir="+-"``, from the right
        (z->z0+) if ``dir="+"``, and from the left (z->z0-) if
        ``dir="-"``. For infinite ``z0`` (``oo`` or ``-oo``), the ``dir``
        argument is determined from the direction of the infinity
        (i.e., ``dir="-"`` for ``oo``).

    Examples
    ========

    >>> from sympy import limit, sin, oo
    >>> from sympy.abc import x
    >>> limit(sin(x)/x, x, 0)
    1
    >>> limit(1/x, x, 0) # default dir=\'+\'
    oo
    >>> limit(1/x, x, 0, dir="-")
    -oo
    >>> limit(1/x, x, 0, dir=\'+-\')
    zoo
    >>> limit(1/x, x, oo)
    0

    Notes
    =====

    First we try some heuristics for easy and frequent cases like "x", "1/x",
    "x**2" and similar, so that it\'s fast. For all other cases, we use the
    Gruntz algorithm (see the gruntz() function).

    See Also
    ========

     limit_seq : returns the limit of a sequence.
    '''
def heuristics(e, z, z0, dir):
    """Computes the limit of an expression term-wise.
    Parameters are the same as for the ``limit`` function.
    Works with the arguments of expression ``e`` one by one, computing
    the limit of each and then combining the results. This approach
    works only for simple limits, but it is fast.
    """

class Limit(Expr):
    '''Represents an unevaluated limit.

    Examples
    ========

    >>> from sympy import Limit, sin
    >>> from sympy.abc import x
    >>> Limit(sin(x)/x, x, 0)
    Limit(sin(x)/x, x, 0, dir=\'+\')
    >>> Limit(1/x, x, 0, dir="-")
    Limit(1/x, x, 0, dir=\'-\')

    '''
    def __new__(cls, e, z, z0, dir: str = '+'): ...
    @property
    def free_symbols(self): ...
    def pow_heuristics(self, e): ...
    def doit(self, **hints):
        """Evaluates the limit.

        Parameters
        ==========

        deep : bool, optional (default: True)
            Invoke the ``doit`` method of the expressions involved before
            taking the limit.

        hints : optional keyword arguments
            To be passed to ``doit`` methods; only used if deep is True.
        """
