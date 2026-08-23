from _typeshed import Incomplete
from sympy.combinatorics import Permutation as Permutation

rmul: Incomplete

def canonicalize_naive(g, dummies, sym, *v):
    """
    Canonicalize tensor formed by tensors of the different types.

    Explanation
    ===========

    sym_i symmetry under exchange of two component tensors of type `i`
          None  no symmetry
          0     commuting
          1     anticommuting

    Parameters
    ==========

    g : Permutation representing the tensor.
    dummies : List of dummy indices.
    msym : Symmetry of the metric.
    v : A list of (base_i, gens_i, n_i, sym_i) for tensors of type `i`.
        base_i, gens_i BSGS for tensors of this type
        n_i  number of tensors of type `i`

    Returns
    =======

    Returns 0 if the tensor is zero, else returns the array form of
    the permutation representing the canonical form of the tensor.

    Examples
    ========

    >>> from sympy.combinatorics.testutil import canonicalize_naive
    >>> from sympy.combinatorics.tensor_can import get_symmetric_group_sgs
    >>> from sympy.combinatorics import Permutation
    >>> g = Permutation([1, 3, 2, 0, 4, 5])
    >>> base2, gens2 = get_symmetric_group_sgs(2)
    >>> canonicalize_naive(g, [2, 3], 0, (base2, gens2, 2, 0))
    [0, 2, 1, 3, 4, 5]
    """
def graph_certificate(gr):
    """
    Return a certificate for the graph

    Parameters
    ==========

    gr : adjacency list

    Explanation
    ===========

    The graph is assumed to be unoriented and without
    external lines.

    Associate to each vertex of the graph a symmetric tensor with
    number of indices equal to the degree of the vertex; indices
    are contracted when they correspond to the same line of the graph.
    The canonical form of the tensor gives a certificate for the graph.

    This is not an efficient algorithm to get the certificate of a graph.

    Examples
    ========

    >>> from sympy.combinatorics.testutil import graph_certificate
    >>> gr1 = {0:[1, 2, 3, 5], 1:[0, 2, 4], 2:[0, 1, 3, 4], 3:[0, 2, 4], 4:[1, 2, 3, 5], 5:[0, 4]}
    >>> gr2 = {0:[1, 5], 1:[0, 2, 3, 4], 2:[1, 3, 5], 3:[1, 2, 4, 5], 4:[1, 3, 5], 5:[0, 2, 3, 4]}
    >>> c1 = graph_certificate(gr1)
    >>> c2 = graph_certificate(gr2)
    >>> c1
    [0, 2, 4, 6, 1, 8, 10, 12, 3, 14, 16, 18, 5, 9, 15, 7, 11, 17, 13, 19, 20, 21]
    >>> c1 == c2
    True
    """
