import enum
import functools
from _typeshed import Incomplete
from collections.abc import Sequence
from jax._src import abstract_arrays as abstract_arrays, api as api, api_util as api_util, basearray as basearray, core as core, dispatch as dispatch, dtypes as dtypes, profiler as profiler, tree_util as tree_util, xla_bridge as xla_bridge
from jax._src.config import config as config
from jax._src.interpreters import mlir as mlir, pxla as pxla, xla as xla
from jax._src.sharding import Sharding as Sharding
from jax._src.sharding_impls import PmapSharding as PmapSharding, SingleDeviceSharding as SingleDeviceSharding, XLACompatibleSharding as XLACompatibleSharding, device_replica_id_map as device_replica_id_map, hashed_index as hashed_index
from jax._src.typing import ArrayLike as ArrayLike
from jax._src.util import safe_zip as safe_zip, unzip3 as unzip3, use_cpp_class as use_cpp_class, use_cpp_method as use_cpp_method
from typing import Any, Callable

Shape = tuple[int, ...]
Device: Incomplete
Index = tuple[slice, ...]
PRNGKeyArrayImpl = Any

class Shard:
    """A single data shard of an Array.

  Attributes:
    device : Which device this shard resides on.
    index : The index into the global array of this shard.
    replica_id : Integer id indicating which replica of the global array this
      shard is part of. Always 0 for fully sharded data
      (i.e. when there’s only 1 replica).
    data : The data of this shard. None if ``device`` is non-local.
  """
    def __init__(self, device: Device, sharding: Sharding, global_shape: Shape, data: None | ArrayImpl | PRNGKeyArrayImpl = None) -> None: ...
    @functools.cached_property
    def index(self) -> Index: ...
    @functools.cached_property
    def replica_id(self) -> int: ...
    @property
    def device(self): ...
    @property
    def data(self): ...

class ArrayImpl(basearray.Array):
    aval: core.ShapedArray
    def __init__(self, aval: core.ShapedArray, sharding: Sharding, arrays: Sequence[ArrayImpl], committed: bool, _skip_checks: bool = False) -> None: ...
    @property
    def shape(self) -> Shape: ...
    @property
    def dtype(self): ...
    @property
    def ndim(self): ...
    @property
    def size(self): ...
    @property
    def sharding(self): ...
    @property
    def weak_type(self): ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __float__(self) -> float: ...
    def __int__(self) -> int: ...
    def __complex__(self) -> complex: ...
    def __hex__(self): ...
    def __oct__(self): ...
    def __index__(self) -> int: ...
    def tobytes(self, order: str = 'C'): ...
    def tolist(self): ...
    def __format__(self, format_spec) -> str: ...
    def __getitem__(self, idx): ...
    def __iter__(self): ...
    @property
    def is_fully_replicated(self) -> bool: ...
    @property
    def is_fully_addressable(self) -> bool:
        '''Is this Array fully addressable?

    A jax.Array is fully addressable if the current process can address all of
    the devices named in the :class:`Sharding`. ``is_fully_addressable`` is
    equivalent to "is_local" in multi-process JAX.

    Note that fully replicated is not equal to fully addressable i.e.
    a jax.Array which is fully replicated can span across multiple hosts and is
    not fully addressable.
    '''
    def __array__(self, dtype: Incomplete | None = None, context: Incomplete | None = None): ...
    def __dlpack__(self, *, stream: int | Any | None = None): ...
    def __dlpack_device__(self) -> tuple[enum.Enum, int]: ...
    def __reduce__(self): ...
    def unsafe_buffer_pointer(self): ...
    @property
    def __cuda_array_interface__(self): ...
    def on_device_size_in_bytes(self):
        """Returns the total global on-device size of the array in bytes."""
    def device(self) -> Device: ...
    def devices(self) -> set[Device]: ...
    @property
    def device_buffer(self) -> ArrayImpl: ...
    @property
    def device_buffers(self) -> Sequence[ArrayImpl]: ...
    def addressable_data(self, index: int) -> ArrayImpl: ...
    @functools.cached_property
    def addressable_shards(self) -> Sequence[Shard]: ...
    @property
    def global_shards(self) -> Sequence[Shard]:
        """Returns list of all `Shard`s of the Array across all devices.

    The result includes shards that are not addressable by the current process.
    If a `Shard` is not addressable, then its `data` will be `None`.
    """
    def delete(self) -> None: ...
    def is_deleted(self): ...
    def block_until_ready(self): ...
    def copy_to_host_async(self) -> None: ...

