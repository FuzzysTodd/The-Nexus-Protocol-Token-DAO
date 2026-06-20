import dataclasses
import enum
import jax
import threading
from _typeshed import Incomplete
from collections.abc import Generator, Iterable, Sequence
from functools import cached_property as cached_property
from jax._src import api_util as api_util, compiler as compiler, core as core, dispatch as dispatch, dtypes as dtypes, effects as effects, linear_util as lu, op_shardings as op_shardings, profiler as profiler, sharding_impls as sharding_impls, sharding_specs as sharding_specs, source_info_util as source_info_util, stages as stages, tree_util as tree_util, util as util, xla_bridge as xb
from jax._src.abstract_arrays import array_types as array_types
from jax._src.config import config as config
from jax._src.core import DShapedArray as DShapedArray, ShapedArray as ShapedArray
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir, xla as xla
from jax._src.lib import xla_client as xc, xla_extension_version as xla_extension_version
from jax._src.lib.mlir import ir as ir
from jax._src.lib.mlir.dialects import hlo as hlo
from jax._src.partition_spec import PartitionSpec as PartitionSpec
from jax._src.sharding_impls import AUTO as AUTO, ArrayMapping as ArrayMapping, ArrayMappingOrAutoOrUnspecified as ArrayMappingOrAutoOrUnspecified, UNSPECIFIED as UNSPECIFIED, UnspecifiedValue as UnspecifiedValue, is_auto as is_auto, is_unspecified as is_unspecified, is_unspecified_or_auto as is_unspecified_or_auto
from jax._src.util import HashableFunction as HashableFunction, distributed_debug_log as distributed_debug_log, partition_list as partition_list, safe_map as safe_map, safe_zip as safe_zip, tuple_delete as tuple_delete, unzip2 as unzip2, weakref_lru_cache as weakref_lru_cache, wrap_name as wrap_name
from jax.errors import JAXTypeError as JAXTypeError
from typing import Any, Callable, Iterator, NamedTuple

class WeakRefList(list): ...

xe: Incomplete
unsafe_map: Incomplete
map: Incomplete
logger: Incomplete
Index = int | slice | tuple[int | slice, ...]
NoSharding: Incomplete
Chunked: Incomplete
Unstacked: Incomplete
ShardedAxis: Incomplete
Replicated: Incomplete
AvalDimSharding = Unstacked | Chunked | NoSharding
Mesh: Incomplete
MeshAxisName: Incomplete
MeshDimAssignment = ShardedAxis | Replicated
ShardingSpec: Incomplete

def identity(x): ...
def shard_arg(arg, devices, arg_indices, sharding, canonicalize: bool = True):
    """Returns a list of size len(devices) containing per-device buffers.

  For the C++ pmap path, we fallback to Python (this function) to shard
  arguments that are not supported by the C++ `ShardArg`.

  Args:
    arg: The Python argument.
    devices: The list of devices to shard over.
    arg_indices: A list of `len(devices)` indices to use to shard the argument.
  """
def shard_args(devices: Sequence[xb.xla_client.Device], indices: Sequence[Sequence[Index]], shardings: Sequence[sharding_impls.XLACompatibleSharding], args) -> Sequence[jax.Array]:
    """Shard each argument data array along its leading axis.

  Args:
    devices: sequence of Devices mapping replica index to a physical device.
    indices: sequence of the same length as `args` describing how each arg
      should be sharded/replicated across `devices`. Each element in `indices`
      is the same length as `devices`.
    args: a sequence of JaxTypes representing arguments to be sharded according
      to `indices` and placed on `devices`.

  Returns:
    A list of length matching args, containing lists of per-device buffers
    for each argument.
  """

shard_arg_handlers: dict[Any, Callable[[Any, Any, Any, Any], Any]]

def batched_device_put(aval: core.ShapedArray, sharding: jax.sharding.Sharding, xs: Sequence[Any], devices: Sequence[jax.Device], committed: bool = True): ...
def shard_aval(size, axis: int, aval): ...

shard_aval_handlers: dict[type[core.AbstractValue], Callable[[int, int, Any], Any]]

