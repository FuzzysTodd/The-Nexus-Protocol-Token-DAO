import torch
import torch.nn as nn
from ..qconfig import QConfigAny as QConfigAny
from ..quantization_mappings import get_quantized_operator as get_quantized_operator
from .utils import collect_producer_nodes as collect_producer_nodes, create_node_from_old_node_preserve_meta as create_node_from_old_node_preserve_meta, get_linear_prepack_op_for_dtype as get_linear_prepack_op_for_dtype, get_new_attr_name_with_prefix as get_new_attr_name_with_prefix, get_qconv_prepack_op as get_qconv_prepack_op, graph_module_from_producer_nodes as graph_module_from_producer_nodes
from _typeshed import Incomplete
from torch.ao.nn.quantized.modules.utils import WeightedQuantizedModule as WeightedQuantizedModule
from torch.fx import GraphModule as GraphModule, Node as Node, map_arg as map_arg
from torch.fx.graph import Graph as Graph
from typing import Callable, Dict, Set, Tuple, Type

QOP_TO_ARG_NAMES_TO_SKIP: Incomplete

def is_fixed_qparams_node(node, modules): ...
def is_default_node(node, modules): ...
def is_copy_node(node, modules): ...
def is_general_tensor_shape_node(node, modules): ...
def is_other_node(node, modules): ...
def is_special_pattern_node(node, modules): ...
def is_dequantize_node(node): ...
def is_getattr_tensor_metadata_node(node): ...
def is_get_tensor_info_node(node): ...
def should_skip_lowering(op: torch.fx.node.Node, qconfig_map: Dict[str, QConfigAny]):
    """
    Return True if the op is configured with a None qconfig, False otherwise.
    Note: maybe need to generalize this to also check for the dtype, and we
    only lower when dtype matches, but right now fbgemm/qnnpack only support
    a single dtype, so it is OK for now.
    """

STATIC_LOWER_MODULE_MAP: Dict[Type[nn.Module], Type[WeightedQuantizedModule]]
DYNAMIC_LOWER_MODULE_MAP: Dict[Type[nn.Module], Type[nn.Module]]
WEIGHT_ONLY_LOWER_MODULE_MAP: Dict[Type[nn.Module], Type[nn.Module]]
SPECIAL_PATTERN_LOWER_MODULE_MAP: Incomplete
STATIC_LOWER_FUSED_MODULE_MAP: Dict[Type[nn.Module], Tuple[Type[nn.Module], Type[WeightedQuantizedModule]]]
STATIC_LOWER_FUSED_MODULE_TWO_INPUTS_MAP: Dict[Type[nn.Module], Tuple[Type[nn.Module], Type[WeightedQuantizedModule]]]
DYNAMIC_LOWER_FUSED_MODULE_MAP: Dict[Type[nn.Module], Tuple[Type[nn.Module], Type[nn.Module]]]
STATIC_LOWER_FUNCTIONAL_MAP: Dict[Callable, Tuple[Callable, Callable]]
WEIGHT_PREPACK_OPS: Set[Callable]
DYNAMIC_LOWER_FUNCTIONAL_MAP: Dict[Callable, Dict[Tuple[torch.dtype, torch.dtype], Tuple[Callable, Callable | None]]]
CONV_FUNCTIONAL_OPS: Set[Callable]
QBIN_OP_MAPPING: Dict[Callable | str, Callable]
QBIN_RELU_OP_MAPPING: Dict[Callable | str, Callable]

def fold_weight(quantized_model: GraphModule, node_name_to_scope: Dict[str, Tuple[str, type]]) -> GraphModule:
    """
    Trace back from the weight node util we hit getattr, reconstruct the
    graph module with the traced nodes and run the graph module to pack the
    weight. then replace the original chain of ops with the packed weight.
    """
def special_pattern_replacement(model: GraphModule): ...
