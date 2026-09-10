from _typeshed import Incomplete
from collections.abc import Generator
from typing import NamedTuple

__all__ = ['k_edge_augmentation', 'is_k_edge_connected', 'is_locally_k_edge_connected']

def is_k_edge_connected(G, k):
    """Tests to see if a graph is k-edge-connected.

    Is it impossible to disconnect the graph by removing fewer than k edges?
    If so, then G is k-edge-connected.

    Parameters
    ----------
    G : NetworkX graph
       An undirected graph.

    k : integer
        edge connectivity to test for

    Returns
    -------
    boolean
        True if G is k-edge-connected.

    See Also
    --------
    :func:`is_locally_k_edge_connected`

    Examples
    --------
    >>> G = nx.barbell_graph(10, 0)
    >>> nx.is_k_edge_connected(G, k=1)
    True
    >>> nx.is_k_edge_connected(G, k=2)
    False
    """
def is_locally_k_edge_connected(G, s, t, k):
    """Tests to see if an edge in a graph is locally k-edge-connected.

    Is it impossible to disconnect s and t by removing fewer than k edges?
    If so, then s and t are locally k-edge-connected in G.

    Parameters
    ----------
    G : NetworkX graph
       An undirected graph.

    s : node
        Source node

    t : node
        Target node

    k : integer
        local edge connectivity for nodes s and t

    Returns
    -------
    boolean
        True if s and t are locally k-edge-connected in G.

    See Also
    --------
    :func:`is_k_edge_connected`

    Examples
    --------
    >>> from networkx.algorithms.connectivity import is_locally_k_edge_connected
    >>> G = nx.barbell_graph(10, 0)
    >>> is_locally_k_edge_connected(G, 5, 15, k=1)
    True
    >>> is_locally_k_edge_connected(G, 5, 15, k=2)
    False
    >>> is_locally_k_edge_connected(G, 1, 5, k=2)
    True
    """
def k_edge_augmentation(G, k, avail: Incomplete | None = None, weight: Incomplete | None = None, partial: bool = False) -> Generator[Incomplete, Incomplete, None]:
    '''Finds set of edges to k-edge-connect G.

    Adding edges from the augmentation to G make it impossible to disconnect G
    unless k or more edges are removed. This function uses the most efficient
    function available (depending on the value of k and if the problem is
    weighted or unweighted) to search for a minimum weight subset of available
    edges that k-edge-connects G. In general, finding a k-edge-augmentation is
    NP-hard, so solutions are not guaranteed to be minimal. Furthermore, a
    k-edge-augmentation may not exist.

    Parameters
    ----------
    G : NetworkX graph
       An undirected graph.

    k : integer
        Desired edge connectivity

    avail : dict or a set of 2 or 3 tuples
        The available edges that can be used in the augmentation.

        If unspecified, then all edges in the complement of G are available.
        Otherwise, each item is an available edge (with an optional weight).

        In the unweighted case, each item is an edge ``(u, v)``.

        In the weighted case, each item is a 3-tuple ``(u, v, d)`` or a dict
        with items ``(u, v): d``.  The third item, ``d``, can be a dictionary
        or a real number.  If ``d`` is a dictionary ``d[weight]``
        correspondings to the weight.

    weight : string
        key to use to find weights if ``avail`` is a set of 3-tuples where the
        third item in each tuple is a dictionary.

    partial : boolean
        If partial is True and no feasible k-edge-augmentation exists, then all
        a partial k-edge-augmentation is generated. Adding the edges in a
        partial augmentation to G, minimizes the number of k-edge-connected
        components and maximizes the edge connectivity between those
        components. For details, see :func:`partial_k_edge_augmentation`.

    Yields
    ------
    edge : tuple
        Edges that, once added to G, would cause G to become k-edge-connected.
        If partial is False, an error is raised if this is not possible.
        Otherwise, generated edges form a partial augmentation, which
        k-edge-connects any part of G where it is possible, and maximally
        connects the remaining parts.

    Raises
    ------
    NetworkXUnfeasible
        If partial is False and no k-edge-augmentation exists.

    NetworkXNotImplemented
        If the input graph is directed or a multigraph.

    ValueError:
        If k is less than 1

    Notes
    -----
    When k=1 this returns an optimal solution.

    When k=2 and ``avail`` is None, this returns an optimal solution.
    Otherwise when k=2, this returns a 2-approximation of the optimal solution.

    For k>3, this problem is NP-hard and this uses a randomized algorithm that
        produces a feasible solution, but provides no guarantees on the
        solution weight.

    Examples
    --------
    >>> # Unweighted cases
    >>> G = nx.path_graph((1, 2, 3, 4))
    >>> G.add_node(5)
    >>> sorted(nx.k_edge_augmentation(G, k=1))
    [(1, 5)]
    >>> sorted(nx.k_edge_augmentation(G, k=2))
    [(1, 5), (5, 4)]
    >>> sorted(nx.k_edge_augmentation(G, k=3))
    [(1, 4), (1, 5), (2, 5), (3, 5), (4, 5)]
    >>> complement = list(nx.k_edge_augmentation(G, k=5, partial=True))
    >>> G.add_edges_from(complement)
    >>> nx.edge_connectivity(G)
    4

    >>> # Weighted cases
    >>> G = nx.path_graph((1, 2, 3, 4))
    >>> G.add_node(5)
    >>> # avail can be a tuple with a dict
    >>> avail = [(1, 5, {"weight": 11}), (2, 5, {"weight": 10})]
    >>> sorted(nx.k_edge_augmentation(G, k=1, avail=avail, weight="weight"))
    [(2, 5)]
    >>> # or avail can be a 3-tuple with a real number
    >>> avail = [(1, 5, 11), (2, 5, 10), (4, 3, 1), (4, 5, 51)]
    >>> sorted(nx.k_edge_augmentation(G, k=2, avail=avail))
    [(1, 5), (2, 5), (4, 5)]
    >>> # or avail can be a dict
    >>> avail = {(1, 5): 11, (2, 5): 10, (4, 3): 1, (4, 5): 51}
    >>> sorted(nx.k_edge_augmentation(G, k=2, avail=avail))
    [(1, 5), (2, 5), (4, 5)]
    >>> # If augmentation is infeasible, then a partial solution can be found
    >>> avail = {(1, 5): 11}
    >>> sorted(nx.k_edge_augmentation(G, k=2, avail=avail, partial=True))
    [(1, 5)]
    '''

class MetaEdge(NamedTuple):
    meta_uv: Incomplete
    uv: Incomplete
    w: Incomplete
