import dataclasses
import jax
from _typeshed import Incomplete
from collections.abc import Sequence
from jax import config as config, sharding as sharding
from jax._src import core as core, dispatch as dispatch, pjit as pjit, sharding_impls as sharding_impls, source_info_util as source_info_util, tree_util as tree_util, util as util
from jax._src.interpreters import mlir as mlir, pxla as pxla
from jax._src.lib import xla_client as xla_client
from jax._src.lib.mlir import ir as ir
from jax._src.lib.mlir.dialects import hlo as hlo
from jax.experimental.export import shape_poly as shape_poly
from typing import Any, Callable

map: Incomplete
zip: Incomplete
DType = Any

class DisabledSafetyCheck:
    """A safety check should be skipped on (de)serialization.

  Most of these checks are performed on serialization, but some are deferred to
  deserialization. The list of disabled checks is attached to the serialization,
  e.g., as a sequence of string attributes to `jax_export.Exported` or of
  `tf.XlaCallModuleOp`.

  You can disable more deserialization safety checks by passing
  `TF_XLA_FLAGS=--tf_xla_call_module_disabled_checks=platform`.
  """
    @classmethod
    def platform(cls) -> DisabledSafetyCheck:
        """Allows the execution platform to differ from the serialization platform.

    Has effect only on deserialization.
    """
    @classmethod
    def custom_call(cls, target_name: str) -> DisabledSafetyCheck:
        """Allows the serialization of a call target not known to be stable.

    Has effect only on serialization.
    Args:
      target_name: the name of the custom call target to allow.
    """
    @classmethod
    def shape_assertions(cls) -> DisabledSafetyCheck:
        """Allows invocations with shapes that do not meet the constraints.

    Has effect on serialization (to suppress the generation of the assertions)
    and also on deserialization (to suppress the checking of the assertions).
    """
    def is_custom_call(self) -> str | None:
        """Returns the custom call target allowed by this directive."""
    def __init__(self, _impl: str) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...

minimum_supported_serialization_version: int
maximum_supported_serialization_version: int

