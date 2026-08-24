from _typeshed import Incomplete
from fusion_base import Fusion
from onnx_model import OnnxModel as OnnxModel
from typing import Dict

logger: Incomplete

class FusionGelu(Fusion):
    def __init__(self, model: OnnxModel) -> None: ...
    def fuse(self, erf_node, input_name_to_nodes: Dict, output_name_to_node: Dict): ...
    def fuse_1(self, erf_node, input_name_to_nodes: Dict, output_name_to_node: Dict) -> bool | None:
        """
        This pattern is from PyTorch model
        Fuse Gelu with Erf into one node:
        Pattern 1:
                       +-------Mul(0.5)---------------------+
                       |                                    |
                       |                                    v
                    [root] --> Div -----> Erf  --> Add --> Mul -->
                              (B=1.4142...)       (1)

        Pattern 2:
                       +------------------------------------+
                       |                                    |
                       |                                    v
                    [root] --> Div -----> Erf  --> Add --> Mul -->Mul -->
                              (B=1.4142...)       (1)            (0.5)

        Note that constant input for Add and Mul could be first or second input: like either A=0.5 or B=0.5 is fine.
        """
    def fuse_2(self, erf_node, input_name_to_nodes: Dict, output_name_to_node: Dict) -> bool | None:
        """
        This pattern is from Keras model
        Fuse Gelu with Erf into one node:
                       +------------------------------------------+
                       |                                          |
                       |                                          v
                    [root] --> Div -----> Erf  --> Add --> Mul -->Mul
                              (B=1.4142...)       (A=1)   (A=0.5)

        Note that constant input for Add and Mul could be first or second input: like either A=0.5 or B=0.5 is fine.
        """
    def fuse_3(self, erf_node, input_name_to_nodes: Dict, output_name_to_node: Dict) -> bool | None:
        """
        This pattern is from TensorFlow model
        Fuse Gelu with Erf into one node:
                       +----------------------------------------------+
                       |                                              |
                       |                                              v
                    [root] --> Mul -----> Erf    -->   Add --> Mul -->Mul
                               (A=0.7071067690849304)  (B=1)  (B=0.5)

        Note that constant input for Add and Mul could be first or second input: like either A=0.5 or B=0.5 is fine.
        """
