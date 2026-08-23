import numpy as np
import numpy.typing as npt
from .onnx_model import ONNXModel as ONNXModel
from .quant_utils import attribute_to_kwarg as attribute_to_kwarg, load_model_with_shape_infer as load_model_with_shape_infer
from _typeshed import Incomplete
from onnx.onnx_pb import GraphProto as GraphProto, ModelProto as ModelProto, NodeProto as NodeProto, TensorProto as TensorProto

def int4_block_quant(quant_type: int, fp32weight: npt.ArrayLike) -> np.ndarray:
    """4b quantize fp32 weight to a blob"""

class MatMulWeight4Quantizer:
    """Perform 4b quantization of constant MatMul weights"""
    BlkQ4Sym: int
    BlkQ4Zp8: int
    model: Incomplete
    quant_type: Incomplete
    def __init__(self, model: ModelProto, quant_type: int) -> None: ...
    def process(self) -> None: ...

def parse_args(): ...
