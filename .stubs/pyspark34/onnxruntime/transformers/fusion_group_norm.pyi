from _typeshed import Incomplete
from fusion_base import Fusion
from onnx_model import OnnxModel as OnnxModel
from typing import Dict

logger: Incomplete

class FusionGroupNorm(Fusion):
    channels_last: Incomplete
    def __init__(self, model: OnnxModel, channels_last: bool = True) -> None: ...
    prune_graph: bool
    def fuse(self, add_node, input_name_to_nodes: Dict, output_name_to_node: Dict):
        """
         Fuse Group Normalization subgraph into one node GroupNorm.
         The following is the pattern with swish activation:
               +----------------Shape-------------------------------+
               |                                                    |
               |    (0, 32, -1)                                     v     (512x1x1) (512x1x1) (optional)
           [Root] --> Reshape -------> InstanceNormalization --> Reshape ---> Mul --> Add --> Mul--> [output]
        Bx512xHxW                 (scale=ones(32), B=zeros(32))                        |       ^     Bx512xHxW
                                                                                       |       |
                                                                                       +--->Sigmoid (optional)
        The Mul and Sigmoid before output is for Swish activation. They are optional.
        """
