from _typeshed import Incomplete
from sympy.assumptions import AppliedPredicate as AppliedPredicate, Predicate as Predicate, Q as Q
from sympy.core.relational import Eq as Eq, Ge as Ge, Gt as Gt, Le as Le, Lt as Lt, Ne as Ne
from sympy.multipledispatch import Dispatcher as Dispatcher

class CommutativePredicate(Predicate):
    """
    Commutative predicate.

    Explanation
    ===========

    ``ask(Q.commutative(x))`` is true iff ``x`` commutes with any other
    object with respect to multiplication operation.

    """
    name: str
    handler: Incomplete

binrelpreds: Incomplete

class IsTruePredicate(Predicate):
    """
    Generic predicate.

    Explanation
    ===========

    ``ask(Q.is_true(x))`` is true iff ``x`` is true. This only makes
    sense if ``x`` is a boolean object.

    Examples
    ========

    >>> from sympy import ask, Q
    >>> from sympy.abc import x, y
    >>> ask(Q.is_true(True))
    True

    Wrapping another applied predicate just returns the applied predicate.

    >>> Q.is_true(Q.even(x))
    Q.even(x)

    Wrapping binary relation classes in SymPy core returns applied binary
    relational predicates.

    >>> from sympy import Eq, Gt
    >>> Q.is_true(Eq(x, y))
    Q.eq(x, y)
    >>> Q.is_true(Gt(x, y))
    Q.gt(x, y)

    Notes
    =====

    This class is designed to wrap the boolean objects so that they can
    behave as if they are applied predicates. Consequently, wrapping another
    applied predicate is unnecessary and thus it just returns the argument.
    Also, binary relation classes in SymPy core have binary predicates to
    represent themselves and thus wrapping them with ``Q.is_true`` converts them
    to these applied predicates.

    """
    name: str
    handler: Incomplete
    def __call__(self, arg): ...
