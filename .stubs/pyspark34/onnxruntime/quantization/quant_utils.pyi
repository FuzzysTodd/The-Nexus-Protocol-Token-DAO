import numpy
from _typeshed import Incomplete
from enum import Enum
from onnx import ModelProto as ModelProto, TensorProto
from onnxruntime import GraphOptimizationLevel as GraphOptimizationLevel, InferenceSession as InferenceSession, SessionOptions as SessionOptions
from pathlib import Path

__producer__: str
__version__: str
onnx_domain: str
ms_domain: str
QUANT_OP_NAME: str
QUANT_INPUT_SUFFIX: str
DEQUANT_OP_NAME: str
DEQUANT_OUTPUT_SUFFIX: str
TENSOR_NAME_QUANT_SUFFIX: str
FLOAT8_DISTRIBUTIONS: Incomplete
type_to_name: Incomplete

class QuantizationMode(Enum):
    IntegerOps: int
    QLinearOps: int
    @staticmethod
    def from_string(mode): ...

class QuantizedValueType(Enum):
    Input: int
    Initializer: int
    @staticmethod
    def from_string(v): ...

class QuantType(Enum):
    QInt8: int
    QUInt8: int
    QFLOAT8E4M3FN: int
    @staticmethod
    def from_string(t): ...
    @property
    def tensor_type(self): ...

class QuantFormat(Enum):
    QOperator: int
    QDQ: int
    @staticmethod
    def from_string(format): ...

ONNX_TYPE_TO_NP_TYPE: Incomplete

def quantize_nparray(qType, arr, scale, zero_point, low: Incomplete | None = None, high: Incomplete | None = None): ...
def compute_scale_zp(rmin, rmax, qmin, qmax, symmetric: bool = False):
    """Calculate the scale s and zero point z for the quantization relation
    r = s(q-z), where r are the original values and q are the corresponding
    quantized values.

    r and z are calculated such that every value within [rmin,rmax] has an
    approximate representation within [qmin,qmax]. In addition, qmin <= z <=
    qmax is enforced. If the symmetric flag is set to True, the interval
    [rmin,rmax] is symmetrized to [-absmax, +absmax], where
    absmax = max(abs(rmin), abs(rmax)).

    :parameter rmin: minimum value of r
    :parameter rmax: maximum value of r
    :parameter qmin: minimum value representable by the target quantization data type
    :parameter qmax: maximum value representable by the target quantization data type
    :return: zero and scale [z, s]

    """
def compute_scale_zp_float8(element_type, std):
    """Calculate the scale s for a float8 type (E4M3FN).
    The function assumes the coefficient distribution and the float 8
    distribution are similar to two gaussian laws.

    :return: zero and scale [z, s]

    More details in notebook `quantization_fp8.ipynb
    <https://github.com/microsoft/onnxruntime/blob/main/docs/python/notebooks/quantization_fp8.ipynb>`_.
    """
def quantize_data(data, qType, symmetric, reduce_range: bool = False):
    """
    :param data: data to quantize
    :param qType: data type to quantize to. Supported types UINT8 and INT8
    :param symmetric: whether symmetric quantization is used or not. This is applied to INT8.
    :return: minimum, maximum, zero point, scale, and quantized weights

    To pack weights, we compute a linear transformation

    - when data `type == uint8` mode, from `[rmin, rmax]` -> :math:`[0, 2^{b-1}]` and
    - when data `type == int8`, from `[-m , m]` -> :math:`[-(2^{b-1}-1), 2^{b-1}-1]` where
        `m = max(abs(rmin), abs(rmax))`

    and add necessary intermediate nodes to trasnform quantized weight to full weight using the equation

    :math:`r = S(q-z)`, where

    - *r*: real original value
    - *q*: quantized value
    - *S*: scale
    - *z*: zero point
    """
def get_qmin_qmax_for_qType(qType, reduce_range: bool = False, symmetric: bool = False):
    """
    Return qmin and qmax, the minimum and maximum value representable by the given qType
    :parameter qType: onnx.onnx_pb.TensorProto.UINT8 or onnx.onnx_pb.TensorProto.UINT8
    :return: qmin, qmax
    """
