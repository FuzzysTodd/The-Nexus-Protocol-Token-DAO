from _typeshed import Incomplete
from fusion_base import Fusion
from onnx_model import OnnxModel as OnnxModel
from typing import List

logger: Incomplete

class FusionNhwcConv(Fusion):
    """Convert Conv to NhwcConv"""
    update_weight: Incomplete
    def __init__(self, model: OnnxModel, update_weight: bool = False) -> None: ...
    def create_transpose_node(self, input_name: str, perm: List[int], output_name: Incomplete | None = None):
        """Append a Transpose node after an input"""
    def fuse(self, conv, input_name_to_nodes, output_name_to_node) -> None: ...
