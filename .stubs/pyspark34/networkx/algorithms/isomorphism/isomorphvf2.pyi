from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['GraphMatcher', 'DiGraphMatcher']

class GraphMatcher:
    """Implementation of VF2 algorithm for matching undirected graphs.

    Suitable for Graph and MultiGraph instances.
    """
    G1: Incomplete
    G2: Incomplete
    G1_nodes: Incomplete
    G2_nodes: Incomplete
    G2_node_order: Incomplete
    old_recursion_limit: Incomplete
    test: str
    def __init__(self, G1, G2) -> None:
        """Initialize GraphMatcher.

        Parameters
        ----------
        G1,G2: NetworkX Graph or MultiGraph instances.
           The two graphs to check for isomorphism or monomorphism.

        Examples
        --------
        To create a GraphMatcher which checks for syntactic feasibility:

        >>> from networkx.algorithms import isomorphism
        >>> G1 = nx.path_graph(4)
        >>> G2 = nx.path_graph(4)
        >>> GM = isomorphism.GraphMatcher(G1, G2)
        """
    def reset_recursion_limit(self) -> None:
        """Restores the recursion limit."""
    def candidate_pairs_iter(self) -> Generator[Incomplete, None, None]:
        """Iterator over candidate pairs of nodes in G1 and G2."""
    core_1: Incomplete
    core_2: Incomplete
    inout_1: Incomplete
    inout_2: Incomplete
    state: Incomplete
    mapping: Incomplete
    def initialize(self) -> None:
        """Reinitializes the state of the algorithm.

        This method should be redefined if using something other than GMState.
        If only subclassing GraphMatcher, a redefinition is not necessary.

        """
    def is_isomorphic(self):
        """Returns True if G1 and G2 are isomorphic graphs."""
    def isomorphisms_iter(self) -> Generator[Incomplete, Incomplete, None]:
        """Generator over isomorphisms between G1 and G2."""
    def match(self) -> Generator[Incomplete, Incomplete, None]:
        """Extends the isomorphism mapping.

        This function is called recursively to determine if a complete
        isomorphism can be found between G1 and G2.  It cleans up the class
        variables after each recursive call. If an isomorphism is found,
        we yield the mapping.

        """
    def semantic_feasibility(self, G1_node, G2_node):
        """Returns True if adding (G1_node, G2_node) is semantically feasible.

        The semantic feasibility function should return True if it is
        acceptable to add the candidate pair (G1_node, G2_node) to the current
        partial isomorphism mapping.   The logic should focus on semantic
        information contained in the edge data or a formalized node class.

        By acceptable, we mean that the subsequent mapping can still become a
        complete isomorphism mapping.  Thus, if adding the candidate pair
        definitely makes it so that the subsequent mapping cannot become a
        complete isomorphism mapping, then this function must return False.

        The default semantic feasibility function always returns True. The
        effect is that semantics are not considered in the matching of G1
        and G2.

        The semantic checks might differ based on the what type of test is
        being performed.  A keyword description of the test is stored in
        self.test.  Here is a quick description of the currently implemented
        tests::

          test='graph'
            Indicates that the graph matcher is looking for a graph-graph
            isomorphism.

          test='subgraph'
            Indicates that the graph matcher is looking for a subgraph-graph
            isomorphism such that a subgraph of G1 is isomorphic to G2.

          test='mono'
            Indicates that the graph matcher is looking for a subgraph-graph
            monomorphism such that a subgraph of G1 is monomorphic to G2.

        Any subclass which redefines semantic_feasibility() must maintain
        the above form to keep the match() method functional. Implementations
        should consider multigraphs.
        """
    def subgraph_is_isomorphic(self):
        """Returns True if a subgraph of G1 is isomorphic to G2."""
    def subgraph_is_monomorphic(self):
        """Returns True if a subgraph of G1 is monomorphic to G2."""
    def subgraph_isomorphisms_iter(self) -> Generator[Incomplete, Incomplete, None]:
        """Generator over isomorphisms between a subgraph of G1 and G2."""
    def subgraph_monomorphisms_iter(self) -> Generator[Incomplete, Incomplete, None]:
        """Generator over monomorphisms between a subgraph of G1 and G2."""
    def syntactic_feasibility(self, G1_node, G2_node):
        """Returns True if adding (G1_node, G2_node) is syntactically feasible.

        This function returns True if it is adding the candidate pair
        to the current partial isomorphism/monomorphism mapping is allowable.
        The addition is allowable if the inclusion of the candidate pair does
        not make it impossible for an isomorphism/monomorphism to be found.
        """