def local_aval_to_result_handler(aval: core.AbstractValue, sharding: sharding_impls.XLACompatibleSharding, indices: tuple[Index, ...] | None) -> Callable[[list[xc.ArrayImpl]], Any]:
    """Returns a function for handling the raw buffers of a single output aval.

  Args:
    aval: The local output AbstractValue.
    sharding_spec: Indicates how the output is sharded across devices, or None
      for non-array avals.
    indices: The pre-computed result of spec_to_indices, or None for non-array
      avals.

  Returns:
    A function for handling the Buffers that will eventually be produced
    for this output. The function will return an object suitable for returning
    to the user, e.g. an Array.
  """
PxlaResultHandler = Callable[..., Callable[[Any], Any]]
local_result_handlers: dict[type[core.AbstractValue], PxlaResultHandler]

def global_aval_to_result_handler(aval: core.AbstractValue, out_sharding, committed: bool, is_out_sharding_from_xla: bool) -> Callable[[Sequence[xc.ArrayImpl]], Any]:
    """Returns a function for handling the raw buffers of a single output aval.

  Args:
    aval: The global output AbstractValue.
    out_axis_resources: A PartitionSpec specifying the sharding of outputs.
      Used for creating GSDAs.
    global_mesh: The global device mesh that generated this output. Used
      for creating GSDAs.
    is_out_sharding_from_xla: True, if the out_sharding comes from XLA i.e.
      the sharding is extracted from the HLO.

  Returns:
    A function for handling the Buffers that will eventually be produced
    for this output. The function will return an object suitable for returning
    to the user, e.g. an Array.
  """

global_result_handlers: dict[type[core.AbstractValue], PxlaResultHandler]

def xla_pmap_impl_lazy(fun: lu.WrappedFun, *args, backend: str | None, axis_name: core.AxisName, axis_size: int, global_axis_size: int, devices: Sequence[Any] | None, name: str, in_axes: Sequence[int | None], out_axes_thunk: Callable[[], Sequence[int | None]], donated_invars: Sequence[bool], is_explicit_global_axis_size: bool) -> Callable: ...
def xla_pmap_impl(fun: lu.WrappedFun, *args, **params): ...

class EmapInfo(NamedTuple):
    backend: str | None
    devices: Sequence[Any] | None

class FakePrimitive(NamedTuple):
    multiple_results: Incomplete
    bind: Incomplete

class MapTrace(core.Trace):
    emap_info: Incomplete
    def __init__(self, *args, emap_info) -> None: ...
    def pure(self, val): ...
    def sublift(self, tracer): ...
    def process_primitive(self, primitive, tracers, params): ...
    def process_call(self, call_primitive, fun, tracers, params) -> None: ...
    def process_map(self, map_primitive, fun, tracers, params): ...
    def process_custom_jvp_call(self, prim, fun, jvp, tracers, *, symbolic_zeros): ...
    def process_custom_vjp_call(self, primitive, fun, fwd, bwd, tracers, out_trees, symbolic_zeros): ...
    def process_axis_index(self, frame): ...

class MapTracer(core.Tracer):
    val: Incomplete
    shard_axes: Incomplete
    def __init__(self, trace: MapTrace, val, shard_axes: dict[core.AxisName, int]) -> None: ...
    @property
    def aval(self): ...
    def full_lower(self): ...

def parallel_callable(fun: lu.WrappedFun, backend_name: str | None, axis_name: core.AxisName, axis_size: int, global_axis_size: int, devices: Sequence[Any] | None, name: str, in_axes: Sequence[int | None], out_axes_thunk: Callable[[], Sequence[int | None]], donated_invars: Sequence[bool], is_explicit_global_axis_size: bool, *avals): ...

@dataclasses.dataclass(frozen=True)
class ParallelCallableInfo:
    name: str
    backend: xc.Client
    axis_name: core.AxisName
    axis_size: int
    global_axis_size: int
    devices: Sequence[xc.Device] | None
    in_axes: Iterable[int | None]
    out_axes_thunk: Callable[[], Sequence[int | None]]
    avals: Sequence[core.AbstractValue]
    @cached_property
    def local_devices(self): ...
    @cached_property
    def out_axes(self): ...
    def __init__(self, name, backend, axis_name, axis_size, global_axis_size, devices, in_axes, out_axes_thunk, avals) -> None: ...

