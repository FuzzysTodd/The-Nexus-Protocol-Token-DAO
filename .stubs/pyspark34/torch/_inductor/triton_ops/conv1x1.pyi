from ..utils import has_triton as has_triton
from _typeshed import Incomplete

class _conv1x1:
    @staticmethod
    def forward(x, w, bias, stride=(1, 1), padding=(0, 0), dilation=(1, 1), transposed: bool = False, output_padding=(0, 0), groups: int = 1): ...

conv1x1: Incomplete
