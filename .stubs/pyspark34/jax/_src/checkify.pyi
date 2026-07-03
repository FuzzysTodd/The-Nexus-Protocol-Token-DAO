import dataclasses
import numpy as np
from _typeshed import Incomplete
from collections.abc import Generator, Sequence
from jax import dtypes as dtypes, lax as lax
from jax._src import api as api, core as core, custom_derivatives as custom_derivatives, effects as effects, pjit as pjit, sharding_impls as sharding_impls, source_info_util as source_info_util, traceback_util as traceback_util
from jax._src.ad_util import SymbolicZero as SymbolicZero
from jax._src.api_util import flatten_fun as flatten_fun
from jax._src.config import config as config
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir
from jax._src.tree_util import tree_flatten as tree_flatten, tree_map as tree_map, tree_unflatten as tree_unflatten
from jax._src.typing import Array as Array
from jax._src.util import HashableWrapper as HashableWrapper, as_hashable_function as as_hashable_function, safe_map as safe_map, safe_zip as safe_zip, split_list as split_list, unzip3 as unzip3, weakref_lru_cache as weakref_lru_cache
from typing import Any, Callable, TypeVar

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
Bool = bool | Array
Int = int | Array
ErrorCategory: Incomplete
Payload = list[np.ndarray | Array]
PyTreeDef: Incomplete
Out = TypeVar('Out')

def popattr(obj, attrname): ...
def setnewattr(obj, name, val) -> None: ...

class JaxException(Exception):
    """Python exception which can contain an error message with JAX run-time info."""
    traceback_info: Incomplete
    def __init__(self, traceback_info) -> None: ...
    def __init_subclass__(cls) -> None: ...
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, metadata, payload): ...
    def get_effect_type(self) -> ErrorEffect: ...

@dataclasses.dataclass(eq=True, frozen=True)
class ErrorEffect(effects.Effect):
    error_type: type[JaxException]
    shape_dtypes: tuple[api.ShapeDtypeStruct, ...]
    def __lt__(self, other: ErrorEffect): ...
    def __init__(self, error_type, shape_dtypes) -> None: ...

class DivisionByZeroError(JaxException):
    def get_effect_type(self): ...

class NaNError(JaxException):
    prim: Incomplete
    def __init__(self, traceback_info, primitive_name) -> None: ...
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, metadata, _): ...
    def get_effect_type(self): ...

class OOBError(JaxException):
    prim: Incomplete
    operand_shape: Incomplete
    def __init__(self, traceback_info, primitive_name, operand_shape, payload) -> None: ...
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, metadata, payload): ...
    def get_effect_type(self): ...

class FailedCheckError(JaxException):
    fmt_string: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, traceback_info, fmt_string, *a, **k) -> None: ...
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, metadata, payload): ...
    def get_effect_type(self): ...

@dataclasses.dataclass
class BatchedError(JaxException):
    error_mapping: dict[tuple[int, ...], JaxException]
    def __post_init__(self) -> None: ...
    def __init__(self, error_mapping) -> None: ...

@dataclasses.dataclass(frozen=True)
class Error:
    def get(self) -> str | None:
        """Returns error message if error happened, None if no error happened."""
    def get_exception(self) -> JaxException | None:
        """Returns Python exception if error happened, None if no error happened."""
    def throw(self) -> None: ...
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, metadata, data): ...
    def __init__(self, _pred, _code, _metadata, _payload) -> None: ...

init_error: Incomplete
next_code: Incomplete

def assert_func(error: Error, pred: Bool, new_error: JaxException) -> Error: ...
def update_error(error, pred, code, metadata, payload, effect_type): ...
def default_checkify_rule(primitive: core.Primitive, error: Error, enabled_errors, *invals: core.Value, **params: Any) -> tuple[Error, Sequence[core.Value]]:
    """Default rule for primitives in `checkify` interpreter."""
