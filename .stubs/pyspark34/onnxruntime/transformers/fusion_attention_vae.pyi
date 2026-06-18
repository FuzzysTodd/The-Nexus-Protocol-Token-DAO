from _typeshed import Incomplete
from fusion_base import Fusion
from onnx import NodeProto as NodeProto
from onnx_model import OnnxModel as OnnxModel
from typing import Tuple

logger: Incomplete

class FusionAttentionVae(Fusion):
    """
    Fuse Attention subgraph of Vae Decoder into one Attention node.
    """
    hidden_size: Incomplete
    num_heads: Incomplete
    num_heads_warning: bool
    hidden_size_warning: bool
    def __init__(self, model: OnnxModel, hidden_size: int, num_heads: int) -> None: ...
    def get_num_heads_and_hidden_size(self, reshape_q: NodeProto, add_q: NodeProto) -> Tuple[int, int]:
        """Detect num_heads and hidden_size from a reshape node.

        Args:
            reshape_q (NodeProto): reshape node for Q
            add_q (NodeProto): add node for Q

        Returns:
            Tuple[int, int]: num_heads and hidden_size
        """
    def create_attention_node(self, q_matmul: NodeProto, q_add: NodeProto, k_matmul: NodeProto, k_add: NodeProto, v_matmul: NodeProto, v_add: NodeProto, num_heads: int, hidden_size: int, input_name: str, output_name: str) -> NodeProto | None:
        """Create an Attention node.

        Args:
            q_matmul (NodeProto): MatMul node in fully connection for Q
            q_add (NodeProto): Add bias node in fully connection for Q
            k_matmul (NodeProto): MatMul node in fully connection for K
            k_add (NodeProto): Add bias node in fully connection for K
            v_matmul (NodeProto): MatMul node in fully connection for V
            v_add (NodeProto): Add bias node in fully connection for V
            num_heads (int): number of attention heads. If a model is pruned, it is the number of heads after pruning.
            hidden_size (int): hidden dimension. If a model is pruned, it is the hidden dimension after pruning.
            input_name (str): input name
            output_name (str): output name

        Returns:
            Union[NodeProto, None]: the node created or None if failed.
        """
    prune_graph: bool
    def fuse(self, softmax_node, input_name_to_nodes, output_name_to_node) -> None: ...
