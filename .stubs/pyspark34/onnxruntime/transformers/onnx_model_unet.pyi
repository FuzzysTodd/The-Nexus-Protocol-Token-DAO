from _typeshed import Incomplete
from fusion_options import FusionOptions as FusionOptions
from onnx import ModelProto as ModelProto
from onnx_model_bert import BertOnnxModel

logger: Incomplete

class UnetOnnxModel(BertOnnxModel):
    def __init__(self, model: ModelProto, num_heads: int = 0, hidden_size: int = 0) -> None:
        """Initialize UNet ONNX Model.

        Args:
            model (ModelProto): the ONNX model
            num_heads (int, optional): number of attention heads. Defaults to 0 (detect the parameter automatically).
            hidden_size (int, optional): hidden dimension. Defaults to 0 (detect the parameter automatically).
        """
    def preprocess(self) -> None: ...
    def postprocess(self) -> None: ...
    def remove_useless_div(self) -> None:
        """Remove Div by 1"""
    def convert_conv_to_nhwc(self) -> None: ...
    def merge_adjacent_transpose(self) -> None: ...
    def fuse_multi_head_attention(self, options: FusionOptions | None = None): ...
    def fuse_bias_add(self) -> None: ...
    def optimize(self, options: FusionOptions | None = None): ...
    def get_fused_operator_statistics(self):
        """
        Returns node count of fused operators.
        """