def get_shaped_aval(val): ...
def checkify_jaxpr(jaxpr: core.ClosedJaxpr, enabled_errors, error: Error, *args) -> tuple[Error, list[core.Value]]: ...
def checkify_jaxpr_flat(jaxpr: core.Jaxpr, consts: Sequence[core.Value], enabled_errors, err_tree: PyTreeDef, *args: core.Value) -> tuple[Error, list[Any]]: ...
def checkify_jaxpr_flat_hashable(jaxpr, hashable_consts, enabled_errors, err_tree, *args): ...
def flatten_fun_output(*args) -> Generator[Incomplete, Incomplete, None]: ...

check_p: Incomplete

class JaxRuntimeError(ValueError): ...

def check_impl(*args, err_tree, debug): ...
def check_abstract_eval(*args, err_tree, debug): ...

functionalization_error: Incomplete

def check_lowering_rule(ctx, *args, err_tree, debug): ...
def check_lowering_rule_unsupported(*a, debug, **k): ...
def python_err(err_tree, *args): ...
def check_batching_rule(batched_args, batch_dims, *, err_tree, debug): ...
def check_jvp_rule(primals, _, *, err_tree, debug): ...
ErrorCheckRule = Callable
error_checks: dict[core.Primitive, ErrorCheckRule]

def get_traceback(): ...
def nan_error_check(prim, error, enabled_errors, *in_vals, **params): ...
def check_nans(prim, error, enabled_errors, out): ...

nan_primitives: Incomplete

def dynamic_slice_error_check(error, enabled_errors, operand, *start_indices, slice_sizes): ...
def dynamic_update_slice_error_check(error, enabled_errors, operand, update, *start_indices): ...
def gather_error_check(error, enabled_errors, operand, start_indices, *, dimension_numbers, slice_sizes, unique_indices, indices_are_sorted, mode, fill_value): ...
def div_error_check(error, enabled_errors, x, y):
    """Checks for division by zero and NaN."""
def oob_payload(oob_mask, indices, dims_map, operand_shape): ...
def scatter_oob(operand, indices, updates, dnums): ...
def scatter_error_check(prim, error, enabled_errors, operand, indices, updates, *, update_jaxpr, update_consts, dimension_numbers, indices_are_sorted, unique_indices, mode):
    """Checks if indices are within bounds and update does not generate NaN."""
def jaxpr_to_checkify_jaxpr(jaxpr: core.ClosedJaxpr, enabled_errors, err_tree: PyTreeDef, *flat_err_and_in_vals) -> tuple[core.ClosedJaxpr, PyTreeDef, set[ErrorEffect]]: ...
def cond_error_check(error: Error, enabled_errors, index, *ops, branches, linear): ...
def scan_error_check(error, enabled_errors, *in_flat, reverse, length, jaxpr, num_consts, num_carry, linear, unroll): ...
def checkify_while_body_jaxpr(cond_jaxpr: core.ClosedJaxpr, body_jaxpr: core.ClosedJaxpr, enabled_errors, error: Error, c_consts_num: int) -> tuple[core.ClosedJaxpr, PyTreeDef, set[ErrorEffect]]: ...
def ignore_error_output_jaxpr(jaxpr, num_error_vals):
    """Constructs a checked jaxpr which does not output its error value."""
def while_loop_error_check(error, enabled_errors, *in_flat, cond_nconsts, cond_jaxpr, body_nconsts, body_jaxpr): ...
def pjit_error_check(error, enabled_errors, *vals_in, jaxpr, in_shardings, out_shardings, resource_env, donated_invars, name, inline, keep_unused): ...
def custom_jvp_call_rule(in_err, enabled_errors, *in_vals, num_consts, jvp_jaxpr_thunk, call_jaxpr, **params): ...
def lift_jvp(num_errs, num_consts, jvp_jaxpr_thunk): ...
def custom_vjp_call_jaxpr_rule(in_err, enabled_errors, *in_vals, fun_jaxpr, fwd_jaxpr_thunk, num_consts, bwd, out_trees, symbolic_zeros): ...
def check_discharge_rule(error, enabled_errors, *args, err_tree, debug): ...

