import dataclasses
import torch
import torch.nn as nn
from . import config as config
from .partitioners import default_partition as default_partition
from _typeshed import Incomplete
from collections.abc import Generator
from dataclasses import dataclass
from torch import Tensor as Tensor
from torch._dispatch.python import enable_python_dispatcher as enable_python_dispatcher
from torch._dynamo.utils import dynamo_timed as dynamo_timed
from torch._guards import DuplicateInputs as DuplicateInputs, TracingContext as TracingContext
from torch._subclasses import CrossRefFakeMode as CrossRefFakeMode, FakeTensor as FakeTensor, FakeTensorMode as FakeTensorMode
from torch.fx import Interpreter as Interpreter, immutable_collections as immutable_collections
from torch.fx.experimental.proxy_tensor import is_sym_node as is_sym_node, py_sym_types as py_sym_types
from torch.fx.experimental.symbolic_shapes import ShapeEnv as ShapeEnv
from torch.multiprocessing.reductions import StorageWeakRef as StorageWeakRef
from torch.nn.utils import stateless as stateless
from typing import Any, Callable, Dict, List, Tuple

log: Incomplete
MutationType: Incomplete
OutputType: Incomplete
aten: Incomplete
AOT_COUNTER: Incomplete
KNOWN_TYPES: Incomplete

def preserve_rng_state() -> Generator[None, None, None]: ...

callback_set: bool

def setup_stacktrace_preservation_hooks(roots: List): ...

@dataclass(frozen=True)
class OutputAliasInfo:
    output_type: OutputType
    base_idx: int | None
    def __init__(self, output_type, base_idx) -> None: ...

@dataclass(frozen=True)
class InputAliasInfo:
    is_leaf: bool
    mutates_data: bool
    mutates_metadata: bool
    def __init__(self, is_leaf, mutates_data, mutates_metadata) -> None: ...

@dataclass()
class ViewAndMutationMeta:
    input_info: List[InputAliasInfo]
    output_info: List[OutputAliasInfo]
    requires_grad_info: List[bool]
    num_intermediate_bases: int
    keep_input_mutations: int
    mutated_inp_indices = ...
    aliased_out_indices = ...
    def __post_init__(self) -> None: ...
    def __init__(self, input_info, output_info, requires_grad_info, num_intermediate_bases, keep_input_mutations) -> None: ...

@dataclass(frozen=True)
class TensorAlias:
    alias: torch.Tensor
    def __init__(self, alias) -> None: ...

def has_same_metadata(t1, t2): ...
def gen_alias_from_base(aliased_base_tensor, target_meta_tensor, target_requires_grad): ...
def to_fun(t): ...
def from_fun(t): ...
def run_functionalized_fw_and_collect_metadata(f, *, keep_input_mutations: bool) -> Tuple[ViewAndMutationMeta, List[Any]]: ...
def unpack_synthetic_bases(primals: List[Any], synthetic_base_info: List[int | Tuple[int, torch.Tensor]] | None) -> List[Any]: ...

@dataclass
class CompiledRuntimeMetadata:
    synthetic_base_info: List[int | Tuple[int, torch.Tensor]] | None
    fw_metadata: ViewAndMutationMeta
    num_outputs = ...
    num_outputs_non_aliased = ...
    num_outputs_aliased_to_inputs = ...
    num_outputs_aliased_to_intermediates = ...
    num_outputs_aliased = ...
    num_mutated_data_inputs = ...
    num_mutated_metadata_inputs = ...
    num_mutated_metadata_only_inputs = ...
    num_mutated_inputs = ...
    def __post_init__(self) -> None: ...
    def __init__(self, synthetic_base_info, fw_metadata) -> None: ...

