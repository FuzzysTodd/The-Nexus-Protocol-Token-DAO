from _typeshed import Incomplete
from fusion_base import Fusion
from onnx_model import OnnxModel as OnnxModel
from typing import Dict

logger: Incomplete

class FusionQOrderedGelu(Fusion):
    def __init__(self, model: OnnxModel) -> None: ...
    def fuse(self, node, input_name_to_nodes: Dict, output_name_to_node: Dict):
        """
        INPUT PATTERN
        Fuse (quantized) Gelu subgraph into one node QOrderedGelu:
            -> quantized input  -> DQ -> Gelu -> Q ->

        (or)

            -> quantized input  -> DQ -> FastGelu -> Q ->

        OUTPUT PATTERN
            -> QOrderedGelu ->
        """
