from _typeshed import Incomplete
from fusion_base import Fusion
from onnx_model import OnnxModel as OnnxModel
from typing import Dict

logger: Incomplete

class FusionBiasSplitGelu(Fusion):
    def __init__(self, model: OnnxModel) -> None: ...
    def fuse(self, gelu_node, input_name_to_nodes: Dict, output_name_to_node: Dict):
        """
        [root] --->Add -------------------->  Slice ---------------> Mul -->
                   |                            ^                    ^
                   |                            |                    |
                   +----------------------------+---Slice --> Gelu---+
                   |                            |     ^
                   |                            |-----|
                   |                            |     |
                   |                           Mul   Mul
                   |                            ^     ^
                   v                            |     |
                  Shape ---> Gather --> Add --> Div --+
        """
