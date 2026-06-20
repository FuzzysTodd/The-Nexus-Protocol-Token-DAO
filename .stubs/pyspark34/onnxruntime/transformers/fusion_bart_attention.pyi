from _typeshed import Incomplete
from fusion_attention import AttentionMask as AttentionMask, FusionAttention
from onnx_model import OnnxModel as OnnxModel

logger: Incomplete

class FusionBartAttention(FusionAttention):
    """
    Fuse Bart Attention subgraph into one Attention node.
    """
    def __init__(self, model: OnnxModel, hidden_size: int, num_heads: int, attention_mask: AttentionMask) -> None: ...
    def check_runtime_shape_path(self, reshape_qkv_2, reshape_qkv_1, reshape_q_2, reshape_k_2, reshape_v_2, root_input): ...
    use_multi_head_attention: bool
    prune_graph: bool
    def fuse(self, normalize_node, input_name_to_nodes, output_name_to_node): ...
