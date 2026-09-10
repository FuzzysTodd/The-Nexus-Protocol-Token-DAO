from _typeshed import Incomplete
from onnx import NodeProto as NodeProto
from onnx_model import OnnxModel as OnnxModel
from typing import Dict, List

logger: Incomplete

class Fusion:
    """
    Base class for Graph Fusion
    """
    search_op_types: Incomplete
    fused_op_type: Incomplete
    description: Incomplete
    model: Incomplete
    nodes_to_remove: Incomplete
    nodes_to_add: Incomplete
    prune_graph: bool
    node_name_to_graph_name: Incomplete
    this_graph_name: Incomplete
    fused_count: Incomplete
    def __init__(self, model: OnnxModel, fused_op_type: str, search_op_types: str | List[str], description: str = '') -> None: ...
    def increase_counter(self, fused_op_name: str):
        """
        Increase counter of a fused operator.
        """
    def fuse(self, node: NodeProto, input_name_to_nodes: Dict[str, List[NodeProto]], output_name_to_node: Dict[str, NodeProto]):
        """Interface for fusion that starts from a node"""
    def apply(self) -> None:
        """
        Apply graph fusion on the whole model graph.
        It searched nodes of given operators, and start fusion on each of those nodes.
        """
