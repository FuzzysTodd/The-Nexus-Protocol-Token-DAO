from _typeshed import Incomplete
from torch._inductor.select_algorithm import realize_inputs as realize_inputs
from torch._inductor.virtualized import V as V

log: Incomplete

def mm_configs(): ...
def mm_grid(m, n, meta):
    """
    The CUDA grid size for matmul triton templates.
    """
def acc_type(dtype): ...
def mm_options(config, sym_k, layout):
    """
    Common options to matmul triton templates.
    """
def mm_args(mat1, mat2, *others, layout: Incomplete | None = None):
    """
    Common arg processing for mm,bmm,addmm,etc
    """
def addmm_epilogue(dtype, alpha, beta): ...
