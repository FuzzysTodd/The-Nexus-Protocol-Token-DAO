from _typeshed import Incomplete
from fusion_base import Fusion
from onnx import NodeProto as NodeProto
from onnx_model import OnnxModel as OnnxModel
from typing import Tuple

logger: Incomplete

class FusionAttentionUnet(Fusion):
    """
    Fuse Attention subgraph of UNet into one Attention node.
    """
    hidden_size: Incomplete
    num_heads: Incomplete
    is_cross_attention: Incomplete
    enable_packed_qkv: Incomplete
    enable_packed_kv: Incomplete
    num_heads_warning: bool
    hidden_size_warning: bool
    def __init__(self, model: OnnxModel, hidden_size: int, num_heads: int, is_cross_attention: bool, enable_packed_qkv: bool, enable_packed_kv: bool) -> None: ...
    def get_num_heads(self, reshape_q: NodeProto, is_torch2: bool = False) -> int:
        """Detect num_heads from a reshape node.

        Args:
            reshape_q (NodeProto): reshape node for Q
            is_torch2 (bool): graph pattern is from PyTorch 2.*
        Returns:
            int: num_heads, or 0 if not found
        """
    def get_hidden_size(self, layernorm_node):
        """Detect hidden_size from LayerNormalization node.
        Args:
            layernorm_node (NodeProto): LayerNormalization node before Q, K and V
        Returns:
            int: hidden_size, or 0 if not found
        """
    def get_num_heads_and_hidden_size(self, reshape_q: NodeProto, layernorm_node: NodeProto, is_torch2: bool = False) -> Tuple[int, int]:
        """Detect num_heads and hidden_size.

        Args:
            reshape_q (NodeProto): reshape node for Q
            is_torch2 (bool): graph pattern is from PyTorch 2.*
            layernorm_node (NodeProto): LayerNormalization node before Q, K, V
        Returns:
            Tuple[int, int]: num_heads and hidden_size
        """
    def create_attention_node(self, q_matmul: NodeProto, k_matmul: NodeProto, v_matmul: NodeProto, num_heads: int, hidden_size: int, input: str, output: str) -> NodeProto | None:
        """Create an Attention node.

        Args:
            q_matmul (NodeProto): MatMul node in fully connection for Q
            k_matmul (NodeProto): MatMul node in fully connection for K
            v_matmul (NodeProto): MatMul node in fully connection for V
            num_heads (int): number of attention heads. If a model is pruned, it is the number of heads after pruning.
            hidden_size (int): hidden dimension. If a model is pruned, it is the hidden dimension after pruning.
            input (str): input name
            output (str): output name

        Returns:
            Union[NodeProto, None]: the node created or None if failed.
        """
    prune_graph: bool
    def fuse(self, normalize_node, input_name_to_nodes, output_name_to_node) -> None: ...
    def match_qkv_torch1(self, root_input, skip_add):
        """Match Q, K and V paths exported by PyTorch 1.*"""
    def match_qkv_torch2(self, root_input, skip_add):
        """Match Q, K and V paths exported by PyTorch 2.*"""
