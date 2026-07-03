from ..lowering import register_lowering as register_lowering
from ..select_algorithm import ExternKernelChoice as ExternKernelChoice, TritonTemplate as TritonTemplate, autotune_select_algorithm as autotune_select_algorithm
from ..utils import use_triton_template as use_triton_template
from .mm_common import addmm_epilogue as addmm_epilogue, mm_args as mm_args, mm_configs as mm_configs, mm_grid as mm_grid, mm_options as mm_options
from _typeshed import Incomplete

log: Incomplete
aten: Incomplete
mm_template: Incomplete
aten_mm: Incomplete
aten_addmm: Incomplete

def bias_addmm(inp, mat1, mat2, *, out: Incomplete | None = None, alpha: int = 1, beta: int = 1):
    """
    Giving torch.addmm a 1D tensor calls a different (faster) cublasLt
    kernel under the hood.  There are a few shapes where this is slower,
    but they are rare.
    """

aten_bias_addmm: Incomplete

def tuned_mm(mat1, mat2, *, layout: Incomplete | None = None): ...
def tuned_addmm(inp, mat1, mat2, *, alpha: int = 1, beta: int = 1, layout: Incomplete | None = None): ...