class ShardInfo(NamedTuple):
    sharded_avals: Sequence[core.AbstractValue]
    out_sharded_avals: Sequence[core.ShapedArray]
    global_sharded_avals: Sequence[core.AbstractValue]
    num_local_shards: int
    num_global_shards: int

class ReplicaInfo(NamedTuple):
    jaxpr_replicas: int
    num_local_replicas: int
    num_global_replicas: int

def find_replicas(jaxpr: core.Jaxpr, axis_size: int, global_axis_size: int) -> ReplicaInfo: ...
def stage_parallel_callable(pci: ParallelCallableInfo, fun: lu.WrappedFun) -> tuple[core.Jaxpr, list[Any], ReplicaInfo, ShardInfo]: ...
def lower_parallel_callable(fun: lu.WrappedFun, backend_name: str | None, axis_name: core.AxisName, axis_size: int, global_axis_size: int, devices: Sequence[xc.Device] | None, name: str, in_axes: Iterable[int | None], out_axes_thunk: Callable[[], Sequence[int | None]], donated_invars: Sequence[bool], is_explicit_global_axis_size: bool, avals: Sequence[core.AbstractValue], *, lowering_parameters: mlir.LoweringParameters): ...

class PmapComputation(stages.XlaLowering):
    compile_args: Incomplete
    def __init__(self, hlo: ir.Module, **compile_args) -> None: ...
    def stablehlo(self) -> ir.Module: ...
    def compile(self, compiler_options: Incomplete | None = None) -> PmapExecutable: ...

@dataclasses.dataclass
class UnloadedPmapExecutable:
    compiled: Any
    backend: xb.XlaBackend
    local_input_avals: Sequence[core.AbstractValue]
    input_shardings: Sequence[sharding_impls.XLACompatibleSharding]
    local_output_avals: Sequence[ShapedArray]
    output_shardings: Sequence[sharding_impls.XLACompatibleSharding]
    unordered_effects: list[core.Effect]
    ordered_effects: list[core.Effect]
    keepalive: Sequence[Any]
    host_callbacks: Sequence[Any]
    jaxpr_debug_info: core.JaxprDebugInfo
    def build_execute_fun(self): ...
    def load(self) -> PmapExecutable: ...
    @staticmethod
    def from_hlo(hlo: ir.Module, pci: ParallelCallableInfo, replicas: ReplicaInfo, shards: ShardInfo, tuple_args: bool, unordered_effects: list[core.Effect], ordered_effects: list[core.Effect], host_callbacks: list[Any], keepalive: Any, jaxpr_debug_info: core.JaxprDebugInfo, compiler_options: Incomplete | None = None): ...
    def __init__(self, compiled, backend, local_input_avals, input_shardings, local_output_avals, output_shardings, unordered_effects, ordered_effects, keepalive, host_callbacks, jaxpr_debug_info) -> None: ...

class PmapExecutable(stages.XlaExecutable):
    xla_executable: Incomplete
    build_unsafe_call: Incomplete
    fingerprint: Incomplete
    in_avals: Incomplete
    def __init__(self, xla_executable, build_unsafe_call, fingerprint, in_avals, jaxpr_debug_info, unloaded_executable) -> None: ...
    @property
    def unsafe_call(self) -> Callable[..., Any]: ...
    def xla_extension_executable(self): ...
    def call(self, *args): ...

class InputsHandler:
    handler: Incomplete
    local_devices: Incomplete
    in_shardings: Incomplete
    input_indices: Incomplete
    def __init__(self, local_devices, in_shardings, input_indices) -> None: ...
    def __call__(self, input_buffers): ...

class ResultsHandler:
    handlers: Incomplete
    out_shardings: Incomplete
    out_avals: Incomplete
    def __init__(self, handlers, out_shardings, out_avals) -> None: ...
    def __call__(self, out_bufs): ...

