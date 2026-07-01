from _typeshed import Incomplete
from fusion_base import Fusion
from onnx_model import OnnxModel as OnnxModel
from typing import Dict

logger: Incomplete

class FusionBiasAdd(Fusion):
    def __init__(self, model: OnnxModel) -> None: ...
    def fuse(self, add_node, input_name_to_nodes: Dict, output_name_to_node: Dict):
        """
        Fuse Add bias and Add skip connection into BiasAdd
        """
