import dataclasses
import torch.fx
import types
from . import config as config
from _typeshed import Incomplete
from collections.abc import Generator
from torch import fx as fx
from torch._dispatch.python import enable_python_dispatcher as enable_python_dispatcher
from torch._subclasses import FakeTensorMode as FakeTensorMode, UnsupportedFakeTensorException as UnsupportedFakeTensorException
from torch._subclasses.fake_tensor import FakeTensor as FakeTensor
from torch.nn.modules.lazy import LazyModuleMixin as LazyModuleMixin
from torch.utils._pytree import tree_flatten as tree_flatten, tree_map as tree_map
from typing import Any, Dict, List

HAS_NUMPY: bool
counters: Incomplete
troubleshooting_url: str
log: Incomplete
compilation_metrics: Incomplete
timer_counter: Incomplete

def tabulate(rows, headers): ...
def dynamo_profiled(func): ...

frame_phase_timing: Incomplete
curr_frame: int

def increment_frame() -> None: ...
def reset_frame_count() -> None: ...

op_count: int

def increment_op_count(cnt) -> None: ...
def print_time_report() -> None: ...
def dynamo_timed(original_function: Incomplete | None = None, phase_name: Incomplete | None = None): ...
def compile_times(repr: str = 'str', aggregate: bool = False):
    """
    Get metrics about torchdynamo frontend/backend compilation times.

    Accumulates information from functions tagged with `@dynamo_timed`.

    repr='str' returns a printable string for user interaction, and 'csv'
    returns headers, rows which can be logged for output

    aggregate causes values from multiple compilations (e.g. split graphs)
    to be accumulated into one value.  If false, expect more than one value
    per metric.
    """

tensortype_to_dtype: Incomplete

class DuplicateWarningChecker:
    maxsize: Incomplete
    def __init__(self, maxsize: int = 4096) -> None: ...
    set: Incomplete
    def reset(self) -> None: ...
    def add(self, key): ...

graph_break_dup_warning_checker: Incomplete

def init_logging() -> None: ...
def format_graph_tabular(graph): ...
def format_bytecode(prefix, name, filename, line_no, code): ...
def gen_record_file_name(exc, code): ...
def write_record_to_file(filename, exec_record) -> None: ...
def count_calls(g: fx.Graph): ...
def identity(x): ...
def nothing(*args, **kwargs) -> None: ...

class ExactWeakKeyDictionary:
    """Similar to weakref.WeakKeyDictionary, but use `is`/`id` rather than `==` to compare equality"""
    values: Incomplete
    refs: Incomplete
    def __init__(self) -> None: ...
    def __getitem__(self, key): ...
    def get(self, key, default: Incomplete | None = None): ...
    def __contains__(self, key) -> bool: ...
    def __setitem__(self, key, value) -> None: ...
    def clear(self) -> None: ...

def istype(obj, allowed_types):
    """isinstance() without subclasses"""
def is_typing(value): ...
def is_numpy_int_type(value): ...
def is_numpy_float_type(value): ...
def is_numpy_ndarray(value): ...
def istensor(obj):
    """Check of obj is a tensor"""
def is_lazy_module(mod): ...
def print_once(*args) -> None: ...
def make_cell(val: Incomplete | None = None):
    """Some black magic to create a cell object that usually only exists in a closure"""
def proxy_args_kwargs(args, kwargs): ...

@dataclasses.dataclass
class CleanupHook:
    """Remove a global variable when hook is called"""
    scope: Dict[str, Any]
    name: str
    def __call__(self, *args) -> None: ...
    @staticmethod
    def create(scope, name, val): ...
    def __init__(self, scope, name) -> None: ...

class CleanupManager(ExactWeakKeyDictionary):
    count: int

def clone_tensor(x):
    """Clone the tensor and its gradient"""
def clone_input(x):
    """copy while preserving strides"""
