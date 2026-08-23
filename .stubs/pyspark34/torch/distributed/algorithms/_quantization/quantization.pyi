from _typeshed import Incomplete
from enum import Enum

TORCH_HALF_MIN: Incomplete
TORCH_HALF_MAX: Incomplete

class DQuantType(Enum):
    """
    Different quantization methods for auto_quantize API are identified here.
    auto_quantize API currently supports fp16 and bfp16 methods.
    """
    FP16: Incomplete
    BFP16: str

def auto_quantize(func, qtype, quant_loss: Incomplete | None = None):
    """
    This is a prototype API that automatically quantize the input tensors, choose the precision types, and
    pass other necessary arguments and then dequantizes the output.
    Currently it only supports:
        . FP16 and BFP16 quantization method supported for gloo and nccl backends
        . all_gather, all_to_all collective ops
    Note: BFP16 only supports 2D tensors.
    Args:
        func (Callable): A function representing collective operations.
        qtype (QuantType): Quantization method
        quant_loss (float, optional): This can be used to improve accuracy in the dequantization.
    Returns:
        (Callable): the same collective as func but enables automatic quantization/dequantization.
    """