def make_array_from_callback(shape: Shape, sharding: Sharding, data_callback: Callable[[Index | None], ArrayLike]) -> ArrayImpl:
    """Returns a ``jax.Array`` via data fetched from ``data_callback``.

  ``data_callback`` is used to fetch the data for each addressable shard of the
  returned ``jax.Array``.

  Args:
    shape : Shape of the ``jax.Array``.
    sharding: A ``Sharding`` instance which describes how the ``jax.Array`` is
      laid out across devices.
    data_callback : Callback that takes indices into the global array value as
      input and returns the corresponding data of the global array value.
      The data can be returned as any array-like object, e.g. a ``numpy.ndarray``.

  Returns:
    A ``jax.Array`` via data fetched from ``data_callback``.

  Example:

    >>> import math
    >>> from jax.sharding import Mesh
    >>> from jax.sharding import PartitionSpec as P
    >>> import numpy as np
    ...
    >>> input_shape = (8, 8)
    >>> global_input_data = np.arange(math.prod(input_shape)).reshape(input_shape)
    >>> global_mesh = Mesh(np.array(jax.devices()).reshape(2, 4), ('x', 'y'))
    >>> inp_sharding = jax.sharding.NamedSharding(global_mesh, P('x', 'y'))
    ...
    >>> def cb(index):
    ...  return global_input_data[index]
    ...
    >>> arr = jax.make_array_from_callback(input_shape, inp_sharding, cb)
    >>> arr.addressable_data(0).shape
    (4, 2)
  """
def make_array_from_single_device_arrays(shape: Shape, sharding: Sharding, arrays: Sequence[basearray.Array]) -> ArrayImpl:
    """Returns a ``jax.Array`` from a sequence of ``jax.Array``\\s on a single device.

  You can use this function if you have already ``jax.device_put`` the value on
  a single device and want to create a global Array. The smaller ``jax.Array``\\s should be
  addressable and belong to the current process.

  Args:
    shape : Shape of the ``jax.Array``.
    sharding: A ``Sharding`` instance which describes how the ``jax.Array`` is
      laid out across devices.
    arrays: Sequence of ``jax.Array``\\s that are on a single device.

  Returns:
    A ``jax.Array`` from a sequence of ``jax.Array``\\s on a single device.

  Example:

    >>> import math
    >>> from jax.sharding import Mesh
    >>> from jax.sharding import PartitionSpec as P
    >>> import numpy as np
    ...
    >>> global_shape = (8, 8)
    >>> global_mesh = Mesh(np.array(jax.devices()).reshape(2, 4), ('x', 'y'))
    >>> sharding = jax.sharding.NamedSharding(global_mesh, P('x', 'y'))
    >>> inp_data = np.arange(math.prod(global_shape)).reshape(global_shape)
    ...
    >>> arrays = [
    ...     jax.device_put(inp_data[index], d)
    ...     for d, index in sharding.addressable_devices_indices_map(global_shape).items()]
    ...
    >>> arr = jax.make_array_from_single_device_arrays(global_shape, sharding, arrays)
    >>> arr.addressable_data(0).shape
    (4, 2)

    In multi-process case, if the input is process local and data parallel
    i.e. each process receives a different part of the data, then you can use
    `make_array_from_single_device_arrays` to create a global jax.Array

    >>> local_shape = (8, 2)
    >>> global_shape = (jax.process_count() * local_shape[0], ) + local_shape[1:]
    >>> local_array = np.arange(math.prod(local_shape)).reshape(local_shape)
    >>> arrays = jax.device_put(
    ...   np.split(local_array, len(global_mesh.local_devices), axis = 0), global_mesh.local_devices)
    >>> sharding = jax.sharding.NamedSharding(global_mesh, P(('x', 'y'), ))
    >>> arr = jax.make_array_from_single_device_arrays(global_shape, sharding, arrays)
    >>> arr.addressable_data(0).shape
    (1, 2)
  """
def as_slice_indices(arr: Any, idx: Index) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    """Returns start_indices, limit_indices, removed_dims"""
def shard_device_array(x, devices, indices, sharding): ...
def shard_sharded_device_array_slow_path(x, devices, indices, sharding): ...
