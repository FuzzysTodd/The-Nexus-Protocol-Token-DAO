import dataclasses
import numpy as np
import typing
from _typeshed import Incomplete
from collections.abc import Iterator, Sequence
from jax._src import ad_util as ad_util, core as core, dtypes as dtypes, effects as effects_lib, pickle_util as pickle_util, sharding_impls as sharding_impls, source_info_util as source_info_util, util as util, xla_bridge as xb
from jax._src.config import config as config
from jax._src.interpreters import xla as xla
from jax._src.lib import xla_client as xc, xla_extension as xla_extension
from jax._src.lib.mlir import dialects as dialects, ir as ir
from jax._src.lib.mlir.dialects import func as func_dialect, hlo as hlo
from jax._src.sharding_impls import XLACompatibleSharding as XLACompatibleSharding
from typing import Any, Callable, NamedTuple, Protocol

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
T = typing.TypeVar('T')
Value = Any
MYPY: bool
lowerable_effects: effects_lib.EffectTypeSet

def dense_int_elements(xs) -> ir.DenseIntElementsAttr: ...
def dense_bool_elements(xs: Sequence[bool]) -> ir.DenseElementsAttr: ...
def i32_attr(i): ...
def i64_attr(i): ...
def shape_tensor(sizes: Sequence[int | ir.RankedTensorType]) -> ir.RankedTensorType: ...
def delegate_lowering(ctx, lowering_fun, *args, **ctx_override_kwargs):
    """Side-effects on `ctx`"""
def dtype_to_ir_type(dtype: core.bint | np.dtype | np.generic) -> ir.Type: ...

ir_type_handlers: dict[type[core.AbstractValue], Callable[[Any], Sequence[ir.Type]]]

def aval_to_ir_types(aval: core.AbstractValue) -> Sequence[ir.Type]:
    """Converts a JAX aval to zero or more MLIR IR types.

  In general, a JAX value may be represented by multiple IR values, so this
  function returns multiple types."""
def aval_to_ir_type(aval: core.AbstractValue) -> ir.Type:
    """Convenience wrapper around aval_to_ir_types for single types.

  For some common cases, e.g. dense arrays, we know JAX values are represented
  by a single IR value."""

class ConstantHandler(Protocol):
    def __call__(self, val: Any) -> Sequence[ir.Value]:
        """Builds an IR representation for a constant `val`.

    A JAX value is represented by zero or more IR values."""

def register_constant_handler(type_: type, handler_fun: ConstantHandler): ...
def get_constant_handler(type_: type) -> ConstantHandler: ...
def ir_constants(val: Any) -> Sequence[ir.Value]:
    """Translate a Python `val` to an IR constant, canonicalizing its dtype.

  Args:
    val: a Python value to be translated to a constant.

  Returns:
    A representation of the constant as a list of IR values.
  """
def ir_constant(val: Any) -> ir.Value:
    """Convenience wrapper around ir_constants for singleton values."""
def get_canonical_source_file(frame: source_info_util.Frame) -> str: ...
def make_ir_context() -> ir.Context:
    """Creates an MLIR context suitable for JAX IR."""

AxisContext: Incomplete

class ShapePolyLoweringState:
    dim_vars: tuple[str, ...]
    uses_dim_vars: bool
    has_platform_index_argument: bool
    def __init__(self, dim_vars: tuple[str, ...], lowering_platforms: tuple[str, ...] | None) -> None: ...

@dataclasses.dataclass(frozen=True)
class LoweringParameters:
    override_lowering_rules: tuple[tuple[core.Primitive, LoweringRule]] | None = ...
    platforms: tuple[str, ...] | None = ...
    @property
    def override_platform(self) -> str | None:
        """Overrides the lowering platform for cross-platform lowering.

    One of 'cpu', 'cuda', 'rocm', 'tpu'.
    If None, use the default JAX mechanisms to pick the lowering platform.
    This is currently used for export and jax2tf.
    """
    @property
    def is_multi_platform(self) -> bool: ...
    def __init__(self, override_lowering_rules, platforms) -> None: ...