def clone_inputs(example_inputs): ...
def preserve_rng_state() -> Generator[None, None, None]: ...
def is_jit_model(model0): ...
def torchscript(model, example_inputs, verbose: bool = False): ...
def getfile(obj): ...
def is_namedtuple(obj):
    """Test if an object is a namedtuple or a torch.return_types.* quasi-namedtuple"""
def is_namedtuple_cls(cls):
    """Test if an object is a namedtuple or a torch.return_types.* quasi-namedtuple"""
def namedtuple_fields(cls):
    """Get the fields of a namedtuple or a torch.return_types.* quasi-namedtuple"""
def checkpoint_params(gm): ...
def timed(model, example_inputs, times: int = 1): ...
def check_is_cuda(gm, example_inputs): ...
def rot_n_helper(n): ...
def is_safe_constant(v): ...
def check_constant_args(args, kwargs): ...
def check_unspec_python_args(args, kwargs): ...
def specialize_args_kwargs(tx, args, kwargs): ...

dict_values: Incomplete
odict_values: Incomplete
tuple_iterator: Incomplete
tuple_iterator_len: Incomplete
object_new: Incomplete

def product(it): ...
def tuple_iterator_getitem(it, index): ...
def enum_repr(value): ...
def dict_param_key_ids(value): ...
def dict_const_keys(value): ...
def dict_const_keys_repr(const_keys): ...
def global_key_name(key): ...
def rename_implicit(v):
    '''
    Usage of inline comprehensions generates a implicit ".0" variable that
    trips up guard generation.  This renames these variables in guards.
    '''
def wrap_fake_exception(fn): ...
def deepcopy_to_fake_tensor(obj, fake_mode): ...
def rmse(ref, res):
    """
    Calculate root mean squared error
    """
def same(ref, res, fp64_ref: Incomplete | None = None, cos_similarity: bool = False, tol: float = 0.0001, equal_nan: bool = False, exact_dtype: bool = True, relax_numpy_equality: bool = False):
    """Check correctness to see if ref and res match"""
def format_func_info(code): ...
def disable_cache_limit() -> Generator[None, None, None]: ...

orig_code_map: Incomplete
guard_failures: Incomplete

class CompileProfiler:
    """Utility for profiling how and what dynamo would compile.

    Can be used for
     * diagnosing recompilation issues
     * determining an appropriate compile cache limit
     * (TODO)confirming which functions got compiled/skipped
    """
    frame_count: int
    op_count: int
    backend_ctx_ctor: Incomplete
    def __init__(self) -> None: ...
    def __call__(self, gm: torch.fx.GraphModule, example_inputs): ...
    def get_metrics(self): ...
    def report(self): ...

def get_debug_dir(): ...
def get_fake_value(node, tx):
    """
    Run the computation represented by `node` using fake tensors and return the result.
    """
def run_node(output_graph, node, args, kwargs, nnmodule):
    """
    Runs a given node, with the given args and kwargs.

    Behavior is dicatated by a node's op.

    run_node is useful for extracting real values out of nodes.
    See get_real_value for more info on common usage.

    Note: The output_graph arg is only used for 'get_attr' ops
    Note: The nnmodule arg is only used for 'call_module' ops

    Nodes that are not call_function, call_method, call_module, or get_attr will
    raise an AssertionError.
    """
def get_real_value(node, output_graph):
    """
    Run the actual computation represented by `node` and return the result.
    This will execute any dependent nodes in the graph as well.
    """
def assert_no_fake_params_or_buffers(gm): ...
def fake_mode_from_tensors(inputs: List[Any]):
    """
    Takes a list of anything, unflattened is fine, returns a fake_mode
    if any are fake. All fake modes on all fake tensors must be identical.
    Returns None if no fake_mode is fine
    """
def fqn(obj: Any):
    """
    Returns the fully qualified name of the object.
    """
def ifdyn(count1, count2): ...
def import_submodule(mod: types.ModuleType):
    """
    Ensure all the files in a given submodule are imported
    """