def get_qrange_for_qType(qType, reduce_range: bool = False, symmetric: bool = False):
    """
    Helper function to get the quantization range for a type.
        parameter qType: quantization type.
        return: quantization range.
    """

class QuantizedInitializer:
    """
    Represents a linearly quantized weight input from ONNX operators
    """
    name: Incomplete
    initializer: Incomplete
    rmins: Incomplete
    rmaxs: Incomplete
    zero_points: Incomplete
    scales: Incomplete
    data: Incomplete
    quantized_data: Incomplete
    axis: Incomplete
    def __init__(self, name, initializer, rmins, rmaxs, zero_points, scales, data=[], quantized_data=[], axis: Incomplete | None = None) -> None: ...

class QuantizedValue:
    """
    Represents a linearly quantized value (input\\output\\intializer)
    """
    original_name: Incomplete
    q_name: Incomplete
    scale_name: Incomplete
    zp_name: Incomplete
    value_type: Incomplete
    axis: Incomplete
    node_type: Incomplete
    node_qtype: Incomplete
    def __init__(self, name, new_quantized_name, scale_name, zero_point_name, quantized_value_type, axis: Incomplete | None = None, node_type: Incomplete | None = None, node_qtype: Incomplete | None = None) -> None: ...

class BiasToQuantize:
    """
    Represents a bias to be quantized
    """
    bias_name: Incomplete
    input_name: Incomplete
    weight_name: Incomplete
    def __init__(self, bias_name, input_name, weight_name) -> None: ...

def attribute_to_kwarg(attribute):
    """
    Convert attribute to kwarg format for use with onnx.helper.make_node.
        :parameter attribute: attribute in AttributeProto format.
        :return: attribute in {key: value} format.
    """
def find_by_name(item_name, item_list):
    """
    Helper function to find item by name in a list.
        parameter item_name: name of the item.
        parameter item_list: list of items.
        return: item if found. None otherwise.
    """
def get_elem_index(elem_name, elem_list):
    """
    Helper function to return index of an item in a node list
    """
def get_mul_node(inputs, output, name):
    """
    Helper function to create a Mul node.
        parameter inputs: list of input names.
        parameter output: output name.
        parameter name: name of the node.
        return: Mul node in NodeProto format.
    """
def generate_identified_filename(filename: Path, identifier: str) -> Path:
    """
    Helper function to generate a identifiable filepath by concatenating the given identifier as a suffix.
    """
def apply_plot(hist, hist_edges) -> None: ...
def write_calibration_table(calibration_cache) -> None:
    """
    Helper function to write calibration table to files.
    """
def smooth_distribution(p, eps: float = 0.0001):
    """Given a discrete distribution (may have not been normalized to 1),
    smooth it by replacing zeros with eps multiplied by a scaling factor
    and taking the corresponding amount off the non-zero values.
    Ref: http://web.engr.illinois.edu/~hanj/cs412/bk3/KL-divergence.pdf
         https://github.com//apache/incubator-mxnet/blob/master/python/mxnet/contrib/quantization.py
    """
def model_has_external_data(model_path: Path): ...
def optimize_model(model_path: Path, opt_model_path: Path):
    """
        Generate model that applies graph optimization (constant folding, etc.)
        parameter model_path: path to the original onnx model
        parameter opt_model_path: path to the optimized onnx model
    :return: optimized onnx model
    """
def add_pre_process_metadata(model: ModelProto):
    """Tag the model that it went through quantization pre-processing"""
def model_has_pre_process_metadata(model: ModelProto) -> bool:
    """Check the model whether it went through quantization pre-processing"""
def add_infer_metadata(model: ModelProto): ...
def model_has_infer_metadata(model: ModelProto) -> bool: ...
def load_model_with_shape_infer(model_path: Path) -> ModelProto: ...
def save_and_reload_model_with_shape_infer(model: ModelProto) -> ModelProto: ...
def tensor_proto_to_array(initializer: TensorProto) -> numpy.ndarray: ...
def add_quant_suffix(tensor_name: str) -> str: ...
def add_quant_input_suffix(tensor_name: str) -> str: ...
def add_quant_output_suffix(tensor_name) -> str: ...
def add_dequant_suffix(tensor_name) -> str: ...
def add_dequant_input_suffix(tensor_name) -> str: ...
def add_dequant_output_suffix(tensor_name) -> str: ...