@dataclasses.dataclass(frozen=True)
class Exported:
    '''A JAX function lowered to StableHLO.

  Attributes:
    fun_name: the name of the exported function, for error messages.
    in_tree: a PyTreeDef describing the tuple (args, kwargs) of the lowered JAX
        function. The actual lowering does not depend on the `in_tree`, but this
        can be used to invoke the exported function using the same argument
        structure.
    in_avals: the flat tuple of input abstract values. May contain dimension
        expressions in the shapes.
    out_tree: a PyTreeDef describing the result of the lowered JAX function.
    out_avals: the flat tuple of output abstract values. May contain dimension
        expressions in the shapes, with dimension variables among those in
        `in_avals.
    in_shardings: the flattened input shardings. Only for the inputs that are
        specified in `module_kept_var_idx`. If `None` then it is equivalent
        to unspecified shardings.
    out_shardings: the flattened output shardings, as long as `in_avals`.
    lowering_platforms: a tuple containing at least one of \'tpu\', \'cpu\',
        \'cuda\', \'rocm\'. See below for the calling convention for when
        there are multiple lowering platforms.
    mlir_module_serialized: the serialized lowered VHLO module.
    serialization_version: a version number for the serialized module.
        See more versioning details at https://github.com/google/jax/blob/main/jax/experimental/jax2tf/README.md#native-serialization-versions.
    module_kept_var_idx: the sorted indices of the arguments among `in_avals` that
        must be passed to the module. The other arguments have been dropped
        because they are not used. Same length as `in_shardings`.
    uses_shape_polymorphism: whether the `mlir_module_serialized` uses shape
        polymorphism. This may be because `in_avals` contains dimension
        variables, but also from inner calls of shape-polymorphic
        Exported modules.
    disabled_checks: a list of descriptors of safety checks that have been
        disabled at export time. See docstring for `DisabledSafetyCheck`.
    _get_vjp: an optional function that takes the current exported function and
        returns the exported VJP function.
        The VJP function takes a flat list of arguments,
        starting with the primal arguments and followed by a cotangent argument
        for each primal output. It returns a tuple with the cotangents
        corresponding to the flattened primal inputs.

  Calling convention for the exported module:

  The `mlir_module` has a `main` function that takes an optional first
  platform index argument if the module supports multiple platforms
  (`len(lowering_platforms) > 1`), followed by the kept array arguments
  (corresponding to `module_kept_var_idx` and `in_avals`).
  The platform index is a i32 scalar encoding the index of the current
  compilation platform into the `lowering_platforms` sequence.

  Inner functions use a different calling convention: an optional
  platform index argument, optional dimension variable arguments specified
  using scalar tensors of type i32 or i64,
  followed by optional token arguments (in presence of side effects),
  followed by the regular array arguments.
  The dimension arguments correspond to the dimension variables appearing in
  the `args_avals`, in sorted order of their names.

  Consider the lowering of a function with one array argument of type "f32[w,
  2 * h]", where "w" and "h" are two dimension variables.
  Assume that we use multi-platform lowering, and we have
  ordered effects. The `main` function will be as follows:

      func public main(platform_index: i32, arg: f32[?, ?]) {
         arg_w = hlo.get_dimension_size(arg, 0)
         dim1 = hlo.get_dimension_size(arg, 1)
         arg_h = hlo.floordiv(dim1, 2)
         call _check_shape_assertions(arg)  # See below
         token = new_token()
         token_out, res = call _wrapped_jax_export_main(platform_index, arg_h, arg_w, token_in, arg)
         return res
      }

  The actual computation is in `_wrapped_jax_export_main`, taking also
  the values of `h` and `w` and the token. Proper exporting of
  functions with side-effects and tokens is still work-in-progress.

  Note that `main` contains a call to `_check_shape_assertions.
  JAX tracing assumes that `arg.shape[1]` is even, and that both `w` and `h`
  have values >= 1. We must check these constraints when we invoke the
  module. We use a special custom call `@shape_assertion` that takes
  a boolean first operand, a string `error_message` attribute that may contain
  format specifiers `{0}`, `{1}`, ..., and a variadic number of integer
  scalar operands corresponding to the format specifiers.

       func private _check_shape_assertions(arg: f32[?, ?]) {
         # Check that w is >= 1
         arg_w = hlo.get_dimension_size(arg, 0)
         custom_call @shape_assertion(arg_w >= 1, arg_w,
            error_message="Dimension variable \'w\' must have integer value >= 1. Found {0}")
         # Check that dim1 is even
         dim1 = hlo.get_dimension_size(arg, 1)
         custom_call @shape_assertion(dim1 % 2 == 0, dim1,
            error_message="Dimension variable \'h\' must have integer value >= 1. Found non-zero remainder {0}")
         # Check that h >= 1
         arg_h = hlo.floordiv(dim1, 2)
         custom_call @shape_assertion(arg_h >= 1, arg_h,
            error_message=""Dimension variable \'h\' must have integer value >= 1. Found {0}")

  If we `call_exported` with this module we perform these checks
  statically (in `call_exported_abstract_eval`).
  '''
    fun_name: str
    in_tree: tree_util.PyTreeDef
    in_avals: tuple[core.AbstractValue, ...]
    out_tree: tree_util.PyTreeDef
    out_avals: tuple[core.AbstractValue, ...]
    in_shardings: tuple[sharding.XLACompatibleSharding | pxla.UnspecifiedValue, ...] | None
    out_shardings: tuple[sharding.XLACompatibleSharding | pxla.UnspecifiedValue, ...] | None
    lowering_platform: str
    lowering_platforms: tuple[str, ...]
    disabled_checks: Sequence[DisabledSafetyCheck]
    mlir_module_serialized: bytes
    serialization_version: int
    module_kept_var_idx: tuple[int, ...]
    uses_shape_polymorphism: bool
    def mlir_module(self) -> ir.Module: ...
    def vjp(self) -> Exported:
        """Gets the exported VJP.

    Returns None if not available, which can happen if the Exported has been
    loaded from an external format, without a VJP."""
    def __init__(self, fun_name, in_tree, in_avals, out_tree, out_avals, in_shardings, out_shardings, lowering_platform, lowering_platforms, disabled_checks, mlir_module_serialized, serialization_version, module_kept_var_idx, uses_shape_polymorphism, _get_vjp) -> None: ...