@dataclasses.dataclass
class ModuleContext:
    """Module-wide context information for MLIR lowering."""
    context: ir.Context
    module: ir.Module
    ip: ir.InsertionPoint
    symbol_table: ir.SymbolTable
    backend_or_name: str | xb.XlaBackend | None
    platform: str
    axis_context: AxisContext
    name_stack: source_info_util.NameStack
    keepalives: list[Any]
    channel_iterator: Iterator[int]
    host_callbacks: list[Any]
    shape_poly_state: ShapePolyLoweringState
    cached_primitive_lowerings: dict[Any, func_dialect.FuncOp]
    cached_call_jaxpr_lowerings: dict[Any, func_dialect.FuncOp]
    lowering_parameters: LoweringParameters
    @property
    def axis_env(self) -> sharding_impls.AxisEnv: ...
    def __init__(self, *, backend_or_name: str | xb.XlaBackend | None, platform: str, axis_context: AxisContext, name_stack: source_info_util.NameStack, keepalives: list[Any], channel_iterator: Iterator[int], host_callbacks: list[Any], lowering_parameters: LoweringParameters, context: ir.Context | None = None, module: ir.Module | None = None, ip: ir.InsertionPoint | None = None, symbol_table: ir.SymbolTable | None = None, cached_primitive_lowerings: None | dict[Any, func_dialect.FuncOp] = None, cached_call_jaxpr_lowerings: None | dict[Any, func_dialect.FuncOp] = None, shape_poly_state: Incomplete | None = None) -> None: ...
    @property
    def backend(self) -> xb.XlaBackend: ...
    def new_channel(self) -> int: ...
    def add_host_callback(self, host_callback: Any) -> None: ...
    def add_keepalive(self, keepalive: Any) -> None: ...
    def replace(self, **kw): ...

@dataclasses.dataclass
class LoweringRuleContext:
    """Per-rule context information for MLIR lowering."""
    module_context: ModuleContext
    primitive: core.Primitive | None
    avals_in: Sequence[core.AbstractValue]
    avals_out: Any
    tokens_in: TokenSet
    tokens_out: TokenSet | None
    axis_size_env: dict[core.Var, ir.Value] | None = ...
    dim_var_values: Sequence[ir.Value] = ...
    def set_tokens_out(self, tokens_out: TokenSet): ...
    def replace(self, **kw): ...
    def __init__(self, module_context, primitive, avals_in, avals_out, tokens_in, tokens_out, axis_size_env, dim_var_values) -> None: ...
LoweringRule = Any

def register_lowering(prim: core.Primitive, rule: LoweringRule, platform: str | None = None): ...
def wrap_singleton_ir_values(x: ir.Value | Sequence[ir.Value]) -> Sequence[ir.Value]:
    """Adds a consistent tuples to a mixture of tupled and untuple values."""
def flatten_lowering_ir_args(xs: Sequence[ir.Value | Sequence[ir.Value]]) -> Sequence[Sequence[ir.Value]]: ...
def sharded_aval(aval: core.AbstractValue, sharding: XLACompatibleSharding | None) -> core.AbstractValue:
    """Returns the new aval sharded based on sharding proto."""
def eval_dynamic_shape(ctx: LoweringRuleContext, shape: core.Shape) -> tuple[int | Value, ...]: ...
def eval_dynamic_shape_as_vals(ctx: LoweringRuleContext, shape: core.Shape) -> tuple[Value, ...]:
    """Evaluates the dynamic shapes as int32 values."""
def eval_dynamic_shape_as_ivals(ctx: LoweringRuleContext, shape: core.Shape) -> tuple[int | Value, ...]:
    """Evaluates the dynamic shapes as int or ir.int32 values."""
def eval_dynamic_shape_as_tensor(ctx: LoweringRuleContext, shape: core.Shape) -> Value:
    """Evaluates the dynamic shapes as one 1d int32 tensor."""

class LoweringResult(NamedTuple):
    module: ir.Module
    keepalive: Any | None
    host_callbacks: list[Any]
    shape_poly_state: ShapePolyLoweringState

def lower_jaxpr_to_module(module_name: str, jaxpr: core.ClosedJaxpr, *, ordered_effects: list[core.Effect], backend_or_name: str | xb.XlaBackend | None, platform: str, axis_context: AxisContext, name_stack: source_info_util.NameStack, donated_args: Sequence[bool], replicated_args: Sequence[bool] | None = None, arg_shardings: Sequence[XLACompatibleSharding | None] | None = None, result_shardings: Sequence[XLACompatibleSharding | None] | None = None, arg_names: Sequence[str | None] | None = None, result_names: Sequence[str | None] | None = None, num_replicas: int = 1, num_partitions: int = 1, all_default_mem_kind: bool = True, lowering_parameters: LoweringParameters) -> LoweringResult:
    """Lowers a top-level jaxpr to an MLIR module.

  Handles the quirks of the argument/return value passing conventions of the
  runtime.
  """