user_checks: Incomplete
nan_checks: Incomplete
index_checks: Incomplete
div_checks: Incomplete
float_checks: Incomplete
automatic_checks: Incomplete
all_checks: Incomplete

def checkify(f: Callable[..., Out], errors: frozenset[ErrorCategory] = ...) -> Callable[..., tuple[Error, Out]]:
    """Functionalize `check` calls in `fun`, and optionally add run-time error checks.

  Run-time errors are either user-added :func:`~check` assertions, or
  automatically added checks like NaN checks, depending on the ``errors``
  argument.

  The returned function will return an Error object `err` along with the output
  of the original function. ``err.get()`` will either return ``None`` (if no
  error occurred) or a string containing an error message. This error message
  will correspond to the first error which occurred. ``err.throw()`` will raise
  a ValueError with the error message if an error occurred.

  By default only user-added :func:`~check` assertions are enabled. You can
  enable automatic checks through the ``errors`` argument.

  The automatic check sets which can be enabled, and when an error is generated:
    - ``user_checks``: a :func:`~check` evaluated to False.
    - ``nan_checks``: a floating-point operation generated a NaN value
      as output.
    - ``div_checks``: a division by zero.
    - ``index_checks``: an index was out-of-bounds.

  Multiple categories can be enabled together by passing in an error `Set` (eg.
  ``errors=nan_checks``). Multiple sets can be re-combined (eg.
  ``errors=float_checks|user_checks``)

  Args:
    fun: Callable which can contain user checks (see :func:`~check`).
    errors: A set of ErrorCategory values which defines the set of enabled
      checks. By default only explicit ``checks`` are enabled
      (``user_checks``). You can also for example enable NAN and
      DIV errors by passing the ``float_checks`` set, or for
      example combine multiple sets through set operations
      (``float_checks | user_checks``)
  Returns:
    A function which accepts the same arguments as ``fun`` and returns as output
    a pair where the first element is an ``Error`` value, representing the first
    failed :func:`~check`, and the second element is the original output of
    ``fun``.

  For example:

    >>> import jax
    >>> import jax.numpy as jnp
    >>> from jax.experimental import checkify
    >>>
    >>> @jax.jit
    ... def f(x):
    ...   y = jnp.sin(x)
    ...   return x+y
    >>> err, out = checkify.checkify(f, errors=checkify.float_checks)(jnp.inf)
    >>> err.throw()  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
      ...
    jax._src.checkify.JaxRuntimeError: nan generated by primitive: sin
  """
def check(pred: Bool, msg: str, *fmt_args, **fmt_kwargs) -> None:
    '''Check a predicate, add an error with msg if predicate is False.

  This is an effectful operation, and can\'t be staged (jitted/scanned/...).
  Before staging a function with checks, :func:`~checkify` it!

  Args:
    pred: if False, a FailedCheckError error is added.
    msg: error message if error is added. Can be a format string.
    fmt_args, fmt_kwargs: Positional and keyword formatting arguments for
      `msg`, eg.:
      ``check(.., "check failed on values {} and {named_arg}", x, named_arg=y)``
      Note that these arguments can be traced values allowing you to add
      run-time values to the error message.
      Note that tracking these run-time arrays will increase your memory usage,
      even if no error happens.

  For example:

    >>> import jax
    >>> import jax.numpy as jnp
    >>> from jax.experimental import checkify
    >>> def f(x):
    ...   checkify.check(x>0, "{x} needs to be positive!", x=x)
    ...   return 1/x
    >>> checked_f = checkify.checkify(f)
    >>> err, out = jax.jit(checked_f)(-3.)
    >>> err.throw()  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
      ...
    jax._src.checkify.JaxRuntimeError: -3. needs to be positive!

  '''
