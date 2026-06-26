from _typeshed import Incomplete

__all__ = ['generic_graph_view', 'subgraph_view', 'reverse_view']

def generic_graph_view(G, create_using: Incomplete | None = None):
    """Returns a read-only view of `G`.

    The graph `G` and its attributes are not copied but viewed through the new graph object
    of the same class as `G` (or of the class specified in `create_using`).

    Parameters
    ----------
    G : graph
        A directed/undirected graph/multigraph.

    create_using : NetworkX graph constructor, optional (default=None)
       Graph type to create. If graph instance, then cleared before populated.
       If `None`, then the appropriate Graph type is inferred from `G`.

    Returns
    -------
    newG : graph
        A view of the input graph `G` and its attributes as viewed through
        the `create_using` class.

    Raises
    ------
    NetworkXError
        If `G` is a multigraph (or multidigraph) but `create_using` is not, or vice versa.

    Notes
    -----
    The returned graph view is read-only (cannot modify the graph).
    Yet the view reflects any changes in `G`. The intent is to mimic dict views.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_edge(1, 2, weight=0.3)
    >>> G.add_edge(2, 3, weight=0.5)
    >>> G.edges(data=True)
    EdgeDataView([(1, 2, {'weight': 0.3}), (2, 3, {'weight': 0.5})])

    The view exposes the attributes from the original graph.

    >>> viewG = nx.graphviews.generic_graph_view(G)
    >>> viewG.edges(data=True)
    EdgeDataView([(1, 2, {'weight': 0.3}), (2, 3, {'weight': 0.5})])

    Changes to `G` are reflected in `viewG`.

    >>> G.remove_edge(2, 3)
    >>> G.edges(data=True)
    EdgeDataView([(1, 2, {'weight': 0.3})])

    >>> viewG.edges(data=True)
    EdgeDataView([(1, 2, {'weight': 0.3})])

    We can change the graph type with the `create_using` parameter.

    >>> type(G)
    <class 'networkx.classes.graph.Graph'>
    >>> viewDG = nx.graphviews.generic_graph_view(G, create_using=nx.DiGraph)
    >>> type(viewDG)
    <class 'networkx.classes.digraph.DiGraph'>
    """
def subgraph_view(G, *, filter_node=..., filter_edge=...):
    '''View of `G` applying a filter on nodes and edges.

    `subgraph_view` provides a read-only view of the input graph that excludes
    nodes and edges based on the outcome of two filter functions `filter_node`
    and `filter_edge`.

    The `filter_node` function takes one argument --- the node --- and returns
    `True` if the node should be included in the subgraph, and `False` if it
    should not be included.

    The `filter_edge` function takes two (or three arguments if `G` is a
    multi-graph) --- the nodes describing an edge, plus the edge-key if
    parallel edges are possible --- and returns `True` if the edge should be
    included in the subgraph, and `False` if it should not be included.

    Both node and edge filter functions are called on graph elements as they
    are queried, meaning there is no up-front cost to creating the view.

    Parameters
    ----------
    G : networkx.Graph
        A directed/undirected graph/multigraph

    filter_node : callable, optional
        A function taking a node as input, which returns `True` if the node
        should appear in the view.

    filter_edge : callable, optional
        A function taking as input the two nodes describing an edge (plus the
        edge-key if `G` is a multi-graph), which returns `True` if the edge
        should appear in the view.

    Returns
    -------
    graph : networkx.Graph
        A read-only graph view of the input graph.

    Examples
    --------
    >>> G = nx.path_graph(6)

    Filter functions operate on the node, and return `True` if the node should
    appear in the view:

    >>> def filter_node(n1):
    ...     return n1 != 5
    ...
    >>> view = nx.subgraph_view(G, filter_node=filter_node)
    >>> view.nodes()
    NodeView((0, 1, 2, 3, 4))

    We can use a closure pattern to filter graph elements based on additional
    data --- for example, filtering on edge data attached to the graph:

    >>> G[3][4]["cross_me"] = False
    >>> def filter_edge(n1, n2):
    ...     return G[n1][n2].get("cross_me", True)
    ...
    >>> view = nx.subgraph_view(G, filter_edge=filter_edge)
    >>> view.edges()
    EdgeView([(0, 1), (1, 2), (2, 3), (4, 5)])

    >>> view = nx.subgraph_view(G, filter_node=filter_node, filter_edge=filter_edge,)
    >>> view.nodes()
    NodeView((0, 1, 2, 3, 4))
    >>> view.edges()
    EdgeView([(0, 1), (1, 2), (2, 3)])
    '''
def reverse_view(G):
    """View of `G` with edge directions reversed

    `reverse_view` returns a read-only view of the input graph where
    edge directions are reversed.

    Identical to digraph.reverse(copy=False)

    Parameters
    ----------
    G : networkx.DiGraph

    Returns
    -------
    graph : networkx.DiGraph

    Examples
    --------
    >>> G = nx.DiGraph()
    >>> G.add_edge(1, 2)
    >>> G.add_edge(2, 3)
    >>> G.edges()
    OutEdgeView([(1, 2), (2, 3)])

    >>> view = nx.reverse_view(G)
    >>> view.edges()
    OutEdgeView([(2, 1), (3, 2)])
    """
