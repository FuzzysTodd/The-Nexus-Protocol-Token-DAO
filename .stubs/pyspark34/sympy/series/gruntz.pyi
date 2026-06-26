from _typeshed import Incomplete
from sympy.core import Basic as Basic, Mul as Mul, PoleError as PoleError, S as S, expand_mul as expand_mul
from sympy.core.cache import cacheit as cacheit
from sympy.core.numbers import I as I, ilcm as ilcm, oo as oo
from sympy.core.symbol import Dummy as Dummy, Wild as Wild
from sympy.core.traversal import bottom_up as bottom_up
from sympy.functions import exp as exp, log as log
from sympy.series.order import Order as Order
from sympy.utilities.exceptions import SymPyDeprecationWarning as SymPyDeprecationWarning
from sympy.utilities.timeutils import timethis as timethis

timeit: Incomplete

def compare(a, b, x):
    '''Returns "<" if a<b, "=" for a == b, ">" for a>b'''

class SubsSet(dict):
    """
    Stores (expr, dummy) pairs, and how to rewrite expr-s.

    Explanation
    ===========

    The gruntz algorithm needs to rewrite certain expressions in term of a new
    variable w. We cannot use subs, because it is just too smart for us. For
    example::

        > Omega=[exp(exp(_p - exp(-_p))/(1 - 1/_p)), exp(exp(_p))]
        > O2=[exp(-exp(_p) + exp(-exp(-_p))*exp(_p)/(1 - 1/_p))/_w, 1/_w]
        > e = exp(exp(_p - exp(-_p))/(1 - 1/_p)) - exp(exp(_p))
        > e.subs(Omega[0],O2[0]).subs(Omega[1],O2[1])
        -1/w + exp(exp(p)*exp(-exp(-p))/(1 - 1/p))

    is really not what we want!

    So we do it the hard way and keep track of all the things we potentially
    want to substitute by dummy variables. Consider the expression::

        exp(x - exp(-x)) + exp(x) + x.

    The mrv set is {exp(x), exp(-x), exp(x - exp(-x))}.
    We introduce corresponding dummy variables d1, d2, d3 and rewrite::

        d3 + d1 + x.

    This class first of all keeps track of the mapping expr->variable, i.e.
    will at this stage be a dictionary::

        {exp(x): d1, exp(-x): d2, exp(x - exp(-x)): d3}.

    [It turns out to be more convenient this way round.]
    But sometimes expressions in the mrv set have other expressions from the
    mrv set as subexpressions, and we need to keep track of that as well. In
    this case, d3 is really exp(x - d2), so rewrites at this stage is::

        {d3: exp(x-d2)}.

    The function rewrite uses all this information to correctly rewrite our
    expression in terms of w. In this case w can be chosen to be exp(-x),
    i.e. d2. The correct rewriting then is::

        exp(-w)/w + 1/w + x.
    """
    rewrites: Incomplete
    def __init__(self) -> None: ...
    def __getitem__(self, key): ...
    def do_subs(self, e):
        """Substitute the variables with expressions"""
    def meets(self, s2):
        """Tell whether or not self and s2 have non-empty intersection"""
    def union(self, s2, exps: Incomplete | None = None):
        """Compute the union of self and s2, adjusting exps"""
    def copy(self):
        """Create a shallow copy of SubsSet"""

def mrv(e, x):
    """Returns a SubsSet of most rapidly varying (mrv) subexpressions of 'e',
       and e rewritten in terms of these"""
def mrv_max3(f, expsf, g, expsg, union, expsboth, x):
    """
    Computes the maximum of two sets of expressions f and g, which
    are in the same comparability class, i.e. max() compares (two elements of)
    f and g and returns either (f, expsf) [if f is larger], (g, expsg)
    [if g is larger] or (union, expsboth) [if f, g are of the same class].
    """
def mrv_max1(f, g, exps, x):
    """Computes the maximum of two sets of expressions f and g, which
    are in the same comparability class, i.e. mrv_max1() compares (two elements of)
    f and g and returns the set, which is in the higher comparability class
    of the union of both, if they have the same order of variation.
    Also returns exps, with the appropriate substitutions made.
    """
def sign(e, x):
    """
    Returns a sign of an expression e(x) for x->oo.

    ::

        e >  0 for x sufficiently large ...  1
        e == 0 for x sufficiently large ...  0
        e <  0 for x sufficiently large ... -1

    The result of this function is currently undefined if e changes sign
    arbitrarily often for arbitrarily large x (e.g. sin(x)).

    Note that this returns zero only if e is *constantly* zero
    for x sufficiently large. [If e is constant, of course, this is just
    the same thing as the sign of e.]
    """
def limitinf(e, x):
    """Limit e(x) for x-> oo."""
def moveup2(s, x): ...
def moveup(l, x): ...
def calculate_series(e, x, logx: Incomplete | None = None):
    """ Calculates at least one term of the series of ``e`` in ``x``.

    This is a place that fails most often, so it is in its own function.
    """
def mrv_leadterm(e, x):
    """Returns (c0, e0) for e."""
def build_expression_tree(Omega, rewrites):
    """ Helper function for rewrite.

    We need to sort Omega (mrv set) so that we replace an expression before
    we replace any expression in terms of which it has to be rewritten::

        e1 ---> e2 ---> e3
                 \\\n                  -> e4

    Here we can do e1, e2, e3, e4 or e1, e2, e4, e3.
    To do this we assemble the nodes into a tree, and sort them by height.

    This function builds the tree, rewrites then sorts the nodes.
    """
def rewrite(e, Omega, x, wsym):
    """e(x) ... the function
    Omega ... the mrv set
    wsym ... the symbol which is going to be used for w

    Returns the rewritten e in terms of w and log(w). See test_rewrite1()
    for examples and correct results.
    """
def gruntz(e, z, z0, dir: str = '+'):
    '''
    Compute the limit of e(z) at the point z0 using the Gruntz algorithm.

    Explanation
    ===========

    ``z0`` can be any expression, including oo and -oo.

    For ``dir="+"`` (default) it calculates the limit from the right
    (z->z0+) and for ``dir="-"`` the limit from the left (z->z0-). For infinite z0
    (oo or -oo), the dir argument does not matter.

    This algorithm is fully described in the module docstring in the gruntz.py
    file. It relies heavily on the series expansion. Most frequently, gruntz()
    is only used if the faster limit() function (which uses heuristics) fails.
    '''
