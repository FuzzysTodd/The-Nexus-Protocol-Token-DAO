from ..quant_utils import QuantizedValue as QuantizedValue, QuantizedValueType as QuantizedValueType, TENSOR_NAME_QUANT_SUFFIX as TENSOR_NAME_QUANT_SUFFIX, attribute_to_kwarg as attribute_to_kwarg, find_by_name as find_by_name, get_mul_node as get_mul_node
from .base_operator import QuantOperatorBase as QuantOperatorBase
from .qdq_base_operator import QDQOperatorBase as QDQOperatorBase

class ConvInteger(QuantOperatorBase):
    def __init__(self, onnx_quantizer, onnx_node) -> None: ...
    def add_bias(self, nodes, scaled_output) -> None:
        '''
        Given a node, this function handles bias add by adding a "reshape" node on bias and an "add" node
            parameter nodes: new nodes would be appended into nodes
            parameter node: current node (Conv)
            parameter scaled_output: output of quant conv without bias
            parameter output: output of Conv
            parameter bias_name: bias of Conv
            return: the name of output
        '''
    def quantize(self) -> None: ...

class QLinearConv(QuantOperatorBase):
    def __init__(self, onnx_quantizer, onnx_node) -> None: ...
    def quantize(self): ...

class QDQConv(QDQOperatorBase):
    def __init__(self, onnx_quantizer, onnx_node) -> None: ...
    def quantize(self) -> None: ...
