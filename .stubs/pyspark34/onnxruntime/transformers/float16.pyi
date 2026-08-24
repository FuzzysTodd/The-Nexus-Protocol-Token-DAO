from _typeshed import Incomplete
from onnx import onnx_pb as onnx_proto

logger: Incomplete

def convert_np_to_float16(np_array, min_positive_val: float = 5.96e-08, max_finite_val: float = 65504.0):
    """
    Convert float32 numpy array to float16 without changing sign or finiteness.
    Positive values less than min_positive_val are mapped to min_positive_val.
    Positive finite values greater than max_finite_val are mapped to max_finite_val.
    Similar for negative values. NaN, 0, inf, and -inf are unchanged.
    """
def convert_tensor_float_to_float16(tensor, min_positive_val: float = 5.96e-08, max_finite_val: float = 65504.0):
    """Convert tensor float to float16.

    Args:
        tensor (TensorProto): the tensor to convert.
        min_positive_val (float, optional): minimal positive value. Defaults to 1e-7.
        max_finite_val (float, optional): maximal finite value. Defaults to 1e4.

    Raises:
        ValueError: input type is not TensorProto.

    Returns:
        TensorProto: the converted tensor.
    """
def make_value_info_from_tensor(tensor): ...

DEFAULT_OP_BLOCK_LIST: Incomplete
ALWAYS_FLOAT_INPUTS: Incomplete

class InitializerTracker:
    """Class for keeping track of initializer."""
    initializer: Incomplete
    fp32_nodes: Incomplete
    fp16_nodes: Incomplete
    def __init__(self, initializer: onnx_proto.TensorProto) -> None: ...
    def add_node(self, node: onnx_proto.NodeProto, is_node_blocked): ...

def convert_float_to_float16(model, min_positive_val: float = 5.96e-08, max_finite_val: float = 65504.0, keep_io_types: bool = False, disable_shape_infer: bool = False, op_block_list: Incomplete | None = None, node_block_list: Incomplete | None = None, force_fp16_initializers: bool = False, force_fp16_inputs: Incomplete | None = None):
    """Convert tensor float type in the input ONNX model to tensor float16.

    Args:
        model (ModelProto or str): The ONNX model or path of the model to convert.
        min_positive_val (float, optional): minimal positive value. Defaults to 5.96e-08.
        max_finite_val (float, optional): maximal finite value of float16. Defaults to 65504.
        keep_io_types (Union[bool, List[str]], optional): It could be boolean or a list of float32 input/output names.
                                                          If True, model inputs/outputs should be left as float32.
                                                          Defaults to False.
        disable_shape_infer (bool, optional): Skips running onnx shape/type inference.
                                              Useful if shape inference has been done. Defaults to False.
        op_block_list (List[str], optional): List of op types to leave as float32.
                                             Defaults to None, which will use `float16.DEFAULT_OP_BLOCK_LIST`.
        node_block_list (List[str], optional): List of node names to leave as float32. Defaults to None.
        force_fp16_initializers(bool): force converting all float initializers to float16.
                                       Default to false, which will convert only the one needed to avoid precision loss.
        force_fp16_inputs(Dict[str, List[int]]): Force the conversion of the inputs of some operators to float16, even if
                                                 this script's preference it to keep them in float32.
    Raises:
        ValueError: input type is not ModelProto.

    Returns:
        ModelProto: converted model.
    """
def float_to_float16_max_diff(tensor, min_positive_val: float = 5.96e-08, max_finite_val: float = 65504.0):
    """Measure the maximum absolute difference after converting a float tensor to float16."""
