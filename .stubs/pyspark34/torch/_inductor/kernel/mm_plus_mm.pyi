from ..lowering import lowerings as lowerings
from ..select_algorithm import ExternKernelChoice as ExternKernelChoice, TritonTemplate as TritonTemplate, autotune_select_algorithm as autotune_select_algorithm
from ..utils import use_triton_template as use_triton_template
from ..virtualized import V as V
from .mm_common import mm_args as mm_args, mm_grid as mm_grid, mm_options as mm_options
from _typeshed import Incomplete

aten: Incomplete

def ref_mm_plus_mm(a, b, c, d, out): ...

aten_mm_plus_mm: Incomplete
mm_plus_mm_template: Incomplete

def mm_configs(): ...
def tuned_mm_plus_mm(mat1, mat2, mat3, mat4, *, layout: Incomplete | None = None):
    """
    Computes mm(mat1, mat2) + mm(mat3, mat4)
    """
