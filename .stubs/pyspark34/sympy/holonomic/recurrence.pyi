from _typeshed import Incomplete
from sympy.core.singleton import S as S
from sympy.core.symbol import Symbol as Symbol, symbols as symbols
from sympy.core.sympify import sympify as sympify
from sympy.printing import sstr as sstr

def RecurrenceOperators(base, generator):
    """
    Returns an Algebra of Recurrence Operators and the operator for
    shifting i.e. the `Sn` operator.
    The first argument needs to be the base polynomial ring for the algebra
    and the second argument must be a generator which can be either a
    noncommutative Symbol or a string.

    Examples
    ========

    >>> from sympy import ZZ
    >>> from sympy import symbols
    >>> from sympy.holonomic.recurrence import RecurrenceOperators
    >>> n = symbols('n', integer=True)
    >>> R, Sn = RecurrenceOperators(ZZ.old_poly_ring(n), 'Sn')
    """

class RecurrenceOperatorAlgebra:
    """
    A Recurrence Operator Algebra is a set of noncommutative polynomials
    in intermediate `Sn` and coefficients in a base ring A. It follows the
    commutation rule:
    Sn * a(n) = a(n + 1) * Sn

    This class represents a Recurrence Operator Algebra and serves as the parent ring
    for Recurrence Operators.

    Examples
    ========

    >>> from sympy import ZZ
    >>> from sympy import symbols
    >>> from sympy.holonomic.recurrence import RecurrenceOperators
    >>> n = symbols('n', integer=True)
    >>> R, Sn = RecurrenceOperators(ZZ.old_poly_ring(n), 'Sn')
    >>> R
    Univariate Recurrence Operator Algebra in intermediate Sn over the base ring
    ZZ[n]

    See Also
    ========

    RecurrenceOperator
    """
    base: Incomplete
    shift_operator: Incomplete
    gen_symbol: Incomplete
    def __init__(self, base, generator) -> None: ...
    def __eq__(self, other): ...

class RecurrenceOperator:
    """
    The Recurrence Operators are defined by a list of polynomials
    in the base ring and the parent ring of the Operator.

    Explanation
    ===========

    Takes a list of polynomials for each power of Sn and the
    parent ring which must be an instance of RecurrenceOperatorAlgebra.

    A Recurrence Operator can be created easily using
    the operator `Sn`. See examples below.

    Examples
    ========

    >>> from sympy.holonomic.recurrence import RecurrenceOperator, RecurrenceOperators
    >>> from sympy import ZZ
    >>> from sympy import symbols
    >>> n = symbols('n', integer=True)
    >>> R, Sn = RecurrenceOperators(ZZ.old_poly_ring(n),'Sn')

    >>> RecurrenceOperator([0, 1, n**2], R)
    (1)Sn + (n**2)Sn**2

    >>> Sn*n
    (n + 1)Sn

    >>> n*Sn*n + 1 - Sn**2*n
    (1) + (n**2 + n)Sn + (-n - 2)Sn**2

    See Also
    ========

    DifferentialOperatorAlgebra
    """
    parent: Incomplete
    listofpoly: Incomplete
    order: Incomplete
    def __init__(self, list_of_poly, parent) -> None: ...
    def __mul__(self, other):
        """
        Multiplies two Operators and returns another
        RecurrenceOperator instance using the commutation rule
        Sn * a(n) = a(n + 1) * Sn
        """
    def __rmul__(self, other): ...
    def __add__(self, other): ...
    __radd__ = __add__
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __pow__(self, n): ...
    def __eq__(self, other): ...

class HolonomicSequence:
    """
    A Holonomic Sequence is a type of sequence satisfying a linear homogeneous
    recurrence relation with Polynomial coefficients. Alternatively, A sequence
    is Holonomic if and only if its generating function is a Holonomic Function.
    """
    recurrence: Incomplete
    u0: Incomplete
    n: Incomplete
    def __init__(self, recurrence, u0=[]) -> None: ...
    def __eq__(self, other): ...
