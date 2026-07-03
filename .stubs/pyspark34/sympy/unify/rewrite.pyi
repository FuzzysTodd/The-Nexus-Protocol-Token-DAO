from _typeshed import Incomplete
from sympy.assumptions import ask as ask
from sympy.core.expr import Expr as Expr
from sympy.strategies.tools import subs as subs
from sympy.unify.usympy import rebuild as rebuild, unify as unify

def rewriterule(source, target, variables=(), condition: Incomplete | None = None, assume: Incomplete | None = None):
    """ Rewrite rule.

    Transform expressions that match source into expressions that match target
    treating all ``variables`` as wilds.

    Examples
    ========

    >>> from sympy.abc import w, x, y, z
    >>> from sympy.unify.rewrite import rewriterule
    >>> from sympy import default_sort_key
    >>> rl = rewriterule(x + y, x**y, [x, y])
    >>> sorted(rl(z + 3), key=default_sort_key)
    [3**z, z**3]

    Use ``condition`` to specify additional requirements.  Inputs are taken in
    the same order as is found in variables.

    >>> rl = rewriterule(x + y, x**y, [x, y], lambda x, y: x.is_integer)
    >>> list(rl(z + 3))
    [3**z]

    Use ``assume`` to specify additional requirements using new assumptions.

    >>> from sympy.assumptions import Q
    >>> rl = rewriterule(x + y, x**y, [x, y], assume=Q.integer(x))
    >>> list(rl(z + 3))
    [3**z]

    Assumptions for the local context are provided at rule runtime

    >>> list(rl(w + z, Q.integer(z)))
    [z**w]
    """
