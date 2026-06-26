import dataclasses
import enum
import functools
import numpy as np
from _typeshed import Incomplete
from collections import OrderedDict
from collections.abc import Mapping, Sequence
from jax._src import mesh as mesh_lib, sharding as sharding, sharding_specs as sharding_specs, tree_util as tree_util, util as util, xla_bridge as xla_bridge
from jax._src.lib import xla_client as xc, xla_extension_version as xla_extension_version
from jax._src.op_shardings import are_op_shardings_equal as are_op_shardings_equal, get_num_ways_dim_sharded as get_num_ways_dim_sharded, is_op_sharding_replicated as is_op_sharding_replicated, op_sharding_to_indices as op_sharding_to_indices
from jax._src.partition_spec import PartitionSpec as PartitionSpec
from jax._src.util import safe_map as safe_map, safe_zip as safe_zip, use_cpp_class as use_cpp_class, use_cpp_method as use_cpp_method
from typing import Any, NamedTuple

Shape = tuple[int, ...]
Device: Incomplete
Index = tuple[slice, ...]
XLADeviceAssignment = tuple[Device, ...]

@dataclasses.dataclass(frozen=True)
class TransferToMemoryKind:
    memory_kind: str
    def __init__(self, memory_kind) -> None: ...

def common_devices_indices_map(s, global_shape: Shape) -> Mapping[Device, Index]: ...

class XLACompatibleSharding(sharding.Sharding):
    """A :class:`Sharding` that describes shardings expressible to XLA.

  Subclasses of :class:`XLACompatibleSharding` work with
  all JAX APIs and transformations that use XLA.
  """
    def devices_indices_map(self, global_shape: Shape) -> Mapping[Device, Index]: ...
    def shard_shape(self, global_shape: Shape) -> Shape: ...
    def is_equivalent_to(self, other: XLACompatibleSharding, ndim: int) -> bool: ...

def hashed_index(x) -> int: ...
def device_replica_id_map(sharding, global_shape: Shape) -> Mapping[Device, int]: ...
def named_sharding_to_xla_hlo_sharding(self, num_dimensions: int) -> xc.HloSharding: ...

class NamedSharding(XLACompatibleSharding):
    """A :class:`NamedSharding` expresses sharding using named axes.

  A :class:`NamedSharding` is a pair of a :class:`Mesh` of devices and
  :class:`PartitionSpec` which describes how to shard an array across that
  mesh.

  A :class:`Mesh` is a multidimensional NumPy array of JAX devices,
  where each axis of the mesh has a name, e.g. ``'x'`` or ``'y'``.

  A :class:`PartitionSpec` is a tuple, whose elements can be a ``None``,
  a mesh axis, or a tuple of mesh axes. Each element describes how an input
  dimension is partitioned across zero or more mesh dimensions. For example,
  ``PartitionSpec('x', 'y')`` says that the first dimension of data
  is sharded across ``x`` axis of the mesh, and the second dimension is sharded
  across ``y`` axis of the mesh.

  The Distributed arrays and automatic parallelization
  (https://jax.readthedocs.io/en/latest/notebooks/Distributed_arrays_and_automatic_parallelization.html#namedsharding-gives-a-way-to-express-shardings-with-names)
  tutorial has more details and diagrams that explain how
  :class:`Mesh` and :class:`PartitionSpec` are used.

  Args:
    mesh: A :class:`jax.sharding.Mesh` object.
    spec: A :class:`jax.sharding.PartitionSpec` object.

  Example:

    >>> from jax.sharding import Mesh
    >>> from jax.sharding import PartitionSpec as P
    >>> mesh = Mesh(np.array(jax.devices()).reshape(2, 4), ('x', 'y'))
    >>> spec = P('x', 'y')
    >>> named_sharding = jax.sharding.NamedSharding(mesh, spec)
  """
    mesh: mesh_lib.Mesh
    spec: PartitionSpec
    def __init__(self, mesh: mesh_lib.Mesh, spec: PartitionSpec, *, memory_kind: str | None = None, _parsed_pspec: Incomplete | None = None, _manual_axes=...) -> None: ...
    def __reduce__(self): ...
    @property
    def memory_kind(self) -> str | None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def is_compatible_aval(self, aval_shape: Shape): ...
    @property
    def device_set(self) -> set[Device]: ...
    @property
    def is_fully_addressable(self) -> bool: ...
    @property
    def addressable_devices(self) -> set[Device]: ...
    @functools.cached_property
    def is_fully_replicated(self) -> bool: ...
    def with_memory_kind(self, kind: str) -> NamedSharding: ...

def get_replicated_hlo_sharding(): ...

