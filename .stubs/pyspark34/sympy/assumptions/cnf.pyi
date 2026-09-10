from _typeshed import Incomplete
from sympy.assumptions.assume import AppliedPredicate as AppliedPredicate, Predicate as Predicate
from sympy.core.relational import Eq as Eq, Ge as Ge, Gt as Gt, Le as Le, Lt as Lt, Ne as Ne
from sympy.core.singleton import S as S
from sympy.logic.boolalg import And as And, Equivalent as Equivalent, ITE as ITE, Implies as Implies, Nand as Nand, Nor as Nor, Not as Not, Or as Or, Xnor as Xnor, Xor as Xor

class Literal:
    """
    The smallest element of a CNF object.

    Parameters
    ==========

    lit : Boolean expression

    is_Not : bool

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.cnf import Literal
    >>> from sympy.abc import x
    >>> Literal(Q.even(x))
    Literal(Q.even(x), False)
    >>> Literal(~Q.even(x))
    Literal(Q.even(x), True)
    """
    def __new__(cls, lit, is_Not: bool = False): ...
    @property
    def arg(self): ...
    def rcall(self, expr): ...
    def __invert__(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class OR:
    """
    A low-level implementation for Or
    """
    def __init__(self, *args) -> None: ...
    @property
    def args(self): ...
    def rcall(self, expr): ...
    def __invert__(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...

class AND:
    """
    A low-level implementation for And
    """
    def __init__(self, *args) -> None: ...
    def __invert__(self): ...
    @property
    def args(self): ...
    def rcall(self, expr): ...
    def __hash__(self): ...
    def __eq__(self, other): ...

def to_NNF(expr, composite_map: Incomplete | None = None):
    """
    Generates the Negation Normal Form of any boolean expression in terms
    of AND, OR, and Literal objects.

    Examples
    ========

    >>> from sympy import Q, Eq
    >>> from sympy.assumptions.cnf import to_NNF
    >>> from sympy.abc import x, y
    >>> expr = Q.even(x) & ~Q.positive(x)
    >>> to_NNF(expr)
    (Literal(Q.even(x), False) & Literal(Q.positive(x), True))

    Supported boolean objects are converted to corresponding predicates.

    >>> to_NNF(Eq(x, y))
    Literal(Q.eq(x, y), False)

    If ``composite_map`` argument is given, ``to_NNF`` decomposes the
    specified predicate into a combination of primitive predicates.

    >>> cmap = {Q.nonpositive: Q.negative | Q.zero}
    >>> to_NNF(Q.nonpositive, cmap)
    (Literal(Q.negative, False) | Literal(Q.zero, False))
    >>> to_NNF(Q.nonpositive(x), cmap)
    (Literal(Q.negative(x), False) | Literal(Q.zero(x), False))
    """
def distribute_AND_over_OR(expr):
    """
    Distributes AND over OR in the NNF expression.
    Returns the result( Conjunctive Normal Form of expression)
    as a CNF object.
    """

class CNF:
    """
    Class to represent CNF of a Boolean expression.
    Consists of set of clauses, which themselves are stored as
    frozenset of Literal objects.

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.cnf import CNF
    >>> from sympy.abc import x
    >>> cnf = CNF.from_prop(Q.real(x) & ~Q.zero(x))
    >>> cnf.clauses
    {frozenset({Literal(Q.zero(x), True)}),
    frozenset({Literal(Q.negative(x), False),
    Literal(Q.positive(x), False), Literal(Q.zero(x), False)})}
    """
    clauses: Incomplete
    def __init__(self, clauses: Incomplete | None = None) -> None: ...
    def add(self, prop) -> None: ...
    def extend(self, props): ...
    def copy(self): ...
    def add_clauses(self, clauses) -> None: ...
    @classmethod
    def from_prop(cls, prop): ...
    def __iand__(self, other): ...
    def all_predicates(self): ...
    def rcall(self, expr): ...
    @classmethod
    def all_or(cls, *cnfs): ...
    @classmethod
    def all_and(cls, *cnfs): ...
    @classmethod
    def to_CNF(cls, expr): ...
    @classmethod
    def CNF_to_cnf(cls, cnf):
        """
        Converts CNF object to SymPy's boolean expression
        retaining the form of expression.
        """

class EncodedCNF:
    """
    Class for encoding the CNF expression.
    """
    data: Incomplete
    encoding: Incomplete
    def __init__(self, data: Incomplete | None = None, encoding: Incomplete | None = None) -> None: ...
    def from_cnf(self, cnf) -> None: ...
    @property
    def symbols(self): ...
    @property
    def variables(self): ...
    def copy(self): ...
    def add_prop(self, prop) -> None: ...
    def add_from_cnf(self, cnf) -> None: ...
    def encode_arg(self, arg): ...
    def encode(self, clause): ...
