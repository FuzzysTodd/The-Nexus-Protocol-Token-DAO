__all__ = ['is_arborescence', 'is_branching', 'is_forest', 'is_tree']

def is_arborescence(G):
    """
    Returns True if `G` is an arborescence.

    An arborescence is a directed tree with maximum in-degree equal to 1.

    Parameters
    ----------
    G : graph
        The graph to test.

    Returns
    -------
    b : bool
        A boolean that is True if `G` is an arborescence.

    Examples
    --------
    >>> G = nx.DiGraph([(0, 1), (0, 2), (2, 3), (3, 4)])
    >>> nx.is_arborescence(G)
    True
    >>> G.remove_edge(0, 1)
    >>> G.add_edge(1, 2)  # maximum in-degree is 2
    >>> nx.is_arborescence(G)
    False

    Notes
    -----
    In another convention, an arborescence is known as a *tree*.

    See Also
    --------
    is_tree

    """
def is_branching(G):
    """
    Returns True if `G` is a branching.

    A branching is a directed forest with maximum in-degree equal to 1.

    Parameters
    ----------
    G : directed graph
        The directed graph to test.

    Returns
    -------
    b : bool
        A boolean that is True if `G` is a branching.

    Examples
    --------
    >>> G = nx.DiGraph([(0, 1), (1, 2), (2, 3), (3, 4)])
    >>> nx.is_branching(G)
    True
    >>> G.remove_edge(2, 3)
    >>> G.add_edge(3, 1)  # maximum in-degree is 2
    >>> nx.is_branching(G)
    False

    Notes
    -----
    In another convention, a branching is also known as a *forest*.

    See Also
    --------
    is_forest

    """
def is_forest(G):
    """
    Returns True if `G` is a forest.

    A forest is a graph with no undirected cycles.

    For directed graphs, `G` is a forest if the underlying graph is a forest.
    The underlying graph is obtained by treating each directed edge as a single
    undirected edge in a multigraph.

    Parameters
    ----------
    G : graph
        The graph to test.

    Returns
    -------
    b : bool
        A boolean that is True if `G` is a forest.

    Raises
    ------
    NetworkXPointlessConcept
        If `G` is empty.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5)])
    >>> nx.is_forest(G)
    True
    >>> G.add_edge(4, 1)
    >>> nx.is_forest(G)
    False

    Notes
    -----
    In another convention, a directed forest is known as a *polyforest* and
    then *forest* corresponds to a *branching*.

    See Also
    --------
    is_branching

    """
def is_tree(G):
    """
    Returns True if `G` is a tree.

    A tree is a connected graph with no undirected cycles.

    For directed graphs, `G` is a tree if the underlying graph is a tree. The
    underlying graph is obtained by treating each directed edge as a single
    undirected edge in a multigraph.

    Parameters
    ----------
    G : graph
        The graph to test.

    Returns
    -------
    b : bool
        A boolean that is True if `G` is a tree.

    Raises
    ------
    NetworkXPointlessConcept
        If `G` is empty.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5)])
    >>> nx.is_tree(G)  # n-1 edges
    True
    >>> G.add_edge(3, 4)
    >>> nx.is_tree(G)  # n edges
    False

    Notes
    -----
    In another convention, a directed tree is known as a *polytree* and then
    *tree* corresponds to an *arborescence*.

    See Also
    --------
    is_arborescence

    """
