from sympy.core.function import Function as Function
from sympy.functions import Piecewise as Piecewise, exp as exp
from sympy.tensor.indexed import Idx as Idx, Indexed as Indexed
from sympy.utilities import sift as sift

class IndexConformanceException(Exception): ...

def get_indices(expr):
    """Determine the outer indices of expression ``expr``

    By *outer* we mean indices that are not summation indices.  Returns a set
    and a dict.  The set contains outer indices and the dict contains
    information about index symmetries.

    Examples
    ========

    >>> from sympy.tensor.index_methods import get_indices
    >>> from sympy import symbols
    >>> from sympy.tensor import IndexedBase
    >>> x, y, A = map(IndexedBase, ['x', 'y', 'A'])
    >>> i, j, a, z = symbols('i j a z', integer=True)

    The indices of the total expression is determined, Repeated indices imply a
    summation, for instance the trace of a matrix A:

    >>> get_indices(A[i, i])
    (set(), {})

    In the case of many terms, the terms are required to have identical
    outer indices.  Else an IndexConformanceException is raised.

    >>> get_indices(x[i] + A[i, j]*y[j])
    ({i}, {})

    :Exceptions:

    An IndexConformanceException means that the terms ar not compatible, e.g.

    >>> get_indices(x[i] + y[j])                #doctest: +SKIP
            (...)
    IndexConformanceException: Indices are not consistent: x(i) + y(j)

    .. warning::
       The concept of *outer* indices applies recursively, starting on the deepest
       level.  This implies that dummies inside parenthesis are assumed to be
       summed first, so that the following expression is handled gracefully:

       >>> get_indices((x[i] + A[i, j]*y[j])*x[j])
       ({i, j}, {})

       This is correct and may appear convenient, but you need to be careful
       with this as SymPy will happily .expand() the product, if requested.  The
       resulting expression would mix the outer ``j`` with the dummies inside
       the parenthesis, which makes it a different expression.  To be on the
       safe side, it is best to avoid such ambiguities by using unique indices
       for all contractions that should be held separate.

    """
def get_contraction_structure(expr):
    '''Determine dummy indices of ``expr`` and describe its structure

    By *dummy* we mean indices that are summation indices.

    The structure of the expression is determined and described as follows:

    1) A conforming summation of Indexed objects is described with a dict where
       the keys are summation indices and the corresponding values are sets
       containing all terms for which the summation applies.  All Add objects
       in the SymPy expression tree are described like this.

    2) For all nodes in the SymPy expression tree that are *not* of type Add, the
       following applies:

       If a node discovers contractions in one of its arguments, the node
       itself will be stored as a key in the dict.  For that key, the
       corresponding value is a list of dicts, each of which is the result of a
       recursive call to get_contraction_structure().  The list contains only
       dicts for the non-trivial deeper contractions, omitting dicts with None
       as the one and only key.

    .. Note:: The presence of expressions among the dictionary keys indicates
       multiple levels of index contractions.  A nested dict displays nested
       contractions and may itself contain dicts from a deeper level.  In
       practical calculations the summation in the deepest nested level must be
       calculated first so that the outer expression can access the resulting
       indexed object.

    Examples
    ========

    >>> from sympy.tensor.index_methods import get_contraction_structure
    >>> from sympy import default_sort_key
    >>> from sympy.tensor import IndexedBase, Idx
    >>> x, y, A = map(IndexedBase, [\'x\', \'y\', \'A\'])
    >>> i, j, k, l = map(Idx, [\'i\', \'j\', \'k\', \'l\'])
    >>> get_contraction_structure(x[i]*y[i] + A[j, j])
    {(i,): {x[i]*y[i]}, (j,): {A[j, j]}}
    >>> get_contraction_structure(x[i]*y[j])
    {None: {x[i]*y[j]}}

    A multiplication of contracted factors results in nested dicts representing
    the internal contractions.

    >>> d = get_contraction_structure(x[i, i]*y[j, j])
    >>> sorted(d.keys(), key=default_sort_key)
    [None, x[i, i]*y[j, j]]

    In this case, the product has no contractions:

    >>> d[None]
    {x[i, i]*y[j, j]}

    Factors are contracted "first":

    >>> sorted(d[x[i, i]*y[j, j]], key=default_sort_key)
    [{(i,): {x[i, i]}}, {(j,): {y[j, j]}}]

    A parenthesized Add object is also returned as a nested dictionary.  The
    term containing the parenthesis is a Mul with a contraction among the
    arguments, so it will be found as a key in the result.  It stores the
    dictionary resulting from a recursive call on the Add expression.

    >>> d = get_contraction_structure(x[i]*(y[i] + A[i, j]*x[j]))
    >>> sorted(d.keys(), key=default_sort_key)
    [(A[i, j]*x[j] + y[i])*x[i], (i,)]
    >>> d[(i,)]
    {(A[i, j]*x[j] + y[i])*x[i]}
    >>> d[x[i]*(A[i, j]*x[j] + y[i])]
    [{None: {y[i]}, (j,): {A[i, j]*x[j]}}]

    Powers with contractions in either base or exponent will also be found as
    keys in the dictionary, mapping to a list of results from recursive calls:

    >>> d = get_contraction_structure(A[j, j]**A[i, i])
    >>> d[None]
    {A[j, j]**A[i, i]}
    >>> nested_contractions = d[A[j, j]**A[i, i]]
    >>> nested_contractions[0]
    {(j,): {A[j, j]}}
    >>> nested_contractions[1]
    {(i,): {A[i, i]}}

    The description of the contraction structure may appear complicated when
    represented with a string in the above examples, but it is easy to iterate
    over:

    >>> from sympy import Expr
    >>> for key in d:
    ...     if isinstance(key, Expr):
    ...         continue
    ...     for term in d[key]:
    ...         if term in d:
    ...             # treat deepest contraction first
    ...             pass
    ...     # treat outermost contactions here

    '''
