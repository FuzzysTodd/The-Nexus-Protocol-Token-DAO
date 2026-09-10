from _typeshed import Incomplete
from collections.abc import Generator
from sympy.core import Add as Add, Basic as Basic, Mul as Mul, Pow as Pow
from sympy.core.operations import AssocOp as AssocOp, LatticeOp as LatticeOp
from sympy.matrices import MatAdd as MatAdd, MatMul as MatMul, MatrixExpr as MatrixExpr
from sympy.sets.sets import FiniteSet as FiniteSet, Intersection as Intersection, Union as Union
from sympy.unify import core as core
from sympy.unify.core import Compound as Compound, CondVariable as CondVariable, Variable as Variable

basic_new_legal: Incomplete
eval_false_legal: Incomplete
illegal: Incomplete

def sympy_associative(op): ...
def sympy_commutative(op): ...
def is_associative(x): ...
def is_commutative(x): ...
def mk_matchtype(typ): ...
def deconstruct(s, variables=()):
    """ Turn a SymPy object into a Compound """
def construct(t):
    """ Turn a Compound into a SymPy object """
def rebuild(s):
    """ Rebuild a SymPy expression.

    This removes harm caused by Expr-Rules interactions.
    """
def unify(x, y, s: Incomplete | None = None, variables=(), **kwargs) -> Generator[Incomplete, None, Incomplete]:
    """ Structural unification of two expressions/patterns.

    Examples
    ========

    >>> from sympy.unify.usympy import unify
    >>> from sympy import Basic, S
    >>> from sympy.abc import x, y, z, p, q

    >>> next(unify(Basic(S(1), S(2)), Basic(S(1), x), variables=[x]))
    {x: 2}

    >>> expr = 2*x + y + z
    >>> pattern = 2*p + q
    >>> next(unify(expr, pattern, {}, variables=(p, q)))
    {p: x, q: y + z}

    Unification supports commutative and associative matching

    >>> expr = x + y + z
    >>> pattern = p + q
    >>> len(list(unify(expr, pattern, {}, variables=(p, q))))
    12

    Symbols not indicated to be variables are treated as literal,
    else they are wild-like and match anything in a sub-expression.

    >>> expr = x*y*z + 3
    >>> pattern = x*y + 3
    >>> next(unify(expr, pattern, {}, variables=[x, y]))
    {x: y, y: x*z}

    The x and y of the pattern above were in a Mul and matched factors
    in the Mul of expr. Here, a single symbol matches an entire term:

    >>> expr = x*y + 3
    >>> pattern = p + 3
    >>> next(unify(expr, pattern, {}, variables=[p]))
    {p: x*y}

    """