def default_lowering_platform() -> str: ...
def poly_spec(arg_shape: Sequence[int | None], arg_dtype: DType, polymorphic_shape: str | None) -> jax.ShapeDtypeStruct:
    """Constructs a jax.ShapeDtypeStruct with polymorphic shapes.

  Args:
    arg_shape: the shape, with possibly some unspecified dimensions.
    arg_dtype: the jax dtype.
    polymorphic_shape: a string specifying the polymorphic shape.

      .. warning:: The shape-polymorphic lowering is an experimental feature.
        It is meant to be sound, but it is known to reject some JAX programs
        that are shape polymorphic. The details of this feature can change.

      It should be either `None` (all dimensions are constant), or a string of
      specification for one axis, and can be either a constant, `_` denoting
      a constant dimension given by the `arg_shape`, or the name of a
      dimension variable assumed to range over dimension greater than 0. For
      convenience, zero or more trailing `_` can be abbreviated with `...`, and
      the surrounding parentheses may be missing.

      Note that this function does not ensure that the provided `arg_shape`
      is compatible with `polymorphic_shape`. The `arg_shape` is used only
      to fill-in placeholders from `polymorphic_shape`.

      See [the README](https://github.com/google/jax/blob/main/jax/experimental/jax2tf/README.md#shape-polymorphic-conversion)
      for more details.

  Returns: a jax.ShapeDTypeStruct with shapes that may contain symbolic
      expressions involving dimension variables.
  """
def shape_and_dtype_jax_array(a) -> tuple[Sequence[int | None], DType]:
    """Returns the shape and dtype of a jax.Array."""
def poly_specs(args, polymorphic_shapes, get_shape_and_dtype=...):
    """Constructs a pytree of jax.ShapeDtypeSpec.

  Args:
    args: a pytree of arguments
    polymorphic_shapes: should be `None` (all arguments are monomorphic),
      a single string (applies to all arguments), or a pytree matching a prefix
      of the `args`.
      See [how optional parameters are matched to
      arguments](https://jax.readthedocs.io/en/latest/pytrees.html#applying-optional-parameters-to-pytrees).

      Note that this function does not ensure that the provided `args` shapes
      are compatible with `polymorphic_shapes`. The `args.shape` are used only
      to fill-in placeholders from `polymorphic_shapes`.

      See docstring of `poly_spec` and
      [the README](https://github.com/google/jax/blob/main/jax/experimental/jax2tf/README.md#shape-polymorphic-conversion)
      for more details.

  Returns: a pytree of jax.ShapeDTypeStruct matching `args`.
  """
def export(fun_jax: Callable, *, lowering_platform: str | None = None, lowering_platforms: Sequence[str] | None = None, disabled_checks: Sequence[DisabledSafetyCheck] = ()) -> Callable[..., Exported]:
    """Exports native serialization for a JAX function.

  Args:
    fun_jax: the function to lower and serialize.
    lowering_platform: one of 'tpu', 'cpu', 'cuda', 'rocm'. If None, then use
        the default JAX backend.
    lowering_platforms: DO NOT USE (NOT YET FUNCTIONAL).
        Optional sequence containing a subset of 'tpu', 'cpu',
        'cuda', 'rocm'. If more than one platform is specified, then
        the lowered code takes an argument specifying the platform.
        If None, then use the default JAX backend.
        The calling convention for multiple platforms is explained in the
        `jax_export.Exported` docstring.
    disabled_checks: the safety checks to disable. See docstring
        of `DisabledSafetyCheck`.

  Returns: a function that takes args and kwargs pytrees of jax.ShapeDtypeStruct,
      or values with `.shape` and `.dtype` attributes, and returns an
      `Exported`.

  Usage:

      def f_jax(*args, **kwargs): ...
      exported = jax_export.export(f_jax)(*args, **kwargs)
  """
def call_exported(exported: Exported) -> Callable[..., jax.Array]: ...

call_exported_p: Incomplete
