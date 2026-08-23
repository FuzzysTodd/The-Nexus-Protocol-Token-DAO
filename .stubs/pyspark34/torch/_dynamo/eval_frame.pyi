import contextlib
import torch
from . import config as config, convert_frame as convert_frame, skipfiles as skipfiles, utils as utils
from .backends.registry import CompilerFn as CompilerFn, lookup_backend as lookup_backend
from .exc import ResetRequired as ResetRequired
from .hooks import Hooks as Hooks
from .mutation_guard import install_generation_tagging_init as install_generation_tagging_init
from .types import DynamoCallback as DynamoCallback
from .utils import compile_times as compile_times
from _typeshed import Incomplete
from enum import Enum
from torch._C._dynamo.eval_frame import reset_code as reset_code, set_eval_frame as set_eval_frame, set_guard_error_hook as set_guard_error_hook, set_guard_fail_hook as set_guard_fail_hook, skip_code as skip_code, unsupported as unsupported
from torch.fx.experimental import proxy_tensor as proxy_tensor
from torch.fx.experimental.proxy_tensor import make_fx as make_fx
from torch.nn.parallel.distributed import DistributedDataParallel as DistributedDataParallel

log: Incomplete
always_optimize_code_objects: Incomplete
null_context = contextlib.nullcontext

class Unset(Enum):
    token: int

unset: Incomplete
compile_lock: Incomplete
most_recent_backend: CompilerFn | None

class OptimizedModule(torch.nn.Module):
    """
    Wraps the original nn.Module object and later patches its
    forward method to optimized self.forward method.
    """
    dynamo_ctx: Incomplete
    def __init__(self, mod, dynamo_ctx) -> None: ...
    def __getattr__(self, name): ...
    def forward(self, *args, **kwargs): ...

def remove_from_cache(f) -> None:
    """
    Make sure f.__code__ is not cached to force a recompile
    """
def nothing() -> None: ...
def innermost_fn(fn):
    """
    In case of nesting of _TorchDynamoContext calls, find the innermost
    function. TorchDynamo caches on fn.__code__ object, so its necessary to find
    the innermost function to pass on the optimize, run, disable etc.
    """
def enable_dynamic(enable: bool = True): ...

class _TorchDynamoContext:
    callback: Incomplete
    prior: Incomplete
    on_enter: Incomplete
    extra_ctx_ctor: Incomplete
    first_ctx: Incomplete
    dynamic: Incomplete
    def __init__(self, callback: DynamoCallback, on_enter=..., backend_ctx_ctor=..., patch_fn=..., first_ctx: bool = False, *, dynamic: bool = False) -> None: ...
    backend_ctx: Incomplete
    dynamic_ctx: Incomplete
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def __call__(self, fn): ...

class OptimizeContext(_TorchDynamoContext):
    def __init__(self, callback, backend_ctx_ctor, first_ctx: bool = False, *, dynamic: bool = False) -> None: ...

class RunOnlyContext(_TorchDynamoContext):
    def __init__(self) -> None: ...

class DisableContext(_TorchDynamoContext):
    def __init__(self) -> None: ...

def catch_errors_wrapper(callback, hooks: Hooks): ...
def get_compiler_fn(compiler_fn): ...

class _NullDecorator(contextlib.nullcontext):
    def __call__(self, fn): ...

def check_if_dynamo_supported() -> None: ...
def optimize(backend: str = 'inductor', *, nopython: bool = False, guard_export_fn: Incomplete | None = None, guard_fail_fn: Incomplete | None = None, disable: bool = False, dynamic: bool = False):
    '''
    The main entrypoint of TorchDynamo.  Do graph capture and call
    backend() to optimize extracted graphs.

    Args:
        backend: One of the two things:
            - Either, a function/callable taking a torch.fx.GraphModule and
            example_inputs and returning a python callable that runs the
            graph faster.
            One can also provide additional context for the backend, like
            torch.jit.fuser("fuser2"), by setting the backend_ctx_ctor attribute.
            See AOTAutogradMemoryEfficientFusionWithContext for the usage.
            - Or, a string backend name in `torch._dynamo.list_backends()`
        nopython: If True, graph breaks will be errors and there will
            be a single whole-program graph.
        disable: If True, turn this decorator into a no-op
        dynamic: If True, turn on dynamic shapes support

    Example Usage::

        @torch._dynamo.optimize()
        def toy_example(a, b):
            ...
    '''
def explain(f, *args, **kwargs): ...
def export(f, *args, aten_graph: bool = False, decomposition_table: Incomplete | None = None, tracing_mode: str = 'real', **kwargs): ...
def assume_constant_result(fn): ...
def optimize_assert(backend, *, hooks=..., export: bool = False, dynamic: bool = False):
    """
    The same as `torch._dynamo.optimize(backend, nopython=True)`
    """
def run(fn: Incomplete | None = None):
    """Don't do any dynamic compiles, just use prior optimizations"""
def disable(fn: Incomplete | None = None):
    """Decorator and context manager to disable TorchDynamo"""
def skip(fn: Incomplete | None = None):
    """
    Skip frames associated with the function code, but still process recursively
    invoked frames
    """

class TorchPatcher:
    @staticmethod
    def patch() -> None: ...
    @staticmethod
    def suppress_torch_distributed_warnings(fn): ...
