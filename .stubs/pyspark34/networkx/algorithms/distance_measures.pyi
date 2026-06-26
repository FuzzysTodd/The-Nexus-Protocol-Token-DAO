from _typeshed import Incomplete

__all__ = ['eccentricity', 'diameter', 'radius', 'periphery', 'center', 'barycenter', 'resistance_distance', 'kemeny_constant']

def eccentricity(G, v: Incomplete | None = None, sp: Incomplete | None = None, weight: Incomplete | None = None):
    """Returns the eccentricity of nodes in G.

    The eccentricity of a node v is the maximum distance from v to
    all other nodes in G.

    Parameters
    ----------
    G : NetworkX graph
       A graph

    v : node, optional
       Return value of specified node

    sp : dict of dicts, optional
       All pairs shortest path lengths as a dictionary of dictionaries

    weight : string, function, or None (default=None)
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number.

        If this is None, every edge has weight/distance/cost 1.

        Weights stored as floating point values can lead to small round-off
        errors in distances. Use integer weights to avoid this.

        Weights should be positive, since they are distances.

    Returns
    -------
    ecc : dictionary
       A dictionary of eccentricity values keyed by node.

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])
    >>> dict(nx.eccentricity(G))
    {1: 2, 2: 3, 3: 2, 4: 2, 5: 3}

    >>> dict(nx.eccentricity(G, v=[1, 5]))  # This returns the eccentricity of node 1 & 5
    {1: 2, 5: 3}

    """
def diameter(G, e: Incomplete | None = None, usebounds: bool = False, weight: Incomplete | None = None):
    """Returns the diameter of the graph G.

    The diameter is the maximum eccentricity.

    Parameters
    ----------
    G : NetworkX graph
       A graph

    e : eccentricity dictionary, optional
      A precomputed dictionary of eccentricities.

    weight : string, function, or None
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number.

        If this is None, every edge has weight/distance/cost 1.

        Weights stored as floating point values can lead to small round-off
        errors in distances. Use integer weights to avoid this.

        Weights should be positive, since they are distances.

    Returns
    -------
    d : integer
       Diameter of graph

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])
    >>> nx.diameter(G)
    3

    See Also
    --------
    eccentricity
    """
def periphery(G, e: Incomplete | None = None, usebounds: bool = False, weight: Incomplete | None = None):
    """Returns the periphery of the graph G.

    The periphery is the set of nodes with eccentricity equal to the diameter.

    Parameters
    ----------
    G : NetworkX graph
       A graph

    e : eccentricity dictionary, optional
      A precomputed dictionary of eccentricities.

    weight : string, function, or None
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number.

        If this is None, every edge has weight/distance/cost 1.

        Weights stored as floating point values can lead to small round-off
        errors in distances. Use integer weights to avoid this.

        Weights should be positive, since they are distances.

    Returns
    -------
    p : list
       List of nodes in periphery

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])
    >>> nx.periphery(G)
    [2, 5]

    See Also
    --------
    barycenter
    center
    """
def radius(G, e: Incomplete | None = None, usebounds: bool = False, weight: Incomplete | None = None):
    """Returns the radius of the graph G.

    The radius is the minimum eccentricity.

    Parameters
    ----------
    G : NetworkX graph
       A graph

    e : eccentricity dictionary, optional
      A precomputed dictionary of eccentricities.

    weight : string, function, or None
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number.

        If this is None, every edge has weight/distance/cost 1.

        Weights stored as floating point values can lead to small round-off
        errors in distances. Use integer weights to avoid this.

        Weights should be positive, since they are distances.

    Returns
    -------
    r : integer
       Radius of graph

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])
    >>> nx.radius(G)
    2

    """
def center(G, e: Incomplete | None = None, usebounds: bool = False, weight: Incomplete | None = None):
    """Returns the center of the graph G.

    The center is the set of nodes with eccentricity equal to radius.

    Parameters
    ----------
    G : NetworkX graph
       A graph

    e : eccentricity dictionary, optional
      A precomputed dictionary of eccentricities.

    weight : string, function, or None
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number.

        If this is None, every edge has weight/distance/cost 1.

        Weights stored as floating point values can lead to small round-off
        errors in distances. Use integer weights to avoid this.

        Weights should be positive, since they are distances.

    Returns
    -------
    c : list
       List of nodes in center

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])
    >>> list(nx.center(G))
    [1, 3, 4]

    See Also
    --------
    barycenter
    periphery
    """
