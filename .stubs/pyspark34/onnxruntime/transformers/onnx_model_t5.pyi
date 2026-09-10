from _typeshed import Incomplete
from fusion_attention import AttentionMask, FusionAttention
from fusion_base import Fusion
from fusion_skiplayernorm import FusionSkipLayerNormalization
from onnx import NodeProto as NodeProto
from onnx_model import OnnxModel as OnnxModel
from onnx_model_bert import BertOnnxModel
from typing import Dict

logger: Incomplete

class FusionT5Attention(FusionAttention):
    """
    Fuse T5 Attention subgraph into one Attention node.
    """
    static_kv: int
    def __init__(self, model: OnnxModel, hidden_size: int, num_heads: int, attention_mask: AttentionMask) -> None: ...
    def create_attention_node(self, mask_index: str, q_matmul: NodeProto, k_matmul: NodeProto, v_matmul: NodeProto, num_heads: int, hidden_size: int, input: str, output: str, add_qk_str: str, scale: float | None = None) -> NodeProto | None:
        """Create an Attention node.
        Args:
            mask_index (str): mask input
            q_matmul (NodeProto): MatMul node in fully connection for Q
            k_matmul (NodeProto): MatMul node in fully connection for  K
            v_matmul (NodeProto): MatMul node in fully connection for  V
            num_heads (int): number of attention heads. If a model is pruned, it is the number of heads after pruning.
            hidden_size (int): hidden dimension. If a model is pruned, it is the hidden dimension after pruning.
            input (str): input name
            output (str): output name
        Returns:
            Union[NodeProto, None]: the node created or None if failed.
        """
    def create_mha_node(self, query: str, key: str, value: str, mask_index: str, res_pos_bias: str, past_key: str, past_value: str, output: str, present_key: str, present_value: str, num_heads: int, hidden_size: int) -> NodeProto | None: ...
    def fuse(self, normalize_node, input_name_to_nodes, output_name_to_node) -> None: ...
    mask_filter_value: Incomplete
    prune_graph: bool
    def fuse_t5_encoder(self, normalize_node, input_name_to_nodes, output_name_to_node) -> None: ...
    def fuse_t5_decoder(self, normalize_node, input_name_to_nodes, output_name_to_node) -> None: ...

class FusionRelativePositionBiasBlock(Fusion):
    max_distance: Incomplete
    is_bidirectional: bool
    def __init__(self, model: OnnxModel, max_distance: int) -> None: ...
    def fuse(self, node, input_name_to_nodes, output_name_to_node) -> None: ...

class FusionSimplifiedLayerNormalization(Fusion):
    def __init__(self, model: OnnxModel) -> None: ...
    def fuse(self, node, input_name_to_nodes: Dict, output_name_to_node: Dict): ...

class FusionSkipSimplifiedLayerNormalization(FusionSkipLayerNormalization):
    def __init__(self, model: OnnxModel) -> None: ...
    def fuse(self, node, input_name_to_nodes, output_name_to_node) -> None: ...

class T5OnnxModel(BertOnnxModel):
    attention_mask: Incomplete
    attention_fusion: Incomplete
    layer_norm_fusion: Incomplete
    skip_layer_norm_fusion: Incomplete
    rpb_fusion: Incomplete
    def __init__(self, model, num_heads, hidden_size) -> None: ...
    def fuse_attention(self) -> None: ...
    def fuse_layer_norm(self) -> None: ...
    def fuse_skip_layer_norm(self) -> None: ...
    def remove_extended_mask_decoder_init(self) -> None: ...
    def remove_extended_mask_decoder(self) -> None: ...
    def preprocess(self) -> None: ...
    def postprocess(self) -> None: ...