def module_to_string(module: ir.Module) -> str: ...
def module_to_bytecode(module: ir.Module) -> bytes: ...

Token: Incomplete

def token_type() -> Sequence[ir.Type]: ...
def create_token() -> Token: ...

class TokenSet:
    """An immutable container of tokens to be used to lower effectful jaxprs. When lowering
  effectful jaxprs, we need to thread HLO tokens to sequence them. Each effect
  will need its own token that will be threaded in and out of the effectful
  primitives. A `TokenSet` encapsulates a set of HLO tokens that will be
  used by the lowering rules.
  """
    def __init__(self, *args, **kwargs) -> None: ...
    def __len__(self) -> int: ...
    def get(self, effect: core.Effect) -> Token: ...
    @classmethod
    def create(cls, effects: Sequence[core.Effect]) -> TokenSet:
        """Creates a `TokenSet` corresponding to a list of `core.Effect`s."""
    def items(self) -> Sequence[tuple[core.Effect, Token]]: ...
    def effects(self) -> set[core.Effect]: ...
    def subset(self, effects: Sequence[core.Effect]) -> TokenSet:
        """Return a subset of the `TokenSet` restricted to a set of `core.Effect`s."""
    def update_tokens(self, tokens: TokenSet) -> TokenSet:
        """Returns a new `TokenSet` with tokens replaced with ones from the input `TokenSet`."""

def dummy_token_type() -> Sequence[ir.Type]: ...
def dummy_token() -> Sequence[ir.Value]: ...
def lower_jaxpr_to_fun(ctx: ModuleContext, name: str, jaxpr: core.ClosedJaxpr, effects: Sequence[core.Effect], *, create_tokens: bool = False, public: bool = False, replace_tokens_with_dummy: bool = False, replicated_args: Sequence[bool] | None = None, arg_shardings: Sequence[xc.HloSharding | None] | None = None, result_shardings: Sequence[xc.HloSharding | None] | None = None, use_sharding_annotations: bool = True, input_output_aliases: Sequence[int | None] | None = None, num_output_tokens: int = 0, api_name: str = 'jit', arg_names: Sequence[str | None] | None = None, result_names: Sequence[str | None] | None = None, arg_memory_kinds: Sequence[str | None] | None = None, result_memory_kinds: Sequence[str | None] | None = None) -> func_dialect.FuncOp:
    '''Lowers jaxpr and its callees to an IR function.

  Assumes that an MLIR context, location, and insertion point are set.

  Args:
    ctx: the lowering context.
    name: the function name. The name will be uniquified by the symbol table,
      so it is ok to use the same name multiple times.
    jaxpr: the jaxpr to lower.
    effects: a sequence of `core.Effect`s corresponding to an ordering of tokens
      that will be created in or used by the lowered function.
    create_tokens: if true, the HLO will create tokens and ignore dummy input tokens.
    public: if true, the function\'s visibility is set to "public".
    replace_tokens_with_dummy: if true, token arguments/return values are
      replaced with bool arrays of size [0].
    replicated_args: if present, annotates arguments as replicated.
    arg_shardings: sharding annotations for each argument (optional).
    result_shardings: sharding annotations for each result (optional).
    use_sharding_annotations: if True, use "mhlo.sharding" annotations on
      parameters and return values to express sharding. If False, use
      hlo.custom_call operators with sharding annotations.
      TODO(b/228598865): remove this option when "mhlo.sharding" annotations are
      propagated on non-entry functions during MLIR->HLO conversion.
    input_output_aliases: optional sequence that maps argument numbers to the
      corresponding output that should alias them.
    api_name: The name of the higher level primitive which should show up in the
      name stack.
  Returns:
    MLIR func op
  '''
def get_compute_type(memory_kind: str) -> str: ...
def wrap_with_memory_kind(x: ir.Value, memory_kind: str, aval_out: core.AbstractValue, is_input: bool = False) -> ir.Value: ...
def jaxpr_subcomp(ctx: ModuleContext, jaxpr: core.Jaxpr, tokens: TokenSet, consts: Sequence[Sequence[ir.Value]], *args: Sequence[ir.Value], dim_var_values: Sequence[ir.Value]) -> tuple[Sequence[Sequence[ir.Value]], TokenSet]:
    """Lowers a jaxpr into MLIR, inlined into an existing function.

  Assumes that an MLIR context, location, and insertion point are set.

  dim_var_values: the list of dimension variables values in the current
    IR function, in the order of ctx.shape_poly_state.dim_vars.
  """