def barycenter(G, weight: Incomplete | None = None, attr: Incomplete | None = None, sp: Incomplete | None = None):
    """Calculate barycenter of a connected graph, optionally with edge weights.

    The :dfn:`barycenter` a
    :func:`connected <networkx.algorithms.components.is_connected>` graph
    :math:`G` is the subgraph induced by the set of its nodes :math:`v`
    minimizing the objective function

    .. math::

        \\sum_{u \\in V(G)} d_G(u, v),

    where :math:`d_G` is the (possibly weighted) :func:`path length
    <networkx.algorithms.shortest_paths.generic.shortest_path_length>`.
    The barycenter is also called the :dfn:`median`. See [West01]_, p. 78.

    Parameters
    ----------
    G : :class:`networkx.Graph`
        The connected graph :math:`G`.
    weight : :class:`str`, optional
        Passed through to
        :func:`~networkx.algorithms.shortest_paths.generic.shortest_path_length`.
    attr : :class:`str`, optional
        If given, write the value of the objective function to each node's
        `attr` attribute. Otherwise do not store the value.
    sp : dict of dicts, optional
       All pairs shortest path lengths as a dictionary of dictionaries

    Returns
    -------
    list
        Nodes of `G` that induce the barycenter of `G`.

    Raises
    ------
    NetworkXNoPath
        If `G` is disconnected. `G` may appear disconnected to
        :func:`barycenter` if `sp` is given but is missing shortest path
        lengths for any pairs.
    ValueError
        If `sp` and `weight` are both given.

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])
    >>> nx.barycenter(G)
    [1, 3, 4]

    See Also
    --------
    center
    periphery
    """
def resistance_distance(G, nodeA: Incomplete | None = None, nodeB: Incomplete | None = None, weight: Incomplete | None = None, invert_weight: bool = True):
    '''Returns the resistance distance between every pair of nodes on graph G.

    The resistance distance between two nodes of a graph is akin to treating
    the graph as a grid of resistors with a resistance equal to the provided
    weight [1]_, [2]_.

    If weight is not provided, then a weight of 1 is used for all edges.

    If two nodes are the same, the resistance distance is zero.

    Parameters
    ----------
    G : NetworkX graph
       A graph

    nodeA : node or None, optional (default=None)
      A node within graph G.
      If None, compute resistance distance using all nodes as source nodes.

    nodeB : node or None, optional (default=None)
      A node within graph G.
      If None, compute resistance distance using all nodes as target nodes.

    weight : string or None, optional (default=None)
       The edge data key used to compute the resistance distance.
       If None, then each edge has weight 1.

    invert_weight : boolean (default=True)
        Proper calculation of resistance distance requires building the
        Laplacian matrix with the reciprocal of the weight. Not required
        if the weight is already inverted. Weight cannot be zero.

    Returns
    -------
    rd : dict or float
       If `nodeA` and `nodeB` are given, resistance distance between `nodeA`
       and `nodeB`. If `nodeA` or `nodeB` is unspecified (the default), a
       dictionary of nodes with resistance distances as the value.

    Raises
    ------
    NetworkXNotImplemented
        If `G` is a directed graph.

    NetworkXError
        If `G` is not connected, or contains no nodes,
        or `nodeA` is not in `G` or `nodeB` is not in `G`.

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])
    >>> round(nx.resistance_distance(G, 1, 3), 10)
    0.625

    Notes
    -----
    The implementation is based on Theorem A in [2]_. Self-loops are ignored.
    Multi-edges are contracted in one edge with weight equal to the harmonic sum of the weights.

    References
    ----------
    .. [1] Wikipedia
       "Resistance distance."
       https://en.wikipedia.org/wiki/Resistance_distance
    .. [2] D. J. Klein and M. Randic.
        Resistance distance.
        J. of Math. Chem. 12:81-95, 1993.
    '''
def kemeny_constant(G, *, weight: Incomplete | None = None):
    '''Returns the Kemeny constant of the given graph.

    The *Kemeny constant* (or Kemeny\'s constant) of a graph `G`
    can be computed by regarding the graph as a Markov chain.
    The Kemeny constant is then the expected number of time steps
    to transition from a starting state i to a random destination state
    sampled from the Markov chain\'s stationary distribution.
    The Kemeny constant is independent of the chosen initial state [1]_.

    The Kemeny constant measures the time needed for spreading
    across a graph. Low values indicate a closely connected graph
    whereas high values indicate a spread-out graph.

    If weight is not provided, then a weight of 1 is used for all edges.

    Since `G` represents a Markov chain, the weights must be positive.

    Parameters
    ----------
    G : NetworkX graph

    weight : string or None, optional (default=None)
       The edge data key used to compute the Kemeny constant.
       If None, then each edge has weight 1.

    Returns
    -------
    K : float
        The Kemeny constant of the graph `G`.

    Raises
    ------
    NetworkXNotImplemented
        If the graph `G` is directed.

    NetworkXError
        If the graph `G` is not connected, or contains no nodes,
        or has edges with negative weights.

    Examples
    --------
    >>> G = nx.complete_graph(5)
    >>> round(nx.kemeny_constant(G), 10)
    3.2

    Notes
    -----
    The implementation is based on equation (3.3) in [2]_.
    Self-loops are allowed and indicate a Markov chain where
    the state can remain the same. Multi-edges are contracted
    in one edge with weight equal to the sum of the weights.

    References
    ----------
    .. [1] Wikipedia
       "Kemeny\'s constant."
       https://en.wikipedia.org/wiki/Kemeny%27s_constant
    .. [2] Lovász L.
        Random walks on graphs: A survey.
        Paul Erdös is Eighty, vol. 2, Bolyai Society,
        Mathematical Studies, Keszthely, Hungary (1993), pp. 1-46
    '''
