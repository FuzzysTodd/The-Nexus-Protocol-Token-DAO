from _typeshed import Incomplete
from collections.abc import Generator
from sympy.utilities.iterables import kbins as kbins

class Compound:
    """ A little class to represent an interior node in the tree

    This is analogous to SymPy.Basic for non-Atoms
    """
    op: Incomplete
    args: Incomplete
    def __init__(self, op, args) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class Variable:
    """ A Wild token """
    arg: Incomplete
    def __init__(self, arg) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class CondVariable:
    """ A wild token that matches conditionally.

    arg   - a wild token.
    valid - an additional constraining function on a match.
    """
    arg: Incomplete
    valid: Incomplete
    def __init__(self, arg, valid) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...

def unify(x, y, s: Incomplete | None = None, **fns) -> Generator[Incomplete, Incomplete, Incomplete]:
    ''' Unify two expressions.

    Parameters
    ==========

        x, y - expression trees containing leaves, Compounds and Variables.
        s    - a mapping of variables to subtrees.

    Returns
    =======

        lazy sequence of mappings {Variable: subtree}

    Examples
    ========

    >>> from sympy.unify.core import unify, Compound, Variable
    >>> expr    = Compound("Add", ("x", "y"))
    >>> pattern = Compound("Add", ("x", Variable("a")))
    >>> next(unify(expr, pattern, {}))
    {Variable(a): \'y\'}
    '''
def unify_var(var, x, s, **fns) -> Generator[Incomplete, Incomplete, None]: ...
def occur_check(var, x):
    """ var occurs in subtree owned by x? """
def assoc(d, key, val):
    """ Return copy of d with key associated to val """
def is_args(x):
    """ Is x a traditional iterable? """
def unpack(x): ...
def allcombinations(A, B, ordered) -> Generator[Incomplete, None, None]:
    """
    Restructure A and B to have the same number of elements.

    Parameters
    ==========

    ordered must be either 'commutative' or 'associative'.

    A and B can be rearranged so that the larger of the two lists is
    reorganized into smaller sublists.

    Examples
    ========

    >>> from sympy.unify.core import allcombinations
    >>> for x in allcombinations((1, 2, 3), (5, 6), 'associative'): print(x)
    (((1,), (2, 3)), ((5,), (6,)))
    (((1, 2), (3,)), ((5,), (6,)))

    >>> for x in allcombinations((1, 2, 3), (5, 6), 'commutative'): print(x)
        (((1,), (2, 3)), ((5,), (6,)))
        (((1, 2), (3,)), ((5,), (6,)))
        (((1,), (3, 2)), ((5,), (6,)))
        (((1, 3), (2,)), ((5,), (6,)))
        (((2,), (1, 3)), ((5,), (6,)))
        (((2, 1), (3,)), ((5,), (6,)))
        (((2,), (3, 1)), ((5,), (6,)))
        (((2, 3), (1,)), ((5,), (6,)))
        (((3,), (1, 2)), ((5,), (6,)))
        (((3, 1), (2,)), ((5,), (6,)))
        (((3,), (2, 1)), ((5,), (6,)))
        (((3, 2), (1,)), ((5,), (6,)))
    """
def partition(it, part):
    """ Partition a tuple/list into pieces defined by indices.

    Examples
    ========

    >>> from sympy.unify.core import partition
    >>> partition((10, 20, 30, 40), [[0, 1, 2], [3]])
    ((10, 20, 30), (40,))
    """
def index(it, ind):
    """ Fancy indexing into an indexable iterable (tuple, list).

    Examples
    ========

    >>> from sympy.unify.core import index
    >>> index([10, 20, 30], (1, 2, 0))
    [20, 30, 10]
    """
