from _typeshed import Incomplete

class QuantOperatorBase:
    quantizer: Incomplete
    node: Incomplete
    def __init__(self, onnx_quantizer, onnx_node) -> None: ...
    def should_quantize(self): ...
    def quantize(self) -> None:
        """
        Given a node which does not support quantization, this method checks whether the input to
        this node is quantized and adds a DequantizeLinear node to dequantize this input back to FP32
            parameter node: Current node
            parameter new_nodes_list: List of new nodes created before processing current node
            return: List of new nodes created
        """
