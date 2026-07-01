__all__ = ['d_separated', 'minimal_d_separator', 'is_minimal_d_separator']

def d_separated(G, x, y, z):
    """
    Return whether node sets ``x`` and ``y`` are d-separated by ``z``.

    Parameters
    ----------
    G : graph
        A NetworkX DAG.

    x : set
        First set of nodes in ``G``.

    y : set
        Second set of nodes in ``G``.

    z : set
        Set of conditioning nodes in ``G``. Can be empty set.

    Returns
    -------
    b : bool
        A boolean that is true if ``x`` is d-separated from ``y`` given ``z`` in ``G``.

    Raises
    ------
    NetworkXError
        The *d-separation* test is commonly used with directed
        graphical models which are acyclic.  Accordingly, the algorithm
        raises a :exc:`NetworkXError` if the input graph is not a DAG.

    NodeNotFound
        If any of the input nodes are not found in the graph,
        a :exc:`NodeNotFound` exception is raised.

    Notes
    -----
    A d-separating set in a DAG is a set of nodes that
    blocks all paths between the two sets. Nodes in `z`
    block a path if they are part of the path and are not a collider,
    or a descendant of a collider. A collider structure along a path
    is ``... -> c <- ...`` where ``c`` is the collider node.

    https://en.wikipedia.org/wiki/Bayesian_network#d-separation
    """
def minimal_d_separator(G, u, v):
    '''Compute a minimal d-separating set between \'u\' and \'v\'.

    A d-separating set in a DAG is a set of nodes that blocks all paths
    between the two nodes, \'u\' and \'v\'. This function
    constructs a d-separating set that is "minimal", meaning it is the smallest
    d-separating set for \'u\' and \'v\'. This is not necessarily
    unique. For more details, see Notes.

    Parameters
    ----------
    G : graph
        A networkx DAG.
    u : node
        A node in the graph, G.
    v : node
        A node in the graph, G.

    Raises
    ------
    NetworkXError
        Raises a :exc:`NetworkXError` if the input graph is not a DAG.

    NodeNotFound
        If any of the input nodes are not found in the graph,
        a :exc:`NodeNotFound` exception is raised.

    References
    ----------
    .. [1] Tian, J., & Paz, A. (1998). Finding Minimal D-separators.

    Notes
    -----
    This function only finds ``a`` minimal d-separator. It does not guarantee
    uniqueness, since in a DAG there may be more than one minimal d-separator
    between two nodes. Moreover, this only checks for minimal separators
    between two nodes, not two sets. Finding minimal d-separators between
    two sets of nodes is not supported.

    Uses the algorithm presented in [1]_. The complexity of the algorithm
    is :math:`O(|E_{An}^m|)`, where :math:`|E_{An}^m|` stands for the
    number of edges in the moralized graph of the sub-graph consisting
    of only the ancestors of \'u\' and \'v\'. For full details, see [1]_.

    The algorithm works by constructing the moral graph consisting of just
    the ancestors of `u` and `v`. Then it constructs a candidate for
    a separating set  ``Z\'`` from the predecessors of `u` and `v`.
    Then BFS is run starting from `u` and marking nodes
    found from ``Z\'`` and calling those nodes ``Z\'\'``.
    Then BFS is run again starting from `v` and marking nodes if they are
    present in ``Z\'\'``. Those marked nodes are the returned minimal
    d-separating set.

    https://en.wikipedia.org/wiki/Bayesian_network#d-separation
    '''
def is_minimal_d_separator(G, u, v, z):
    '''Determine if a d-separating set is minimal.

    A d-separating set, `z`, in a DAG is a set of nodes that blocks
    all paths between the two nodes, `u` and `v`. This function
    verifies that a set is "minimal", meaning there is no smaller
    d-separating set between the two nodes.

    Note: This function checks whether `z` is a d-separator AND is minimal.
    One can use the function `d_separated` to only check if `z` is a d-separator.
    See examples below.

    Parameters
    ----------
    G : nx.DiGraph
        The graph.
    u : node
        A node in the graph.
    v : node
        A node in the graph.
    z : Set of nodes
        The set of nodes to check if it is a minimal d-separating set.
        The function :func:`d_separated` is called inside this function
        to verify that `z` is in fact a d-separator.

    Returns
    -------
    bool
        Whether or not the set `z` is a d-separator and is also minimal.

    Examples
    --------
    >>> G = nx.path_graph([0, 1, 2, 3], create_using=nx.DiGraph)
    >>> G.add_node(4)
    >>> nx.is_minimal_d_separator(G, 0, 2, {1})
    True
    >>> # since {1} is the minimal d-separator, {1, 3, 4} is not minimal
    >>> nx.is_minimal_d_separator(G, 0, 2, {1, 3, 4})
    False
    >>> # alternatively, if we only want to check that {1, 3, 4} is a d-separator
    >>> nx.d_separated(G, {0}, {4}, {1, 3, 4})
    True

    Raises
    ------
    NetworkXError
        Raises a :exc:`NetworkXError` if the input graph is not a DAG.

    NodeNotFound
        If any of the input nodes are not found in the graph,
        a :exc:`NodeNotFound` exception is raised.

    References
    ----------
    .. [1] Tian, J., & Paz, A. (1998). Finding Minimal D-separators.

    Notes
    -----
    This function only works on verifying a d-separating set is minimal
    between two nodes. To verify that a d-separating set is minimal between
    two sets of nodes is not supported.

    Uses algorithm 2 presented in [1]_. The complexity of the algorithm
    is :math:`O(|E_{An}^m|)`, where :math:`|E_{An}^m|` stands for the
    number of edges in the moralized graph of the sub-graph consisting
    of only the ancestors of ``u`` and ``v``.

    The algorithm works by constructing the moral graph consisting of just
    the ancestors of `u` and `v`. First, it performs BFS on the moral graph
    starting from `u` and marking any nodes it encounters that are part of
    the separating set, `z`. If a node is marked, then it does not continue
    along that path. In the second stage, BFS with markings is repeated on the
    moral graph starting from `v`. If at any stage, any node in `z` is
    not marked, then `z` is considered not minimal. If the end of the algorithm
    is reached, then `z` is minimal.

    For full details, see [1]_.

    https://en.wikipedia.org/wiki/Bayesian_network#d-separation
    '''