def local_avals_to_results_handler(unmapped_local_out_avals: Sequence[ShapedArray], local_shardings: Sequence[sharding_impls.XLACompatibleSharding]) -> ResultsHandler: ...
def global_avals_to_results_handler(global_out_avals: Sequence[ShapedArray], shardings: Sequence[sharding_impls.XLACompatibleSharding], committed: bool, are_out_shardings_from_xla: Sequence[bool]) -> ResultsHandler: ...

class ExecuteReplicated:
    """The logic to shard inputs, execute a replicated model, returning outputs."""
    xla_executable: Incomplete
    name: Incomplete
    backend: Incomplete
    in_handler: Incomplete
    out_handler: Incomplete
    has_unordered_effects: Incomplete
    ordered_effects: Incomplete
    keepalive: Incomplete
    has_host_callbacks: Incomplete
    kept_var_idx: Incomplete
    def __init__(self, xla_executable, name, backend, in_handler: InputsHandler, out_handler: ResultsHandler, unordered_effects: list[core.Effect], ordered_effects: list[core.Effect], keepalive: Any, has_host_callbacks: bool, kept_var_idx: set[int]) -> None: ...
    def __call__(self, *args): ...

xla_pmap_p: Incomplete
xla_pmap: Incomplete

def xla_call_jvp_update_params(params, nz_tangents): ...
def axis_groups(axis_env: sharding_impls.AxisEnv, name) -> tuple[tuple[int, ...]]: ...
def tile_aval_nd(axis_sizes, in_axes: ArrayMapping, aval): ...
def untile_aval_nd(axis_sizes, out_axes: ArrayMapping, aval): ...
def mesh_local_to_global(mesh, axes: ArrayMapping, aval): ...
def mesh_global_to_local(mesh, axes: ArrayMapping, aval): ...

class SPMDBatchTrace(batching.BatchTrace):
    def get_axis_primitive_batcher(self, primitive, frame): ...

spmd_primitive_batchers: dict[core.Primitive, Callable]

def vtile_by_mesh(fun: lu.WrappedFun, mesh: Mesh, in_axes: Sequence[ArrayMapping], out_axes: Sequence[ArrayMapping]): ...

full_to_shard_p: Incomplete

def manual_proto(aval: core.ShapedArray, manual_axes_set: frozenset[sharding_impls.MeshAxisName], mesh: Mesh):
    """Create an OpSharding proto that declares all mesh axes from `axes` as manual
  and all others as replicated.
  """

shard_to_full_p: Incomplete

def vtile_manual(manual_axes: frozenset[sharding_impls.MeshAxisName], mesh: Mesh, in_axes: Sequence[ArrayMapping], out_axes: Sequence[ArrayMapping], *args): ...

@dataclasses.dataclass(frozen=True)
class TileVectorize: ...

@dataclasses.dataclass(frozen=True)
class TileManual:
    manual_axes: frozenset[sharding_impls.MeshAxisName]
    def __init__(self, manual_axes) -> None: ...
TilingMethod = TileVectorize | TileManual

def check_if_any_auto(shardings: Iterable[sharding_impls.XLACompatibleSharding | AUTO | UnspecifiedValue]) -> bool: ...

class MismatchType(enum.Enum):
    ARG_SHARDING: int
    OUT_SHARDING: int
    SHARDING_INSIDE_COMPUTATION: int
    CONTEXT_DEVICES: int
    IN_SHARDING: int

@dataclasses.dataclass
class DeviceAssignmentMismatch:
    da: Sequence[xc.Device]
    m_type: MismatchType
    source_info: dispatch.SourceInfo | None
    @property
    def device_ids(self) -> Sequence[int]: ...
    @property
    def platform(self) -> str: ...
    @property
    def source_info_str(self): ...
    def m_type_str(self, api_name): ...
    def __init__(self, da, m_type, source_info) -> None: ...

class DeviceAssignmentMismatchError(Exception): ...

ShardingInfo: Incomplete

class _thread_local_decorator(threading.local):
    fn: Incomplete
    def __init__(self, fn) -> None: ...
    def __call__(self, *args, **kwargs): ...

MaybeSharding: Incomplete

def cache_wrap(fn): ...
def prune_unused_inputs(jaxpr: core.Jaxpr) -> tuple[core.Jaxpr, set[int], set[int]]: ...

