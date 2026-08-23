from _typeshed import Incomplete

__all__ = ['_dispatch']

class _dispatch:
    '''Dispatches to a backend algorithm based on input graph types.

    Parameters
    ----------
    func : function

    name : str, optional
        The name of the algorithm to use for dispatching. If not provided,
        the name of ``func`` will be used. ``name`` is useful to avoid name
        conflicts, as all dispatched algorithms live in a single namespace.

    graphs : str or dict or None, default "G"
        If a string, the parameter name of the graph, which must be the first
        argument of the wrapped function. If more than one graph is required
        for the algorithm (or if the graph is not the first argument), provide
        a dict of parameter name to argument position for each graph argument.
        For example, ``@_dispatch(graphs={"G": 0, "auxiliary?": 4})``
        indicates the 0th parameter ``G`` of the function is a required graph,
        and the 4th parameter ``auxiliary`` is an optional graph.
        To indicate an argument is a list of graphs, do e.g. ``"[graphs]"``.
        Use ``graphs=None`` if *no* arguments are NetworkX graphs such as for
        graph generators, readers, and conversion functions.

    edge_attrs : str or dict, optional
        ``edge_attrs`` holds information about edge attribute arguments
        and default values for those edge attributes.
        If a string, ``edge_attrs`` holds the function argument name that
        indicates a single edge attribute to include in the converted graph.
        The default value for this attribute is 1. To indicate that an argument
        is a list of attributes (all with default value 1), use e.g. ``"[attrs]"``.
        If a dict, ``edge_attrs`` holds a dict keyed by argument names, with
        values that are either the default value or, if a string, the argument
        name that indicates the default value.

    node_attrs : str or dict, optional
        Like ``edge_attrs``, but for node attributes.

    preserve_edge_attrs : bool or str or dict, optional
        For bool, whether to preserve all edge attributes.
        For str, the parameter name that may indicate (with ``True`` or a
        callable argument) whether all edge attributes should be preserved
        when converting.
        For dict of ``{graph_name: {attr: default}}``, indicate pre-determined
        edge attributes (and defaults) to preserve for input graphs.

    preserve_node_attrs : bool or str or dict, optional
        Like ``preserve_edge_attrs``, but for node attributes.

    preserve_graph_attrs : bool or set
        For bool, whether to preserve all graph attributes.
        For set, which input graph arguments to preserve graph attributes.

    preserve_all_attrs : bool
        Whether to preserve all edge, node and graph attributes.
        This overrides all the other preserve_*_attrs.

    '''
    __defaults__: Incomplete
    __kwdefaults__: Incomplete
    __module__: Incomplete
    __qualname__: Incomplete
    __wrapped__: Incomplete
    orig_func: Incomplete
    name: Incomplete
    edge_attrs: Incomplete
    node_attrs: Incomplete
    preserve_edge_attrs: Incomplete
    preserve_node_attrs: Incomplete
    preserve_graph_attrs: Incomplete
    optional_graphs: Incomplete
    list_graphs: Incomplete
    graphs: Incomplete
    backends: Incomplete
    def __new__(cls, func: Incomplete | None = None, *, name: Incomplete | None = None, graphs: str = 'G', edge_attrs: Incomplete | None = None, node_attrs: Incomplete | None = None, preserve_edge_attrs: bool = False, preserve_node_attrs: bool = False, preserve_graph_attrs: bool = False, preserve_all_attrs: bool = False): ...
    @property
    def __doc__(self): ...
    @__doc__.setter
    def __doc__(self, val) -> None: ...
    @property
    def __signature__(self): ...
    def __call__(self, *args, backend: Incomplete | None = None, **kwargs): ...
    def __reduce__(self):
        """Allow this object to be serialized with pickle.

        This uses the global registry `_registered_algorithms` to deserialize.
        """
