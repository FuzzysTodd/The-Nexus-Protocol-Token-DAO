from _typeshed import Incomplete
from fusion_attention import AttentionMask as AttentionMask
from fusion_base import Fusion
from onnx import NodeProto as NodeProto
from onnx_model import OnnxModel as OnnxModel
from typing import Tuple

logger: Incomplete

class FusionQOrderedAttention(Fusion):
    hidden_size: Incomplete
    num_heads: Incomplete
    attention_mask: Incomplete
    def __init__(self, model: OnnxModel, hidden_size: int, num_heads: int, attention_mask: AttentionMask) -> None: ...
    num_heads_warning: bool
    hidden_size_warning: bool
    def get_num_heads_and_hidden_size(self, reshape_q: NodeProto) -> Tuple[int, int]:
        """Detect num_heads and hidden_size from a reshape node.
        Args:
            reshape_q (NodeProto): reshape node for Q
        Returns:
            Tuple[int, int]: num_heads and hidden_size
        """
    prune_graph: bool
    def fuse(self, normalize_node, input_name_to_nodes, output_name_to_node) -> None: ...
