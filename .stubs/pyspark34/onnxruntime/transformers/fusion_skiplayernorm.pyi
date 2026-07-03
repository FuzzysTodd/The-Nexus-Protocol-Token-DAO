from _typeshed import Incomplete
from fusion_base import Fusion
from onnx_model import OnnxModel as OnnxModel

logger: Incomplete

class FusionSkipLayerNormalization(Fusion):
    """
    Fuse Add + LayerNormalization into one node: SkipLayerNormalization
    Note: This fusion does not check the input shape of Add and LayerNormalization.
    """
    shape_infer_helper: Incomplete
    def __init__(self, model: OnnxModel, fused_op_type: str = 'SkipLayerNormalization', search_op_types: str = 'LayerNormalization') -> None: ...
    def fuse(self, node, input_name_to_nodes, output_name_to_node) -> None: ...

class FusionBiasSkipLayerNormalization(Fusion):
    def __init__(self, model: OnnxModel) -> None: ...
    def fuse(self, node, input_name_to_nodes, output_name_to_node) -> None: ...
