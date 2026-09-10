from sympy.assumptions import AppliedPredicate, Predicate

__all__ = ['BinaryRelation', 'AppliedBinaryRelation']

class BinaryRelation(Predicate):
    '''
    Base class for all binary relational predicates.

    Explanation
    ===========

    Binary relation takes two arguments and returns ``AppliedBinaryRelation``
    instance. To evaluate it to boolean value, use :obj:`~.ask()` or
    :obj:`~.refine()` function.

    You can add support for new types by registering the handler to dispatcher.
    See :obj:`~.Predicate()` for more information about predicate dispatching.

    Examples
    ========

    Applying and evaluating to boolean value:

    >>> from sympy import Q, ask, sin, cos
    >>> from sympy.abc import x
    >>> Q.eq(sin(x)**2+cos(x)**2, 1)
    Q.eq(sin(x)**2 + cos(x)**2, 1)
    >>> ask(_)
    True

    You can define a new binary relation by subclassing and dispatching.
    Here, we define a relation $R$ such that $x R y$ returns true if
    $x = y + 1$.

    >>> from sympy import ask, Number, Q
    >>> from sympy.assumptions import BinaryRelation
    >>> class MyRel(BinaryRelation):
    ...     name = "R"
    ...     is_reflexive = False
    >>> Q.R = MyRel()
    >>> @Q.R.register(Number, Number)
    ... def _(n1, n2, assumptions):
    ...     return ask(Q.zero(n1 - n2 - 1), assumptions)
    >>> Q.R(2, 1)
    Q.R(2, 1)

    Now, we can use ``ask()`` to evaluate it to boolean value.

    >>> ask(Q.R(2, 1))
    True
    >>> ask(Q.R(1, 2))
    False

    ``Q.R`` returns ``False`` with minimum cost if two arguments have same
    structure because it is antireflexive relation [1] by
    ``is_reflexive = False``.

    >>> ask(Q.R(x, x))
    False

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Reflexive_relation
    '''
    is_reflexive: bool | None
    is_symmetric: bool | None
    def __call__(self, *args): ...
    @property
    def reversed(self): ...
    @property
    def negated(self) -> None: ...
    def eval(self, args, assumptions: bool = True): ...

class AppliedBinaryRelation(AppliedPredicate):
    """
    The class of expressions resulting from applying ``BinaryRelation``
    to the arguments.

    """
    @property
    def lhs(self):
        """The left-hand side of the relation."""
    @property
    def rhs(self):
        """The right-hand side of the relation."""
    @property
    def reversed(self):
        """
        Try to return the relationship with sides reversed.
        """
    @property
    def reversedsign(self):
        """
        Try to return the relationship with signs reversed.
        """
    @property
    def negated(self): ...
    def __bool__(self) -> bool: ...