MultiPlatformLoweringRule = tuple[Sequence[str] | None, Callable]

def lower_multi_platform(ctx: LoweringRuleContext, description: str, rules: Sequence[MultiPlatformLoweringRule], *rule_args: ir.Value, **rule_kwargs) -> ir.Value:
    '''Emits single- or multi-platform code for a primitive.

  For example, given
      ctx.module_context.lowering_parameters.platforms = ("cpu", "gpu", "tpu")
  and
      rules = [(["tpu", "cpu"], rule0),
               (None, rule1)
  emits:
    rule_idx = case current_platform_idx:
                   0: return 0  # cpu rule index
                   1: return 1  # gpu rule index
                   2: return 0  # tpu rule index
    output = case rule_idx
               0: return rule0(*rule_args, **rule_kwargs)
               1: return rule1(*rule_args, **rule_kwargs)

  If the primitive has a single lowering rule for all platforms of interest,
  skips the conditionals and emits the same code as for classic single-platform
  lowering.

  Args:
   ctx: lowering context.
   description: a string to include in error messages.
   rules: a sequence of per-platform rules. Each entry is a tuple, with the
     first element specifying the platforms, either a sequence of applicable
     platform names (maybe empty), or None to denote a default entry to use
     when no other entry applies. The second element of the tuple is a
     lowering rule, i.e., a function to invoke with a
     LoweringRuleContext (a sub-context of `ctx`),
     and `*rule_args` and `**rule_kwargs`.
   rule_args: the args of the lowering rules.
   rule_kwargs: the kwargs of the lowering rules.
  '''
def lower_fun(fun: Callable, multiple_results: bool = True) -> Callable:
    """Converts a traceable JAX function `fun` into a lowering rule.

  The returned function does not use `avals_out`, so callers may pass any value
  as `avals_out`."""
def check_backend_matches(inner_backend, outer_backend) -> None: ...
def core_call_lowering(ctx, *args, name, backend: Incomplete | None = None, call_jaxpr): ...
def broadcast_in_dim(ctx: LoweringRuleContext, op, aval_out: core.AbstractValue, *, broadcast_dimensions) -> ir.Value: ...
def multi_broadcast_in_dim(ctx: LoweringRuleContext, ops: Sequence[ir.Value], ops_avals: Sequence[core.AbstractValue], out_shape: core.Shape) -> Sequence[ir.Value]:
    """Broadcasts multiple ops to the out_shape."""
def reshape(ctx: LoweringRuleContext, op, aval_out: core.AbstractValue) -> ir.Value: ...
def slice_op(ctx: LoweringRuleContext, x, aval_out, *, start_indices, limit_indices, strides) -> ir.Value: ...
def dynamic_slice(ctx: LoweringRuleContext, aval_out, x, *, start_indices) -> ir.Value: ...
def dynamic_update_slice(ctx: LoweringRuleContext, aval_out, x, update, *, start_indices) -> ir.Value: ...
def pad(ctx: LoweringRuleContext, aval_out, x, padding_value, padding_low, padding_high, padding_interior) -> ir.Value: ...
def iota(ctx: LoweringRuleContext, aval_out, *, dimension: int): ...
def full_like_aval(ctx: LoweringRuleContext, value, aval: core.ShapedArray) -> ir.Value:
    """Returns an IR constant shaped full of `value` shaped like `aval`."""
def zeros_like_lowering(ctx, x): ...
def add_jaxvals_lowering(ctx, x, y): ...
def compare_hlo(x, y, direction: str, comparison_type: str | None = None):
    """Creates CompareOp."""

min_hlo: Incomplete
max_hlo: Incomplete

def convert_hlo(ctx: LoweringRuleContext, x, aval_in, aval_out):
    """Variant of convert that has HLO semantics.

  In particular, treat casts to boolean as x != 0, rather than truncating
  integer values (b/209440332)."""

wrap_with_sharding_op: Incomplete
wrap_with_full_to_shard_op: Incomplete
wrap_with_shard_to_full_op: Incomplete

def set_sharding(op, sharding_proto: xc.OpSharding): ...
def get_sharding_attr(sharding_proto: xc.OpSharding): ...
def cache_lowering(f):
    """Decorator that causes the contents of a lowering rule to be reused.

  The lowering will be emitted out-of-line in a separate function, together with
  a call to that function. If the same primitive is called with the same shapes
  and parameters, a new call to the original function will be added, without
  emitting a new function.
  """
