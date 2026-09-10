from sympy.core import Mul as Mul
from sympy.core.function import count_ops as count_ops
from sympy.core.traversal import bottom_up as bottom_up, preorder_traversal as preorder_traversal
from sympy.functions import gamma as gamma
from sympy.functions.combinatorial.factorials import binomial as binomial, factorial as factorial
from sympy.simplify.gammasimp import gammasimp as gammasimp
from sympy.utilities.timeutils import timethis as timethis

def combsimp(expr):
    '''
    Simplify combinatorial expressions.

    Explanation
    ===========

    This function takes as input an expression containing factorials,
    binomials, Pochhammer symbol and other "combinatorial" functions,
    and tries to minimize the number of those functions and reduce
    the size of their arguments.

    The algorithm works by rewriting all combinatorial functions as
    gamma functions and applying gammasimp() except simplification
    steps that may make an integer argument non-integer. See docstring
    of gammasimp for more information.

    Then it rewrites expression in terms of factorials and binomials by
    rewriting gammas as factorials and converting (a+b)!/a!b! into
    binomials.

    If expression has gamma functions or combinatorial functions
    with non-integer argument, it is automatically passed to gammasimp.

    Examples
    ========

    >>> from sympy.simplify import combsimp
    >>> from sympy import factorial, binomial, symbols
    >>> n, k = symbols(\'n k\', integer = True)

    >>> combsimp(factorial(n)/factorial(n - 3))
    n*(n - 2)*(n - 1)
    >>> combsimp(binomial(n+1, k+1)/binomial(n, k))
    (n + 1)/(k + 1)

    '''
