from _typeshed import Incomplete
from collections.abc import Generator
from jax._src import core as core, traceback_util as traceback_util
from jax._src.config import config as config
from jax._src.tree_util import tree_map as tree_map
from jax._src.util import curry as curry
from typing import Any, Callable, NamedTuple

class StoreException(Exception): ...
class EmptyStoreValue: ...

class Store:
    """Storage for a value, with checks for overwriting or reading empty store."""
    def __init__(self) -> None: ...
    def store(self, val) -> None: ...
    def reset(self) -> None: ...
    @property
    def val(self): ...
    def __nonzero__(self): ...
    __bool__ = __nonzero__

class EqualStore:
    def __init__(self) -> None: ...
    val: Incomplete
    def store(self, val) -> None: ...
    def reset(self) -> None: ...

class WrappedFun:
    """Represents a function `f` to which `transforms` are to be applied.

  Args:
    f: the function to be transformed.
    transforms: a list of `(gen, gen_static_args)` tuples representing
      transformations to apply to `f.` Here `gen` is a generator function and
      `gen_static_args` is a tuple of static arguments for the generator. See
      description at the start of this module for the expected behavior of the
      generator.
    stores: a list of out_store for the auxiliary output of the `transforms`.
    params: extra parameters to pass as keyword arguments to `f`, along with the
      transformed keyword arguments.
  """
    f: Incomplete
    transforms: Incomplete
    stores: Incomplete
    params: Incomplete
    in_type: Incomplete
    debug_info: Incomplete
    def __init__(self, f, transforms, stores, params, in_type, debug_info) -> None: ...
    def wrap(self, gen, gen_static_args, out_store) -> WrappedFun:
        """Add another transform and its store."""
    def populate_stores(self, stores) -> None:
        """Copy the values from the `stores` into `self.stores`."""
    def call_wrapped(self, *args, **kwargs):
        """Calls the underlying function, applying the transforms.

    The positional `args` and keyword `kwargs` are passed to the first
    transformation generator.
    """
    def __hash__(self): ...
    def __eq__(self, other): ...

def transformation(gen, fun: WrappedFun, *gen_static_args) -> WrappedFun:
    """Adds one more transformation to a WrappedFun.

  Args:
    gen: the transformation generator function
    fun: a WrappedFun on which to apply the transformation
    gen_static_args: static args for the generator function
  """
def transformation_with_aux(gen, fun: WrappedFun, *gen_static_args, use_eq_store: bool = False) -> tuple[WrappedFun, Any]:
    """Adds one more transformation with auxiliary output to a WrappedFun."""
def fun_name(f): ...
def wrap_init(f, params: Incomplete | None = None) -> WrappedFun:
    """Wraps function `f` as a `WrappedFun`, suitable for transformation."""
def annotate(f: WrappedFun, in_type: core.InputType | None) -> WrappedFun: ...

class TracingDebugInfo(NamedTuple):
    traced_for: str
    func_src_info: str
    arg_names: tuple[str, ...]
    result_paths: Callable[[], tuple[str, ...]] | None

def add_debug_info(f: WrappedFun, debug_info: TracingDebugInfo | None) -> WrappedFun:
    """Produce a new WrappedFun with debug_info attached."""
def cache(call: Callable):
    """Memoization decorator for functions taking a WrappedFun as first argument.

  Args:
    call: a Python callable that takes a WrappedFun as its first argument. The
      underlying transforms and params on the WrappedFun are used as part of the
      memoization cache key.

  Returns:
     A memoized version of ``call``.
  """

cache_clearing_funs: Incomplete

def clear_all_caches() -> None: ...
def hashable_partial(*args) -> Generator[Incomplete, None, None]: ...
def merge_linear_aux(aux1, aux2): ...