class DiGraphMatcher(GraphMatcher):
    """Implementation of VF2 algorithm for matching directed graphs.

    Suitable for DiGraph and MultiDiGraph instances.
    """
    def __init__(self, G1, G2) -> None:
        """Initialize DiGraphMatcher.

        G1 and G2 should be nx.Graph or nx.MultiGraph instances.

        Examples
        --------
        To create a GraphMatcher which checks for syntactic feasibility:

        >>> from networkx.algorithms import isomorphism
        >>> G1 = nx.DiGraph(nx.path_graph(4, create_using=nx.DiGraph()))
        >>> G2 = nx.DiGraph(nx.path_graph(4, create_using=nx.DiGraph()))
        >>> DiGM = isomorphism.DiGraphMatcher(G1, G2)
        """
    def candidate_pairs_iter(self) -> Generator[Incomplete, None, None]:
        """Iterator over candidate pairs of nodes in G1 and G2."""
    core_1: Incomplete
    core_2: Incomplete
    in_1: Incomplete
    in_2: Incomplete
    out_1: Incomplete
    out_2: Incomplete
    state: Incomplete
    mapping: Incomplete
    def initialize(self) -> None:
        """Reinitializes the state of the algorithm.

        This method should be redefined if using something other than DiGMState.
        If only subclassing GraphMatcher, a redefinition is not necessary.
        """
    def syntactic_feasibility(self, G1_node, G2_node):
        """Returns True if adding (G1_node, G2_node) is syntactically feasible.

        This function returns True if it is adding the candidate pair
        to the current partial isomorphism/monomorphism mapping is allowable.
        The addition is allowable if the inclusion of the candidate pair does
        not make it impossible for an isomorphism/monomorphism to be found.
        """

class GMState:
    """Internal representation of state for the GraphMatcher class.

    This class is used internally by the GraphMatcher class.  It is used
    only to store state specific data. There will be at most G2.order() of
    these objects in memory at a time, due to the depth-first search
    strategy employed by the VF2 algorithm.
    """
    GM: Incomplete
    G1_node: Incomplete
    G2_node: Incomplete
    depth: Incomplete
    def __init__(self, GM, G1_node: Incomplete | None = None, G2_node: Incomplete | None = None) -> None:
        """Initializes GMState object.

        Pass in the GraphMatcher to which this GMState belongs and the
        new node pair that will be added to the GraphMatcher's current
        isomorphism mapping.
        """
    def restore(self) -> None:
        """Deletes the GMState object and restores the class variables."""

class DiGMState:
    """Internal representation of state for the DiGraphMatcher class.

    This class is used internally by the DiGraphMatcher class.  It is used
    only to store state specific data. There will be at most G2.order() of
    these objects in memory at a time, due to the depth-first search
    strategy employed by the VF2 algorithm.

    """
    GM: Incomplete
    G1_node: Incomplete
    G2_node: Incomplete
    depth: Incomplete
    def __init__(self, GM, G1_node: Incomplete | None = None, G2_node: Incomplete | None = None) -> None:
        """Initializes DiGMState object.

        Pass in the DiGraphMatcher to which this DiGMState belongs and the
        new node pair that will be added to the GraphMatcher's current
        isomorphism mapping.
        """
    def restore(self) -> None:
        """Deletes the DiGMState object and restores the class variables."""
