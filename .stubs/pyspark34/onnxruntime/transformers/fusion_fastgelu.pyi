from _typeshed import Incomplete
from fusion_base import Fusion
from onnx_model import OnnxModel as OnnxModel
from typing import Dict

logger: Incomplete

class FusionFastGelu(Fusion):
    def __init__(self, model: OnnxModel) -> None: ...
    def fuse(self, tanh_node, input_name_to_nodes: Dict, output_name_to_node: Dict): ...
    def fuse_1(self, tanh_node, input_name_to_nodes, output_name_to_node) -> bool | None:
        """
        Fuse Gelu with tanh into one node:
              +---------------------------+
              |                           |
              |                           v
            [root] --> Pow --> Mul -----> Add  --> Mul --> Tanh --> Add --> Mul
              |       (Y=3)   (B=0.0447...)       (B=0.7978...)    (B=1)     ^
              |                                                              |
              +------> Mul(B=0.5)--------------------------------------------+
        Note that constant input for Add and Mul could be first or second input: like either A=0.5 or B=0.5 is fine.
        """
    def fuse_2(self, tanh_node, input_name_to_nodes: Dict, output_name_to_node: Dict) -> bool | None:
        """
        This pattern is from Tensorflow model.
        Fuse Gelu with tanh into one node:
              +---------------------------+
              |                           |
              |                           v
            [root] --> Pow --> Mul -----> Add  --> Mul --> Tanh --> Add --> Mul(B=0.5)-->Mul-->
              |       (Y=3)   (B=0.0447...)       (B=0.7978...)    (B=1)                  ^
              |                                                                           |
              +---------------------------------------------------------------------------+
        Note that constant input for Add and Mul could be first or second input: like either A=0.5 or B=0.5 is fine.
        """
    def fuse_3(self, tanh_node, input_name_to_nodes: Dict, output_name_to_node: Dict) -> bool | None:
        """
        OpenAI's gelu implementation, also used in Megatron:
           Gelu(x) = x * 0.5 * (1.0 + torch.tanh(0.79788456 * x * (1.0 + 0.044715 * x * x)))

        Fuse subgraph into a FastGelu node:
            +------------ Mul (B=0.79788456) -------------------+
            |                                                   |
            +-------------------------------+                   |
            |                               |                   |
            |                               v                   v
          [root] --> Mul (B=0.044715) --> Mul --> Add(B=1) --> Mul --> Tanh --> Add(B=1) --> Mul-->
            |                                                                                 ^
            |                                                                                 |
            +-----------> Mul (B=0.5) --------------------------------------------------------+
        """
