from _typeshed import Incomplete
from fusion_base import Fusion
from onnx_model import OnnxModel as OnnxModel
from typing import Dict

logger: Incomplete

class FusionQOrderedLayerNormalization(Fusion):
    def __init__(self, model: OnnxModel) -> None: ...
    def fuse(self, node, input_name_to_nodes: Dict, output_name_to_node: Dict):
        """
        Fuse (quantized) Layer Normalization subgraph into one node QOrderedLayerNormalization:
            quantized input  -> DQ
                                |
                                |
            (other inputs)-> LayerNormalization --> Q -->

            should become

            (quantized input + other inputs)->  QOrderedLayerNormalization --> Q -->
        """
