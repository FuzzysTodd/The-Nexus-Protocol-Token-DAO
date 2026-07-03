from .. import config as config, triton_ops as triton_ops
from ..virtualized import V as V
from _typeshed import Incomplete
from torch._dynamo.testing import rand_strided as rand_strided

aten: Incomplete

def str2func(str): ...

class Autotuner:
    cache: Incomplete
    def __init__(self) -> None: ...

autotune: Incomplete

def tuned_conv(x_shape, w_shape, x_stride, w_stride, stride, padding, dilation, transposed, output_padding, groups, device, dtype, adjust_triton: float = 0.95):
    """
    Return the best kernel name given inputs and layer parameters;
    Considering potential pointwise fusion of conv, we could adjust triton timing
    by multiplying adjust_triton (default=0.95)
    """
def tuned_conv_layout(kernel, x_shape, w_shape, stride, padding, dilation, transposed, output_padding, groups, device, dtype): ...
