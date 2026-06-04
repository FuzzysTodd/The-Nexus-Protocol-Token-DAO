from . import rl as rl
from .core import do_one as do_one, exhaust as exhaust, switch as switch
from .traverse import top_down as top_down

def subs(d, **kwargs):
    """ Full simultaneous exact substitution.

    Examples
    ========

    >>> from sympy.strategies.tools import subs
    >>> from sympy import Basic, S
    >>> mapping = {S(1): S(4), S(4): S(1), Basic(S(5)): Basic(S(6), S(7))}
    >>> expr = Basic(S(1), Basic(S(2), S(3)), Basic(S(4), Basic(S(5))))
    >>> subs(mapping)(expr)
    Basic(4, Basic(2, 3), Basic(1, Basic(6, 7)))
    """
def canon(*rules, **kwargs):
    """ Strategy for canonicalization.

    Explanation
    ===========

    Apply each rule in a bottom_up fashion through the tree.
    Do each one in turn.
    Keep doing this until there is no change.
    """
def typed(ruletypes):
    """ Apply rules based on the expression type

    inputs:
        ruletypes -- a dict mapping {Type: rule}

    Examples
    ========

    >>> from sympy.strategies import rm_id, typed
    >>> from sympy import Add, Mul
    >>> rm_zeros = rm_id(lambda x: x==0)
    >>> rm_ones  = rm_id(lambda x: x==1)
    >>> remove_idents = typed({Add: rm_zeros, Mul: rm_ones})
    """
