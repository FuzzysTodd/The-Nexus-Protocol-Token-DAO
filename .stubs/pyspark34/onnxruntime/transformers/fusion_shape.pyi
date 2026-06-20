from _typeshed import Incomplete
from fusion_base import Fusion
from onnx import NodeProto as NodeProto, TensorProto as TensorProto
from onnx_model import OnnxModel as OnnxModel
from typing import Dict, List

logger: Incomplete

class FusionShape(Fusion):
    utils: Incomplete
    shape_infer: Incomplete
    shape_infer_done: bool
    def __init__(self, model: OnnxModel) -> None: ...
    def get_dimensions_from_tensor_proto(self, tensor_proto: TensorProto) -> int | None: ...
    def get_dimensions(self, input_name: str) -> int | None: ...
    prune_graph: bool
    def fuse(self, concat_node: NodeProto, input_name_to_nodes: Dict[str, List[NodeProto]], output_name_to_node: Dict[str, NodeProto]):
        """
        Smplify subgraph like

                   (2d_input)
                    /                       Shape       shape
                /                         Gather(indices=0)  Gather(indices=1)
                |                |
            Unsqueeze(axes=0)   Unsqueeze(axes=0)
                   \\          /
                      Concat
                        |

        into  (2d_input) --> Shape -->
        """
