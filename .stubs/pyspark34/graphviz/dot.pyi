import typing
from . import base, quoting
from _typeshed import Incomplete

__all__ = ['GraphSyntax', 'DigraphSyntax', 'Dot']

class GraphSyntax:
    """DOT graph head and edge syntax."""
class DigraphSyntax:
    """DOT digraph head and edge syntax."""

class Dot(quoting.Quote, base.Base):
    """Assemble DOT source code."""
    directed: bool
    name: Incomplete
    comment: Incomplete
    graph_attr: Incomplete
    node_attr: Incomplete
    edge_attr: Incomplete
    body: Incomplete
    strict: Incomplete
    def __init__(self, *, name: str | None = None, comment: str | None = None, graph_attr: Incomplete | None = None, node_attr: Incomplete | None = None, edge_attr: Incomplete | None = None, body: Incomplete | None = None, strict: bool = False, **kwargs) -> None: ...
    def clear(self, keep_attrs: bool = False) -> None:
        """Reset content to an empty body, clear graph/node/egde_attr mappings.

        Args:
            keep_attrs (bool): preserve graph/node/egde_attr mappings
        """
    def __iter__(self, subgraph: bool = False) -> typing.Iterator[str]:
        """Yield the DOT source code line by line (as graph or subgraph).

        Yields: Line ending with a newline (``'\\n'``).
        """
    def node(self, name: str, label: str | None = None, _attributes: Incomplete | None = None, **attrs) -> None:
        """Create a node.

        Args:
            name: Unique identifier for the node inside the source.
            label: Caption to be displayed (defaults to the node ``name``).
            attrs: Any additional node attributes (must be strings).
        """
    def edge(self, tail_name: str, head_name: str, label: str | None = None, _attributes: Incomplete | None = None, **attrs) -> None:
        """Create an edge between two nodes.

        Args:
            tail_name: Start node identifier
                (format: ``node[:port[:compass]]``).
            head_name: End node identifier
                (format: ``node[:port[:compass]]``).
            label: Caption to be displayed near the edge.
            attrs: Any additional edge attributes (must be strings).

        Note:
            The ``tail_name`` and ``head_name`` strings are separated
            by (optional) colon(s) into ``node`` name, ``port`` name,
            and ``compass`` (e.g. ``sw``).
            See :ref:`details in the User Guide <node-ports-compass>`.
        """
    def edges(self, tail_head_iter) -> None:
        """Create a bunch of edges.

        Args:
            tail_head_iter: Iterable of ``(tail_name, head_name)`` pairs
                (format:``node[:port[:compass]]``).


        Note:
            The ``tail_name`` and ``head_name`` strings are separated
            by (optional) colon(s) into ``node`` name, ``port`` name,
            and ``compass`` (e.g. ``sw``).
            See :ref:`details in the User Guide <node-ports-compass>`.
        """
    def attr(self, kw: str | None = None, _attributes: Incomplete | None = None, **attrs) -> None:
        """Add a general or graph/node/edge attribute statement.

        Args:
            kw: Attributes target
                (``None`` or ``'graph'``, ``'node'``, ``'edge'``).
            attrs: Attributes to be set (must be strings, may be empty).

        See the :ref:`usage examples in the User Guide <attributes>`.
        """
    def subgraph(self, graph: Incomplete | None = None, name: str | None = None, comment: str | None = None, graph_attr: Incomplete | None = None, node_attr: Incomplete | None = None, edge_attr: Incomplete | None = None, body: Incomplete | None = None):
        """Add the current content of the given sole ``graph`` argument
            as subgraph or return a context manager
            returning a new graph instance
            created with the given (``name``, ``comment``, etc.) arguments
            whose content is added as subgraph
            when leaving the context manager's ``with``-block.

        Args:
            graph: An instance of the same kind
                (:class:`.Graph`, :class:`.Digraph`) as the current graph
                (sole argument in non-with-block use).
            name: Subgraph name (``with``-block use).
            comment: Subgraph comment (``with``-block use).
            graph_attr: Subgraph-level attribute-value mapping
                (``with``-block use).
            node_attr: Node-level attribute-value mapping
                (``with``-block use).
            edge_attr: Edge-level attribute-value mapping
                (``with``-block use).
            body: Verbatim lines to add to the subgraph ``body``
                (``with``-block use).

        See the :ref:`usage examples in the User Guide <subgraphs-clusters>`.

        When used as a context manager, the returned new graph instance
        uses ``strict=None`` and the parent graph's values
        for ``directory``, ``format``, ``engine``, and ``encoding`` by default.

        Note:
            If the ``name`` of the subgraph begins with
            ``'cluster'`` (all lowercase)
            the layout engine will treat it as a special cluster subgraph.
        """
