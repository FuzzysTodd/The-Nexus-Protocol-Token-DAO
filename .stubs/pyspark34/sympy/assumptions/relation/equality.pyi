from .binrel import BinaryRelation
from _typeshed import Incomplete

__all__ = ['EqualityPredicate', 'UnequalityPredicate', 'StrictGreaterThanPredicate', 'GreaterThanPredicate', 'StrictLessThanPredicate', 'LessThanPredicate']

class EqualityPredicate(BinaryRelation):
    """
    Binary predicate for $=$.

    The purpose of this class is to provide the instance which represent
    the equality predicate in order to allow the logical inference.
    This class must remain internal to assumptions module and user must
    use :obj:`~.Eq()` instead to construct the equality expression.

    Evaluating this predicate to ``True`` or ``False`` is done by
    :func:`~.core.relational.is_eq()`

    Examples
    ========

    >>> from sympy import ask, Q
    >>> Q.eq(0, 0)
    Q.eq(0, 0)
    >>> ask(_)
    True

    See Also
    ========

    sympy.core.relational.Eq

    """
    is_reflexive: bool
    is_symmetric: bool
    name: str
    handler: Incomplete
    @property
    def negated(self): ...
    def eval(self, args, assumptions: bool = True): ...

class UnequalityPredicate(BinaryRelation):
    """
    Binary predicate for $\\neq$.

    The purpose of this class is to provide the instance which represent
    the inequation predicate in order to allow the logical inference.
    This class must remain internal to assumptions module and user must
    use :obj:`~.Ne()` instead to construct the inequation expression.

    Evaluating this predicate to ``True`` or ``False`` is done by
    :func:`~.core.relational.is_neq()`

    Examples
    ========

    >>> from sympy import ask, Q
    >>> Q.ne(0, 0)
    Q.ne(0, 0)
    >>> ask(_)
    False

    See Also
    ========

    sympy.core.relational.Ne

    """
    is_reflexive: bool
    is_symmetric: bool
    name: str
    handler: Incomplete
    @property
    def negated(self): ...
    def eval(self, args, assumptions: bool = True): ...

class StrictGreaterThanPredicate(BinaryRelation):
    '''
    Binary predicate for $>$.

    The purpose of this class is to provide the instance which represent
    the ">" predicate in order to allow the logical inference.
    This class must remain internal to assumptions module and user must
    use :obj:`~.Gt()` instead to construct the equality expression.

    Evaluating this predicate to ``True`` or ``False`` is done by
    :func:`~.core.relational.is_gt()`

    Examples
    ========

    >>> from sympy import ask, Q
    >>> Q.gt(0, 0)
    Q.gt(0, 0)
    >>> ask(_)
    False

    See Also
    ========

    sympy.core.relational.Gt

    '''
    is_reflexive: bool
    is_symmetric: bool
    name: str
    handler: Incomplete
    @property
    def reversed(self): ...
    @property
    def negated(self): ...
    def eval(self, args, assumptions: bool = True): ...

class GreaterThanPredicate(BinaryRelation):
    '''
    Binary predicate for $>=$.

    The purpose of this class is to provide the instance which represent
    the ">=" predicate in order to allow the logical inference.
    This class must remain internal to assumptions module and user must
    use :obj:`~.Ge()` instead to construct the equality expression.

    Evaluating this predicate to ``True`` or ``False`` is done by
    :func:`~.core.relational.is_ge()`

    Examples
    ========

    >>> from sympy import ask, Q
    >>> Q.ge(0, 0)
    Q.ge(0, 0)
    >>> ask(_)
    True

    See Also
    ========

    sympy.core.relational.Ge

    '''
    is_reflexive: bool
    is_symmetric: bool
    name: str
    handler: Incomplete
    @property
    def reversed(self): ...
    @property
    def negated(self): ...
    def eval(self, args, assumptions: bool = True): ...

class StrictLessThanPredicate(BinaryRelation):
    '''
    Binary predicate for $<$.

    The purpose of this class is to provide the instance which represent
    the "<" predicate in order to allow the logical inference.
    This class must remain internal to assumptions module and user must
    use :obj:`~.Lt()` instead to construct the equality expression.

    Evaluating this predicate to ``True`` or ``False`` is done by
    :func:`~.core.relational.is_lt()`

    Examples
    ========

    >>> from sympy import ask, Q
    >>> Q.lt(0, 0)
    Q.lt(0, 0)
    >>> ask(_)
    False

    See Also
    ========

    sympy.core.relational.Lt

    '''
    is_reflexive: bool
    is_symmetric: bool
    name: str
    handler: Incomplete
    @property
    def reversed(self): ...
    @property
    def negated(self): ...
    def eval(self, args, assumptions: bool = True): ...

class LessThanPredicate(BinaryRelation):
    '''
    Binary predicate for $<=$.

    The purpose of this class is to provide the instance which represent
    the "<=" predicate in order to allow the logical inference.
    This class must remain internal to assumptions module and user must
    use :obj:`~.Le()` instead to construct the equality expression.

    Evaluating this predicate to ``True`` or ``False`` is done by
    :func:`~.core.relational.is_le()`

    Examples
    ========

    >>> from sympy import ask, Q
    >>> Q.le(0, 0)
    Q.le(0, 0)
    >>> ask(_)
    True

    See Also
    ========

    sympy.core.relational.Le

    '''
    is_reflexive: bool
    is_symmetric: bool
    name: str
    handler: Incomplete
    @property
    def reversed(self): ...
    @property
    def negated(self): ...
    def eval(self, args, assumptions: bool = True): ...