def maybe_to_fresh_input(idx, t, meta): ...
def forward_or_joint(fn: Callable, primals_before_cloning: List[Any], primals_after_cloning: List[Any], maybe_tangents: List[Any] | None, meta: CompiledRuntimeMetadata, keep_input_mutations: bool) -> Any: ...
def flat_fn_with_synthetic_bases_expanded(fn: Callable, primals_before_cloning: List[Any], primals_after_cloning: List[Any], maybe_tangents: List[Any] | None, meta: CompiledRuntimeMetadata, keep_input_mutations: bool): ...
def flat_fn_no_input_mutations(fn: Callable, primals: List[Any], maybe_tangents: List[Any] | None, meta: CompiledRuntimeMetadata, keep_input_mutations: bool): ...
def create_forward_or_joint_functionalized(fn, *, meta: CompiledRuntimeMetadata, trace_joint: bool, keep_input_mutations: bool): ...
def normalize_as_list(x): ...

aot_autograd_decompositions: Incomplete
graph_being_compiled: List[str]
nth_graph: int
model_name: str

def set_model_name(name) -> None: ...
def get_aot_compilation_context() -> Tuple[List[str], str, int]: ...
def get_aot_graph_name() -> str:
    """
    Returns the name of the graph being compiled.
    """
get_graph_being_compiled = get_aot_graph_name

def track_graph_compiling(aot_config, graph_name) -> Generator[None, None, None]: ...
def make_boxed_func(f): ...
def make_boxed_compiler(compiler): ...
def call_func_with_args(f, args, steal_args: bool = False, disable_amp: bool = False): ...

@dataclasses.dataclass
class AOTConfig:
    """
    Configuration for AOTDispatcher
    """
    fw_compiler: Callable
    bw_compiler: Callable
    partition_fn: Callable
    decompositions: Dict[Callable, Callable]
    num_params_buffers: int
    aot_id: int
    keep_inference_input_mutations: bool
    def __init__(self, fw_compiler, bw_compiler, partition_fn, decompositions, num_params_buffers, aot_id, keep_inference_input_mutations) -> None: ...

def aot_dispatch_base(flat_fn, flat_args: List[Tensor], aot_config: AOTConfig): ...
def assert_functional_graph(fx_g: torch.fx.Graph): ...
def disable_autocast_manager() -> Generator[None, None, None]: ...
def are_differentiable_views(view1, view2): ...
def same_dtype_views(view1, view2): ...
def merge_view_inputs(fwd_inputs: List[Any], mutated_input_info: List[InputAliasInfo], *, is_inference: bool) -> Tuple[List[Any], List[int | Tuple[int, torch.Tensor]] | None]: ...
def format_guard_bug_msg(aot_config, expected): ...
def aot_wrapper_dedupe(flat_fn, flat_args: List[Tensor], aot_config: AOTConfig, *, compiler_fn): ...
def describe_input(i, aot_config): ...
def create_runtime_wrapper(compiled_fn, *, runtime_metadata: CompiledRuntimeMetadata, trace_joint: bool, keep_input_mutations: bool): ...
def aot_dispatch_autograd(flat_fn, flat_args: List[Any], aot_config: AOTConfig): ...
def create_aot_dispatcher_function(flat_fn, flat_args: List[Any], aot_config: AOTConfig):
    """
    Traces the forward and backward graphs of the attr:`flat_fn` to generate a
    joint graph. The joint graph is an Fx graph with Aten ops. Please refer to
    the tracing mechanism to understand the graph capturing details.

    The joint graph is then passed through attr:`partition_fn` to isolate the
    forward and backward portions, which are then respectively compiled via the
    provided attr:`fw_compiler` and attr:`bw_compiler`.

    The resulting compiled forward and backward graphs are then wrapped up in a
    ``torch.autograd.Function`` object.

    The calling convention here is that the first aot_config.num_params_buffers
    inputs in flat_args are parameters and buffers, and the rest are inputs.

    We use this to assume that parameters/buffer's shapes don't change.
    """

class PytreeThunk:
    spec: Incomplete
    is_simple: Incomplete
    is_really_simple: Incomplete
    def set(self, spec) -> None: ...
    def unflatten(self, x): ...

