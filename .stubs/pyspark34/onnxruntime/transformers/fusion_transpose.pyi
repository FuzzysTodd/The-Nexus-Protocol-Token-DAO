from _typeshed import Incomplete
from fusion_base import Fusion
from onnx import NodeProto as NodeProto
from onnx_model import OnnxModel
from typing import Dict, List

logger: Incomplete

class FusionTranspose(Fusion):
    def __init__(self, model: OnnxModel) -> None: ...
    def fuse(self, transpose_node: NodeProto, input_name_to_nodes: Dict[str, List[NodeProto]], output_name_to_node: Dict[str, NodeProto]):
        """
        Note that onnxruntime will do comprehensive transpose optimization after loading model.
        The purpose of this fusion is to make graph clean before running onnxruntime.

        Case 1:
              (input)-->Transpose(perm=a)-->Transpose(perm=b)-->
        After:
              (input)-->Transpose(perm=a)-->  (this path can be removed if the output is not used anymore)
                |
                +----->Transpose(perm=a*b)-->

        Case 2 (Cast has only one child):
              (input)-->Transpose(perm=a)--> Cast -->Transpose(perm=b)-->
        After:
              (input)-->Transpose(perm=a)-->  (this path can be removed if the output is not used anymore)
                |
                +----->Cast --> Transpose(perm=a*b)-->
        """

class FusionInsertTranspose(Fusion):
    def __init__(self, model: OnnxModel) -> None: ...
    def create_transpose_node(self, input_name: str, perm: List[int], output_name: Incomplete | None = None):
        """Append a Transpose node after an input"""
    def fuse(self, group_norm_node: NodeProto, input_name_to_nodes: Dict[str, List[NodeProto]], output_name_to_node: Dict[str, NodeProto]):
        """
        This optimization will insert an Transpose, and onnxruntime transpose optimizer will remove it together with
        another Transpose so that we can get effect of reducing one Transpose after onnxruntime optimization.
        Before:
            --> Gemm --> Unsqueeze(axes=[2]) --> Unsqueeze(axes=[3]) --> Add --> Transpose([0,2,3,1]) --> GroupNorm
        After:
            --> Gemm --> Unsqueeze(axes=[1]) --> Unsqueeze(axes=[2]) -->Transpose([0,3,1,2]) --> Add --> Transpose([0,2,3,1]) --> GroupNorm
        """
