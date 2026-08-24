from .ns_types import NSNodeTargetType as NSNodeTargetType, NSSingleResultValuesType as NSSingleResultValuesType, NSSubgraph as NSSubgraph
from .utils import NodeInputOrOutputType as NodeInputOrOutputType, get_arg_indices_of_inputs_to_log as get_arg_indices_of_inputs_to_log, get_node_first_input_and_output_type as get_node_first_input_and_output_type, get_node_input_qparams as get_node_input_qparams, get_normalized_nth_input as get_normalized_nth_input, get_number_of_non_param_args as get_number_of_non_param_args, get_target_type_str as get_target_type_str, getattr_from_fqn as getattr_from_fqn, op_type_supports_shadowing as op_type_supports_shadowing, return_first_non_observer_node as return_first_non_observer_node
from torch.ao.ns.fx.mappings import get_node_type_to_io_type_map as get_node_type_to_io_type_map
from torch.ao.quantization.fx.utils import get_new_attr_name_with_prefix as get_new_attr_name_with_prefix
from torch.fx import GraphModule as GraphModule, map_arg as map_arg
from torch.fx.graph import Graph as Graph, Node as Node
from typing import Callable, Dict, Set, Tuple

def add_loggers_to_model(gm: GraphModule, node_to_instrument_inputs_to_ref_node_name: Dict[Node, Tuple[str, str]], node_to_instrument_outputs_to_ref_node_name: Dict[Node, Tuple[str, str]], logger_cls: Callable, model_name: str) -> GraphModule:
    """
    Takes the graph of gm, adds loggers to the output
    of each node in nodes_to_instrument. Returns a GraphModule with the new
    graph.
    """
def create_a_shadows_b(name_a: str, gm_a: GraphModule, name_b: str, gm_b: GraphModule, matched_subgraph_pairs: Dict[str, Tuple[NSSubgraph, NSSubgraph]], logger_cls: Callable, should_log_inputs: bool, node_type_to_io_type_map: Dict[str, Set[NSNodeTargetType]] | None = None) -> GraphModule:
    """
    Creates a new GraphModule consisting of the graph of C, with the meaningful
    nodes of A shadowing the corresponding nodes of B.  For example,

    Graph A:
    a0 -> op0_fp32 -> a1 -> op1_fp32 -> a2

    Graph B:
    b0 -> op0_int8 -> b1 -> op1_int8 -> b2

    matched_node_pairs: {'op0': (op0_fp32, op0_int8), 'op1': (op1_fp32, op1_int8)}

    Graph C (A shadows B):

        / dequant0 -> op0_fp32 -> logger_a_0  / dequant_1 -> op1_fp32 -> logger_a_1
       /                                     /
    b0 -------------> op0_int8 -> logger_b_0 --------------> op1_int8 -> logger_b_1

    In a nutshell, this function does the following for each node pair:
    * copies the necessary attributes and modules from gm_a to gm_b,
      keeping names unique
    * adds a dtype cast op (dequant, quant, etc)
    * adds a copy of node_a in gm_b's graph
    * adds loggers to the outputs of node_a and node_b
    """