def aot_function(fn: Callable, fw_compiler: Callable, bw_compiler: Callable | None = None, partition_fn: Callable = ..., decompositions: Dict | None = None, num_params_buffers: int = 0, hasher_type: Incomplete | None = None, static_argnums: Tuple[int] | None = None, keep_inference_input_mutations: bool = False) -> Callable:
    """
    Traces the forward and backward graph of :attr:`fn` using torch dispatch
    mechanism, and then compiles the generated forward and backward graphs
    through :attr:`fw_compiler` and :attr:`bw_compiler`.

    :func:`aot_function` traces the forward and backward graph ahead of time,
    and generates a joint forward and backward graph.  :attr:`partition_fn` is
    then used to separate out forward and backward graphs. The partitioner
    function can be used to perform optimizations such as recomputation. One can
    set `decompositions` dictionary to decompose the operators into a sequence
    of core or simpler operators supported by the backend compilers.

    :func:`aot_function` uses a compilation cache, based on input tensor
    properties, to detect when there is a need of recompilation.

    .. warning::
        This API is experimental and likely to change.

    Args:
        fn (Callable): A Python function that takes one ore more arguments. Must
            return one or more Tensors.
        fw_compiler (Callable): A Python function that accepts an Fx graph with
            Aten ops and input args, and returns a Callable that semantically is
            equivalent to the input Fx graph.
        bw_compiler (Optional[Callable]): A Python function that accepts an
            Fx graph with Aten ops and input args, and returns a Callable that
            semantically is equivalent to the input Fx graph.  Default: None
            (when None, it defaults to the :attr:`fw_compiler`)
        partition_fn (Callable): A Python function that takes a joint forward
            and backward graph, and partitions it into separate forward and
            backward graphs.
        decompositions (Dict): A dictionary to define the decomposition of
            larger Aten ops into simpler or core Aten ops.

    Returns:
        Returns a ``Callable`` that retains the eager behavior of the original
        :attr:`fn`, but with forward and backward graph compiled via
        :attr:`fw_compile` and :attr:`bw_compile`.

    A simple example usage of :func:`aot_function` is as follows. This example
    will print the forward and backward graphs of the function ``fn``

        >>> fn = lambda x : x.sin().cos()
        >>> def print_compile_fn(fx_module, args):
        >>>     print(fx_module)
        >>>     return fx_module
        >>> aot_fn = aot_function(fn, print_compile_fn)
        >>> x = torch.randn(4, 5, requires_grad=True)
        >>> aot_fn(x)
    """
def aot_module(mod: nn.Module, *args, **kwargs) -> nn.Module:
    """
    Traces the forward and backward graph of :attr:`mod` using torch dispatch
    tracing mechanism. It is wrapper function, that underneath uses
    :func:`aot_function` to perform tracing and compilation.

    :func:`aot_module` lifts the parameters and buffers of ``nn.Module`` as inputs
    to a new callable which is then compiled through :func:`aot_function`.

    .. warning::
        This API is experimental and likely to change.

    Args:
        mod (Callable): A ``nn.Module`` module.
        args : args to be passed to :func:`aot_function`
        kwargs : kwargs to be passed to :func:`aot_function`

    Returns:
        Returns a ``nn.Module`` that retains the eager behavior of the original
        :attr:`mod`, but with forward and backward graph compiled.

    """
def aot_module_simplified(mod: nn.Module, args, fw_compiler: Callable, bw_compiler: Callable | None = None, partition_fn: Callable = ..., decompositions: Dict | None = None, hasher_type: Incomplete | None = None, static_argnums: Incomplete | None = None, keep_inference_input_mutations: bool = False) -> nn.Module:
    """
    This is the simplified or low overhead version of aot_module. For frontends
    like TorchDynamo, the input functions/modules to AOT are static and have
    unpacked inputs/outputs. This gives us an opportunity to remove the
        (1) pytree overhead to parse inputs/outputs,
        (2) AOT Autograd cache,
        (3) Reading of params/buffers in every forward call

    :func:`aot_module_simplified` removes these overheads.
    """
compiled_function = aot_function
compiled_module = aot_module
