from .basic import Basic as Basic
from .sorting import ordered as ordered
from .sympify import sympify as sympify
from _typeshed import Incomplete
from collections.abc import Generator
from sympy.utilities.iterables import iterable as iterable

def iterargs(expr) -> Generator[Incomplete, None, None]:
    """Yield the args of a Basic object in a breadth-first traversal.
    Depth-traversal stops if `arg.args` is either empty or is not
    an iterable.

    Examples
    ========

    >>> from sympy import Integral, Function
    >>> from sympy.abc import x
    >>> f = Function('f')
    >>> from sympy.core.traversal import iterargs
    >>> list(iterargs(Integral(f(x), (f(x), 1))))
    [Integral(f(x), (f(x), 1)), f(x), (f(x), 1), x, f(x), 1, x]

    See Also
    ========
    iterfreeargs, preorder_traversal
    """
def iterfreeargs(expr, _first: bool = True) -> Generator[Incomplete, None, None]:
    """Yield the args of a Basic object in a breadth-first traversal.
    Depth-traversal stops if `arg.args` is either empty or is not
    an iterable. The bound objects of an expression will be returned
    as canonical variables.

    Examples
    ========

    >>> from sympy import Integral, Function
    >>> from sympy.abc import x
    >>> f = Function('f')
    >>> from sympy.core.traversal import iterfreeargs
    >>> list(iterfreeargs(Integral(f(x), (f(x), 1))))
    [Integral(f(x), (f(x), 1)), 1]

    See Also
    ========
    iterargs, preorder_traversal
    """

class preorder_traversal:
    """
    Do a pre-order traversal of a tree.

    This iterator recursively yields nodes that it has visited in a pre-order
    fashion. That is, it yields the current node then descends through the
    tree breadth-first to yield all of a node's children's pre-order
    traversal.


    For an expression, the order of the traversal depends on the order of
    .args, which in many cases can be arbitrary.

    Parameters
    ==========
    node : SymPy expression
        The expression to traverse.
    keys : (default None) sort key(s)
        The key(s) used to sort args of Basic objects. When None, args of Basic
        objects are processed in arbitrary order. If key is defined, it will
        be passed along to ordered() as the only key(s) to use to sort the
        arguments; if ``key`` is simply True then the default keys of ordered
        will be used.

    Yields
    ======
    subtree : SymPy expression
        All of the subtrees in the tree.

    Examples
    ========

    >>> from sympy import preorder_traversal, symbols
    >>> x, y, z = symbols('x y z')

    The nodes are returned in the order that they are encountered unless key
    is given; simply passing key=True will guarantee that the traversal is
    unique.

    >>> list(preorder_traversal((x + y)*z, keys=None)) # doctest: +SKIP
    [z*(x + y), z, x + y, y, x]
    >>> list(preorder_traversal((x + y)*z, keys=True))
    [z*(x + y), z, x + y, x, y]

    """
    def __init__(self, node, keys: Incomplete | None = None) -> None: ...
    def skip(self) -> None:
        """
        Skip yielding current node's (last yielded node's) subtrees.

        Examples
        ========

        >>> from sympy import preorder_traversal, symbols
        >>> x, y, z = symbols('x y z')
        >>> pt = preorder_traversal((x + y*z)*z)
        >>> for i in pt:
        ...     print(i)
        ...     if i == x + y*z:
        ...             pt.skip()
        z*(x + y*z)
        z
        x + y*z
        """
    def __next__(self): ...
    def __iter__(self): ...

def use(expr, func, level: int = 0, args=(), kwargs={}):
    """
    Use ``func`` to transform ``expr`` at the given level.

    Examples
    ========

    >>> from sympy import use, expand
    >>> from sympy.abc import x, y

    >>> f = (x + y)**2*x + 1

    >>> use(f, expand, level=2)
    x*(x**2 + 2*x*y + y**2) + 1
    >>> expand(f)
    x**3 + 2*x**2*y + x*y**2 + 1

    """
def walk(e, *target) -> Generator[Incomplete, Incomplete, None]:
    """Iterate through the args that are the given types (target) and
    return a list of the args that were traversed; arguments
    that are not of the specified types are not traversed.

    Examples
    ========

    >>> from sympy.core.traversal import walk
    >>> from sympy import Min, Max
    >>> from sympy.abc import x, y, z
    >>> list(walk(Min(x, Max(y, Min(1, z))), Min))
    [Min(x, Max(y, Min(1, z)))]
    >>> list(walk(Min(x, Max(y, Min(1, z))), Min, Max))
    [Min(x, Max(y, Min(1, z))), Max(y, Min(1, z)), Min(1, z)]

    See Also
    ========

    bottom_up
    """
def bottom_up(rv, F, atoms: bool = False, nonbasic: bool = False):
    """Apply ``F`` to all expressions in an expression tree from the
    bottom up. If ``atoms`` is True, apply ``F`` even if there are no args;
    if ``nonbasic`` is True, try to apply ``F`` to non-Basic objects.
    """
def postorder_traversal(node, keys: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]:
    """
    Do a postorder traversal of a tree.

    This generator recursively yields nodes that it has visited in a postorder
    fashion. That is, it descends through the tree depth-first to yield all of
    a node's children's postorder traversal before yielding the node itself.

    Parameters
    ==========

    node : SymPy expression
        The expression to traverse.
    keys : (default None) sort key(s)
        The key(s) used to sort args of Basic objects. When None, args of Basic
        objects are processed in arbitrary order. If key is defined, it will
        be passed along to ordered() as the only key(s) to use to sort the
        arguments; if ``key`` is simply True then the default keys of
        ``ordered`` will be used (node count and default_sort_key).

    Yields
    ======
    subtree : SymPy expression
        All of the subtrees in the tree.

    Examples
    ========

    >>> from sympy import postorder_traversal
    >>> from sympy.abc import w, x, y, z

    The nodes are returned in the order that they are encountered unless key
    is given; simply passing key=True will guarantee that the traversal is
    unique.

    >>> list(postorder_traversal(w + (x + y)*z)) # doctest: +SKIP
    [z, y, x, x + y, z*(x + y), w, w + z*(x + y)]
    >>> list(postorder_traversal(w + (x + y)*z, keys=True))
    [w, z, x, y, x + y, z*(x + y), w + z*(x + y)]


    """
