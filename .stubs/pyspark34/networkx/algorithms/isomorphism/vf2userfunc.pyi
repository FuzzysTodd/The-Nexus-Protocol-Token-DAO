from . import isomorphvf2 as vf2
from _typeshed import Incomplete

__all__ = ['GraphMatcher', 'DiGraphMatcher', 'MultiGraphMatcher', 'MultiDiGraphMatcher']

class GraphMatcher(vf2.GraphMatcher):
    """VF2 isomorphism checker for undirected graphs."""
    node_match: Incomplete
    edge_match: Incomplete
    G1_adj: Incomplete
    G2_adj: Incomplete
    def __init__(self, G1, G2, node_match: Incomplete | None = None, edge_match: Incomplete | None = None) -> None:
        """Initialize graph matcher.

        Parameters
        ----------
        G1, G2: graph
            The graphs to be tested.

        node_match: callable
            A function that returns True iff node n1 in G1 and n2 in G2
            should be considered equal during the isomorphism test. The
            function will be called like::

               node_match(G1.nodes[n1], G2.nodes[n2])

            That is, the function will receive the node attribute dictionaries
            of the nodes under consideration. If None, then no attributes are
            considered when testing for an isomorphism.

        edge_match: callable
            A function that returns True iff the edge attribute dictionary for
            the pair of nodes (u1, v1) in G1 and (u2, v2) in G2 should be
            considered equal during the isomorphism test. The function will be
            called like::

               edge_match(G1[u1][v1], G2[u2][v2])

            That is, the function will receive the edge attribute dictionaries
            of the edges under consideration. If None, then no attributes are
            considered when testing for an isomorphism.

        """
    semantic_feasibility: Incomplete

class DiGraphMatcher(vf2.DiGraphMatcher):
    """VF2 isomorphism checker for directed graphs."""
    node_match: Incomplete
    edge_match: Incomplete
    G1_adj: Incomplete
    G2_adj: Incomplete
    def __init__(self, G1, G2, node_match: Incomplete | None = None, edge_match: Incomplete | None = None) -> None:
        """Initialize graph matcher.

        Parameters
        ----------
        G1, G2 : graph
            The graphs to be tested.

        node_match : callable
            A function that returns True iff node n1 in G1 and n2 in G2
            should be considered equal during the isomorphism test. The
            function will be called like::

               node_match(G1.nodes[n1], G2.nodes[n2])

            That is, the function will receive the node attribute dictionaries
            of the nodes under consideration. If None, then no attributes are
            considered when testing for an isomorphism.

        edge_match : callable
            A function that returns True iff the edge attribute dictionary for
            the pair of nodes (u1, v1) in G1 and (u2, v2) in G2 should be
            considered equal during the isomorphism test. The function will be
            called like::

               edge_match(G1[u1][v1], G2[u2][v2])

            That is, the function will receive the edge attribute dictionaries
            of the edges under consideration. If None, then no attributes are
            considered when testing for an isomorphism.

        """
    def semantic_feasibility(self, G1_node, G2_node):
        """Returns True if mapping G1_node to G2_node is semantically feasible."""

class MultiGraphMatcher(GraphMatcher):
    """VF2 isomorphism checker for undirected multigraphs."""
class MultiDiGraphMatcher(DiGraphMatcher):
    """VF2 isomorphism checker for directed multigraphs."""
