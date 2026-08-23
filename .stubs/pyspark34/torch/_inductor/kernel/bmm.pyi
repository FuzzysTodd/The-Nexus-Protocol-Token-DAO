from ..lowering import register_lowering as register_lowering
from ..select_algorithm import ExternKernelChoice as ExternKernelChoice, TritonTemplate as TritonTemplate, autotune_select_algorithm as autotune_select_algorithm
from ..utils import use_triton_template as use_triton_template
from .mm_common import addmm_epilogue as addmm_epilogue, mm_args as mm_args, mm_configs as mm_configs, mm_options as mm_options
from _typeshed import Incomplete

aten: Incomplete

def bmm_grid(b, m, n, meta): ...

bmm_template: Incomplete
aten_bmm: Incomplete
aten_baddbmm: Incomplete

def tuned_bmm(mat1, mat2, *, layout: Incomplete | None = None): ...
def tuned_baddbmm(inp, mat1, mat2, *, alpha: int = 1, beta: int = 1, layout: Incomplete | None = None): ...
