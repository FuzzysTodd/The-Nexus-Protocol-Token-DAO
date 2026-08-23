import enum
from .mappings import get_base_name_to_sets_of_related_ops as get_base_name_to_sets_of_related_ops, get_unmatchable_types_map as get_unmatchable_types_map
from .ns_types import NSNodeTargetType as NSNodeTargetType, NSSubgraph as NSSubgraph
from .pattern_utils import end_node_matches_reversed_fusion as end_node_matches_reversed_fusion, get_reversed_fusions as get_reversed_fusions, get_type_a_related_to_b as get_type_a_related_to_b
from _typeshed import Incomplete
from torch.ao.quantization import FakeQuantizeBase as FakeQuantizeBase, ObserverBase as ObserverBase
from torch.ao.quantization.utils import getattr_from_fqn as getattr_from_fqn
from torch.fx import GraphModule as GraphModule
from torch.fx.graph import Graph as Graph, Node as Node
from typing import Dict, Set, Tuple

toq: Incomplete

class _NSGraphMatchableSubgraphsIterator:
    """
    Iterates through the graph of gm, starting with the output nodes
    and continuing backwards.
    1. Returns matchable subgraphs, in order. A subgraph is defined by
       (start_node, end_node).
    2. Skips over non-matchable subgraphs
    """
    gm: Incomplete
    non_matchable_functions: Incomplete
    non_matchable_modules: Incomplete
    non_matchable_methods: Incomplete
    seen_nodes: Incomplete
    stack: Incomplete
    def __init__(self, gm: GraphModule, non_matchable_functions: Set[NSNodeTargetType], non_matchable_modules: Set[NSNodeTargetType], non_matchable_methods: Set[NSNodeTargetType]) -> None: ...
    def __iter__(self): ...
    def __next__(self) -> NSSubgraph:
        """
        Returns the next matchable subgraph.
        """

class GraphMatchingException(Exception):
    """
    Exception raised when two graphs cannot be matched.
    """

class SubgraphTypeRelationship(enum.Enum):
    EQUAL: Incomplete
    EQUAL_BUT_UKNOWN: Incomplete
    RELATED_BUT_NOT_EQUAL: Incomplete
    NOT_RELATED: Incomplete

def get_matching_subgraph_pairs(gm_a: GraphModule, gm_b: GraphModule, base_name_to_sets_of_related_ops: Dict[str, Set[NSNodeTargetType]] | None = None, unmatchable_types_map: Dict[str, Set[NSNodeTargetType]] | None = None) -> Dict[str, Tuple[NSSubgraph, NSSubgraph]]:
    '''
    Matches matchable subgraphs of graph_a to graph_b.

    For a node, "matchable" is defined as a node which is not an observer,
    fake_quants, quant or dequant.

    A subgraph can contain one or more nodes.  A subgraph is matchable if
    at least one node inside of it is matchable.  Currently, all nodes in
    a subgraph must be matchable (because we assume no observers will be
    inserted in the middle of a fusion).

    A subgraph is defined by (start_node, end_node).  We assume that only
    start_node and end_node are linked with the surrounding graph, all other
    nodes in a subgraph are self-contained.

    A pair of nodes is "related" if both nodes represent the same mathematical
    operation across different quantization flavors. For example,
    `F.linear` and `torch.ops.quantized.linear` are related, and
    `F.linear` and `torch.nn.Conv` are not related.

    For each matchable pair of nodes node_a and node_b, they will match
    if node_a and node_b are related.

    For graphs A and B, they will match iff:
    1. the number of matchable subgraphs in A and B is equivalent
    2. when iterating through the matchable subgraphs of A and B in the same order, each
       corresponding pair of base nodes is related.

    This enables us to find the corresponding subgraphs between
    graphs of related models.  For example, if we had two graphs such as:

    graph_a: x0 -> conv_0 (type: nn.Conv2d) -> obs_0 -> x1
             w  -/
             b  -/

    graph_b: x0 -> quant_0 -> qconv_0 (type: nnq.Conv2d) -> dequant_0 -> x1
           packed_params_0 -/

    This function will return the following result:
    {
        \'conv_0\': (  # the name of the node in graph_b
          (conv_0, conv_0),  # (start_node_a, end_node_a)
          (qconv_0, qconv_0),  # (start_node_b, end_node_b)
        ),
    }

    Or, if we have a fusion pattern,

    graph_a: x0 -> linear_0 -> relu_0 -> obs_0 -> x1
             w  -/
             b  -/

    graph_b: x0 -> quant_0 -> linear_relu_0 -> dequant_0 -> x1
           packed_params_0 -/

    This function will return the following result:
    {
        \'linear_relu_0\': (  # the name of the node in graph_b
          (linear_0, relu_0),  # (start_node_a, end_node_a)
          (linear_relu_0, linear_relu_0),  # (start_node_b, end_node_b)
        ),
    }
    '''
