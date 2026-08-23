from ..quant_utils import attribute_to_kwarg as attribute_to_kwarg, ms_domain as ms_domain
from .base_operator import QuantOperatorBase as QuantOperatorBase

class AttentionQuant(QuantOperatorBase):
    def __init__(self, onnx_quantizer, onnx_node) -> None: ...
    def should_quantize(self): ...
    def quantize(self):
        """
        parameter node: Attention node.
        parameter new_nodes_list: List of new nodes created before processing this node.
        return: a list of nodes in topological order that represents quantized Attention node.
        """