def is_scalar_pred(pred) -> bool: ...
def debug_check(pred: Bool, msg: str, *fmt_args, **fmt_kwargs) -> None:
    '''Check a predicate when running under checkify, otherwise is a no-op.

  A `debug_check` will only be run if it is transformed by :func:`~checkify`,
  otherwise the check will be dropped.

  Args:
    pred: if False, a FailedCheckError error is added.
    msg: error message if error is added.
    fmt_args, fmt_kwargs: Positional and keyword formatting arguments for
      `msg`, eg.:
      ``debug_check(.., "check failed on values {} and {named}", x, named=y)``
      Note that these arguments can be traced values allowing you to add
      run-time values to the error message.
      Note that tracking these run-time arrays will increase your memory usage,
      even if no error happens.

  For example:

    >>> import jax
    >>> import jax.numpy as jnp
    >>> from jax.experimental import checkify
    >>> def f(x):
    ...   checkify.debug_check(x!=0, "cannot be zero!")
    ...   return x
    >>> _ = f(0)  # running without checkify means no debug_check is run.
    >>> checked_f = checkify.checkify(f)
    >>> err, out = jax.jit(checked_f)(0)  # running with checkify runs debug_check.
    >>> err.throw()  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
      ...
    jax._src.checkify.JaxRuntimeError: cannot be zero!

  '''
def check_error(error: Error) -> None:
    '''Raise an Exception if ``error`` represents a failure. Functionalized by :func:`~checkify`.

  The semantics of this function are equivalent to:

  >>> def check_error(err: Error) -> None:
  ...   err.throw()  # can raise ValueError

  But unlike that implementation, ``check_error`` can be functionalized using
  the :func:`~checkify` transformation.

  This function is similar to :func:`~check` but with a different signature: whereas
  :func:`~check` takes as arguments a boolean predicate and a new error message
  string, this function takes an ``Error`` value as argument. Both :func:`~check`
  and this function raise a Python Exception on failure (a side-effect), and
  thus cannot be staged out by :func:`~jax.jit`, :func:`~jax.pmap`,
  :func:`~jax.lax.scan`, etc. Both also can
  be functionalized by using :func:`~checkify`.

  But unlike :func:`~check`, this function is like a direct inverse of
  :func:`~checkify`:
  whereas :func:`~checkify` takes as input a function which
  can raise a Python
  Exception and produces a new function without that effect but which produces
  an ``Error`` value as output, this ``check_error`` function can accept an
  ``Error`` value as input and can produce the side-effect of raising an
  Exception. That is, while :func:`~checkify` goes from
  functionalizable Exception
  effect to error value, this ``check_error`` goes from error value to
  functionalizable Exception effect.

  ``check_error`` is useful when you want to turn checks represented by an
  ``Error`` value (produced by functionalizing ``checks`` via
  :func:`~checkify`) back into Python Exceptions.

  Args:
    error: Error to check.

  For example, you might want to functionalize part of your program through
  checkify, stage out your functionalized code through :func:`~jax.jit`, then
  re-inject your error value outside of the :func:`~jax.jit`:

  >>> import jax
  >>> from jax.experimental import checkify
  >>> def f(x):
  ...   checkify.check(x>0, "must be positive!")
  ...   return x
  >>> def with_inner_jit(x):
  ...   checked_f = checkify.checkify(f)
  ...   # a checkified function can be jitted
  ...   error, out = jax.jit(checked_f)(x)
  ...   checkify.check_error(error)
  ...   return out
  >>> _ = with_inner_jit(1)  # no failed check
  >>> with_inner_jit(-1)  # doctest: +IGNORE_EXCEPTION_DETAIL
  Traceback (most recent call last):
    ...
  jax._src.JaxRuntimeError: must be positive!
  >>> # can re-checkify
  >>> error, _ = checkify.checkify(with_inner_jit)(-1)
  '''
