from .onnx_quantizer import ONNXQuantizer as ONNXQuantizer
from .quant_utils import DEQUANT_OP_NAME as DEQUANT_OP_NAME, QUANT_OP_NAME as QUANT_OP_NAME, QuantizedValue as QuantizedValue, QuantizedValueType as QuantizedValueType, __producer__ as __producer__, __version__ as __version__, add_dequant_output_suffix as add_dequant_output_suffix, add_dequant_suffix as add_dequant_suffix, add_quant_input_suffix as add_quant_input_suffix, add_quant_output_suffix as add_quant_output_suffix, add_quant_suffix as add_quant_suffix, find_by_name as find_by_name
from .registry import CreateQDQQuantizer as CreateQDQQuantizer
from _typeshed import Incomplete
from enum import Enum

class QDQQuantTensorType(Enum):
    ACTIVATION: int
    WEIGHT: int
    BIAS: int

class QDQTensorQuantInfo:
    tensor_type: Incomplete
    quant_para_provider: Incomplete
    axis: Incomplete
    is_shared: Incomplete
    def __init__(self, tensor_type=..., quant_para_provider: Incomplete | None = None, axis: Incomplete | None = None) -> None: ...

class QDQQuantizer(ONNXQuantizer):
    tensors_to_quantize: Incomplete
    bias_to_quantize: Incomplete
    nodes_to_remove: Incomplete
    op_types_to_exclude_output_quantization: Incomplete
    add_qdq_pair_to_weight: Incomplete
    quantize_bias: Incomplete
    dedicated_qdq_pair: Incomplete
    tensor_to_its_receiving_nodes: Incomplete
    qdq_op_type_per_channel_support_to_axis: Incomplete
    def __init__(self, model, per_channel, reduce_range, mode, static, weight_qType, activation_qType, tensors_range, nodes_to_quantize, nodes_to_exclude, op_types_to_quantize, extra_options: Incomplete | None = None) -> None: ...
    def quantize_activation_tensor(self, tensor_name, quant_sharing_param: Incomplete | None = None):
        """
        Quantize Activation Tensor
        Args:
            tensor_name: name of the tensor to quantize
            quant_sharing_param: name of the tensor that provides quantization parameter

        """
    def quantize_weight_tensor(self, tensor_name, quant_sharing_param: Incomplete | None = None):
        """
        Quantize Weight Tensor
        Args:
            tensor_name: name of the tensor to quantize
            quant_sharing_param: name of the tensor that provides quantization parameter

        """
    def quantize_weight_tensor_per_channel(self, tensor_name, axis) -> None: ...
    def quantize_bias_tensor(self, bias_name, input_name, weight_name, beta: float = 1.0) -> None: ...
    def remove_node(self, node) -> None: ...
    def remove_nodes(self) -> None: ...
    def quantize_model(self): ...
    def try_replacing_upstream_output(self, upstream_output_name, output_name): ...
    def is_tensor_quantized(self, tensor_name): ...
