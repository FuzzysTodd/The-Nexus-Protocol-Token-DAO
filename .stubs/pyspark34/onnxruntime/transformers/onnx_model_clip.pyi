from _typeshed import Incomplete
from onnx import ModelProto as ModelProto
from onnx_model_unet import UnetOnnxModel

logger: Incomplete

class ClipOnnxModel(UnetOnnxModel):
    def __init__(self, model: ModelProto, num_heads: int = 0, hidden_size: int = 0) -> None: ...
    def get_fused_operator_statistics(self):
        """
        Returns node count of fused operators.
        """
