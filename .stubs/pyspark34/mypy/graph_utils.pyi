from typing import AbstractSet, Iterable, Iterator, TypeVar

T = TypeVar('T')

def strongly_connected_components(vertices: AbstractSet[T], edges: dict[T, list[T]]) -> Iterator[set[T]]:
    """Compute Strongly Connected Components of a directed graph.

    Args:
      vertices: the labels for the vertices
      edges: for each vertex, gives the target vertices of its outgoing edges

    Returns:
      An iterator yielding strongly connected components, each
      represented as a set of vertices.  Each input vertex will occur
      exactly once; vertices not part of a SCC are returned as
      singleton sets.

    From https://code.activestate.com/recipes/578507/.
    """
def prepare_sccs(sccs: list[set[T]], edges: dict[T, list[T]]) -> dict[AbstractSet[T], set[AbstractSet[T]]]:
    """Use original edges to organize SCCs in a graph by dependencies between them."""
def topsort(data: dict[T, set[T]]) -> Iterable[set[T]]:
    """Topological sort.

    Args:
      data: A map from vertices to all vertices that it has an edge
            connecting it to.  NOTE: This data structure
            is modified in place -- for normalization purposes,
            self-dependencies are removed and entries representing
            orphans are added.

    Returns:
      An iterator yielding sets of vertices that have an equivalent
      ordering.

    Example:
      Suppose the input has the following structure:

        {A: {B, C}, B: {D}, C: {D}}

      This is normalized to:

        {A: {B, C}, B: {D}, C: {D}, D: {}}

      The algorithm will yield the following values:

        {D}
        {B, C}
        {A}

    From https://code.activestate.com/recipes/577413/.
    """
