from _typeshed import Incomplete

__all__ = ['Term', 'ModelDesc', 'INTERCEPT']

class Term:
    '''The interaction between a collection of factor objects.

    This is one of the basic types used in representing formulas, and
    corresponds to an expression like ``"a:b:c"`` in a formula string.
    For details, see :ref:`formulas` and :ref:`expert-model-specification`.

    Terms are hashable and compare by value.

    Attributes:
    
    .. attribute:: factors

       A tuple of factor objects.
    '''
    factors: Incomplete
    def __init__(self, factors) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    def name(self):
        """Return a human-readable name for this term."""

INTERCEPT: Incomplete

class _MockFactor:
    def __init__(self, name) -> None: ...
    def name(self): ...

class ModelDesc:
    """A simple container representing the termlists parsed from a formula.

    This is a simple container object which has exactly the same
    representational power as a formula string, but is a Python object
    instead. You can construct one by hand, and pass it to functions like
    :func:`dmatrix` or :func:`incr_dbuilder` that are expecting a formula
    string, but without having to do any messy string manipulation. For
    details see :ref:`expert-model-specification`.

    Attributes:

    .. attribute:: lhs_termlist
                   rhs_termlist

       Two termlists representing the left- and right-hand sides of a
       formula, suitable for passing to :func:`design_matrix_builders`.
    """
    lhs_termlist: Incomplete
    rhs_termlist: Incomplete
    def __init__(self, lhs_termlist, rhs_termlist) -> None: ...
    def describe(self):
        """Returns a human-readable representation of this :class:`ModelDesc`
        in pseudo-formula notation.

        .. warning:: There is no guarantee that the strings returned by this
           function can be parsed as formulas. They are best-effort
           descriptions intended for human users. However, if this ModelDesc
           was created by parsing a formula, then it should work in
           practice. If you *really* have to.
        """
    @classmethod
    def from_formula(cls, tree_or_string):
        """Construct a :class:`ModelDesc` from a formula string.

        :arg tree_or_string: A formula string. (Or an unevaluated formula
          parse tree, but the API for generating those isn't public yet. Shh,
          it can be our secret.)
        :returns: A new :class:`ModelDesc`.
        """

class IntermediateExpr:
    """This class holds an intermediate result while we're evaluating a tree."""
    intercept: Incomplete
    intercept_origin: Incomplete
    intercept_removed: Incomplete
    terms: Incomplete
    def __init__(self, intercept, intercept_origin, intercept_removed, terms) -> None: ...

class Evaluator:
    stash: Incomplete
    def __init__(self) -> None: ...
    def add_op(self, op, arity, evaluator) -> None: ...
    def eval(self, tree, require_evalexpr: bool = True): ...
