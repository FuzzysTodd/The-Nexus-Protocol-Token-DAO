from .calibrate import TensorData as TensorData
from .onnx_model import ONNXModel as ONNXModel
from .quant_utils import QuantType as QuantType, QuantizationMode as QuantizationMode, QuantizedValue as QuantizedValue, QuantizedValueType as QuantizedValueType, TENSOR_NAME_QUANT_SUFFIX as TENSOR_NAME_QUANT_SUFFIX, __producer__ as __producer__, __version__ as __version__, add_infer_metadata as add_infer_metadata, attribute_to_kwarg as attribute_to_kwarg, compute_scale_zp as compute_scale_zp, compute_scale_zp_float8 as compute_scale_zp_float8, find_by_name as find_by_name, get_qmin_qmax_for_qType as get_qmin_qmax_for_qType, get_qrange_for_qType as get_qrange_for_qType, model_has_infer_metadata as model_has_infer_metadata, ms_domain as ms_domain, quantize_data as quantize_data, save_and_reload_model_with_shape_infer as save_and_reload_model_with_shape_infer, tensor_proto_to_array as tensor_proto_to_array
from .registry import CreateOpQuantizer as CreateOpQuantizer
from _typeshed import Incomplete
from typing import Any, Dict

class QuantizationParams:
    data: Incomplete
    def __init__(self, **data: Dict[str, Any]) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, key): ...
    def __len__(self) -> int: ...

class ONNXQuantizer:
    value_infos: Incomplete
    model: Incomplete
    per_channel: Incomplete
    reduce_range: Incomplete
    mode: Incomplete
    static: Incomplete
    fuse_dynamic_quant: bool
    extra_options: Incomplete
    enable_subgraph_quantization: Incomplete
    force_quantize_no_input_check: Incomplete
    q_matmul_const_b_only: Incomplete
    is_weight_symmetric: Incomplete
    is_activation_symmetric: Incomplete
    activation_qType: Incomplete
    weight_qType: Incomplete
    tensors_range: Incomplete
    nodes_to_quantize: Incomplete
    nodes_to_exclude: Incomplete
    op_types_to_quantize: Incomplete
    new_nodes: Incomplete
    parent: Incomplete
    graph_scope: str
    tensor_names: Incomplete
    opset_version: Incomplete
    quantization_params: Incomplete
    fixed_qrange_uint8_name: str
    fixed_qrange_int8_name: str
    fixed_zero_name: str
    fixed_zero_zp_name: str
    quantized_value_map: Incomplete
    generated_value_names: Incomplete
    used_scale_zp_map: Incomplete
    def __init__(self, model, per_channel, reduce_range, mode, static, weight_qType, activation_qType, tensors_range, nodes_to_quantize, nodes_to_exclude, op_types_to_quantize, extra_options: Incomplete | None = None) -> None: ...
    def quantize_subgraph(self, subgraph, graph_key):
        """
        generate submodel for the subgraph, so that we re-utilize current quantization implementation.
        quantize the submodel
        update subgraph and set it back to node
        """
    def quantize_node_with_sub_graph(self, node):
        """
        Check subgraph, if any, quantize it and replace it.
        return new_nodes added for quantizing subgraph
        """
    def check_opset_version(self): ...
    def has_QDQ_nodes(self):
        """
        Detect if model already has QuantizeLinear or DequantizeLinear.
        """
    def find_initializer_in_path(self, initializer_name): ...
    def add_new_nodes(self, nodes) -> None: ...
    def quantize_model(self): ...
    def is_input_a_initializer(self, input_name): ...
    def is_per_channel(self): ...
    def is_valid_quantize_weight(self, weight_name): ...
    def is_float_tensor(self, tensor_name): ...
    def should_quantize_node(self, node): ...
    def set_quant_scale_zp(self, tensor_name, value) -> None: ...
    def find_quant_scale_zp(self, input_name): ...
    def find_quantized_value(self, input_name): ...
    def quantize_bias_static(self, bias_name, input_name, weight_name, beta: float = 1.0):
        """
        Quantized the bias. Zero Point == 0 and Scale == Input_Scale * Weight_Scale
        """
    def contains_tensor(self, tensor_name):
        """
        only check for value info and newly generated tensor names, initializers are checked separately
        """
    def quantize_activation(self, node, indices, from_subgraph: bool = False): ...
    def quantize_weight(self, node, indices, reduce_range: bool = False, op_level_per_channel: bool = False, axis: int = -1, from_subgraph: bool = False): ...
    def quantize_initializer(self, weight, qType, reduce_range: bool = False, keep_float_weight: bool = False):
        """
        :param weight: TensorProto initializer
        :param qType: type to quantize to
        :param keep_float_weight: Whether to quantize the weight. In some cases, we only want to qunatize scale and zero point.
                                  If keep_float_weight is False, quantize the weight, or don't quantize the weight.
        :return: quantized weight name, zero point name, scale name
        """
    def quantize_weight_per_channel(self, weight_name, weight_qType, channel_axis, reduce_range: bool = True, keep_float_weight: bool = False): ...
    def calculate_quantization_params(self): ...
