import sympy
from . import ir as ir, lowering as lowering
from .codecache import DiskCache as DiskCache, PyCodeCache as PyCodeCache, code_hash as code_hash
from .codegen.common import IndentedBuffer as IndentedBuffer
from .codegen.triton import TritonKernel as TritonKernel, TritonPrinter as TritonPrinter, config_of as config_of, signature_of as signature_of, texpr as texpr
from .utils import do_bench as do_bench, sympy_dot as sympy_dot, sympy_product as sympy_product
from .virtualized import V as V
from _typeshed import Incomplete
from torch._dynamo.testing import rand_strided as rand_strided
from torch._dynamo.utils import counters as counters, identity as identity
from typing import Any, List

log: Incomplete
VERIFY: bool
PRINT_AUTOTUNE: bool

class KernelNamespace: ...

template_kernels: Incomplete
extern_kernels: Incomplete

class TritonTemplateKernel(TritonKernel):
    input_nodes: Incomplete
    output_node: Incomplete
    named_input_nodes: Incomplete
    defines: Incomplete
    kernel_name: Incomplete
    template_mask: Incomplete
    use_jit: Incomplete
    num_stages: Incomplete
    num_warps: Incomplete
    grid_fn: Incomplete
    meta: Incomplete
    call_sizes: Incomplete
    prefix_args: Incomplete
    suffix_args: Incomplete
    epilogue_fn: Incomplete
    def __init__(self, kernel_name, input_nodes, output_node, defines, num_stages, num_warps, grid_fn, meta, call_sizes, use_jit: bool = True, prefix_args: int = 0, suffix_args: int = 0, epilogue_fn=...) -> None: ...
    def jit_line(self): ...
    def def_kernel(self, *argnames):
        """
        Hook called from template code to generate function def and
        needed args.
        """
    def size(self, name: str, index: int):
        """
        Hook called from template code to get the size of an arg.
        Will add needed args to pass it in if it is dynamic.
        """
    def stride(self, name, index):
        """
        Hook called from template code to get the stride of an arg.
        Will add needed args to pass it in if it is dynamic.
        """
    template_indices: Incomplete
    def store_output(self, indices, val, mask):
        """
        Hook called from template code to store the final output
        (if the buffer hasn't been optimized away), then append any
        epilogue fusions.
        """
    def make_load(self, name, indices, mask):
        """
        Optional helper called from template code to generate the code
        needed to load from an tensor.
        """
    def template_env(self):
        """
        Generate the namespace visible in the template.
        """
    def indexing(self, index: sympy.Expr, *, copy_shape: Incomplete | None = None, dense_indexing: bool = False):
        """
        Override the default indexing to use our custom mask and force
        dense indexing.
        """
    def initialize_range_tree(self, pid_cache) -> None: ...
    def call_kernel(self, code, name: str): ...

class TritonTemplate:
    index_counter: Incomplete
    all_templates: Incomplete
    name: Incomplete
    grid: Incomplete
    template: Incomplete
    debug: Incomplete
    def __init__(self, name: str, grid: Any, source: str, debug: bool = False) -> None: ...
    def generate(self, input_nodes, layout, num_stages, num_warps, prefix_args: int = 0, suffix_args: int = 0, epilogue_fn=..., **kwargs): ...
    @staticmethod
    def fake_get_dtype(fake_out): ...

class ExternKernelChoice:
    name: Incomplete
    cpp_kernel: Incomplete
    def __init__(self, kernel, cpp_kernel: Incomplete | None = None, *, name: Incomplete | None = None) -> None: ...
    def to_callable(self): ...
    def call_name(self): ...
    def hash_key(self): ...
    def bind(self, input_nodes, layout, **kwargs): ...

class ChoiceCaller:
    name: Incomplete
    layout: Incomplete
    input_nodes: Incomplete
    def __init__(self, name, input_nodes, layout) -> None: ...

class TritonTemplateCaller(ChoiceCaller):
    make_kernel_render: Incomplete
    def __init__(self, name, input_nodes, layout, make_kernel_render) -> None: ...
    def call_name(self): ...
    def to_callable(self): ...
    def hash_key(self): ...
    def output_node(self): ...

class ExternKernelCaller(ChoiceCaller):
    choice: Incomplete
    kwargs: Incomplete
    def __init__(self, choice: ExternKernelChoice, input_nodes, layout, kwargs: Incomplete | None = None) -> None: ...
    def to_callable(self): ...
    def hash_key(self): ...
    def output_node(self): ...

class AlgorithmSelectorCache(DiskCache):
    def __call__(self, choices: List[ChoiceCaller], input_nodes, layout): ...
    @classmethod
    def make_benchmark_fn(cls, choices, input_nodes, layout): ...
    @staticmethod
    def log_results(name, input_nodes, timings) -> None: ...
    @staticmethod
    def benchmark_example_value(node):
        """
        Convert an ir.Buffer into a concrete torch.Tensor we can use for
        benchmarking.
        """
    @staticmethod
    def key_of(node):
        """
        Extract the pieces of an ir.Buffer that we should invalidate cached
        autotuning results on.
        """

autotune_select_algorithm: Incomplete

def realize_inputs(*args): ...