class SingleDeviceSharding(XLACompatibleSharding):
    """A :class:`Sharding` that places its data on a single device.

  Args:
    device: A single :py:class:`Device`.

  Example:

    >>> single_device_sharding = jax.sharding.SingleDeviceSharding(
    ...     jax.devices()[0])
  """
    def __init__(self, device: Device, *, memory_kind: str | None = None) -> None: ...
    def __reduce__(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    @property
    def device_set(self) -> set[Device]: ...
    @property
    def memory_kind(self) -> str | None: ...
    def with_memory_kind(self, kind: str) -> SingleDeviceSharding: ...
    def devices_indices_map(self, global_shape: Shape) -> Mapping[Device, Index]: ...
    @property
    def is_fully_replicated(self) -> bool: ...
    @property
    def is_fully_addressable(self) -> bool: ...

def pmap_sharding_devices_indices_map(self, global_shape: Shape) -> Mapping[Device, Index]: ...

class PmapSharding(XLACompatibleSharding):
    """Describes a sharding used by :func:`jax.pmap`."""
    devices: np.ndarray
    sharding_spec: sharding_specs.ShardingSpec
    def __init__(self, devices: Sequence[Device] | np.ndarray, sharding_spec: sharding_specs.ShardingSpec) -> None: ...
    def __reduce__(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def is_equivalent_to(self, other: PmapSharding, ndim: int) -> bool: ...
    @classmethod
    def default(cls, shape: Shape, sharded_dim: int = 0, devices: Sequence[xc.Device] | None = None) -> PmapSharding:
        """Creates a :class:`PmapSharding` which matches the default placement
    used by :func:`jax.pmap`.

    Args:
      shape: The shape of the input array.
      sharded_dim: Dimension the input array is sharded on. Defaults to 0.
      devices: Optional sequence of devices to use. If omitted, the implicit
      device order used by pmap is used, which is the order of
        :func:`jax.local_devices`.
    """
    @functools.cached_property
    def device_set(self) -> set[Device]: ...
    def devices_indices_map(self, global_shape: Shape) -> Mapping[Device, Index]: ...
    @property
    def memory_kind(self) -> str | None: ...
    def with_memory_kind(self, kind: str): ...
    @functools.cached_property
    def is_fully_replicated(self) -> bool: ...
    @functools.cached_property
    def is_fully_addressable(self) -> bool: ...
    def shard_shape(self, global_shape: Shape) -> Shape: ...

class PositionalSharding(XLACompatibleSharding):
    def __init__(self, devices: Sequence[xc.Device] | np.ndarray, *, memory_kind: str | None = None) -> None: ...
    @property
    def shape(self): ...
    @property
    def ndim(self): ...
    def reshape(self, *shape) -> PositionalSharding: ...
    def transpose(self, *axes) -> PositionalSharding: ...
    T: Incomplete
    def replicate(self, axis: Incomplete | None = None, keepdims: bool = True) -> PositionalSharding: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    @functools.cached_property
    def device_set(self) -> set[xc.Device]: ...
    @property
    def memory_kind(self) -> str | None: ...
    def with_memory_kind(self, kind: str) -> PositionalSharding: ...
    @functools.cached_property
    def is_fully_replicated(self) -> bool: ...
    @functools.cached_property
    def is_fully_addressable(self) -> bool: ...

class DeviceIdSet:
    def __init__(self, name, *ids) -> None: ...
    def __iter__(self): ...
    def __add__(self, other) -> DeviceIdSet: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...

def gspmd_sharding_devices_indices_map(self, global_shape: Shape) -> Mapping[Device, Index]: ...

class GSPMDSharding(XLACompatibleSharding):
    def __init__(self, devices: Sequence[Device], op_sharding: xc.OpSharding | xc.HloSharding, *, memory_kind: str | None = None) -> None: ...
    def __reduce__(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def is_compatible_aval(self, aval_shape: Shape): ...
    @functools.cached_property
    def device_set(self) -> set[Device]: ...
    @property
    def memory_kind(self) -> str | None: ...
    def with_memory_kind(self, kind: str) -> GSPMDSharding: ...
    def devices_indices_map(self, global_shape: Shape) -> Mapping[Device, Index]: ...
    @functools.cached_property
    def is_fully_replicated(self) -> bool: ...
    @functools.cached_property
    def is_fully_addressable(self) -> bool: ...
    @classmethod
    def get_replicated(cls, device_assignment, *, memory_kind: str | None = None): ...

class AUTO:
    mesh: Incomplete
    def __init__(self, mesh: mesh_lib.Mesh) -> None: ...

def is_auto(x): ...

class UnspecifiedValue: ...

UNSPECIFIED: Incomplete

def is_unspecified(x): ...
def is_unspecified_or_auto(x): ...
MeshAxisName = Any
ArrayMapping = OrderedDict[MeshAxisName, int]
ArrayMappingOrAutoOrUnspecified = ArrayMapping | AUTO | UnspecifiedValue

def array_mapping_to_axis_resources(array_mapping: ArrayMapping): ...
def get_array_mapping(axis_resources: ParsedPartitionSpec | AUTO | UnspecifiedValue) -> ArrayMappingOrAutoOrUnspecified: ...

get_single_pspec: Incomplete

class SpecSync(enum.IntEnum):
    """Encodes how much out of sync the real value of partitions is compared to the user specified one.

  We use this to make sure we don't show garbage modified values while claiming
  that the users have specified them like that.
  """
    OUT_OF_SYNC: int
    DIM_PERMUTE: int
    IN_SYNC: int

class ParsedPartitionSpec:
    unsafe_user_spec: Incomplete
    partitions: Incomplete
    sync: Incomplete
    def __init__(self, user_spec, partitions, sync=...) -> None: ...
    @property
    def user_spec(self): ...
    def get_partition_spec(self) -> PartitionSpec: ...
    def unsynced_user_spec(self, min_sync): ...
    def insert_axis_partitions(self, dim, val): ...
    @classmethod
    def from_user_input(cls, entry, arg_name, allow_unconstrained_dims: bool = False): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...
    def __iter__(self): ...

class CanonicalizedParsedPartitionSpec(ParsedPartitionSpec):
    """ParsedPartitionSpecs that are canonicalized.

  ParsedPartitionSpecs may contain trailing empty tuples, that make them
  semantically different in general, and yet in some situations we prefer
  to regard them as equivalent. For example, partitions of () and ((),)
  cannot be always considered equivalent, since the first one is a valid
  spec for a scalar value, while the second is not! However, when either of
  those are applied to a 2D array, they both mean that the array is fully
  replicated.

  So CanonicalizedParsedPartitionSpecs removes the trailing empty tuples from
  partitions.
  """
    def __init__(self, parsed_pspec: ParsedPartitionSpec) -> None: ...

def check_all_or_none_unspecified(axis_resources, name): ...
def prepare_axis_resources(axis_resources, arg_name, allow_unconstrained_dims: bool = False): ...

class AxisEnv(NamedTuple):
    """Represents a pmap mesh (only along the replica axes)."""
    nreps: int
    names: tuple[Any, ...]
    sizes: tuple[int, ...]

@dataclasses.dataclass(frozen=True)
class SPMDAxisContext:
    """A hardware axis context for parallel computations that use the GSPMD partitioner.

  This includes the mesh that will later by used to execute this computation,
  as well as a set of mesh axes that are currently (e.g. because the current lowering
  is invoked inside an xmap) lowered in the MANUAL sharding mode.
  """
    mesh: mesh_lib.Mesh
    manual_axes: frozenset[MeshAxisName] = ...
    @property
    def axis_env(self): ...
    @property
    def unsafe_axis_env(self): ...
    def extend_manual(self, axes: frozenset[MeshAxisName]) -> SPMDAxisContext: ...
    def __init__(self, mesh, manual_axes) -> None: ...

@dataclasses.dataclass(frozen=True)
class ReplicaAxisContext:
    """A hardware axis context for parallel computations that are partitioned by JAX.

  Unlike in the SPMDAxisContext, this means that JAX might need to emit calls to
  explicit collectives.
  """
    axis_env: AxisEnv
    def __init__(self, axis_env) -> None: ...

@dataclasses.dataclass(frozen=True)
class ShardingContext:
    """A hardware axis context for parallel computations that use the sharding
  interface.

  This context also uses the GSPMD partitioner.
  """
    device_assignment: Sequence[xc.Device]
    @property
    def axis_env(self): ...
    def __init__(self, device_assignment) -> None: ...

def strides_for_sizes(sizes):
    """Returns an array of strides for major-to-minor sizes."""
def unflatten_array(named_sizes, assignment):
    """Recovers the ordering of axis names based on a device assignment.

  The device assignments that this function can convert into axis orders
  are of the form::

    np.arange(np.prod(named_sizes.values())).transpose(...).flatten()

  for some transposition ``...``. This is satisfied by all OpSharding assignments
  generated from partition specs.

  Arguments:
    named_sizes: A dictionary mapping axis names to their sizes.
    assignment: A permutation of integers between 0 and the product of all
      named sizes.

  Returns:
    A major-to-minor list of axis names that corresponds to the given assignment.
  """
def unflatten_superdims(assignment):
    """Unflatten a list of dimension sizes and their strides that generates assignment.

  If this function succeeds for a given ``assignment``, then the following property
  should be satisfied::

    dims_with_strides = unflatten_superdims(assignment)
    base_array = np.arange(map(fst, sorted(dims_with_strides, key=snd, reverse=True)))
    assignment == base_array.transpose(argsort(dims_with_strides, key=snd, reverse=True)).flatten()

  That is, the returned dimensions list all sizes of the base array (with strides
  indicating their initial order). The order of dimensions in the list corresponds
  to the permutation that applied to the base array generates the assignment.
  """
def explode_superdims(sizes, dims):
    """Explode superdims to fit a known shape.

  The unflattening process might mistakenly generate too few too large dimensions.
  For example, ``unflatten_superdims(np.arange(n))`` always returns ``[(n, 1)]``.
  This function takes a list of such contiguous super-dimensions and splits them
  into smaller dimensions such that::

    set(map(fst, explode_superdims(sizes, dims))) == set(sizes)
  """
def parse_flatten_op_sharding(hlo_sharding: xc.OpSharding | xc.HloSharding, mesh: mesh_lib.Mesh) -> Sequence[ParsedPartitionSpec]: ...
