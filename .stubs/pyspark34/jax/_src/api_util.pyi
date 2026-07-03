import inspect
from _typeshed import Incomplete
from collections.abc import Generator, Iterable
from jax._src import core as core, dtypes as dtypes, linear_util as lu, traceback_util as traceback_util
from jax._src.abstract_arrays import numpy_scalar_types as numpy_scalar_types
from jax._src.core import ShapedArray as ShapedArray
from jax._src.linear_util import TracingDebugInfo as TracingDebugInfo
from jax._src.tree_util import PyTreeDef as PyTreeDef, broadcast_prefix as broadcast_prefix, generate_key_paths as generate_key_paths, keystr as keystr, prefix_errors as prefix_errors, tree_flatten as tree_flatten, tree_map as tree_map, tree_structure as tree_structure, tree_unflatten as tree_unflatten, treedef_children as treedef_children
from jax._src.util import Hashable as Hashable, HashableFunction as HashableFunction, Unhashable as Unhashable, WrapKwArgs as WrapKwArgs, safe_map as safe_map
from typing import Any, Callable

map = safe_map

def flatten_fun(in_tree, *args_flat) -> Generator[Incomplete, Incomplete, None]: ...
def apply_flat_fun(fun, io_tree, *py_args): ...
def flatten_fun_nokwargs(in_tree, *args_flat) -> Generator[Incomplete, Incomplete, None]: ...
def apply_flat_fun_nokwargs(fun, io_tree, py_args): ...
def flattened_fun_in_tree(fn: lu.WrappedFun) -> tuple[PyTreeDef, Callable[[], PyTreeDef], bool] | None: ...
def flatten_fun_nokwargs2(in_tree, *args_flat) -> Generator[Incomplete, Incomplete, None]: ...

class _HashableWithStrictTypeEquality:
    """Box object used when comparing static arguments as a jit key.

  Requires exact type equality using `is` and value equality."""
    val: Incomplete
    def __init__(self, val) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...

def validate_argnums(sig: inspect.Signature, argnums: tuple[int, ...], argnums_name: str) -> None:
    """
  Validate that the argnums are sensible for a given function.

  For functions that accept a variable number of positions arguments
  (`f(..., *args)`) all positive argnums are considered valid.
  """
def validate_argnames(sig: inspect.Signature, argnames: tuple[str, ...], argnames_name: str) -> None:
    """
  Validate that the argnames are sensible for a given function.

  For functions that accept a variable keyword arguments
  (`f(..., **kwargs)`) all argnames are considered valid except those
  marked as position-only (`f(pos_only, /, ...)`).
  """
def argnums_partial(f, dyn_argnums, args, require_static_args_hashable: bool = True): ...
def argnums_partial_except(f: lu.WrappedFun, static_argnums: tuple[int, ...], args: tuple[Any, ...], *, allow_invalid: bool):
    """Version of ``argnums_partial`` that checks hashability of static_argnums."""
def argnames_partial_except(f: lu.WrappedFun, static_argnames: tuple[str, ...], kwargs: dict[str, Any]): ...
def donation_vector(donate_argnums, donate_argnames, args, kwargs) -> tuple[bool, ...]:
    """Returns a tuple with a boolean value for each leaf in args and kwargs.

  What if a user specifies donate_argnums but calls the function with kwargs
  or vice-versa? In that case, in `resolve_argnums` using the signature of the
  function, the counterpart (donate_argnames or donate_argnums respectively) is
  calculated so when this function is called both donate_argnums and
  donate_argnames are available. This allows JAX to donate kwargs when only
  donate_argnums is specified and vice-versa.

  When both donate_argnums and donate_argnames are specified, only the args and
  kwargs specified are donated.
  """
def rebase_donate_argnums(donate_argnums, static_argnums) -> tuple[int, ...]:
    """Shifts donate to account for static.

  >>> rebase_donate_argnums((3, 4), (0, 1))
  (1, 2)

  Args:
    donate_argnums: An iterable of ints.
    static_argnums: An iterable of ints.

  Returns:
    A tuple of unique, sorted integer values based on donate_argnums with each
    element offset to account for static_argnums.
  """
def is_hashable(arg): ...
def flatten_axes(name, treedef, axis_tree, *, kws: bool = False, tupled_args: bool = False): ...
def flat_out_axes(f: lu.WrappedFun, out_spec: Any) -> tuple[lu.WrappedFun, Callable]: ...
def check_callable(fun) -> None: ...
def infer_argnums_and_argnames(sig: inspect.Signature, argnums: int | Iterable[int] | None, argnames: str | Iterable[str] | None) -> tuple[tuple[int, ...], tuple[str, ...]]:
    """Infer missing argnums and argnames for a function with inspect."""
def resolve_argnums(fun, donate_argnums, donate_argnames, static_argnums, static_argnames) -> tuple[tuple[int, ...], tuple[str, ...], tuple[int, ...], tuple[str, ...]]: ...
def assert_no_intersection(static_argnames, donate_argnames) -> None: ...
def shaped_abstractify(x): ...
def api_hook(fun, tag: str): ...
def debug_info(traced_for: str, fun: Callable, args: tuple[Any], kwargs: dict[str, Any], static_argnums: tuple[int, ...], static_argnames: tuple[str, ...]) -> TracingDebugInfo | None:
    """Try to build trace-time debug info for fun when applied to args/kwargs."""
def fun_sourceinfo(fun: Callable) -> str | None: ...
def result_paths(*args, **kwargs) -> Generator[Incomplete, Incomplete, None]:
    """linear_util transform to get output pytree paths of pre-flattened function."""
def jaxpr_debug_info(jaxpr: core.Jaxpr, trace_debug: TracingDebugInfo | None, result_paths: tuple[str | None, ...] | None = None) -> core.Jaxpr:
    """Add debug info to jaxpr, given trace-time debug info and result paths."""
def debug_info_final(f: lu.WrappedFun, dbg: TracingDebugInfo | None, res_paths: Callable[[], tuple[str, ...]]) -> lu.WrappedFun:
    """Attach trace-time debug info and result paths lazy thunk to an lu.WrappedFun"""