@dataclasses.dataclass(frozen=True)
class SemanticallyEqualShardings:
    shardings: tuple[sharding_impls.GSPMDSharding | UnspecifiedValue, ...]
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __init__(self, shardings) -> None: ...

@dataclasses.dataclass(frozen=True)
class _DeviceAssignment:
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: Any) -> Any: ...
    def __iter__(self) -> Iterator[xc.Device]: ...
    @cached_property
    def is_fully_addressable(self) -> bool: ...
    @cached_property
    def addressable_device_list(self) -> _DeviceAssignment: ...
    @cached_property
    def memory_kinds(self) -> tuple[str, ...]: ...
    @cached_property
    def default_memory_kind(self) -> str | None: ...
    def __init__(self, _device_assignment) -> None: ...

def jaxpr_transfer_mem_kinds(jaxpr: core.Jaxpr) -> Iterator[sharding_impls.TransferToMemoryKind]: ...
def are_all_shardings_default_mem_kind(da_object, shardings): ...
def lower_sharding_computation(fun_or_jaxpr: lu.WrappedFun | core.ClosedJaxpr, api_name: str, fun_name: str, in_shardings: Sequence[MaybeSharding], out_shardings: Sequence[MaybeSharding] | UnspecifiedValue, donated_invars: Sequence[bool], global_in_avals: Sequence[core.ShapedArray], *, keep_unused: bool, inline: bool, devices_from_context: Sequence[xc.Device] | None = None, lowering_parameters: mlir.LoweringParameters) -> MeshComputation:
    """Lowers a computation to XLA. It can take arbitrary shardings as input.

  The caller of this code can pass in a singleton UNSPECIFIED because the
  number of out_avals might not be known at that time and
  lower_sharding_computation calculates the number of out_avals so it can apply
  the singleton UNSPECIFIED to all out_avals.
  """
def lower_mesh_computation(fun_or_jaxpr: lu.WrappedFun | core.ClosedJaxpr, api_name: str, fun_name: str, mesh: Mesh, in_shardings: Sequence[sharding_impls.NamedSharding | AUTO], out_shardings: Sequence[sharding_impls.NamedSharding | AUTO | UnspecifiedValue], donated_invars: Sequence[bool], spmd_lowering: bool, global_in_avals: Sequence[core.ShapedArray], tiling_method: TilingMethod | None, lowering_parameters: mlir.LoweringParameters) -> MeshComputation: ...

class MeshComputation(stages.XlaLowering):
    compile_args: Incomplete
    def __init__(self, name: str, hlo: ir.Module | None, donated_invars: Sequence[bool], **compile_args) -> None: ...
    def stablehlo(self) -> ir.Module: ...
    def compile(self, compiler_options: Incomplete | None = None) -> MeshExecutable: ...
    def cost_analysis(self) -> dict[str, float]: ...

def get_gspmd_shardings_from_executable(xla_executable, device_assignment: Sequence[xc.Device], num_out_avals: int, num_ordered_effects: int, all_default_mem_kind: bool) -> Sequence[sharding_impls.XLACompatibleSharding]: ...
def maybe_get_orig_out_sharding(in_shardings, out_shardings, are_out_shardings_from_xla, in_avals, out_avals): ...