def xla_computation_to_mlir_module(xla_computation: xc.XlaComputation) -> ir.Module: ...
def merge_mlir_modules(dst_module: ir.Module, sym_name: str, src_module: ir.Module) -> str:
    '''
  Args:
    dst_module: the module into which the contents of src_module should be
      moved. Nothing in dst_module will be renamed.
    sym_name: the desired name for the "main" function of src_module after
      merging. This is a hint: the true name may be different because of symbol
      uniquification, and the true name is returned by this function.
    src_module: the module whose contents are to be alpha-renamed, set to
      private visibility, and merged into dst_module. src_module must contain
      exactly one symbol named "main".

      Functions in src_module will be renamed such that they do not collide with
      functions in dst_module.

      This function mutates `src_module`. On return, `src_module` is left in an
      undefined state.

  Returns:
    the name of src_module\'s main() function, after renaming.
  '''
def xla_fallback_lowering(prim: core.Primitive): ...

DEVICE_TO_DEVICE_TYPE: int
SEND_TO_HOST_TYPE: int
RECV_FROM_HOST_TYPE: int

def is_empty_shape(s: core.Shape) -> bool: ...
def send_to_host(channel: int, token: hlo.TokenType, operand: Any, aval: core.ShapedArray, name: str, *, sharding: xc.OpSharding | None = None) -> ir.Value: ...
def receive_from_host(channel: int, token: hlo.TokenType, out_aval: core.ShapedArray, name: str, *, sharding: xc.OpSharding | None = None) -> ir.Value: ...
def emit_python_callback(ctx: LoweringRuleContext, callback, token: Any | None, operands: Sequence[ir.Value], operand_avals: Sequence[core.ShapedArray], result_avals: Sequence[core.ShapedArray], has_side_effect: bool, *, sharding: xc.OpSharding | None = None, operand_layouts: Sequence[Sequence[int] | None] | None = None, result_layouts: Sequence[Sequence[int] | None] | None = None) -> tuple[Sequence[ir.Value], Any, Any]:
    """Emits MLIR that calls back to a provided Python function."""
def build_xla_computation_helper(closed_jaxpr: core.ClosedJaxpr, *, name: str, platform: str, backend_or_name: str, axis_context: AxisContext) -> xc.XlaComputation:
    """Helper to generate pmap-style XLA computations for custom partitioners."""
def custom_call(call_target_name: str, *, result_types: Sequence[ir.Type], operands: Sequence[ir.Value], backend_config: str | bytes | dict[str, ir.Attribute] = '', has_side_effect: bool = False, result_shapes: Sequence[ir.Value] | None = None, called_computations: Sequence[str] = (), api_version: int = 2, operand_output_aliases: dict[int, int] | None = None, operand_layouts: Sequence[Sequence[int]] | None = None, result_layouts: Sequence[Sequence[int]] | None = None, extra_attributes: dict[str, ir.Attribute] | None = None) -> ir.Operation:
    """Helper function for building an hlo.CustomCall.

  Args:
    call_target_name: the name of the custom call target
    result_types: the MLIR types of the results of the custom call
    operands: the MLIR IR values that are arguments to the custom call
    backend_config: an opaque string passed to the custom call kernel
    has_side_effect: if True, marks the custom call as effectful
    result_shapes: tensors that represent the result shapes, to be used when
      the results have dynamic shapes. If not-None, its length must match the
      number of the results.
    called_computations: the list of function names called by the custom call.
    api_version: the ABI contract version of the custom call
    operand_output_aliases: a dict mapping operand numbers to outputs they alias
    operand_layouts: a sequence of layouts (dimension orders) for each operand
    result_layouts: a sequence of layouts (dimension orders) for each result
    extra_attributes: additional IR attributes to apply to the custom_call.
  """
def reduce_window(ctx: LoweringRuleContext, *, reducer_name: str, reducer_body: Callable[[ir.Block], Sequence[ir.Value]], operands: Sequence[ir.Value], init_values: Sequence[ir.Value], init_values_avals: Sequence[core.AbstractValue], out_avals: Sequence[core.AbstractValue], window_dimensions, window_strides, padding, base_dilation, window_dilation):
    """Builds a ReduceWindowOp, with support for dynamic shapes."""
def refine_polymorphic_shapes(module: ir.Module) -> ir.Module:
    """Refines the polymorphic shapes inside a module.

  Given a module with static input shapes, but using dynamic shapes due to
  shape polymorphism, runs shape refinement to resolve all the dynamic shapes.
  Then verifies that there are no more dynamic shapes in the module.
  """
