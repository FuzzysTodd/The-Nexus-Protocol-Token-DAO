from _typeshed import Incomplete
from tensorflow.python.autograph.utils import py_func as py_func, tensors as tensors, type_registry as type_registry
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_parsing_ops as gen_parsing_ops, gen_string_ops as gen_string_ops, list_ops as list_ops, math_ops as math_ops, sort_ops as sort_ops

UNSPECIFIED: Incomplete
abs_registry: Incomplete
len_registry: Incomplete
enumerate_registry: Incomplete
zip_registry: Incomplete
map_registry: Incomplete
filter_registry: Incomplete
any_registry: Incomplete
all_registry: Incomplete
next_registry: Incomplete

def registry_lookup(reg, obj): ...
def overload_of(f): ...
def locals_in_original_context(caller_fn_scope):
    """Executes the locals function in the context of a specified function."""
def globals_in_original_context(caller_fn_scope):
    """Executes the locals function in the context of a specified function."""
def eval_in_original_context(f, args, caller_fn_scope):
    """Executes the eval function in the context of a specified function."""
def super_in_original_context(f, args, caller_fn_scope):
    """Executes the super function in the context of a specified function.

  See https://docs.python.org/3/library/functions.html#super for the exact
  details

  Args:
    f: Callable, typically the super builtin
    args: List[Any], the original call arguments
    caller_fn_scope: Optional[function_wrappers.FunctionScope], the function
      scope of the converted function in which this call was originally made

  Returns:
    The result of calling `f` as if it was called in the frame indicated by
      `caller_fn_scope`.
  """
def abs_(x): ...
def float_(x: int = 0): ...
def int_(x: int = 0, base=...): ...
def len_(s): ...
def print_(*objects, **kwargs):
    """Overload of the print builtin."""
def min_(*args, **kwargs): ...
def max_(*args, **kwargs): ...
def range_(start_or_stop, stop=..., step=...): ...
def enumerate_(s, start: int = 0): ...
def zip_(*iterables): ...
def map_(fn, *iterables): ...
def next_(iterator, default=...): ...
def next_py(iterator, default=...): ...
def filter_(function, iterable): ...
def any_(iterable): ...
def all_(iterable): ...
def sorted_(iterable, key=..., reverse=...): ...

SUPPORTED_BUILTINS: Incomplete
BUILTIN_FUNCTIONS_MAP: Incomplete
