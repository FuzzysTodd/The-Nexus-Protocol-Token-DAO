from torch import _C
from torch.onnx._internal import jit_utils
from typing import Sequence

__all__ = ['layer_norm']

def layer_norm(g: jit_utils.GraphContext, input: _C.Value, normalized_shape: Sequence[int], weight: _C.Value, bias: _C.Value, eps: float, cudnn_enable: bool): ...
