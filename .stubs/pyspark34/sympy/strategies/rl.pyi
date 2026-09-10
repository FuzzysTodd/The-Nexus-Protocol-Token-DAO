from .util import new as new
from sympy.utilities.iterables import sift as sift

def rm_id(isid, new=...):
    """ Create a rule to remove identities.

    isid - fn :: x -> Bool  --- whether or not this element is an identity.

    Examples
    ========

    >>> from sympy.strategies import rm_id
    >>> from sympy import Basic, S
    >>> remove_zeros = rm_id(lambda x: x==0)
    >>> remove_zeros(Basic(S(1), S(0), S(2)))
    Basic(1, 2)
    >>> remove_zeros(Basic(S(0), S(0))) # If only identites then we keep one
    Basic(0)

    See Also:
        unpack
    """
def glom(key, count, combine):
    """ Create a rule to conglomerate identical args.

    Examples
    ========

    >>> from sympy.strategies import glom
    >>> from sympy import Add
    >>> from sympy.abc import x

    >>> key     = lambda x: x.as_coeff_Mul()[1]
    >>> count   = lambda x: x.as_coeff_Mul()[0]
    >>> combine = lambda cnt, arg: cnt * arg
    >>> rl = glom(key, count, combine)

    >>> rl(Add(x, -x, 3*x, 2, 3, evaluate=False))
    3*x + 5

    Wait, how are key, count and combine supposed to work?

    >>> key(2*x)
    x
    >>> count(2*x)
    2
    >>> combine(2, x)
    2*x
    """
def sort(key, new=...):
    """ Create a rule to sort by a key function.

    Examples
    ========

    >>> from sympy.strategies import sort
    >>> from sympy import Basic, S
    >>> sort_rl = sort(str)
    >>> sort_rl(Basic(S(3), S(1), S(2)))
    Basic(1, 2, 3)
    """
def distribute(A, B):
    """ Turns an A containing Bs into a B of As

    where A, B are container types

    >>> from sympy.strategies import distribute
    >>> from sympy import Add, Mul, symbols
    >>> x, y = symbols('x,y')
    >>> dist = distribute(Mul, Add)
    >>> expr = Mul(2, x+y, evaluate=False)
    >>> expr
    2*(x + y)
    >>> dist(expr)
    2*x + 2*y
    """
def subs(a, b):
    """ Replace expressions exactly """
def unpack(expr):
    """ Rule to unpack singleton args

    >>> from sympy.strategies import unpack
    >>> from sympy import Basic, S
    >>> unpack(Basic(S(2)))
    2
    """
def flatten(expr, new=...):
    """ Flatten T(a, b, T(c, d), T2(e)) to T(a, b, c, d, T2(e)) """
def rebuild(expr):
    """ Rebuild a SymPy tree.

    Explanation
    ===========

    This function recursively calls constructors in the expression tree.
    This forces canonicalization and removes ugliness introduced by the use of
    Basic.__new__
    """
