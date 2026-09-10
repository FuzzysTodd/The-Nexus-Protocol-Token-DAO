from _typeshed import Incomplete
from fusion_base import Fusion
from fusion_options import AttentionMaskFormat
from onnx import NodeProto
from onnx_model import OnnxModel as OnnxModel
from typing import List, Tuple

logger: Incomplete

class AttentionMask:
    """
    Fuse Attention subgraph into one Attention node.
    """
    model: Incomplete
    mask_indice: Incomplete
    mask_casted: Incomplete
    utils: Incomplete
    mask_format: Incomplete
    opset_version: Incomplete
    def __init__(self, model: OnnxModel) -> None: ...
    def set_mask_format(self, mask_format: AttentionMaskFormat): ...
    def set_mask_indice(self, mask, mask_index) -> None: ...
    def get_first_mask(self): ...
    def process_mask(self, input: str) -> str: ...

class FusionAttention(Fusion):
    """
    Fuse Attention subgraph into one Attention node.
    """
    hidden_size: Incomplete
    num_heads: Incomplete
    attention_mask: Incomplete
    use_multi_head_attention: Incomplete
    disable_multi_head_attention_bias: Incomplete
    mask_filter_value: Incomplete
    num_heads_warning: bool
    hidden_size_warning: bool
    def __init__(self, model: OnnxModel, hidden_size: int, num_heads: int, attention_mask: AttentionMask, use_multi_head_attention: bool = False, disable_multi_head_attention_bias: bool = False, search_op_types: List[str] = ['SkipLayerNormalization', 'LayerNormalization']) -> None: ...
    def get_num_heads_and_hidden_size_from_concat(self, concat: NodeProto) -> Tuple[int, int]:
        """
        Detect num_heads and hidden_size from Concat node in the following subgraph:

        SkipLayerNormalization or EmbedLayerNormalization
                        /        |
                     MatMul    Shape
                        |        |
                       Add     Gather(indices=0)
                        |        |
                        |      Unsqueeze
                        |        |
                        |     Concat (*, -1, 12, 64)
                        |     /
                       Reshape
                          |
                       Transpose
        """
    def get_num_heads_and_hidden_size(self, reshape_q: NodeProto) -> Tuple[int, int]:
        """Detect num_heads and hidden_size from a reshape node.

        Args:
            reshape_q (NodeProto): reshape node for Q

        Returns:
            Tuple[int, int]: num_heads and hidden_size
        """
    def get_add_qk_str(self, add_qk: NodeProto): ...
    def concat_kv(self, past_k: str, past_v: str) -> str:
        """Concatenate past_k and past_v inputs to create past_kv input.

        Args:
            past_k (str): name of past K value
            past_v (str): name of past V value

        Returns:
            kv_output_name (str): name of past KV value
        """
    def reshape_kv(self, past_k: str, past_v: str) -> tuple[str, str]:
        """Reshape past_k and past_v from 4D to 3D to use as inputs for multihead attention node.

        Args:
            past_k (str): name of past K value of shape 4D
            past_v (str): name of past V value of shape 4D

        Returns:
            k_3d (str): name of past K value of shape 3D
            v_3d (str): name of past V value of shape 3D
        """
    def split_kv(self, present_k_name: str, present_v_name: str, kv_node: str):
        """Split kv_node containing present KV values into separate present K and present V values.

        Args:
            present_k_name (str): name of output to store present K value in
            present_v_name (str): name of output to store present V value in
            kv_node (str): name of present KV values
        """
    def transpose_kv(self, past_k: str, past_v: str):
        """Transpose past_k and past_v from (B,N,P,H) to (B,P,N,H)

        Args:
            past_k (str): name of past K value of shape (B,N,P,H)
            past_v (str): name of past V value of shape (B,N,P,H)

        Returns:
            past_k_transpose (str): name of past K value of shape (B,P,N,H)
            past_v_transpose (str): name of past V value of shape (B,P,N,H)
        """
    def create_combined_qkv_bias(self, q_add: NodeProto, k_add: NodeProto | None, v_add: NodeProto | None, name_prefix: str) -> NodeProto | None: ...
    def create_packed_qkv_matmul_node(self, q_matmul: NodeProto, k_matmul: NodeProto, v_matmul: NodeProto, q_add: NodeProto, k_add: NodeProto | None, v_add: NodeProto | None, num_heads: int) -> NodeProto | None:
        """Create packed QKV MatMul node before MultiHeadAttention node.
           This is for the scenario where an Attention node should be created but cannot be created
           because past_key and past_value are separate inputs and not one concatenated input.

        Args:
            q_matmul (NodeProto): name of MatMul from Q path - (batch_size, sequence_length, hidden_size)
            k_matmul (NodeProto): name of MatMul from K path - (batch_size, sequence_length, hidden_size)
            v_matmul (NodeProto): name of MatMul from V path - (batch_size, sequence_length, hidden_size)
            q_add (NodeProto): name of Add from Q path
            k_add (NodeProto): name of Add from K path
            v_add (NodeProto): name of Add from V path
            num_heads (int): number of heads

        Returns:
            Union[NodeProto, None]: the node created or None if failed.
        """
    def create_multihead_attention_node(self, q_matmul: NodeProto, k_matmul: NodeProto | str | None, v_matmul: NodeProto | str | None, q_add: NodeProto, k_add: NodeProto | None, v_add: NodeProto | None, num_heads: int, hidden_size: int, output: str, key_padding_mask: str = '', add_qk: str = '', past_k: str = '', past_v: str = '', present_k: str = '', present_v: str = '', packed_qkv: bool = False) -> NodeProto | None:
        """Create a MultiHeadAttention node.

        Args:
            q_matmul (NodeProto): name of MatMul from Q path - (batch_size, sequence_length, hidden_size)
            k_matmul (NodeProto): name of MatMul from K path - (batch_size, sequence_length, hidden_size) or (batch_size, num_heads, past_sequence_length, head_size)
            v_matmul (NodeProto): name of MatMul from V path - (batch_size, sequence_length, hidden_size) or (batch_size, num_heads, past_sequence_length, head_size)
            q_add (NodeProto): name of Add from Q path
            k_add (NodeProto): name of Add from K path
            v_add (NodeProto): name of Add from V path
            num_heads (int): number of attention heads. If a model is pruned, it is the number of heads after pruning.
            hidden_size (int): hidden dimension. If a model is pruned, it is the hidden dimension after pruning.
            output (str): output name of MHA
            key_padding_mask (str): name of key padding mask
            add_qk (str): name of add after Q x K'
            past_k (str): name of past K value - (batch_size, num_heads, past_sequence_length, head_size)
            past_v (str): name of past V value - (batch_size, num_heads, past_sequence_length, head_size)
            present_k (str): name of present K value - (batch_size, num_heads, sequence_length, head_size)
            present_v (str): name of present V value - (batch_size, num_heads, sequence_length, head_size)
            packed_qkv (bool): whether to combine MatMuls from Q, K, V paths
                               Note: This is for the scenario where an Attention node should be created but cannot be created
                               because past_key and past_value are separate inputs and not one concatenated input.

        Returns:
            Union[NodeProto, None]: the node created or None if failed.
        """
    def create_attention_node(self, mask_index: str, q_matmul: NodeProto, k_matmul: NodeProto, v_matmul: NodeProto, q_add: NodeProto, k_add: NodeProto, v_add: NodeProto, num_heads: int, hidden_size: int, input: str, output: str, add_qk_str: str = '', past_k: str = '', past_v: str = '', present_k: str = '', present_v: str = '', scale: float | None = None) -> NodeProto | None:
        """Create an Attention node.

        Args:
            mask_index (str): mask input
            q_matmul (NodeProto): MatMul node in fully connection for Q
            k_matmul (NodeProto): MatMul node in fully connection for K
            v_matmul (NodeProto): MatMul node in fully connection for V
            q_add (NodeProto): Add bias node in fully connection for Q
            k_add (NodeProto): Add bias node in fully connection for K
            v_add (NodeProto): Add bias node in fully connection for V
            num_heads (int): number of attention heads. If a model is pruned, it is the number of heads after pruning.
            hidden_size (int): hidden dimension. If a model is pruned, it is the hidden dimension after pruning.
            input (str): input name
            output (str): output name
            add_qk_str (str): name of Add node after Q x K'
            past_k (str): name of input for past K value
            past_v (str): name of input for past V value
            present_k (str): name of output to store present K value
            present_v (str): name of output to store present V value

        Returns:
            Union[NodeProto, None]: the node created or None if failed.
        """
    prune_graph: bool
    def fuse(self, normalize_node, input_name_to_nodes, output_name_to_node) -> None: ...