@dataclasses.dataclass
class UnloadedMeshExecutable:
    xla_executable: Any
    device_assignment: _DeviceAssignment | Sequence[xc.Device]
    backend: xb.XlaBackend
    input_avals: Sequence[ShapedArray]
    input_shardings: Sequence[sharding_impls.XLACompatibleSharding]
    output_avals: Sequence[ShapedArray]
    output_shardings: Sequence[sharding_impls.XLACompatibleSharding]
    committed: bool
    are_out_shardings_from_xla: Sequence[bool]
    name: str
    unordered_effects: list[core.Effect]
    ordered_effects: list[core.Effect]
    keepalive: Sequence[Any]
    host_callbacks: Sequence[Any]
    kept_var_idx: set[int]
    auto_spmd_lowering: bool
    jaxpr_debug_info: core.JaxprDebugInfo | None
    def build_unsafe_call(self): ...
    def load(self) -> MeshExecutable: ...
    @staticmethod
    def from_hlo(name: str, hlo: ir.Module, global_in_avals: Sequence[ShapedArray], global_out_avals: Sequence[ShapedArray], in_shardings: Sequence[sharding_impls.XLACompatibleSharding | AUTO], out_shardings: Sequence[sharding_impls.XLACompatibleSharding | AUTO | UnspecifiedValue], spmd_lowering: bool, tuple_args: bool, auto_spmd_lowering: bool, unordered_effects: list[core.Effect], ordered_effects: list[core.Effect], host_callbacks: list[Any], keepalive: Any, kept_var_idx: set[int], backend: xb.XlaBackend, device_assignment: _DeviceAssignment | Sequence[xc.Device], committed: bool, pmap_nreps: int = 1, jaxpr_debug_info: core.JaxprDebugInfo | None = None, shape_poly_state: mlir.ShapePolyLoweringState | None = None, all_default_mem_kind: bool = True, compiler_options: Incomplete | None = None) -> MeshExecutable: ...
    def __init__(self, xla_executable, device_assignment, backend, input_avals, input_shardings, output_avals, output_shardings, committed, are_out_shardings_from_xla, name, unordered_effects, ordered_effects, keepalive, host_callbacks, kept_var_idx, auto_spmd_lowering, jaxpr_debug_info) -> None: ...

class MeshExecutableFastpathData(NamedTuple):
    xla_executable: xc.LoadedExecutable
    out_pytree_def: Any
    in_shardings: Sequence[sharding_impls.XLACompatibleSharding]
    out_shardings: Sequence[sharding_impls.XLACompatibleSharding]
    out_avals: Sequence[ShapedArray]
    out_committed: Sequence[bool]
    kept_var_bitvec: Iterable[bool]

def reflatten_outputs_for_dispatch(out_tree, out_flat): ...

class MeshExecutable(stages.XlaExecutable):
    xla_executable: Incomplete
    build_unsafe_call: Incomplete
    in_avals: Incomplete
    def __init__(self, xla_executable, build_unsafe_call, in_avals, in_shardings, out_shardings, auto_spmd_lowering, kept_var_idx, jaxpr_debug_info: Incomplete | None = None, unloaded_executable: Incomplete | None = None) -> None: ...
    @property
    def unsafe_call(self) -> Callable[..., Any]: ...
    def xla_extension_executable(self): ...
    def call(self, *args): ...
    def input_shardings(self) -> Sequence[sharding_impls.XLACompatibleSharding]: ...
    def output_shardings(self) -> Sequence[sharding_impls.XLACompatibleSharding]: ...
    def create_cpp_call(self, no_kwargs, in_tree, out_tree): ...
    def create_cpp_call_for_apply_primitive(self, out_tree): ...

def check_arg_avals_for_call(ref_avals, arg_avals, jaxpr_debug_info: core.JaxprDebugInfo | None = None): ...
def create_mesh_pspec_sharding(mesh: Mesh, pspec: PartitionSpec | None, parsed_pspec: Incomplete | None = None, memory_kind: str | None = None) -> sharding_impls.NamedSharding: ...
def check_device_backend_on_shardings(shardings) -> bool: ...
def check_gda_or_array_xla_sharding_match(args, in_xla_shardings: Sequence[sharding_impls.XLACompatibleSharding], jaxpr_debug_info: core.JaxprDebugInfo | None) -> None: ...
def get_array_mapping(pspec: PartitionSpec) -> ArrayMappingOrAutoOrUnspecified: ...

custom_resource_typing_rules: dict[core.Primitive, Callable]

def resource_typecheck(jaxpr, resource_env, axis_resources, what_jaxpr_thunk): ...
def mesh_sharding_specs(axis_sizes, axis_names, allow_uneven_axes: bool = False): ...
def maybe_extend_axis_env(*args, **kwargs) -> Generator[None, None, None]: ...
def device_put(x, devices: Sequence[xc.ArrayImpl], replicate: bool = False) -> list[xc.ArrayImpl]:
    """Call device_put on a sequence of devices and return a flat sequence of buffers."""
