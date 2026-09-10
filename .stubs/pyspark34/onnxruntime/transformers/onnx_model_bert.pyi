from _typeshed import Incomplete
from fusion_options import FusionOptions as FusionOptions
from onnx import GraphProto, ModelProto as ModelProto, ValueInfoProto
from onnx_model import OnnxModel
from typing import List

logger: Incomplete

class BertOnnxModel(OnnxModel):
    num_heads: Incomplete
    hidden_size: Incomplete
    attention_mask: Incomplete
    attention_fusion: Incomplete
    qordered_attention_fusion: Incomplete
    utils: Incomplete
    def __init__(self, model: ModelProto, num_heads: int = 0, hidden_size: int = 0) -> None:
        """Initialize BERT ONNX Model.

        Args:
            model (ModelProto): the ONNX model
            num_heads (int, optional): number of attention heads. Defaults to 0 (detect the parameter automatically).
            hidden_size (int, optional): hidden dimension. Defaults to 0 (detect the parameter automatically).
        """
    def fuse_attention(self) -> None: ...
    def fuse_gelu(self) -> None: ...
    def fuse_bias_gelu(self, is_fastgelu) -> None: ...
    def gelu_approximation(self) -> None: ...
    def fuse_gemm_fast_gelu(self) -> None: ...
    def fuse_add_bias_skip_layer_norm(self) -> None: ...
    def fuse_reshape(self) -> None: ...
    def fuse_shape(self) -> None: ...
    def fuse_embed_layer(self, use_mask_index) -> None: ...
    def fuse_layer_norm(self) -> None: ...
    def fuse_skip_layer_norm(self) -> None: ...
    def fuse_qordered_mamtul(self) -> None: ...
    def get_graph_inputs_from_node_type(self, op_type: str, input_indices: List[int], casted: bool):
        """
        Get graph inputs that feed into node type (like EmbedLayerNormalization or Attention).
        Returns a list of the graph input names based on the filter whether it is casted or not.
        """
    def get_graph_inputs_from_fused_nodes(self, casted: bool): ...
    def change_graph_input_type(self, graph: GraphProto, graph_input: ValueInfoProto, new_type: int = ...):
        """Change graph input type, and add Cast node if needed.

        Args:
            graph (GraphProto): graph
            graph_input (TensorProto): input of the graph
            new_type (int, optional): new data type. Defaults to TensorProto.INT32.

        Returns:
            NodeProto: a new Cast node that added. None if Cast node is not added.
            List[NodeProto]: Cast nodes that have been removed.
        """
    def change_graph_inputs_to_int32(self) -> None:
        """Change data type of all graph inputs to int32 type, and add Cast node if needed."""
    def use_dynamic_axes(self, dynamic_batch_dim: str = 'batch_size', dynamic_seq_len: str = 'max_seq_len') -> None:
        """
        Update input and output shape to use dynamic axes.
        """
    def preprocess(self) -> None: ...
    def adjust_reshape_and_expand(self) -> None: ...
    def clean_graph(self) -> None: ...
    def postprocess(self) -> None: ...
    def optimize(self, options: FusionOptions | None = None, add_dynamic_axes: bool = False): ...
    def get_fused_operator_statistics(self):
        """
        Returns node count of fused operators.
        """
    def is_fully_optimized(self):
        """
        Returns True when the model is fully optimized.
        """
    def convert_to_packing_mode(self, use_symbolic_shape_infer: bool = False): ...
