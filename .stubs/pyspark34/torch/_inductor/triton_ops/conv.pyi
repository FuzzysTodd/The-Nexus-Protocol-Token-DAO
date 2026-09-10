from ..utils import has_triton as has_triton
from .autotune import conv_heuristics as conv_heuristics
from _typeshed import Incomplete

class _conv:
    kernel: Incomplete
    @staticmethod
    def forward(x, w, bias, stride=(1, 1), padding=(0, 0), dilation=(1, 1), transposed: bool = False, output_padding=(0, 0), groups: int = 1): ...

conv: Incomplete
