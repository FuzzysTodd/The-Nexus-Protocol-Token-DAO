from . import dot, jupyter_integration, piping, rendering, unflattening
from _typeshed import Incomplete

__all__ = ['Graph', 'Digraph']

class BaseGraph(dot.Dot, rendering.Render, jupyter_integration.JupyterIntegration, piping.Pipe, unflattening.Unflatten):
    """Dot language creation and source code rendering."""
    def __init__(self, name: str | None = None, comment: str | None = None, filename: Incomplete | None = None, directory: Incomplete | None = None, format: str | None = None, engine: str | None = None, encoding: str | None = ..., graph_attr: Incomplete | None = None, node_attr: Incomplete | None = None, edge_attr: Incomplete | None = None, body: Incomplete | None = None, strict: bool = False, *, renderer: str | None = None, formatter: str | None = None) -> None: ...
    @property
    def source(self) -> str:
        """The generated DOT source code as string."""

class Graph(dot.GraphSyntax, BaseGraph):
    """Graph source code in the DOT language.

    Args:
        name: Graph name used in the source code.
        comment: Comment added to the first line of the source.
        filename: Filename for saving the source
            (defaults to ``name`` + ``'.gv'``).
        directory: (Sub)directory for source saving and rendering.
        format: Rendering output format (``'pdf'``, ``'png'``, ...).
        engine: Layout command used (``'dot'``, ``'neato'``, ...).
        renderer: Output renderer used (``'cairo'``, ``'gd'``, ...).
        formatter: Output formatter used (``'cairo'``, ``'gd'``, ...).
        encoding: Encoding for saving the source.
        graph_attr: Mapping of ``(attribute, value)`` pairs for the graph.
        node_attr: Mapping of ``(attribute, value)`` pairs set for all nodes.
        edge_attr: Mapping of ``(attribute, value)`` pairs set for all edges.
        body: Iterable of verbatim lines (including their final newline)
            to add to the graph ``body``.
        strict (bool): Rendering should merge multi-edges.

    Note:
        All parameters are `optional` and can be changed under their
        corresponding attribute name after instance creation.
    """
    @property
    def directed(self) -> bool:
        """``False``"""

class Digraph(dot.DigraphSyntax, BaseGraph):
    """Directed graph source code in the DOT language."""
    @property
    def directed(self) -> bool:
        """``True``"""
