from _typeshed import Incomplete
from fusion_base import Fusion
from onnx_model import OnnxModel as OnnxModel
from typing import Dict

logger: Incomplete

class FusionLayerNormalization(Fusion):
    def __init__(self, model: OnnxModel) -> None: ...
    def fuse(self, node, input_name_to_nodes: Dict, output_name_to_node: Dict):
        """
        Fuse Layer Normalization subgraph into one node LayerNormalization:
              +----------------------+
              |                      |
              |                      v
          [Root] --> ReduceMean -->  Sub  --> Pow --> ReduceMean --> Add --> Sqrt --> Div --> Mul --> Add
                     (axis=2 or -1)  |      (Y=2)   (axis=2 or -1)  (E-6 or E-12 or 0)    ^
                                     |                                               |
                                     +-----------------------------------------------+

         It also handles cases of duplicated sub nodes exported from older version of PyTorch:
              +----------------------+
              |                      v
              |           +-------> Sub-----------------------------------------------+
              |           |                                                           |
              |           |                                                           v
          [Root] --> ReduceMean -->  Sub  --> Pow --> ReduceMean --> Add --> Sqrt --> Div  --> Mul --> Add
              |                      ^
              |                      |
              +----------------------+
        """

class FusionLayerNormalizationTF(Fusion):
    def __init__(self, model: OnnxModel) -> None: ...
    def fuse(self, node, input_name_to_nodes: Dict, output_name_to_node: Dict):
        """
         Layer Norm from Tensorflow model(using keras2onnx or tf2onnx):
          +------------------------------------+
          |                                    |
          |                                    |
        (Cast_1)                               |
          |                                    |
          |                                    v                                           (B)                             (B)             (A)
         Add --> (Cast_1) --> ReduceMean -->  Sub  --> Mul --> ReduceMean --> (Cast_3) --> Add --> Sqrt --> Reciprocol --> Mul --> Mul --> Sub --> Add
          |                       |                                                                                         |       ^              ^
          |                       |                                                                                         |       |              |
          |                       +--------------------------------------------------(Cast_2)-------------------------------|-------+              |
          |                                                                                                                 v                      |
          +---------------------------------------------------------------------------------------------------------------> Mul--------------------+
        """
