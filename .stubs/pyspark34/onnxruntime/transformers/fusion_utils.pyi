from _typeshed import Incomplete
from numpy import ndarray
from onnx import NodeProto as NodeProto, TensorProto, onnx_pb as onnx_proto
from onnx_model import OnnxModel as OnnxModel
from typing import Tuple

logger: Incomplete

class FusionUtils:
    model: Incomplete
    def __init__(self, model: OnnxModel) -> None: ...
    def cast_graph_input_to_int32(self, input_name: str) -> Tuple[bool, str]: ...
    def cast_input(self, input_name: str, target_type: str = 'int32'): ...
    def cast_input_to_int32(self, input_name: str): ...
    def remove_cast_int32(self, input_name: str): ...
    @staticmethod
    def update_node_input(node, i, new_input_name, input_name_to_nodes): ...
    @staticmethod
    def skip_parent(model: OnnxModel, node, parent_node, input_name_to_nodes, node_input_index: int = 0, parent_input_index: int = 0):
        """
        Before:
              (input)-->parent-->node-->(output)
        After:
              (input)-->parent-->
                |
                +----->node-->(output)

        This function returns a flag whether the parent node can be removed.
        """
    @staticmethod
    def check_node_attribute(node, attribute_name: str, expected_value, default_value: Incomplete | None = None):
        """Verify that a node has expected value for an attribute.

        Args:
            node (NodeProto): a node to check
            attribute_name (str): name of attribute
            expected_value (Any): expected value of the attribute
            default_value (Any, optional): default value if the attribute does not exist. Defaults to None.

        Returns:
            bool: whether the check is passed or not
        """
    @staticmethod
    def transpose_2d_int8_tensor(tensor: onnx_proto.TensorProto):
        """Transpose a 2-D INT8 TensorProto
        Args:
            tensor (TensorProto): tensor to be transposed
        Returns:
            tensor (TensorProto): transposed tensor
        """
    @staticmethod
    def check_qdq_node_for_fusion(node: NodeProto, model: OnnxModel, allow_per_tensor_quantization_only: bool = True):
        """Verify if a provided QuantizeLinear (Q) / DequantizeLinear (DQ) node is a good candidate for fusion.
           It is a good candidate for fusion if:
           (1) The Q/DQ node is for per-tensor quantization if allow_per_tensor_quantization_only is `True`
           (2) The Q/DQ node should have constant scale
           (3) The Q/DQ node should have a zero point of 0
        Args:
            node (NodeProto): a Q/DQ node to check
        Returns:
            bool: whether the check is passed or not
        """
    def check_node_input_value(self, node, input_index: int, expected_value):
        """Verify that a node has expected input value

        Args:
            node (NodeProto): a node to check
            input_index (int): index of its input to be verified
            expected_value (Any): expected value of the input

        Returns:
            bool: whether the check is passed or not
        """
    def remove_identity_nodes(self) -> None:
        """Remove Identity nodes, except those right before graph output."""
    def remove_cascaded_cast_nodes(self) -> None: ...
    def remove_useless_cast_nodes(self) -> None: ...
    def remove_useless_reshape_nodes(self) -> None:
        """Remove reshape node that is not needed based on symbolic shape inference: input and output has same shape"""

class NumpyHelper:
    @staticmethod
    def to_array(tensor: TensorProto, fill_zeros: bool = False) -> ndarray: ...
